

---
## Panoramica

**Scenario:** Un utente vuole esplorare le connessioni tra caffeina e prestazioni atletiche. Il sistema rivela non solo il percorso noto (via dopamina), ma anche un percorso meno ovvio (via vasocostrizione/ossigenazione muscolare).

---
## FASE 0: Stato Iniziale del Metagrafo

### Conoscenza Importata dai 3 Paper

```
┌─────────────────────────────────────────────────────────────────┐
│  CARTA DELLA CONOSCENZA (pre-compilazione GPU)                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Paper Neuroscienze 2019]                                      │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  ID:2891  [Caffeine] ──blocca──> ID:4521  [Adenosine] │    │
│  │  ID:4521  [Adenosine] ──attiva──> ID:6733  [A2A_Receptor]│   │
│  │  ID:6733  [A2A_Receptor] ──regola──> ID:8844  [Dopamine]│   │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  [Paper Fisiologia 2021]                                        │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  ID:2891  [Caffeine] ──causa──> ID:5102  [Vasoconstriction]│  │
│  │  ID:5102  [Vasoconstriction] ──aumenta──> ID:7234  [Muscle_O2]││
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  [Paper Sport 2020]                                             │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  ID:7234  [Muscle_O2] ──migliora──> ID:3341  [Athletic_Perf]││
│  │  ID:8844  [Dopamine] ──aumenta──> ID:3341  [Athletic_Perf] ││
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Grounding applicato (tutto in inglese, ID univoci):            │
│  - "caffeina", "Caffeine", "caffè" → ID:2891 [Caffeine]        │
│  - "prestazioni atletiche", "athletic performance" → ID:3341   │
│  - "ossigenazione muscolare", "muscle oxygenation" → ID:7234   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Grafo Compilato in VRAM

```
┌─────────────────────────────────────────────────────────────────┐
│  GPU VRAM - Atom Buffer (dopo compilazione)                     │
│  Ogni Atomo contiene: dati + relazioni annidate                 │
├──────────┬───────────────┬──────────────┬──────────────────────┐
│  AtomID  │   Label       │  Energy      │  Structure (annidato)│
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  2891    │  Caffeine     │  0.0         │  [blocca→4521]       │
│          │               │              │  [causa→5102]        │
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  4521    │  Adenosine    │  0.0         │  [attiva→6733]       │
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  6733    │  A2A_Receptor │  0.0         │  [regola→8844]       │
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  8844    │  Dopamine     │  0.0         │  [aumenta→3341]      │
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  5102    │  Vasoconstr.  │  0.0         │  [aumenta→7234]      │
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  7234    │  Muscle_O2    │  0.0         │  [migliora→3341]     │
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  3341    │  Athletic_P.  │  0.0         │  [] (sink)           │
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  ...     │  ...          │  ...         │  ...                 │
│  (9.993 atomi non mostrati)                                     │
└──────────┴───────────────┴──────────────┴──────────────────────┘

Nota: Le relazioni SONO atomi annidati nella structure di ogni atomo.
      Non esiste un Relation Buffer separato (coerente con Omnispace: tutto è Atomo).
```

---
## FASE 1: Query Processing (CPU)

```
┌─────────────────────────────────────────────────────────────────┐
│  UTENTE digita: "caffeina → prestazioni atletiche"              │
└─────────────────────────────────────────────────────────────────┘
                              ↓ (50 ms)
┌─────────────────────────────────────────────────────────────────┐
│  LLM/SLM (CPU) - Interpretazione                                │
│  - Intent: trova percorsi tra due concetti                      │
│  - Keywords estratte: ["caffeine", "athletic_performance"]      │
│  - Vincoli: hop_max=3, threshold=0.2                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓ (5 ms)
┌─────────────────────────────────────────────────────────────────┐
│  Semantic Index Lookup (CPU RAM - Hash Table)                   │
│                                                                  │
│  Cerca "caffeine":                                              │
│    → Trovato! ID: [2891]                                        │
│                                                                  │
│  Cerca "athletic_performance":                                  │
│    → Trovato! ID: [3341]                                        │
│                                                                  │
│  Seed IDs: [2891, 3341]                                         │
│  Energia iniziale: 2891=1.0, 3341=1.0                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓ (1 ms - invio a GPU)
```

### Semantic Index (CPU RAM)

```
┌─────────────────────────────────────────────────────────────────┐
│  "caffeine"          → [2891]                                   │
│  "adenosine"         → [4521]                                   │
│  "a2a_receptor"      → [6733]                                   │
│  "dopamine"          → [8844]                                   │
│  "vasoconstriction"  → [5102]                                   │
│  "muscle_o2"         → [7234]                                   │
│  "athletic_perf"     → [3341]                                   │
│                                                                  │
│  Lookup time: O(1) per termine                                  │
│  Grounding: tutte le varianti linguistiche mappate allo stesso ID│
└─────────────────────────────────────────────────────────────────┘
```

---
## FASE 2: Energy Propagation (GPU Compute Shader)

### Stato Iniziale (t=0)

```
┌──────────┬───────────────┬──────────────┬──────────────────────┐
│  AtomID  │   Label       │  Energy      │  Structure           │
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  2891    │  Caffeine     │  1.0         │  [→4521, →5102]      │ ← SEED
│  4521    │  Adenosine    │  0.0         │  [→6733]             │
│  6733    │  A2A_Receptor │  0.0         │  [→8844]             │
│  8844    │  Dopamine     │  0.0         │  [→3341]             │
│  5102    │  Vasoconstr.  │  0.0         │  [→7234]             │
│  7234    │  Muscle_O2    │  0.0         │  [→3341]             │
│  3341    │  Athletic_P.  │  1.0         │  []                  │ ← SEED
└──────────┴───────────────┴──────────────┴──────────────────────┘
```

### Propagazione per Hop

| Hop | Attenuazione | Nodi Attivati | Note |
|-----|--------------|---------------|------|
| 1 | ×0.7 | Adenosine (0.7), Vasoconstr. (0.7) | Dai seed |
| 2 | ×0.49 | A2A_Receptor (0.34), Muscle_O2 (0.34) | Dai vicini |
| 3 | ×0.343 | Dopamine (0.24), **Athletic_P. (1.68)** | Convergenza! |

### Risultato Finale (HOP 3)

```
┌──────────┬───────────────┬──────────────┬──────────────────────┐
│  AtomID  │   Label       │  Energy      │  Note                │
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  2891    │  Caffeine     │  1.000       │  seed                │
│  4521    │  Adenosine    │  0.700       │  percorso 1          │
│  5102    │  Vasoconstr.  │  0.700       │  percorso 2          │
│  6733    │  A2A_Receptor │  0.343       │  percorso 1          │
│  8844    │  Dopamine     │  0.240       │  da 6733             │
│  7234    │  Muscle_O2    │  0.343       │  percorso 2          │
│  3341    │  Athletic_P.  │  1.680       │  ← BARICENTRO!       │
│           │               │              │  (0.343+0.343+1.0)   │
└──────────┴───────────────┴──────────────┴──────────────────────┘

Nota: Athletic_Performance riceve energia da DUE percorsi indipendenti.
      Questo lo rende un BARICENTRO di energia - punto di convergenza.
```

---
## FASE 3: Read-back Selettivo (GPU → CPU)

```
┌─────────────────────────────────────────────────────────────────┐
│  GPU filtra: energy > threshold (0.2)                           │
│  Trovati: 7 atomi (su 10.000 totali)                            │
├──────────┬───────────────┬──────────────┬──────────────────────┐
│  AtomID  │   Label       │  Energy      │  Structure           │
├──────────┼───────────────┼──────────────┼──────────────────────┤
│  2891    │  Caffeine     │  1.000       │  [→4521, →5102]      │
│  4521    │  Adenosine    │  0.700       │  [→6733]             │
│  5102    │  Vasoconstr.  │  0.700       │  [→7234]             │
│  6733    │  A2A_Receptor │  0.343       │  [→8844]             │
│  8844    │  Dopamine     │  0.240       │  [→3341]             │
│  7234    │  Muscle_O2    │  0.343       │  [→3341]             │
│  3341    │  Athletic_P.  │  1.680       │  []                  │
└──────────┴───────────────┴──────────────┴──────────────────────┘

Dimensione: ~2 KB (invece di 10.000 atomi = ~400 KB)
Tempo trasferimento PCIe: ~0.1 ms
```

### Threshold Filtering

- **Totale atomi nel grafo:** 10.000
- **Atomi con energy > 0.2:** 7
- **Rapporto di compressione:** 1.428 : 1

**Vantaggi:**
- Trasferimento PCIe minimo (~2 KB vs ~400 KB)
- CPU elabora solo dati rilevanti
- UI renderizza solo ciò che conta

**Threshold dinamico:**
- Query esplorative → threshold basso (0.1) → più risultati
- Query focalizzate → threshold alto (0.5) → meno risultati

---
## FASE 4: Analisi Percorsi (CPU)

### Percorsi Identificati

```
┌─────────────────────────────────────────────────────────────────┐
│  PATHFINDER - Ricostruzione percorsi dagli atomi attivati       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Percorso 1 (via Neuroscienze):                                 │
│  Caffeine ──blocca──> Adenosine ──attiva──> A2A_Receptor       │
│           (1.0)        (0.7)          (0.343)                   │
│              ──regola──> Dopamine ──aumenta──> Athletic_Perf    │
│                        (0.240)         (1.680)                  │
│                                                                  │
│  Percorso 2 (via Fisiologia + Sport): ⭐ SCOPERTA               │
│  Caffeine ──causa──> Vasoconstriction ──aumenta──> Muscle_O2   │
│           (1.0)         (0.7)            (0.343)                │
│              ──migliora──> Athletic_Perf                        │
│                            (1.680)                              │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  🎯 SCOPERTA INASPETTATA:                                │   │
│  │  "Vasoconstriction → Muscle_O2"                          │   │
│  │  Perché interessante:                                    │   │
│  │  • Non era un percorso ovvio dalla query                 │   │
│  │  • Collega due domini: fisiologia → sport                │   │
│  │  • Energia significativa: 0.70 → 0.34                    │   │
│  │  • Paper fonte: [Paper Fisiologia 2021]                  │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Cosa Hai Scoperto

```
┌─────────────────────────────────────────────────────────────────┐
│  PRIMA della query:                                             │
│  "So che la caffeina è uno stimolante e migliora le prestazioni"│
│                                                                  │
│  DOPO la query:                                                 │
│  "La caffeina migliora le prestazioni attraverso DUE meccanismi:│
│   1. Via neurologica: blocca adenosina → aumenta dopamina       │
│   2. Via fisiologica: vasocostrizione → più ossigeno ai muscoli│
│                                                                  │
│  Quest'ultimo non lo sapevo! Ora posso:                         │
│  • Leggere il [Paper Fisiologia 2021] per approfondire          │
│  • Cercare se ci sono altri percorsi correlati                  │
│  • Usare questa informazione per il mio studio/ricerca          │
│  • Esplorare "Muscle_O2" per scoprire altre connessioni         │
└─────────────────────────────────────────────────────────────────┘
```

---
## FASE 5: Visualizzazione (UI)

### Graph View

```
┌─────────────────────────────────────────────────────────────────┐
│  ELEVIA - Graph View                                            │
│  Query: "caffeina → prestazioni atletiche"                      │
│  Tempo: 127 ms | Nodi attivati: 7 | Hop: 3                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                         ● Caffeine (1.0)                        │
│                        ╱ ╲                                      │
│              (blocca) ╱   ╲ (causa)                             │
│                      ╱     ╲                                    │
│                    ╱         ╲                                  │
│                  ╱             ╲                                │
│        ● Adenosine           ● Vasoconstriction                 │
│         (0.7)    ╲              (0.7)    ╲                       │
│                    ╲ (attiva)              ╲ (aumenta)          │
│                      ╲                      ╲                   │
│                        ╲                    ╲                   │
│              ● A2A_Receptor                ● Muscle_O2          │
│               (0.34)                        (0.34)              │
│                  ╲                          ╱                   │
│            (regola) ╲                    ╱ (migliora)          │
│                      ╲                  ╱                       │
│                        ╲                ╱                        │
│                          ● Dopamine                             │
│                           (0.24)                                │
│                              ╲                                  │
│                        (aumenta) ╲                              │
│                                ╲                                │
│                                  ● Athletic_Performance (1.68)  │
│                                          ↑                      │
│                                   BARICENTRO!                   │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  Legenda:                                                       │
│  ● Grande + Rosso scuro (≥0.8): seed/baricentro                 │
│  ● Medio + Arancione (0.4-0.8): percorso principale             │
│  ● Piccolo + Giallo (0.2-0.4): percorso secondario              │
│                                                                  │
│  💡 Insight: "La caffeina migliora le prestazioni non solo      │
│   tramite dopamina, ma anche aumentando l'ossigenazione         │
│   muscolare via vasocostrizione."                               │
│   Fonte: [Paper Fisiologia 2021], [Paper Sport 2020]            │
└─────────────────────────────────────────────────────────────────┘
```

### Modalità UI Potenziali

| Modalità | Descrizione | Caso d'uso |
|----------|-------------|------------|
| **Graph View** | Nodi e archi in 2D/3D, dimensione=energia | Esplorazione visiva |
| **Energy Heatmap** | Vista tabellare, colore=intensità | Molti nodi (>50) |
| **Focus Mode** | Solo nodi > soglia alta (0.6) | Query specifiche |
| **Discovery Mode** | Evidenzia solo scoperte inaspettate | Esplorazione serendipitosa |
| **List View** | Elenco testuale ordinato per energia | Esportazione CSV/JSON |

---
## Considerazioni Finali

### Cosa Questo Sistema Fa

✓ **Rivela connessioni nascoste** in conoscenza che già possiedi  
✓ **Collega domini separati** (es. neuroscienze + fisiologia sportiva)  
✓ **Mostra percorsi inaspettati** che non avresti cercato esplicitamente  
✓ **Esegue in tempo reale** (~126 ms per query completa)  
✓ **Scalabile** a milioni di atomi (GPU parallelism)  

### Cosa Questo Sistema NON Fa

✗ **Non crea conoscenza nuova** (non è magia!)  
✗ **Non sostituisce il pensiero umano** (amplifica, non sostituisce)  
✗ **Non funziona senza conoscenza importata** (devi importare paper/articoli)  
✗ **Non è un motore di ricerca tradizionale** (non cerca parole, cerca percorsi)  

### Requisiti per Funzionare Bene

1. **Grounding di qualità:** concetti normalizzati e ID univoci
2. **Relazioni estratte correttamente:** ingestion layer accurato
3. **Indice semantico completo:** tutte le varianti linguistiche mappate
4. **GPU con sufficiente VRAM:** almeno 4 GB per 100K atomi

---