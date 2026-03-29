---
title: Barcos e aeronaves
url: https://developers.olx.com.br/anuncio/json/autoparts/sub_boat_plane.html
source: crawler
fetched_at: 2026-02-07T15:17:55.915611465-03:00
rendered_js: false
word_count: 183
summary: This document outlines the technical specifications and parameter requirements for listing items in the Boats and Aircraft subcategory of an advertising API.
tags:
    - boats-and-aircraft
    - api-parameters
    - listing-metadata
    - integration-reference
    - vehicle-attributes
category: reference
---

### Subcategoria `Barcos e aeronaves`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `2104`.

Além disso, há parâmetros específicos para esta subcategoria, que devem constar dentro do parâmetro `params` e preenchidos conforme a tabela a seguir:

ParâmetroValorTipoObrigatórioDescrição`carcolor``1` para Preto  
`2` para Branco  
`3` para Prata  
`4` para Vermelho  
`5` para Cinza  
`6` para Azul  
`7` para Amarelo  
`8` para Verde  
`9` para Laranja  
`10` para Outrastringnão1Cor do veículo`parts_name_boats``1` para Motores  
`2` para Inversores  
`3` para Bombas  
`4` para Iluminação  
`5` para Rotores  
`6` para Cabos  
`7` para Velas  
`8` para Sonares e GPS  
`9` para Hélices  
`10` para Âncoras  
`11` para Outrosstringnão1Indica o tipo de peça`condition``1` para Novo  
`2` para UsadoStringsimProduto novo ou de segunda mão`exchange``1` para Sim  
`2` para NãoStringnão1Aceita troca como pagamento

> **Notas**
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).

Aqui está um exemplo de JSON para a subcategoria `Barcos e aeronaves`:

```
[  
   {  
      "subject":"Peça de barco em ótimo estado",
      "body":"Peça de barco do tipo X, usado no caso Y.\nPeça em excelente estado, com características X, Y e Z.",
      "category":2104,
      "id":"BOAT005_ROD1",
      "images":[  
         "http://www.sitedeautos.com/img1.jpg",
         "http://www.sitedeautos.com/img2.jpg"
      ],
      "params":{  
         "carcolor":"1",
         "parts_name_boats":"9",
         "condition":"1",
         "exchange":"2"
      },
      "price":1000,
      "type":"s",
      "zipcode":"20521160"
   },
   {  
      "subject":"Peça de avião em ótimo estado",
      "body":"Peça de avião do tipo X, usado no caso Y.\nPeça em excelente estado, com características X, Y e Z.",
      "category":2104,
      "id":"PLANE005_ROD2",
      "images":[  
         "http://www.sitedeautos.com/img1.jpg",
         "http://www.sitedeautos.com/img2.jpg"
      ],
      "params":{  
         "carcolor":"1",
         "parts_name_boats":"9",
         "condition":"1",
         "exchange":"2"
      },
      "price":1000,
      "type":"s",
      "zipcode":"20521160"
   }
]
```