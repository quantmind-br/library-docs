---
title: Configuração de Notificações
url: https://developers.olx.com.br/webhooks/notifications_configuration.html
source: crawler
fetched_at: 2026-02-07T15:17:22.168219873-03:00
rendered_js: false
word_count: 854
summary: This document explains how to set up and manage webhook notifications for advertisement status updates using the OLX self-service API. It covers authentication via OAuth and the CRUD operations required to manage notification endpoints and tokens.
tags:
    - olx-api
    - webhooks
    - notification-configuration
    - oauth-authentication
    - ad-status
    - rest-api
category: guide
---

## Configuração de Notificações

**Aviso:** Esta é uma versão **beta** e deverá sofrer modificações conforme a necessidade.

O Autoserviço de Configuração de Notificações é uma funcionalidade que permite que integradores configurem detalhes de como e onde as notificações serão recebidas em seus servidores.

Esta funcionalidade foi projetada para melhorar a eficiência e a transparência do processo de configuração de notificações.

Com esta funcionalidade, poderá definir regras personalizadas o endpoint onde os webhooks serão postados. Isso significa que, uma vez configurado, os status dos anúncios serão enviados automaticamente para o endereço informado. Integradores têm controle total sobre suas configurações de notificação, podendo inserir uma nova configuração, consultar a configuração existente, alterar a configuração ou excluir a configuração a qualquer momento. Isso oferece-lhes a flexibilidade de adaptar as notificações às suas necessidades específicas. Para configurar as notificações basta realizar uma requisição seguindo as instruções abaixo.

Em resumo, o Autoserviço de Configuração de Notificações de Status de Anúncios Importados oferece aos integradores uma maneira flexível e eficiente de monitorar o status dos anúncios importados.

## Autenticação oAuth no OLX

Para utilizar a configuração de notificações por Webhook, é necessário autenticar-se em nome de um usuário do OLX através do protocolo oAuth. A documentação da autenticação oAuth encontra-se [aqui](https://developers.olx.com.br/anuncio/api/oauth.html).

Na autenticação, o sistema solicitante receberá o `client_id` e o `client_secret` que deverão ser usados na URL de conexão. Durante o fluxo oAuth será requisitado que o usuário dê permissão ao integrador para gerenciar seus anúncios na OLX. No *handshake* do oAuth, é requisitado também o `scope` que a aplicação-cliente necessitará. Para utilizar o sistema de integração de anúncios via API, é preciso o `scope` `autoupload`.

## Criar uma configuração de notificação

Para criar uma nova configuração de notificação, você deve realizar uma requisição `POST` para o endpoint específico. Esta requisição deve incluir no cabeçalho o `Content-Type` como `application/json` e o `Authorization` com o seu token de acesso. No corpo da requisição, especifique o método de notificação, a URL do seu servidor que receberá as notificações, o tipo de mídia (que deve ser `application/json`), e um token que será utilizado para autenticar a requisição no seu servidor.

Aqui está um exemplo de como fazer essa requisição usando o `curl`:

```
curl 'https://apps.olx.com.br/autoservice/v1/notification' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer SEU_TOKEN_AQUI' \
--data '{
  "method": "POST",
  "url": "http://localhost:9090",
  "media_type": "application/json",
  "token": "1231232213"
}'
```

Substitua `SEU_TOKEN_AQUI` pelo seu token de acesso real.

A URL `http://localhost:9090` é apenas um exemplo; você deve substituí-la pela URL do seu servidor que está configurado para receber as notificações.

Após a requisição ser processada com sucesso, você receberá uma resposta indicando que a configuração de notificação foi criada. A resposta será semelhante a esta:

```
{
    "id": "97370d55-e596-4598-8bc3-ee31403c3e43",
    "method": "POST",
    "url": "http://localhost:9090",
    "media_type": "application/json",
    "token": "1231232213",
    "type": "AD_STATUS"
}
```

Este objeto de resposta confirma que a configuração de notificação foi criada com sucesso. O campo `id` é o identificador único da configuração de notificação, que pode ser usado para consultar ou alterar a configuração no futuro.

## Consultar configuração de notificação

Para consultar sua configuração de notificações, use o método `GET`, passando seu `Access Token` no campo `Authorization` do header.

Aqui está um exemplo de como fazer essa requisição usando o curl:

```
curl -L \
--url 'https://apps.olx.com.br/autoservice/v1/notification/{id}' \
--header 'Authorization: Bearer SEU_TOKEN_AQUI'
```

Substitua `{id}` pelo ID da configuração de notificação que você deseja consultar e `SEU_TOKEN_AQUI` pelo seu token de acesso real.

A resposta será semelhante a esta:

```
{
  "id": "cedbb66c-b9a0-4c1b-a558-21fe987004c6",
  "method": "POST",
  "url": "https://urlintegrador.com.br/notif",
  "media_type": "application/json",
  "token": "1231232213",
  "type": "AD_STATUS"
}
```

Este objeto de resposta confirma que a configuração de notificação foi consultada com sucesso. O campo `id` é o identificador único da configuração de notificação, que pode ser usado para consultar ou alterar a configuração no futuro.

## Alterar configuração de notificação

Para alterar sua configuração de notificações, use o método `PUT`, passando seu `Access Token` no campo `Authorization` do header.

Aqui está um exemplo de como fazer essa requisição usando o curl:

```
curl -X PUT 'https://apps.olx.com.br/autoservice/v1/notification/{id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer SEU_TOKEN_AQUI' \
--data '{
  "method": "POST",
  "url": "http://localhost:9090",
  "media_type": "application/json",
  "token": "1231232213"
}'
```

Substitua `{id}` pelo ID da configuração de notificação que você deseja alterar e `SEU_TOKEN_AQUI` pelo seu token de acesso real.

A URL `http://localhost:9090` é apenas um exemplo; você deve substituí-la pela URL do seu servidor que está configurado para receber as notificações.

## Excluir configuração de notificação

Para excluir sua configuração de notificações, use o método `DELETE`, passando seu `Access Token` no campo `Authorization` do header.

Aqui está um exemplo de como fazer essa requisição usando o curl:

```
curl -X PUT 'https://apps.olx.com.br/autoservice/v1/notification/{id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer SEU_TOKEN_AQUI'
```

Substitua `{id}` pelo ID da configuração de notificação que você deseja excluir e `SEU_TOKEN_AQUI` pelo seu token de acesso real.

## Tipos de Notificação

Atualmente, o Autoserviço de Configuração de Notificações suporta apenas um tipo de notificação: `Status de Anúncios`. Este tipo de notificação é enviado sempre que o status de um anúncio importado é alterado. O status dos anúncios possíveis estão listados na tabela (Status de Anúncio)\[/webhooks/notifications\_ad\_status.md#status-de-anuncio]. O status do anúncio é enviado no corpo da notificação, juntamente com o `ID` do anúncio e a `data e hora da alteração`.

## Campos da Configuração de Notificação

A configuração de notificação é um objeto JSON que contém os seguintes campos:

CampoDescrição`id`O identificador único da configuração de notificação.`method`O método HTTP que será usado para enviar a notificação. Atualmente, apenas o método `POST` é suportado.`url`A URL do servidor que receberá a notificação.`media_type`O tipo de mídia que será usado para enviar a notificação. Atualmente, apenas o tipo `application/json` é suportado.`token`O token que será usado para autenticar a requisição no servidor.`type`O tipo de notificação. Atualmente, apenas o tipo `AD_STATUS` é suportado.

## Aviso

- Se você tem dúvida sobre o formato do endpoint que aceitamos, por favor [confira aqui](https://developers.olx.com.br/webhooks/url_encoding/#exemplos-de-endpoints-que-poderao-ser-utilizados)