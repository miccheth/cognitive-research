
___
# Come funziona l'Attenzione Simbolica?

Il modello sfrutta **L'ECAN (Economic Attention Network)**: ogni concetto (Nodo) e ogni relazione (Collegamento) nell'ipergrafo ha due numeri attaccati, detti **Valori di Attenzione**:

1. **STI (Short-Term Importance):** L'importanza a breve termine. È la quantità di "energia elettrica" o stimolo che il nodo ha in questo preciso momento.
    
2. **LTI (Long-Term Importance):** L'importanza a lungo termine. Indica se quel concetto è utile spesso (viene salvato in VRAM) o se non serve quasi mai (viene archiviato su disco rigido).

Immagina che l'utente stia parlando di _"motori aeronautici"_.

- La CPU attiva il nodo `Motore_Aereo` dandogli il massimo dell'energia (STI = 100).
    
- Questa energia si "propaga" (Spreading Activation) come una scossa elettrica lungo i legami dell'ipergrafo. I nodi vicini come `Turbina`, `Cherosene` e `Spinta` si accendono di riflesso (STI = 70). Nodi lontani come `Gazzella` o `Filosofia` rimangono al buio (STI = 0).
	
- Esempio con LTI?

- Quando la GPU deve fare un'inferenza o una moltiplicazione matematica, **non scansiona tutto il Terabyte di conoscenza**. Guarda solo i nodi che hanno l'attenzione accesa (STI > 0). L'attenzione simbolica funge da **filtro hardware**: dice alla GPU su quali coordinate del tensore focalizzare i suoi fari-laser matematici, tagliando fuori il 99% dei dati irrilevanti e rendendo il calcolo istantaneo.
- Però è da capire, perchè magari ci sono informazioni lontane, che sono utili.

___