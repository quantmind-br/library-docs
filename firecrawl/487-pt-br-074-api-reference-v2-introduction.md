---
title: Introdução - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v2-introduction
source: sitemap
fetched_at: 2026-03-23T07:32:01.515536-03:00
rendered_js: false
word_count: 228
summary: This document provides the foundational technical specifications for the Firecrawl API, including authentication, base URL, response code handling, and rate limiting policies.
tags:
    - api-documentation
    - authentication
    - rate-limiting
    - http-status-codes
    - firecrawl-api
category: reference
---

A API do Firecrawl oferece acesso programático a dados da web. Todos os endpoints compartilham uma URL base comum, um esquema de autenticação e um formato de resposta descritos nesta página.

## Recursos

## Recursos de agentes

## URL base

Todas as requisições usam a seguinte URL base:

```
https://api.firecrawl.dev
```

## Autenticação

Toda requisição exige um cabeçalho `Authorization` com sua chave de API:

```
Authorization: Bearer fc-YOUR-API-KEY
```

Inclua este cabeçalho em todas as chamadas à API. Você pode encontrar sua chave de API no [painel do Firecrawl](https://www.firecrawl.dev/app/api-keys).

## Códigos de resposta

O Firecrawl usa códigos de status HTTP convencionais para indicar o resultado das suas requisições. Códigos na faixa `2xx` indicam sucesso, códigos `4xx` indicam erros do cliente e códigos `5xx` indicam erros do servidor.

StatusDescrição`200`Requisição bem-sucedida.`400`Parâmetros de requisição inválidos.`401`Chave de API ausente ou inválida.`402`Pagamento necessário.`404`O recurso solicitado não foi encontrado.`429`Limite de requisições excedido.`5xx`Erro de servidor no Firecrawl.

Quando ocorre um erro `5xx`, o corpo da resposta inclui um código de erro específico para ajudar você a diagnosticar o problema.

## Limite de taxa de requisições

A API do Firecrawl impõe limites de taxa de requisições em todos os endpoints para garantir a estabilidade do serviço. Esses limites são definidos com base no número de requisições em uma janela de tempo específica. Quando você ultrapassa o limite de taxa, a API retorna o código de status `429`. Aguarde um pouco e tente fazer a requisição novamente após um breve intervalo.