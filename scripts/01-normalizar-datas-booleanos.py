#!/usr/bin/env python3
"""
Normaliza datas e booleanos do CSV para conformidade FAIR.

Operações:
  - Datas → ISO 8601 (AAAA-MM-DD), preservando originais em coluna Data_original
  - Booleanos → 1/0 (padrão FAIR, True/False legado)
  - Correções conhecidas: códigos 511 e 512 com typo de ano (19012 → 1912)

Entrada:  data/sociedades-carnavalescas.csv (ou CSV intermediário)
Saída:    data/sociedades-carnavalescas-normalizado.csv

Uso:
  python scripts/01-normalizar-datas-booleanos.py

Nota: Adiciona coluna Data_original com datas no formato DD/MM/AAAA do arquivo
      original. A coluna Data passa a conter valores ISO 8601.
"""
import csv
import os

INPUT = 'data/sociedades-carnavalescas.csv'
OUTPUT = 'data/sociedades-carnavalescas-normalizado.csv'

# Known corrections (código → fixed ISO date)
DATE_FIXES = {
    '511': '1912-11-23',  # 23/11/19012 → 1912-11-23
    '512': '1912-11-17',  # 17/11/19012 → 1912-11-17
}

def normalize_date(raw, code):
    """Convert date string to ISO 8601."""
    raw = raw.strip()
    if not raw:
        return ''
    # Known fixes
    if code in DATE_FIXES:
        return DATE_FIXES[code]
    # YYYY only
    if len(raw) == 4 and raw.isdigit():
        return raw
    # MM/AAAA
    if '/' in raw and raw.count('/') == 1:
        parts = raw.split('/')
        if len(parts[0]) <= 2 and len(parts[1]) == 4:
            return f"{parts[1]}-{parts[0].zfill(2)}"
    # DD/MM/AAAA
    if '/' in raw and raw.count('/') == 2:
        parts = raw.split('/')
        if len(parts[2]) == 4:
            return f"{parts[2]}-{parts[1].zfill(2)}-{parts[0].zfill(2)}"
    return raw


with open(INPUT, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ['Data_original']
    rows = list(reader)

with open(OUTPUT, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        original_date = row.get('Data', '')
        row['Data_original'] = original_date
        row['Data'] = normalize_date(original_date, row.get('Código', ''))
        # Normalize booleans
        for bool_col in ['Licença', 'Estatuto', 'Licença anterior', 'Nomes/Sujeitos', 'Doc policial']:
            val = row.get(bool_col, '').strip()
            if val in ('True', 'true', '1', 'Sim', 'sim'):
                row[bool_col] = '1'
            elif val in ('False', 'false', '0', 'Não', 'não', 'Nao', 'nao'):
                row[bool_col] = '0'
        writer.writerow(row)

print(f"CSV normalizado salvo em {OUTPUT}")
print(f"  {len(rows)} registros, {len(fieldnames)} colunas")