# 1. Inbox
- Quando un nuovo utente approda, il sistema gli chiede nome, data di nascita e magari anche foto profilo, da definire.
- Per generare la piattaforma, bisogna capire che metriche far visualizzare al'utente.
- Ingegneria della conoscenza, modalità che sarà presente.
- Provare generare immaginr homepage, però basata che è ottimizzata per il cerbello umano
- Comandi vocali
- La piattaforma non vuole essere un'app nuova da imparare: è una fusione ordinata di tutte le app che l'utente già usa, dando vita a un LifeOS coerente. _(da valutare)_
- Come si chiama il concetto tipo la Lista della Spesa o Finance Tracker, è nei Routines o un pl custom?
- Ogni informazione nuova va taggata, sempre, capendo le keyword della Raw.
- Nell'APP ci sono i vari Spaces e Anche Collections
- come capisce il contesto OpenCOG da proporre? Forse è un problema non presente visto che le releazioni sono corrette.
- Mini LLM sull'Edge fine-tunato per essere bravissimo a riconoscere le relazione nei RAW che l'utente aggiunge inizialmente.
- Il LifeOS deve essere bravo a riprendere il punto da dove si è interrotto, magari improvvisamente, l'utente.
- Inferenza lo fa umano, l AI aiuta a collegare i punti e tenere ordine nelle cose per non accumulare troppe cose da gestire in un botto
- Il sistema da la possibilità di applicare al Markdown delle variabili locali (Vengono assegnate in base ad un sistema tags per ordine) dove permette di mettere dei valori dinamici sul markdown che si aggiornano.
- Fare manutenzione è uno dei problemi principali, il Linting.
- •⁠Zero duplicazione di concetti
•⁠  ⁠Ogni nota deve avere uno scopo di recupero futuro
•⁠  ⁠Ogni link deve avere un motivo semantico
•⁠  ⁠Tag = filtro, non struttura
•⁠  ⁠Se una cosa è difficile da ritrovare, il sistema è sbagliato, non la tua memoria
- File system cerebrale
- I tuoi Path sono i tags su cui navicgi, dove puoi creare cartelle (ma non si crea rigidita ?) e ci sono i files
- In gni nota .lifeos, ogni riga/elemtno è un blocco oggetto personalizzata, che si può unificare più blocchi, e sono variabile dinamici che si aggiornano.
- approccio zero mark up, tipo senza [[]], ma solo con tipo CittaMilano

---
# 4. Flusso Operativo
### Review Giornaliera
- Il sistema lavora su un indice globale che si aggiorna ad ogni review.

---

### Rendering del frontend
- Il frontend logico viene costruito dinamicamente in base al profilo e al comportamento dell'utente.
- Il design deve essere accattivante per l'occhio umano.

___
In un LifeOS, il sistema AI deve lavorare in modo tale che l’utente mantenga sempre il punto dell’ordine all’interno del suo Vault o Workflow.

Sennò si rischia di avere cose sparse, senza che l’utente ne capisca l’ordine.

___

Feature interessante tenere l'utente informato su novità che vuole seguire.


Per estrarre cose per stare sul pezzo, il LifeOS prende l'attuale contesto, e ricerca in automatica e propone all'utente le nuove scoperte.



I progetti o coding lavorano sulla logica che ogni fase di revisione, LLM ottimizza il codice, ciclo di debug.


Areas() Outfit, Skin Care, Diet ---> Daily Routine (MOC)



Il sistema nel backend archivia tutti i files con tag soltanto (tag origine però, non un termine nuovo tutte le nuovo) senza rigidità, magari solo i PARA esitono. Poi il tutto viene ricostruito (l'ordine che vede l'utente), in base a cosa vuole vedere in quell'esatto momento.



Bisogna definire Domini Origine ---> e da lì si creano MOC finali dove raggruppanno tutto, senza avere rigidità.

Faren un prompt che compara le nuove modifiche proposte dall LLM riga per riga e per parola, per capire se non ha tralasciato niente. Solo sulle cose ancora da approvare dall'utente.


I project di LifeOS funzionano come Claude Code, dove c'è un microcontesto all'interno isolato iniettato, ma può leggere lo stesso LifeOS quando serve, tipo RAG però.


LifeOS possiede un System Log dove ha traccia e versioning delle modifiche che vengono fatte. Ma anche un Life Log dell'utente delle sue modifiche nella sua vita.

Il sottosistema non usa il Context, è iniettato manualmente in un sistema differente, per renderlo efficiente e veloce. Inietta ciò che serve in quell'esatto momento. E funziona anche per strutturato tipo un progetto che nel prompt iniettato c'è tutto la scrittura, però con logica piramidale per non iniettare tutto tutte le volte. L'iniezzione dei token è soltanto un indice globale che scende man mano che deve diventare preciso.

Un singolo file viene taggato con più tags, le cartelle sono solo strutture on demand con elecanti i vari files appartenenti a quel dominio. Ma può avere più domini, e li visualizza.

I tag possono essere messi anche all'interno dei singoli files (Direi solo i Markdown) e sui singoli file.


Durante il processo di riformattazione o approvazione, l'AI subsystem non deve usare parole sue, ma deve mantenere l'intenzione e le parole che usa normalmente l'utente. E' come se dovesse correggere solo la lingua.


Il meccanismo dei TAG è presente anche all'interno del Markdown, dove quando compiliamo, viene anche qui generato un nuovo files con solo i tags che lo riguardano. Unendo anche da altri files se serve. Mantenendo il contenuto, ma unendo i TAG esterni. Serve con approvazione dall'utente.


Il sistema offre la possibilità di usare AI in cloud oppure locale per il processing.


La nomenclatura dei Tag potrebbe funzionare come segue: magari tenere soltanto il dominio più piccolo tipo Analisi Sangue. Poi nel Map of Content c'è il dominio grande


  

Per collegare tag tra testo markdown, l’utente deve evidenziare il contenuto da collegare ad un altro TAG o file (?). Logica a blocchi stile Logseq. Evitare oggetti stile Anytype, perchè creano rigidità dovendo definire a priori.

Usare WebApp nella fase BETA, perchè è più facile da far provare agli utenti.


Il sistema ha un Versioning che permette di vedere come evolve il tutto.



https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/ Paper Utile, magari per far collaborare più utenti nuovi ha senso? Simile a questo: https://github.com/Agent-Knowledge-Standard/AKS-Specification


Fare i cicli di debug passando sempre ad una versione migliore. Magari con una matrice che raffina sempre.


Puoi creare blocchi di codice, dove si aggiorna in tempo reale in tutti i Markdown dove è posizionato


Questo sistema, idea per zero knowledge del mio lifeos. Stile ipervettori

https://www.reddit.com/r/PKMS/comments/1uvpnw9/a_short_human_made_critiqe_of_llmwiki/?share_id=V_6VrBHDBj9SE7Nb-foBG&utm_medium=ios_app&utm_name=ioscss&utm_source=share&utm_term=3

___
# Raw Core Engine LifeOS:
Spazio utente stesso knowledge graph che usano gli utenti però possono caricare dati personali. Usando Attributi Extra per identificare. Stile Obsidian.

Tipo creare nuove categorie. Ottica di Karl Voit.


Nella piattaforma devo rispettare il postulato chebsi puo creare qualsiai cosa, non ce rigidia, io pffro solo strumenti che estendono il cervello, il workflow è custom pero, ognuno puo usare la creatività per creare quello che ha bisogno


Workflow essendo immaginazione forse usare LLM, ma usare sempre rigidida, da capire


Ma come gestire qualsiasi informazione tipo un banale grafico o libro fanrasy? Ha senso? Il cervello come farebbe

___

17. Rischiamo di diventare rigidi con i Tags

___

15. Cronologie modifiche Stile Git, assi del tempo su LifeOS o sul workflow