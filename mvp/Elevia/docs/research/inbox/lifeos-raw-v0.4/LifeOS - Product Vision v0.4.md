*Versione: v0.4*
*Tipo: draft*

---
### La Filosofia
La conoscenza non manca. Manca la capacità di farne inferenza.

Il problema non è raccogliere dati — è connettere ciò che già esiste. Questo tipo di ragionamento è computazionalmente impossibile per un cervello umano su scala: non per limite di intelligenza, ma per limite fisico di attenzione e memoria. L'AI può farlo.

Ma c'è un rischio opposto: delegare il pensiero invece di amplificarlo. Gli strumenti che decidono al posto tuo non ti rendono più intelligente — ti rendono dipendente.

Questo sistema ha un'intenzione opposta: **non sostituire la cognizione umana, ma estenderla**. Il ragionamento rimane tuo. L'AI come protesi cognitiva, non come sostituto.

---
## Il Problema
Gli strumenti attualmente disponibili impongono una struttura rigida, mentre il cervello umano non funziona così: gli input arrivano in modo caotico e i contesti si sovrappongono. Le categorie cognitive sono fluide, imprecise, cambiano nel tempo — fanno sì che l'utente debba adattarsi agli strumenti anziché il contrario.

In quest'epoca eccessivamente veloce, siamo sommersi da un surplus di informazioni, da numerose contraddizioni e verità differenti. Il cervello, non progettato per gestire tale sovraccarico, ha bisogno di essere supportato.

---
## La Risposta
Un sistema che tiene insieme tutto ciò che riguarda la tua vita: idee, attività, conoscenza, tempo. Uno **Spazio Cognitivo Personale** che accetta il caos in ingresso, organizza senza imporre strutture rigide, e restituisce chiarezza in uscita.

Strutturato su **PARA**, mosso dal flusso:

**Cattura → Elaborazione → Connessione → Organizzazione → Azione ↔ Review**

|Fase|Chi|Dove|Cosa succede|
|---|---|---|---|
|**Cattura**|Utente|Dispositivo locale|Il testo in chiaro viene letto solo sul tuo dispositivo|
|**Elaborazione**|Sistema|Dispositivo locale|Le entità vengono estratte e anonimizzate|
|**Connessione**|Sistema|Server|Il motore ragiona sul grafo anonimizzato|
|**Organizzazione**|Sistema|Server|Gli agenti in background rivalutano le relazioni nel tempo|
|**Azione**|Sistema|Dispositivo locale|I risultati vengono decifrati e mostrati a te|
|**Review**|Utente|Dispositivo locale|Validi, correggi o approfondi ciò che il sistema ha portato in superficie|

Il sistema si muove su due modalità:

- **Automatica (Routine)** — il server ragiona in background, anche quando il dispositivo è spento. Quando riapri il sistema, le connessioni nuove sono già pronte. E per eventuali automatismi, decisi dall'utente.
- **Consapevole (Workflow)** — quando decidi di fermarti, guardare e intervenire.

---
## Come Pensa il Sistema

**Non dimentica. Decide cosa mostrarti prima.** Ogni informazione che entra viene sempre conservata nella sua forma originale (RAW). Il sistema non cancella: comprime, collega, e porta in superficie solo ciò che è rilevante nel momento. Quando serve, risale fino alla fonte originale.

**Conosce il tempo.** Le informazioni non sono statiche. Se oggi vivi a Milano e tra sei mesi ti trasferisci a Barcellona, il sistema aggiorna il fatto attivo — ma conserva la storia. Ogni relazione nel grafo porta un peso probabilistico che varia nel tempo: il sistema sa cosa era vero ieri, cosa è vero oggi, e permette di risalire all'evoluzione nel tempo. Non è un archivio: è una memoria viva.

**Ragiona senza vederti.** Il motore di calcolo lavora esclusivamente su identificatori anonimi. Non conosce il tuo nome, né quello delle persone che menzioni, né il contenuto delle tue note. Vede solo la struttura delle relazioni. La chiave per riportare tutto al significato reale non lascia mai il tuo dispositivo. Questo non è una promessa: è una garanzia architetturale. → _Vedi: Privacy Architecture v0.4_

**Si costruisce attorno a te.** Il sistema impara i tuoi pattern, i tuoi contesti ricorrenti, le tue connessioni più forti. Con il tempo, anticipa. Non chiede di classificare tutto manualmente: propone, e tu confermi o correggi con un'azione singola.

---
## Principi Fissi

- **Si adatta al cervello dell'utente**, non il contrario.
- **Ogni utente ha il proprio spazio cognitivo privato.**
- **Il server è potente ma cieco.** Calcola tutto, vede solo struttura.
- **La chiave non lascia mai il dispositivo.** Partially-Zero-knowledge by design.
- **Nessun dato viene mai perso.** Il RAW originale è sempre conservato.
- **Semplicità come default.**
- **Nessuna modifica senza conferma esplicita.**
- **Aperto.** Integra qualsiasi strumento o dato l'utente voglia includere.
- **Zero attrito in ingresso.** Il caos è accettato. L'ordine emerge dopo.
- **Ridurre il carico cognitivo**, non aumentarlo.

---
## Perché Esiste

Come le aziende, anche noi abbiamo bisogno di dati per prendere decisioni consapevoli. Per questo nascono le **Life-Metrics**: la stessa potenza decisionale delle analytics aziendali, applicata al benessere personale.

Su questa base emergono in modo naturale strumenti di direzione come gli **OKR personali**: non imposti dall'alto, ma guidati dai dati reali. In questo modo si passa dal rumore informativo a scelte consapevoli, veloci e mirate — mantenendo allineati ciò che si vuole ottenere e ciò che accade davvero.

---

## Il Modello Privacy — Il Motore Cieco

Il sistema è costruito su un principio chiamato **zero-knowledge**: il server che esegue il calcolo non può mai risalire alle informazioni reali dell'utente.

Funziona così:

Le tue note (in chiaro)
    │
    │  solo sul tuo dispositivo
    ├──────────────────────────────────────────────┐
    │                                              │ cifrate con la tua chiave
    ▼                                              ▼
Anonimizzazione                          Backup RAW sul server
    "Cliente Rossi"  →  ID_999           (blob cifrato — il server
    "Azienda X"      →  ID_444            non può aprirlo senza
    │                                     la tua chiave, che non
    │  solo ID escono dal dispositivo      lascia mai il dispositivo)
    ▼
Server (Il Motore Cieco)
    Ragiona su ID_999, ID_444
    Trova connessioni, pattern, inferenze
    Non sa chi sono
    │
    │  risultati anonimi tornano al dispositivo
    ▼
Decifratura locale
    ID_999  →  "Cliente Rossi"
    │
    ▼
Quello che vedi tu

Il server è potente — esegue tutto il calcolo pesante, ragiona su milioni di relazioni, fa girare agenti in background 24 ore su 24. Ma è strutturalmente cieco: anche se venisse compromesso, non conterrebbe nulla di leggibile.

