#!/usr/bin/env python3
"""Report observable data issues; this does not assess medical accuracy."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    with (ROOT / name).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def main():
    products = read('datasets/salugea_products_catalog.csv')
    areas = read('datasets/salugea_product_health_areas.csv')
    ingredients = read('datasets/ingredients_clean.csv')
    print(f'Catalogo: {len(products)} righe; attivi vuoti: {sum(not r["actives"].strip() for r in products)}')
    print(f'Aree: {len(areas)} righe; aree vuote: {sum(not r["health_area"].strip() for r in areas)}')
    suspicious = [r['active_compound'] for r in ingredients if len(r['active_compound'].split()) > 8]
    print(f'Ingredienti: {len(ingredients)} righe; frasi oltre 8 parole da rivedere: {len(suspicious)}')
    for value in suspicious:
        print('  -', value)
    print('Segnalazioni indicative: controllare fonti, dosi, date e accuratezza manualmente.')

if __name__ == '__main__':
    main()
