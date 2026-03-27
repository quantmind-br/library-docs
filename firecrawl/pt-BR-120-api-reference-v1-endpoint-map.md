---
title: Mapear - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:10:12.197557-03:00
rendered_js: false
word_count: 163
summary: This document provides the reference specifications for an API endpoint used to map multiple URLs, including authentication requirements, request parameters, and configuration options.
tags:
    - url-mapping
    - web-scraping
    - api-reference
    - sitemap-crawling
    - proxy-configuration
category: reference
---

[Pular para o conteúdo principal](#content-area)

Mapear várias URLs de acordo com as opções

> Observação: Uma nova [versão v2 desta API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/map) já está disponível e oferece recursos e desempenho aprimorados.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corpo

A URL base de onde iniciar o rastreamento

Consulta de pesquisa usada para mapeamento. Durante a fase Alpha, o componente "inteligente" da funcionalidade de pesquisa é limitado a 500 resultados. Porém, se o mapeamento encontrar mais resultados, nenhum limite será aplicado.

Ignorar o sitemap do site durante o rastreamento.

Retorne apenas os links encontrados no sitemap do site

Incluir subdomínios do site

Número máximo de links a retornar

Intervalo obrigatório: `x <= 30000`

Tempo limite em milissegundos. Não há tempo limite definido por padrão.

Configurações de localização da requisição. Quando definidas, será usado um proxy apropriado, se disponível, e serão emuladas as configurações correspondentes de idioma e fuso horário. O padrão é "US" se não for especificado.

#### Resposta