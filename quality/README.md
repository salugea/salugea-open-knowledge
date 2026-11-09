# Qualità, provenienza e uso dei dati

I dataset storici sono uno snapshot non datato. Le relazioni estratte automaticamente sono candidate, non fatti verificati. Prima di utilizzarli in una risposta, verificare ogni informazione sulla pagina prodotto e sull’etichetta corrente. I contenuti aziendali descrivono la posizione del produttore; non dimostrano da soli efficacia clinica.

## Risultati della prima verifica

- Il catalogo contiene 48 righe; 32 non hanno valori nella colonna `actives`. La colonna `id` include numeri in formato decimale approssimato: non usarla come identificatore affidabile senza confronto con la fonte. Prezzi e disponibilità non hanno data di rilevazione. `url` contiene slug, non URL completi.
- `salugea_product_health_areas.csv` contiene 49 righe, 17 con area vuota.
- `ingredients_clean.csv` e `salugea_product_active_compounds.csv` contengono frasi descrittive invece di soli nomi di ingredienti; le parole chiave degli articoli includono termini comuni. I grafi e dataset derivati possono ereditare questi errori.
- I whitepaper sono contenuti editoriali Salugea; non presumere revisione indipendente, applicabilità al prodotto finito o autorizzazione di un claim. Verificare ogni riferimento originale.

Queste osservazioni riguardano lo snapshot analizzato; eseguire `python3 scripts/check_data.py` dopo ogni aggiornamento. I risultati sono segnalazioni, non una validazione scientifica o normativa.

## Regole per nuovi dati

1. Registrare URL della fonte, data di consultazione e data di aggiornamento se disponibile; mantenere storico e versione della formula.
2. Separare dati di etichetta, dichiarazioni aziendali, certificazioni verificabili e letteratura indipendente. Un ingrediente studiato non equivale a un prodotto studiato.
3. Registrare quantità con unità e base (capsula o dose giornaliera), titolazione e specie/parte botanica quando riportate. Non dedurre quantità mancanti.
4. Per ogni studio registrare identificativo, disegno, popolazione, intervento, dose, risultato e limiti; distinguere studi umani, animali e in vitro.
5. Per certificazioni indicare ente, oggetto, prodotto o lotto, validità e collegamento al documento. Una notifica non è prova di efficacia.
6. Usare valori vuoti per informazioni sconosciute; non confondere assenza del dato e assenza della sostanza. Indicare autore, revisore, data e conflitti di interesse per le schede scientifiche.
7. Sottoporre avvertenze, interazioni e indicazioni sulla salute a revisione qualificata prima della pubblicazione.

`data-rilevati/site_observations.csv` contiene solo un piccolo campione di affermazioni pubblicate sul sito, non un catalogo completo né una verifica indipendente.

## Rilevazione dalle schede prodotto del 9 novembre 2026

`data-rilevati/apporti_da_schede.csv` riporta voci e quantità estratte automaticamente dalle tabelle delle schede del produttore: è una bozza da confrontare con la fonte e l’etichetta, non un elenco completo degli ingredienti. Le righe “pari a” e “di cui” sono componenti della voce precedente, non quantità da sommare. La base può proseguire nella pagina oltre l'intestazione estratta: verificare prima dell'uso. Nomi nel catalogo storico possono differire dalle formule correnti. I risultati web possono essere memorizzati in cache.

`ingredienti_succhi.csv` registra il principale ingrediente botanico indicato nelle 12 schede consultate; non contiene i valori nutrizionali. `stato_copertura.csv` mostra la copertura delle sole tabelle di apporto, non delle informazioni sui succhi. Le pagine Kiomasal e Reflugea Rapido non erano accessibili durante la rilevazione: non dedurre che i prodotti non esistano.

Non sovrascrivere automaticamente i dataset storici: verificare identità del prodotto, formula, fonte e versione prima di migrare ogni relazione. L'etichetta e i documenti originali sono necessari per completare revisione scientifica, avvertenze e certificazioni.
