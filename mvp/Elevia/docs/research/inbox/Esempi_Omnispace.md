

## 4. Collaborazione e Dataset Condivisi

```
UTENTE A (Neuroscienziato):
  Pubblica: "Motor_Learning_Graph_v2.3"
  Include: 150 paper, 500 atomi, 23 regole inferenziali

UTENTE B (Atleta/Coach):
  Importa il dataset di A nel proprio Omnispace
  Aggiunge: Dati personali (allenamenti, recuperi, performance)
  Esegue Query: "Qual è il protocollo ottimale per skill X?"
  
OUTPUT:
  Il sistema combina conoscenza scientifica (da A) + dati personali (da B)
  → Suggerimento personalizzato basato su evidenze + contesto individuale
```


## 5. Pattern di Inferenza Multipli

```
DATI NEL METAGRAFO:
  (Tutti_gli_ucelli_volano)
  (Pinguino è_un uccello)
  (Pinguino non_volano)
  (Osservo: uccello_sconosciuto X)

DEDUZIONE:
  (X è_uccello) + (Uccelli_volano) → (X vola)

DEFEASIBLE/NON-MONOTONICA:
  Ma se scopro: (X è_Pinguino) → Ritratto: (X non vola)
  Il sistema permette revisione quando arrivano nuovi dati.

ABDUZIONE:
  (Osservo: impronte a 3 dita)
  → Ipotesi migliore: (Uccello è_passato_di_qui)
```


## 8. Esempio: Query con Vincoli di Contesto

```
QUERY BASE:
  "Mostra connessioni tra stress e performance"

QUERY CON VINCOLI:
  QUERY: "Mostra connessioni tra stress e performance"
  FILTRI:
    - Includi: solo studi 2020-2026
    - Escludi: studi su animali
    - Considera: solo popolazione adulta
    - Ordina per: numero_citazioni (decrescente)
  HOP_MAX: 5

QUERY CON FOCUS DINAMICO:
  QUERY: "Analizza pathway dello stress"
  FOCUS_INIZIALE: Cortisolo
  FOCUS_DYNAMICO: true (l'utente può spostare il fuoco durante l'esplorazione)
  ENERGIA: adattiva (decresce con la distanza dal focus corrente)
```


## 9. Esempio: Revisione Defeasible

```
STATO INIZIALE:
  (Antibiotico_A ──Tratta──> Infezione_B)
  (Infezione_B ──Causa──> Febbre)
  
QUERY: "Come trattare la febbre da Infezione_B?"
OUTPUT: "Somministra Antibiotico_A"

NUOVO DATO (resistenza scoperta):
  (Ceppo_Resistente ──Immune_a──> Antibiotico_A)
  (Ceppo_Resistente ──Sostituisce──> Infezione_B)

REVISIONE AUTOMATICA:
  Il sistema NON ritrae automaticamente la conclusione,
  ma segnala all'utente il conflitto:
  ⚠️ "Ceppo_Resistente rilevato. Antibiotico_A potrebbe non essere efficace."

DECISIONE UMANA:
  L'utente valuta e aggiorna:
  (Antibiotico_C ──Tratta──> Ceppo_Resistente)
```

## 10. Campo Gravitazionale del Contesto

Il vincolo di contesto deforma il panorama energetico del grafo, rendendo specifici attrattori più profondi e "invitanti".

```
SCENARIO: Ricerca su "Ferrari"

CONTESTO ATTIVO: [Maranello, Auto Sportiva, Rossa]

GRAFO PRIMA DEL CONTESTO:
  [Ferrari]─────[Lamborghini]─────[Maserati]
       │               │                │
  [Fondatore]    [Sede]           [Storia]
       │               │                │
  [Enzo]       [Sant'Agata]      [Modena]

GRAFO DOPO ATTIVAZIONE CONTESTO:
  Il contesto crea un "bacino di attrazione" verso Ferrari:
  
  [Maranello] ────(forte)────> [Ferrari] ←───(forte)──── [Auto Sportiva]
                                       │
                                  (medio)
                                       │
                                       v
                                 [Rosso]

QUERY: "Storia del marchio"
→ L'energia converge naturalmente su Ferrari, non su Lamborghini o Maserati
→ Hop 1: Ferrari (energia 100%)
→ Hop 2: Fondatore, Maranello, Auto Sportiva (energia 70%)
→ Hop 3: Enzo, Sede stabilimento, Modello iconico (energia 40%)
```


## 11. Annidamento Ricorsivo con Evidenze e Contestazioni

```
LIVELLO 0 - Atomi Base:
  [Caffeina], [Adrenalina], [Aumenta], [Paper_2023], [Contesta], [Osservazione]

LIVELLO 1 - Processo Fisiologico:
  Processo_Caffeina: (Caffeina ──Aumenta──> Adrenalina)

LIVELLO 2 - Evidenza Scientifica:
  Evidenza_A: (Paper_2023 ──Dimostra──> [Processo_Caffeina])
  Evidenza_B: (Meta_analisi_2024 ──Conferma──> [Processo_Caffeina])

LIVELLO 3 - Contestazione:
  Contestazione_X: (Istruttore_Y ──Contesta──> [Evidenza_A])
  Motivazione: (Campione_limitato ──Riduce_affidabilità──> [Evidenza_A])

LIVELLO 4 - Sintesi Utente:
  Valutazione_Utente: 
    (Baricentro_verità ──Pesa──> {[Evidenza_A], [Evidenza_B], [Contestazione_X]})
    → Conclusione: (Effetto ──Probabile──> vero)

QUERY: "Qual è lo stato dell'arte sull'effetto della caffeina?"
OUTPUT:
  Il sistema mostra l'intero annidamento, permettendo all'utente di:
  - Vedere le evidenze a favore
  - Valutare le contestazioni
  - Applicare il proprio criterio di verità
```


## 14. Sintesi Multi-Dominio con Visione d'Insieme

```
SCENARIO: Ricercatore esplora interconnessioni tra domini eterogenei

DOMINI NEL METAGRAFO:
  - Neuroscienze (sonno, memoria, apprendimento)
  - Biochimica (neurotrasmettitori, ormoni)
  - Fisiologia (sistema cardiovascolare, metabolismo)
  - Psicologia (stress, motivazione, attenzione)

QUERY TRASVERSALE:
  "Mostra come lo stress influisce sull'apprendimento motorio"

PERCORSI RILEVATI (grazie alla visione d'insieme):

  PATHWAY 1 (Neuro-endocrino):
    Stress ──Aumenta──> Cortisolo ──Riduce──> BDNF 
    ──Compromette──> Neuroplasticità ──Riduce──> Apprendimento_motorio

  PATHWAY 2 (Cardiovascolare):
    Stress ──Attiva──> Sistema_simpatico ──Aumenta──> Battito 
    ──Compromette──> Coordinazione_fine ──Riduce──> Precisione

  PATHWAY 3 (Psicologico):
    Stress ──Aumenta──> Ansia ──Riduce──> Attenzione 
    ──Compromette──> Feedback_processing ──Riduce──> Consolidamento

  PATHWAY 4 (Sonno):
    Stress ──Riduce──> Qualità_sonno ──Compromette──> REM 
    ──Riduce──> Consolidamento_memoria_procedurale

SINTESI GENERATA:
  "Lo stress compromette l'apprendimento motorio attraverso 4 pathway 
   indipendenti ma convergenti: neuro-endocrino (BDNF), cardiovascolare 
   (coordinazione), psicologico (attenzione) e del sonno (consolidamento). 
   Interventi su uno qualsiasi di questi pathway possono mitigare l'effetto."

VALORE AGGIUNTO:
  Nessuna singola disciplina avrebbe rivelato tutti e 4 i pathway.
  Omnispace connette domini eterogenei per una comprensione sistemica.
```


## 15. LLM Context e Generation Layer

```
SESSIONE DI LAVORO:

  Trascrizione interazione utente:
    U: "Mostrami connessioni tra sonno e memoria"
    S: [Restituisce 5 pathway principali]
    U: "Approfondisci il ruolo del sonno REM"
    S: [Espande il sottografo REM]
    U: "Ci sono studi su privazione del sonno?"
    S: [Filtra per studi su privazione]

LLM CONTEXT (compreso nel Generation Layer):
  - Focus corrente: Sonno_REM → Memoria_dichiarativa
  - Storico sessione: 3 query, 2 approfondimenti
  - Contesto attivo: [Consolidamento, Privazione, Performance_cognitiva]
  - Preferenze utente: Mostra sempre fonti, ordina per anno

QUERY FINALE:
  "Sintetizza cosa abbiamo scoperto"

OUTPUT LLM (Generation Layer):
  "Durante questa sessione abbiamo esplorato il ruolo del sonno REM 
   nel consolidamento della memoria dichiarativa. I punti chiave:
   
   1. Il sonno REM aumenta l'attività ippocampale (Paper_2022, Paper_2024)
   2. La privazione di REM riduce il ricordo del 40% (Meta_analisi_2023)
   3. L'effetto è dose-dipendente: più REM = migliore consolidamento
   
   Vuoi approfondire qualche aspetto o esportare questa sintesi?"

```


## 16. Query con Vincoli di Contesto Complessi

```
QUERY BASE:
  "Analizza effetti della caffeina"

QUERY CON VINCOLI MULTIPLI:

  QUERY: "Effetti della caffeina su performance atletica"
  
  VINCOLI:
    CONTESTO_PRIMARIO: [Performance_atletica, Effetti_acuti]
    CONTESTO_SECONDARIO: [Dosaggio_ottimale, Timing]
    
    FILTRI_INCLUSIONE:
      - Tipo_studio: [RCT, Meta_analisi]
      - Popolazione: [Atleti_adulti, 18-45_anni]
      - Anno: [2015-2026]
      - Lingua: [EN, IT]
    
    FILTRI_ESCLUSIONE:
      - Tipo_studio: [Case_report, Opinione_esperto]
      - Popolazione: [Animali, Bambini, Donne_in_gravidanza]
      - Condizione: [Ipertensione_non_controllata]
    
    CONFIGURAZIONE_ENERGIA:
      HOP_MAX: 5
      ENERGIA_MINIMA_PER_HOP: 15%
      FOCUS_DINAMICO: true
    
    ORDINAMENTO:
      CRITERIO_1: Rilevanza_contesto (decrescente)
      CRITERIO_2: Numero_citazioni (decrescente)
      CRITERIO_3: Anno_pubblicazione (crescente)

OUTPUT ATTESO:
  Sottografo focalizzato su:
  - Dosaggi efficaci (3-6 mg/kg)
  - Timing pre-workout (60 min prima)
  - Tipi di performance (endurance, forza, potenza)
  
  Esclusi:
  - Effetti cardiovascolari (fuori contesto)
  - Studi su popolazione clinica (filtro esclusione)
```

