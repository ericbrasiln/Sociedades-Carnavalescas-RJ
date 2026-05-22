<p align="center"><img src="images/capa-SC.png" width="100%"/></p>

[![DOI](https://zenodo.org/badge/268927103.svg)](https://doi.org/10.5281/zenodo.20345409)

**Eric Brasil**

*Banco de dados produzido a partir da documentação do GIFI-AN: pedidos de licenças de sociedades carnavalescas entre 1900 e 1914.*

**A ferramenta foi desenvolvida apenas para pesquisas acadêmicas, sem fins lucrativos.**
**O banco não se propôs a esgotar as fontes do GIFI, nem mesmo da documentação referente aos pedidos de licença.**

## Acesso

👉 **[sociedades-carnavalescas.ericbrasil.com.br](https://ericbrasil.com.br/Sociedades-Carnavalescas-RJ/)**

## Funcionalidades

- 🔍 **Busca avançada** — busca fuzzy com seletor de campo (Sociedade, Endereço, Assinatura, Tipo de licença etc.) e operadores lógicos (AND, OR, NOT); múltiplos termos acumuláveis; botões Incluir e Limpar
- 🏷️ **Facetas** — filtre por presença de licença, estatuto, lista de membros, documento policial e categoria de tipo de licença
- 📊 **6 gráficos interativos** — registros por ano, categoria de licença (total e ao longo do tempo), presença de elementos, tipo de sociedade (total e proporção por ano); todos reativos aos filtros
- 📋 **Ficha detalhada** — clique em qualquer registro para ver todos os campos, incluindo categoria e componentes normalizados
- 📥 **Download CSV** — CSV normalizado (ISO 8601, booleanos 0/1, categorias controladas) disponível para download
- 📱 **Responsivo** — funciona em desktop e celular

## Índice

- [Introdução](#introdução)
- [Pesquisa](#pesquisa)
  - [Fontes](#fontes)
- [Banco de dados](#banco-de-dados)
- [Questões técnicas](#questões-técnicas-e-história-digital)
- [Como citar](#como-citar)
- [Licença](#licença)

## Introdução

A publicização desse banco de dados visa tornar acessível a qualquer pessoa parte dos dados produzidos na pesquisa de doutorado entre 2012 e 2016. Ele foi pensado como um recurso para pesquisas em história social da cultura da cidade do Rio de Janeiro no início do século XX.

A criação do banco de dados público e pesquisável é fruto das reflexões e experiências empíricas de historiadores e sociólogos que têm enfrentado o [desafio de fazer ciências humanas no mundo digital](http://bibliotecadigital.fgv.br/ojs/index.php/reh/article/view/79933). Defendemos a importância da apropriação, uso, desenvolvimento e aprimoramento de ferramentas digitais para as humanidades, assim como a urgência na sofisticação teórica, metodológica e epistemológica sobre as chamadas Humanidades Digitais e especialmente sobre História Digital.

## Pesquisa

A tese de doutorado, proveniente dessa pesquisa, intitulada [*Carnavais Atlânticos: cidadania e cultura negra no pós-abolição. Rio de Janeiro e Port-of-Spain, Trinidad (1838-1920)*](https://www.historia.uff.br/stricto/td/1806.pdf), teve como objetivo principal analisar transnacionalmente experiências de mobilização negra através dos carnavais das cidades do Rio de Janeiro e de Port-of-Spain, Trinidad entre 1838 e 1920. Busquei compreender a atuação de sujeitos negros em sociedades tão distintas e como elaboraram estratégias de ação pública, de organização social e de reivindicação de direitos e cidadania no Pós-Abolição, tendo o carnaval como elemento que catalisou e potencializou suas experiências.

### Fontes

O primeiro conjunto de fontes trabalhado na pesquisa consiste nos pedidos de licença e documentação policial referentes à sociedades recreativas do Rio de Janeiro, preservadas no fundo GIFI do Arquivo Nacional.

O Grupo de Identificação de Fundos Internos - GIFI -, segundo o [site do Arquivo Nacional](http://dibrarq.arquivonacional.gov.br/index.php/diversos-gifi-caixas-e-codices), "foi formado em 1981, com o objetivo de identificar o acervo documental da antiga Seção do Poder Executivo que não tinha sofrido tratamento técnico - cerca da quinta parte do acervo da Seção." Nele encontramos inúmeras pastas sobre pedidos de licenças de associações carnavalescas.

Esses pedidos de licença forneceram um conjunto rico de dados qualitativos e quantitativos para a pesquisa, contendo nomes, endereços, profissões, estatutos, além da movimentação e argumentação das forças policiais sobre a concessão ou não das licenças solicitadas.

## Banco de dados

O banco de dados foi inicialmente elaborado em Access e recentemente transformado em CSV para melhor visualização, pesquisa e compartilhamento.

O Banco de dados Sociedades Carnavalescas possui 1178 entradas, contendo as seguintes colunas:

- **Código** — identificador numérico do registro
- **Nome da Sociedade** — nome da entidade carnavalesca
- **Data** — data do pedido de licença (formato ISO 8601: AAAA-MM-DD)
- **Data_original** — data no formato original do arquivo (DD/MM/AAAA)
- **Endereço** — endereço da associação
- **Licença** — se contém pedido de licença (1=sim, 0=não)
- **Estatuto** — se contém estatuto (1=sim, 0=não)
- **Notação-GIFI** — referência arquivística
- **Tipo de licença** — descrição original do tipo de licença solicitada (texto livre, 152 valores únicos)
- **Tipo_licenca_categoria** — categoria normalizada do tipo de licença, mutuamente exclusiva (20 categorias controladas)
- **Tipo_licenca_componentes** — componentes semânticos do tipo de licença, separados por `|` (14 componentes; 27,6% dos registros têm mais de um)
- **Obs** — comentários breves da época da pesquisa
- **Presidente** — signatário do pedido (presidente, secretário, vice, tesoureiro etc.)
- **Licença anterior** — se há registro de licença anterior (1=sim, 0=não)
- **Nomes/Sujeitos** — se há lista de membros ou diretoria (1=sim, 0=não)
- **Doc policial** — se é um documento interno da polícia (1=sim, 0=não)

**As colunas booleanas (1/0) indicam se a informação consta na fonte.** Veja `scripts/README.md` para detalhes sobre a normalização.

## Princípios FAIR

O dataset segue os princípios [FAIR](https://www.go-fair.org/fair-principles/) (Findable, Accessible, Interoperable, Reusable):

### Findable (Encontrável)
- Identificador persistente: DOI (Zenodo) + URL estável via GitHub Pages
- Metadados rich: `datapackage.json` (schema Frictionless Data), Dublin Core e Schema.org no HTML
- Keywords: sociedades carnavalescas, Rio de Janeiro, história digital, humanidades digitais, GIFI, Arquivo Nacional, pós-abolição, licença, carnaval

### Accessible (Acessível)
- Dados abertos em CSV via GitHub Pages e repositório público
- Protocolo aberto (HTTPS), sem autenticação
- Dados originais preservados (`data/`) ao lado da versão normalizada

### Interoperable (Interoperável)
- Formato aberto: CSV (`text/csv`)
- Datas normalizadas em ISO 8601 (AAAA-MM-DD); formato original preservado em `Data_original`
- Booleanos como 0/1 (sem ambiguidade textual)
- Vocabulário controlado: `Tipo_licenca_categoria` (20 categorias com enum no `datapackage.json`)
- Componentes semânticos: `Tipo_licenca_componentes` separados por `|`
- Pipeline de normalização documentado e versionado em `scripts/`

### Reusable (Reutilizável)
- Licença de dados: CC BY 4.0
- Licença de código: MIT
- Atribuição clara: DOI da tese, ORCID do autor, procedência do Arquivo Nacional/GIFI
- Proveniência documentada: fonte arquivística, referência ao fundo GIFI, série 6C
- Seção "Como citar" com BibTeX
- Reprodutibilidade: 3 scripts numerados, idempotentes, com `scripts/README.md`

## Questões técnicas e História Digital

O site foi construído com HTML, CSS e JavaScript puros (sem frameworks), com Fuse.js para busca fuzzy e Chart.js para gráficos interativos. O CSV carrega client-side, sem necessidade de backend. Hospedado via GitHub Pages.

Para o caso do banco de dados Sociedades Carnavalescas, utilizei Python para manipular o CSV original e gerar a versão web.

## Como citar

BRASIL, Eric. *Banco de dados de Sociedades Carnavalescas do Rio de Janeiro, 1900-1914 - GIFI/AN*. 2016. Disponível em <https://ericbrasil.com.br/Sociedades-Carnavalescas-RJ/>. DOI: http://dx.doi.org/10.5281/zenodo.20345409

```bibtex
@misc{sociedades-carnavalescas-RJ,
  author = {Eric Brasil},
  title = {Banco de dados de Sociedades Carnavalescas do Rio de Janeiro, 1900-1914 - GIFI/AN},
  year = {2016},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/ericbrasiln/Sociedades-Carnavalescas-RJ}},
  doi = {10.5281/zenodo.20345409}
}
```

## Uso de inteligência artificial

Em conformidade com o Art. 9º, inciso I, alínea "c", da [Portaria CNPq nº 2.664/2026](https://www.in.gov.br/web/dou/-/portaria-cnpq-n-2.664-de-6-de-marco-de-2026-612498498), declaramos que a ferramenta de inteligência artificial generativa **Hermes Agent** foi utilizada na atualização deste site e na normalização dos dados. As ferramentas de IAG auxiliaram na estruturação do HTML/CSS/JS, na classificação semântica da coluna "Tipo de licença" em categorias controladas e na geração dos scripts de normalização. O conteúdo final, os dados originais, a análise e as decisões metodológicas são de inteira responsabilidade do autor.

## Licença

The MIT License (MIT)
(c) Eric Brasil 2021