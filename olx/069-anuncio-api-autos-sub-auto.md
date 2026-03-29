---
title: Carros, vans e utilitários
url: https://developers.olx.com.br/anuncio/api/autos/sub_auto.html
source: crawler
fetched_at: 2026-02-07T15:17:30.603156714-03:00
rendered_js: false
word_count: 787
summary: This document specifies the technical parameters and data requirements for creating or editing vehicle advertisements in the cars and vans subcategory via API.
tags:
    - olx-api
    - automotive-ads
    - api-parameters
    - vehicle-listings
    - data-schema
    - technical-reference
category: api
---

### Subcategoria `Carros, vans e utilitários`

Para esta subcategoria, é necessário preencher o parâmetro `category` com o valor `2020`.

Além disso, há parâmetros específicos para esta subcategoria, que devem constar dentro do parâmetro `params` e preenchidos conforme a tabela a seguir:

ParâmetroValorTipoObg.Descrição`regdate`Ano do veículo para os fabricados à partir de 1980 ou  
`1975` para Entre 1975 e 1980  
`1970` para Entre 1970 a 1975  
`1965` para Entre 1965 e 1970  
`1960` para Entre 1960 e 1965  
`1955` para Entre 1955 e 1960  
`1950` para 1950 ou anteriorstringSimAno do automóvel`mileage`integerSimQuilometragem do automóvel`gearbox``1` para Manual  
`2` para Automático  
`3` para Semi-Automático  
`4` para AutomatizadostringNão1Tipo de câmbio`fuel``1` para Gasolina  
`2` para Álcool  
`3` para Flex  
`4` para Gás Natural![](https://img.shields.io/badge/-deprecated-critical)  
`5` para Diesel  
`6` para Híbrido  
`7` para ElétricostringNão1Tipo de combustível`gnv_kit``1` para Sim  
`2` para NãostringNão1Caso o automóvel possui Kit GNV`vehicle_brand`stringSim5Marca do automóvel. Para verificar as disponíveis, [use o serviço da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).`vehicle_model`stringSim5Modelo da marca do automóvel. Para verificar os disponíveis, [use o serviço da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).`vehicle_version`stringSim5Versão do modelo do automóvel. Para verificar as disponíveis, [use o serviço da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).`vehicle_tag`stringSim4 4.1Placa do Carro`chassi`stringNão1Chassi do automóvel`renavam`7stringNão1,7Renavam do automóvel`cpf_cnpj`7stringNão1,7Dono do automóvel`car_features``1` para Ar condicionado  
`2` para Dir. hidráulica3![](https://img.shields.io/badge/-deprecated-critical)  
`3` para Vidro elétrico  
`4` para Trava elétrica  
`5` para Air bag  
`6` para Alarme  
`7` para Som  
`8` para Sensor de ré  
`9` para Câmera de ré  
`10` para Blindado  
`11` para Bancos de couro  
`12` Computador de bordo  
`13` para Conexão USB  
`14` para Volante multifuncional  
`15` para Interface bluetooth  
`16` para Navegador GPS  
`17` para Controle automático de velocidade  
`18` para Rodas de liga leve  
`19` para Teto solar  
`20` para Tração 4x4  
array de stringsNão1Opcionais`doors``1` para 2 portas  
`2` para 4 portas  
`3` para 3 portasstringNão1Número de portas`end_tag` ![](https://img.shields.io/badge/-deprecated-critical)`1` para 0  
`2` para 1  
`3` para 2  
`4` para 3  
`5` para 4  
`6` para 5  
`7` para 6  
`8` para 7  
`9` para 8  
`10` para 9stringNão1,4Número final da placa do automóvel`car_steering``1` para Hidráulica3  
`2` para Elétrica  
`3` para Mecânica  
`4` para Assistida![](https://img.shields.io/badge/-deprecated-critical)  
`5` para Eletro-hidráulicastringNão1Direção`motorpower``1` para 1  
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
`12` para 4.0 ou maisstringNão1Potência do motor`cartype``1` para Passeio6 ![](https://img.shields.io/badge/-deprecated-critical)  
`2` para Conversível  
`3` para Pick-up  
`4` para Antigo6 ![](https://img.shields.io/badge/-deprecated-critical)  
`5` para SUV  
`6` para Buggy  
`7` para Van/Utilitário  
`8` para Sedã  
`9` para Hatch  
`10` para Caminhão Leve  
`11` para Coupé  
`12` para PeruastringNão1Tipo de automóvel`carcolor``1` para Preto  
`2` para Branco  
`3` para Prata  
`4` para Vermelho  
`5` para Cinza  
`6` para Azul  
`7` para Amarelo  
`8` para Verde  
`9` para Laranja  
`10` para OutrastringNão1Cor do automóvel`exchange``1` para Sim  
`2` para NãostringNão1Aceita trocas pelo produto`financial``1` para Financiado2 ![](https://img.shields.io/badge/-deprecated-critical)  
`2` para IPVA Pago  
`3` para Com multas  
`4` para De leilãoarray de strings2.1Não1Estado financeiro`financial_status``1` para Quitado  
`2` para Financiado2stringNão1Estado financeiro`vehicle_history`![](https://img.shields.io/static/v1?label=&message=New&color=green)`1` para Aplicar o HV7  
`2` para Não Aplicar o HVstringNão1Indica se o Histórico Veicular será aplicado ao anúncio. Para mais informações sobre o HV, consulte nossa [Central de Ajudaopen in new window](https://ajuda.olx.com.br/s/article/historico-veicular)`owner``1` para Sim  
`2` para NãostringNão1Único dono`owner_manual``1` para Sim  
`2` para NãostringNão1Com manual do Automóvel`extra_key``1` para Sim  
`2` para NãostringNão1Com chave reserva`dealership_review``1` para Sim  
`2` para NãostringNão1Com revisões feitas em concessionária`warranty``1` para Sim  
`2` para NãostringNão1Com garantia`zero_km``1` para Sim  
`0` para NãostringNão1Carro Zero KM

> **Notas**
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).
> 
> 2 Não aceitamos mais o valor `1 - para Financiado` no parâmetro `financial`. Em vez disso, você deverá utilizar o parâmetro `financial_status` para informar se o estado financeiro é quitado ou financiado.  
> 2.1 Além disso, o parâmetro financial passou a receber um array de strings, permitindo que você informe mais de um valor.
> 
> 3 Não aceitamos mais o valor `2 - para Direção hidráulica` no parâmetro `car_features`. Em vez disso, você deverá utilizar o parâmetro `car_steering` passando o valor `1 - para Hidráulica`.
> 
> 4 O campo `vehicle_tag` passou a ser **obrigatório** para veículos usados e o campo `end_tag` será atribuido com base na placa do veículo.  
> **Observação:** a placa do veículo não é exibida em nossos anúncios.
> 
> 4.1 O campo `vehicle_tag` precisa ser com letras maiúsculas.
> 
> 5 Os campos `vehicle_brand`, `vehicle_model` e `vehicle_version` passaram a ser **obrigatórios**.
> 
> 6 Não aceitamos mais o valor `1 - para Passeio` e `4 - para Antigo` no parâmetro `cartype`.
> 
> 7 Os campos `renavam` e `cpf_cnpj` serão **obrigatórios** caso o valor `1 - para Aplicar o HV` seja passado no parâmetro `vehicle_history`.

Aqui está um exemplo de JSON para inserção ou edição de anúncios na subcategoria `Carros, vans e utilitários`:

```
{
    "access_token": "ca18abccaadd282490e75173f98b8ec6f0c1c6c8",
    "ad_list": [
        {
            "id": "5555555555",
            "operation": "insert",
            "category": 2020,
            "subject": "Carro Novo",
            "body": "Corpo do anúnucio",
            "phone": 2155555555,
            "type": "s",
            "price": 10500,
            "zipcode": "24230090",
            "params": {
                "vehicle_brand": "3",
                "vehicle_model": "6",
                "vehicle_version": "2",
                "regdate": "1988",
                "gearbox": "1",
                "financial": [
                    "2",
                    "3"
                ],
                "financial_status": "1",
                "fuel": "1",
                "renavam": "123456789",
                "vehicle_tag": "ABC1234",
                "vehicle_history": "1",
                "cpf_cnpj": "12345678901",
                "cartype": "2",
                "mileage": 10000,
                "doors": "1",
                "motorpower": "5",
                "car_steering": "1",
                "carcolor": "1",
                "car_features": [
                    "1",
                    "3"
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
            "category": 2020,
            "subject": "Carro Novo 2",
            "body": "Corpo do anúnucio 2",
            "phone": 2155555544,
            "type": "s",
            "price": 12500,
            "zipcode": "24234590",
            "params": {
                "vehicle_brand": "3",
                "vehicle_model": "6",
                "vehicle_version": "2",
                "regdate": "2001",
                "gearbox": "2",
                "fuel": "3",
                "cartype": "2",
                "mileage": 0,
                "doors": "1",
                "motorpower": "5",
                "car_steering": "1",
                "carcolor": "1",
                "car_features": [
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