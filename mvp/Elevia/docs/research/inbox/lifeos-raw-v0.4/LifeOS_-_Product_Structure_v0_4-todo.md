# LifeOS — Product Structure
*Versione 0.4 / Draft*

---

## Principio Generale

Il sistema è stratificato in due dimensioni indipendenti:

- **Tier delle Entità** (Tier 0 → Tier 2): cosa il sistema contiene. Universale, sempre presente, funziona anche offline e senza AI.
- **Layer del Motore** (Layer 1 → Layer 3): come il sistema ragiona. Si attiva progressivamente, su scelta dell'utente o al raggiungimento di soglie automatiche.

La complessità è disponibile, non obbligatoria. Tutto comunica con tutto: un Task può nascere da una Daily Note, un Habit può collegarsi a un Progetto, una Page può incorporare un Whiteboard. Le entità non sono silos — sono nodi dello stesso grafo.

---

## Tier delle Entità

### Tier 0 — Core

Le entità universali. Sempre presenti, sempre disponibili, funzionano anche offline e senza motore di inferenza.

#### Tasks

Unità di azione. Hanno:

- Titolo e descrizione
- Scadenza (opzionale)
- Reminder (opzionale — proprietà del task, non entità separata)
- Stato: aperto / in corso / completato / archiviato
- Collegamento a un Progetto, Area o nota

#### Calendar

Unità temporale. Hanno:

- Data e ora
- Durata
- Reminder (opzionale)
- Collegamento a Tasks, Note, Persone

> **Nota:** I Reminder non sono un'entità separata. Sono una proprietà temporale che si aggancia a Tasks e Calendar. Qualsiasi entità del sistema può avere un reminder associato.

#### Notes

Unità di conoscenza. Non è un'entità unica — è un contenitore con quattro modalità:

| Modalità | Scopo | Caratteristiche |
|---|---|---|
| **Quick note** | Cattura rapida | Zero attrito, nessuna struttura richiesta |
| **Doc** | Testo lungo e strutturato | Headings, formattazione, contenuto ricco |
| **Daily note** | Ancoraggio temporale | Legata a una data, aggrega eventi del giorno |
| **Page** | Interattiva e connessa | Menzioni, link bidirezionali, incorpora altri elementi |

---

### Tier 1 — Organizzazione

#### PARA

Il sistema organizzativo che struttura tutto il contenuto del Core.

| Livello | Descrizione |
|---|---|
| **Progetti** | Obiettivi con scadenza e outcome definito |
| **Aree** | Responsabilità continuative senza scadenza |
| **Risorse** | Materiale di riferimento per argomento |
| **Archivio** | Tutto ciò che non è più attivo |

I **tag** sono variabili e non gerarchici: ogni entità può appartenere a più contesti contemporaneamente. I tag non sono solo etichette: sono la prima unità di navigazione del retrieval progressivo — ogni tag rappresenta un dominio cognitivo dell'utente.

**Template dei Progetti.** I Progetti supportano template scaricabili dalla community. Un template definisce la struttura iniziale (tasks standard, note collegate, metriche da tracciare).

---

### Tier 2 — Estensioni

Moduli attivabili dall'utente in base alle proprie esigenze. Non obbligatori — si aggiungono quando servono.

| Estensione | Scopo |
|---|---|
| **Habits / Daily Routine** | Tracciamento di comportamenti ricorrenti |
| **Journal** | Spazio riflessivo, separato dalle note operative |
| **Flashcards** | Apprendimento attivo dal contenuto esistente |
| **Whiteboards** | Spazio visivo per brainstorming e mappe concettuali |

Ogni estensione si integra con il Core: un Habit può collegarsi a un'Area PARA, le Flashcards si generano da un Doc, un Whiteboard può diventare una Page.

---

## Layer del Motore

Il motore è trasversale a tutto il sistema ma non è sempre attivo. I tre layer hanno complessità crescente.

### Layer 1 — App Nativa

Sempre attivo. Gestisce Tasks, Calendar, Notes senza AI. Leggero, immediato, disponibile offline. Copre il 90% dell'uso quotidiano.

### Layer 2 — Memoria Semantica

Ricerca per significato, suggerimenti contestuali, note simili. Risponde in meno di un secondo. Si attiva automaticamente durante la navigazione e la scrittura.

```
"Trovami note simili a questa"     → Layer 2
"Cosa ho scritto su questo tema?"  → Layer 2
```

### Layer 3 — Inferenza (OpenCog / PLN)

Il motore di ragionamento profondo. **Non è sempre attivo** — si attiva in tre situazioni:

**1. Richiesta esplicita dell'utente**
```
"Cosa mi dice il sistema su come sto gestendo la salute?"
"Cosa collega questi tre progetti?"
"Perché continuo a procrastinare il lunedì?"
```

**2. Soglia raggiunta.** Il sistema rileva che su un tema si è accumulato abbastanza materiale per proporre una connessione non ovvia. Propone — l'utente decide se approfondire.

**3. Sessione di Review.** Programmata dall'utente (es. ogni domenica sera). Il motore analizza il periodo, porta in superficie pattern, contraddizioni, evoluzioni nelle Life-Metrics.

#### Guida rapida — quando serve quale Layer

| Situazione | Layer |
|---|---|
| Aggiungere un task | 1 |
| Settare un reminder | 1 |
| Cercare una nota per parola chiave | 1 |
| Trovare note simili per significato | 2 |
| "Cosa so di questa persona?" | 2 |
| "Perché continuo a procrastinare?" | 3 |
| "Cosa collega questi progetti?" | 3 |
| Analisi Life-Metrics nel tempo | 3 |
| Weekly / Monthly Review | 3 |
| Pattern anomalo rilevato dal sistema | 3 |

---

## Object / Metrics

Ogni entità del sistema è anche un **Object** — un nodo nel grafo con attributi misurabili. Questi attributi emergono automaticamente dal contenuto: l'LLM li estrae, l'utente li conferma con un'azione singola.

```
Nota: "Riunione con Rossi, 2 ore, molto produttiva"

LLM propone:
  durata       = 2h
  qualità      = alta
  partecipanti = [Rossi]

Utente conferma → entra nel grafo come fatto validato.
```

Gli Object/Metrics estratti automaticamente si distinguono dalle **Life-Metrics**, che l'utente definisce esplicitamente:

| Tipo | Chi le crea | Esempi |
|---|---|---|
| **Object/Metrics** | Sistema (LLM estrae, utente conferma) | durata riunione, qualità percepita, energia |
| **Life-Metrics** | Utente (definite esplicitamente) | Kcal giornaliere = 2000, ore sonno = 7.5, sessioni sport = 3/sett. |

Nel tempo, le Object/Metrics si agganciano alle Life-Metrics, permettendo al Layer 3 di misurare lo scarto tra target e reale durante la Review.

---

## Supersessione dei Fatti

I fatti strutturati hanno metadati temporali, estratti in formato soggetto-verbo-oggetto:

```
utente | vive a | Milano [dal: 2025-03-10, status: attivo]
```

Quando un fatto viene aggiornato, la versione precedente non viene eliminata ma marcata come superata:

```
utente | vive a | Milano    [dal: 2025-03-10, al: 2025-09-15, status: superato]
utente | vive a | Barcellona [dal: 2025-09-15, status: attivo]
```

Il sistema risponde sempre usando solo i fatti con status attivo, ma conserva l'intera storia per audit e contesto storico.

---

## Normalizzazione Semantica

Per mantenere la coerenza del grafo ed evitare duplicati semantici (es. "ha mangiato", "had eaten", "si è abbuffato"), ogni relazione estratta dall'LLM passa attraverso una pipeline di normalizzazione prima di entrare nel grafo.

```
LLM estrae relazione in linguaggio libero
    │
    ▼
Passo 1 — Mapping ontologico
    L'LLM mappa sul concetto canonico più vicino
    "ha mangiato" → onto:consumare_cibo
    │
    ▼
Passo 2 — Controllo duplicati (Vector DB)
    Esiste già onto:consumare_cibo nel grafo?
    Sì → usa quella, aggiorna il peso
    No → crea nuova voce canonica
    │
    ▼
Passo 3 — Soglia di ambiguità
    Se il mapping ontologico non è sicuro (< soglia):
    → propone all'utente di confermare
    │
    ▼
Grafo pulito con concetti canonici
```

Il risultato è un grafo multilingua by design: una nota in italiano e una in inglese sullo stesso argomento producono gli stessi atomi canonici, indipendentemente dalla lingua originale.

---

## Comunicazione tra Entità

Tutte le entità del sistema sono nodi dello stesso grafo. Possono comunicare e creare esperienze interattive:

- Una **Daily Note** aggrega automaticamente i Tasks del giorno e gli eventi del Calendar
- Un **Habit** può collegarsi a un'**Area** PARA e contribuire alle Life-Metrics
- Una **Page** può incorporare un **Whiteboard**, Tasks in linea, e link bidirezionali ad altre Pages
- Un **Progetto** aggrega Tasks, Note, Metriche e può essere creato da template
- Le **Flashcards** si generano dal contenuto di un **Doc**
- Il **Journal** può referenziare eventi del **Calendar** e Tasks completati

Il Layer 3 può attraversare queste connessioni per trovare pattern che nessun singolo modulo vedrebbe da solo.
