---
title: Modelo de notificações
url: https://developers.olx.com.br/webhooks/notifications_model.html
source: crawler
fetched_at: 2026-02-07T15:17:22.690743342-03:00
rendered_js: false
word_count: 118
summary: This document defines the structure and data format of webhook notifications, including the specific JSON payload fields and requirements for receiving ad status updates.
tags:
    - webhook-notifications
    - json-payload
    - api-integration
    - ad-status
    - event-notifications
category: reference
---

## Modelo de notificações

Todas as notificações serão enviadas para a URL configurada no webhook, utilizando o método cadastrado e o token de autenticação fornecido. O corpo da notificação será um objeto `JSON` contendo as informações do anúncio e ações que podem ser realizadas sobre ele.

## Pré-requisitos

Para receber notificações de status de anúncios, você precisa configurar um webhook. Veja como fazer isso na seção [Configuração de Notificações](https://developers.olx.com.br/webhooks/notifications_configuration.html).

## Modelo de notificação

Toda notificação seguirá o mesmo modelo, com os seguintes campos:

```
{
  "id":"<Identificador único da notificação>",
  "topic":"<Tipo de notificação>",
  "created_at":"<Data e hora que o evento ocorreu>",
  "data":{
    <Dados da notificação conforme o tipo>,
    "actions":{
      <Ações possíveis sobre o recurso conforme o tipo>
    }
  }
}
```

Aqui está um exemplo de notificação de status de anúncio:

```
{
  "id":"191389c3-d42a-464d-9c3f-4edfb6c1fc05",
  "topic":"AD_STATUS",
  "created_at":"2024-05-29T18:00:00.123",
  "data":{
    "ad":{
      "id":"12345",
      "list_id":1234553,
      "category":11020,
      "status":"published",
      "operation":"INSERT"
    },
    "actions":{
      "view":"https://www.olx.com.br/vi/1223432423.htm"
    }
  }
}
```

## Tipos de Notificação

- `Status de Anúncios`: Este tipo de notificação é enviado sempre que o status de um anúncio importado é alterado. Para maiores informações, consulte a [documentação](https://developers.olx.com.br/webhooks/notifications_ad_status.html).