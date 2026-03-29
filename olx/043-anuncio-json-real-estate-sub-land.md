---
title: Importação de Anúncios via Arquivo JSON
url: https://developers.olx.com.br/anuncio/json/real_estate/sub_land.html
source: crawler
fetched_at: 2026-02-07T15:17:28.042477025-03:00
rendered_js: false
word_count: 173
summary: This document outlines the specific parameters and data formatting required for posting or editing listings in the land and farm real estate subcategory via API.
tags:
    - api-integration
    - real-estate-data
    - data-parameters
    - json-payload
    - listing-management
category: api
---

### Subcategoria `Terrenos, sítios e fazendas`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `1100`.

Além disso, há parâmetros específicos para esta subcategoria, que devem constar dentro do parâmetro `params` e preenchidos conforme a tabela a seguir:

ParâmetroValorTipoObrigatórioDescrição`size`string numéricaNão1Área do imóvel (m²)`re_land_type``1` para Terrenos e lotes  
`2` para Sítios e chácaras  
`3` para Fazendas  
`4` para OutrosstringSimTipo de imóvel`re_land_features``1` para Área verde  
`2` para Casa sede  
`3` para Pomar  
`4` para Piscina  
`5` para Churrasqueira  
`6` para Poço artesiano  
`7` para Água encanada  
`8` para Energia elétrica  
`9` para Campo de futebol  
`10` para Acesso asfaltadoarray de stringsNão1Detalhes do imóvel`iptu`string numéricaNão1Valor mensal do IPTU`condominio`string numéricaNão1Valor mensal do condomínio

> **Notas**
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).

Aqui está um exemplo de JSON para inserção ou edição de anúncios na subcategoria `Terrenos, sítios e fazendas`:

```
[
    {
        "id": "5555555555",
        "operation": "insert",
        "category": 1100,
        "subject": "Terreno à Venda Super Legal",
        "body": "Descrição do anúncio\nNova linha da descrição\nAinda outra linha da descrição",
        "phone": 2155555555,
        "type": "s",
        "price": 1000500,
        "zipcode": "24230090",
        "params": {
            "size": "150",
            "iptu": 1000,
            "condominio": 500,
            "re_land_type": "2",
            "re_land_features": [
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
        "id": "66666666",
        "operation": "insert",
        "category": 1100,
        "subject": "Terreno à Venda Super Legal",
        "body": "Descrição do anúncio\nNova linha da descrição\nAinda outra linha da descrição",
        "phone": 2155555555,
        "type": "s",
        "price": 1000500,
        "zipcode": "24230090",
        "params": {
            "size": "150",
            "iptu": 1000,
            "condominio": 500,
            "re_land_type": "2",
            "re_land_features": [
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