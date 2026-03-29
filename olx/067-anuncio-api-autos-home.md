---
title: Categoria de Autos
url: https://developers.olx.com.br/anuncio/api/autos/home.html
source: crawler
fetched_at: 2026-02-07T15:17:13.99120076-03:00
rendered_js: false
word_count: 101
summary: This document explains how to correctly categorize and import automobile advertisements on the OLX platform, detailing subcategory codes and specific parameter requirements.
tags:
    - olx-api
    - advertisement-import
    - autos-category
    - vehicle-listings
    - api-documentation
category: guide
---

## Categoria de Autos

Para importação da categoria de Autos, é necessário informar a `category`, que será utilizada para que o anúncio esteja disponível na categoria correta. As subcategorias existentes são as seguintes:

`category`Categoria na OLX`2020`Carros, vans e utilitários`2060`Motos`2050`Ônibus`2040`Caminhões`2080`Barcos e aeronaves

### Parâmetros específicos por subcategoria

Cada subcategoria de Autos tem seu conjunto de parâmetros e valores específicos. Para isso, você deverá considerar os parâmetros específicos para cada subcategoria, bem como os [parâmetros gerais para quaisquer anúncios na OLX](https://developers.olx.com.br/anuncio/api/import.html).

Exemplos de JSONs completos de cada subcategoria estão disponíveis na página de cada subcategoria.

- [Carros, vans e utilitários](https://developers.olx.com.br/anuncio/api/autos/sub_auto.html)
- [Motos](https://developers.olx.com.br/anuncio/api/autos/sub_motorcycle.html)
- [Ônibus](https://developers.olx.com.br/anuncio/api/autos/sub_bus.html)
- [Caminhões](https://developers.olx.com.br/anuncio/api/autos/sub_truck.html)
- [Barcos e aeronaves](https://developers.olx.com.br/anuncio/api/autos/sub_boat_plane.html)