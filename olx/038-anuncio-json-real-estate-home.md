---
title: JSON para Imóveis na OLX
url: https://developers.olx.com.br/anuncio/json/real_estate/home.html
source: crawler
fetched_at: 2026-02-07T15:17:12.428451441-03:00
rendered_js: false
word_count: 113
summary: This document outlines the requirements and category codes for importing real estate listings into the OLX platform via JSON, providing links to subcategory-specific parameters.
tags:
    - olx-api
    - real-estate
    - json-import
    - data-integration
    - property-listings
    - category-codes
category: reference
---

## Documentação para a Importação via JSON para Imóveis na OLX

Para importação da categoria de Imóveis, é necessário informar a `category`, que será utilizada para que o anúncio esteja disponível na categoria correta. As subcategorias existentes são as seguintes:

`category`Categoria na OLX`1020`Apartamentos`1040`Casas`1060`Aluguel de quartos`1080`Temporada`1100`Terrenos, sítios e fazendas`1120`Comércio e indústria

### Parâmetros específicos por subcategoria

Cada subcategoria de Imóveis tem seu conjunto de parâmetros e valores específicos. Para isso, você deverá considerar os parâmetros específicos para cada subcategoria, bem como os [parâmetros gerais para quaisquer anúncios na OLX](https://developers.olx.com.br/anuncio/api/).

Exemplos de JSONs completos de cada subcategoria estão disponíveis na página de cada subcategoria.

- [Apartamentos](https://developers.olx.com.br/anuncio/json/real_estate/sub_apartment.html)
- [Casas](https://developers.olx.com.br/anuncio/json/real_estate/sub_house.html)
- [Aluguel de quartos](https://developers.olx.com.br/anuncio/json/real_estate/sub_roomrent.html)
- [Temporada](https://developers.olx.com.br/anuncio/json/real_estate/sub_season.html)
- [Terrenos, sítios e fazendas](https://developers.olx.com.br/anuncio/json/real_estate/sub_land.html)
- [Comércio e Indústria](https://developers.olx.com.br/anuncio/json/real_estate/sub_commercial.html)