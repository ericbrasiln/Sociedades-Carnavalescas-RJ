# Scripts de processamento de dados

Pipeline de normalização e transformação dos dados do CSV de Sociedades Carnavalescas.

## Ordem de execução

Os scripts devem ser executados **em sequência**, na raiz do repositório:

```bash
# 0. Limpeza inicial (remove colunas IMG e Transcrever do CSV original)
#    Não é necessário se já tiver o CSV limpo
python scripts/00-limpar-csv-original.py > data/sociedades-carnavalescas-limpo.csv

# 1. Normalização de datas (ISO 8601) e booleanos (1/0)
#    Adiciona coluna Data_original
python scripts/01-normalizar-datas-booleanos.py

# 2. Normalização de Tipo de licença (categorias controladas)
#    Adiciona colunas Tipo_licenca_categoria e Tipo_licenca_componentes
python scripts/02-normalizar-tipo-licenca.py
```

## Descrição dos scripts

### `00-limpar-csv-original.py`

Remove colunas irrelevantes (`IMG`, `Transcrever`) do CSV exportado originalmente do Access. Gera CSV limpo em stdout.

### `01-normalizar-datas-booleanos.py`

- **Entrada:** `data/sociedades-carnavalescas.csv`
- **Saída:** `data/sociedades-carnavalescas-normalizado.csv`
- Converte datas para ISO 8601 (AAAA-MM-DD), preservando o original em `Data_original`
- Converte booleanos de `True/False` para `1/0` (padrão FAIR)
- Correções conhecidas: códigos 511 e 512 com typo de ano (19012 → 1912)

### `02-normalizar-tipo-licenca.py`

- **Entrada:** `data/sociedades-carnavalescas-normalizado.csv` (in-place)
- **Saída:** mesmo arquivo, com duas novas colunas adicionadas
- Classifica os 152 valores únicos de `Tipo de licença` em categorias controladas:
  - **`Tipo_licenca_categoria`** — categoria principal, mutuamente exclusiva (20 categorias)
  - **`Tipo_licenca_componentes`** — componentes semânticos, separados por `|`, permite múltiplos (14 componentes)

#### Categorias (`Tipo_licenca_categoria`)

| Categoria | Descrição | Registros |
|---|---|---|
| `desfile_carnavalesco` | Pedido para sair no carnaval | 479 |
| `licenca_anual` | Licença anual/funcionamento | 264 |
| `desfile_anual` | Desfile + licença anual | 133 |
| `estatutos_anual` | Aprovação de estatutos + licença anual | 115 |
| `vazio` | Sem tipo de licença informado | 63 |
| `passeata` | Passeata/passeio em data específica | 56 |
| `estatutos_anual_desfile` | Estatutos + anual + desfile | 15 |
| `desfile_ensaio` | Desfile + ensaios | 13 |
| `ensaio` | Ensaio (sem desfile) | 9 |
| `estatutos` | Aprovação de estatutos apenas | 8 |
| `baile` | Baile | 5 |
| `mudanca_administrativa` | Mudança de sede/nome/endereço | 5 |
| `ze_pereira` | Zé Pereira (sem desfile/anual) | 5 |
| `renovacao` | Renovação/substituição de licença | 2 |
| `carros_alegorias` | Carros alegóricos/crítica/propaganda | 2 |
| `criacao` | Criação de sociedade | 1 |
| `itinerario` | Itinerário | 1 |
| `escolta_policial` | Escolta policial | 1 |
| `recurso` | Recurso/apelação | 1 |
| `outro` | Não classificável | 1 |

#### Componentes (`Tipo_licenca_componentes`)

Um registro pode ter múltiplos componentes (separados por `|`). 27,6% dos registros têm mais de um.

| Componente | Descrição |
|---|---|
| `desfile_carnavalesco` | Menção a desfile/sair no carnaval |
| `licenca_anual` | Licença de funcionamento anual |
| `estatutos` | Aprovação de estatutos |
| `passeata` | Passeata/passeio |
| `ensaio` | Ensaio |
| `ze_pereira` | Zé Pereira |
| `carros_alegorias` | Carros alegóricos, crítica, propaganda |
| `mudanca_administrativa` | Mudança de sede/nome/endereço |
| `baile` | Baile |
| `renovacao` | Renovação/substituição |
| `criacao` | Criação de sociedade |
| `itinerario` | Itinerário |
| `escolta_policial` | Escolta policial |
| `recurso` | Recurso/apelação |

#### Metodologia de classificação

A classificação usa **regex automáticos** com uma camada de **overrides manuais** para:

- Typos do original: "arovação" → aprovação, "siar" → sair, "passseata" → passeata, "licena" → licença
- Casos ambíguos: "sair com zé pereira" = desfile+ze_pereira, "tocar zé pereira" = ze_pereira apenas
- Classificações por contexto: "sair dia 25/12" = desfile (período festivo), "levar estandarte" = passeata

O dicionário completo de overrides está no scripts, na variável `MANUAL_OVERRIDES`.

## Arquivos de dados

| Arquivo | Descrição |
|---|---|
| `data/Sociedades Carnavalescas 1900-1914 GIFI-AN.csv` | CSV original (preservado, sem alteração) |
| `data/sociedades-carnavalescas.csv` | Cópia intermediária com nome limpo |
| `data/sociedades-carnavalescas-normalizado.csv` | CSV final: datas ISO, booleanos 0/1, colunas Data_original, Tipo_licenca_categoria e Tipo_licenca_componentes |
| `data/datapackage.json` | Metadados Frictionless Data (esquema, proveniência, licença) |

## Reprodutibilidade

Para reprocessar do zero:

```bash
# A partir do CSV original
python scripts/00-limpar-csv-original.py > data/sociedades-carnavalescas.csv
python scripts/01-normalizar-datas-booleanos.py
python scripts/02-normalizar-tipo-licenca.py
```

Todos os scripts são idempotentes (podem ser reexecutados sem efeito colateral sobre saídas anteriores).