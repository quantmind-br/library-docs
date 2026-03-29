---
title: Leads com informações detalhadas do anúncio
url: https://developers.olx.com.br/lead/leads_enriched.html
source: crawler
fetched_at: 2026-02-07T15:17:30.311341485-03:00
rendered_js: false
word_count: 80
summary: This document explains the integration of lead data with an additional 'adsInfo' structure that provides detailed advertisement metadata for automotive categories.
tags:
    - lead-integration
    - ads-info
    - api-payload
    - autos-category
    - olx-integration
    - webhook-data
category: api
---

Para facilitar a pesquisa dos anúncios com integração de Leads, disponibilizamos para os integradores, o Lead com informações detalhadas do anúncio. Este possui as mesmas regras de [Envio de Leads](https://developers.olx.com.br/lead/leads.html), porém, no corpo dos dados, adicionamos a estrutura `adsInfo` contendo detalhes do anúncio. Esta nova característica está disponível apenas para algumas categorias.

CategoriaSubcategoriaCódigo da CategoriaAutos[Carros, vans e utilitários](https://developers.olx.com.br/lead/descriptions/autos/sub_auto.html)`2020`Autos[Motos](https://developers.olx.com.br/lead/descriptions/autos/sub_motorcycle.html)`2060`Autos[Caminhões](https://developers.olx.com.br/lead/descriptions/autos/sub_truck.html)`2040`

> Para mais detalhes sobre os campos retornados de adsInfo, navegue na subcategorias acima

Segue exemplo de um JSON para um lead enviado:

```
{
  "source": "financing",
  "adId": "a1234",
  "listId": "12345689",
  "linkAd": "https://www.olx.com.br/vi/12345689",
  "name": "Nome do cliente",
  "email": "email.docliente@gmail.com",
  "phone": "2199999999",
  "message": "Olá, gostaria de saber mais informações sobre o anúncio a1234", 
  "createdAt": "2019-02-12T14:30:00.500Z",
  "adsInfo": {
    "category": 2020,
    "subject": "Harley Davidson",
    "body": "Harley Davidson fat boy carburada, frente cabeça de touro",
    "type": "sell",
    "price": "90000",
    "zipcode": "25964000",
    "regdate": "90000",
    "mileage": "43000",
    "carcolor": "1",
    "fuel": "1",
    "car_steering": "1",
    "exchange": "1",
    "owner": "1",
    "financial": "2|3|4",
    "financial_status": "1",
    "vehicle_brand": "28",
    "vehicle_model": "7",
    "vehicle_version": "2",
    "cubiccms": "21",
    "moto_features": "1|2|3|4|5|6|7|8|9"
  },
  "externalId": "123jdanjkdna-danjndaada"
}
```