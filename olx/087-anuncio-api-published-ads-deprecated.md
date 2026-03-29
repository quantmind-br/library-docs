---
title: Listagem de Publicação
url: https://developers.olx.com.br/anuncio/api/published_ads_deprecated.html
source: crawler
fetched_at: 2026-02-07T15:17:21.255616585-03:00
rendered_js: false
word_count: 129
summary: This document describes a deprecated API endpoint for retrieving a list of active and processed advertisements associated with an OLX user account.
tags:
    - olx-ads
    - api-endpoint
    - deprecated-api
    - published-ads
    - ad-retrieval
category: api
---

Essa consulta é limitada na quantidade de anúncios retornados da plataforma por usuário e será **descontinuada 17/11/2025**. Por favor atualize a forma de obter os anúncios do cliente [aqui](https://developers.olx.com.br/anuncio/api/published_ads.md).

Esta consulta retorna todos os anúncios que já foram processados e estão ativos, ou seja, disponíveis para visualização em nosso site por qualquer usuário da OLX.

Nosso servidor deve receber a requisição com método do tipo `POST` e com um JSON no corpo da requisição.

Exemplo de chamada para a URL https://apps.olx.com.br/autoupload/published:

```
{
    "access_token":"2cb68a524c25b9a934e9edf4102ef82db5babd77"
}
```

O retorno da chamada trará o identificador usado pelo integrador/anunciante na inserção do anúncio e outro identificador do anúncio na OLX. Caso o anunciante não tenha anúncios ativos, será retornado um array vazio.

ParâmetroValoresDescrição`id`Regular expression: \[A-Za-z0-9\_{}-]{1,19}Identificador do anúncio definido pelo usuário`list_id`integerid do anúncio na OLX

Exemplo de retorno:

```
[
    {
        "id": "original-id-01",
        "list_id": "81262515"
    },
    {
        "id": "original-id-02",
        "list_id": "81262987"
    }
]
```