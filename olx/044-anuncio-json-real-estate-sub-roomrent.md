---
title: Importação de Anúncios via Arquivo JSON
url: https://developers.olx.com.br/anuncio/json/real_estate/sub_roomrent.html
source: crawler
fetched_at: 2026-02-07T15:17:27.229059083-03:00
rendered_js: false
word_count: 135
summary: This document specifies the mandatory parameters and JSON structure required to create or edit listings in the room rental subcategory.
tags:
    - room-rental
    - api-integration
    - category-parameters
    - json-payload
    - listing-management
category: api
---

### Subcategoria `Aluguel de quartos`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `1060`.

Além disso, há parâmetros específicos para esta subcategoria, que devem constar dentro do parâmetro `params` e preenchidos conforme a tabela a seguir:

ParâmetroValorTipoObrigatórioDescrição`room_rent_features``1` para Armário no quarto  
`2` para Banheiro no quarto  
`3` para Mobiliado  
`4` para Ar condicionado  
`5` para Varanda  
`6` para Aquecimento  
`7` para Internet  
`8` para TV a caboarray de stringsNão1Detalhes do quarto

> **Notas**
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).

Aqui está um exemplo de JSON para inserção ou edição de anúncios na subcategoria `Aluguel de quartos`:

```
[
    {
        "id": "5555555555",
        "operation": "insert",
        "category": 1060,
        "subject": "Quarto para Alugar Super Legal",
        "body": "Descrição do anúncio\nNova linha da descrição\nAinda outra linha da descrição",
        "phone": 2155555555,
        "type": "s",
        "price": 1000,
        "zipcode": "24230090",
        "params": {
            "room_rent_features": [
                "1",
                "2"
            ]
        },
        "images": [
            "http://www.a.com/image1.png",
            "http://www.a.com/image2.png"
        ]
    },
    {
        "id": "6666666",
        "operation": "insert",
        "category": 1060,
        "subject": "Quarto para Alugar Super Legal",
        "body": "Descrição do anúncio\nNova linha da descrição\nAinda outra linha da descrição",
        "phone": 2155555555,
        "type": "s",
        "price": 1000,
        "zipcode": "24230090",
        "params": {
            "room_rent_features": [
                "1",
                "2"
            ]
        },
        "images": [
            "http://www.a.com/image1.png",
            "http://www.a.com/image2.png"
        ]
    }
]
```