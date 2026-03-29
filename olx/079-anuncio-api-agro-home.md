---
title: Categoria de Agro e Indústria
url: https://developers.olx.com.br/anuncio/api/agro/home.html
source: crawler
fetched_at: 2026-02-07T15:17:14.576031318-03:00
rendered_js: false
word_count: 111
summary: This document provides the specific subcategory IDs and parameter requirements for importing listings into the Agriculture and Industry category on the OLX platform.
tags:
    - olx-api
    - category-mapping
    - agriculture-industry
    - listing-import
    - subcategory-ids
category: reference
---

## Categoria de Agro e Indústria

Para importação da categoria de Agro e Indústria, é necessário informar a `category`, que será utilizada para que o anúncio esteja disponível na categoria correta. As subcategorias existentes são as seguintes:

`category`Categoria na OLX`12020`Tratores e máquinas agrícolas`12040`Peças para tratores e máquinas`12100`Animais para agropecuária`12120`Máquinas pesadas para construção`12140`Máquinas para produção industrial`12160`Outros itens para agro e indústria`12180`Produção Rural

### Parâmetros específicos por subcategoria

As subcategorias de Agro e Indústria, com exceção de `Produção Rural`, não possuem parâmetros específicos. Desta forma, basta respeitar os [parâmetros gerais para quaisquer anúncios na OLX](https://developers.olx.com.br/anuncio/api/import.html).

Para a subcategoria `Produção Rural`, verifique os parâmetros específicos na [página desta subcategoria](https://developers.olx.com.br/anuncio/api/agro/rural_production.html).

Para as demais subcategorias, verifique esta [página](https://developers.olx.com.br/anuncio/api/agro/agro.html).