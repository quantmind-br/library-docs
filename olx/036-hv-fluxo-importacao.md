---
title: Via Importação do Anúncio
url: https://developers.olx.com.br/hv/fluxo_importacao.html
source: crawler
fetched_at: 2026-02-07T15:17:37.203443431-03:00
rendered_js: false
word_count: 163
summary: This document explains how to activate the Vehicle History feature during the ad import process on OLX, detailing specific API parameters and mandatory field requirements.
tags:
    - olx-api
    - vehicle-history
    - ad-import
    - api-parameters
    - automotive-ads
category: api
---

## Aplicar Histórico Veicular via Importação

A ativação do Histórico Veicular (HV) também pode ser feita diretamente durante o processo de importação de anúncios na OLX, por meio do campo `vehicle_history` dentro do objeto `params`.

> 📌 Consulte também o [guia completo de parâmetros para carros, vans e utilitários](https://developers.olx.com.br/anuncio/api/autos/sub_auto.html) para mais detalhes sobre cada campo utilizado na importação de anúncios.

## Como funciona

- O campo `vehicle_history` indica se o HV deve ser aplicado ao anúncio.
- Quando o valor deste campo for `"1"`, os campos `renavam` e `cpf_cnpj` se tornam **obrigatórios**.
- Caso o valor enviado seja `"2"` ou o campo `vehicle_history` não esteja presente, o comportamento segue o fluxo padrão, **sem a ativação do HV**.

* * *

### Valores aceitos para `vehicle_history`

ValorSignificado`"1"`Aplicar Histórico Veicular`"2"`Não aplicar Histórico Veicular (comportamento padrão)

> ⚠️ Caso `vehicle_history = "1"` e os campos `renavam` ou `cpf_cnpj` não forem enviados, a requisição de importação será rejeitada.

* * *

### Exemplo JSON com Histórico Veicular aplicado

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
        "financial": ["2", "3"],
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
        "car_features": ["1", "3"]
      },
      "images": ["http://www.a.com/image1.png", "http://www.a.com/image2.png"]
    }
  ]
}
```

### Exemplo JSON sem ativação do Histórico Veicular

```
{
  "access_token": "ca18abccaadd282490e75173f98b8ec6f0c1c6c8",
  "ad_list": [
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
        "car_features": ["1", "2"]
      },
      "images": ["http://www.a.com/image3.png"]
    }
  ]
}
```

### Validações importantes

CampoObrigatório quando vehicle\_history = "1"`renavam`Sim`cpf_cnpj`Sim