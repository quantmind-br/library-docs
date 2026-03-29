---
title: Subcategoria Caminhões
url: https://developers.olx.com.br/anuncio/api/autos/sub_truck.html
source: crawler
fetched_at: 2026-02-07T15:17:33.746612233-03:00
rendered_js: false
word_count: 471
summary: This document defines the technical parameters and mandatory values required for creating or editing truck advertisements via API.
tags:
    - api-integration
    - truck-category
    - ad-listing
    - parameter-specification
    - data-mapping
    - payload-configuration
category: reference
---

### Subcategoria `Caminhões`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `2040`.

Além disso, há parâmetros específicos para esta subcategoria, que devem constar dentro do parâmetro `params` e preenchidos conforme a tabela a seguir:

ParâmetroValorTipoObrigatórioDescrição`regdate``2025` para 2025  
`2024` para 2024  
`2023` para 2023  
`2022` para 2022  
`2021` para 2021  
`2020` para 2020  
`2019` para 2019  
`2018` para 2018  
`2017` para 2017  
`2016` para 2016  
`2015` para 2015  
`2014` para 2014  
`2013` para 2013  
`2012` para 2012  
`2011` para 2011  
`2010` para 2010  
`2009` para 2009  
`2008` para 2008  
`2007` para 2007  
`2006` para 2006  
`2005` para 2005  
`2004` para 2004  
`2003` para 2003  
`2002` para 2002  
`2001` para 2001  
`2000` para 2000  
`1999` para 1999  
`1998` para 1998  
`1997` para 1997  
`1996` para 1996  
`1995` para 1995  
`1994` para 1994  
`1993` para 1993  
`1992` para 1992  
`1991` para 1991  
`1990` para 1990  
`1989` para 1989  
`1988` para 1988  
`1987` para 1987  
`1986` para 1986  
`1985` para 1985  
`1984` para 1984  
`1983` para 1983  
`1982` para 1982  
`1981` para 1981  
`1980` para 1980  
`1975` para Entre 1975 e 1980  
`1970` para Entre 1970 a 1975  
`1965` para Entre 1965 e 1970  
`1960` para Entre 1960 e 1965  
`1955` para Entre 1955 e 1960  
`1950` para 1950 ou anteriorstringSimAno do caminhão`mileage`integerSimQuilometragem do caminhão`gearbox``1` para Manual  
`2` para Automático  
`3` para Semi-AutomáticostringNão1 `4` para Automatizado  
Tipo de câmbio`fuel``1` para Gasolina  
`2` para Álcool  
`3` para Flex  
`4` para Gás Natural  
`5` para Diesel  
`6` para Híbrido  
`7` para ElétricostringNão1Tipo de combustível`trucktype``1` para Caçamba  
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
`12` para OutrostringNão1Tipo de caminhão`truck_features``1` para Ar condicionado  
`2` para Vidro elétrico  
`3` para Trava elétrica  
`4` para Blindado  
`5` para ABSarray de stringsNão1Opcionais`exchange``1` para Sim  
`2` para NãostringNão1Aceita trocas pelo produto`financial``1` para Financiado2 ![](https://img.shields.io/badge/-deprecated-critical)  
`2` para IPVA Pago  
`3` para Com multas  
`4` para De leilãoarray de strings2.1Não1Estado financeiro`financial_status``1` para Quitado  
`2` para Financiado2stringNão1Estado financeiro`owner``1` para Sim  
`2` para NãostringNão1Único dono`car_steering``1` para Hidráulica3  
`2` para Elétrica  
`3` para Mecânica  
`5` para Eletro-hidráulicastringNão1Direção

> **Notas**
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).
> 
> 2 Em breve, não aceitaremos mais o valor `1 - para Financiado` no parâmetro `financial`. Em vez disso, você deverá utilizar o parâmetro `financial_status` para informar se o estado financeiro é quitado ou financiado.  
> 2.1 Além disso, o parâmetro financial passará a receber um array de strings, permitindo que você informe mais de um valor.

Aqui está um exemplo de JSON para inserção ou edição de anúncios na subcategoria `Caminhões`:

```
{
    "access_token": "ca18abccaadd282490e75173f98b8ec6f0c1c6c8",
    "ad_list": [
        {
            "id": "5555555555",
            "operation": "insert",
            "category": 2040,
            "subject": "Caminhão Novo",
            "body": "Caminhão legal, super bom, com características X, Y e Z.\nEntre em contato e vamos fazer negócio.",
            "phone": 2155555555,
            "type": "s",
            "price": 10500,
            "zipcode": "24230090",
            "params": {
                "regdate": "1988",
                "gearbox": "1",
                "financial": [
                    "2",
                    "3"
                ],
                "financial_status": "1",
                "fuel": "1",
                "trucktype": "2",
                "mileage": 10000,
                "carcolor": "1",
                "truck_features": [
                    "1",
                    "2"
                ]
            },
            "images": [
                "http://www.a.com/image1.png",
                "http://www.a.com/image2.png"
            ]
        },
        {
            "id": "666666666",
            "operation": "insert",
            "category": 2040,
            "subject": "Caminhão Novo 2",
            "body": "Caminhão legal, super bom, com características X, Y e Z.\nEntre em contato e vamos fazer negócio.",
            "phone": 2155555544,
            "type": "s",
            "price": 12500,
            "zipcode": "24234590",
            "params": {
                "regdate": "2001",
                "gearbox": "2",
                "fuel": "3",
                "trucktype": "2",
                "mileage": 1000,
                "truck_features": [
                    "1",
                    "2"
                ]
            },
            "images": [
                "http://www.a.com/image3.png"
            ]
        }
    ]
}
```