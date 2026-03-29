---
title: Automóveis
url: https://developers.olx.com.br/anuncio/json/autos.html
source: crawler
fetched_at: 2026-02-07T15:17:52.064230873-03:00
rendered_js: false
word_count: 137
summary: This manual provides technical guidelines and category codes for importing vehicle advertisements into the OLX platform via JSON integration.
tags:
    - olx-integration
    - json-import
    - vehicle-ads
    - category-mapping
    - api-documentation
category: reference
---

## Documentação para a Importação via JSON para Veículos na OLX

Este manual tem como objetivo auxiliar a implantação de importação de anúncios de veículos para as subcategorias `Carros, vans e utilitários`, `Ônibus`, `Caminhões`, `Motos` e `Barcos e aeronaves`, via JSON.

### Subcategorias

Para que o anúncio seja categorizado corretamente na OLX, é preciso que cada anúncio esteja associado à `category` correspondente:

`category`Categoria na OLX`2020`Carros, vans e utilitários`2060`Motos`2050`Ônibus`2040`Caminhões`2080`Barcos e aeronaves

### Parâmetros específicos por subcategoria

Cada subcategoria de Veículos tem seu conjunto de parâmetros e valores específicos. Para isso, você deverá considerar os parâmetros específicos para cada subcategoria, bem como os [parâmetros gerais para quaisquer anúncios na OLX](https://developers.olx.com.br/anuncio/json/home.html).

Exemplos de JSONs completos de cada subcategoria estão disponíveis na página de cada subcategoria.

- [Carros, vans e utilitários](https://developers.olx.com.br/anuncio/json/autos/sub_autos) (Em breve)
- [Motos](https://developers.olx.com.br/anuncio/json/autos/sub_motorcycle) (Em breve)
- [Ônibus](https://developers.olx.com.br/anuncio/json/autos/sub_bus) (Em breve)
- [Caminhões](https://developers.olx.com.br/anuncio/json/autos/sub_truck)
- [Barcos e aeronaves](https://developers.olx.com.br/anuncio/json/autos/sub_boat_plane) (Em breve)