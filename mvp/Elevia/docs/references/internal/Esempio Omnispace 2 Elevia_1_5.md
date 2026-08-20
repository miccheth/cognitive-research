
## Panoramica

**Scenario:** Un ricercatore vuole esplorare le connessioni tra "Cambiamento Climatico" e "Sicurezza Alimentare". Il sistema rivela non solo il percorso diretto (temperature → agricoltura → produzione cibo), ma anche percorsi trasversali (migrazioni → instabilità politica → interruzioni supply chain → accesso al cibo).

**Allineamento con Elevia v1.5 (sezioni 1-3):**
- **Manifesto:** liberare risorse mentali per funzioni cognitive superiori, rendere visibili connessioni latenti
- **Space:** rappresentazione composizionale basata su Atomi (Symbol, Expression, Primitive)
- **Pipeline:** Ingestion → Compilation → Session → Generation


## FASE 0: Ingestion Layer

### Conoscenza Importata da 4 Fonti Multidominio

```
┌─────────────────────────────────────────────────────────────────┐
│  INPUT: Linguaggio non strutturato da fonti esterne             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Fonte: IPCC Climate Report 2023]                              │
│  "Le temperature globali sono aumentate di 1.1°C rispetto       │
│   all'era pre-industriale. Gli eventi estremi (siccità,         │
│   alluvioni) sono aumentati del 40% negli ultimi 20 anni."      │
│                                                                  │
│  [Fonte: FAO Agriculture 2023]                                  │
│  "La resa delle colture principali (grano, riso, mais) è        │
│   diminuita del 5-15% nelle regioni tropicali. La sicurezza     │
│   alimentare è compromessa per 828 milioni di persone."         │
│                                                                  │
│  [Fonte: World Bank Migration 2022]                             │
│  "Le migrazioni climatiche hanno interessato 21 milioni di      │
│   persone nel 2021. Le regioni più colpite: Sahel, Sud-est      │
│   asiatico, America centrale."                                  │
│                                                                  │
│  [Fonte: Nature Geopolitics 2023]                               │
│  "L'instabilità politica correlata al clima ha causato 12       │
│   conflitti per le risorse naturali dal 2020. Le supply chain   │
│   alimentari sono interrotte in 8 regioni critiche."            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Trasformazione in Space (manuale o automatizzata)

```
┌─────────────────────────────────────────────────────────────────┐
│  SPACE FILE: climate_food_security_001.space                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ;; Fonte: IPCC Climate Report 2023                             │
│  (GlobalTemperature Aumenta 1.1C)                               │
│  (GlobalTemperature Causa EventiEstremi)                        │
│  (EventiEstremi Include Siccità)                                │
│  (EventiEstremi Include Alluvioni)                              │
│  (EventiEstremi AumentatoPercentuale 40)                        │
│                                                                  │
│  ;; Fonte: FAO Agriculture 2023                                 │
│  (GlobalTemperature Riduce ResaColture)                         │
│  (ResaColture Per Colture Grano)                                │
│  (ResaColture Per Colture Riso)                                 │
│  (ResaColture Per Colture Mais)                                 │
│  (ResaColture DiminuitaPercentuale 5-15)                        │
│  (ResaColture Influenza SicurezzaAlimentare)                    │
│  (SicurezzaAlimentare CompromessaPersone 828000000)             │
│                                                                  │
│  ;; Fonte: World Bank Migration 2022                            │
│  (EventiEstremi Causa MigrazioniClimatiche)                     │
│  (MigrazioniClimatiche Persone 21000000 Anno 2021)              │
│  (MigrazioniClimatiche Regione Sahel)                           │
│  (MigrazioniClimatiche Regione SudEstAsia)                      │
│  (MigrazioniClimatiche Regione AmericaCentrale)                 │
│                                                                  │
│  ;; Fonte: Nature Geopolitics 2023                              │
│  (MigrazioniClimatiche Influenza InstabilitàPolitica)           │
│  (InstabilitàPolitica Causa ConflittiRisorse)                   │
│  (ConflittiRisorse Numero 12 DalAnno 2020)                      │
│  (InstabilitàPolitica Interrompe SupplyChain)                   │
│  (SupplyChain Tipo Alimentare)                                  │
│  (SupplyChain InterrottaRegioni 8)                              │
│  (SupplyChain Influenza AccessoCibo)                            │
│  (AccessoCibo ParteDi SicurezzaAlimentare)                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Nota Ingestion Layer:**
- Processo automatizzato: LLM considera contesto complessivo, preserva relazioni e sfumature
- Processo manuale: ricercatore verifica e corregge estrazione
- Obiettivo: trasformare linguaggio fluido in conoscenza strutturata Space

---
## FASE 1: Compilation Layer

### Syntax Check

```
┌─────────────────────────────────────────────────────────────────┐
│  Verifica formalmente valida per ogni Space                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ✓ (GlobalTemperature Aumenta 1.1C)        → VALIDO             │
│  ✓ (EventiEstremi Include Siccità)         → VALIDO             │
│  ✓ (ResaColture Per Colture Grano)         → VALIDO             │
│  ✓ (MigrazioniClimatiche Persone 21000000  → VALIDO             │
│     Anno 2021)                                                   │
│  ✗ (GlobalTemperature Causa                → ERRORE             │
│     ;; manca chiusura parentesi                                  │
│                                                                  │
│  Risultato: 23 Expression valide, 1 errore corretto              │
│  Output: Alberi di espressione creati per ciascun Space         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Canonical Grounding

```
┌─────────────────────────────────────────────────────────────────┐
│  Normalizzazione termini concettuali e relazionali              │
│  (Inglese come Pivot, mappe lessicali preinstallate)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Originali → Normalizzati:                                      │
│  - "temperature globali", "global warming" → GlobalTemperature  │
│  - "eventi estremi", "extreme weather" → ExtremeEvents          │
│  - "sicurezza alimentare", "food security" → FoodSecurity       │
│  - "supply chain", "catena di approvvigionamento" → SupplyChain │
│  - "aumento", "increased" → Increases                           │
│  - "riduce", "decreases" → Decreases                            │
│  - "causa", "provoca" → Causes                                  │
│  - "influenza", "affects" → Affects                             │
│                                                                  │
│  Nomi propri e valori mantenuti invariati:                      │
│  - "Sahel" → Sahel                                              │
│  - "1.1°C" → 1.1C                                               │
│  - "828 milioni" → 828000000                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Semantic Atom Resolution

```
┌─────────────────────────────────────────────────────────────────┐
│  Identificazione Symbol differenti per stesso concetto          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Equivalenze linguistiche identificate:                         │
│  - "Crops" e "Colture" → stesso concetto (Colture)              │
│  - "Yield" e "ResaColture" → stesso concetto (CropYield)        │
│  - "Conflict" e "ConflittiRisorse" → contesto diverso           │
│    (Conflict generico vs ConflittiRisorse specifico)            │
│                                                                  │
│  Distinzioni concettuali preservate:                            │
│  - "FoodSecurity" e "AccessoCibo" → correlati ma diversi        │
│    (FoodSecurity = concetto ampio, AccessoCibo = componente)    │
│  - "MigrazioniClimatiche" e "MigrazioniEconomiche" → diversi    │
│    (cause differenti, anche se effetto simile)                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Indexing

```
┌─────────────────────────────────────────────────────────────────┐
│  Costruzione indici per navigazione rapida                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Indice per Atomo → Expression contenenti:                      │
│                                                                  │
│  GlobalTemperature → [                                          │
│    (GlobalTemperature Increases 1.1C),                          │
│    (GlobalTemperature Causes ExtremeEvents),                    │
│    (GlobalTemperature Decreases CropYield)                      │
│  ]                                                              │
│                                                                  │
│  ExtremeEvents → [                                              │
│    (GlobalTemperature Causes ExtremeEvents),                    │
│    (ExtremeEvents Includes Drought),                            │
│    (ExtremeEvents Includes Floods),                             │
│    (ExtremeEvents IncreasedPercent 40),                         │
│    (ExtremeEvents Causes ClimateMigration)                      │
│  ]                                                              │
│                                                                  │
│  FoodSecurity → [                                               │
│    (CropYield Affects FoodSecurity),                            │
│    (FoodSecurity CompromisedPeople 828000000),                  │
│    (FoodAccess PartOf FoodSecurity)                             │
│  ]                                                              │
│                                                                  │
│  SupplyChain → [                                                │
│    (PoliticalInstability Interrupts SupplyChain),               │
│    (SupplyChain Type Food),                                     │
│    (SupplyChain InterruptedRegions 8),                          │
│    (SupplyChain Affects FoodAccess)                             │
│  ]                                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Omnispace Risultante

```
┌─────────────────────────────────────────────────────────────────┐
│  OMNISPACE: Conoscenza compilata e organizzata                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Totale Atomi unici: 47                                         │
│  Totale Expression: 31                                          │
│  Totale Relazioni: 58                                           │
│                                                                  │
│  Strutture semantiche emergenti:                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Cluster 1: Impatto Climatico Diretto                    │   │
│  │  GlobalTemperature → ExtremeEvents → CropYield           │   │
│  │                                                          │   │
│  │  Cluster 2: Conseguenze Sociali                          │   │
│  │  CropYield → FoodSecurity → HumanImpact                  │   │
│  │                                                          │   │
│  │  Cluster 3: Migrazioni e Geopolitica                     │   │
│  │  ExtremeEvents → ClimateMigration → PoliticalInstability │   │
│  │                                                          │   │
│  │  Cluster 4: Supply Chain                                 │   │
│  │  PoliticalInstability → SupplyChain → FoodAccess         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  Pattern identificati:                                          │
│  - Feedback loop: FoodSecurity → Migration → Conflict →         │
│                   FoodSecurity (peggioramento)                   │
│  - Punti di leva: CropYield (intervento agronomico),            │
│                   PoliticalInstability (intervento politico)     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---
## FASE 2: Session Layer

### Query dell'Utente

```
┌─────────────────────────────────────────────────────────────────┐
│  UTENTE: "Qual è l'impatto del cambiamento climatico sulla      │
│          sicurezza alimentare?"                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Interpretazione Query (LLM integrato)

```
┌─────────────────────────────────────────────────────────────────┐
│  1. Interpreta la query                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Intent: trova percorsi causali tra due concetti                │
│  Keywords estratte: ["cambiamento climatico", "sicurezza        │
│                       alimentare", "impatto"]                    │
│  Vincoli impliciti: esplorazione causale, non solo correlazione │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  2. Individuazione nodi seed                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Semantic Index Lookup:                                         │
│  - "cambiamento climatico" → GlobalTemperature [match primario] │
│  - "sicurezza alimentare" → FoodSecurity [match primario]       │
│                                                                  │
│  Seed selezionati:                                              │
│  - Seed 1: GlobalTemperature (energia iniziale: 1.0)            │
│  - Seed 2: FoodSecurity (energia iniziale: 0.8)                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Cono di Luce

```
┌─────────────────────────────────────────────────────────────────┐
│  Focus attivo dell'utente definito dai seed                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                    ┌─────────────────┐                          │
│                    │  GlobalTemp     │ ← Seed 1 (energia 1.0)   │
│                    │  (fuoco centrale)                          │
│                    └────────┬────────┘                          │
│                             │                                   │
│              ┌──────────────┼──────────────┐                   │
│              │              │              │                    │
│              ▼              ▼              ▼                    │
│        ExtremeEvents   CropYield    (altri percorsi)           │
│                                                                  │
│                    ┌─────────────────┐                          │
│                    │  FoodSecurity   │ ← Seed 2 (energia 0.8)   │
│                    │  (fuoco secondario)                        │
│                    └────────┬────────┘                          │
│                             │                                   │
│              ┌──────────────┼──────────────┐                   │
│              │              │              │                    │
│              ▼              ▼              ▼                    │
│        HumanImpact   FoodAccess   (altri percorsi)             │
│                                                                  │
│  Il Cono di Luce definisce l'area di osservazione attiva:       │
│  tutti gli Atomi entro N hop dai seed sono nel focus            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Campo Gravitazionale (ricalcolato da Embedding)

```
┌─────────────────────────────────────────────────────────────────┐
│  Gravità degli Atomi nel nuovo campo (reset ogni sessione)      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Atomo                  Gravità   Determinata da                │
│  ─────────────────────────────────────────────────────────────  │
│  GlobalTemperature      1.00      seed primario                 │
│  FoodSecurity           0.80      seed secondario               │
│  CropYield              0.92      forte relazione con entrambi  │
│  ExtremeEvents          0.75      relazione diretta con seed 1  │
│  FoodAccess             0.71      parte di FoodSecurity         │
│  ClimateMigration       0.54      relazione indiretta (2 hop)   │
│  PoliticalInstability   0.43      relazione indiretta (3 hop)   │
│  SupplyChain            0.38      relazione indiretta (3 hop)   │
│  HumanImpact            0.29      relazione debole (4 hop)      │
│                                                                  │
│  Nota: gravità ricalcolata da Embedding originali, specifica    │
│        per questa sessione e contesto query                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Propagazione Energetica (Limite di Hop)

```
┌─────────────────────────────────────────────────────────────────┐
│  Paesaggio energetico con decadimento progressivo               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Hop 0 (seed):                                                  │
│  GlobalTemperature = 1.0, FoodSecurity = 0.8                    │
│                                                                  │
│  Hop 1 (×0.7 attenuazione):                                     │
│  ExtremeEvents = 0.70, CropYield = 0.70                         │
│  FoodAccess = 0.56, HumanImpact = 0.56                          │
│                                                                  │
│  Hop 2 (×0.49 attenuazione):                                    │
│  Drought = 0.49, Floods = 0.49                                  │
│  ClimateMigration = 0.49                                        │
│  CropYield (rinforzo) = 0.85 ← convergenza!                     │
│                                                                  │
│  Hop 3 (×0.343 attenuazione):                                   │
│  PoliticalInstability = 0.34                                    │
│  SupplyChain = 0.34                                             │
│  FoodAccess (rinforzo) = 0.68 ← convergenza!                    │
│                                                                  │
│  Hop 4 (×0.240 attenuazione):                                   │
│  Conflicts = 0.24                                               │
│  HumanImpact (rinforzo) = 0.52 ← convergenza!                   │
│                                                                  │
│  Hop 5 (×0.168 attenuazione):                                   │
│  FeedbackLoop = 0.17 (PoliticalInstability → Migration →        │
│                        PoliticalInstability)                     │
│                                                                  │
│  Threshold attivazione: 0.15                                    │
│  Atomi attivi (>0.15): 13 su 47 totali                          │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  CONVERGENZE IDENTIFICATE:                               │   │
│  │  - CropYield: riceve energia da GlobalTemperature        │   │
│  │    e influenza FoodSecurity (ponte tra seed)             │   │
│  │  - FoodAccess: riceve energia da FoodSecurity e          │   │
│  │    SupplyChain (convergenza multi-percorso)              │   │
│  │  - HumanImpact: converge da FoodSecurity e Conflict      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Connessioni Inattese Emergenti

```
┌─────────────────────────────────────────────────────────────────┐
│  Il paesaggio energetico fa emergere naturalmente connessioni   │
│  inizialmente periferiche che diventano rilevanti               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Percorso diretto (atteso):                                     │
│  GlobalTemperature → CropYield → FoodSecurity                   │
│                                                                  │
│  Percorsi trasversali (emergenti):                              │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  1. Migrazioni → Instabilità → Supply Chain             │   │
│  │     ExtremeEvents → ClimateMigration →                  │   │
│  │     PoliticalInstability → SupplyChain → FoodAccess     │   │
│  │     → FoodSecurity                                      │   │
│  │     Insight: impatto indiretto via geopolitica           │   │
│  │                                                          │   │
│  │  2. Feedback loop di peggioramento                      │   │
│  │     FoodSecurity↓ → Migration↑ → Conflict↑ →            │   │
│  │     FoodSecurity↓↓ (ulteriore diminuzione)              │   │
│  │     Insight: ciclo vizioso auto-rinforzante              │   │
│  │                                                          │   │
│  │  3. Punti di leva per intervento                        │   │
│  │     CropYield (intervento agronomico/adattamento)        │   │
│  │     PoliticalInstability (intervento politico/cooperazione)│ │
│  │     Insight: due leve distinte per stesso problema       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---
## FASE 3: Generation Layer

### Input per LLM

```
┌─────────────────────────────────────────────────────────────────┐
│  Porzione di conoscenza attivata + metriche di rilevanza        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Atomi attivati (13 su 47):                                     │
│  - GlobalTemperature (1.0), FoodSecurity (0.8)                  │
│  - CropYield (0.85), ExtremeEvents (0.70)                       │
│  - FoodAccess (0.68), HumanImpact (0.52)                        │
│  - ClimateMigration (0.49), PoliticalInstability (0.34)         │
│  - SupplyChain (0.34), Conflicts (0.24)                         │
│  - Drought (0.49), Floods (0.49), FeedbackLoop (0.17)           │
│                                                                  │
│  Percorsi rilevanti:                                            │
│  1. Diretto: GlobalTemperature → CropYield → FoodSecurity       │
│  2. Trasversale: ExtremeEvents → Migration → Conflict →         │
│                SupplyChain → FoodAccess → FoodSecurity          │
│  3. Feedback: FoodSecurity → Migration → Conflict →             │
│               FoodSecurity (peggioramento)                      │
│                                                                  │
│  Metriche:                                                      │
│  - Hop totali: 5                                                │
│  - Convergenze: 3 (CropYield, FoodAccess, HumanImpact)          │
│  - Punti di leva: 2 (CropYield, PoliticalInstability)           │
│                                                                  │
│  Riferimenti fonti:                                             │
│  - [IPCC Climate Report 2023]                                   │
│  - [FAO Agriculture 2023]                                       │
│  - [World Bank Migration 2022]                                  │
│  - [Nature Geopolitics 2023]                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Output Generato (Linguaggio Naturale)

```
┌─────────────────────────────────────────────────────────────────┐
│  RISPOSTA GENERATA                                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  L'impatto del cambiamento climatico sulla sicurezza            │
│  alimentare avviene attraverso tre meccanismi principali:       │
│                                                                  │
│  1. IMPATTO DIRETTO (produzione agricola):                      │
│     L'aumento delle temperature globali (1.1°C) causa eventi    │
│     estremi più frequenti (siccità, alluvioni, +40% in 20       │
│     anni), che riducono la resa delle colture principali        │
│     (grano, riso, mais) del 5-15% nelle regioni tropicali.      │
│     Questo compromette direttamente la sicurezza alimentare      │
│     per 828 milioni di persone [IPCC 2023, FAO 2023].           │
│                                                                  │
│  2. IMPATTO INDIRETTO (migrazioni e geopolitica): ⭐           │
│     Gli eventi estremi causano migrazioni climatiche (21        │
│     milioni di persone nel 2021), che generano instabilità      │
│     politica nelle regioni di transito e destinazione.          │
│     L'instabilità interrompe le supply chain alimentari in      │
│     8 regioni critiche, limitando l'accesso al cibo anche       │
│     dove la produzione è sufficiente [World Bank 2022,          │
│     Nature 2023].                                               │
│                                                                  │
│  3. CICLO DI PEGGIORAMENTO (feedback loop): ⭐⭐                │
│     La ridotta sicurezza alimentare spinge ulteriori            │
│     migrazioni, che aumentano i conflitti per le risorse        │
│     (12 conflitti dal 2020), che a loro volta peggiorano        │
│     la sicurezza alimentare. Questo ciclo auto-rinforzante      │
│     amplifica l'impatto iniziale del clima [Nature 2023].       │
│                                                                  │
│  PUNTI DI LEVA PER INTERVENTO:                                  │
│  - Agronomico: aumentare la resilienza delle colture            │
│    (intervento su CropYield)                                    │
│  - Politico: cooperazione internazionale per gestire            │
│    migrazioni e stabilizzare regioni critiche (intervento        │
│    su PoliticalInstability)                                     │
│                                                                  │
│  CONNESSIONI INATTESE:                                          │
│  Il percorso migratorio → instabilità → supply chain non         │
│  era ovvio dalla query iniziale, ma emerge come meccanismo       │
│  cruciale che collega clima a sicurezza alimentare attraverso    │
│  la geopolitica.                                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Tracciabilità alle Fonti

```
┌─────────────────────────────────────────────────────────────────┐
│  Ogni affermazione è collegata alle fonti originali             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  "1.1°C aumento" → [IPCC Climate Report 2023, pag. 12]          │
│  "40% eventi estremi" → [IPCC Climate Report 2023, pag. 24]     │
│  "5-15% resa colture" → [FAO Agriculture 2023, pag. 8]          │
│  "828 milioni persone" → [FAO Agriculture 2023, pag. 3]         │
│  "21 milioni migranti" → [World Bank Migration 2022, pag. 15]   │
│  "12 conflitti" → [Nature Geopolitics 2023, pag. 7]             │
│  "8 regioni critiche" → [Nature Geopolitics 2023, pag. 11]      │
│                                                                  │
│  Click su [fonte] → visualizza estratto originale del documento │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```


