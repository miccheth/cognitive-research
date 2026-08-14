***Versione:** 1.5
***Data:** Agosto 2026*
***Stato:** Bozza*

***Nota:** il nome **Elevia** è provvisorio e verrà sostituito, poiché non disponibile.*

***Nota:** sto valutando se trasformarlo in un paper collaborativo. Servirà una struttura decisionale (es. ad albero) e tool gestionali per organizzare i contributi senza disperdere le idee migliori.*


# 1. Manifesto
___
## 1.1 Il Motivo

Nel lavoro intellettuale e nella ricerca l'intralcio principale è sempre lo stesso: accorgersi troppo tardi di una connessione decisiva o di un metodo migliore.

Non è una colpa individuale, ma un vincolo biologico: la memoria di lavoro gestisce pochissimi elementi alla volta e, quando il cervello è costretto a trattenere a fatica i dettagli, l'energia mentale si esaurisce nel lavoro meccanico.

Lo scopo di questo progetto non è rendere gli umani pigri o dipendenti dalla tecnologia, ma **liberare risorse mentali per ridare energia a quelle funzioni cognitive superiori che ci rendono superiori alle macchine.**

Non serve un semplice archivio, ma un'architettura di supporto che si adatti al flusso di ragionamento umano per potenziarlo, anziché sostituirlo.

## 1.2 Visione

L'evoluzione umana si basa sulla capacità di **modellare la realtà in modo astratto** e ricavare nuove opzioni dalle informazioni. Oggi, però, la quantità di dati disponibili supera i limiti biologici di memoria e attenzione: occorre uno strumento che estenda la portata della mente invece di sostituirla.

Rappresentando la conoscenza come una rete, la mente riesce a esplorarne solo pochi nodi per volta. Rendere visibili le connessioni latenti significa offrire una mappa completa per riconoscere pattern, testare ipotesi e governare sistemi complessi senza disperdere la concentrazione.

## 1.3 I principi

1. **Amplificare, non sostituire:** la tecnologia si fa carico del lavoro mnemonico e meccanico per liberare la mente umana, lasciando alle persone il controllo, l'intuizione e la visione d'insieme. **Human in the Loop** sempre.

2. **Architettura esplorabile:** i dati non vengono solo conservati, ma organizzati per essere navigati e messi in relazione.

3. **Aderenza ai processi mentali:** lo strumento si adatta alla logica dell'utente, riducendo la frizione tra il pensiero e la sua esecuzione.

4. **Precisione contestuale:** il sistema deve interpretare il significato reale delle informazioni, gestendo la complessità e il contesto del linguaggio senza appiattirli.

___


# 2. Space
___
## 2.1 Introduzione

**Space** è lo stato rappresentazionale della conoscenza: uno spazio strutturato e composizionale basato sugli **Atomi**, attraverso cui è possibile rappresentare entità, concetti, relazioni e valori. Nasce dall'idea di avvicinare la rappresentazione della conoscenza alla **struttura ricorsiva del pensiero umano**, puntando a una **Completezza Espressiva** paragonabile a quella del linguaggio naturale, ma per la conoscenza. Creando un sistema Simbolico-Probabilistico.

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

## 2.2 Omnispace

Ogni file **Space** contiene una porzione della conoscenza rappresentata dal sistema. Più file Space possono essere raccolti e compilati congiuntamente per costruire un unico **Omnispace**, nel quale la conoscenza complessiva viene analizzata e organizzata.

Durante questa fase, verranno costruite progressivamente le **associazioni, i pattern e le strutture semantiche** che emergono dall'insieme della conoscenza.

## 2.3 Language

### Query Engine

È il linguaggio di interfacciamento con Omnispace. A differenza dei linguaggi procedurali tradizionali come SQL, si basa interamente sulla definizione di vincoli di contesto (maschere) per delimitare lo spazio di esplorazione. Devono essere Espressivamente Completi per poter esplorare qualsiasi cosa. Con la possibilità di generalizzare nuove idee.

Le query funzionano attraverso l'interpretazione del linguaggio naturale e la mappatura iniziale:

1. **Interpreta la query:** Un LLM integrato comprende la frase dell'utente, ne estrae le parole chiave e i vincoli.

2. **Individuazione dei nodi seed:** Il sistema legge l'indice semantico, trova corrispondenza e cerca i nodi _seed_ (punti di partenza).

___


# 3. Pipeline
___
## 3.1 Ingestion Layer

**Ingestion costruisce la conoscenza.**

Il pensiero umano è fluido e articolato attraverso linguaggi eterogenei. Questo strato si occupa di trasformare il linguaggio non strutturato in **conoscenza strutturata**, assimilando informazioni provenienti da fonti esterne come manuali, articoli scientifici e note.

La conoscenza estratta viene quindi trasformata, manualmente o tramite processi automatizzati, in file **Space** pronti per la compilazione.

Nel processo automatizzato, sarà necessario utilizzare modelli in grado di considerare il **contesto complessivo del testo**, preservandone relazioni, sfumature e informazioni rilevanti.

## 3.2 Compilation Layer

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

## 3.3 Session Layer

Il **Session Layer** è la fase in cui gli Space già compilati vengono caricati per generare un'**istanza attiva di Omnispace**, rendendo la conoscenza disponibile per l'interazione e l'esplorazione.

- **Cono di Luce:** rappresenta il **focus attivo dell'utente**. Il nodo _seed_ costituisce il punto centrale dell'attenzione e determina il riferimento attuale, che varia dinamicamente in base all'attenzione dell'utente. Il vincolo di contesto agisce come un **"Cono di Luce" focalizzato**, definendo l'area di osservazione attiva.
    _Esempio:_ selezionando `Maranello`, il nodo `Maranello` diventa il _seed_ e il Cono di Luce definisce il nuovo focus dell'esplorazione.

- **Campo Gravitazionale:** a partire dal focus definito dal Cono di Luce, il sistema ricalcola la **gravità degli Atomi**. La gravità rappresenta il peso relativo di ciascun Atomo nel nuovo campo, determinato dalle sue relazioni e dalla sua rilevanza rispetto al focus. Viene ricalcolato dagli Embedding originale, e questo campo si resetta ad ogni nuova sessione.
    _Esempio:_ con `Maranello` come seed, `Ferrari` potrebbe assumere una gravità elevata, mentre un Atomo non correlato potrebbe diventare molto più leggero.

- **Propagazione Energetica e Limite di Hop:** il nuovo campo gravitazionale determina il **paesaggio energetico** attraverso cui si propaga l'attivazione a partire dal _seed_. L'energia decade progressivamente durante la propagazione e viene influenzata dalla gravità degli Atomi attraversati. Un limite massimo di _hop_ determina la distanza massima raggiungibile, evitando un'espansione incontrollata dell'attivazione. Gli Atomi che superano una determinata _threshold_ vengono considerati attivi.  
    _Esempio:_ partendo da `Maranello`, `Ferrari` può ricevere una forte attivazione, mentre Atomi progressivamente più lontani o meno rilevanti ricevono un'attivazione inferiore.

Il **paesaggio energetico può far emergere naturalmente connessioni inattese**: relazioni inizialmente periferiche possono diventare progressivamente rilevanti quando il campo gravitazionale e la propagazione dell'attivazione le rendono accessibili.

## 3.4 Generation Layer

È lo strato che traduce l'esplorazione strutturata di Omnispace in **linguaggio naturale**.

Riceve in input la porzione di conoscenza attivata, i percorsi rilevanti e le relative metriche di rilevanza. Un **LLM** interpreta e sintetizza queste informazioni per generare una risposta coerente con il contesto dell'esplorazione, evidenziando le relazioni e i meccanismi emersi.

Se disponibili, possono essere inoltre utilizzati **riferimenti alle fonti originali** per fornire maggiore tracciabilità alla conoscenza espressa.

___


# Seek Higher Things
___
## L'idea di un network di conoscenza

Ogni utente può pubblicare il proprio **Space personale**, rappresentativo, ad esempio, delle proprie conoscenze ed esperienze, rendendolo consultabile dagli altri utenti che scelgono di condividerlo. Gli Space possono quindi essere utilizzati anche in **modalità collaborativa**

- **Limite Funzionale — Embodied Experience:** questa visione incontra il limite delle **esperienze incarnate**, che per loro natura non possono essere digitalizzate o trasferite integralmente nel sistema.
- **Selezione delle Fonti:** ogni utente decide autonomamente quali fonti importare nel proprio Space, mantenendo il controllo sulla conoscenza che intende integrare e condividere.
- **Obiettivo Finale:** sviluppare una piattaforma aperta per la **condivisione e costruzione collaborativa della conoscenza**, orientata all'apprendimento, all'auto-potenziamento e alla crescita personale.

## Pattern Matching

In futuro, **Space** potrà supportare le **Variabili**, utilizzate per costruire pattern — cioè Expression contenenti elementi non specificati — che possono essere confrontati con altre strutture dello Space per determinare le corrispondenze delle variabili.

_Esempio:_ `(Parent $x $y)` può corrispondere a `(Parent Marco Luca)`, producendo il binding `$x = Marco` e `$y = Luca`.

Il **Pattern Matching** dovrà essere progettato tenendo conto della natura potenzialmente vaga e sfumata della conoscenza: le regole troppo generiche rischiano di produrre corrispondenze e inferenze poco significative. Potrebbe quindi essere necessario introdurre successivamente **Type e vincoli semantici** per rendere le corrispondenze più precise.

**Meccanismi di inferenza:** le possibilità di inferenza sono molteplici e non devono essere necessariamente imposte dal sistema. L'utente potrà definire o selezionare i propri meccanismi, tra cui **deduzione, induzione, abduzione, analogia, ragionamento controfattuale e inferenza non monotona**, oltre a forme di ragionamento spazio-temporale e causale.

## Modellazione Avanzata della Conoscenza

Poiché vorremo rendere il linguaggio **Turing-completo**, il sistema offre un'estensibilità nativa per la creazione e l'esecuzione di strumenti analitici e cognitivi avanzati custom (es. _modelli decisionali, motori inferenziali, simulazioni_).

## Elevia come co-processore

Una strategia efficace consiste nell'utilizzare **Elevia come co-processore** insieme agli LLM. Questo approccio integrato consente di:

- **Mitigare le allucinazioni:** verificare costantemente l'accuratezza e la coerenza delle risposte per ridurre gli errori causati dai modelli di linguaggio.
- **Validare la logica:** accertarsi che i modelli arrivino a conclusioni corrette e prive di fallacie formali.
- **Stimolare nuove intuizioni:** analizzare e correlare le informazioni per identificare insight rilevanti o scoperte inaspettate. E sfruttare la natura generativa degli LLM.

___


# Eureka
___
## Caso di studio: la Relatività Generale

Compilando una sessione di Omnispace contenente esclusivamente la conoscenza disponibile **prima di Einstein**, è possibile far emergere le stesse tensioni concettuali — relatività, gravità, equivalenza e geometria dello spazio-tempo — che portarono Einstein verso la Relatività Generale? Il cervello umano come lo farebbe?

## Caso di studio: Propagazione a 100 Hop

Un sistema che propaga attivazione attraverso 100 hop di relazioni può raggiungere le stesse conclusioni a cui arriva un umano per intuizione? Il cervello umano collega concetti distanti in pochi salti associativi: verificare se la propagazione energetica su larga scala (100 hop) fa emergere insight comparabili al ragionamento umano indiretto, o se produce solo rumore semantico.

___


# Examples
___
1. [[Esempio Omnispace 1 Elevia_1]||Esempio Omnispace - Elevia v1.0]]

___


# I problemi da gestire
____

1. Ottimizzazione GPU: navigazione scatole annidate salta tra memoria non-contigua, distrugge cache efficiency. Soluzione: compilare Metagrafo in GPU trasformando Atomi in oggetti 3D+ con coordinate (simile Topologia Algebrica/Complessi Simpliciali).
2. Memoria olografica HDC: imita ragionamento umano per associazione e similarità, generalizza elementi vicini nell'userspace senza cambiare semantica di base. Da decidere: fondere HDC con ReRanking/Embedding o tenerli separati.
3. Tipi: da definire se servono (nel cervello umano forse non esistono). Il contesto va gestito (es. Panca vs Panca Piana sono diversi), forse i Tipi risolvono.
4. LLM e RAG: rimuovere linguaggio gergale/oscurantista. RAG puro sbaglia spesso (es. Gemini). Meglio RAG con fonte originale accoppiata a LLM che arricchisce generazione. Problema: estrarre conoscenza utile da ore di video (come fa il cervello?).
5. Comunicazione umana: basata su parole, concetti astratti, grammatica complessa, condivisione passato/futuro. Metagrafo deve essere tutto astratto. Supporto multimodale necessario.
6. Problema: come fa l'utente a ricordare la struttura esatta quando scrive una query? L'auto-completamento basato sulla struttura esistente aiuta ma rischia di rendere il linguaggio rigido, perdendo la flessibilità del pensiero umano. L'ordine degli atomi è lineare (sinistra-destra, esterno-interno) come un computer, ma la mente umana non pensa in modo sequenziale. Tensione da risolvere: struttura computazionale precisa vs espressività cognitiva libera. Possibili soluzioni: query per pattern (ordine non conta), auto-completamento contestuale (suggerisce ma non impone), o atomi named (parametri con nome così la posizione è irrilevante).
7. Struttura minima: Space fornisce una radice essenziale lasciando all'utente la personalizzazione (è pure utopia rappresentare tutto il pensiero umano le sue caratteristiche, perchè sono generativi e non pre programmate) (verità soggettiva, logica non-monotona, saggezza della folla, programmazione propria).
8. Memoria e apprendimento umano: il cervello non impara tutto ma estrae parole chiave che impattano la traiettoria cognitiva, con micro-sfumature che modificano gradualmente lo schema cerebrale. Space deve essere Turing-Completo come il cervello.
9. Ma l utente come capisce nell caos gigantesco del metagrafo? Da capire anche per discorso query, magari si autocompleta
10. Apprendimento e estrazione conoscenza: il cervello umano non memorizza tutto ma estrae parole chiave che impattano la traiettoria cognitiva, accumulando micro-sfumature che modificano gradualmente lo schema cerebrale trovando un baricentro di verità. Il Metagrafo non deve rappresentare ogni sfumatura del linguaggio umano (impresa utopica), ma fornire una struttura minima essenziale. Per le query complesse (es. mostrami un film con queste caratteristiche) e la generazione di risposte, usare RAG accoppiato a LLM con fonte originale: il RAG arricchisce il testo finale ma non gestisce da solo la semantica profonda. Problema aperto: come estrarre conoscenza utile da grandi moli di dati (es. 1 ora di video) scartando il superfluo, imitando il cervello che conserva solo ciò che serve. Le variabili stile RAG vanno definite nel loro utilizzo pratico. Forse questa parte neurale/statistica non si fonde completamente con il Metagrafo simbolico: i due approcci potrebbero essere complementari per rispettare la complessità del pensiero umano senza sovraccaricare la struttura centrale.

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
