---
title: Apartamentos
url: https://developers.olx.com.br/anuncio/api/real_estate/sub_apartment.html
source: crawler
fetched_at: 2026-02-07T15:17:48.381192303-03:00
rendered_js: false
word_count: 282
summary: This document defines the technical parameters and data schema required for creating or editing real estate listings in the Apartments subcategory. It specifies mandatory and optional fields, valid values, and payload structures for property details like room count, area, and building features.
tags:
    - real-estate-api
    - ad-insertion
    - json-parameters
    - property-metadata
    - data-specification
category: reference
---

### Subcategoria `Apartamentos`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `1020`.

Além disso, há parâmetros específicos para esta subcategoria, que devem constar dentro do parâmetro `params` e preenchidos conforme a tabela a seguir:

ParâmetroValorTipoObrigatórioDescrição`rooms``0` para 0 quartos  
`1` para 1 quarto  
`2` para 2 quartos  
`3` para 3 quartos  
`4` para 4 quartos  
`5` para 5 ou mais quartos  
stringSimQuantidade de quartos`bathrooms``1` para 1 banheiro  
`2` para 2 banheiros  
`3` para 3 banheiros  
`4` para 4 banheiros  
`5` para 5 ou mais banheiros  
stringNão1Quantidade de banheiros`garage_spaces``0` para 0 vagas  
`1` para 1 vaga  
`2` para 2 vagas  
`3` para 3 vagas  
`4` para 4 vagas  
`5` para 5 ou mais vagas  
stringNão1Quantidade de vagas de garagem`size`string numéricaNão1Área do apartamento (m²)`apartment_type``1` para Padrão  
`2` para Cobertura  
`3` para Duplex/triplex  
`4` para Kitnet  
`5` para LoftstringSimTipo de apartamento`apartment_features``1` para Ar condicionado  
`2` para Academia  
`3` para Armários no quarto  
`4` para Varanda  
`5` para Área de serviço  
`6` para Academia  
`7` para Quarto de serviço  
`8` para Piscina  
`11` para Armários na cozinha  
`12` para Mobiliadoarray de stringsNão1Detalhes do imóvel`apartment_complex_features``1` para Condomínio fechado  
`2` para Elevador  
`3` para Segurança 24h  
`4` para Portaria  
`5` para Permitido animais  
`6` para Academia  
`7` para Piscina  
`8` para Salão de festas  
array de stringsNão1Detalhes do condomínio`iptu`string numéricaNão1Valor mensal do IPTU`condominio`string numéricaNão1Valor mensal do condomínio

> **Notas**
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).

Aqui está um exemplo de JSON para inserção ou edição de anúncios na subcategoria `Apartamentos`:

```
{
    "access_token": "ca18abccaadd282490e75173f98b8ec6f0c1c6c8",
    "ad_list": [
        {
            "id": "5555555555",
            "operation": "insert",
            "category": 1020,
            "subject": "Apartamento à Venda Super Legal",
            "body": "Descrição do anúncio\nNova linha da descrição\nAinda outra linha da descrição",
            "phone": 2155555555,
            "type": "s",
            "price": 1000500,
            "zipcode": "24230090",
            "params": {
                "rooms": "3",
                "bathrooms": "2",
                "garage_spaces": "2",
                "size": "150",
                "iptu": "1000",
                "condominio": "500",
                "apartment_type": "3",
                "apartment_features": [
                    "1",
                    "2"
                ],
                "apartment_complex_features": [
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
            "category": 1020,
            "subject": "Apartamento para Alugar Super Legal",
            "body": "Descrição do anúncio\nNova linha da descrição\nAinda outra linha da descrição",
            "phone": 2155555555,
            "type": "u",
            "price": 1500,
            "zipcode": "24230090",
            "params": {
                "rooms": "3",
                "bathrooms": "2",
                "garage_spaces": "2",
                "size": "150",
                "iptu": "1000",
                "condominio": "500",
                "apartment_type": "3",
                "apartment_features": [
                    "1",
                    "2"
                ],
                "apartment_complex_features": [
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