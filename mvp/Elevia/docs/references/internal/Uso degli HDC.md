
___
# Hyperdimensional Computing (HDC)

## Vantaggi e Svantaggi

### Vantaggi

- **Efficienza energetica:** Particolarmente adatto per hardware neuromorfico, FPGA e sistemi embedded ad altissima efficienza energetica.
    
- **Ricerca accademica avanzata:** Ampiamente utilizzato in laboratori di AI avanzata e settori ad alta tecnologia (es. IBM Research, Difesa e Aerospaziale).
    
- **Nessun codice di controllo esplicito:** Le relazioni logiche ed emergenti derivano dalle proprietà matematiche pure dell'algebra geometrica, senza bisogno di regole condizionali rigide.

### Svantaggi

- **Paradigma prevalentemente sperimentale:** Tecnologia attualmente non pronta per progetti di produzione industriale su larga scala.
    
- **Curva di apprendimento ripidissima:** Richiede solide competenze matematiche e una profonda comprensione dell'algebra astratta avanzata.
    
- **Librerie non plug-and-play:** Assenza di framework standardizzati; quasi tutte le librerie disponibili sono componenti di ricerca personalizzati.
    
- **Saturazione della memoria (_Interference_):** Un singolo ipervettore possiede una capacità teorica massima; sommare troppi dati (es. 100 GB) distrugge le informazioni a causa del rumore numerico.
    
- **Necessità di _Distributed Item Memory_:** Per evitare la saturazione, i dati devono essere suddivisi e distribuiti all'interno di una rete di memorie vettoriali interconnesse anziché in un unico vettore.
    
- **Design accurato dell'algebra vettoriale:** È richiesta una progettazione con precisione matematica assoluta:
    
    - **Commutatività vs. Non-Commutatività:** Per preservare l'ordine temporale o causale delle relazioni (es. _Causa → Effetto_, _Prima → Dopo_), occorre impiegare operatori non commutativi (permutazioni di bit, moltiplicazioni di matrici).
        
    - **Ortogonalità:** L'operazione di _Binding_ deve produrre vettori strettamente ortogonali rispetto a quelli di partenza per prevenire interferenze.
        
    - **Gerarchie e sistemi di tipi:** La rappresentazione di relazioni nidificate (es. _Cane → Mammifero → Animale_) necessita di spazi vettoriali nidificati o proiezioni algebriche complesse (come le algebre FHRR o MAP).

## Note di Progettazione HDC

Per applicare l'HDC a un problema di classificazione (audio o di altra natura), è necessario seguire questa pipeline procedurale:

1. **Definizione dei dati di ingresso:** Estrarre caratteristiche significative dai dati grezzi (_feature extraction_), evitando di alimentare il sistema con dati casuali o eccessivamente rumorosi.
    
2. **Codifica in ipervettori (_Encoding_):** Convertire le informazioni in vettori ad alta dimensione assicurandosi che la codifica preservi le relazioni di similarità tra i dati originali.
    
3. **Applicazione delle operazioni HDC fondamentali:**
      
    - **Binding:** Per combinare e legare informazioni di natura diversa.
        
    - **Bundling:** Per sovrapporre e aggregare informazioni simili.
        
    - **Permutation:** Per rappresentare l'ordine sequenziale o la posizione spaziale/temporale.
        
4. **Creazione dei prototipi di classe:** Durante la fase di addestramento, aggreagare gli esempi appartenenti a ciascuna categoria per definire un rappresentante stabile per ogni classe.
    
5. **Selezione della metrica di confronto:** Confrontare i nuovi elementi con i prototipi memorizzati utilizzando idonee metriche di similarità (es. similarità coseno, distanza di Hamming).
    
6. **Controllo di qualità dei dati:** Garantire la normalizzazione dei vettori, l'eliminazione del rumore, il bilanciamento delle classi e la presenza di un numero sufficiente di campioni.
    
7. **Verifica della generalizzazione:** Testare il modello su dataset non visti in fase di addestramento per valutarne le capacità di generalizzazione.
    

8. **Tuning dei parametri HDC:** Calibrare finemente la dimensione degli ipervettori (es. $D = 10.000$), la tipologia dei vettori (binari, bipolari, reali) e la strategia di aggiornamento dei prototipi.

> **In sintesi:**
> 
$$\text{Dati puliti} \longrightarrow \text{Feature significative} \longrightarrow \text{Encoding corretto} \longrightarrow \text{Operazioni HDC} \longrightarrow \text{Prototipi} \longrightarrow \text{Confronto} \longrightarrow \text{Generalizzazione}$$
> 
> La componente critica di qualsiasi architettura HDC è l'**encoding**: un buon metodo di codifica combinato con un classificatore semplice garantisce elevate prestazioni; al contrario, una codifica errata produrrà esclusivamente vettori privi di significato informativo.

___