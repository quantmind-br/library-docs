---
title: Subcategoria Máquinas para produção industrial
url: https://developers.olx.com.br/anuncio/api/agro/industrial_production.html
source: crawler
fetched_at: 2026-02-07T15:18:30.764804711-03:00
rendered_js: false
word_count: 119
summary: This document outlines the required parameters and category codes for listing items in the Industrial Production Machinery subcategory via API.
tags:
    - api-integration
    - industrial-machinery
    - category-parameters
    - json-payload
    - listing-configuration
category: configuration
---

### Subcategoria `Máquinas para produção industrial`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `12140`.

Além disso, há parâmetros específicos para esta subcategoria, que devem constar dentro do parâmetro `params` e preenchidos conforme a tabela a seguir:

ParâmetroValorTipoObrigatórioDescrição`condition_full``1` para Novo  
`2` para Usado - Excelente  
`3` para Usado - Bom  
`4` para Recondicionado  
`5` para Com defeitostringsimCondição da máquina

> **Notas**
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).

Aqui está um exemplo de JSON para a subcategoria `Máquinas para produção industrial`:

```
{
    "access_token": "12345678909876543211abcdefghijklmnopqrstuv",
    "ad_list": [
        {
            "id": "AGR000_ROD1",
            "operation": "insert",
            "type": "s",
            "price": 1000,
            "phone": 1132303891,
            "zipcode": "20521160",
            "subject": "Ventilador Aviario Frete não incluso",
            "body": "VENTILADOR AVIARIO",
            "category": 12140,
            "images": [
                "http://www.sitedeagro.com/img1.jpg",
                "http://www.sitedeagro.com/img2.jpg"
            ],
            "params": {
                "condition_full": "1"
            }
        }
    ]
}
```