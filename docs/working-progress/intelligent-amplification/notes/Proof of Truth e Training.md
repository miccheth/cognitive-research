
___
# Addestramento e Dati

L'addestramento è **inevitabile**. Non è possibile ottenere precisione e resistenza al rumore con pochi dati.

**Principio:** La potenza del sistema deriva dalla quantità e qualità dei dati su cui è stato addestrato. Non esistono scorciatoie.

___
# Conversione Conoscenza → Simboli

Il sistema deve avere la capacità di **convertire conoscenza in simboli**, con una componente neurale/probabilistica che decide:
- **Quando usare** una rappresentazione simbolica
- **Come interpretare** il risultato

**Problema aperto:** Definire una **lingua comune** per la traduzione tra componente neurale e simbolica.

___
# Estrazione della Verità da Grandi Dataset

Quando il sistema ha accesso a un dataset grande (molteplici fonti/opinioni), deve:

**Collassare le opinioni multiple** per trovare una via di mezzo → la **verità emergente**.

**Meccanismo:**
- Creare un **baricentro di massa** dalle opinioni convergenti
- La verità è il punto di equilibrio statistico
- Dopo la verità viene raffinata dalla conoscenza già presente nel sistema
- **Estrarre la catena di nodi** che giustifica quell'inferenza

___
# Apprendimento Incrementale ed Evoluzione delle Verità

Il sistema deve gestire l'**evoluzione temporale della conoscenza**:

**Problemi:**
1. Come impara cose nuove senza rompere le conoscenze esistenti?
2. Quando scartare concetti vecchi (obsoleti, errati, non utili)?
3. Come fare **pruning selettivo** senza perdere informazione valida?

**Soluzione: Ciclo di Ricorsione Simbolica**
- Il sistema opera in cicli iterativi
- Ogni ciclo rende il simbolico **più potente e preciso**
- **Pruning delle inferenze sbagliate** (stile Reinforcement Learning)
- **Consolidamento delle inferenze verificate**

**Apprendimento Incrementale:**
- Le verità non sono statiche, si evolvono
- Il sistema deve tracciare la **provenienza** e la **data di validazione** di ogni conoscenza
- Concetti vecchi possono essere:
  - **Mantenuti** (se ancora validi)
  - **Aggiornati** (se parzialmente corretti)
  - **Scartati** (se errati o obsoleti)

___
# Principi di Verità e Apprendimento

1. **Verità come Baricentro:** La verità emerge dalla convergenza statistica di fonti multiple
2. **Traceability:** Ogni inferenza deve mostrare la catena di ragionamento che la giustifica
3. **Incrementalità:** L'apprendimento non distrugge la conoscenza esistente, la evolve
4. **Pruning Selettivo:** Eliminare solo ciò che è verificato come errato o inutile
5. **Ricorsione Migliorativa:** Cicli iterativi che rafforzano il simbolico nel tempo

___
