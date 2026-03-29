---
title: Motos
url: https://developers.olx.com.br/anuncio/json/autoparts/sub_motorcycle.html
source: crawler
fetched_at: 2026-02-07T15:17:54.308470196-03:00
rendered_js: false
word_count: 184
summary: This document outlines the required parameters and valid value mappings for listing motorcycle parts and accessories using the specific category ID 2103.
tags:
    - api-reference
    - motorcycle-category
    - data-specification
    - json-payload
    - listing-configuration
    - parameter-mapping
category: reference
---

### Subcategoria `Motos`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `2103`.

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
`10` para Outrastringnão1Cor do carro`parts_name_motos``1` para Pneus  
`2` para Rodas  
`3` para Calotas  
`4` para Capacetes  
`5` para Acabamento  
`6` para Roupas de moto  
`7` para Bagageiros, baús e mochilas  
`8` para Suportes  
`9` para Alarmes  
`10` para Peças de motos  
`11` para Outrosstringnão1Indica o tipo de peça`condition``1` para Novo  
`2` para UsadoStringsimProduto novo ou de segunda mão`exchange``1` para Sim  
`2` para NãoStringnão1Aceita troca como pagamento

> **Notas**
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).

Aqui está um exemplo de JSON para a subcategoria `Motos`:

```
[  
   {  
      "subject":"Peça de moto em ótimo estado",
      "body":"Peça de moto do tipo X, usado no caso Y.\nPeça em excelente estado, com características X, Y e Z.",
      "category":2103,
      "id":"MOTO005_ROD1",
      "images":[  
         "http://www.sitedeautos.com/img1.jpg",
         "http://www.sitedeautos.com/img2.jpg"
      ],
      "params":{  
         "carcolor":"1",
         "parts_name_motos":"9",
         "condition":"1",
         "exchange":"2"
      },
      "price":1000,
      "type":"s",
      "zipcode":"20521160"
   },
   {  
      "subject":"Peça de moto em ótimo estado",
      "body":"Peça de moto do tipo X, usado no caso Y.\nPeça em excelente estado, com características X, Y e Z.",
      "category":2103,
      "id":"MOTO005_ROD2",
      "images":[  
         "http://www.sitedeautos.com/img1.jpg",
         "http://www.sitedeautos.com/img2.jpg"
      ],
      "params":{  
         "carcolor":"1",
         "parts_name_motos":"9",
         "condition":"1",
         "exchange":"2"
      },
      "price":1000,
      "type":"s",
      "zipcode":"20521160"
   }
]
```