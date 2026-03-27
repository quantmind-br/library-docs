---
title: Introdução - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/v1/api-reference/introduction
source: sitemap
fetched_at: 2026-03-23T07:37:34.45933-03:00
rendered_js: false
word_count: 169
summary: This document outlines the foundational requirements for integrating with the Firecrawl API, including base URL, authentication via Bearer tokens, HTTP status code handling, and rate limiting policies.
tags:
    - api-authentication
    - rate-limiting
    - http-status-codes
    - api-integration
    - firecrawl-api
category: reference
---

## Recursos

## URL base

Todas as solicitações usam a seguinte URL base:

```
https://api.firecrawl.dev
```

## Autenticação

Para autenticar, inclua um cabeçalho Authorization. Esse cabeçalho deve conter `Bearer fc-123456789`, em que `fc-123456789` é a sua chave de API.

```
Authorization: Bearer fc-123456789
```

​

## Códigos de resposta

Firecrawl utiliza códigos de status HTTP convencionais para indicar o resultado das suas solicitações. Em geral, códigos 2xx indicam sucesso, 4xx representam erros relacionados ao cliente e 5xx sinalizam problemas de infraestrutura.

StatusDescrição200Solicitação bem-sucedida.400Verifique se os parâmetros estão corretos.401A chave de API não foi fornecida.402Pagamento necessário404O recurso solicitado não foi encontrado.429O limite de taxa foi excedido.5xxIndica um erro de servidor no Firecrawl.

Consulte a seção Códigos de erro para uma explicação detalhada de todos os erros de API possíveis.

## Limite de taxa

A API do Firecrawl possui um limite de taxa para garantir a estabilidade e confiabilidade do serviço. O limite se aplica a todos os endpoints e é baseado no número de solicitações feitas em um determinado período. Ao exceder o limite de taxa, você receberá o código de status 429.