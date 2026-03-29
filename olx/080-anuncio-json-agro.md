---
title: Agro e Indústria
url: https://developers.olx.com.br/anuncio/json/agro.html
source: crawler
fetched_at: 2026-02-07T15:17:51.012777235-03:00
rendered_js: false
word_count: 161
summary: This document provides technical instructions and category codes for importing advertisements into the Agro and Industry sections of OLX using JSON format.
tags:
    - olx-api
    - json-import
    - agro-industry
    - ad-integration
    - category-codes
category: reference
---

## Documentação para a Importação via JSON para a categoria `Agro e Indústria` na OLX

Este manual tem como objetivo auxiliar a implantação de importação de anúncios de Agro e Indústria para as subcategorias `Tratores e máquinas agrícolas`, `Máquinas pesadas para construção`, `Máquinas para produção industrial`, `Peças para tratores e máquinas`, `Animais para agropecuária`, `Produção Rural` e `Outros itens para agro e indústria`, via JSON.

### Subcategorias

Para que o anúncio seja categorizado corretamente na OLX, é preciso que cada anúncio esteja associado à `category` correspondente:

`category`Categoria na OLX`12020`Tratores e máquinas agrícolas`12120`Máquinas pesadas para construção`12140`Máquinas para produção industrial`12040`Peças para tratores e máquinas`12100`Animais para agropecuária`12180`[Produção Rural](https://developers.olx.com.br/anuncio/json/agro/rural_production.html)`12160`Outros itens para agro e indústria

### Parâmetros específicos por subcategoria

As subcategorias Agro e Indústria, com exceção de `Produção Rural`, não possuem parâmetros específicos. Desta forma, basta respeitar os [parâmetros gerais para quaisquer anúncios na OLX](https://developers.olx.com.br/anuncio/json/home.html).

Para a subcategoria `Produção Rural`, verifique os parâmetros específicos na [página desta subcategoria](https://developers.olx.com.br/anuncio/json/agro/rural_production.html).

### Exemplo de JSON para a subcategoria `Tratores e máquinas agrícolas`

```
[  
   {  
      "subject":"Trator em bom estado",
      "body":"Trator excelente, quase não foi usado.\nTem com características X, Y e Z.",
      "category":12020,
      "id":"AGRO01",
      "images":[  
         "http://www.sitedeagro.com/img1.jpg",
         "http://www.sitedeagro.com/img2.jpg"
      ],
      "price":1000,
      "type":"s",
      "zipcode":"20521160"
   },
   {  
      "subject":"Trator excelente",
      "body":"Escavadeira excelente, com característica X, usado no caso Y.\nPeça em excelente estado, com características X, Y e Z.",
      "category":12120,
      "id":"AGRO02",
      "images":[  
         "http://www.sitedeagro.com/img3.jpg",
         "http://www.sitedeagro.com/img4.jpg"
      ],
      "price":1000,
      "type":"s",
      "zipcode":"20521160"
   }
]
```