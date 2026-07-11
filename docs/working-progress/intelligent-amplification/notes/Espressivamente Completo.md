
___
# 1. Il problema delle Triplette Limitate

Una frase non è solo `Soggetto-Azione-Oggetto`. Le rappresentazioni piatte a triplette limitano la precisione e la capacità espressiva.

**Soluzione:** Abbandonare le triplette piatte a favore di strutture **ricorsive, nidificate e multi-dimensionali**. Un ipergrafo o struttura equivalente permette di:
- Avere relazioni con infiniti argomenti
- Nidificare espressioni dentro altre espressioni
- Aggiungere assi (Tempo, Spazio, Contesto, Vincoli) per aumentare la precisione

Più assi si aggiungono, più la rappresentazione diventa precisa e aderente alla complessità del concetto reale.

**Completezza Espressiva:** Il sistema deve poter definire espressioni logiche di complessità infinita che integrano:
- Logica probabilistica
- Dimensioni temporali e spaziali
- Vincoli e regole
- Codice eseguibile

___
# 2. Il problema delle Variabili Rigide vs Caos dell'LLM

Se il sistema simbolico non ha variabili rigide, l'inferenza fallisce. Serve un equilibrio tra:
- **Rigidità:** per garantire correttezza logica e inferenze valide
- **Flessibilità:** per permettere l'integrazione con componenti probabilistiche (LLM)

**Soluzione:** Implementare un **sistema di tipi rigoroso (Strict Typing)** con le seguenti proprietà:

1. **Homoiconicità:** Codice e dati hanno la stessa struttura, permettendo metaprogrammazione e riflessione
2. **Pattern Matching:** Validazione strutturale delle espressioni in ingresso
3. **Type Checking:** Verifica dei tipi a livello di compilazione/inserimento
4. **Integrità:** Se una componente probabilistica (LLM) inventa una variabile o tipo non registrato, il sistema la rifiuta

___
# 3. Gestione del Vocabolario (Tokenizer)

Il vocabolario delle variabili e dei valori deve essere **blindato, rigido e pre-esistente**, ma allo stesso tempo **estensibile** per mantenere la completezza espressiva.

## Domande aperte:

**1. Tokenizer unico o custom per dataset?**
- **Unico:** Mantiene una lingua comune, garantisce interoperabilità tra diversi dataset e utenti
- **Custom per dataset:** Permette specializzazione, ma rischia di perdere la traducibilità tra sistemi

**2. Come gestire l'estensione del vocabolario?**
Quando un utente crea un nuovo dataset simbolico:
- Deve usare solo simboli esistenti? (limita ma garantisce compatibilità)
- Può introdurre nuovi simboli? (come si traduce poi nella lingua comune?)

**3. Traduzione Neuro-Simbolica:**
Come mappare le rappresentazioni neurali (continue, sfumate) su simboli discreti (rigidi, tipizzati) senza perdere informazione?

___
# Principio di Completezza Espressiva

Un sistema è **espressivamente completo** quando:
1. Può rappresentare qualsiasi concetto complessa senza semplificazioni riduttive
2. Mantiene integrità logica durante l'inferenza
3. Permette estensibilità senza rompere la compatibilità
4. Supporta l'interoperabilità tra componenti simboliche e subsimboliche

___




