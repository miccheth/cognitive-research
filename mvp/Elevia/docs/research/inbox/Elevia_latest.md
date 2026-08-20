***Versione:** 1.5
***Data:** Agosto 2026*
***Stato:** Bozza*

***Nota:** il nome **Elevia** è provvisorio e verrà sostituito, poiché non disponibile.*

***Nota:** sto valutando se trasformarlo in un paper collaborativo. Servirà una struttura decisionale (es. ad albero) e tool gestionali per organizzare i contributi senza disperdere le idee migliori.*


# 1. Manifesto
___
## 1.1 Il Motivo

Nel lavoro intellettuale e nella ricerca l'intralcio principale è sempre lo stesso: **la mancanza di una visione d'insieme** che fa accorgersi troppo tardi di una connessione decisiva o di un metodo migliore.

Non è una colpa individuale, ma un vincolo biologico: la memoria di lavoro può gestire solo pochi elementi alla volta e, quando il cervello è costretto a trattenere a fatica troppi dettagli, **perde di vista il quadro generale**, mentre una parte consistente delle risorse cognitive viene assorbita dal semplice mantenimento delle informazioni.

Viviamo in un’epoca caratterizzata da ritmi sempre più veloci e da un flusso continuo di informazioni, ma il cervello umano non è strutturato per gestire senza limiti una mole così elevata di dati.

Lo scopo di questo progetto non è rendere gli umani pigri o dipendenti dalla tecnologia, ma **liberare risorse mentali per ridare energia a quelle funzioni cognitive superiori che ci hanno permesso di costruire la nostra civiltà**. L'uomo ha sempre progredito attraverso strumenti capaci di amplificare le proprie capacità: la scrittura ha esteso la memoria, il calcolo ha esteso la capacità di elaborazione, gli strumenti scientifici hanno esteso i sensi. Non serve quindi un semplice archivio, ma un'architettura di supporto che si adatti al flusso di ragionamento umano per **potenziarlo, anziché sostituirlo**.

## 1.2 Visione

L'evoluzione umana si basa sulla capacità di **modellare la realtà in modo astratto simbolico** e ricavare nuove opzioni dalle informazioni. La nostra storia è anche una storia di strumenti che hanno progressivamente esteso ciò che la mente e il corpo potevano fare; oggi, però, la quantità di dati disponibili supera i limiti biologici di memoria e attenzione: occorre uno strumento che **estenda la portata della mente senza sostituirla**.

Rappresentando la conoscenza come una rete, la mente riesce a esplorarne solo pochi nodi per volta. Rendere visibili le connessioni latenti significa offrire una mappa completa per riconoscere pattern, testare ipotesi e governare sistemi complessi senza disperdere la concentrazione. **Come ogni grande strumento della storia umana, il suo ruolo non è pensare al posto dell'uomo, ma permettergli di pensare oltre i propri limiti biologici.**

## 1.3 I principi

1. **Amplificare, non sostituire:** la tecnologia deve farsi carico del lavoro mnemonico e meccanico per liberare la mente umana, non per sollevarla dal compito di pensare. Deve lasciare alle persone il controllo, l’intuizione, il pensiero critico e la capacità di avere una visione d’insieme. Dobbiamo usare la tecnologia per diventare più capaci, **non per disimparare a pensare e diventare cognitivamente dipendenti da essa**. **Human in the Loop, sempre.**

2. **Architettura esplorabile:** i dati non vengono solo conservati, ma organizzati per essere navigati e messi in relazione.

3. **Aderenza ai processi mentali:** lo strumento si adatta alla logica dell'utente, riducendo la frizione tra il pensiero e la sua esecuzione.

4. **Precisione contestuale:** il sistema deve interpretare il significato reale delle informazioni, gestendo la complessità e il contesto del linguaggio senza appiattirli.

## 1.4 Divisione dei Ruoli

| La macchina si occupa di        | L'essere umano decide                 |
| ------------------------------- | ------------------------------------- |
| Ricordare                       | Cosa è importante                     |
| Indicizzare                     | Cosa è vero                           |
| Collegare                       | Quale ipotesi vale la pena perseguire |
| Cercare                         | Quale connessione è significativa     |
| Raggruppare                     | Quale interpretazione adottare        |
| Evidenziare                     | Cosa fare                             |
| Recuperare contesti             | —                                     |
| Mostrare connessioni            | —                                     |
| Individuare possibili relazioni | —                                     |

## 1.5 Roadmap

1. **Rappresentazione Universale:** normalizzare qualsiasi input umano (paper, commento Reddit, dataset) in Space. Quindi aver risolto il problema delle infinite sfumature del linguaggio umano, unificandolo con i simboli rigidi. Se due fonti condividono semantica, emergono vicine. (es. come vedremmo un commento Reddit e un paper scientifico, pertinenti dello stesso argomento)

2. **Estrazione Regole:** dall'esplorazione delle connessioni, cristallizzare nuove regole logiche (es. se impara che l'acqua bolle a 100°C e diventa ghiaccio a 0°C, si genera una regola). Definizione: manuale (utente) o automatica (sistema propone).

___


# 2. Il Grande Dilemma
___
## 2.1 Il problema: precisione contro continuità

Come costruire una memoria computazionale che sia sufficientemente **precisa e strutturata** da funzionare come un sistema simbolico, ma anche capace di rappresentare la **continuità, la vaghezza e le sfumature del linguaggio naturale**?

Un sistema puramente **simbolico** rappresenta molto bene i fatti espliciti:

```text
Apple Inc.
    ↓
è una
    ↓
azienda
```

È efficace per entità, relazioni, gerarchie e vincoli, ma diventa rigido quando deve rappresentare concetti sfumati o connessioni non esplicitamente definite.

Un sistema puramente **vettoriale**, al contrario, rappresenta bene la similarità semantica:

```text
"Apple sta spostando l'iPhone verso la fascia premium"
                ↕
"Le aziende mature cercano segmenti ad alto margine"
```

Ma la similarità non equivale a una relazione logica:

```text
A è simile a B
```

non significa:

```text
A → è → B
```

Il problema, quindi, non è scegliere tra i due approcci, ma **farli convivere senza confonderne i ruoli**.

> **Il simbolico garantisce precisione e struttura; il vettoriale garantisce continuità e capacità di scoperta.**

## 2.2 Due livelli di conoscenza

La memoria può essere organizzata su due livelli complementari.

### Livello simbolico

Rappresenta ciò che il sistema considera sufficientemente definito da poter essere espresso esplicitamente:

```text
Apple Inc. → tipo → Azienda
Apple Inc. → produce → iPhone
Steve Jobs → tipo → Persona
Steve Jobs → ha guidato → Apple Inc.
```

Questo livello permette: identificazione e disambiguazione delle entità, relazioni e gerarchie, filtri e aggregazioni, interrogazioni precise, vincoli e ragionamento. 

### Livello vettoriale

Rappresenta invece la **posizione semantica** delle informazioni nello spazio concettuale.

Permette di individuare somiglianze e connessioni che non erano state definite esplicitamente.

Una rappresentazione vettoriale, quindi, non afferma necessariamente che due informazioni siano equivalenti o logicamente collegate. Indica soltanto che **potrebbero appartenere allo stesso spazio concettuale**.

## 2.3 L'ancoraggio simbolico

Il punto centrale dell'architettura è che le rappresentazioni vettoriali non devono necessariamente diventare nuove strutture simboliche.

Un'entità o un concetto simbolico può fungere da **punto di ancoraggio comune** per molte rappresentazioni vettoriali.

In questo senso, il simbolo funziona come un baricentro:

```text
              S1
              │
              │
        S2 ─── ● ─── S3
              │
              │
              S4

              ●
         Apple Inc.
```

Le diverse informazioni possono quindi essere semanticamente vicine, pur mantenendo la propria individualità.

Questo consente di conservare la ricchezza semantica senza trasformare ogni sfumatura del linguaggio in una nuova relazione del grafo.

La memoria non deve formalizzare tutto ciò che comprende.

## 2.4 Diversi tipi di conoscenza e certezza

Non tutte le informazioni hanno lo stesso grado di certezza o devono essere rappresentate nello stesso modo.

Per esempio:

```text
"Apple è un'azienda tecnologica."
```

può essere rappresentato come un fatto strutturato.

Al contrario:

```text
"Apple sembra aver perso parte della sua capacità innovativa."
```

esprime una valutazione, mentre:

```text
"Questo testo ricorda concettualmente quest'altro."
```

esprime una relazione di similarità.

Queste tre informazioni non dovrebbero essere forzate nella stessa struttura.

La memoria deve quindi distinguere almeno tra:

- **fatti strutturati**;
- **valutazioni o affermazioni incerte**;
- **relazioni semantiche e similarità**.

> **Non serve una rappresentazione universale della conoscenza. Serve una memoria capace di rappresentare diversi tipi di certezza e relazione.**

## 2.5 La granularità della conoscenza

Consideriamo:

> «Negli ultimi anni Apple ha aumentato il prezzo degli iPhone. Alcuni utenti ritengono che l'azienda punti sempre più sul mercato premium e che, rispetto all'epoca di Steve Jobs, abbia perso parte della sua capacità innovativa.»

Il sistema non dovrebbe trasformare l'intero testo in una gigantesca struttura logica.

Può estrarre ciò che è utile rendere esplicito:

```text
Apple Inc.
iPhone
Steve Jobs

Apple Inc. ── produce ──> iPhone
Steve Jobs ── ha guidato ──> Apple Inc.
```

La valutazione sulla capacità innovativa, invece, può rimanere nella rappresentazione vettoriale.

Non avrebbe senso trasformare:

> "ha perso parte della sua capacità innovativa"

in decine di nodi e relazioni.

La segmentazione deve seguire la struttura simbolica estratta dal contenuto: a ogni insieme coerente di simboli può corrispondere una rappresentazione vettoriale distinta. Creare un unico vettore per un testo di mille righe comprimerebbe informazioni troppo diverse, facendo perdere granularità e precisione nei collegamenti semantici.

## 2.6 Scoprire connessioni senza trasformarle in fatti

Supponiamo che, mesi dopo, venga inserito:

> «Le aziende tecnologiche mature possono aumentare i margini concentrandosi su prodotti premium, anche quando la crescita delle vendite rallenta.»

Il sistema può rappresentare questo contenuto come un nuovo segmento semantico:

```text
S4 → vector_087
```

e rilevare una forte similarità con:

```text
S2
"Apple punta sempre più sul mercato premium."
```

La similarità può quindi produrre:

```text
S4
 ↓
potenzialmente correlato a
 ↓
S2
 ↓
Apple Inc.
```

Ma **non deve modificare automaticamente il grafo**.

Non deve creare:

```text
Apple Inc. ── segue strategia ──> aumentare i margini
```

perché questa sarebbe un'inferenza ulteriore, non direttamente giustificata dai dati.

Il sistema deve quindi distinguere tra:

> **ciò che sa, ciò che rappresenta come ipotesi e ciò che considera semanticamente correlato.**

___


# 3. Space
___
## 3.1 Introduzione

**Space** è lo stato rappresentazionale della conoscenza: uno spazio strutturato e composizionale basato sugli **Atomi**, attraverso cui è possibile rappresentare entità, concetti, relazioni e valori. Nasce dall'idea di avvicinare la rappresentazione della conoscenza alla **struttura ricorsiva del pensiero umano**, puntando a una **Completezza Espressiva** paragonabile a quella del linguaggio naturale. Creando un sistema Simbolico-Probabilistico.

È una **struttura minima**: tutto emerge dalla personalizzazione dell'utente. Come il pensiero umano, è **generativo** — funzioni complesse derivano da una base semplice, creando cose potenziale come: **verità soggettiva**, **logica non-monotona**, **saggezza della folla** e **programmazione propria**. Oppure forme illimitati di inferenza come **deduzione, induzione, abduzione, analogia, ragionamento controfattuale e inferenza non monotona**.

Un **Atomo** è l'unità fondamentale della conoscenza. Può essere utilizzato singolarmente oppure combinato con altri Atomi per costruire strutture più complesse.

### Tipi di Atomi

- **Symbol:** rappresenta un'entità, un concetto o una relazione. Due Symbol con lo stesso nome rappresentano lo stesso elemento.  
    _Esempi:_ `Marco`, `Parma`, `persona`, `viveIn`.

- **Expression:** combina Atomi, incluse altre Expression, permettendo di costruire strutture annidabili. *Esempio:* `(viveIn Marco Parma)`.
	 *Esempio di annidamento progressivo:* 
	- `(Caffeina Aumenta Adrenalina)` 
	- `(PaperX Dimostra (Caffeina Aumenta Adrenalina))`
	- `(Istruttore Contesta (PaperX Dimostra (Caffeina Aumenta Adrenalina)))`

- **Primitive:** valori concreti e codici eseguibili (numeri, stringhe, funzioni o logiche esterne) che non necessitano di un'ancora semantica astratta. Rappresentano dati reali, collezioni o operazioni matematiche valutate direttamente dal runtime o da estensioni esterne.  
	_Esempi:_ `42`, `3.14`, `"ciao"`, `True`, `+` (funzione per l'operazione di somma).

Questa struttura permette di rappresentare conoscenza arbitrariamente complessa mantenendo una **forma unica e composizionale**.

Space non impone un'ontologia o una semantica specifica: rappresenta la conoscenza in forma esplicita, sulla quale i successivi processi di compilazione possono costruire rappresentazioni più ricche e ottimizzate.

## 3.2 Omnispace

Ogni file **Space** contiene una porzione della conoscenza rappresentata dal sistema. Più file Space possono essere raccolti e compilati congiuntamente per costruire un unico **Omnispace**, nel quale la conoscenza complessiva viene analizzata e organizzata.

Durante questa fase, verranno costruite progressivamente le **associazioni, i pattern e le strutture semantiche** che emergono dall'insieme della conoscenza.

## 3.3 Language

### Query Engine

È il linguaggio di interfacciamento con Omnispace. A differenza dei linguaggi procedurali tradizionali come SQL, si basa interamente sulla definizione di vincoli di contesto (maschere) per delimitare lo spazio di esplorazione (similmente alle String Regex). Devono essere Espressivamente Completi per poter esplorare qualsiasi cosa. Con la possibilità di generalizzare nuove idee.

Le query funzionano attraverso l'interpretazione del linguaggio naturale e la mappatura iniziale:

1. **Interpreta la query:** Un LLM integrato comprende la frase dell'utente, ne estrae le parole chiave e i vincoli.

2. **Individuazione dei nodi seed:** Il sistema legge l'indice semantico, trova corrispondenza e cerca i nodi _seed_ (punti di partenza).

___


# 4. Pipeline
___
## 4.1 Ingestion Layer

**Ingestion costruisce la conoscenza.**

Il pensiero umano è fluido e articolato attraverso linguaggi eterogenei. Questo strato si occupa di trasformare il linguaggio non strutturato in **conoscenza strutturata**, assimilando informazioni provenienti da fonti esterne come manuali, articoli scientifici e note.

La conoscenza estratta viene quindi trasformata, manualmente o tramite processi automatizzati, in file **Space** pronti per la compilazione.

Nel processo automatizzato, sarà necessario utilizzare modelli in grado di considerare il **contesto complessivo del testo**, preservandone relazioni, sfumature e informazioni rilevanti.

La fonte originale non viene mantenuta, ma viene completamente trasformata, mantenendo i metadati.

## 4.2 Compilation Layer

**La Compilation analizza e organizza la struttura della conoscenza.**

La Compilation non deve inventare nuova conoscenza, ma **analizzare, collegare e organizzare quella già presente nello Space**, producendo le strutture necessarie alla costruzione di Omnispace. Ha anche un puntatore di contesto perchè Banca in base al contesto, ha un significato diverso.

Ai fini per mantenere ordine, è consigliabile avere un singolo Space per ogni singola fonte.

- **Syntax Check:** verifica che ogni Space sia formalmente valido secondo la grammatica prevista, controllando la struttura delle Expression, la corretta composizione degli Atomi e la validità della sintassi. In caso di errore, la compilazione viene interrotta. Se tutto corretto, comincia a creare alberi di espressione per ciascun Space.
    _Esempio:_ `(livesIn Marco Rome)` → valido; `(livesIn Marco` → errore di sintassi.
    
- **Canonical Grounding:** verifica che la rappresentazione rispetti le regole canoniche dello Space. La normalizzazione riguarda principalmente termini concettuali e relazionali, mentre nomi propri, valori e identificativi vengono mantenuti invariati. Il compilatore può utilizzare **mappe lessicali preinstallate** (solo in Inglese come Pivot, vale per ogni scritta testuale scritta sullo Space) come riferimento per la normalizzazione. Vanno importati le mappe lessicali per ogni Space.
    _Esempio:_ `viveIn` → `livesIn`, mentre `Marco` rimane `Marco`.
    
- **Semantic Atom Resolution:** utilizza le mappe lessicali e le relazioni presenti nello Space per individuare quando **Symbol differenti possono rappresentare lo stesso concetto**, distinguendo però tra equivalenza linguistica e relazioni concettuali.  
    _Esempio:_ `livesIn` e `residesIn` → possibile corrispondenza semantica; `Water` e `H2O` → stesso referente, ma rappresentazioni differenti. Rispetto all'equivalenza `Water` -> `Acqua`

- **Indexing:** costruisce indici sulle strutture presenti nello Space, collegando gli Atomi alle Expression in cui compaiono. Questo permette di organizzare la conoscenza e navigare rapidamente tra entità, concetti e relazioni.
    _Esempio:_ `(livesIn Marco Rome)` e `(person Marco)` → `Marco → [livesIn Marco Rome, person Marco]`.

- **Robustezza al Rumore (Noise Tolerance):** capacità del compilatore di riconoscere che espressioni con variazioni sintattiche, d'ordine o di lingua esprimono la stessa informazione semantica, riconducendole a un'unica rappresentazione canonica. _Esempio:_ `(livesIn Marco Rome)`, `(livesIn Marco Roma)` _(rumore di lingua)_ e `(Marco livesIn Rome)` _(rumore di struttura/sintassi)_ dicono tutti la stessa cosa e vengono risolti nella medesima struttura semantica.

## 4.3 Session Layer

Il **Session Layer** è la fase in cui gli Space già compilati vengono caricati per generare un'**istanza attiva di Omnispace**, rendendo la conoscenza disponibile per l'interazione e l'esplorazione.

- **Cono di Luce:** rappresenta il **focus attivo dell'utente**. Il nodo _seed_ costituisce il punto centrale dell'attenzione e determina il riferimento attuale, che varia dinamicamente in base all'attenzione dell'utente. Il vincolo di contesto agisce come un **"Cono di Luce" focalizzato**, definendo l'area di osservazione attiva.
    _Esempio:_ selezionando `Maranello`, il nodo `Maranello` diventa il _seed_ e il Cono di Luce definisce il nuovo focus dell'esplorazione.

- **Campo Gravitazionale:** a partire dal focus definito dal Cono di Luce, il sistema ricalcola la **gravità degli Atomi**. La gravità rappresenta il peso relativo di ciascun Atomo nel nuovo campo, determinato dalle sue relazioni e dalla sua rilevanza rispetto al focus. Viene ricalcolato dagli Embedding originale, e questo campo si resetta ad ogni nuova sessione.
    _Esempio:_ con `Maranello` come seed, `Ferrari` potrebbe assumere una gravità elevata, mentre un Atomo non correlato potrebbe diventare molto più leggero.

- **Propagazione Energetica e Limite di Hop:** il nuovo campo gravitazionale determina il **paesaggio energetico** attraverso cui si propaga l'attivazione a partire dal _seed_. L'energia decade progressivamente durante la propagazione e viene influenzata dalla gravità degli Atomi attraversati. Un limite massimo di _hop_ determina la distanza massima raggiungibile, evitando un'espansione incontrollata dell'attivazione. Gli Atomi che superano una determinata _threshold_ vengono considerati attivi.  
    _Esempio:_ partendo da `Maranello`, `Ferrari` può ricevere una forte attivazione, mentre Atomi progressivamente più lontani o meno rilevanti ricevono un'attivazione inferiore.

Il **paesaggio energetico può far emergere naturalmente connessioni inattese**: relazioni inizialmente periferiche possono diventare progressivamente rilevanti quando il campo gravitazionale e la propagazione dell'attivazione le rendono accessibili.

## 4.4 Generation Layer

È lo strato che traduce l'esplorazione strutturata di Omnispace in **linguaggio naturale**.

Riceve in input la porzione di conoscenza attivata, i percorsi rilevanti e le relative metriche di rilevanza. Un **LLM** interpreta e sintetizza queste informazioni per generare una risposta coerente con il contesto dell'esplorazione, evidenziando le relazioni e i meccanismi emersi.

Se disponibili, possono essere inoltre utilizzati **riferimenti alle fonti originali** per fornire maggiore tracciabilità alla conoscenza espressa.

___


# 5. Seek Higher Things
___
## 5.1 L'idea di un network di conoscenza

Ogni utente può pubblicare il proprio **Space personale**, rappresentativo, ad esempio, delle proprie conoscenze ed esperienze, rendendolo consultabile dagli altri utenti che scelgono di condividerlo. Gli Space possono quindi essere utilizzati anche in **modalità collaborativa**

- **Limite Funzionale — Embodied Experience:** questa visione incontra il limite delle **esperienze incarnate**, che per loro natura non possono essere digitalizzate o trasferite integralmente nel sistema.
- **Selezione delle Fonti:** ogni utente decide autonomamente quali fonti importare nel proprio Space, mantenendo il controllo sulla conoscenza che intende integrare e condividere.
- **Obiettivo Finale:** sviluppare una piattaforma aperta per la **condivisione e costruzione collaborativa della conoscenza**, orientata all'apprendimento, all'auto-potenziamento e alla crescita personale.

## 5.2 Pattern Matching

In futuro, **Space** potrà supportare le **Variabili**, utilizzate per costruire pattern — cioè Expression contenenti elementi non specificati — che possono essere confrontati con altre strutture dello Space per determinare le corrispondenze delle variabili.

_Esempio:_ `(Parent $x $y)` può corrispondere a `(Parent Marco Luca)`, producendo il binding `$x = Marco` e `$y = Luca`.

Il **Pattern Matching** dovrà essere progettato tenendo conto della natura potenzialmente vaga e sfumata della conoscenza: le regole troppo generiche rischiano di produrre corrispondenze e inferenze poco significative. Potrebbe quindi essere necessario introdurre successivamente **Type e vincoli semantici** per rendere le corrispondenze più precise. Dando la possibilità di creare conoscenza nuova derivata.

## 5.3 Modellazione Avanzata della Conoscenza

Poiché vorremo rendere il linguaggio **Turing-completo**, il sistema offre un'estensibilità nativa per la creazione e l'esecuzione di strumenti analitici e cognitivi avanzati custom (es. _modelli decisionali, motori inferenziali, simulazioni_).

Dando la possibilità di Variabili Grounded a dati provenienti da altre fonti (datset, API, stream file, ecc)

## 5.4 Elevia come co-processore

Una strategia efficace consiste nell'utilizzare **Elevia come co-processore** insieme agli LLM. Questo approccio integrato consente di:

- **Mitigare le allucinazioni:** verificare costantemente l'accuratezza e la coerenza delle risposte per ridurre gli errori causati dai modelli di linguaggio.
- **Validare la logica:** accertarsi che i modelli arrivino a conclusioni corrette e prive di fallacie formali.
- **Stimolare nuove intuizioni:** analizzare e correlare le informazioni per identificare insight rilevanti o scoperte inaspettate. E sfruttare la natura generativa degli LLM.

## 5.5 Supporto Multimodale

___


# 6. Eureka
___
## 6.1 Caso di studio: la Relatività Generale

Compilando una sessione di Omnispace contenente esclusivamente la conoscenza disponibile **prima di Einstein**, è possibile far emergere le stesse tensioni concettuali — relatività, gravità, equivalenza e geometria dello spazio-tempo — che portarono Einstein verso la Relatività Generale? Il cervello umano come lo farebbe?

## 6.2 Caso di studio: Propagazione a 100 Hop

Un sistema che propaga attivazione attraverso 100 hop di relazioni può raggiungere le stesse conclusioni a cui arriva un umano per intuizione? Il cervello umano collega concetti distanti in pochi salti associativi: verificare se la propagazione energetica su larga scala (100 hop) fa emergere insight comparabili al ragionamento umano indiretto, o se produce solo rumore semantico.

## 6.3 Caso di studio: Correlazione Evento-Dati Finanziari

Caricando in Omnispace:
- **Space A:** notizia finanziaria (es. "Banca X dichiara fallimento", data, attori)
- **Space B:** dati di mercato (prezzi, volumi, indici, stesse date/attori)

**Domanda:** il sistema vede nativamente la vicinanza?

**Cosa misurare:**
- Gli atomi ponte (nome banca, data) attivano propagazione tra i due Space?
- Quanti hop servono per collegare notizia → crollo prezzi?
- Emergono correlazioni non ovvie (effetto domino su settori correlati)?

**Successo:** il sistema mostra connessioni senza ontologia predefinita, solo tramite struttura Space e campo gravitazionale.

___


# 7. Examples
___
1. [[Esempio Omnispace 1 Elevia_1]]
2. [[Esempio Omnispace 2 Elevia_1_5]]

___


# 8. I problemi da gestire
____

1. Ottimizzazione GPU: navigazione scatole annidate salta tra memoria non-contigua, distrugge cache efficiency. Soluzione: compilare Metagrafo in GPU trasformando Atomi in oggetti 3D+ con coordinate (simile Topologia Algebrica/Complessi Simpliciali).
2. Memoria olografica HDC: imita ragionamento umano per associazione e similarità, generalizza elementi vicini nell'userspace senza cambiare semantica di base. Da decidere: fondere HDC con ReRanking/Embedding o tenerli separati. E arricchimento Contesto nel sistema per singolo simbolo arricchimento di vettori in contesti diversi, ma riferiti a quella entità.
3. LLM e RAG: rimuovere linguaggio gergale/oscurantista. RAG puro sbaglia spesso (es. Gemini). Meglio RAG con fonte originale accoppiata a LLM che arricchisce generazione. Problema: estrarre conoscenza utile da ore di video (come fa il cervello?).
4. Problema: come fa l'utente a ricordare la struttura esatta quando scrive una query? L'auto-completamento basato sulla struttura esistente aiuta ma rischia di rendere il linguaggio rigido, perdendo la flessibilità del pensiero umano. L'ordine degli atomi è lineare (sinistra-destra, esterno-interno) come un computer, ma la mente umana non pensa in modo sequenziale. Tensione da risolvere: struttura computazionale precisa vs espressività cognitiva libera. Possibili soluzioni: query per pattern (ordine non conta), auto-completamento contestuale (suggerisce ma non impone), o atomi named (parametri con nome così la posizione è irrilevante).
5. Memoria e apprendimento umano: il cervello non impara tutto ma estrae parole chiave che impattano la traiettoria cognitiva, con micro-sfumature che modificano gradualmente lo schema cerebrale. Space deve essere Turing-Completo come il cervello.
6. Ma l utente come capisce nell caos gigantesco del metagrafo? Da capire anche per discorso query, magari si autocompleta
7. Il problema sarà anche come sarà, se ci sarà disordine in un Omnispace di 100 GB. Forse il Focus è la chiave? il cono di luce? Forse con la legge dei Grandi numeri, filtriamo ciò che dice la stessa cosa statistica che si ripetete tra i tanti dati che dicono più o meno la stessa cosa. Forse fa così il cervello per imparare quando legge tante cose che dicono la stssa cosa più o meno.
8. Fare il modo di creare buoni vettori di qualità: strategie da usare ReRanker, oppure anche deve guardare tutto il contesto e altre.
9. Ci sono due possibilità: o in qualche modo trasformo le sfumature in simbolico, oppure le sfumature sono su un altro piano, e nel simbolico sono fatti strutturati entrano.
10. Basta imitare soltanto la Memoria Associativa? Penso che tutto: regole inferenza, deduzione, ecc. Deriva da quest'ultima, è solo che noi la chiamiamo deduzione, ma è un eco della memoria associativa, perchè ci sono più concetti attivi nella testa e quindi associamo. Non so se hai capito. Tipo esempio stavo parlando del mio piede che è cavo, ed ho associato nella mia testa con un ragionamento distante, e quindi nella mia testa si è attivato il concetto di supino, perchè l'arco plantare tende a supinare, e quindi nella mia testa si è ora avvicinato il concetto di mignolo vago. Questo meccanismo è la chiave. E funziona anche con cose indirette che hanno un filo conduttore. Questa è la generalizzazione.

___
*Riferimenti:*
- *[I1] [[Amplifica l'Essere Umano senza sostituirlo]]*
- *[I2] [[Il Problema delle Triplette Limitate]]*
- *[I3] [[I limiti umani]]*
- *[I4] [https://metta-lang.dev/](https://metta-lang.dev/)*
- *[I5] [[Post Reddit Spiegazione con Esempio Omnispace]]*
- *[I6] [https://www.nayuki.io/page/designing-better-file-organization-around-tags-not-hierarchies](https://www.nayuki.io/page/designing-better-file-organization-around-tags-not-hierarchies)*
- *[I7] [ https://karl-voit.at/managing-digital-photographs/](https://karl-voit.at/managing-digital-photographs/)*
- *[I8] [https://karl-voit.at/2022/01/29/How-to-Use-Tags/](https://karl-voit.at/2022/01/29/How-to-Use-Tags/)*
- *[I9] [[Uso degli HDC]]*
- *[I10] [[Attenzione come Convergenza Energetica Geometrica]]*

