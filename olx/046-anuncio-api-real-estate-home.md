---
title: Categoria de Imóveis
url: https://developers.olx.com.br/anuncio/api/real_estate/home.html
source: crawler
fetched_at: 2026-02-07T15:17:12.424084501-03:00
rendered_js: false
word_count: 106
summary: This document provides the specific category codes and documentation links required for importing real estate listings via the OLX API.
tags:
    - olx-api
    - real-estate
    - listing-import
    - category-codes
    - integration-reference
category: reference
---

## Categoria de Imóveis

Para importação da categoria de Imóveis, é necessário informar a `category`, que será utilizada para que o anúncio esteja disponível na categoria correta. As subcategorias existentes são as seguintes:

`category`Categoria na OLX`1020`Apartamentos`1040`Casas`1060`Aluguel de quartos`1080`Temporada`1100`Terrenos, sítios e fazendas`1120`Comércio e indústria

### Parâmetros específicos por subcategoria

Cada subcategoria de Imóveis tem seu conjunto de parâmetros e valores específicos. Para isso, você deverá considerar os parâmetros específicos para cada subcategoria, bem como os [parâmetros gerais para quaisquer anúncios na OLX](https://developers.olx.com.br/anuncio/api/import.html).

Exemplos de JSONs completos de cada subcategoria estão disponíveis na página de cada subcategoria.

- [Apartamentos](https://developers.olx.com.br/anuncio/api/real_estate/sub_apartment.html)
- [Casas](https://developers.olx.com.br/anuncio/api/real_estate/sub_house.html)
- [Aluguel de quartos](https://developers.olx.com.br/anuncio/api/real_estate/sub_roomrent.html)
- [Temporada](https://developers.olx.com.br/anuncio/api/real_estate/sub_season.html)
- [Terrenos, sítios e fazendas](https://developers.olx.com.br/anuncio/api/real_estate/sub_land.html)
- [Comércio e Indústria](https://developers.olx.com.br/anuncio/api/real_estate/sub_commercial.html)