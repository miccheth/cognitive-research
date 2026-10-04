# /// script
# requires-python = ">=3.13"
# dependencies = ["numpy>=2.0", "openai>=1.0", "python-dotenv>=1.0"]
# ///
"""Esperimento: da embedding Qwen a ipervettori binari per la ricerca.

COSA ABBIAMO FATTO
Abbiamo preso testi fissi, generato gli embedding float con Qwen3-Embedding-8B
(4096 dimensioni) e li abbiamo trasformati in ipervettori binari con una
proiezione casuale h = sign(Rx) da 10000 bit. Per ogni coppia di testi abbiamo
confrontato la cosine tra i float e la similarita' binaria 1 - Hamming/bit, e
misurato con Pearson e Spearman quanto la relazione spaziale sopravvive alla
binarizzazione (Spearman circa 0.994, Pearson circa 0.983 sui 22 pair).

IL PROBLEMA RISCONTRATO
L'ordine delle similarita' regge, ma la scala si comprime. Il difetto piu'
grave sono le coppie deboli: testi su argomenti diversi (cosine circa 0.3)
restano a una similarita' binaria di circa 0.6, appiccicati al pavimento. Il
pavimento nasce dal segno, non dal numero di bit: due vettori ortogonali danno
0.5 per geometria della proiezione casuale, e piu' bit non lo alzano. Centrare
prima di proiettare lo abbassa (0.60 -> 0.43) ma non migliora Pearson/Spearman,
quindi non risolve. Con soli binari non possiamo usare soglie assolute di
similarita': il pavimento falsa ogni confronto con la cosine.

LA PROPOSTA
Usare un approccio ibrido. L'indice binario fa da filtro grezzo: data una query,
si calcola l'Hamming contro tutti i documenti e si prendono i primi K candidati.
Cosi' il binario fa solo il lavoro che sa fare bene, cioe' l'ordinamento, e la
scala assoluta smette di contare. Il reranking finale usa i vettori float FP32,
che riordinano i K candidati con la precisione piena. La memoria dei float resta
necessaria per il reranking: il binario aggiunge un indice veloce, non sostituisce
i vettori.

DA VERIFICARE
Dobbiamo capire se questo approccio ibrido conviene, cioe' se il filtro binario
porta i documenti giusti nei primi K senza scartarli, e se il guadagno di velocita'
vale l'indice binario in piu'. Se conviene, bisogna trovare il miglior compromesso
di dimensione: il minimo numero di bit dell'ipervettore che tiene il recall alto,
e la minima dimensione dei vettori float che tiene la precisione del reranking.
"""

import os

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

# --- Configurazione ---

# Coppie usate per stimare quanta relazione spaziale resta.
# Similarita' forte: stesse parole, piccolo cambio.
# Similarita' media: stesso tema, soggetto o frase diversa.
# Similarita' debole: argomenti distinti.
TEXT_PAIRS = [
    # Forte.
    ("Il gatto dorme sul divano.", "Un felino riposa sul sofa'."),
    ("Il gatto dorme sul divano.", "Il gatto non dorme sul divano."),
    ("La ricetta della pasta al pomodoro.", "La ricetta della pasta al pomodoro e' semplice."),
    ("La borsa ha chiuso in ribasso.", "Il mercato azionario e' in calo."),
    ("Il treno per Milano parte alle otto.", "Il treno per Milano parte alle nove."),
    ("Domani piove su tutta la regione.", "Domani piovera' su tutta la regione."),
    ("Il libro e' sul tavolo della cucina.", "Il libro si trova sul tavolo in cucina."),
    ("Mario guida la macchina rossa.", "Mario guida la macchina di colore rosso."),
    # Media.
    ("Il gatto dorme sul divano.", "Il cane dorme sul tappeto."),
    ("Il gatto dorme sul divano.", "Il gatto insegue un topo in giardino."),
    ("Domani piove su tutta la regione.", "Il clima sta cambiando in tutto il mondo."),
    ("La borsa ha chiuso in ribasso.", "Le azioni della banca sono salite molto."),
    ("La ricetta della pasta al pomodoro.", "Il ristorante serve una cena di pesce."),
    ("Il treno per Milano parte alle otto.", "L'aereo per Roma decolla a mezzogiorno."),
    ("Il libro e' sul tavolo della cucina.", "La rivista e' sul tavolino del salotto."),
    # Debole.
    ("Il gatto dorme sul divano.", "Il prezzo del petrolio e' aumentato oggi."),
    ("Domani piove su tutta la regione.", "L'orologio meccanico ha bisogno di manutenzione."),
    ("La borsa ha chiuso in ribasso.", "Il gatto insegue un topo in giardino."),
    ("La ricetta della pasta al pomodoro.", "Il treno per Milano parte alle otto."),
    ("Il libro e' sul tavolo della cucina.", "L'azienda assume dieci ingegneri quest'anno."),
    ("Mario guida la macchina rossa.", "La stella alpina cresce ad alta quota."),
    ("Le api impollinano i fiori del prato.", "Il mese scorso sono andato in montagna."),
]

MODEL = "qwen3-embedding-8b"
BASE_URL = "https://api.scaleway.ai/v1"
FLOAT_DIMENSION = 4096
HD_DIMENSION = 10000
SEED = 42


def embed(texts):
    """Genera gli embedding float con Qwen tramite Scaleway.

    Args:
        texts: Testi da trasformare in vettori.
    Returns:
        Matrice (n_testi, FLOAT_DIMENSION), una riga per testo.
    Raises:
        SystemExit: Se l'API non restituisce FLOAT_DIMENSION dimensioni.
    """

    load_dotenv()
    client = OpenAI(base_url=BASE_URL, api_key=os.environ["SCW_SECRET_KEY"])
    response = client.embeddings.create(model=MODEL, input=texts, encoding_format="float")
    ordered = sorted(response.data, key=lambda item: item.index)
    vectors = np.array([item.embedding for item in ordered], dtype=np.float64)
    if vectors.shape[1] != FLOAT_DIMENSION:
        raise SystemExit(f"Attesi {FLOAT_DIMENSION} dimensioni float, ricevute {vectors.shape[1]}.")
    return vectors


def center(vectors):
    """Sottrae la media del corpus da ogni vettore.

    Toglie la componente comune a tutti i testi, cosi' i vettori esprimono solo
    cio' che li distingue. Le coppie non correlate si allontanano dal pavimento
    della proiezione casuale intorno a 0.5.

    Args:
        vectors: Matrice con un vettore per riga.
    Returns:
        La stessa matrice con media zero per colonna.
    """

    return vectors - vectors.mean(axis=0, keepdims=True)


def float_to_hypervector(input_vector, hd_dimension=HD_DIMENSION, seed=SEED):
    """Trasforma un vettore di float in un ipervettore binario.

    Proiezione casuale con matrice gaussiana fissa, poi segno.

    Args:
        input_vector: Vettore float di partenza.
        hd_dimension: Numero di bit dell'ipervettore.
        seed: Seed della matrice di proiezione, per rendere la trasformazione
            riproducibile e condivisa tra tutti i vettori.
    Returns:
        Vettore binario di hd_dimension elementi, valori 0 o 1.
    """

    input_vector = np.array(input_vector, dtype=np.float64)
    np.random.seed(seed)
    projection_matrix = np.random.randn(hd_dimension, len(input_vector))
    projected = projection_matrix @ input_vector
    return (projected >= 0).astype(np.uint8)


def cosine_similarity(a, b):
    """Calcola la cosine similarity tra due vettori float.

    Args:
        a: Primo vettore.
        b: Secondo vettore, stessa lunghezza del primo.
    Returns:
        La cosine in [-1, 1].
    """

    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def hamming_similarity(a_bin, b_bin):
    """Calcola la similarita' binaria tra due ipervettori.

    Args:
        a_bin: Primo ipervettore binario.
        b_bin: Secondo ipervettore, stessa lunghezza del primo.
    Returns:
        La similarita' 1 - Hamming / dimensione, in [0, 1]; 1 = bit identici.
    """

    return float(1.0 - np.mean(a_bin != b_bin))


def pearson(x, y):
    """Calcola la correlazione di Pearson tra due serie.

    Args:
        x: Prima serie di valori.
        y: Seconda serie, stessa lunghezza della prima.
    Returns:
        La correlazione in [-1, 1].
    """

    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    return float(np.corrcoef(x, y)[0, 1])


def spearman(x, y):
    """Calcola la correlazione di Spearman tra due serie.

    Pearson applicato ai ranghi: misura se l'ordine dei valori e' conservato,
    non se lo sono le distanze.

    Args:
        x: Prima serie di valori.
        y: Seconda serie, stessa lunghezza della prima.
    Returns:
        La correlazione dei ranghi in [-1, 1].
    """

    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    rank_x = np.argsort(np.argsort(x)).astype(np.float64)
    rank_y = np.argsort(np.argsort(y)).astype(np.float64)
    return pearson(rank_x, rank_y)


unique_texts = list(dict.fromkeys([text for pair in TEXT_PAIRS for text in pair]))
vectors = embed(unique_texts)
centered = center(vectors)
by_text = {text: vectors[index] for index, text in enumerate(unique_texts)}
by_text_centered = {text: centered[index] for index, text in enumerate(unique_texts)}

print(f"Dimensioni float: {FLOAT_DIMENSION}; bit ipervettore: {HD_DIMENSION}; coppie: {len(TEXT_PAIRS)}")
print(f"{'cosine':>9}{'binaria':>10}{'binaria centrata':>18}")

cosines, hammings, hammings_centered = [], [], []
for text_a, text_b in TEXT_PAIRS:
    cosine = cosine_similarity(by_text[text_a], by_text[text_b])
    binary = hamming_similarity(float_to_hypervector(by_text[text_a]), float_to_hypervector(by_text[text_b]))
    binary_centered = hamming_similarity(
        float_to_hypervector(by_text_centered[text_a]), float_to_hypervector(by_text_centered[text_b])
    )
    cosines.append(cosine)
    hammings.append(binary)
    hammings_centered.append(binary_centered)
    print(f"{cosine:>9.6f}{binary:>10.6f}{binary_centered:>18.6f}")

print(f"\nSenza centraggio  Pearson {pearson(cosines, hammings):.6f}  Spearman {spearman(cosines, hammings):.6f}")
print(f"Con centraggio    Pearson {pearson(cosines, hammings_centered):.6f}  Spearman {spearman(cosines, hammings_centered):.6f}")
print(f"Pavimento binario senza centraggio: {min(hammings):.6f}")
print(f"Pavimento binario con centraggio:   {min(hammings_centered):.6f}")
