---
title: JSON para Autopeças na OLX
url: https://developers.olx.com.br/anuncio/json/autoparts/home.html
source: crawler
fetched_at: 2026-02-07T15:17:14.251242916-03:00
rendered_js: false
word_count: 129
summary: This document provides technical guidelines and category codes for importing auto parts advertisements into the OLX platform using JSON format.
tags:
    - olx-integration
    - json-import
    - auto-parts
    - category-mapping
    - ad-insertion
category: reference
---

## Documentação para a Importação via JSON para Autopeças na OLX

Este manual tem como objetivo auxiliar a implantação de importação de anúncios de autopeças para as subcategorias `Carros, vans e utilitários`, `Ônibus`, `Caminhões`, `Motos` e `Barcos e aeronaves`, via JSON.

### Subcategorias

Para que o anúncio seja categorizado corretamente na OLX, é preciso que cada anúncio esteja associado à `category` correspondente:

`category`Categoria na OLX`2101`Carros, vans e utilitários`2103`Motos`2105`Ônibus`2102`Caminhões`2104`Barcos e aeronaves

### Parâmetros específicos por subcategoria

Cada subcategoria de Autopeças tem seu conjunto de parâmetros e valores específicos. Para isso, você deverá considerar os parâmetros específicos para cada subcategoria, bem como os [parâmetros gerais para quaisquer anúncios na OLX](https://developers.olx.com.br/anuncio/json/home.html).

Exemplos de JSONs completos de cada subcategoria estão disponíveis na página de cada subcategoria.

- [Carros, vans e utilitários](https://developers.olx.com.br/anuncio/json/autoparts/sub_autos.html)
- [Motos](https://developers.olx.com.br/anuncio/json/autoparts/sub_motorcycle.html)
- [Ônibus](https://developers.olx.com.br/anuncio/json/autoparts/sub_bus.html)
- [Caminhões](https://developers.olx.com.br/anuncio/json/autoparts/sub_truck.html)
- [Barcos e aeronaves](https://developers.olx.com.br/anuncio/json/autoparts/sub_boat_plane.html)