***Versione:** 1.0*  
***Data:** Agosto 2026*
***Stato:** Bozza*

***Nota:** il nome **Elevia** è provvisorio e verrà sostituito, poiché non disponibile.*


# Manifesto
---
## Il motivo di tutto questo

L'idea nasce da un'esperienza comune: durante lo studio di un nuovo argomento, capita spesso di scoprire solo in un secondo momento l'esistenza di approcci migliori, connessioni chiave o informazioni fondamentali che all'inizio erano difficili da individuare o semplicemente non disponibili. E ogni volta la conclusione è la stessa: «Se lo avessi saputo prima!».

Si potrebbe pensare che sarebbe bastato informarsi meglio fin da subito, ma come esseri umani le nostre capacità di elaborazione sono limitate. In una società moderna che lascia sempre meno tempo per approfondire la conoscenza, nasce la necessità di accelerare il processo. Serve un acceleratore.

Il problema non è necessariamente la mancanza di conoscenza, ma la sua frammentazione. Le informazioni esistono, ma sono distribuite in fonti diverse, organizzate in modo isolato e spesso prive di collegamenti espliciti.

La sfida non è quindi soltanto raccogliere nuova conoscenza, ma creare uno spazio in cui la conoscenza esistente possa essere collegata, esplorata e compresa nella sua interezza. Dando la possibilità di avere una visione molto più allargata.


## Visione

L'essere umano ha costruito la propria evoluzione attraverso la capacità di comprendere, creare modelli della realtà e trasformare la conoscenza in nuove possibilità. 

Tuttavia, la quantità di informazioni disponibili oggi supera la capacità individuale di organizzarle, collegarle e utilizzarle pienamente. Nasce quindi la necessità di costruire strumenti che estendano le capacità cognitive umane, non sostituendole, ma amplificandole. 

Se rappresentassimo la conoscenza come un grafo, il cervello umano riesce normalmente a esplorare solo una porzione limitata delle connessioni disponibili. Vogliamo permettere di rendere accessibili molte più relazioni tra concetti, offrendo una visione più ampia da cui l'essere umano può individuare pattern, formulare ipotesi e costruire nuove conoscenze.

Il manifesto nasce con questo obiettivo: diventare un'estensione del sistema nervoso cognitivo umano, permettendo alle persone di comprendere, ragionare e creare conoscenza oltre i limiti naturali della memoria e dell'attenzione.

L'obbiettivo è creare un ambiente in cui l'essere umano possa interagire con la conoscenza in modo più profondo, individuando connessioni, costruendo nuovi modelli e aumentando la propria capacità di comprendere sistemi complessi. E' che sia condivisibile anche tra i vari utenti.


### Principi 

1. **Amplificare, non sostituire:** la tecnologia deve aumentare le capacità dell'essere umano senza eliminare il suo ruolo nel pensiero, nella creatività e nelle decisioni. 
2. **Centralità dell'essere umano (Human in the Loop):** il controllo, il giudizio e la responsabilità rimangono sempre umani. La tecnologia è uno strumento di potenziamento, non un sostituto dell'intelligenza umana. 
3. **Espansione della conoscenza:** la conoscenza non deve essere soltanto conservata, ma resa esplorabile, collegabile e trasformabile. 
4. **Sintonia cognitiva:** Gli strumenti cognitivi devono adattarsi al modo in cui l'essere umano comprende il mondo, diventando un'estensione naturale del processo di pensiero.

___


# Omnispace
---

Per realizzare una delle idee del manifesto, il progetto adotta **Omnispace**: un metagrafo spazio-universale della conoscenza progettato per rappresentare e manipolare concetti, relazioni, logica e processi all'interno di un'unica struttura **Turing-completa**, di conseguenza una Completezza Espressiva. Che è tipo del linguaggio umano.

Grazie alla rappresentazione unificata, il sistema applica la **metaprogrammazione**: può descrivere, modificare ed estendere sé stesso manipolando la conoscenza attraverso gli stessi meccanismi con cui la rappresenta.

### Principi

1. **Postulato dell'Unità Atomica** Ogni elemento della conoscenza è un **Atomo**. Dati, concetti, entità, proprietà, relazioni, regole, processi e comportamenti condividono la stessa natura fondamentale e differiscono solo per struttura, proprietà e comportamento.
2. **Postulato della Rappresentazione Unificata e dell'Omoiconicità** Ogni forma di conoscenza risiede nello stesso spazio concettuale. La sua natura **omoiconica** fa sì che codice e dati condividano la medesima struttura, superando la separazione tradizionale tra dati, logica e comportamento per permetterne la trasformazione all'interno dello stesso ambiente.
3. **Postulato dell'Evoluzione Progressiva** Il sistema si espande e si adatta continuamente tramite l'introduzione di nuovi Atomi, strutture, regole e comportamenti, preservando la coerenza delle informazioni già esistenti.

## Metagrafo

I grafi tradizionali separano "nodi" (entità) e "archi" (relazioni). L'architettura di Omnispace li supera attraverso il **metagrafo**, in cui ogni elemento è un **Atomo autonomo**.

Il metagrafo rappresenta la struttura che meglio rispecchia la natura ricorsiva, stratificata e in continua evoluzione del pensiero umano. La sua organizzazione atomica permette di mappare una conoscenza capace di autocorreggersi nel tempo e di effettuare deduzioni complesse tra domini eterogenei (come le interrelazioni tra biochimica e fisiologia dell'allenamento), eliminando ogni ambiguità contestuale.

Ho scelto questa struttura dati muovendo dalle mie ricerche nel campo dei sistemi di produttività per il _Second Brain_: analizzando i limiti della classica gerarchia a cartelle — che non rispetta il reale flusso di pensiero — ho individuato inizialmente nei tag, e successivamente nei metagrafi, l'approccio più naturale e coerente.

### La Metafora dei Contenitori

Per comprendere il funzionamento degli Atomi e l'annidamento ricorsivo, possiamo usare la metafora dei contenitori:

1. **Atomi Base:** Ogni singolo elemento primario è un Atomo (es. _Caffeina_, _Adrenalina_).
2. **Atomi Composti:** Quando colleghiamo più elementi, la struttura risultante non è una semplice "linea di connessione", ma diventa essa stessa un nuovo Atomo che racchiude i precedenti.
3. **Annidamento Ricorsivo:** Poiché ogni composizione genera un nuovo Atomo di primo livello, questo può essere inserito all'interno di Atomi di ordine superiore a qualsiasi livello di profondità.

**Esempio di annidamento progressivo:**

- **Atomo_1 (Processo):** `(Caffeina ──Aumenta──> Adrenalina)`
- **Atomo_2 (Evidenza):** `(Paper_X ──Dimostra──> [Atomo_1])`
- **Atomo_3 (Contestazione):** `(Istruttore ──Contesta──> [Atomo_2])`

## La Semplicità-Completa

Ho deciso di rendere **Omnispace** il più semplice possibile e, al tempo stesso, espressivamente completo: è pura utopia rappresentare ogni sfaccettatura del pensiero umano. L'obiettivo è creare la radice; tutto il resto viene da sé ed è personalizzabile da ciascun utente.

Per esempio, non ho inserito nativamente una gestione della verità, poiché è impossibile gestirla in un sistema simbolico per via delle troppe eccezioni. Ho preferito lasciare all'utente la scelta di valutare un'informazione: il grafo offre una visione allargata, ma il giudizio spetta a lui.

Personalmente uso il **Baricentro di massa della verità** (ascolto molti e formo un'idea centrale, modificabile se emergono nuovi elementi), ma esistono molti altri approcci (es. _Equilibrio statistico_, _Raffinamento contestuale_, _Tracciabilità_, _Principio di Pareto_, _Saggezza della Folla_, _Logica Non-Monotonica_). Il sistema è _open_ proprio per permettere a ciascuno di adottare il proprio metodo. Un'altra mia tecnica è accumulare conoscenza e fare _pruning_ del superfluo; Omnispace mi permette di vedere oltre.

Nel metagrafo le possibilità di inferenza sono infinite, per questo spetta all'utente definirle. Il cervello ne usa probabilmente 7 fondamentali: **Deduzione**, **Induzione**, **Abduzione**, **Analogia**, **Controfattuale**, **Defeasible/Non-Monotonica** e **Spaziale/Temporale/Causale**.

In definitiva, diamo all'utente la possibilità di allargare la propria visione, ma il giudizio finale resta sempre il suo.

___


# Pipeline
___
## Ingestion Layer

Il pensiero umano è fluido, sfumato e articolato in linguaggi e formati eterogenei. Questo strato nasce per permettere a **Omnispace** di assimilare e unificare la conoscenza esterna, integrando manuali, articoli scientifici, teorie e note in un unico sistema.

Vengono usate tecniche di Text Mining per fare questo.


## Grounding Layer

Poiché i linguaggi umani sono complessi, caotici e ricchi di sfumature, il rischio primario è la frammentazione del grafo a causa della creazione di Atomi duplicati per il medesimo concetto (es. _"Acqua"_, _"Water"_, _"H₂O"_). Man mano che il lessico si arricchisce e nuovi elementi vengono aggiunti alla mappa, garantire la convergenza semantica diventa fondamentale. E' necessario importare il Grounding utilizzato per ogni file.

Per questo motivo, Omnispace applica due meccanismi di stabilizzazione:

- **Inglese come Lingua Pivot:** qualsiasi testo o pensiero espresso in altre lingue viene tradotto e normalizzato nello spazio semantico in lingua inglese. Questo approccio azzera le difformità sintattiche internazionali e sfrutta la lingua che racchiude il maggior volume di conoscenza globale.
- **Atom Resolution tramite ID Univoci Standard:** ancora ogni atomo alla mappa lessicale, assegnandogli un identificativo di riferimento univoco per evitare ridondanze.


## Compilation Layer

E' la fase finale di compilazione dell'Omnispace.
Qui l'utente, può interfacciarsi con il sistema.

### Query Omnispace

È il linguaggio che ci permette di interfacciarci con Omnispace. A differenza dei linguaggi di interrogazione tradizionali come SQL, non si basa su procedure ma sulla definizione di vincoli/contesto. Questo approccio è coerente con la natura del sistema, poiché in Omnispace non si eseguono inferenze, trattandosi del layer di presentazione.

### Energy Based

Per prevenire l'esplosione combinatoria, il sistema richiede la definizione di un numero massimo di _hop_. L'energia iniziale si genera nel primo nodo invocato — il punto di massimo fuoco — corrispondente all'elemento con la maggiore massa gravitazionale nell'Omnispace compilato. Questo punto è dinamico e varia in base al focus dell'utente.

Di conseguenza, sia la propagazione dell'energia sia la traiettoria degli _hop_ sono variabili: ogni nuovo elemento raggiunto acquisisce una propria energia — la cui intensità decresce man mano che ci si allontana dall'origine — modulata dall'attenzione dell'utente. Quest'ultima agisce come un cono di luce focalizzato sul pensiero corrente, diventando un vero e proprio generatore di energia.

Poiché con l'espansione dell'Omnispace la complessità combinatoria del grafo tende all'infinito, la definizione preventiva di vincoli/contesto e limite di _hop_ è essenziale per evitare una diramazione incontrollata del sistema.


## Generation Layer

È l'ultima fase in cui visualizziamo il workflow generato dall'esplorazione e dall'interrogazione della compilazione. In questo step, traduciamo il flusso in linguaggio naturale tramite un LLM. Per farlo, il modello considera sia il contesto dell'utente sia la trascrizione della sessione Omnispace su cui si sta lavorando. In questo modo, gli utenti possono interagire in linguaggio naturale per svolgere attività come il brainstorming e altre operazioni future.

___


# Seek Higher Things
___

## L'idea di un network di conoscenza

### Condivisione dell'Esperienza

Ogni utente ha la possibilità di pubblicare il proprio dataset personale (rappresentativo, ad esempio, della propria esperienza di vita). L'obiettivo è consentire agli altri utenti di consultare tali dati ed evitare di ripetere i medesimi errori.

- **Il Limite Funzionale (Hard Problem):** Questa visione si scontra con il limite delle _esperienze incarnate_ (_embodied experiences_), le quali per loro natura non possono essere digitalizzate o caricate direttamente nel sistema.
- **Mitigazione dei Dataset Fittizi:** Il problema dei dataset falsi o fittizi viene superato grazie al modello di selezione attiva: ogni utente è libero di scegliere autonomamente quali fonti o dataset importare nel proprio ambiente.
- **Obiettivo Finale:** Sviluppare una piattaforma aperta di condivisione della conoscenza orientata all'auto-potenziamento e alla crescita personale.

## Strumenti Prevedibili e Modellazione Avanzata della Conoscenza

Poiché il linguaggio di **Omnispace** è **Turing-completo**, il sistema offre un'estensibilità nativa per la creazione e l'esecuzione di strumenti analitici e cognitivi avanzati (es. _modelli decisionali, motori inferenziali, simulazioni_).

La completezza secondo Turing garantisce che l'utente possa esprimere qualsiasi logica computazionale direttamente all'interno dell'ecosistema. Quindi qualsiasi funzione.

---


# Gli Esempi
___

___


# I problemi da gestire
___
1. Bisogna fondere le gli Embedding (scegliere tra Qwen o Cohere) e gli HDC per creare l'algoritmo che verrà utilizzato nel Compilation Layer.
2. Usare approccio stile Shazam che è O(1) e sembrerebbe bravo a gestire il rumore, ma forse solo nell'audio è possibile. Da capire se con HDC ha senso.
3. Problema da gestire è che il linguaggio umano è ricco di sfumature e forse nel metagrafo non si riesce a rappresentare tutto. Magari usare RAG con fonte originale per accoppiarla insieme e un LLM. Il RAG arricchisce il testo finale da generare.
4. Da gestire nel Grounding Layer quando e come ancorare, visto il problema è che molte cose vogliono dire altre cose, è difficile ancorare precisamente.
5. Grounding non su tutto, pensa alle variabili come i numeri, non ha senso.
6. Bisogna capire come sarà gestito il supporto multi-modale nell'Omnispace.
7. Bisogna capire se è necessario fare Grounding solo nei Tipi oppure anche degli atomi stessi nidificati. Forse è possibile farlo quando sono uguali al 100%. Visto il problema che il linguaggio umano è ricco di sfumature.
8. Altra tecnica che uso è resettare sempre LLM context.
9. Nuove idee umane rivoluzionarie ma difformi dalle regole attuali potrebbero richiedere un aggiornamento manuale dei vincoli: penso che questo problema sia risolto con le query!
10. **Rallentamento su GPU**: Per navigare scatole annidate, la GPU salta continuamente tra indirizzi di memoria non contigui. Questo distrugge l'efficienza della cache, rallentando le prestazioni su grandi dataset se l'indicizzazione non è ottimale.
11. Per eliminare colli di bottiglia, può convenire tenere SLM o LLM nello stesso spazio di memoria VRAM della GPU, dove sarà presente il Metagrafo compilato.
12. Potremmo compilare il Metagrafo all'interno della GPU trasformando gli Atomi in oggetti 3D con coordinate 3D o di più, così sfruttiamo la massima ottimizzazione della GPU, essendo essa stessa fatta per questo.
13. Interessante come ottimizzazione: HDC (Hyperdimensional Computing), Matryoshka Embeddings e Reranking.
14. Da capire se ha senso prendere spunto su qualcosa dalle Graph Neural Network.

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