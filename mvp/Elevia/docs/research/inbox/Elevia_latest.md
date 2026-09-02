***Versione:** 1.5
***Data:** Agosto 2026*
***Stato:** Bozza*

***Nota:** il nome **Elevia** è provvisorio e verrà sostituito, poiché non disponibile.*

***Nota:** sto valutando se trasformarlo in un paper collaborativo. Servirà una struttura decisionale (es. ad albero) e tool gestionali per organizzare i contributi senza disperdere le idee migliori.*


# 3. Space
___
## 3.1 Introduzione

**Space** è lo stato rappresentazionale della conoscenza: uno spazio strutturato e composizionale basato sugli **Atomi**, attraverso cui è possibile rappresentare entità, concetti, relazioni e valori. Nasce dall'idea di avvicinare la rappresentazione della conoscenza alla **struttura ricorsiva del pensiero umano**, puntando a una **Completezza Espressiva** paragonabile a quella del linguaggio naturale. Creando un sistema Simbolico-Probabilistico.

il formato Space serve perchè così il sistema capisce costa gli stiamo dando in pasto. Darli la possibilità di caricare qualsiasi file caricato, il sistema non capisce la struttura.

Ce il problema estrarre conoscenza da un file Space e ogni singolo file le sue robe all interno hanno vicinanza massima visto lo stesso file.

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

LE query Espressivamente complete, devono essere in qualche modo come un utente scrive ad un LLM che scrive qualsiasi parola e frase nel modo suo, e LLM capisce.

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
9. Basta imitare soltanto la Memoria Associativa? Penso che tutto: regole inferenza, deduzione, ecc. Deriva da quest'ultima, è solo che noi la chiamiamo deduzione, ma è un eco della memoria associativa, perchè ci sono più concetti attivi nella testa e quindi associamo. Non so se hai capito. Tipo esempio stavo parlando del mio piede che è cavo, ed ho associato nella mia testa con un ragionamento distante, e quindi nella mia testa si è attivato il concetto di supino, perchè l'arco plantare tende a supinare, e quindi nella mia testa si è ora avvicinato il concetto di mignolo vago. Questo meccanismo è la chiave. E funziona anche con cose indirette che hanno un filo conduttore. Questa è la generalizzazione.
10. Da considerare bacini di attrazione Energy Based Model
11. non ha senso partire con la sintassi (qualcosa qualcosa), è una cosa per dopo. Il vettore non è il piano B quando il simbolico fallisce. È una rappresentazione complementare che viene generata comunque. No, serve soltanto per il simbolico direi.
12. Il significato delle parole avviene per associazione. La singola parola non vuol dire niente. E considera anche il contesto.


## 2.2 Esplorazione del sistema

## 2.3 Estrazione delle Regole

Dall'esplorazione delle connessioni, il sistema cristallizza nuove regole logiche. Esempio: se apprende che l'acqua bolle a 100 °C e congela a 0 °C, da queste osservazioni può generarsi una regola sul comportamento dell'acqua rispetto alla temperatura.

La definizione delle regole avviene in due modi:

- **Manuale** — l'utente la formula direttamente;
- **Automatica** — il sistema la propone e l'utente la valida (coerentemente con il principio _Human in the Loop_).

___


📝 Appunto per il Modello: Cognitive-Science-Grounded Ontology Generation

**Definizione sintetica:**  
La _cognitive-science-grounded ontology generation_ è il processo con cui un'I.A. crea mappe concettuali (ontologie) strutturate imitando il modo in cui il cervello umano organizza, percepisce e sperimenta il mondo reale. A differenza delle ontologie classiche (che sono rigide e solo logico-matematiche), questa unisce la logica del computer con la flessibilità della psicologia cognitiva e delle neuroscienze.

Agisce come una **memoria associativa spiegata**: non si limita a unire i concetti per "vicinanza" o statistica, ma definisce la relazione esatta tra di essi basandosi sulle esperienze umane.

---

💡 Esempio Semplice (Da usare come analogia)

- **Approccio Ontologico Classico (Rigido):**  
    Se chiedi al computer di definire una **"Tazza"**, creerebbe una regola matematica: _"Un cilindro cavo con un manico laterale, fatto di ceramica, con un diametro tra 7 e 12 cm"_.  
    _Il problema:_ Se il computer vede una tazza quadrata, una tazza di plastica per bambini o un thermos senza manico pieno di tè caldo, rischia di non riconoscerli perché non rispettano i parametri freddi del database.
- **Approccio Basato sulle Scienze Cognitive (Flessibile e Umano):**  
    Il computer genera un'ontologia basata sulle **esperienze e sulle azioni umane** (_Grounded Cognition_). Collega il concetto di "Tazza" all'azione motoria di _afferrare con la mano_ e allo scopo di _contenere un liquido caldo da bere_.  
    _Il risultato:_ Se il computer si imbatte in un cilindro di cartone senza manico ma pieno di caffè bollente, capirà che l'essere umano lo userà come una tazza. L'I.A. riconosce l'oggetto perché ragiona sulle _sensazioni fisiche_ e sui _bisogni_ dell'utente, non solo sulle geometrie.

Deriva da questo: Cognee is an open-source AI memory platform for AI Agents. Ingest data in any format, and Cognee continuously builds a self-hosted knowledge graph that gives your agents persistent long-term memory across sessions. Cognee combines vector embeddings, graph reasoning, and cognitive-science-grounded ontology generation to make documents both searchable by meaning and connected by relationships that evolve as your knowledge does.

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

