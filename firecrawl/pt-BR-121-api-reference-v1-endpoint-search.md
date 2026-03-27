---
title: Search - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:10:00.299173-03:00
rendered_js: false
word_count: 339
summary: This document describes the /search endpoint, which enables web searching combined with content scraping, including support for search operators, location-based filtering, and temporal queries.
tags:
    - web-scraping
    - search-api
    - data-extraction
    - query-operators
    - api-documentation
category: api
---

Pesquisar e, opcionalmente, raspar os resultados da busca

> Observação: Uma nova [versão v2 desta API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/search) está disponível, com recursos e desempenho aprimorados.

O endpoint /search combina a busca na web com os recursos de scraping do Firecrawl para retornar o conteúdo completo da página para qualquer consulta. Inclua `scrapeOptions` com `formats: ["markdown"]` para obter o conteúdo completo em Markdown para cada resultado de busca; caso contrário, por padrão você receberá apenas os resultados (url, title, description).

## Operadores de consulta compatíveis

Oferecemos uma variedade de operadores de consulta que permitem filtrar melhor suas buscas.

OperadorFuncionalidadeExemplos`""`Faz correspondência exata (não difusa) com um trecho de texto`"Firecrawl"``-`Exclui determinadas palavras-chave ou nega outros operadores`-bad`, `-site:firecrawl.dev``site:`Retorna apenas resultados de um site específico`site:firecrawl.dev``inurl:`Retorna apenas resultados que incluem uma palavra na URL`inurl:firecrawl``allinurl:`Retorna apenas resultados que incluem várias palavras na URL`allinurl:git firecrawl``intitle:`Retorna apenas resultados que incluem uma palavra no título da página`intitle:Firecrawl``allintitle:`Retorna apenas resultados que incluem várias palavras no título da página`allintitle:firecrawl playground``related:`Retorna apenas resultados relacionados a um domínio específico`related:firecrawl.dev`

## Parâmetro de localização

Use o parâmetro `location` para obter resultados de pesquisa segmentados por região. Formato: `"string"`. Exemplos: `"Germany"`, `"San Francisco,California,United States"`. Consulte a [lista completa de locais compatíveis](https://firecrawl.dev/search_locations.json) para ver todos os países e idiomas disponíveis.

## Pesquisa por período

Use o parâmetro `tbs` para filtrar os resultados por períodos, incluindo intervalos de datas personalizados. Consulte a [documentação do recurso de busca](https://docs.firecrawl.dev/features/search#time-based-search) para exemplos detalhados e formatos compatíveis.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corpo

Número máximo de resultados a retornar

Intervalo obrigatório: `1 <= x <= 100`

Parâmetro de pesquisa baseado em tempo. Suporta períodos de tempo predefinidos (`qdr:h`, `qdr:d`, `qdr:w`, `qdr:m`, `qdr:y`) e intervalos de datas personalizados (`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`)

Parâmetro de localização para resultados de pesquisa

Tempo limite em milissegundos

Exclui dos resultados de pesquisa as URLs que são inválidas para outros endpoints do Firecrawl. Isso ajuda a reduzir erros se você estiver encaminhando dados da pesquisa para outros endpoints da API do Firecrawl.

Opções para extrair resultados de busca

#### Resposta

Mensagem de aviso caso ocorra algum problema