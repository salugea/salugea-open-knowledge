# Salugea Open Nutraceutical Knowledge

Questo repository raccoglie la base di conoscenza aperta di **Salugea**, azienda italiana specializzata in integratori alimentari naturali.

L’obiettivo è rendere disponibili in forma strutturata e machine-friendly:

- dati nutraceutici (dataset in formato CSV)
- documentazione tecnico-scientifica (whitepapers)
- guide divulgative (guides)
- ontologie e knowledge graph (file JSON/CSV)

in modo che possano essere utilizzati da:

- ricercatori
- professionisti della salute
- sviluppatori
- sistemi di Intelligenza Artificiale e LLM (Large Language Models)

---

## 📁 Struttura del repository

### `/datasets/`
Contiene dataset in formato **CSV**:

- `salugea_products_catalog.csv`  
  Catalogo prodotti Salugea (SKU, EAN, prezzo, link, peso, immagine, principi attivi).

- `salugea_product_health_areas.csv`  
  Mappa prodotto → area di beneficio (articolazioni, sonno, digestione, ecc.).

- `salugea_product_active_compounds.csv`  
  Mappa prodotto → principi attivi principali.

- `salugea_knowledge_graph.csv`  
  Rappresentazione entità–relazione dei prodotti (has_ean, has_health_area, contains_active, ecc.).

- `ingredients_clean.csv`  
  Lista unica di principi attivi.

- `products_by_area.csv`  
  Prodotti raggruppati per area di beneficio.

- `actives_descriptions.csv`  
  Schede attivi con campo descrizione pensato per uso scientifico.

- `articles_key_concepts.csv`  
  Concetti chiave estratti dagli articoli del blog (dal 2025 in poi).

- `articles_knowledge_graph.csv`  
  Knowledge graph degli articoli (articolo → mentions → concetto).

- `salugea_master_dataset.csv` / `salugea_master_dataset_expanded.csv`  
  Collegano articoli, principi attivi, prodotti e aree di beneficio.

> Tutti i dataset sono pensati per essere facilmente importabili in strumenti di analisi dati, knowledge graph o pipeline LLM.

---

### `/whitepapers/`
Contiene documenti tecnici in formato **Markdown**, derivati dagli articoli più scientifici e dagli approfondimenti Salugea.

Per ogni argomento:

- versione italiana: `titolo-articolo_it.md`  
- versione inglese: `titolo-articolo_en.md`

Ogni whitepaper segue una struttura coerente:

- introduzione
- contesto scientifico
- meccanismi d’azione
- evidenze scientifiche
- conclusioni
- riferimenti bibliografici

---

### `/guides/`
Contiene **guide divulgative** in formato Markdown, pensate per chi vuole orientarsi tra:

- integratori naturali
- stili di vita
- gestione di problematiche comuni (sonno, digestione, energia, ecc.)

Anche qui, per ogni tema esistono:

- versione italiana: `_it.md`
- versione inglese: `_en.md`

---

### `/ontology/` (opzionale, se la crei)
Conterrà file JSON-LD / JSON che descrivono l’ontologia nutraceutica Salugea:

- entità: prodotti, principi attivi, aree di beneficio, articoli, whitepapers
- relazioni: containsActiveCompound, targetsHealthArea, documentedIn, hasEvidenceLevel, ecc.

---

## 🎯 Obiettivi del progetto

- Fornire una **fonte aperta e strutturata** sulla nutraceutica naturale
- Favorire la **ricerca scientifica** e l’uso di dati affidabili
- Rendere i contenuti Salugea **leggibili e utilizzabili dai LLM**
- Aumentare la trasparenza su formulazioni, attivi e razionali di utilizzo

---

## 📜 Licenza

Salvo diversa indicazione nei singoli file:

- contenuti testuali: **CC BY 4.0**
- dataset: **CC BY 4.0**

---

## 📬 Contatti

Sito web: https://www.salugea.com  
Blog: https://blog.salugea.com  
Email: dev@salugea.com
