# Il problema delle cartelle

Il modello a cartelle riprende gli schedari da ufficio: per conservare un documento bisogna scegliere dove metterlo. Nel digitale, però, uno stesso file può appartenere a più categorie. Una foto può riguardare un luogo, un evento e una persona, mentre un percorso come `2009/Vacanze/Roma/IMG_123.jpg` rappresenta soltanto una delle organizzazioni possibili.

I collegamenti permettono di richiamare un file da più posizioni, ma richiedono manutenzione. Quelli simbolici possono rompersi quando il file di destinazione viene spostato; gestire migliaia di collegamenti non risolve il lavoro di classificazione.

Anche il salvataggio richiede decisioni: scegliere un nome che non crei conflitti e una cartella in cui ritrovare il file. Questo lavoro può produrre nomi ridondanti o poco informativi, senza rendere più chiaro il contenuto.


# L'esempio delle applicazioni multimediali

Omvlee osserva che applicazioni come iTunes, iPhoto e Picasa separano la posizione dei file dal modo in cui vengono consultati. L'applicazione gestisce il salvataggio sul disco; la persona sceglie come vedere la propria raccolta.

Una canzone può comparire per artista, album o genere senza essere duplicata. Queste viste dipendono dai metadati, come i tag ID3 per la musica o i dati EXIF per le foto, non dalla cartella che contiene il file. Le diverse faccette (*facets*) permettono di consultare la stessa raccolta secondo criteri diversi.


# I limiti dei tag e delle ontologie globali

Una lista di parole chiave non chiarisce il ruolo di ciascun termine. Il tag `Mozart` può indicare il compositore oppure l'esecutore; `Oro` e `Argento` non dichiarano, da soli, di essere valori della categoria `Materiale`.

Omvlee critica anche l'uso di una gerarchia semantica fissa per tutto il sistema, come nelle proposte basate su WordNet o su ontologie ad albero. Il significato di un termine dipende dal contesto del file: `Ajax` può indicare una squadra di calcio in una raccolta di foto sportive oppure una tecnologia web in documenti di programmazione. Una classificazione globale deve gestire questa ambiguità e adattarsi a significati che cambiano nel tempo.


# Metadati chiave-valore per ogni file

La proposta è associare a ogni file un dizionario di metadati, espresso attraverso coppie `chiave = valore`: per esempio `Autore = John Doe`, `Ruolo = Presentatore` o `Tipo = Contratto`. La chiave specifica che cosa rappresenta il valore.

Le chiavi possono essere definite dalla persona, senza limitarsi ai campi previsti dal software, come artista e album in iTunes. Una stessa chiave può inoltre avere più valori: un articolo può avere più autori e una foto può ritrarre più persone.

Il modello si può leggere come una tabella: ogni riga rappresenta un file, le colonne corrispondono agli attributi e le celle contengono i valori. Una vista, o cartella virtuale, nasce da un'interrogazione sui metadati. Per esempio, si possono cercare tutti i file con `Compositore = Mozart` e `Anno = 1785`, senza spostarli o duplicarli. In un'implementazione basata su database, questa selezione può essere espressa con una query SQL.


# Organizzazione e implementazione

In questo modello, nome e cartella non sono più il modo con cui la persona identifica e ritrova un file. Il sistema assegna un identificativo interno univoco, mentre la consultazione avviene attraverso gli attributi. La posizione fisica resta un dettaglio gestito dal sistema.

Omvlee propone due possibilità di implementazione: integrare il modello nel file system, a livello di kernel, oppure costruire un'applicazione sopra un file system tradizionale. La seconda permette di adottare questa organizzazione mantenendo la compatibilità con i sistemi operativi esistenti.


___
*Questa è una traduzione del Paper di riferimento.*

*Riferimenti:*
- *[I1] [A novel idea for a new file system](../external/a-novel-idea-for-a-new-filesystem.pdf)*
