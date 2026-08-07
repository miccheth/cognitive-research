*Versione: v0.4*
*Tipo: draft*

---
## Valutazione Generale
Il progetto è genuinamente differente da ciò che esiste oggi. Nessun PKMS attuale combina ragionamento simbolico persistente nel tempo, privacy architetturale partially-zero-knowledge e un modello pro attivo che porta in superficie informazioni senza che l'utente chieda. Notion, Obsidian, Roam — nessuno ragiona, tutti archiviano. Questo sistema pensa.

Il successo dipende dalla risoluzione dei rischi qui sotto.

---
## Rischi Critici
#### R1 — Latenza Percepita
**Stato: Aperto**

Se scrivo una nota e il suggerimento pro attivo arriva 30 secondi dopo, l'utente non capisce il valore. Se arriva in 2 secondi, è magia. La differenza tra successo e fallimento sta lì.

**Direzione di risoluzione:** separare i layer per latenza. Layer 2 (semantico) deve rispondere sotto il secondo. Layer 3 (inferenza profonda) può lavorare in background e presentare i risultati in modo asincrono — non come risposta immediata, ma come suggerimento che appare al momento giusto.

---
#### R2 — Cold Start
**Stato: Aperto**

Un sistema che "impara i tuoi pattern" è inutile il primo mese. L'esperienza dei primi 30 giorni deve essere utile anche prima che il grafo sia ricco. E bisogna gestire il primo onboarding dell'utente, se vuole importate i suoi contenuti da un'altra piattaforma.

**Direzione di risoluzione:** progettare un'esperienza di onboarding che fornisce valore immediato. Nella prima fase, il sistema funziona come una buona app di produttività (Layer 1). Il Layer 2 si attiva già con poche note. Il Layer 3 richiede più dati, ma non viene proposto all'utente finché non c'è abbastanza contesto per essere utile.

---
#### R3 — Complessità Architetturale
**Stato: Da monitorare**

OpenCog, DAS, LLM locale, Mappa ID cifrata, Vector DB — lo stack è potente ma complesso da mantenere e spiegare. Ogni componente aggiunge un punto di fallimento.

**Direzione di risoluzione:** progettare ogni componente come sostituibile in modo indipendente. Il sistema non deve dipendere da una versione specifica di OpenCog per funzionare a livello base.

---
## Decisioni Aperte

Queste idee sono state valutate ma non ancora assegnate a uno scope.

| Idea                                              | Stato       | Note                                                                                        |
| ------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------- |
| Spaces e Collections                              | Da decidere | Entità non ancora definite nella struttura; capire se sono alias di PARA o livelli separati |
| Condivisione parziale della Mind con altri utenti | Da decidere | Già in roadmap come "Team (futuro)" nella Spec — confermato fuori da v1                     |
| Frontend dinamico basato sul profilo utente       | Da decidere | Principio già incluso nella Spec; definire i limiti della personalizzazione automatica      |
