# Aumento della veduta umana per amplificare il ragionamento

Questo documento descrive un'implementazione concreta di Intelligent Amplification — un sistema che **accumula conoscenza in una base simbolica deterministica**, eliminando le allucinazioni e permettendo inferenze verificabili. Il sistema non sostituisce il pensiero umano: fornisce spunti e connessioni per supportare decisioni che richiedono giudizio critico.

___
# L'Architettura in 3 Fasi

Il sistema funziona come una catena di montaggio che trasforma il linguaggio umano disordinato in calcoli matematici istantanei.

```
[Documenti] ──(1. Hyper-Extract)──> [Conoscenza Strutturata] ──(2. GraphBLAS)──> [Grafo Simbolico su GPU] ──(3. Inferenza)──> [Connessioni Verificate] ──> [Spunti per Decisione Umana]
```

___
## Fase 1: Acquisizione della Conoscenza (Hyper-Extract)

È la fase di **ingestione e strutturazione**. Prende i documenti (50 GB o 1 TB che siano) ed estrae conoscenza verificabile, eliminando il rumore.

**Come funziona:**
- Un template YAML definisce le regole (es. "cerca Persone, Aziende e i loro Ruoli nel tempo")
- Si utilizza la libreria [Hyper-Extract](https://github.com/yifanfeng97/hyper-extract)
- Un LLM locale (es. Qwen o Llama a 4/8 bit su framework vLLM) legge i testi e comprende il linguaggio umano
- Grazie alla funzionalità di *Structured Output*, estrae le informazioni formattandole in JSON rigidi

**Caratteristiche:**
- È la fase più lenta (richiede da poche ore a giorni a seconda delle GPU)
- Si esegue **una sola volta** per ogni documento
- L'LLM qui non genera conoscenza: la estrae dal testo sorgente

___
## Fase 2: Accumulo Simbolico (GraphBLAS)

È il cuore del sistema. Prende il JSON generato da Hyper-Extract e lo converte in una **base di conoscenza simbolica e deterministica**.

**Come funziona:**
- Ogni entità (es. "Elon Musk" o "SpaceX") riceve un indice numerico stabile
- Le relazioni vengono inserite in **matrici sparse giganti**
- Se Elon Musk (riga 0) è CEO di SpaceX (colonna 2), la cella `[0, 2]` contiene il metadato della relazione

**Caratteristiche:**
- GraphBLAS memorizza solo i collegamenti reali, ignorando i miliardi di "zeri" (relazioni inesistenti)
- Questo permette di comprimere l'intero grafo nella memoria della GPU
- La conoscenza è ora **simbolica, verificabile, priva di allucinazioni**

___
## Fase 3: Inferenza e Ragionamento (L'Hardware in Azione)

È il momento in cui il sistema **fa inferenza sulla conoscenza accumulata**. L'utente o un agente esplora il grafo con domande complesse (es. *"Trova le aziende collegate a SpaceX dopo 3 passaggi logici"*).

**Come funziona:**
- La query viene tradotta in un'operazione di **algebra lineare**
- Trovare connessioni a 3 passaggi significa fare una moltiplicazione di matrici sparse: $v \times M \times M \times M$

**Caratteristiche:**
- La GPU esegue questa operazione in parallelo su miliardi di bit
- La risposta avviene in **meno di 1 millisecondo**
- Il sistema è deterministico al 100% — **non può allucinare**
- Può gestire decine di migliaia di query al secondo contemporaneamente

**Output all'umano:**
- Il risultato delle operazioni su GPU (nodi e relazioni selezionate) viene presentato come **spunto per il ragionamento**
- L'umano applica il proprio **pensiero critico** per interpretare, valutare e decidere
- Il sistema fornisce connessioni verificate; l'umano fornisce giudizio, contesto e responsabilità

___
# Perché questa architettura funziona

Unisce i vantaggi di due mondi che di solito non si parlano:

**1. Conoscenza senza allucinazioni**
La conoscenza è accumulata in forma simbolica deterministica. Una volta estratta, non può essere distorta o inventata. Le inferenze sono operazioni matematiche verificabili.

**2. Efficienza computazionale**
Usi l'LLM solo per estrarre conoscenza dai testi (dove serve comprensione linguistica). Poi lo spegni. Per ragionare usi algebra lineare su GPU, che costa un milione di volte meno in termini di calcolo ed energia.

**3. Scalabilità**
Un database a grafi tradizionale crolla sotto il peso delle query a molti passaggi. GraphBLAS su GPU macina Terabyte di relazioni alla velocità della luce.

**4. Human in the Loop**
Il sistema non prende decisioni. Fornisce connessioni verificate in millisecondi. L'umano applica pensiero critico, giudizio etico, responsabilità — ciò che nessun agente autonomo può fare.

___
# Limiti dell'Architettura

**1. La Fase 1 è il collo di bottiglia**
Se Hyper-Extract non estrae una relazione dal testo originale, quella connessione **non esiste** nel sistema. La GPU può solo trovare percorsi esistenti, non creare conoscenza nuova. La qualità dell'estrazione determina tutto il sistema.

**2. Solo inferenza deduttiva, non induttiva**
Il sistema trova connessioni esistenti ma non-notate (inferenza deduttiva). **Non può fare ipotesi su controfattuali, probabilità o mondi possibili (inferenza induttiva). Per quello serve il pensiero umano.**

**3. Hardware per dataset grandi**
Per grafi tipo Wikidata (100M+ nodi) serve hardware enterprise:
- GPU con 80+ GB VRAM (A100, H100) o multiple GPU
- O architettura ibrida complessa (GPU per indici, CPU per metadati)
- GPU consumer (24 GB) bastano solo per domini limitati

**4. Aggiornamenti incrementali (parzialmente risolto)**
Hyper-Extract permette di aggiungere nuovi documenti con `he feed`:
- ✅ Carica la knowledge base esistente
- ✅ Estrae dai nuovi documenti
- ✅ Merge intelligente: entità uguali vengono fuse, descrizioni combinate
- ⚠️ Da verificare se GraphBLAS aggiorna le matrici incrementalmente o richiede ricostruzione

**5. Complessità delle ontologie**
Ontologie molto ricche (con molte dimensioni, vincoli, regole) richiedono più memoria e computazione. Il trade-off tra espressività e performance va gestito per dominio.

**6. Query devono essere traducibili in vincoli**
Non tutte le domande si mappano bene su operazioni tensoriali. Query con condizioni molto complesse o mal definite richiedono pre-processing su CPU o riformulazione.

___
# Il Tensore della Conoscenza e Query Domain-Agnostic

## Il Tensore della Conoscenza

La conoscenza accumulata non è un grafo piatto, ma un **tensore multi-dimensionale esprimibilmente completo**. Ogni asse rappresenta una dimensione della conoscenza:

Esempio:
1. **Entità** — i nodi del grafo (chi/cosa)
2. **Relazioni** — i collegamenti (come sono collegati)
3. **Tempo** — quando la relazione è valida (timestamp, intervalli, validità temporale)
4. **Spazio/Contesto** — dove/in quale contesto la relazione sussiste
5. **Tipo/Dominio** — in quale ontologia la relazione ha senso
6. **Truth Value** — grado di certezza/verifica (float32, propagabile)
7. **Ricorsione** — profondità di nidificazione (relazioni dentro relazioni)
8. **Vincoli** — regole e condizioni applicabili
9. **Codice Eseguibile** — funzioni associate alle relazioni

**Completezza Espressiva:** Il tensore può rappresentare qualsiasi concetto complesso senza semplificazioni riduttive, integrando:
- Strutture **ricorsive e nidificate** (ipergrafi, non triplette piatte)
- **Logica probabilistica** (truth value propagabili)
- **Relazioni con infiniti argomenti** (non solo soggetto-azione-oggetto)
- **Strict typing** con validazione strutturale

## Il Dilemma Domain-Agnostic

Ogni dominio ha:
- **Ontologie diverse** (biologia: pathway/proteine; diritto: leggi/casi; business: aziende/mercati)
- **Regole di inferenza specifiche** (cosa conta come prova varia per dominio)
- **Pattern di query differenti** (domande tipiche del settore)

**Soluzione:** Il sistema non impone un'ontologia universale. Invece:

1. **Ogni dataset porta la propria ontologia** — definita nel template YAML di Hyper-Extract
2. **Le query specificano vincoli, non procedure** — come un computer quantistico
3. **Il motore di inferenza è separato dall'ontologia** — GraphBLAS opera su strutture, non su significati
4. **Type checking a inserimento** — se un LLM o utente inventa un tipo non registrato, il sistema lo rifiuta

## Query come Vincoli (Analogo Quantistico)

Invece di dire *"cerca A, poi B, poi C"*, l'utente specifica i **vincoli del risultato finale**:

```
Voglio trovare: [pattern desiderato]
Vincoli: [condizioni da soddisfare]
Dominio: [ontologia di riferimento]
```

Il sistema traduce questo in operazioni di algebra lineare che **collassano** il tensore verso gli stati che soddisfano i vincoli.

**Esempio (Biologia Strutturale):**
```
Voglio trovare: proteine che influenzano questo pathway
Vincoli: 
  - interazione diretta o a 2 passaggi
  - pubblicazioni ≥ 3 che confermano
  - organismo: Homo sapiens
  - trust value > 0.8
```

Il sistema esegue operazioni sul tensore che isolano le componenti che soddisfano tutti i vincoli simultaneamente.

## Perché è Domain-Agnostic

- **Struttura separata da significato** — GraphBLAS vede numeri, non "proteine" o "aziende"
- **Ontologie plug-and-play** — ogni dominio definisce le sue regole
- **Query astratte** — il linguaggio di query non conosce i domini
- **Inferenza verificabile** — ogni risultato mostra la catena di operazioni che l'ha prodotto
- **Homoiconicità** — codice e dati hanno la stessa struttura, permettendo metaprogrammazione

___
# Ciclo di Brainstorming Generativo + Verifica Simbolica

Oltre alle query dirette, il sistema supporta un **ciclo di ragionamento assistito** che combina generazione creativa e verifica deterministica.

## Il Problema

Gli LLM sono eccellenti per:
- **Generare idee** (brainstorming, connessioni inattese, ipotesi)
- **Pensiero induttivo** (controfattuali, probabilità, mondi possibili)

Ma sono inaffidabili per:
- **Verificare fatti** (allucinano con sicurezza)
- **Tracciare ragionamenti** (black box, non sai perché hanno risposto così)

## La Soluzione: Due Fasi Separate

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│ 1. GENERA   │ ──> │ 2. VERIFICA  │ ──> │ 3. VALUTA   │
│   (LLM)     │     │ (Simbolico)  │     │   (Umano)   │
│ Brainstorm  │     │ Chain check  │     │  Giudizio   │
└─────────────┘     └──────────────┘     └─────────────┘
```

### Fase 1: Generazione (LLM)

L'LLM genera ipotesi, idee, connessioni in modalità **creativa**:

```
Input: "Quali proteine potrebbero influenzare questo pathway?"
Output LLM: "Proteina X, Proteina Y, o forse il complesso Z..."
```

Qui l'LLM **non sta affermando verità**. Sta facendo brainstorming.

### Fase 2: Verifica (Sistema Simbolico)

Ogni ipotesi generata viene **confrontata con la base di conoscenza**:

```
Ipotesi: "Proteina X influenza il pathway P"

Il sistema simbolico:
1. Cerca nel tensore se esiste la relazione
2. Se esiste: restituisce la chain di giustificazione
   - Quali documenti la menzionano
   - Trust value della relazione
   - Path di inferenza che la supporta
3. Se non esiste: segnala "non verificato" (non "falso")
```

**La chain di giustificazione** è cruciale:
- Non è una black box
- Mostra il percorso: Documento A → Estrazione → Relazione → Inferenza
- Permette all'umano di **risalire alle fonti**

### Fase 3: Valutazione (Umano)

L'umano riceve:
- ✅ **Verificato** + chain di giustificazione → "Buona intuizione, supportata da evidenze"
- ⚠️ **Non verificato** → "Potrebbe essere nuova conoscenza, serve investigazione"
- ❌ **Contraddetto** → "Incompatibile con conoscenza esistente"

**Il giudizio finale è umano:**
- Una idea non verificata può essere:
  - Una ca**ata (probabile)
  - Una scoperta potenziale (raro, ma possibile)
- Solo l'esperto del dominio può distinguere

## Perché Questo Ciclo Funziona

| Componente | Ruolo | Perché |
|------------|-------|--------|
| **LLM** | Genera ipotesi | Creativo, induttivo, fa connessioni inattese |
| **Simbolico** | Verifica | Deterministico, tracciabile, no allucinazioni |
| **Umano** | Decide | Giudizio critico, contesto, responsabilità |

## Esempio Concreto

**Ricercatore in biologia strutturale:**

```
1. GENERA (LLM):
   "Potrei testare se la proteina BRCA1 interagisce con questo dominio"

2. VERIFICA (Simbolico):
   ✅ Trovato: 3 pubblicazioni confermano l'interazione
   Chain: PMID:12345 → Fig.3 → Co-IP → Trust: 0.87
   
3. VALUTA (Umano):
   "Già noto, ma posso esplorare le condizioni specifiche 
    non ancora studiate"
```

**Oppure:**

```
1. GENERA (LLM):
   "E se questo enzima avesse attività inversa in condizioni anaerobiche?"

2. VERIFICA (Simbolico):
   ⚠️ Non trovato: nessuna pubblicazione menziona questa condizione
   
3. VALUTA (Umano):
   "Nessuno l'ha mai studiato. Potrebbe essere una direzione 
    di ricerca valida. Progettiamo un esperimento."
```

## Modalità Spiegazione

Quando il sistema restituisce un risultato, include sempre:

```
Risultato: [connessione trovata]
Confidenza: [trust value]
Giustificazione:
  - Fonte: [documento X, pagina Y]
  - Estratto il: [data]
  - Inferenze intermedie: [A → B → C]
  - Verificato da: [numero di fonti indipendenti]
```

Questo trasforma il sistema da **oracolo** (risponde e basta) a **strumento di pensiero** (ti mostra come ci è arrivato).

___
# Composizione del Sistema

Questa architettura integra:

- **Hyperon** — concetti semplici e composizionalità
- **OpenCog** — grafo + inferenza (ECAN, AtomSpace)
- **GPU** — performance 100x su grafi massivi
- **Hyper-Extract** — ingestione automatica da documenti
- **.microsymbol** — community distribuita che costruisce conoscenza
- **Intelligent Amplification** — visione guida: amplificare l'umano, non sostituirlo

___
# Note su Questo Documento

Questo è un **esempio concreto** di architettura di Intelligent Amplification. Serve come:

1. **Casistica di studio** — per ragionare su cosa significa IA in pratica
2. **Punto di partenza** — non è la soluzione definitiva, ma un'istanza specifica
3. **Strumento di pensiero** — per esplorare trade-off, limiti e possibilità

Per i principi fondamentali dell'Intelligent Amplification, vedi:
- [[Amplifica l'Essere Umano senza sostituirlo]]
- [[Espressivamente Completo]]
- [[Proof of Truth e Training]]
- [[Attenzione Simbolica]]