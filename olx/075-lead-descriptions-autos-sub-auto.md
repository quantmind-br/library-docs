---
title: Carros, vans e utilitários
url: https://developers.olx.com.br/lead/descriptions/autos/sub_auto.html
source: crawler
fetched_at: 2026-02-07T15:18:05.345344311-03:00
rendered_js: false
word_count: 441
summary: This document defines the schema and allowed values for the adsInfo object fields specifically for vehicle advertisements on the OLX platform.
tags:
    - olx-api
    - ads-info
    - vehicle-data
    - field-definitions
    - api-reference
    - data-schema
category: reference
---

### Campos de `adsInfo`, subcategoria `Carros, vans e utilitários` (2020)

Descrição dos campos retornados em `adsInfo`.

ParâmetroValorTipoDescrição`subject`stringTítulo do anúncio`body`stringDescrição do anúncio`type``sell` para venda  
`let` para aluguelstringVenda ou aluguel`price`integerPreço do anúncio`zipcode`string numéricaO CEP do anúncio.`regdate`Ano do veículo para os fabricados à partir de 1980 ou  
`1975` para Entre 1975 e 1980  
`1970` para Entre 1970 a 1975  
`1965` para Entre 1965 e 1970  
`1960` para Entre 1960 e 1965  
`1955` para Entre 1955 e 1960  
`1950` para 1950 ou anteriorstringAno do automóvel`mileage`integerQuilometragem do automóvel`gearbox``1` para Manual  
`2` para Automático  
`3` para Semi-AutomáticostringTipo de câmbio`fuel``1` para Gasolina  
`2` para Álcool  
`3` para Flex  
`4` para Gás Natural ![](https://img.shields.io/badge/-deprecated-critical)  
`5` para Diesel  
`6` para Híbrido  
`7` para ElétricostringTipo de combustível`vehicle_brand`stringMarca do automóvel. Para verificar as disponíveis, [use o serviço da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).`vehicle_model`stringModelo da marca do automóvel. Para verificar os disponíveis, [use o serviço da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).`vehicle_version`stringVersão do modelo do automóvel. Para verificar as disponíveis, [use o serviço da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).`vehicle_tag`stringPlaca do Carro`owner_manual``1` para Sim  
`2` para Não  
stringCom manual do Automóvel`dealership_review``1` para Sim  
`2` para Não  
stringCom revisões feitas em concessionária`extra_key``1` para Sim  
`2` para Não  
stringCom chave reserva`gnv_kit``1` para Sim  
`2` para Não  
stringCaso o automóvel possui Kit GNV`warranty``1` para Sim  
`2` para Não  
stringCom garantia`car_features``1` para Ar condicionado  
`2` para Dir. hidráulica ![](https://img.shields.io/badge/-deprecated-critical)  
`3` para Vidro elétrico  
`4` para Trava elétrica  
`5` para Air bag  
`6` para Alarme  
`7` para Som  
`8` para Sensor de ré  
`9` para Câmera de ré  
`10` para Blindadoarray de stringsOpcionais`doors``1` para 2 portas  
`2` para 4 portasstringNúmero de portas`end_tag``1` para 0  
`2` para 1  
`3` para 2  
`4` para 3  
`5` para 4  
`6` para 5  
`7` para 6  
`8` para 7  
`9` para 8  
`10` para 9stringNúmero final da placa do automóvel`car_steering``1` para Hidráulica  
`2` para Elétrica  
`3` para Mecânica  
`4` para AssistidastringDireção`motorpower``1` para 1  
`2` para 1.2  
`3` para 1.3  
`4` para 1.4  
`5` para 1.5  
`6` para 1.6  
`7` para 1.7  
`8` para 1.8  
`9` para 1.9  
`10` para 2.0 - 2.9  
`11` para 3.0 - 3.9  
`12` para 4.0 ou maisstringPotência do motor`cartype``1` para Passeio ![](https://img.shields.io/badge/-deprecated-critical)  
`2` para Conversível  
`3` para Pick-up  
`4` para Antigo ![](https://img.shields.io/badge/-deprecated-critical)  
`5` para SUV  
`6` para Buggy  
`7` para Van/Utilitário  
`8` para Sedã  
`9` para HatchstringTipo de automóvel`carcolor``1` para Preto  
`2` para Branco  
`3` para Prata  
`4` para Vermelho  
`5` para Cinza  
`6` para Azul  
`7` para Amarelo  
`8` para Verde  
`9` para Laranja  
`10` para OutrastringCor do automóvel`exchange``1` para Sim  
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
    "subject": "VOLKSWAGEN T-CROSS 1.4 TSI HIGHLINE AUTOMÁTICO",
    "body": "Bancos de couro, Computador de bordo, Desembaçador traseiro, Farol de neblina, Freio ABS,Limpador traseiro, Retrovisores elétricos, Rodas de liga leve, Sensor de chuva, Volante com Regulagem de Altura, Entrada USB, Direção Elétrica, Garantia de Fábrica.",
    "type": "sell",
    "price": "181990",
    "zipcode": "25964000",
    "regdate": "2022",
    "gearbox": "2",
    "financial": "2|3|4",
    "financial_status": "1",
    "fuel": "3",
    "doors": "2",
    "mileage": "0",
    "end_tag": "0",
    "motorpower": "4",
    "car_steering": "1",
    "carcolor": "4",
    "car_features": "5|6|1|7|8|4|3",
    "vehicle_brand": "75",
    "vehicle_model": "37",
    "vehicle_tag": "AAA1A10"
  },
  "createdAt": "2019-02-12T14:30:00.500Z"
}
```