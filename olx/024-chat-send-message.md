---
title: Respondendo à um chat (CRM → OLX)
url: https://developers.olx.com.br/chat/send_message.html
source: crawler
fetched_at: 2026-02-07T15:17:35.606209085-03:00
rendered_js: false
word_count: 51
summary: This document provides the technical specification for the OLX Auto Service API endpoint used to send chat messages from a CRM system to the OLX platform.
tags:
    - olx-api
    - crm-integration
    - chat-messaging
    - api-endpoint
    - http-post
category: api
---

## Respondendo à um chat (CRM → OLX)

## Endpoint de ativação:

- Método: POST
- Endpoint: https://apps.olx.com.br/autoservice/v1/chat/send
- Header: Authorization - Bearer token
- Body:

```
{
  "textMessage": "string",
  "messageId": "string",
  "chatId": "string",
}
```

Respostas:

- 200 - mensagem enviada com sucesso;
- 401 - token inválido;
- 400 - body inválido/conta não tem integração/não foi possível obter o endereço de IP;
- 500 - erro interno no envio;