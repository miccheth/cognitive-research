
$$\text{IDEA} \rightarrow \text{FORMALIZZAZIONE} \rightarrow \text{ATTACCO} \rightarrow \text{CONSOLIDAMENTO} \rightarrow \text{VERSIONE}$$

## 1. Le 4 Funzioni Principali (In ordine di priorità)

### I. LLM come Critico Logico / Avversario (Massima priorità)

- **Obiettivo:** Smontare il testo per trovarne i punti deboli, senza edulcorare il feedback.
    
- **Regola d'oro:** Non chiedere mai all'LLM di "migliorare" o "espandere" in questa fase.
    
- **Prompt chiave:** > _"Trova tutte le contraddizioni interne, le assunzioni nascoste e i punti non definiti di questo testo. Non proporre soluzioni."_
    

### II. AI come Simulatore

- **Obiettivo:** Effettuare stress-test di scenari e ipotesi (sfruttando l'eccellenza dell'LLM nel calcolo delle ramificazioni logiche rispetto agli umani).
    
- **Prompt chiave:**
    
    > _"Se succede X, cosa emerge?"_
    > 
    > _"Genera 5 scenari concreti che mettono in crisi questa ipotesi."_
    

### III. LLM come Compressore / Riordinatore

- **Obiettivo:** Ottimizzare la struttura, i titoli e le tassonomie.
    
- **Test di chiarezza:** Se l'LLM non riesce a comprimere il testo, significa che l'idea di partenza non è ancora chiara.
    
- **Prompt chiave:**
    
    > _"Riduci questo testo alla sua forma minimale senza perdere informazione."_
    

### IV. LLM come Scrittore (Ultima priorità)

- **Regola d'oro:** Se si delega la scrittura all'LLM troppo presto, si sta barando e si perde il controllo del processo creativo. L'AI deve intervenire solo come esecutore finale di un pensiero già validato.
    

## 2. Principio Avanzato di Ingegneria del Prompt: I Doppi Ruoli

Non affidarsi mai a una sola istanza o a una sola "voce" dell'LLM per evitare l'illusione di solidità del testo. Durante la fase critica, utilizza sempre due ruoli AI distinti e contrapposti:

- **LLM Logica:** Rigida, analitica e "stupida" (esegue i controlli di consistenza rigorosa senza inventare nulla).
    
- **LLM Creativa:** Aggressiva, laterale e focalizzata sullo stress-test e sulla generazione di scenari di crisi.
    

## 3. Il Flusso di Integrazione Operativa (In 5 Fasi)

### Fase 1: IDEA

La scintilla iniziale o l'ipotesi grezza. Viene messa per iscritto dall'utente senza alcun filtro o intervento dell'AI.

### Fase 2: FORMALIZZAZIONE

Si applica la **Funzione III (Compressore / Riordinatore)** per pulire il rumore di fondo. Il testo viene ridotto alla sua struttura ossea e tassonomica essenziale. Se l'LLM fallisce la compressione coerente, si torna alla fase 1.

### Fase 3: ATTACCO (Il Loop Iterativo)

L'idea formalizzata entra nel tritacarne dei **Doppi Ruoli**:

1. L'**LLM Logica** applica la **Funzione I (Critico)** per mappare i buchi logici e le assunzioni non dichiarate.
    
2. L'**LLM Creativa** applica la **Funzione II (Simulatore)** per generare i 5 scenari di crisi.
    
3. **Valutazione di senso:** L'utente analizza l'output. L'idea ha ancora senso? Se i problemi emersi non sono gestibili o l'idea crolla, si reitera modificando la formalizzazione. Se l'idea regge, si passa oltre.
    

### Fase 3.5: TEST DEI BIAS COGNITIVI

Prima di consolidare le soluzioni, verificare che l'architettura logica non sia contaminata da distorsioni cognitive sistematiche.

- **Obiettivo:** Identificare e neutralizzare i bias che potrebbero compromettere la validità dell'idea.
    
- **Prompt chiave per l'LLM Logica:**
    
    > _"Analizza questo testo e identifica quali dei seguenti bias cognitivi potrebbero essere presenti: confirmation bias, anchoring bias, availability heuristic, overconfidence bias, survivorship bias. Per ciascuno, indica il punto esatto del testo dove emerge."_
    
- **Prompt chiave per l'LLM Creativa:**
    
    > _"Genera 3 scenari in cui un decisore razionale arriverebbe a conclusioni opposte a quelle presenti in questo testo. Quale bias potrebbe spiegare la divergenza?"_
    
- **Criterio di superamento:** Se vengono identificati bias non gestiti, si torna alla Fase 2 (FORMALIZZAZIONE) per ripulire l'idea dalle assunzioni distorte.
    
- **Flusso:** L'LLM Logica esegue la mappatura sistematica. L'LLM Creativa esegue lo stress-test divergente. L'utente valuta se i bias identificati inficiano la validità dell'idea.

### Fase 4: CONSOLIDAMENTO (Sampling Multiplo & Verifica)

**Prerequisito:** L'idea ha superato il Test dei BIAS Cognitivi.

Fase dedicata alla risoluzione delle falle emerse dall'Attacco. Invece di generare una singola risposta lineare, si sfrutta la solidità statistica del campionamento parallelo:

- **Best-of-N & Self-Consistency:** Si chiede all'LLM di generare _N_ soluzioni indipendenti per superare i punti critici evidenziati nella fase di attacco.
    
- **Reranking & Verifier Models:** Si utilizza l'**LLM Logica** (configurata come modello verificatore) per analizzare, valutare e classificare le _N_ soluzioni prodotte. Valutare e scartare le opzioni deboli è un compito matematicamente più efficiente per l'AI rispetto alla generazione cieca. Si seleziona la variante migliore e si integra nell'architettura logica dell'idea.
    

### Fase 5: VERSIONE

L'idea è blindata, priva di contraddizioni e validata dagli stress-test. Viene attivata la **Funzione IV (Scrittore)** per espandere il distillato logico nella sua forma finale (articolo, codice, report, saggio), garantendo la massima qualità espressiva senza il rischio di allucinazioni strutturali.