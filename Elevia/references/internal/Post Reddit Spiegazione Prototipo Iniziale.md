# English Version

Hi everyone,

A few days ago I made another post about a similar idea, but I would like to explain it better and hear your opinions.

The question I am starting from is:

> **What if knowledge could be shared not only as documents, but as a common structured representation?**

Today, most knowledge is stored as text: papers, books, databases, and code. The problem is that it remains fragmented: often an important relationship already exists, but it is distributed across different sources and has to be manually reconstructed by a person.

The idea is to create an intermediate format where knowledge can be extracted, normalized, and then combined with other knowledge coming from different sources.

My intuition is to use **metagraphs** as the underlying representation. Not because I think they literally represent human thought, but because they seem closer to the way humans organize complex ideas: concepts are rarely isolated, but usually nested inside other concepts, connected through multiple layers of relationships, context, and abstraction.

Unlike traditional graphs, metagraphs can also represent relationships between relationships, which could be useful for modeling more complex structures of knowledge.

A possible pipeline could look like this:

```
Source → Extraction → Grounding → Metagraph Representation
```

The grounding phase would transform concepts expressed in natural language into shared canonical entities and relationships.



For example, two independent laboratories could produce separate pieces of knowledge.

### Source A

The first laboratory studies a drug:
`file: source_a.thinking`

```
; ========================================
; SOURCE A (Genetics Lab)
; ========================================

; --- Grounded Types ---
(: Drug Type)
(: Protein Type)
(: Biological_Process Type)

; --- Grounded Entities ---
(: Drug_A Drug)
(: EGFR Protein)
(: Tumor_Growth Biological_Process)

; --- Source Assertions ---
(stimulates EGFR Tumor_Growth)
(inhibits Drug_A EGFR)
```

This representation says only:
- **EGFR** stimulates the **tumor growth** process.
- **Drug_A** inhibits **EGFR**.

### Source B

A second laboratory studies another mechanism:
`file: source_b.thinking`

```
; ========================================
; SOURCE B (Biochemistry Lab)
; ========================================

; --- Grounded Entities ---
(: Drug_B Drug)
(: MET Protein)
(: Tumor_Growth Biological_Process)

; --- Source Assertions ---
(stimulates MET Tumor_Growth)
(inhibits Drug_B MET)
```

This second source says only:
- **MET** stimulates **tumor growth**.
- **Drug_B** inhibits **MET**.

## Combining Knowledge in OmniSpace

The next step would be compiling all `.thinking` files into a representation better suited for graph algebra and GPU-based parallel processing. All these representations would be temporarily merged into a global space that I currently call **OmniSpace**.

OmniSpace would represent a snapshot of the available knowledge at a given moment. The interesting part is that, once thousands or millions of independent representations are combined, the graph could make previously hidden connections visible.

For example, by looking at the global graph compiled, a researcher might see:

Plaintext

```
Drug_A
  │
inhibits
  ↓
 EGFR
  │
stimulates
  ↓
Tumor_Growth
  ↑
stimulates
  │
 MET
  ↑
inhibits
  │
Drug_B
```

From this structure, a question could emerge:

> _"Could there be a compensatory mechanism between EGFR and MET that explains treatment resistance?"_

## Human-Centric Discovery

The system should not automatically provide a final answer. Instead, it should increase the ability of humans to explore knowledge by showing relationships, paths, and connections that would be difficult to discover by reading thousands of separate documents.

I would not want the system to automatically write scientific rules or decide what is true and what is false. The hardest part of knowledge is not only finding information, but determining:

1. Which relationships are meaningful?
2. Which inferences are valid?
3. Which conclusions are scientifically correct?

Those responsibilities should remain human.

## Motivation and Challenges

The motivation comes from a common experience: many times, while learning a new topic, I later discover a better approach or an important connection that was already somewhere on the Internet. The problem is not always the lack of knowledge, but the fact that knowledge is fragmented and disconnected.

The goal of this system would be to explore a different way of representing knowledge: not as a collection of documents, but as a structure that can be shared, composed, and navigated.

One of the biggest challenges I see is that **representing knowledge is not the same as understanding it**. A graph can expose connections, but deciding whether those connections represent meaningful knowledge still requires human judgment.

## Questions for the Community

I would like to hear your thoughts. In particular:

- **Are there similar projects** that I should look into?
- **What do you think are the main limitations** of this approach?
- **Do metagraphs seem like a suitable structure** for complete expression of human thought?

Thanks everyone in advance!

# Versione Italiana

Ciao a tutti,

Qualche giorno fa ho pubblicato un altro post su un'idea simile, ma vorrei spiegarla meglio e conoscere le vostre opinioni.

La domanda da cui parto è questa:

> **E se la conoscenza potesse essere condivisa non solo sotto forma di documenti, ma anche come una rappresentazione strutturata comune?**

Oggi la maggior parte della conoscenza è conservata sotto forma di testo: articoli scientifici, libri, database e codice. Il problema è che rimane frammentata: spesso una relazione importante esiste già, ma è distribuita tra fonti diverse e deve essere ricostruita manualmente da una persona.

L'idea è creare un formato intermedio in cui la conoscenza possa essere estratta, normalizzata e poi combinata con altra conoscenza proveniente da fonti differenti.

La mia intuizione è utilizzare i **metagrafi** come rappresentazione di base. Non perché ritenga che rappresentino letteralmente il pensiero umano, ma perché mi sembrano più vicini al modo in cui gli esseri umani organizzano idee complesse: i concetti sono raramente isolati, ma sono generalmente annidati all'interno di altri concetti e collegati attraverso molteplici livelli di relazioni, contesto e astrazione.

A differenza dei grafi tradizionali, i metagrafi possono rappresentare anche relazioni tra relazioni, caratteristica che potrebbe risultare utile per modellare strutture di conoscenza più complesse.

Una possibile pipeline potrebbe essere la seguente:

```
Sorgente → Estrazione → Grounding → Rappresentazione come Metagrafo
```

La fase di _grounding_ trasformerebbe i concetti espressi in linguaggio naturale in entità e relazioni canoniche condivise.

Per esempio, due laboratori indipendenti potrebbero produrre due insiemi distinti di conoscenza.

### Sorgente A

Il primo laboratorio studia un farmaco:
`file: source_a.thinking`

```lisp
; ========================================
; SOURCE A (Genetics Lab)
; ========================================

; --- Grounded Types ---
(: Drug Type)
(: Protein Type)
(: Biological_Process Type)

; --- Grounded Entities ---
(: Drug_A Drug)
(: EGFR Protein)
(: Tumor_Growth Biological_Process)

; --- Source Assertions ---
(stimulates EGFR Tumor_Growth)
(inhibits Drug_A EGFR)
```

Questa rappresentazione afferma semplicemente che:

- **EGFR** stimola il processo di **crescita tumorale**.
- **Drug_A** inibisce **EGFR**.

### Sorgente B

Un secondo laboratorio studia un altro meccanismo:
`file: source_b.thinking`

```lisp
; ========================================
; SOURCE B (Biochemistry Lab)
; ========================================

; --- Grounded Entities ---
(: Drug_B Drug)
(: MET Protein)
(: Tumor_Growth Biological_Process)

; --- Source Assertions ---
(stimulates MET Tumor_Growth)
(inhibits Drug_B MET)
```

Questa seconda sorgente afferma semplicemente che:

- **MET** stimola la **crescita tumorale**.
- **Drug_B** inibisce **MET**.

## Combinare la conoscenza in OmniSpace

Il passo successivo sarebbe compilare tutti i file `.thinking` in una rappresentazione più adatta all'algebra dei grafi e all'elaborazione parallela su GPU. Tutte queste rappresentazioni verrebbero temporaneamente fuse in uno spazio globale che, per ora, chiamo **OmniSpace**.

OmniSpace rappresenterebbe un'istantanea della conoscenza disponibile in un determinato momento. L'aspetto interessante è che, una volta combinate migliaia o milioni di rappresentazioni indipendenti, il grafo potrebbe rendere visibili connessioni che prima erano nascoste.

Per esempio, osservando il grafo globale compilato, un ricercatore potrebbe vedere:

```text
Drug_A
  │
inibisce
  ↓
 EGFR
  │
stimola
  ↓
Crescita_Tumorale
  ↑
stimola
  │
 MET
  ↑
inibisce
  │
Drug_B
```

Da questa struttura potrebbe emergere una domanda:

> _"Potrebbe esistere un meccanismo compensatorio tra EGFR e MET che spiega la resistenza ai trattamenti?"_

## Una scoperta centrata sull'essere umano

Il sistema non dovrebbe fornire automaticamente una risposta definitiva. Piuttosto, dovrebbe aumentare la capacità degli esseri umani di esplorare la conoscenza mostrando relazioni, percorsi e connessioni che sarebbero difficili da individuare leggendo migliaia di documenti separati.

Non vorrei che il sistema scrivesse automaticamente regole scientifiche o decidesse cosa è vero e cosa è falso. La parte più difficile della conoscenza non consiste soltanto nel trovare informazioni, ma nel determinare:

1. Quali relazioni sono realmente significative?
2. Quali inferenze sono valide?
3. Quali conclusioni sono scientificamente corrette?

Queste responsabilità dovrebbero rimanere in capo agli esseri umani.

## Motivazione e sfide

L'idea nasce da un'esperienza comune: molte volte, mentre studio un nuovo argomento, mi accorgo solo in seguito che esisteva già un approccio migliore o una connessione importante, nascosta da qualche parte su Internet. Il problema non è sempre la mancanza di conoscenza, ma il fatto che la conoscenza sia frammentata e scollegata.

L'obiettivo di questo sistema sarebbe esplorare un modo diverso di rappresentare la conoscenza: non come una semplice raccolta di documenti, ma come una struttura che possa essere condivisa, composta e navigata.

Una delle sfide più grandi che vedo è che **rappresentare la conoscenza non equivale a comprenderla**. Un grafo può mettere in evidenza delle connessioni, ma stabilire se tali connessioni rappresentino davvero conoscenza significativa richiede comunque il giudizio umano.

## Domande per la community

Mi farebbe piacere conoscere le vostre opinioni. In particolare:

- **Esistono progetti simili** che dovrei approfondire?
- **Quali ritenete siano i principali limiti** di questo approccio?
- **I metagrafi vi sembrano una struttura adatta** per rappresentare in modo completo il pensiero umano?

Grazie a tutti in anticipo!
