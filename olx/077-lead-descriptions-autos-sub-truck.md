---
title: Caminhões
url: https://developers.olx.com.br/lead/descriptions/autos/sub_truck.html
source: crawler
fetched_at: 2026-02-07T15:18:05.725423338-03:00
rendered_js: false
word_count: 227
summary: This document specifies the schema and value mappings for the adsInfo field within the trucks subcategory, detailing parameters for vehicle advertisements.
tags:
    - api-reference
    - truck-listings
    - metadata-fields
    - data-specification
    - lead-integration
category: reference
---

### Campos de `adsInfo`, subcategoria `Caminhões` (2040)

Descrição dos campos retornados em `adsInfo`.

ParâmetroValorTipoDescrição`subject`stringTítulo do anúncio`body`stringDescrição do anúncio`type``sell` para venda  
`let` para aluguelstringVenda ou aluguel`price`integerPreço do anúncio`zipcode`string numéricaO CEP do anúncio.`regdate`Ano do veículo para os fabricados à partir de 1980  
ou  
`1975` para Entre 1975 e 1980  
`1970` para Entre 1970 a 1975  
`1965` para Entre 1965 e 1970  
`1960` para Entre 1960 e 1965  
`1955` para Entre 1955 e 1960  
`1950` para 1950 ou anteriorstringAno de caminhão`mileage`integerQuilometragem do caminhão`gearbox``1` para Manual  
`2` para Automático  
`3` para Semi-AutomáticostringTipo de câmbio`car_steering``1` para Hidráulica  
`2` para Elétrica  
`3` para Mecânica  
`4` para AssistidastringDireção`fuel``1` para Gasolina  
`2` para Álcool  
`3` para Flex  
`4` para Gás Natural  
`5` para Diesel  
`6` para Híbrido  
`7` para ElétricostringTipo de combustível`trucktype``1` para Caçamba  
`2` para No chassi  
`3` para Baú  
`4` para Carroceria  
`5` para Graneleiro  
`6` para Plataforma  
`7` para Munck  
`8` para Pipa  
`9` para Boladeiro  
`10` para Carga seca  
`11` para Guindaste  
`12` para OutrostringTipo de caminhão`truck_features``1` para Ar condicionado  
`2` para Vidro elétrico  
`3` para Trava elétrica  
`4` para Blindado  
`5` para ABSarray de stringsOpcionais`exchange``1` para Sim  
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
    "subject": "Volvo Fh 440 6x2 2011",
    "body": "Volvo Fh 440 6x2 2011\n\nCaminhão ano 2011 muito bem conservado, veiculo completo.",
    "type": "sell",
    "price": "181700",
    "zipcode": "25964000",
    "regdate": "2011",
    "gearbox": "2",
    "fuel": "5",
    "mileage": "541000",
    "car_steering": "1",
    "exchange": "4",
    "owner": "1",
    "financial": "2|3|4",
    "financial_status": "1",
    "trucktype": "2",
    "truck_features": "1|2|3|5"
  },
  "createdAt": "2019-02-12T14:30:00.500Z"
}
```