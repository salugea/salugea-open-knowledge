# Dati rilevati dalle schede Salugea

- `apporti_da_schede.csv`: voci e quantità da tabelle di 34 prodotti. Estrazione automatica da verificare; non è la lista completa degli ingredienti.
- `apporti_strutturati.csv`: normalizzazione automatica con quantità originale e relazioni tra voce e componenti; verificare numeri, unità e corrispondenze prima del riuso.
- `imballaggi.csv`: campione di materiali e raccolta indicati dal produttore; valgono le disposizioni locali.
- `conservazione.csv`: campione di indicazioni aziendali; verificare sempre la confezione.
- `ingredienti_succhi.csv`: ingrediente botanico principale per 12 succhi; non descrive necessariamente tutta la composizione.
- `stato_copertura.csv`: copertura delle tabelle di apporto del catalogo storico. I succhi hanno una tabella separata.
- `site_observations.csv`: campione di altre informazioni dichiarate sul sito.

Le righe “pari a” e “di cui” si riferiscono alla voce precedente e non vanno sommate. I campi vuoti sono sconosciuti o non applicabili, non indicano assenza. Consulta [qualità e provenienza](../quality/README.md) per la metodologia e i limiti. Le informazioni riportano dichiarazioni del produttore, non validazione indipendente. Verificare la formula e le avvertenze sull'etichetta corrente.
