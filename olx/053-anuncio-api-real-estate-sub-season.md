---
title: Temporada
url: https://developers.olx.com.br/anuncio/api/real_estate/sub_season.html
source: crawler
fetched_at: 2026-02-07T15:17:48.8887604-03:00
rendered_js: false
word_count: 364
summary: This document specifies the mandatory and optional parameters required for creating or editing advertisements in the 'Season Rental' subcategory. It provides technical details on field values, types, and the expected JSON payload structure.
tags:
    - season-rental
    - api-integration
    - json-schema
    - listing-parameters
    - property-listings
category: reference
---

### Subcategoria `Temporada`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `1080`.

Além disso, há parâmetros específicos para esta subcategoria, que devem constar dentro do parâmetro `params` e preenchidos conforme a tabela a seguir:

ParâmetroValorTipoObrigatórioDescrição`rooms``0` para 0 quartos  
`1` para 1 quarto  
`2` para 2 quartos  
`3` para 3 quartos  
`4` para 4 quartos  
`5` para 5 ou mais quartos  
stringSimQuantidade de quartos`bathrooms``1` para 1 banheiro  
`2` para 2 banheiros  
`3` para 3 banheiros  
`4` para 4 banheiros  
`5` para 5 ou mais banheiros  
stringNão1Quantidade de banheiros`garage_spaces``0` para 0 vagas  
`1` para 1 vaga  
`2` para 2 vagas  
`3` para 3 vagas  
`4` para 4 vagas  
`5` para 5 ou mais vagas  
stringNão1Quantidade de vagas de garagem`beds``1` para 1 cama  
`2` para 2 camas  
`3` para 3 camas  
`4` para 4 camas  
`5` para 5 camas  
`6` para 6 camas  
`7` para 7 camas  
`8` para 8 camas  
`9` para 9 camas  
`10` para 10 camas  
`11` para 11 camas  
`12` para 12 camas  
`13` para 13 camas  
`14` para 14 camas  
`15` para 15 camas  
`16` para 20 camas  
`17` para 25 camas  
`18` para 30 ou mais camasstringSimQuantidade de camas`size`string numéricaNão1Área do apartamento (m²)`season_type``1` para Apartamento  
`2` para Casa  
`3` para Quarto individual  
`4` para Quarto compartilhado  
`5` para Hotel, hostel e pousada  
`6` para Sítio, fazenda e chácarastringSimTipo de imóvel`season_features``1` para Ar condicionado  
`2` para Aquecimento  
`3` para Café da manhã  
`4` para Churrasqueira  
`5` para Estacionamento  
`6` para Fogão  
`7` para Geladeira  
`8` para Internet  
`9` para Lareira  
`10` para Máquina de lavar  
`11` para Permitido animais  
`12` para Piscina  
`13` para Roupa de cama  
`14` para Toalhas  
`15` para TV a cabo  
`16` para Ventilador  
`17` para Varanda/Terraçoarray de stringsNão1Detalhes do imóvel`rent_type``1` para Por dia  
`2` para Por semana  
`3` para Por mês  
`4` para PacotestringNão1Tipo de pagamento

1: Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).

Aqui está um exemplo de JSON para inserção ou edição de anúncios na subcategoria `Temporada`:

```
{
    "access_token": "ca18abccaadd282490e75173f98b8ec6f0c1c6c8",
    "ad_list": [
        {
            "id": "5555555555",
            "operation": "insert",
            "category": 1080,
            "subject": "Casa para Aluguel de Temporada Super Legal",
            "body": "Descrição do anúncio\nNova linha da descrição\nAinda outra linha da descrição",
            "phone": 2155555555,
            "type": "s",
            "price": 150,
            "zipcode": "24230090",
            "params": {
                "rooms": "3",
                "bathrooms": "2",
                "garage_spaces": "2",
                "beds": "10",
                "size": "150",
                "rent_type": "1",
                "season_type": "2",
                "season_features": [
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
            "id": "6666666",
            "operation": "insert",
            "category": 1080,
            "subject": "Casa para Aluguel de Temporada Super Legal",
            "body": "Descrição do anúncio\nNova linha da descrição\nAinda outra linha da descrição",
            "phone": 2155555555,
            "type": "s",
            "price": 150,
            "zipcode": "24230090",
            "params": {
                "rooms": "3",
                "bathrooms": "2",
                "garage_spaces": "2",
                "beds": "10",
                "size": "150",
                "rent_type": "1",
                "season_type": "2",
                "season_features": [
                    "1",
                    "2"
                ]
            },
            "images": [
                "http://www.a.com/image1.png",
                "http://www.a.com/image2.png"
            ]
        }
    ]
}
```