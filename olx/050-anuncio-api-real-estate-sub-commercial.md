---
title: Comércio e indústria
url: https://developers.olx.com.br/anuncio/api/real_estate/sub_commercial.html
source: crawler
fetched_at: 2026-02-07T15:17:48.545355566-03:00
rendered_js: false
word_count: 192
summary: This document specifies the mandatory parameters and configuration requirements for listing or editing advertisements within the Commerce and Industry subcategory.
tags:
    - api-integration
    - property-listings
    - parameter-specification
    - json-payload
    - real-estate-api
category: reference
---

### Subcategoria `Comércio e indústria`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `1120`.

Além disso, há parâmetros específicos para esta subcategoria, que devem constar dentro do parâmetro `params` e preenchidos conforme a tabela a seguir:

ParâmetroValorTipoObrigatórioDescrição`garage_spaces``0` para 0 vagas  
`1` para 1 vaga  
`2` para 2 vagas  
`3` para 3 vagas  
`4` para 4 vagas  
`5` para 5 ou mais vagas  
stringNão1Quantidade de vagas de garagem`size`string numéricaNão1Área do imóvel (m²)`commercial_type``1` para Escritório  
`2` para Galpão/Depósito  
`3` para Hotel  
`4` para Fábrica  
`5` para Garagem/Vaga  
`6` para Loja  
`7` para OutrosstringNão1Tipo de imóvel comercial`commercial_features``1` para Garagem  
`2` para Segurança 24h  
`3` para Câmeras de segurança  
`4` para Elevador  
`5` para Portaria  
`6` para Acesso para deficientesarray de stringsNão1Detalhes do imóvel`iptu`string numéricaNão1Valor mensal do IPTU`condominio`string numéricaNão1Valor mensal do condomínio

> **Notas**
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).

Aqui está um exemplo de JSON para inserção ou edição de anúncios na subcategoria `Comércio e indústria`:

```
{
    "access_token": "ca18abccaadd282490e75173f98b8ec6f0c1c6c8",
    "ad_list": [
        {
            "id": "5555555555",
            "operation": "insert",
            "category": 1120,
            "subject": "Galpão à Venda Super Legal",
            "body": "Descrição do anúncio\nNova linha da descrição\nAinda outra linha da descrição",
            "phone": 2155555555,
            "type": "s",
            "price": 1000500,
            "zipcode": "24230090",
            "params": {
                "garage_spaces": "2",
                "size": "150",
                "iptu": "1000",
                "condominio": "500",
                "commercial_type": "2",
                "commercial_features": [
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
           "id": "666666666",
            "operation": "insert",
            "category": 1120,
            "subject": "Escritório à Venda Super Legal",
            "body": "Descrição do anúncio\nNova linha da descrição\nAinda outra linha da descrição",
            "phone": 2155555555,
            "type": "s",
            "price": 1000500,
            "zipcode": "24230090",
            "params": {
                "garage_spaces": "1",
                "size": "150",
                "iptu": "1000",
                "condominio": "500",
                "commercial_type": "2",
                "commercial_features": [
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
}
```