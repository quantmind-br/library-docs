---
title: Categoria de Autopeças
url: https://developers.olx.com.br/anuncio/api/autoparts/home.html
source: crawler
fetched_at: 2026-02-07T15:17:13.784772706-03:00
rendered_js: false
word_count: 101
summary: This document outlines the category IDs and subcategory parameters required for importing listings into the Auto Parts section of the OLX platform.
tags:
    - auto-parts
    - category-mapping
    - olx-api
    - listing-import
    - vehicle-subcategories
category: reference
---

## Categoria de Autopeças

Para importação da categoria de Autopeças, é necessário informar a `category`, que será utilizada para que o anúncio esteja disponível na categoria correta. As subcategorias existentes são as seguintes:

`category`Categoria na OLX`2101`Carros, vans e utilitários`2103`Motos`2105`Ônibus`2102`Caminhões`2104`Barcos e aeronaves

### Parâmetros específicos por subcategoria

Cada subcategoria de Autopeças tem seu conjunto de parâmetros e valores específicos. Para isso, você deverá considerar os parâmetros específicos para cada subcategoria, bem como os [parâmetros gerais para quaisquer anúncios na OLX](https://developers.olx.com.br/anuncio/api/import.html).

Exemplos de JSONs completos de cada subcategoria estão disponíveis na página de cada subcategoria.

- [Carros, vans e utilitários](https://developers.olx.com.br/anuncio/api/autoparts/sub_autos.html)
- [Motos](https://developers.olx.com.br/anuncio/api/autoparts/sub_motorcycle.html)
- [Ônibus](https://developers.olx.com.br/anuncio/api/autoparts/sub_bus.html)
- [Caminhões](https://developers.olx.com.br/anuncio/api/autoparts/sub_truck.html)
- [Barcos e aeronaves](https://developers.olx.com.br/anuncio/api/autoparts/sub_boat_plane.html)