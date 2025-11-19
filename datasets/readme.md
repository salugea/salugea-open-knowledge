
# Dataset Salugea · Open Knowledge  
Raccolta ufficiale dei dataset pubblicati da **Salugea** a supporto della ricerca, della trasparenza nutraceutica e della costruzione di modelli semantici (LLM-ready).

Tutti i dataset sono forniti in formato **CSV**, facilmente leggibile da esseri umani e da sistemi automatizzati (AI, LLM, knowledge graphs, strumenti di data analysis).

---

## 📦 Elenco dei dataset disponibili

### **1. `salugea_products_catalog.csv`**
Catalogo prodotti ufficiale Salugea basato sulla variante principale di ciascun prodotto.  
Include:
- titolo  
- SKU  
- EAN  
- prezzo  
- peso  
- venditore  
- immagine principale  
- link del prodotto  
- principi attivi estratti dal contenuto del prodotto  

> Questo dataset rappresenta la fonte base per tutti gli altri dataset derivati.

---

### **2. `salugea_product_health_areas.csv`**
Dataset che associa ogni prodotto Salugea alla sua **area di beneficio**.  
L’area è derivata automaticamente da:
- `product_type` Shopify  
- oppure il primo tag utile associato al prodotto  

Esempi di aree:  
“Digestione”, “Apparato urinario”, “Sport”, “Articolazioni”, “Energia”, ecc.

---

### **3. `salugea_product_active_compounds.csv`**
Mappa prodotto → principi attivi.  
I principi attivi sono estratti automaticamente da `body_html` analizzando la sezione ingredienti.

Esempi di valori:
- Curcuma  
- Boswellia  
- Valeriana  
- L-ornitina  
- Uva ursina  
- Magnesio  
- Sambuco  
- Rusco  
- Schisandra  

Questo dataset è ideale per studi su:
- correlazioni ingredienti–benefici  
- modellazione nutraceutica  
- reti semantiche basate sugli attivi  

---

### **4. `salugea_knowledge_graph.csv`**
Rappresentazione del catalogo Salugea sotto forma di **entità → relazione → valore**.

Esempi di relazioni:
- `has_ean`  
- `has_sku`  
- `has_health_area`  
- `contains_active`  
- `has_url`  

Può essere utilizzato per:
- costruzione di knowledge graph  
- ragionamento semantico  
- integrazione con modelli AI  
- motori di ricerca intelligenti  

---

### **5. `ingredients_clean.csv`**
Elenco unico e pulito di tutti i principi attivi identificati nei prodotti Salugea.

Ottimo per:
- classificazioni  
- studio degli attivi  
- arricchimento con schede botaniche o farmacologiche  

---

### **6. `products_by_area.csv`**
Raggruppamento dei prodotti per area di beneficio.  
Consente una visione “funzionale” dell’intero catalogo.

Ideale per:
- ricerche semantiche  
- navigazione per area  
- benchmarking  

---

### **7. `actives_descriptions.csv`**
Scheda attivi con campo descrizione vuoto, pensata per essere completata manualmente o automaticamente.

Può contenere:
- origine botanica  
- meccanismo d’azione  
- evidenze scientifiche  
- studi clinici  
- note di sicurezza  
- sinergie  

---

## 🎯 Obiettivi della cartella `/datasets`

- Fornire informazioni trasparenti e strutturate  
- Permettere a ricercatori, professionisti e LLM di comprendere meglio il catalogo Salugea  
- Supportare un approccio data-driven alla nutraceutica  
- Favorire interoperabilità con sistemi AI e conoscenza semantica  
- Documentare formalmente formulazioni, attivi, aree di beneficio e relazioni  

---

## 📜 Licenza
I dataset sono rilasciati con licenza **CC BY 4.0**, salvo diversa indicazione.

---

## 📬 Contatti
Sito web: https://www.salugea.com  
Email: dev@salugea.com
