# LifeOS — Product Specification
*Versione 0.4 / Draft*


- I **tag** sono variabili e non gerarchici: ogni entità può appartenere a più contesti contemporaneamente
- I **collegamenti tra note** (MOC) sono preferiti alla categorizzazione rigida
- I tag non sono solo etichette: sono la prima unità di navigazione del retrieval progressivo — ogni tag rappresenta un dominio cognitivo dell'utente

---

## 1. Flusso Operativo

```
Cattura → Elaborazione → Connessione → Organizzazione → Azione ↔ Review
```

Il flusso è l'unica definizione canonica. → *Vedi anche: Vision v0.4 per la mappa completa fase/chi/dove.*

### Cattura (RAW)

Zero attrito, qualsiasi fonte, qualsiasi formato compatibile. Con peso assegnato dall'utente. Ogni informazione nuova viene taggata automaticamente dal sistema, che identifica le keyword dalla RAW.

Formati supportati in ingresso: testo, PDF, audio/video, immagini (descritte testualmente per consentire l'inferenza, essendo troppo pesanti, viene escluso il singolo file dall'elaborazione, ma solo le descrizione, vengono salvati puntando per capire), link esterni.

### Elaborazione

- Tipizzazione AI iniziale per ridurre il carico cognitivo della review
- L'utente conferma o corregge con un'azione singola
- Il dato RAW originale rimane sempre intatto
- Un LLM fine-tunato sull'Edge è ottimizzato per il riconoscimento delle relazioni nei RAW

### Connessione

- Link suggeriti automaticamente dal sistema tra note, task ed eventi correlati
- La normalizzazione semantica garantisce coerenza del grafo → *Vedi: Structure v0.4 — Normalizzazione Semantica*

### Organizzazione

- Tag validati dall'utente; il backend ottimizza in autonomia
- L'utente approva la tassonomia visibile
- I tag sono la prima unità di navigazione del retrieval progressivo

### Azione

- Il sistema propone riformulazioni
- Suggerisce prossimi step basandosi sullo storico
- Riprende dal punto in cui l'utente si è interrotto

### Review

- Mostra i dati grezzi da approvare
- Questo meccanismo resetta l'entropia del sistema senza mai perdere dati
- Le informazioni a basso valore vengono proposte per archivio o eliminazione

**Algoritmo Reset Entropia**

L'ordinamento parte dalle azioni più semplici (eliminare duplicati) fino alle più complesse. Le cose facili si risolvono subito; quelle difficili rimangono visibili finché non vengono affrontate.

---

## 2. Modalità di Utilizzo

### Routines

Gestisce promemoria e attivazioni passive configurate dall'utente. Gira in background senza richiedere attenzione deliberata.

### Session

L'utente lavora attivamente su una sessione.

**Workflow**
- Le sessioni vengono salvate e analizzate
- Il sistema predice e anticipa le attività future basandosi sullo storico

**Focus**
- Concentra il contesto su una specifica attività o progetto
- Filtra dinamicamente ciò che è rilevante nel momento
- Restringe l'attenzione a un dominio specifico (es. Lavoro, Studio, Personale)
- Il filtro è dinamico, non strutturale

---

## 3. Sistema di Memoria e Retrieval

### Principi

- Il sistema non dimentica: decide cosa mostrare prima e cosa tenere in profondità
- I dati RAW non vengono mai persi
- Supporta qualsiasi formato in ingresso: PDF, testo, audio/video
- La supersessione dei fatti garantisce che il sistema risponda sempre con lo stato attuale, conservando la storia → *Vedi: Structure v0.4 — Supersessione dei Fatti*

### Architettura

- Ogni informazione viene archiviata in modalità **embedding vettoriale**
- Il recupero avviene tramite **ricerca semantica** combinata con **full-text search**
- Il ranking tra questi è unificato tramite **Reciprocal Rank Fusion (RRF)**
- Ricerca vettoriale: **Qdrant**

### Retrieval Progressivo (3 livelli) Stile Checkpoint

Ogni livello è un compromesso tra compressione e fedeltà. Il sistema naviga questo compromesso dinamicamente, senza caricare tutto in anticipo.

- **Tag** — il sistema legge il sommario compresso dell'intero dominio tematico. Spesso è sufficiente per rispondere.
- **Segmento** — se serve più dettaglio, scende nei segmenti del tag: blocchi di dialogo attorno a un sotto-argomento coerente.
- **Turno originale** — solo se necessario, risale alla fonte grezza esatta.

### Spreading Activation

- Il sistema attiva pattern e vettori in base allo storico di attivazione dell'utente
- Le risposte vengono rankate considerando ciò che è stato attivato in passato

### Indice Globale

Il sistema lavora su un indice globale che si aggiorna ad ogni Review. L'indice usa implementazioni tipo MOC (Map of Content) e rimane flessibile.

---

## 4. AI Subsystem

### Architettura

- Agenti specializzati (es. formattazione Markdown, ricerca su dataset, ricerca su Web)
- Ottimizzazione su tre leve: **meno contesto** (inviato solo quando serve), **modello giusto** (potente solo quando necessario), **meno step** (niente loop inutili)

### Loop di Tool-Call Iterativi

Il modello costruisce attivamente il proprio contesto round dopo round:

1. Legge il vocabolario dei tag e identifica i domini rilevanti
2. Recupera i sommari dei tag pertinenti
3. Se serve più profondità, espande un segmento specifico
4. Se necessario, risale al turno originale o al fatto strutturato

### Comportamento Adattivo

- Impara il vocabolario abituale dell'utente
- Suggerisce correzioni o ottimizzazioni quando l'utente inserisce nuove informazioni
- Valuta il feedback dell'utente: se positivo, rafforza il comportamento; se negativo, inibisce e ricalcola

### Personalizzazione

- Supporta la creazione di plugin basati su LLM custom con API esterne configurabili
- Il costo di utilizzo è comunicato in modo trasparente
- L'utente può definire istruzioni personalizzate (Functions) per automatizzare alcuni comportamenti

### Modalità d'uso delle API

L'utente può scegliere tra:

- **API proprie** (es. OpenAI, Anthropic) per le funzionalità LLM di riepilogo e comprensione
- **API del LifeOS** come layer di astrazione unificato
- **OpenCog** per il ragionamento simbolico e la gestione della memoria a lungo termine

---

## 5. Metriche

### Object/Metrics e Life-Metrics

La distinzione canonica è definita in Structure v0.4. In sintesi:

- **Object/Metrics**: estratte automaticamente dall'LLM, confermate dall'utente con un'azione singola
- **Life-Metrics**: definite esplicitamente dall'utente, base per gli OKR personali

Le Life-Metrics permettono di assegnare metriche a qualsiasi valore della propria vita e guidano le decisioni con dati reali, non percezioni.

### Statistiche di Sistema *(futuro)*

- Sistema di monitoraggio basato su eventi (es. TaskCompleted)
- Visibile all'utente per trasparenza

---

## 6. Integrazioni

### API ed Estensioni

- Interfaccia con API di app e servizi esterni
- Supporto Webhook come sistema di personalizzazione
- Supporto Shortcuts (stile Apple)
- Interfaccia con l'OS dell'utente, inclusa la possibilità di selezionare un'area specifica del desktop

### Contenuti Media

- Importazione da video/audio (es. sottotitoli): il riferimento originale viene mantenuto
- Per contenuti lunghi, riassunto contestuale basato sullo scopo dichiarato dall'utente
- Tutto ciò che non è testuale viene descritto in testo, per consentire l'inferenza

### Team *(futuro)*

- Condivisione parziale dello spazio cognitivo con altri utenti
- Collaborazione real-time
- Meccanismo di condivisione del contesto per collaborazione cognitiva sui Progetti

### Esportazione

- Possibilità di esportare tutto il LifeOS (Front e Back) in formato Markdown

---

## 7. Architettura Backend

**Formato:** WebApp (compatibilità universale)

### Principi

- **Lato elaborazione**: rigido e ottimizzato per i computer (strutture dati, embedding numerici, indici)
- **Lato utente**: fluido, si adatta al cervello dell'utente
- **Modulare**: ogni componente può essere aggiornato o sostituito in modo indipendente

### Rendering del Frontend

- Il frontend logico viene costruito dinamicamente in base al profilo e al comportamento dell'utente
- Il design è ottimizzato per il cervello umano: riduzione del carico visivo, gerarchie chiare

### Sincronizzazione

- Sync a blocchi per velocità e leggerezza
- Funzionamento offline con cache basata sullo storico di utilizzo
- Gestione multi-device senza creare conflitti

---

## 8. Onboarding

- Al primo accesso, audit completo con autorizzazione step-by-step
- Il sistema chiede: nome, data di nascita, eventuali metriche iniziali da tracciare
- L'esperienza dei primi 30 giorni è progettata per essere utile anche prima che il grafo sia ricco → *Vedi: Risk v0.4 — Cold Start*
