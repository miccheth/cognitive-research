***Versione:** 1.0*  
***Data:** Agosto 2026*
***Stato:** Bozza*

***Nota:** il nome **Elevia** è provvisorio e verrà sostituito, poiché non disponibile.*


# Manifesto
---
## Il motivo di tutto questo

L'idea nasce da un'esperienza comune: durante lo studio di un argomento, scopriamo spesso solo a posteriori l'esistenza di approcci migliori o connessioni chiave che all'inizio erano introvabili. La conclusione è sempre la stessa: _«Se lo avessi saputo prima!»_.

Non si tratta necessariamente di una ricerca superficiale, ma dei limiti umani nella gestione della complessità. In una società che lascia poco tempo all'approfondimento, serve un acceleratore. Il vero problema non è la mancanza di conoscenza, ma la sua frammentazione: le informazioni esistono, ma restano isolate. La sfida è quindi creare uno spazio in cui la conoscenza possa connettersi, restituendo una visione d'insieme.

Dopo mesi di lavoro dedicati allo studio del cervello umano per imitarne i meccanismi — portati avanti in parallelo ad altri progetti — sono riuscito a unire le idee: il progetto indiretto, che propongo oggi, si avvicina in modo sorprendente al flusso del ragionamento umano.


## Visione

L’evoluzione umana si fonda sulla capacità di modellare la realtà e trasformare l'informazione in nuove possibilità. Oggi, tuttavia, la mole di dati supera i nostri limiti biologici di memoria e attenzione: serve uno strumento che amplifichi le capacità cognitive umane, anziché sostituirle.

Se immaginiamo la conoscenza come un grafo, il cervello ne esplora solo una frazione. Rendendo accessibili le connessioni nascoste, si offre una visione d'insieme per individuare pattern, formulare ipotesi e padroneggiare sistemi complessi in un ambiente d'interazione più profondo.


## Principi 

1. **Amplificare, non sostituire:** la tecnologia deve aumentare le capacità dell'essere umano senza eliminare il suo ruolo nel pensiero, nella creatività e nelle decisioni. 
2. **Centralità dell'essere umano (Human in the Loop):** il controllo, il giudizio e la responsabilità rimangono sempre umani. La tecnologia è uno strumento di potenziamento, non un sostituto dell'intelligenza umana. 
3. **Espansione della conoscenza:** la conoscenza non deve essere soltanto conservata, ma resa esplorabile, collegabile e trasformabile. 
4. **Sintonia cognitiva:** deve adattarsi al modo in cui l'essere umano comprende il mondo, diventando un'estensione naturale del processo di pensiero.

___


# Omnispace
---
## Introduzione

Per concretizzare la visione del manifesto, il progetto adotta **Omnispace**: un metagrafo spazio-universale della conoscenza. Progettato per rappresentare e manipolare concetti, relazioni, logica e processi in un'unica struttura Turing-completa, Omnispace offre una _Completezza Espressiva_ analoga a quella del linguaggio umano. Grazie all'omoiconicità, codice e dati condividono la stessa natura: il sistema applica la metaprogrammazione per descrivere, modificare ed estendere sé stesso all'interno dello stesso ambiente.

### Principi

- **Unità Atomica:** Ogni elemento della conoscenza è un _Atomo_. Dati, concetti, entità, relazioni, regole e comportamenti condividono la stessa natura fondamentale e differiscono solo per struttura e funzione.
- **Rappresentazione Unificata:** Tutta la conoscenza risiede nel medesimo spazio concettuale, superando la separazione tradizionale tra dati, logica e comportamento.
- **Evoluzione Progressiva:** Il sistema si espande e si adatta continuamente con nuovi Atomi e regole, preservando la coerenza delle informazioni esistenti.

### Il Metagrafo

A differenza dei grafi tradizionali, che separano nodi e archi, in Omnispace ogni elemento è un Atomo autonomo. Nato dal superamento dei limiti dei classici sistemi di gestione della conoscenza (dalle gerarchie a cartelle fino ai tag), il metagrafo rispecchia la natura ricorsiva e stratificata del pensiero. Permette di connettere domini eterogenei, eliminare ambiguità contestuali ed effettuare deduzioni complesse.

### La Metafora dei Contenitori

Il funzionamento degli Atomi si basa sull'annidamento ricorsivo:

1. **Atomi Base:** Elementi primari (es. _[Caffeina]_, _[Adrenalina]_, _[Aumenta]_).  
2. **Atomi Composti:** Le connessioni tra Atomi generano un nuovo Atomo di primo livello che racchiude i precedenti.
3. **Annidamento Ricorsivo:** Ogni composizione può essere inserita in Atomi di ordine superiore senza limiti di profondità.

_Esempio di annidamento progressivo:_

- **Atomo 1 (es: Processo):** `(Caffeina ──Aumenta──> Adrenalina)`
- **Atomo 2 (es: Evidenza):** `(Paper X ──Dimostra──> [Atomo 1])`
- **Atomo 3 (es: Contestazione):** `(Istruttore ──Contesta──> [Atomo 2])`

### Semplicità e Completezza Espressiva

Rappresentare ogni sfaccettatura del pensiero umano è un'utopia. Omnispace fornisce una radice minima ed essenziale, lasciando la personalizzazione all'utente, esempio:

- **Valutazione della verità:** Il sistema non impone una logica di verità nativa. Offre la visione d'insieme, ma lascia all'utente la libertà di adottare il proprio criterio di analisi (es. _Baricentro di massa della verità_, _Logica Non-Monotonica_, _Saggezza della Folla_).
- **Meccanismi di inferenza:** Poiché le possibilità deduttive sono infinite, l'utente definisce le proprie regole tra quelle fondamentali del pensiero (deduttiva, induttiva, abduttiva, analogica, controfattuale, non-monotonica, spazio-temporale/causale).

___


# Pipeline
___
## Ingestion Layer

Il pensiero umano è fluido e articolato in linguaggi eterogenei. Questo strato permette a Omnispace di assimilare la conoscenza esterna (manuali, articoli scientifici, note) tramite tecniche di Text Mining o estrazione avanzata (**Hyper-extract**).

I dati estratti vengono poi trasformati — manualmente o tramite automatismi — in file `.thinking` pronti per la compilazione.

In questa fase, se automatizzato, sarà necessario usare un LLM che consideri tutto il contesto del testo non strutturato.


## Grounding Layer

Per evitare la frammentazione del grafo dovuta alla creazione di Atomi duplicati per lo stesso concetto (es. "Acqua", "Water"), Omnispace applica due meccanismi di stabilizzazione semantica:

- **Inglese come Lingua Pivot:** Qualsiasi concetto espresso in altre lingue viene tradotto e normalizzato in lingua inglese, eliminando le difformità sintattiche e sfruttando il maggior volume di conoscenza globale disponibile.
    
- **Atom Resolution tramite ID Univoci:** Ogni Atomo viene ancorato a una mappa lessicale standard, ricevendo un identificativo univoco per prevenire ridondanze.

### Type System e Grounding

I **Type** rappresentano le strutture dati fondamentali di Omnispace. Tutti i Type usati sono indicizzati in una mappa globale gestita dall'utente, indispensabile sia durante la fase di compilazione, sia come supporto sintattico/semantico nell'IDE durante la scrittura del codice.

Il Grounding non si applica a tutto indistintamente, ma viene importato nei file unicamente per i Type che definiscono il lessico controllato. Valori liberi, come le variabili numeriche, non richiedono ancoraggio.

Si distinguono tre tipologie principali:

1. **Symbol (Simbolo):** Atomi indivisibili definiti esclusivamente dal loro nome testuale. Rappresentano costanti, funzioni o concetti. _Esempi:_ `A`, `green`, `+`, `f`.
    
2. **Expression (Espressione):** Liste ordinate di altri Atomi racchiuse tra parentesi tonde. Sono strutture composite usate indistintamente per rappresentare dati o codice da valutare (omoiconicità). _Esempi:_ `(+ 1 2)`, `(green tree)`, `(f A B)`.
    
3. **Variable (Variabile):** Valori dinamici e non vincolati (es. numeri, stringhe) che non necessitano di ancoraggio semantico e possono essere restituiti da esecuzioni o codice esterno. _Esempi:_ `42`, `3.14`, `"ciao"`.


## Compilation Layer

È la fase dell'architettura in cui i file `.thinking` selezionati dall'utente vengono compilati per generare l'istanza attiva di Omnispace, rendendo il sistema pronto per l'interazione.

### Energy-Based Propagation

Con l'espansione del metagrafo, la complessità combinatoria tende all'infinito: senza restrizioni, la navigazione causerebbe un'esplosione incontrollata dei rami. Per prevenire questo problema, il sistema applica un modello di propagazione energetica guidato dai vincoli di contesto (maschere).

- **Focus e Campo Gravitazionale del Contesto:** L'energia iniziale nasce dal nodo _seed_ selezionato (il punto di massimo fuoco), che varia dinamicamente secondo l'attenzione dell'utente. Il vincolo di contesto agisce sia come un "cono di luce" focalizzato, sia come una forza gravitazionale che deforma il panorama energetico: altera i dislivelli del grafo e rende specifici bacini di attrazione (attrattori) più profondi e cinematicamente "invitanti".
    
    - _Esempio:_ Se il contesto attivo evidenzia i nodi _Maranello_, _Auto Sportiva_ e _Rossa_, la struttura energetica devierà naturalmente e con alta probabilità verso l'attivazione di _Ferrari_.
        
- **Propagazione e Limite di Hop:** L'energia si diffonde ai nodi adiacenti attenuandosi man mano che ci si allontana dalla sorgente. L'utente definisce un limite massimo di hop (passaggi), garantendo esplorazioni rapide, rilevanti e strettamente delimitate dal contesto impostato. Ogni atomo è considerato attivo quando supera un certo threshold di energia.

### Query Engine

È il linguaggio di interfacciamento con Omnispace. A differenza dei linguaggi procedurali tradizionali come SQL, si basa interamente sulla definizione di vincoli di contesto per delimitare lo spazio di esplorazione.

Le query funzionano attraverso l'interpretazione del linguaggio naturale e la mappatura iniziale:

1. **Interpreta la query:** Un LLM integrato (eventualmente supportato da un sistema **GraphRAG**) comprende la frase dell'utente, ne estrae le parole chiave e i vincoli.
    
2. **Individuazione dei nodi seed:** Il sistema legge l'indice semantico, trova corrispondenza e cerca i nodi _seed_ (punti di partenza) nel metagrafo.

### Quando Serve Ricompilare

La ricompilazione è necessaria **solo** quando:
- Si aggiungono/rimuovono Atomi o relazioni al metagrafo
- Si modificano le regole di grounding o i Type
- Si cambia la dimensionalità dello spazio embedding

Le sessioni di esplorazione con query diverse non richiedono ricompilazione.


## Generation Layer

È lo strato che traduce l'esplorazione strutturata di Omnispace in linguaggio naturale.

Prende in input il sotto-grafo attivato (atomi, energie), i percorsi ricostruiti, le metriche di rilevanza (es. baricentri) e le eventuali fonti originali (se verranno implementati). Un LLM sintetizza questi elementi in una risposta conversazionale che evidenzia i meccanismi scoperti, cita i riferimenti e fornisce insight azionabili.

___


# Seek Higher Things
___
## L'idea di un network di conoscenza

### Condivisione dell'Esperienza

Ogni utente ha la possibilità di pubblicare il proprio dataset personale (rappresentativo, ad esempio, della propria esperienza di vita). L'obiettivo è consentire agli altri utenti di consultare dataset di altri che li condividono. Quindi va in modalità Collaborativa:

- **Il Limite Funzionale (Hard Problem):** Questa visione si scontra con il limite delle _esperienze incarnate_ (_embodied experiences_), le quali per loro natura non possono essere digitalizzate o caricate direttamente nel sistema.
- **Mitigazione dei Dataset Fittizi:** Il problema dei dataset falsi o fittizi viene superato grazie al modello di selezione attiva: ogni utente è libero di scegliere autonomamente quali fonti o dataset importare nel proprio ambiente.
- **Obiettivo Finale:** Sviluppare una piattaforma aperta di condivisione della conoscenza orientata all'auto-potenziamento e alla crescita personale.

## Strumenti Prevedibili e Modellazione Avanzata della Conoscenza

Poiché il linguaggio di **Omnispace** è **Turing-completo**, il sistema offre un'estensibilità nativa per la creazione e l'esecuzione di strumenti analitici e cognitivi avanzati (es. _modelli decisionali, motori inferenziali, simulazioni_).

La completezza secondo Turing garantisce che l'utente possa esprimere qualsiasi logica computazionale direttamente all'interno dell'ecosistema. Quindi qualsiasi funzione.

### Usare gli LLM in modo strategico

Una strategia efficace consiste nell'utilizzare **Omnispace come co-processore** insieme agli LLM. Questo approccio integrato consente di:

- **Mitigare le allucinazioni:** verificare costantemente l'accuratezza e la coerenza delle risposte per ridurre gli errori causati dai modelli di linguaggio.
- **Validare la logica:** accertarsi che i modelli arrivino a conclusioni corrette e prive di fallacie formali.
- **Stimolare nuove intuizioni:** analizzare e correlare le informazioni per identificare insight rilevanti o scoperte inaspettate.

---


# Tests
___
## Gli esempi

- [[Esempio Omnispace 1]]

## Experiments

Da capire pero se il sistema tipo con 100 Hop fa alcune conclusioni che l umano giunge, da provare

___


# I problemi da gestire
___
1. Bisogna fondere le gli Embedding (scegliere tra Qwen o Cohere) e gli HDC per creare l'algoritmo che verrà utilizzato nel Compilation Layer.
2. Usare approccio stile Shazam che è O(1) e sembrerebbe bravo a gestire il rumore, ma forse solo nell'audio è possibile. Da capire se con HDC ha senso.
3. Problema da gestire è che il linguaggio umano è ricco di sfumature e forse nel metagrafo non si riesce a rappresentare tutto. Magari usare RAG con fonte originale per accoppiarla insieme e un LLM. Il RAG arricchisce il testo finale da generare. Esempio problematica: Tipo 1h di video estrarre solo conoscenza non robe inutile, ma come si capisce? Tipo il cervello come fa a tenere solo quello che serve se lo fa?
4. Da gestire nel Grounding Layer quando e come ancorare, visto il problema è che molte cose vogliono dire altre cose, è difficile ancorare precisamente. Esempio: comprimere l' informazione se già presenti, tipo una relazione o espressione nidificata. Sennò ci sono duplicati della stessa cosa. Ma come capirlo?
5. Bisogna capire come sarà gestito il supporto multi-modale nell'Omnispace.
6. Bisogna capire se è necessario fare Grounding solo nei Tipi oppure anche degli atomi stessi nidificati. Forse è possibile farlo quando sono uguali al 100%. Visto il problema che il linguaggio umano è ricco di sfumature.
7. Altra tecnica che uso è resettare sempre LLM context.
8. Nuove idee umane rivoluzionarie ma difformi dalle regole attuali potrebbero richiedere un aggiornamento manuale dei vincoli: penso che questo problema sia risolto con le query!
9. Per eliminare colli di bottiglia, può convenire tenere SLM o LLM nello stesso spazio di memoria VRAM della GPU, dove sarà presente il Metagrafo compilato.
10. Interessante come ottimizzazione: HDC (Hyperdimensional Computing), Matryoshka Embeddings e Reranking.
11. Da capire se ha senso prendere spunto su qualcosa dalle Graph Neural Network.
12. Teoricamente potrebbero mettere qualsiasi lingua nel Grounding e di conseguenza nell'Omnispace. Noi ci limitiamo, per ora, a tenere solo l'inglese.
13. E' da capire anche se dobbiamo usare lo stesso Tokenizer di Qwen o motore di Embedding, perchè sennò si crea incongruenze se non sono la stessa cosa.
14. Le query vincoli di contesto devono essere teoricamente espressivamente complete nel senso che puoi definire qualsiasi vincoli tipo ignora, considera ecc.
15. Pattern Matching sara da mettere perchè permette di eseguire qualsisia codice o inferenza? Perchè infatti sto valutando se renderlo proprio come MeTTa: nella fase di ingestion l'utente può inserire anche regole nuove che vuole.
16. **Rallentamento su GPU**: Per navigare scatole annidate, la GPU salta continuamente tra indirizzi di memoria non contigui. Questo distrugge l'efficienza della cache, rallentando le prestazioni su grandi dataset se l'indicizzazione non è ottimale.
17. Potremmo compilare il Metagrafo all'interno della GPU trasformando gli Atomi in oggetti 3D con coordinate 3D o di più, così sfruttiamo la massima ottimizzazione della GPU, essendo essa stessa fatta per questo. Molti simile a: **Topologia Algebrica:** Complessi Simpliciali per scoprire "forma" dei dati (buchi, cavità, cluster)
18. Riconfermo la necessità di gestire bene il Grounding, tipo: Acqua e H20, sono la stessa cosa, ma sono due campi diversi, H20 è scientifico. Non è la stessa cosa di dire Acqua e Water. Questo è da considerare come esempio.
19. Da capire se meglio reranker o embedding, o usarli insieme.
20. Memoria olografico degli HDC si avvicina molta al ragionamento umano, lo fa così.
21. Le regole che si potrebbero intrdurre, funzionano bene quando sono super specifiche, essendo la conoscenza e di conseguenza il linguaggio umano molto sfumato e imprevedibile.
22. Il cervello umano è impossibile che impari tutto leggendo. E' come se estraeste le parole chiavi che a sua volta sono le cose che impattano maggiormente la traiettoria provisionale. Magari accumula anche microsfumatura che fanno micromodifche allo schema cerebrale.
23. Da sistemare tutte le fasi, così LLM può comprendere l'ordine.
24. Come fa il cervello umano tipo che pian piano impara e trova il baricentro di verità?
25. Non si può rappresentare tutto, perchè ogni umano usa la propria strategia. E' come se il cervello umano fosse Touring Completo.
26. Forse tutte le cose extra come controllo dei tipi ecc, non servono, perchè il pensiero umano non è rigido. Noi lasciamo il giudizio agli umani, deve solo mostrare, per la verità ecc ci penso l'umano.
27. Forse Tana Outliner si avvicina a questo?
28. Visto che uso gli embedding se sono caricati in Vram, e il sistema altrra il campo semantico, sono permanenti? Come gestire? Oppire ce un altro valore che cambia
29. È un paper collaborativo, cerco persone per cooperare, unire le forze ecc da scrivere su reddit
30. Essendo collaborativo, bisogna strutturata un modo tipo ad albero o altre tecniche per prendere decisioni, senza perdere magari scartando alcune idee interessati. Ci sara un tool? Ingegneria gestionale, come si studia?
31. dagli LLM rimuove linguaggio gergiale e esperto oscurantista è uno dei problemik "Da ora tu interpreti (nome), una critica letteraria malvagia, sadica e super critica al limite dell'immaginabile. Adesso ti darò dei miei scritti e tu li valuterai usando questa personalità fittizia"
32. il mio ssitema fa come gemini che scrapa nel suo database, ma è RAG quindi sbaglia quasi sempre Gemini
33. il sistema generalizza tipo con la memoria olografica, vede cose vicino, e quindi le considera nella generazione. Ma le cose diventano vicine perchè l’ho fa l’utente questa azione di modifica del suo userspace, cosa usa insieme ecc. A livello semantica direi che non cambia niente, visto che può fare lo share delle sua conoscenza.
34. Le cose senza senso semantico perchè spam o cose scritte non reali, saranno lontani negli Hop, visto gli embedding che aiutano.
35. La convergenza delle opinione sorge in modo automatico, perchè se in tnati dicono le stesse cose, nel metagrafo si vede, anche nell'Hop, per via degli embedding direi.
36. Pattern Matching ca pire se ha senso, magari l'utente lo scrive dopo aver osservato, non lo fa il ssitema in automatico.
37. come il sistema gestisce se tipo gli chiedo mostrami un film con queste caratteristiche nel metagrafo? Forse appartiene alla parte neurale e i due non si possono fondenere nel metagrafo e quindi rispettare complemtantre la compessità del pensiero umano?
38. **Logiche di Ordine Superiore:** Il metagrafo definisce solo la struttura. Per esprimere conoscenza reale serve arricchire con Logiche Descrittive o Type Theory (regole, quantificatori, implicazioni)
39. **Router All'Ingresso:** Quando fai una domanda, capisce da solo se ti serve un calcolo, una regola o una ricerca di testo e smista la richiesta al motore giusto.
40. **Text-to-SQL Integrato:** Se chiedi numeri, medie o statistiche, non usa il grafo ma interroga un database SQL/Analytics con **precisione matematica al 100%**. Tutti i dati anche SQL tipo sono nel Omnispace, magari come libreria per comunicare che è ottimizzato SQL. Questo è l'evoluzione è l'orchestratore.
41. Il contesto è da considerare? Come lo gestisce nel caso il metagrafo? Forse i tipi risolvono il problema. Perchè Panca e Panca Piana sono due cose diverse e hanno contesti diversi.
42. Ogni informazione, anche se sbagliata viene aggiunta. Però sempre deve essere controllato, perchè se pubblico chiunque mette cose false. Per gestire il tempo, serve che il tempo è considerato negli atomi, per ogni nuova operazione è essa stessa un atomo.
43. Come gestire il fatto che l idea cambia di continuo e non so come andarw e come gestire. Rischio di resettare il progetto ogni volta.
44. L'effetto dei bacini di energia permette di far scoprire naturalmente delle relazioni inaspetate.

___


____
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
