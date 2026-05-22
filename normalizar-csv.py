#!/usr/bin/env python3
"""
Normaliza o CSV de Sociedades Carnavalescas:
1. Datas → ISO 8601 (AAAA-MM-DD), preservando originais em coluna _Data_original
2. Booleanos → 1/0 (padrão FAIR)

Casos especiais de data:
  - "1909", "1912" etc. (só ano) → "1909", mantém como ano-only
  - "23/11/19012" (erro de digitação) → assumir 1912 → "1912-11-23"
  - "17/11/19012" → "1912-11-17"
  - "03/1912" (mês/ano) → "1912-03"
  - vazio → vazio
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
    
    # Already just a year (e.g. "1909", "1912")
    if raw.isdigit() and len(raw) == 4:
        return raw
    
    # MM/AAAA format (e.g. "03/1912")
    if raw.count('/') == 1:
        parts = raw.split('/')
        month, year = parts[0].strip(), parts[1].strip()
        if year.isdigit() and len(year) == 4 and month.isdigit():
            return f'{year}-{month.zfill(2)}'
    
    # DD/MM/AAAA format
    if raw.count('/') == 2:
        parts = raw.split('/')
        day, month, year = parts[0].strip(), parts[1].strip(), parts[2].strip()
        # Handle typos like 19012 → 1912
        if year.startswith('190') and len(year) == 5:
            year = year[:4]  # truncate extra digit
        if day.isdigit() and month.isdigit() and year.isdigit() and len(year) == 4:
            return f'{year}-{month.zfill(2)}-{day.zfill(2)}'
    
    # Fallback: return as-is (shouldn't happen with clean data)
    return raw

def normalize_bool(val):
    """Convert True/False to 1/0."""
    val = val.strip()
    if val == 'True':
        return '1'
    elif val == 'False':
        return '0'
    return val

# Read
with open(INPUT, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    original_fields = reader.fieldnames
    rows = list(reader)

# Boolean columns
BOOL_COLS = ['Licença', 'Estatuto', 'Licença anterior', 'Nomes/Sujeitos', 'Doc policial']

# New field order: add Data_original after Data
new_fields = []
for f in original_fields:
    new_fields.append(f)
    if f == 'Data':
        new_fields.append('Data_original')

# Process
for row in rows:
    # Normalize date
    original_date = row['Data']
    row['Data'] = normalize_date(original_date, row['Código'])
    row['Data_original'] = original_date.strip()
    
    # Normalize booleans
    for col in BOOL_COLS:
        row[col] = normalize_bool(row[col])

# Write
with open(OUTPUT, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=new_fields)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

# Verify
with open(OUTPUT, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows_out = list(reader)
    print(f'Registros escritos: {len(rows_out)}')
    
    # Check all dates
    bad = []
    for r in rows_out:
        d = r['Data']
        if d and not r['Data_original'] == '':
            # Should be ISO-ish
            if d.count('-') == 0 and len(d) == 4:
                continue  # year-only is fine
            if d.count('-') == 1:
                continue  # year-month is fine
            if d.count('-') == 2:
                parts = d.split('-')
                if len(parts[0]) == 4 and len(parts[1]) == 2 and len(parts[2]) == 2:
                    continue
            bad.append((r['Código'], d, r['Data_original']))
    print(f'Datas não-ISO: {len(bad)}')
    for code, d, orig in bad:
        print(f'  Código {code}: ISO="{d}" original="{orig}"')
    
    # Check booleans
    for col in BOOL_COLS:
        vals = set(r[col] for r in rows_out)
        print(f'  {col}: {vals}')
    
    # Check some conversions
    print('\nAmostra de linhas normalizadas:')
    for r in rows_out[:3]:
        print(f'  Código {r["Código"]}: Data={r["Data"]}, Data_original={r["Data_original"]}, Licença={r["Licença"]}')