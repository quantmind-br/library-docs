---
title: Listagem de Marcas e Modelos de Celulares e Smartphones na OLX
url: https://developers.olx.com.br/anuncio/api/electronics/cellphone_models.html
source: crawler
fetched_at: 2026-02-07T15:18:32.573495564-03:00
rendered_js: false
word_count: 133
summary: This document outlines the API endpoints and request formats for retrieving lists of mobile phone brands and models available on the OLX platform.
tags:
    - olx-api
    - mobile-phones
    - smartphones
    - api-documentation
    - brand-models
    - json-api
category: api
---

## Listagem de Marcas e Modelos de Celulares e Smartphones na OLX

Os endpoints disponíveis para consultar detalhes de marcas e modelos para Celulares e Smartphones na OLX são os seguintes:

SubcategoriaDescriçãoEndpointCelulares e SmartphonesMarcas de celulares e smartphones disponíveishttps://apps.olx.com.br/autoupload/cellphone\_infoCelulares e SmartphonesModelos de celulares e smartphones de uma determinada marcahttps://apps.olx.com.br/autoupload/cellphone\_info/{id\_marca}

Nosso servidor deve receber a requisição com método do tipo `POST`, sendo que o formato do arquivo a ser enviado para nosso servidor deverá ser do tipo JSON.

## Celulares e Smartphones

### Marcas de Celulares e Smartphones Disponíveis

Exemplo de chamada: `POST` https://apps.olx.com.br/autoupload/cellphone\_info:

Utilizando o cURL:

```
$ curl -A Mozila -L -X POST 'https://apps.olx.com.br/autoupload/cellphone_info' -H 'Content-Type: application/json' --data-raw '{
    "access_token": "token"
}'
```

Utilizando postman/insomnia:

```
{
    "access_token":"token"
}
```

Exemplo de retorno:

```
{
    "data": {
        "APPLE": 2,
        "SAMSUNG": 3,
        "XIAOMI": 4,
        "MOTOROLA": 5,
        "LENOVO": 6,
        "LG": 7,
        "ASUS": 8,
        "SONY": 9,
        "HUAWEI": 10,
        "INFINIX": 11
    },
    "status": "ok"
}
```

### Modelos de Celulares e Smartphones de Determinada Marca

Exemplo de chamada: `POST` https://apps.olx.com.br/autoupload/cellphone\_info/2 (no caso, o id `2` é a marca `APPLE`, conforme visto no exemplo acima):

Utilizando o cURL:

```
$ curl -A Mozila -L -X POST 'https://apps.olx.com.br/autoupload/cellphone_info/2' -H 'Content-Type: application/json' --data-raw '{
    "access_token": "token"
}'
```

Utilizando postman/insomnia:

```
{
    "access_token": "token"
}
```

Exemplo de retorno:

```
{
    "data": {
        "IPHONE 11": 1,
        "IPHONE 11 PRO": 2,
        "IPHONE 11 PRO MAX": 3,
        "IPHONE 12": 4,
        "IPHONE 12 MINI": 5,
        "IPHONE 12 PRO": 6,
        "IPHONE 12 PRO MAX": 7,
        "IPHONE 13": 8,
        "IPHONE 13 MINI": 9,
        "IPHONE 13 PRO": 10,
        "IPHONE 13 PRO MAX": 11,
        "IPHONE 6": 12,
        "IPHONE 6 PLUS": 13,
        "IPHONE 6S": 14,
        "IPHONE 6S PLUS": 15,
        "IPHONE 7": 16,
        "IPHONE 7 PLUS": 17,
        "IPHONE 8": 18,
        "IPHONE 8 PLUS": 19,
        "IPHONE SE 2020": 20,
        "IPHONE X": 21,
        "IPHONE XR": 22,
        "IPHONE XS": 23,
        "IPHONE XS MAX": 24,
        "OUTROS": 25,
        "IPHONE 14": 26,
        "IPHONE 14 PLUS": 27,
        "IPHONE 14 PRO": 28,
        "IPHONE 14 PRO MAX": 29,
        "IPHONE 15": 30,
        "IPHONE 15 PLUS": 31,
        "IPHONE 15 PRO": 32,
        "IPHONE 15 PRO MAX": 33,
        "IPHONE SE 2022": 34
    },
    "status": "ok"
}
```