# L'idea di un network di conoscenza

Ogni utente può pubblicare il proprio **Space personale**, rappresentativo, ad esempio, delle proprie conoscenze ed esperienze, rendendolo consultabile dagli altri utenti che scelgono di condividerlo. Gli Space possono quindi essere utilizzati anche in **modalità collaborativa**

- **Limite Funzionale — Embodied Experience:** questa visione incontra il limite delle **esperienze incarnate**, che per loro natura non possono essere digitalizzate o trasferite integralmente nel sistema.
- **Selezione delle Fonti:** ogni utente decide autonomamente quali fonti importare nel proprio Space, mantenendo il controllo sulla conoscenza che intende integrare e condividere.
- **Obiettivo Finale:** sviluppare una piattaforma aperta per la **condivisione e costruzione collaborativa della conoscenza**, orientata all'apprendimento, all'auto-potenziamento e alla crescita personale.


# Pattern Matching

In futuro, **Space** potrà supportare le **Variabili**, utilizzate per costruire pattern — cioè Expression contenenti elementi non specificati — che possono essere confrontati con altre strutture dello Space per determinare le corrispondenze delle variabili.

_Esempio:_ `(Parent $x $y)` può corrispondere a `(Parent Marco Luca)`, producendo il binding `$x = Marco` e `$y = Luca`.

Il **Pattern Matching** dovrà essere progettato tenendo conto della natura potenzialmente vaga e sfumata della conoscenza: le regole troppo generiche rischiano di produrre corrispondenze e inferenze poco significative. Potrebbe quindi essere necessario introdurre successivamente **Type e vincoli semantici** per rendere le corrispondenze più precise. Dando la possibilità di creare conoscenza nuova derivata.


# Modellazione Avanzata della Conoscenza

Poiché vorremo rendere il linguaggio **Turing-completo**, il sistema offre un'estensibilità nativa per la creazione e l'esecuzione di strumenti analitici e cognitivi avanzati custom (es. _modelli decisionali, motori inferenziali, simulazioni_).

Dando la possibilità di Variabili Grounded a dati provenienti da altre fonti (datset, API, stream file, ecc)
