#!/usr/bin/env python3
"""
Normaliza a coluna 'Tipo de licença' em duas colunas controlled:
- Tipo_licenca_categoria: categoria principal (mutuamente exclusiva)
- Tipo_licenca_componentes: componentes semânticos (pipe-separated, múltiplos)

Lê o CSV normalizado (com datas ISO e booleanos 0/1) e adiciona as duas colunas.
"""

import csv
import re
from collections import Counter

INPUT = 'data/sociedades-carnavalescas-normalizado.csv'
OUTPUT = 'data/sociedades-carnavalescas-normalizado.csv'  # in-place

# ── Componentes semânticos ──────────────────────────────────────

def detect_components(val):
    """Detecta componentes semânticos no campo Tipo de licença original."""
    if not val or not val.strip():
        return []

    v = val.lower().strip()
    components = []

    # 1. Desfile carnavalesco
    if re.search(r'carnav', v) and 'mudar' not in v:
        components.append('desfile_carnavalesco')

    # 2. Licença anual / funcionamento
    if re.search(r'licen[çc]a anual|funcionar|corrente ano|ao longo do ano|durante o ano|uma vez por mez|licen[çc]a para funcionar|^licen[çc]a$', v):
        components.append('licenca_anual')

    # 3. Aprovação de estatutos
    if re.search(r'arova[çc]|[aá]prova[çc][aãá][oõ]?\s*(d[eo])?\s*estatuto|estatuto', v):
        components.append('estatutos')

    # 4. Passeata/passeio (não-carnavalesco) + visitas/estandartes
    if re.search(r'passeata|passseata|passeta|passeio|visitar|estandarte|tocar na igrej', v):
        if 'carnav' not in v:
            components.append('passeata')

    # 5. Ensaio
    if re.search(r'ensai', v):
        components.append('ensaio')

    # 6. Zé Pereira
    if re.search(r'z[eé]\s*pereira|z[eé]-pereira|z[eé] ?pereira', v):
        components.append('ze_pereira')

    # 7. Baile
    if re.search(r'baile', v):
        components.append('baile')

    # 8. Mudança administrativa
    if re.search(r'mudan[çc]a de (sede|endere[çc]o|nome)|transfer[eê]ncia de sede', v):
        components.append('mudanca_administrativa')

    # 9. Renovação / segunda via
    if re.search(r'renova[rç][cã][aáo]|segunda via|substituir licen[çc]a|renovar licen[çc]a', v):
        components.append('renovacao')

    # 10. Carros/alegorias/crítica/propaganda
    if re.search(r'carro|alegori|cr[ií]tica|propaganda|reclame|carreata', v):
        components.append('carros_alegorias')

    # 11. Escolta policial
    if re.search(r'escolta policial', v):
        components.append('escolta_policial')

    # 12. Itinerário
    if v.strip() == 'itinerário':
        components.append('itinerario')

    # 13. Criação de sociedade
    if v.strip() == 'criação':
        components.append('criacao')

    # 14. Recurso/apelação
    if re.search(r'recorrendo|reaver|impugnad', v):
        components.append('recurso')

    # 15. Estandarte (passeata ceremonial)
    if re.search(r'estandarte', v):
        components.append('passeata')

    # Regex automático para "sair" no contexto carnavalesco
    if 'desfile_carnavalesco' not in components:
        # "sair" + datas carnavalescas
        if re.search(r'sair (no |nos |na |domingo |3[ªª] )', v):
            if 'carnav' in v or 'aleluia' in v:
                components.append('desfile_carnavalesco')
            elif 'passeata' not in v and 'ze_pereira' not in '|'.join(components):
                # "sair a rua", "sair hoje e amanhã" = desfile genérico
                components.append('desfile_carnavalesco')
        elif v.strip().startswith('sair') and 'passeata' not in v:
            # "sair dia 25/12", "sair ente 24/12", etc. = festivo
            if re.search(r'sair (dia |com |ente |a rua|hoje)', v):
                components.append('desfile_carnavalesco')
        # "sairno" (sem espaço)
        if re.search(r'sairno', v):
            components.append('desfile_carnavalesco')

    # "sábado de aleluia" é contexto carnavalesco
    if re.search(r'aleluia|s[aá]bado', v) and 'desfile_carnavalesco' not in components:
        components.append('desfile_carnavalesco')

    # "sair com zé pereira" adiciona desfile; "tocar zé pereira" sozinho NÃO
    if 'ze_pereira' in components and 'desfile_carnavalesco' not in components:
        if re.search(r'sair com z[eé]', v):
            components.append('desfile_carnavalesco')

    return sorted(set(components))


# ── Override manual para casos ambíguos ────────────────────────

MANUAL_OVERRIDES = {
    "licença": ("licenca_anual", ["licenca_anual"]),
    "sair no sábado de aleluia": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "renovar licença": ("renovacao", ["renovacao"]),
    "sair 3ª feira de caranval": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "sair dia 25/12 e em janeiro": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "sair dia 24/12 e em janeiro": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "sair com zé pereira de 30/12 a 01/01": ("ze_pereira", ["desfile_carnavalesco", "ze_pereira"]),
    "sair ente 24/12 e 20/01": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "licença para funcionar": ("licenca_anual", ["licenca_anual"]),
    "licença para levar estandarte até o clube dos fenianos": ("passeata", ["passeata"]),
    "levar estandarte até o JB": ("passeata", ["passeata"]),
    "sair hoje e amanhã": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "sair a rua": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "sair no domingo de carnaval": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "sair no carnaval dia": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "sair domingo de carnaval": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "sairno carnaval e fazer carreata no domingo próximo": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "sair na 3ª feira de carnaval": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    # Typos e casos variados
    "licena anual": ("licenca_anual", ["licenca_anual"]),
    "siar dia 24/02": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "para visitar o grupo estrela dalva": ("passeata", ["passeata"]),
    "saída para tocar na igreja de santo antonio": ("passeata", ["passeata"]),
    "mudar o carnaval para abril": ("mudanca_administrativa", ["mudanca_administrativa"]),
    "festividade africana": ("desfile_carnavalesco", ["desfile_carnavalesco"]),
    "realizar bando precatório": ("outro", ["outro"]),
    # Zé Pereira sem desfile carnavalesco
    "funcionar e tocar zé pereira aos domingos": ("licenca_anual", ["licenca_anual", "ze_pereira"]),
    "licença para tocar ze pereira como recleme de seu negócio": ("ze_pereira", ["ze_pereira"]),
}


def classify_category(components, original_val):
    """Determina a categoria principal baseada nos componentes."""
    if not components:
        return 'indefinido'

    c = set(components)

    # Combinações compostas (prioridade decrescente)
    if 'estatutos' in c and 'licenca_anual' in c and 'desfile_carnavalesco' in c:
        return 'estatutos_anual_desfile'
    if 'estatutos' in c and 'licenca_anual' in c:
        return 'estatutos_anual'
    if 'estatutos' in c:
        return 'estatutos'
    if 'desfile_carnavalesco' in c and 'licenca_anual' in c:
        return 'desfile_anual'
    if 'desfile_carnavalesco' in c and 'ensaio' in c:
        return 'desfile_ensaio'
    if 'desfile_carnavalesco' in c:
        return 'desfile_carnavalesco'
    if 'licenca_anual' in c:
        return 'licenca_anual'
    if 'passeata' in c:
        return 'passeata'
    if 'ensaio' in c:
        return 'ensaio'
    if 'ze_pereira' in c:
        return 'ze_pereira'
    if 'baile' in c:
        return 'baile'
    if 'mudanca_administrativa' in c:
        return 'mudanca_administrativa'
    if 'renovacao' in c:
        return 'renovacao'
    if 'carros_alegorias' in c:
        return 'carros_alegorias'
    if 'escolta_policial' in c:
        return 'escolta_policial'
    if 'itinerario' in c:
        return 'itinerario'
    if 'criacao' in c:
        return 'criacao'
    if 'recurso' in c:
        return 'recurso'

    return 'outro'


# ── Processar CSV ──────────────────────────────────────────────

with open(INPUT, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Adicionar novas colunas
if 'Tipo_licenca_categoria' not in fieldnames:
    fieldnames += ['Tipo_licenca_categoria', 'Tipo_licenca_componentes']

cat_counts = Counter()
comp_counts = Counter()
indefinidos = []

for row in rows:
    val = row.get('Tipo de licença', '').strip()

    if not val:
        row['Tipo_licenca_categoria'] = 'vazio'
        row['Tipo_licenca_componentes'] = ''
        cat_counts['vazio'] += 1
        continue

    # Verificar override manual
    if val in MANUAL_OVERRIDES:
        cat, comps = MANUAL_OVERRIDES[val]
        row['Tipo_licenca_categoria'] = cat
        row['Tipo_licenca_componentes'] = '|'.join(comps)
        cat_counts[cat] += 1
        for c in comps:
            comp_counts[c] += 1
        continue

    # Classificação automática
    components = detect_components(val)
    category = classify_category(components, val)

    row['Tipo_licenca_categoria'] = category
    row['Tipo_licenca_componentes'] = '|'.join(components)

    cat_counts[category] += 1
    for c in components:
        comp_counts[c] += 1

    if category == 'indefinido' or category == 'outro':
        indefinidos.append((val, category, components))

# Escrever CSV atualizado
with open(OUTPUT, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Relatório
print(f"CSV atualizado: {OUTPUT}")
print(f"Total de registros: {len(rows)}")
print(f"Campos: {len(fieldnames)} colunas")
print()

print("=== CATEGORIAS (Tipo_licenca_categoria) ===")
for cat, count in cat_counts.most_common():
    pct = count / len(rows) * 100
    print(f"  {cat:30s} {count:5d} ({pct:.1f}%)")

print(f"\n=== COMPONENTES (Tipo_licenca_componentes) ===")
for comp, count in comp_counts.most_common():
    print(f"  {comp:30s} {count:5d}")

if indefinidos:
    print(f"\n⚠ {len(indefinidos)} casos indefinidos/outros:")
    for val, cat, comps in indefinidos:
        print(f'  "{val}" → {cat} [{comps}]')
else:
    print("\n✓ Todos os registros classificados!")

# Estatísticas de componente múltiplo
multi = sum(1 for r in rows if '|' in r.get('Tipo_licenca_componentes', ''))
print(f"\nRegistros com componentes múltiplos: {multi} ({multi/len(rows)*100:.1f}%)")