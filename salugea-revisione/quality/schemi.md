# Schemi proposti per la revisione

Questi campi sono una proposta: compilare solo dati verificati e conservare le versioni precedenti.

**Prodotto:** `product_id`, `nome`, `versione_formula`, `url_scheda`, `url_etichetta`, `formato`, `dose_giornaliera`, `avvertenze`, `conservazione`, `data_fonte`, `data_verifica`, `revisore`.

**Ingrediente per prodotto:** `product_id`, `versione_formula`, `nome_ingrediente`, `nome_scientifico`, `parte`, `tipo_estratto`, `titolazione`, `quantità`, `unità`, `base_quantità`, `fonte`, `data_verifica`.

**Evidenza:** `evidence_id`, `doi_o_pmid`, `url`, `tipo_studio`, `popolazione`, `intervento`, `dose`, `durata`, `esito`, `limiti`, `oggetto_studiato`, `revisore`, `data_revisione`.

**Certificazione:** `product_id`, `ente`, `programma`, `oggetto`, `lotto`, `validità_da`, `validità_a`, `url_verifica`, `stato_verifica`.

Le relazioni fra tabelle devono indicare fonte e versione. I campi mancanti restano vuoti.
