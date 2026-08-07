# Opzioni di Unificazione: Spazio Geometrico e Componente Simbolica

Tre modelli possibili per integrare la componente subsimbolica (capire) e simbolica (verificare).

---

## Opzione 1: Spazio Unico, Due Regimi di Lettura

Il Spazio Geometrico è **uno solo**, ma il sistema lo interroga in due modi diversi:

```
Spazio Geometrico (unico)
    ↓
    ├── Lettura Subsimbolica: legge pattern distribuiti, attrattori, tendenze (lossy)
    └── Lettura Simbolica: legge simboli discreti, regole, logiche (lossless)
```

**Analogia:** Come guardare un quadro. Da lontano vedi sfumature e atmosfere (subsimbolico). Da vicino vedi pennellate precise e contorni (simbolico). È lo stesso quadro, due modalità di lettura.

**Vantaggi:**
- Elegante, economico, nessun "ponte" da costruire
- Unificazione naturale delle due componenti

**Problemi:**
- Come fai a garantire rigidità se la base è sempre lossy?
- Come passi da tendenze probabilistiche a simboli discreti senza perdita?

---

## Opzione 2: Due Spazi Accoppiati

Ci sono **due spazi distinti** che comunicano tramite un'interfaccia:

```
Spazio Geometrico (GPU, subsimbolico) ←→ Interfaccia (PLN) ←→ Spazio Logico (CPU, simbolico)
         ↓                                         ↓
    Attrattori, energie                       Simboli, regole
    Generalizzazione                          Verifica formale
```

**Analogia:** Come avere una lavagna per schizzi (subsimbolico) e un foglio di calcolo (simbolico). Usi la prima per brainstorming, il secondo per verifiche.

**Vantaggi:**
- Chiaro, ogni spazio ha le sue regole
- Separazione netta dei compiti
- Il simbolico garantisce anti-allucinazione

**Problemi:**
- Devi definire l'interfaccia di traduzione (PLN?)
- Overhead computazionale nel passaggio tra spazi
- Rischio di perdita di informazione nella traduzione

---

## Opzione 3: Livelli di una Piramide (Emergenza)

Il simbolico **emerge** dal subsimbolico quando certi attrattori diventano stabili:

```
Subsimbolico (base)
    ↓ (stabilizzazione tramite apprendimento/verifica)
Simbolico (livello superiore)
```

**Analogia:** Come l'acqua che diventa ghiaccio. Le molecole sono le stesse, ma sopra una certa soglia di stabilità emergono proprietà rigide.

**Meccanismo:**
- Un pattern subsimbolico viene ripetutamente confermato
- L'attrattore si stabilizza (bassa energia, alta confidenza)
- Il sistema "cristallizza" il pattern in un simbolo discreto
- Il simbolo diventa disponibile per ragionamento logico

**Vantaggi:**
- Naturale, spiegazione unitaria
- Il simbolico è "grounded" nel subsimbolico
- Spiega come si formano gli acceleratori cognitivi

**Problemi:**
- Come definisci la "soglia" di stabilizzazione?
- Cosa succede se un simbolo cristallizzato si rivela errato?
- Difficile da implementare formalmente

---

## Tracce nei Note Esistenti

- **Working Memory "ibrida"** → Opzione 1
- **PLN come "traduttore"** → Opzione 2
- **Acceleratori Cognitivi che diventano automatici** → Opzione 3
- **"Una volta estratto e capito, si trasforma in parte deterministica"** → Opzione 3

---

## Domande Aperte

1. Il passaggio subsimbolico → simbolico è **sequenziale** (prima uno, poi l'altro) o **parallelo** (entrambi attivi simultaneamente)?

2. Il simbolico può **influenzare** il subsimbolico (top-down) o è solo un consumatore passivo?

3. Esiste un **feedback loop**? (es.: il simbolico verifica → il subsimbolico si riadatta)

4. Gli **Acceleratori Cognitivi** sono simbolico cristallizzato o subsimbolico ottimizzato?
