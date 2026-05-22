<p align="center"><img src="images/capa-SC.png" width="100%"/></p>

[![DOI:10.13140/RG.2.2.31670.83521/1](https://zenodo.org/badge/DOI/10.13140/RG.2.2.31670.83521/1.svg)](http://dx.doi.org/10.13140/RG.2.2.31670.83521/1)

**Eric Brasil**

*Banco de dados produzido a partir da documentação do GIFI-AN: pedidos de licenças de sociedades carnavalescas entre 1900 e 1914.*

**A ferramenta foi desenvolvida apenas para pesquisas acadêmicas, sem fins lucrativos.**
**O banco não se propôs a esgotar as fontes do GIFI, nem mesmo da documentação referente aos pedidos de licença.**

## Acesso

👉 **[sociedades-carnavalescas.ericbrasiln.github.io](https://ericbrasiln.github.io/Sociedades-Carnavalescas-RJ/)**

## Funcionalidades

- 🔍 **Busca fuzzy** — encontre termos mesmo com variações de grafia ou acentuação
- 🏷️ **Facetas** — filtre rapidamente por presença de licença, estatuto, nomes/sujeitos ou documento policial
- 📊 **Visualizações** — gráficos interativos de distribuição por ano, tipos de licença, presença de elementos e sociedades mais mencionadas
- 📋 **Ficha detalhada** — clique em qualquer registro para ver todos os campos
- 📥 **Download CSV** — arquivo original disponível para download
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
- **Data** — data do pedido de licença
- **Endereço** — endereço da associação
- **Licença** — se contém pedido de licença (True/False)
- **Estatuto** — se contém estatuto (True/False)
- **Notação-GIFI** — referência arquivística
- **Tipo de licença** — descrição do tipo de licença solicitada
- **Obs** — comentários breves da época da pesquisa
- **Presidente** — nome do presidente, quando registrado
- **Licença anterior** — se há registro de licença anterior (True/False)
- **Nomes/Sujeitos** — se há referência aos membros ou diretoria (True/False)
- **Doc policial** — se é um documento interno da polícia (True/False)

**As colunas booleanas (True/False) indicam se a informação consta na fonte.**

## Questões técnicas e História Digital

O site foi construído com HTML, CSS e JavaScript puros (sem frameworks), com Fuse.js para busca fuzzy e Chart.js para gráficos interativos. O CSV carrega client-side, sem necessidade de backend. Hospedado via GitHub Pages.

Para o caso do banco de dados Sociedades Carnavalescas, utilizei Python para manipular o CSV original e gerar a versão web.

## Como citar

BRASIL, Eric. *Banco de dados de Sociedades Carnavalescas do Rio de Janeiro, 1900-1914 - GIFI/AN*. 2016. Disponível em <https://ericbrasiln.github.io/Sociedades-Carnavalescas-RJ/>. DOI: http://dx.doi.org/10.13140/RG.2.2.31670.83521/1

```bibtex
@misc{sociedades-carnavalescas-RJ,
  author = {Eric Brasil},
  title = {Banco de dados de Sociedades Carnavalescas do Rio de Janeiro, 1900-1914 - GIFI/AN},
  year = {2016},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/ericbrasiln/Sociedades-Carnavalescas-RJ}},
  doi = {10.13140/RG.2.2.31670.83521/1}
}
```

## Licença

The MIT License (MIT)
(c) Eric Brasil 2021