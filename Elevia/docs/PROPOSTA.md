# 1. Space

Proponiamo uno spazio unificato chiamato **Space**, che raccoglie la conoscenza salvata dall'utente e la rende esplorabile. L'obiettivo è preservare la ricchezza espressiva del linguaggio naturale, senza costringere ogni contenuto in categorie rigide o descrizioni che ne perdano il significato.

Space deve poter accogliere contenuti in formati diversi. Per i formati supportati, il sistema legge il file e ne ricava una descrizione del contenuto. Anche i file che non può interpretare possono essere caricati: in questi casi, l'utente ne descrive manualmente il significato. Accettare un file non equivale quindi a comprenderne automaticamente il contenuto.

In accordo con il principio **Human in the loop**, è l'utente a decidere quali contenuti entrano nel proprio spazio di conoscenza. Prima di aggiungerli, li legge o li esamina e ne valuta l'utilità. L'IA può assisterlo nell'interpretazione e nell'organizzazione, ma non dovrebbe alimentare lo spazio autonomamente, senza il suo controllo.

Sono previsti dei meccanismi per limitare un'esplorazione incontrollata. Questo serve perchè in futuro potrebbero esserci centinaia di nuovi file.

## 1.1 Caratteristiche

1. **Inserimento dei file:** aggiungere nuovi contenuti, con una descrizione ricavata dal sistema o fornita dall'utente.
2. **Rimozione di un file:** consentire all'utente di rimuovere il file conservando la descrizione e i metadati associati. Questi saranno scritti nel nome del file stesso.


# 2. Interfaccia
## 2.1 Query Engine

Il Query Engine è l'interfaccia attraverso cui l'utente consulta Space. Permette di organizzare i contenuti per ritrovarli e di esplorarli per cercare informazioni pertinenti e possibili collegamenti. L'utente comunica con il sistema attraverso maschere di contesto (iniezioni di guida) usando il linguaggio naturale.

## 2.2 Discovery Engine

Il Discovery Engine guida l'esplorazione di Space attraverso le maschere di contesto definite dall'utente. Queste orientano l'attenzione e permettono di cercare contenuti e possibili collegamenti rispetto alla richiesta corrente.

### Il Cono di Luce

Il Cono di Luce rappresenta il focus dell'utente nello spazio di rappresentazione unificato. È definito dalle maschere di contesto, che delimitano l'esplorazione e indicano dove concentrare l'attenzione.

Possono essere attive più maschere contemporaneamente. Una maschera può esprimere un tema, un problema, uno scopo o un insieme di contenuti da considerare.

Il focus determina come viene osservata la memoria, senza modificarla né creare relazioni. Quando l'utente cambia le maschere, il sistema ricalcola il Campo Contestuale.

### Il Campo Contestuale

Il Campo Contestuale è una deformazione temporanea dello spazio di rappresentazione prodotta dal focus corrente. La struttura memorizzata rimane invariata; cambiano le **distanze contestuali**, cioè quanto gli elementi risultano vicini o lontani rispetto alle maschere attive.

Con la maschera «produzione delle auto Ferrari», per esempio, `Maranello` può risultare particolarmente vicino. Con «consumi delle auto Ferrari», possono ricevere maggiore attenzione altri contenuti.

Questa vicinanza favorisce l'esplorazione di percorsi già possibili nello spazio, senza creare nuove relazioni. Il Campo Contestuale è unico per il focus corrente: tutte le maschere attive contribuiscono a definirlo.

### La propagazione dell'energia

L'energia rappresenta l'attivazione prodotta dalle maschere di contesto e propagata tra i contenuti di Space. Può seguire le relazioni esplicite già presenti oppure le vicinanze di significato nello spazio di rappresentazione.

La struttura dello spazio determina i percorsi possibili. Il Campo Contestuale favorisce alcuni passaggi rispetto ad altri, entro i confini stabiliti dalle maschere.

A ogni passaggio, o **hop**, l'energia decade. L'utente definisce un budget massimo per non avere un'attivazione incontrollata.

### Esempio: scoprire il riscaldamento a microonde con Elevia

Immaginiamo di usare Elevia prima che sia nota l'applicazione delle microonde alla cottura degli alimenti. Il magnetron esiste già ed è impiegato nei radar. Space contiene informazioni sul cioccolato, sul funzionamento del magnetron e sull'interazione tra onde elettromagnetiche e materia, ma nessun documento che descriva un forno a microonde o colleghi direttamente il magnetron alla cottura.

L'utente nota che il cioccolato si è sciolto mentre lavorava vicino a un apparato radar. Registra l'osservazione e definisce la maschera «Che cosa potrebbe aver fatto sciogliere il cioccolato in queste condizioni?». Il radar è parte del contesto osservato, non una causa già stabilita.

Il Discovery Engine dovrebbe poter esplorare un percorso come questo:

```text
       osservazione: cioccolato sciolto
              vicino a un radar
                      │
              contesto cioccolato
                      │
                 scioglimento
                      │
                 riscaldamento
                       ╲
                        ╲  distanza contestuale
                         ╲ ridotta dal campo
                          ╲
                assorbimento di energia
                   da onde elettromagnetiche
                          │
                       microonde
                          │
                      magnetron
                          │
                     contesto radar
```

In questo esempio, Elevia non crea nuove relazioni nella memoria. La maschera modifica il Campo Contestuale e riduce le distanze contestuali tra regioni che, rispetto ad altri focus, risultano lontane. Le conoscenze sul cioccolato e quelle sul radar diventano così più vicine rispetto al problema osservato. Emergono percorsi già possibili nello spazio, ma prima poco favoriti, mentre la struttura memorizzata rimane invariata.

Dal percorso emerge un’ipotesi da verificare: le microonde emesse dal magnetron potrebbero aver riscaldato il cioccolato fino a scioglierlo.


# 3. Ingestion

L'Ingestion Layer prepara i contenuti scelti dall'utente per inserirli in Space e renderli consultabili. L'utente mantiene il controllo su ciò che viene aggiunto e può correggere metadati e descrizioni.

## Organizzazione

Per ogni file, l’ingestion raccoglie i metadati disponibili o forniti dall’utente e li registra come coppie chiave-valore. Le facets sono le dimensioni attraverso cui il file viene descritto, come autore, fonte, data e tipo. Questi attributi costituiscono la base dell'organizzazione deterministica: permettono di selezionare, raggruppare e ordinare i file secondo criteri espliciti. A parità di dati e criteri, il risultato è lo stesso.

## Rappresentazione per l'esplorazione

Per i formati supportati, l'ingestion legge il contenuto, ne ricava una descrizione e prepara una rappresentazione comune destinata all'esplorazione probabilistica. Questa rappresentazione permette di confrontare ciò che i file esprimono anche quando provengono da fonti e formati diversi, senza limitarsi alle corrispondenze tra metadati.

L'utente può aggiungere annotazioni, spiegare perché ha salvato il file e descriverne il rapporto con altri contenuti o con lo scopo di Space. Queste informazioni restano espresse in linguaggio naturale, senza doverle ridurre a categorie o tag, e contribuiscono alla rappresentazione insieme al contenuto disponibile e alla descrizione.

La rappresentazione mantiene il riferimento al file originale e, quando possibile, ai singoli passaggi. La descrizione non sostituisce l'originale e i possibili collegamenti restano proposte da verificare.

Anche i file che il sistema non può interpretare possono essere inseriti. In questi casi, la rappresentazione si basa sulla descrizione e sul contesto forniti dall'utente, senza considerare il contenuto come automaticamente compreso.
