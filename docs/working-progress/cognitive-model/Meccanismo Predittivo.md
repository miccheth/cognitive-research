
___
# Spazio Latente e Modello Interno

Il modello si sviluppa all'interno del suo **spazio latente astratto**: una rappresentazione matematica compressa dove l'IA conserva solo il significato profondo delle cose, eliminando i dettagli inutili. Questo spazio funziona logicamente in modo simile alle _"tasche di riducibilità"_ descritte da Stephen Wolfram: ad esempio, per capire come si muoverà un pianeta a causa della gravità non si calcola il comportamento di ogni singolo atomo, ma si applica direttamente la formula di Newton.

Grazie a questo spazio latente, il modello può pianificare e decidere le sue azioni utilizzando un proprio **modello interno**, il quale comprende le regole generali del mondo e ragiona in modo astratto. Ad esempio, se il modello vede un bicchiere cadere, non calcolerà l'esatta traiettoria fisica di ogni frammento, ma prevederà il concetto astratto che il bicchiere si romperà.

___
# Architettura: La Piramide di Competenze

Questa architettura interna si struttura verticalmente come una vera e propria **piramide di competenze predittive**, in cui ogni livello si poggia su quello inferiore:

- **Causal (Causale - La base):** È la capacità fondamentale di comprendere i rapporti di causa-effetto (_"Se faccio X, accade Y"_), superando la semplice correlazione statistica dei dati.
    
- **Interactive (Interattivo):** Su questa base causale, il sistema diventa un agente attivo che interagisce con l'ambiente, comprendendo come le sue stesse azioni modificano lo stato del mondo.
    
- **Persistent (Persistente):** Salendo la piramide, il modello acquisisce la permanenza dell'oggetto; capisce che il mondo e le sue regole continuano a esistere stabilmente anche quando escono dal suo campo visivo immediato.

___
# Il Ciclo di Predizione, Errore e Incertezza

Operando all'interno di questa struttura, il sistema vive immerso in un ambiente costantemente perturbato da stimoli e opera una **predizione continua**. Quando c'è equilibrio, il sistema si trova in una condizione di **confidenza**, in cui i feedback del mondo reale rispettano il modello previsionale interno e il modello può agire in modo fluido.

Quando il sistema compie un'azione non ottimale e riceve un feedback inatteso, **l'errore di previsione rompe l'equilibrio**, modificando la traiettoria del sistema. È precisamente questa rottura a innescare l'**apprendimento per esperienza o statistico**: l'errore costringe lo spazio latente a ricalibrarsi per aggiornare il modello del mondo.

**Nota:** La previsione è sempre asincrona rispetto a ciò che sta accadendo. Il cervello continua a predire, ma appena riceve un feedback contrastante la previsione viene rotta istantaneamente.

A questo meccanismo si lega strettamente la variabile di **Incertezza**: un indicatore dinamico che esprime quanto il modello predittivo sia insicuro delle proprie stime. Quando questa variabile si alza a causa di feedback imprevisti, la traiettoria del sistema perde stabilità, smette di essere lineare e richiede maggiore computazione per ritrovare l'equilibrio.

___
# Gradiente di Certezza e Percezione della Risposta

Il sistema percepisce il proprio stato di incertezza come un **gradiente dinamico** nello spazio latente:

- **Incertezza alta**: nessun attrattore domina, percezione di indecisione
- **Incertezza in diminuzione**: un cluster si sta stabilizzando, percezione di "avvicinamento"
- **Certezza**: l'attrattore è stabile.

Questa percezione non è simbolica ma **energetica**: il sistema sente la stabilità dell'attrattore prima di generare la risposta esplicita. La conoscenza distribuita e lossy della componente non-deterministica permette di rappresentare sfumature graduali tra stati mentali, catturando la similarità progressiva verso la risposta corretta.

Il sistema genera un **valore tendenziale** simile alla risposta vera prima di averla completamente formulata: questa è la sensazione di "essere vicini" alla soluzione.

___