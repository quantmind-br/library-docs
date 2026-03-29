---
title: Barcos e Aeronaves
url: https://developers.olx.com.br/anuncio/api/autos/sub_boat_plane.html
source: crawler
fetched_at: 2026-02-07T15:17:32.431368259-03:00
rendered_js: false
word_count: 362
summary: This document details the specific parameters and configuration requirements for listing items under the Boats and Aircraft subcategory. It defines the mandatory fields, allowed values, and data types necessary for successful API integration within this category.
tags:
    - api-integration
    - parameter-definitions
    - boats-and-aircraft
    - data-schema
    - listing-configuration
category: reference
---

### Subcategoria `Barcos e Aeronaves`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `2080`.

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
`1950` para 1950 ou anteriorstringSimAno do barco ou aeronave`mileage`integerSimQuilometragem do barco ou aeronave`fuel``1` para Gasolina  
`2` para Álcool  
`3` para Flex  
`4` para Gás Natural  
`5` para Diesel  
`6` para Híbrido  
`7` para ElétricostringNão1Tipo de combustível`boattype``1` para Lancha  
`2` para Barco  
`3` para Jet Ski  
`4` para Motor  
`5` para Veleiro Monocasco  
`6` para Veleiro Multicasco  
`7` para Embarcação Inflável  
`8` para Pedalinho  
`9` para Hovercraft  
`10` para Outros  
stringNão1Tipo de barco`boatheight`stringNão1Altura do barco`boatlength`stringNão1Comprimento do barco`boatwidth`stringNão1Largura do barco`exchange``1` para Sim  
`2` para NãostringNão1Aceita trocas pelo produto`financial_boat``1` para Financiado  
`2` para De leilãostringNão1Estado financeiro`owner``1` para Sim  
`2` para NãostringNão1Único dono

> **Notas**
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).

Aqui está um exemplo de JSON para a subcategoria `Barcos e aeronaves`:

```
{
    "access_token": "ca18abccaadd282490e75173f98b8ec6f0c1c6c8",
    "ad_list": [
        {
            "id": "BOAT005_ROD1",
            "operation": "insert",
            "category": 2080,
            "subject": "Barco em ótimo estado",
            "body": "Barco do tipo X, usado no caso Y.\nBarco em excelente estado, com características X, Y e Z.o",
            "phone": 2155555555,
            "type": "s",
            "price": 10500,
            "zipcode": "24230090",
            "params": {
                "regdate": "1950",
                "mileage": 20000,
                "fuel": "1",
                "boattype": "2",
                "boatlength": "10",
                "boatheight": "5",
                "exchange": "1",
                "financial_boat": "1",
                "owner": 1
            },
            "images": [
                "http://www.a.com/image1.png",
                "http://www.a.com/image2.png"
            ]
        },
        {
            "id": "PLANE005_ROD2",
            "operation": "insert",
            "category": 2080,
            "subject":"Avião em ótimo estado",
            "body":"Avião do tipo X, usado no caso Y.\nAvião em excelente estado, com características X, Y e Z.",
            "phone": 2155555544,
            "type": "s",
            "price": 12500,
            "zipcode": "24234590",
            "params": {
                "regdate": "1950",
                "mileage": 20000
            },
            "images": [
                "http://www.a.com/image3.png"
            ]
        }
    ]
}
```