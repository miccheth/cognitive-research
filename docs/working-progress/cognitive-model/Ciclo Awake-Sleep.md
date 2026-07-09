___
# Descrizione:

Il sistema opera in due fasi cicliche complementari:

- **Fase di Veglia (Awake):** Accumula dati dall'ambiente esterno
- **Fase di Sonno (Sleep):** Si isola dagli input esterni e compie ottimizzazioni interne

Durante la fase di sonno avviene un **pruning massiccio**: ciò che è forte e sensato sopravvive, il resto viene eliminato. Il ciclo migliora iterativamente le prestazioni del ciclo successivo.

___
# Meccanismo: Synaptic Tagging e Potatura Selettiva

Il modello implementa una fase di scaricamento e ottimizzazione basata sul _Synaptic Tagging and Capture_ e sulla teoria del riequilibrio sinaptico:

## Fase di Veglia (Tagging & LTP)

Durante l'interazione con l'ambiente, l'attenzione evoca un Potenziamento a Lungo Termine (LTP) locale. Questo processo applica un **"Tag" (marcatore bio-computazionale)** sui collegamenti ritenuti salienti o associati a un successo.

## Fase di Sonno (Potatura e Consolidamento)

- **Riproduzione Off-line:** Il sottosistema di memoria a breve termine riproduce ciclicamente i pattern salienti appresi, proiettandoli sulla rete principale per consolidarli nelle "fortezze strutturali".

- **Potatura Selettiva (Pruning Omeostatico):** Il sistema abbassa uniformemente l'energia o il peso di tutte le connessioni. I collegamenti deboli e _privi di Tag_ (rumore di fondo) scendono sotto soglia critica e vengono **eliminati**. I circuiti marcati dal "Tag" resistono, emergendo dal rumore e stabilizzandosi.

___