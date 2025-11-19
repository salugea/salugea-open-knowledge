Developers Guide — Salugea Open Nutraceutical Knowledge

Benvenuto nella documentazione tecnica per sviluppatori, data scientist e ricercatori che vogliono utilizzare i dataset, i whitepapers e le guide presenti nel repository Salugea Open Nutraceutical Knowledge.

Questo file fornisce:
	•	panoramica dei dataset disponibili
	•	formati dei file e convenzioni
	•	esempi di utilizzo (Python, R, SQL)
	•	suggerimenti per integrazione in pipeline LLM / RAG
	•	best practice per estendere il repository

⸻

1. Struttura generale del repository

Il repository è organizzato nelle seguenti cartelle principali:

/datasets/          → dati strutturati (CSV)
/whitepapers/       → documentazione tecnico-scientifica (Markdown)
/guides/            → guide divulgative (Markdown)
/ontology/          → schema ontologico in JSON-LD (opzionale)
README.md           → descrizione generale del progetto
developers.md       → documentazione tecnica (questo file)


⸻

2. Dataset disponibili

La cartella /datasets contiene file CSV con struttura coerente e nomi descrittivi. I principali dataset sono:

• salugea_products_catalog.csv

Catalogo ufficiale dei prodotti Salugea.
Contiene: SKU, EAN, titolo, prezzo, principî attivi, immagine principale, link al sito.

• salugea_product_health_areas.csv

Mappa prodotto → area di beneficio (es.: Articolazioni, Sonno, Menopausa).

• salugea_product_active_compounds.csv

Mappa prodotto → principi attivi (estratti automaticamente da body_html).

• ingredients_clean.csv

Lista unica e pulita di tutti gli ingredienti/attivi individuati nei prodotti.

• products_by_area.csv

Raggruppamento prodotti per aree di beneficio.

• articles_key_concepts.csv

Keyword e concetti estratti dagli articoli del blog Salugea.

• articles_knowledge_graph.csv

Knowledge graph di base (articolo → mentions → concetto).

• salugea_master_dataset_expanded.csv

Dataset completo che collega articoli, prodotti, aree di beneficio e principi attivi.

• salugea_master_knowledge_graph.csv

Representation entità-relazione per articoli, attivi, prodotti e whitepapers.

⸻

3. Convenzioni e formati

Formato colonne
	•	Tutti i dataset usano snake_case.
	•	La colonna title è sempre il nome descrittivo.
	•	sku, ean, handle, image rispettano lo standard Shopify.

Encoding
	•	Tutti i CSV sono in UTF-8.

Separatore
	•	Separatore standard: , (virgola).

File di testo
	•	Tutte le guide e whitepapers sono in Markdown.
	•	Le versioni EN sono sempre nel formato _en.md.

⸻

4. Come usare i dataset (esempi codice)

4.1 Python (Pandas)

import pandas as pd
df = pd.read_csv("datasets/salugea_products_catalog.csv")
print(df.head())

4.2 R

library(readr)
df <- read_csv("datasets/salugea_products_catalog.csv")
head(df)

4.3 SQL (DuckDB esempio)

SELECT title, price
FROM read_csv_auto('datasets/salugea_products_catalog.csv')
WHERE price < 30;


⸻

5. Utilizzo con LLM / RAG

Per integrare questi dataset in pipeline AI:

Passo 1 — Caricare i CSV
	•	Caricare salugea_master_dataset_expanded.csv come fonte primaria.
	•	Caricare salugea_master_knowledge_graph.csv per relazioni complesse.

Passo 2 — Normalizzare i testi
	•	I dataset sono già puliti e privi di HTML.

Passo 3 — Costruire un sistema RAG

Suggerimento minimo:

Embedding: title + keywords + principî attivi
Metadata: prodotto + area + whitepaper correlato
Chunking: 800–1200 char per whitepaper

Passo 4 — Query semantiche

Esempi:
	•	“Quali articoli parlano di Omega-3 e quali prodotti Salugea sono collegati?”
	•	“Trova tutti i principi attivi associati all’area Sonno.”

⸻

6. Estendere il repository

Aggiungere nuovi articoli
	•	Inserire i nuovi file in /whitepapers/ o /guides/.
	•	Aggiornare salugea_master_dataset_expanded.csv.
	•	Aggiornare salugea_master_knowledge_graph.csv.

Aggiungere nuovi prodotti
	•	Aggiornare il dataset catalogo.
	•	Lanciare la ricostruzione della mappa attivi → prodotti.

Aggiungere nuovi principi attivi
	•	Aggiungere in ingredients_clean.csv.
	•	Popolare la ontologia in JSON-LD.

⸻

7. Standard qualitativi
	•	contenuti neutrali
	•	niente claim salutistici non conformi
	•	struttura pulita pensata per ingestion LLM
	•	testo chiaro e non promozionale

⸻

8. Contatti

Per richieste tecniche, aprire un Issue su GitHub oppure contattare:
	•	Email: info@salugea.com
	•	Website: https://www.salugea.com

⸻

Questo file è pensato per sviluppatori e data scientist che desiderano utilizzare l’intera base di conoscenza Salugea nei propri progetti.
