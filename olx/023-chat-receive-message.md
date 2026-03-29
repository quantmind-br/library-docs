---
title: Recebendo mensagens do chat (OLX → CRM)
url: https://developers.olx.com.br/chat/receive_message.html
source: crawler
fetched_at: 2026-02-07T15:17:33.280688601-03:00
rendered_js: false
word_count: 328
summary: This document explains how to configure and receive OLX chat messages via webhooks in a CRM, detailing the activation/deactivation endpoints and the chat message data structure.
tags:
    - olx-integration
    - webhook-configuration
    - chat-api
    - crm-integration
    - http-protocol
category: api
---

## Recebendo mensagens do chat (OLX → CRM)

O envio de mensagens do chat da OLX para o CRM ocorre através de webhook. Ou seja, o CRM deve possuir um endpoint acessível através da internet e capaz de receber uma requisição contendo a mensagem do chat.

> Webhook é um método de comunicação entre diferentes aplicações, facilitando e agilizando a troca de informações entre elas.
> 
> Isso permite configurar o envio de notificações automáticas, assim que um evento relevante acontece em um sistema, bastando definir para qual URL cada webhook deve ser enviado quando os eventos ocorrerem.
> 
> Nosso sistema enviará aos integradores as mensagens de chat nas URLs (endpoints) configuradas. Esta requisição será realizada via protocolo HTTP no verbo POST, no endpoint especificado passando um JSON como corpo do request.

## Configuração de webhook

### Endpoint de ativação:

- Método: POST
- Endpoint: https://apps.olx.com.br/autoservice/v1/chat
- Header: Authorization - Bearer token
- Body: { "webhook": "url" } - JSON

Respostas:

- 201 - ativação concluída com registro criado (primeira vez);
- 401 - token inválido;
- 200 - ativação concluída com registro atualizado (update);
- 500 - erro interno na ativação;

> Caso o CRM deseje aumentar a segurança do seu endpoint, pode restringir o acesso à ele por IP, concedendo o acesso para somente o nosso IP de saída 54.162.151.93

### Endpoint de desativação:

- Método: DELETE
- Endpoint: https://apps.olx.com.br/autoservice/v1/chat
- Header: Authorization - Bearer token

Respostas:

- 200 - desativação concluída;
- 401 - token inválido;
- 400 - conta não existe;
- 500 - erro interno na ativação;

## Mensagem do chat

Quando um novo evento de chat ocorrer (ou seja, quando um comprador submeter uma mensagem no chat em um anúncio cuja conta do vendedor possuir um webhook configurado) enviaremos uma requisição POST no endpoint configurado conforme informações abaixo.

```
{
  "chatId": "{msg.publicId}",
  "message": "{msg.message}",
  "senderType": "buyer",
  "email": "{get_email(msg.senderAccountId)}",
  "name": "{get_name(msg.senderAccountId)}",
  "phone": "{get_phone(msg.senderAccountId)}",
  "messageTimestamp": "{msg.messageTimestamp}",
  "messageId": "{msg.messageId}",
  "origin": "{msg.origin}",
  "listId": "{msg.listId}"
}
```

### Descrição dos campos

CampoTipoDescrição`chatId``String`Identificador do chat`message``String`Texto enviado pelo remetente`senderType``String`Tipo de mensagem:  
`account`: mensagem enviada de forma orgânica  
`system`: mensagem enviada por um sistema`email``String`Email do comprador`name``String`Nome do comprador`phone``String`Telefone do comprador`messageTimestamp``Timestamp`Data/hora da notificação  
Formato: `yyyy-MM-ddThh24:mm:ss.ms``messageId``String`Identificador da mensagem`origin``String`Origem da mensagem:  
`buyer`: mensagem originada pelo comprador  
`seller`: mensagem originada pelo vendedor`listId``String`Identificador do anúncio