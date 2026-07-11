
___
# L'Architettura in 3 Fasi

Il sistema funziona come una catena di montaggio che trasforma il linguaggio umano disordinato in calcoli matematici istantanei.

```
[Testo Grezzo] ──(1. Hyper-Extract + LLM)──> [JSON Strutturato] ──(2. GraphBLAS)──> [Matrici Sparse su GPU] ──(3. Query)──> [Risultati GPU] ──(4. LLM)──> [Risposta in Linguaggio Naturale]
```

___
## Fase 1: La Distillazione (Hyper-Extract + LLM)

È la fase di **ingestione e comprensione**. Prende i documenti (50 GB o 1 TB che siano) e li traduce in dati puliti. Eliminando prima il rumore.

**Come funziona:**
- Un template YAML definisce le regole (es. "cerca Persone, Aziende e i loro Ruoli nel tempo")
- Si utilizza la libreria [Hyper-Extract](https://github.com/yifanfeng97/hyper-extract)
- Un LLM locale (es. Qwen o Llama a 4/8 bit su framework vLLM) legge i testi
- Grazie alla funzionalità di *Structured Output*, estrae le informazioni formattandole in JSON rigidi

**Caratteristiche:**
- È la fase più lenta e pesante (richiede da poche ore a giorni a seconda delle GPU)
- Si esegue **una sola volta** per ogni documento

___
## Fase 2: La Mappatura Matematica (GraphBLAS)

È il cuore computazionale del sistema. Prende il JSON generato da Hyper-Extract e lo converte in **matematica pura**.

**Come funziona:**
- Ogni entità (es. Elon Musk o SpaceX) riceve un indice numerico stabile
- Le relazioni vengono inserite all'interno di **Matrici Sparse Giganti**
- Se Elon Musk (riga 0) è CEO di SpaceX (colonna 2), la cella `[0, 2]` conterrà il metadato della relazione

**Caratteristiche:**
- GraphBLAS memorizza solo i collegamenti reali, ignorando i miliardi di "zeri" (le relazioni inesistenti)
- Questo permette di comprimere l'intero grafo direttamente nella memoria della GPU

___
## Fase 3: L'Interrogazione (L'Hardware in Azione)

È il momento in cui l'utente o un agente IA fa una domanda complessa (es. *"Trova le aziende collegate a SpaceX dopo 3 passaggi logici"*).

**Come funziona:**
- La query non viene letta da un LLM, ma viene tradotta in un'operazione di **Algebra Lineare**
- Trovare connessioni a 3 passaggi significa fare una moltiplicazione di matrici sparse: $v \times M \times M \times M$

**Caratteristiche:**
- La GPU esegue questa operazione in parallelo su miliardi di bit
- La risposta avviene in **meno di 1 millisecondo**
- Il sistema è deterministico al 100% (non può allucinare)
- Può gestire decine di migliaia di query al secondo contemporaneamente

**Output all'LLM:**
- Il risultato delle operazioni su GPU (i nodi e le relazioni selezionate) viene passato a un LLM
- L'LLM genera la risposta finale in linguaggio naturale, basandosi sui dati strutturati ricevuti
- Questo combina la precisione deterministica del simbolico con la fluidità espressiva del neurale

___
# Perché questa architettura è rivoluzionaria

Unisce i vantaggi di due mondi che di solito non si parlano:

**1. Massima Precisione ed Efficienza**
Usi l'LLM solo per il compito in cui eccelle (capire il testo all'inizio e generare la risposta finale). Poi lo spegni. Per cercare le connessioni usi la matematica delle matrici sparse, che costa un milione di volte meno in termini di calcolo ed energia rispetto a un LLM.

**2. Scalabilità Infinita**
Un database a grafi tradizionale crolla sotto il peso delle query a molti passaggi (esplosione combinatoria). GraphBLAS su GPU macina Terabyte di relazioni alla velocità della luce perché sfrutta la stessa architettura hardware nata per i videogiochi e per il deep learning, ma applicata alla logica simbolica.

**3. Evoluzione di LLM Wiki (Karpathy)**
Questa architettura è un'evoluzione del concetto di LLM Wiki proposto da Andrej Karpathy: invece di chiedere all'LLM di ricordare tutto (e allucinare), si usa un sistema esterno deterministico per la conoscenza, e l'LLM fa solo ciò che sa fare meglio — comprendere e generare linguaggio.

___
# Limiti dell'Architettura

**1. La Fase 1 è il collo di bottiglia**
Se Hyper-Extract non estrae una relazione dal testo originale, quella connessione **non esiste** nel sistema. La GPU può solo trovare percorsi esistenti, non creare conoscenza nuova. La qualità dell'estrazione determina tutto il sistema.

**2. Solo inferenza deduttiva, non induttiva**
Il sistema trova connessioni esistenti ma non-notate (inferenza deduttiva). Non può fare ipotesi su controfattuali, probabilità o mondi possibili (inferenza induttiva). Per quello serve l'LLM sopra, ma introduce possibilità di allucinazione nella generazione del linguaggio.

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

**5. Query devono essere traducibili in algebra lineare**
Non tutte le domande si mappano bene su moltiplicazioni di matrici sparse. Query con condizioni complesse (filtri temporali, aggregazioni, ordinamenti) richiedono logica aggiuntiva su CPU.

**6. Scalabilità delle relazioni**
Ogni tipo di relazione (`born_in`, `worked_for`, ecc.) diventa una matrice separata. Con 1000+ tipi di relazioni (come Wikidata), la gestione diventa complessa.

___
