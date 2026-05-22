#!/usr/bin/env python3
"""
Limpeza inicial do CSV original exportado do Access.

Operações:
  - Remove colunas IMG e Transcrever (vazias ou irrelevantes)
  - Salva resultado intermediário

Entrada:  data/Sociedades Carnavalescas 1900-1914 GIFI-AN.csv
Saída:    (stdout — CSV limpo sem as colunas removidas)

Uso:
  python scripts/00-limpar-csv-original.py > data/sociedades-carnavalescas-limpo.csv

Nota: Este script foi reescrito a partir do original tratamento-csv.py
      (que usava caminhos absolutos hardcoded). A versão original
      está preservada em scripts/original/tratamento-csv.py.
"""
import csv
import sys

INPUT = 'data/Sociedades Carnavalescas 1900-1914 GIFI-AN.csv'
DROP_COLS = {'IMG', 'Transcrever'}

with open(INPUT, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    orig_fields = reader.fieldnames
    keep_fields = [h for h in orig_fields if h not in DROP_COLS]
    writer = csv.DictWriter(sys.stdout, fieldnames=keep_fields)
    writer.writeheader()
    for row in reader:
        clean_row = {k: row[k] for k in keep_fields}
        writer.writerow(clean_row)