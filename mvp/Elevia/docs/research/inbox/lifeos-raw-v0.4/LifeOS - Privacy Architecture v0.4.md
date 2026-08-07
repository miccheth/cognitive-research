*Versione: v0.4*
*Tipo: draft*

---
## Panoramica
Il client è **open source**, per garantire trasparenza e verificabilità.

Il sistema è costruito sul principio **zero-knowledge** (partially): il server che esegue il calcolo non può mai risalire alle informazioni reali dell'utente. Anche se venisse compromesso, non conterrebbe nulla di leggibile.

Il sistema si articola in tre livelli:

1. **Edge (dispositivo locale)** — gestisce tutti i dati in chiaro, il parsing NLP, l'offuscamento e la decifratura. La chiave privata non lascia mai questo livello.
2. **Server** — archivia ed elabora atomi anonimizzati e blob cifrati; non può mai leggerne il contenuto.
3. **Mappa ID** — tabella di lookup che collega le entità reali ai loro identificatori opachi. Archiviata sul server come blob cifrato, scaricata e decifrata localmente dall'Edge.

---
## Parte 1 — Flusso dei Dati

### 1.1 Fase di Input (Edge)

Scrivi una nota: _"Il Cliente Rossi ha comprato il Progetto Alpha"_.

**Parsing Locale** (es. spaCy) — estrae la struttura semantica:

|Ruolo|Valore|
|---|---|
|Soggetto|`Cliente Rossi`|
|Predicato|`ha comprato`|
|Oggetto|`Progetto Alpha`|

**Offuscamento (Mapping)** — l'Edge scarica la Mappa ID cifrata, la decifra localmente e sostituisce le entità reali:

|Entità reale|Identificatore|
|---|---|
|`Cliente Rossi`|`ID_999`|
|`Progetto Alpha`|`ID_111`|
|`ha comprato`|`REL_XYZ`|

**Invio al Server** — l'Edge trasmette un atomo in formato MeTTa/Atomese:

```
EvaluationLink
  (PredicateNode "REL_XYZ")
  (ListLink
    (ConceptNode "ID_999")
    (ConceptNode "ID_111"))
```

> Il server riceve solo codici opachi: non sa che si tratta di un cliente e di un progetto.

---

### 1.2 Fase di Elaborazione (Server — Il Motore Cieco)
Il server aggiunge l'atomo ricevuto al suo **AtomSpace** globale, dove risiedono migliaia di altri atomi cifrati.

**Query di esempio:** _"Trova connessioni per ID_999"_

**Pattern Matching + Inferenza PLN** — il server individua che in una nota precedente:

```
ID_999  --[REL_77]-->  ID_444
```

**Risposta del server:** _"Ho trovato un collegamento: ID_999 è legato a ID_444 tramite REL_77."_

> Il server non sa che sta parlando di un cliente e della sua azienda.

---

### 1.3 Fase di Risultato (Edge — Ritorno al PKMS)

**Decodifica** — l'Edge scarica la Mappa ID cifrata, la decifra localmente e ricostruisce le entità reali:

|Identificatore|Entità reale|
|---|---|
|`ID_999`|`Cliente Rossi`|
|`ID_444`|`Azienda X`|
|`REL_77`|`lavora per`|

**Visualizzazione nel PKMS:**

> _"Ehi, ti ricordo che il Cliente Rossi (di cui stai scrivendo) lavora per l'Azienda X."_

---
## Parte 2 — Scalabilità
### 2.1 Workflow di Ingestione Massiva

Per processare migliaia di note in modo automatizzato:

1. **Ingestion Script** — uno script Python legge i file sorgente (Markdown, PDF, ecc.), estrae concetti tramite NLP e li trasforma in atomi MeTTa offuscati.
2. **Indexing** — gli atomi vengono inviati al DAS, che li indicizza per ricerche rapide basate su pattern matching.
3. **Reflective Maintenance** — agenti MeTTa girano in background (codice auto-modificante) e riorganizzano i collegamenti tra le note, trovando nuove correlazioni man mano che il PKMS cresce.

> **Nota sull'indicizzazione:** una volta elaborati, i dati vanno indicizzati. Poiché il sistema è offuscato, l'indice evita di dover ricalcolare ogni volta le stesse inferenze.


---
## Parte 3 — Gestione delle Ontologie

### 3.1 Mappa ID Cifrata sul Server

La Mappa ID segue la stessa strategia zero-knowledge delle ontologie:

1. **Archiviazione:** la mappa `ID → Nome` viene cifrata con la chiave privata dell'utente e caricata sul server come blob opaco. Il server non può risalire alle entità reali.
2. **Fetch al bisogno:** prima di elaborare una nota, l'Edge scarica la mappa (o solo la porzione rilevante) e la decifra in RAM.
3. **Aggiornamento:** quando si aggiunge una nuova entità (es. un nuovo cliente), l'Edge aggiorna la mappa localmente, la ri-cifra e carica la versione aggiornata sul server.
4. **Nessun dato in chiaro sul disco locale:** la mappa non è mai salvata in chiaro sul dispositivo; vive solo in RAM durante l'elaborazione.

**Vantaggio:** se il dispositivo viene perso o rubato, la mappa non è recuperabile senza la chiave privata. Se il server viene compromesso, i blob cifrati sono inutili senza la chiave.


---

## Parte 4 — Integrazione con LLM Locale

### 4.1 Ruoli nel Sistema

|Componente|Ruolo|
|---|---|
|**LLM locale**|Interprete: traduce il linguaggio umano in strutture logiche|
|**OpenCog/MeTTa**|Memoria a lungo termine: conserva miliardi di schemi e trova pattern|
|**Mappa ID**|Sicurezza: archiviata cifrata sul server, decifrata localmente all'occorrenza|

### 4.2 Pipeline di Elaborazione

1. **Estrazione (LLM):** legge la nota _"Ieri ho incontrato il Sig. Rossi al bar"_ e produce fatti strutturati:
    
    ```
    (Incontrato Io Rossi)(Luogo Bar)(Tempo Ieri)
    ```
    
2. **Anonimizzazione (Edge Script):** sostituisce `Rossi` con `ID_999`.
3. **Ragionamento (OpenCog):** invia i fatti anonimizzati al server per individuare collegamenti con altre note.

### 4.3 Vantaggi dell'LLM Locale

- **Privacy:** il testo in chiaro viene letto solo dall'LLM sul tuo hardware. Nessun dato leggibile esce mai dal dispositivo.
- **Nessuna manualità:** non è necessario imparare MeTTa. Si scrive normalmente e l'LLM "compila" la nota in logica per OpenCog.
- **Risoluzione delle ambiguità:** l'LLM distingue se "Rossi" indica il cliente o il colore, aiutando l'Edge a selezionare l'ID corretto dalla mappa.

### 4.4 Modalità d'uso delle API

L'utente può scegliere tra:

- **API proprie** (es. OpenAI, Anthropic) per le funzionalità LLM di riepilogo e comprensione.
- **API del LifeOS** come layer di astrazione unificato.
- **OpenCog** per il ragionamento simbolico e la gestione della memoria a lungo termine.

---

## Parte 5 — Sicurezza Avanzata

### 5.1 Salt per Prevenire Attacchi di Correlazione

**Problema:** anche con l'offuscamento, un attaccante potrebbe eseguire attacchi di correlazione confrontando la frequenza degli ID nel grafo cifrato con pattern noti (es. un ID che appare in migliaia di relazioni è probabilmente un'entità importante).

**Soluzione — Salt per ID:** aggiungere un valore casuale (salt) durante il mapping, in modo che la stessa entità reale produca ID diversi in contesti differenti.

**Trade-off:**

|Aspetto|Con Salt|Senza Salt|
|---|---|---|
|Sicurezza|✅ Resistente agli attacchi di correlazione|⚠️ Vulnerabile a pattern analysis|
|Consistenza|⚠️ Lo stesso nome può avere più ID|✅ Un ID univoco per entità|
|Complessità|Alta (gestione di mapping multipli)|Bassa|

**Possibile compromesso:** usare il salt solo per le relazioni più sensibili (es. nomi di persone), mantenendo ID stabili per entità meno critiche (es. categorie generali).

---