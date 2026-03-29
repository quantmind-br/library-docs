---
title: Motos
url: https://developers.olx.com.br/lead/descriptions/autos/sub_motorcycle.html
source: crawler
fetched_at: 2026-02-07T15:18:05.631766018-03:00
rendered_js: false
word_count: 326
summary: This document defines the schema and valid values for the adsInfo object when processing motorcycle advertisements. It details technical specifications, categorization values, and financial attributes required for the Motos subcategory.
tags:
    - olx-api
    - motorcycle-listings
    - api-reference
    - adsinfo-schema
    - data-types
category: reference
---

### Campos de `adsInfo`, subcategoria `Motos` (2060)

Descrição dos campos retornados em `adsInfo`.

ParâmetroValorTipoDescrição`subject`stringTítulo do anúncio`body`stringDescrição do anúncio`type``sell` para venda  
`let` para aluguelstringVenda ou aluguel`price`integerPreço do anúncio`zipcode`string numéricaO CEP do anúncio.`regdate`Ano do veículo para os fabricados à partir de 1980 ou  
`1975` para Entre 1975 e 1980  
`1970` para Entre 1970 a 1975  
`1965` para Entre 1965 e 1970  
`1960` para Entre 1960 e 1965  
`1955` para Entre 1955 e 1960  
`1950` para 1950 ou anteriorstringAno da moto`mileage`integerQuilometragem da moto`gearbox``1` para Manual  
`2` para Automático  
`3` para Semi-AutomáticostringTipo de câmbio`fuel``1` para Gasolina  
`2` para Álcool  
`3` para Flex  
`4` para Gás Natural  
`5` para Diesel  
`6` para Híbrido  
`7` para ElétricostringTipo de combustível`vehicle_brand`stringMarca da moto. Para verificar as disponíveis, [use o serviço da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).`vehicle_model`stringModelo da marca da moto. Para verificar os disponíveis, [use o serviço da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).`vehicle_version`stringVersão do modelo da moto. Para verificar as disponíveis, [use o serviço da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).`cubiccms`stringCilindradas da moto. Para verificar as disponíveis, [use o serviço da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).`moto_features``1` para ABS  
`2` para Computador de bordo  
`3` para Escapamento esportivo  
`4` para Bolsa / Baú / Bauleto  
`5` para Contra peso no guidon  
`6` para Alarme  
`7` para Amortecedor de direção  
`8` para Faróis de Neblina  
`9` para GPS  
`10` para Somarray de stringsOpcionais`mototype``1` para Street  
`2` para Esportiva  
`3` para Custom  
`4` para Trail  
`5` para Naked  
`6` para Scooter  
`7` para Offroad  
`8` para Touring  
`9` para Utilitária  
`10` para Supermotard  
`11` para Triciclo  
`12` para Quadriciclo  
`13` para Trial  
`14` para Mini crossstringTipo da moto`carcolor``1` para Preto  
`2` para Branco  
`3` para Prata  
`4` para Vermelho  
`5` para Cinza  
`6` para Azul  
`7` para Amarelo  
`8` para Verde  
`9` para Laranja  
`10` para OutrastringCor da moto`exchange``1` para Sim  
`2` para NãostringAceita trocas pelo produto`financial``1` para Financiado ![](https://img.shields.io/badge/-deprecated-critical)  
`2` para IPVA Pago  
`3` para Com multas  
`4` para De leilãoarray de stringsEstado financeiro`financial_status``1` para Quitado  
`2` para FinanciadostringEstado financeiro`owner``1` para Sim  
`2` para NãostringÚnico dono

Segue exemplo de um JSON para um lead enviado:

```
{
  "source": "OLX",
  "adId": "a1234",
  "listId": "12345689",
  "name": "Nome do cliente",
  "email": "email.docliente@gmail.com",
  "phone": "2199999999",
  "message": "Olá, gostaria de saber mais informações sobre o anúncio a1234", 
  "adsInfo": {
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
  "createdAt": "2019-02-12T14:30:00.500Z"
}
```