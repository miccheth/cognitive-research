# Space

**Space** è lo spazio di conoscenza unificato di Elevia: raccoglie i contenuti scelti dall'utente e permette di ritrovarli ed esplorarne i possibili collegamenti. L'obiettivo è preservare ciò che esprimono, senza ridurli a categorie rigide, mantenendo accessibili le fonti originali.

In accordo con il principio **Human in the loop**, l'utente decide che cosa aggiungere e ne valuta l'utilità. L'IA lo assiste nell'organizzazione e nell'esplorazione, senza alimentare lo spazio autonomamente né sostituirsi al suo giudizio.

Sono previsti meccanismi per delimitare l'esplorazione e limitarne l'estensione, così da mantenerla sotto il controllo dell'utente anche quando cresce il numero di contenuti.


# Interfaccia

## Query Engine

Il Query Engine è il motore che gestirà le query in linguaggio naturale usate dall'utente per consultare Space. Da queste dovrà estrarre le maschere di contesto, così da definire la direzione in cui l'utente intende orientare l'esplorazione.

## Discovery Engine

Il Discovery Engine riceve le maschere di contesto generate dal Query Engine e le applica a Space. Il sistema adatta l’esplorazione per rendere accessibili i contenuti pertinenti, senza modificare la struttura permanente.

### Attention Beam

Rappresenta il focus dell’utente in Space. È definito dalle maschere di contesto generate, che indicano su che cosa concentrare l’attenzione e delimitare l’esplorazione.

Più maschere possono contribuire allo stesso focus, specificando temi, problemi, scopi o contenuti da considerare.

### Relevance Field

E' la deformazione temporanea dello spazio di rappresentazione. Modifica le **distanze contestuali** tra i contenuti: elementi lontani rispetto ad altri focus possono risultare vicini rispetto alla richiesta corrente.

Con la maschera «produzione delle auto Ferrari», per esempio, `Maranello` può risultare particolarmente vicino ai contenuti sulla produzione. Con «consumi delle auto Ferrari», saranno favoriti altri contenuti e percorsi.

Tutte le maschere attive contribuiscono a un unico campo, che viene ricalcolato quando cambia il focus. La struttura permanente resta invariata: cambiano le vicinanze usate per l’esplorazione, senza registrare nuove relazioni.

### Activation Spread

Rappresenta l’attivazione prodotta dalle maschere di contesto. Si propaga tra i contenuti di Space seguendo le relazioni esplicite o le vicinanze di significato nello spazio di rappresentazione.

La struttura di Space determina i percorsi possibili; il Campo Contestuale favorisce alcuni passaggi rispetto ad altri. La propagazione permette così di esplorare anche contenuti collegati indirettamente al focus dell’utente.

A ogni passaggio, o **hop**, l’energia decade. L’utente definisce un budget massimo per limitare l’estensione dell’esplorazione ed evitare un’attivazione incontrollata.


# Ingestion

L'Ingestion Layer prepara i contenuti scelti dall'utente per inserirli in Space e renderli consultabili. L'utente mantiene il controllo su ciò che viene aggiunto e può correggere metadati e descrizioni.

## Organizzazione deterministica

L'ingestion registra tag, concetti e metadati associati ai contenuti, seguendo il modello proposto da Nayuki. Questa organizzazione si basa su associazioni esplicite, non su somiglianze di significato. Ogni file può essere classificato in più modi, senza assegnargli una sola posizione in una gerarchia di cartelle.

**Tag semplici**: Sono etichette testuali associate ai file, come `vacanza` per `foto1.jpg`. Un file può avere più etichette oppure nessuna; la stessa etichetta può descrivere più file.

**Tag complessi**: Separano il concetto dai suoi nomi attraverso un nucleo chiamato *tag core*. Il modello permette di gestire:
	- Lingue diverse: `Roma` e `Rome` sono nomi associati allo stesso concetto.
	- Omonimi: la città di Roma e una persona di cognome Roma hanno nuclei distinti, anche se condividono un nome.
	- Cambi di nome: aggiungere `Anfiteatro Flavio` come nome del concetto `Colosseo` non richiede di riclassificare le foto già associate.

**Metadati**: Tag e metadati sono conservati separatamente dai file. Per `foto1.jpg` puoi indicare autore e data, senza imporre gli stessi attributi a tutti i contenuti. Una proprietà può avere più valori oppure non essere specificata.

**Consultazione delle associazioni**: Da un file puoi consultare i suoi tag; da un tag puoi trovare i file associati. Combinando il concetto della città di Roma con l'etichetta `vacanza`, ottieni i file associati a entrambi.

La selezione applica criteri espliciti ai dati registrati: a parità di dati e criteri, restituisce gli stessi file.

## Rappresentazione dei contenuti

Per i formati supportati, l’ingestion legge il contenuto dei file e ne costruisce una rappresentazione attraverso tecniche come gli embedding vettoriali, reranking, cross domain, ecc. Questa rappresentazione permette di confrontare ciò che i contenuti esprimono, anche quando usano parole diverse o provengono da formati differenti.

Le annotazioni dell’utente contribuiscono alla rappresentazione: possono chiarire un’espressione ambigua, aggiungere contesto o spiegare perché un contenuto è stato salvato. Per i file non supportati, descrizioni e annotazioni costituiscono la base della rappresentazione.

Il Discovery Engine usa questa base per esplorare i contenuti rispetto alle maschere di contesto. Le vicinanze di significato non equivalgono a relazioni certe: servono a proporre collegamenti da verificare, senza modificare tag e metadati registrati.

La rappresentazione mantiene il riferimento al file originale e, quando possibile, ai singoli passaggi. È un’interpretazione del contenuto, non un suo sostituto, e l’utente può correggere le descrizioni e le annotazioni che contribuiscono a definirla.


___
*Riferimenti:*
- *[I1] [Designing better file organization around tags, not hierarchies](https://www.nayuki.io/page/designing-better-file-organization-around-tags-not-hierarchies)*
- *[I2] [Managing digital photographs](https://karl-voit.at/managing-digital-photographs/)*
- *[I3] [How to Use Tags](https://karl-voit.at/2022/01/29/How-to-Use-Tags/)*
- *[I4] [Attenzione come Convergenza Energetica Geometrica](../references/internal/Attenzione%20come%20Convergenza%20Energetica%20Geometrica.md)*
- *[I5] [A novel idea for a new file system](../references/internal/A%20novel%20idea%20for%20a%20new%20Filesystem.md)*
