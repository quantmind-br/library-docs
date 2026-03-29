---
title: Integrar lead na OLX
url: https://developers.olx.com.br/lead/how_to.html
source: crawler
fetched_at: 2026-02-07T15:17:29.523359773-03:00
rendered_js: false
word_count: 619
summary: Explica como configurar e gerenciar endpoints para o recebimento de leads da OLX via API, incluindo autenticação oAuth e operações de CRUD para URLs de notificação.
tags:
    - olx-leads
    - api-integration
    - oauth-authentication
    - lead-configuration
    - webhooks
    - endpoint-management
category: api
---

Se você ainda não está integrado com a OLX para recebimento de leads, deverá disponibilizar um endpoint para a OLX homologar a integração de leads.

A OLX requer que cada anunciante tenha um endpoint único. Recomendamos estruturas similares a essas:

- https://seudominio.com.br/olx/lead/TOKEN
- https://TOKEN.seudominio.com.br/olx/lead

O `TOKEN`, nestes exemplos, é o identificador do anunciante na base do sistema ou CRM que receberá o lead. Pode ser utilizado para identificar um determinado cliente da base.

Recomendamos essa estrutura especificamente para sistemas integrados que serão usados por mais do que um anunciante (isso normalmente acontece quando um sistema de mercado é contratado por diversos anunciantes ou quando um sistema é usado por um anunciante que tem filiais e quer manter controle desse contexto).

## Autenticação oAuth no OLX

Para utilizar a configuração da URL de envio do leads, é necessário autenticar-se em nome de um usuário do OLX através do protocolo oAuth. A documentação da autenticação oAuth encontra-se [aqui](https://developers.olx.com.br/anuncio/api/oauth.html) para conseguir o `access_token`.

Na autenticação, o sistema solicitante receberá o `client_id` e o `client_secret` que deverão ser usados na URL de conexão. Durante o fluxo oAuth será requisitado que o usuário dê permissão ao integrador para gerenciar seus anúncios na OLX. No *handshake* do oAuth, é requisitado também o `scope` que a aplicação-cliente necessitará. Para utilizar o sistema de integração de anúncios via API, é preciso o `scope` `autoservice`.

> Atenção: o `scope` necessita ter `autoservice`, caso contrário a requisição será invalidada.

## Criar uma configuração de lead

A URL usada para fazer a requisição é https://apps.olx.com.br/autoservice/v1/lead, método `POST`. Essa requisição deve conter o `access_token` de cada anunciante no header como: `Authorization: Bearer <access_token>`.

Exemplo de requisição usando o `cURL`:

```
curl -POST 'https://apps.olx.com.br/autoservice/v1/lead' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>' \
--data '{
  "url": "https://seudominio.com.br/olx/lead/de42f9b4-6fdb-4d65-a8b8-30648ffa3685"
  "token": "b2x4OnVuZGVmaW5lZA"
}'
```

Valores do Body:

ParâmetroValoresObrigatórioDescrição`url``string`simURL que irá receber a requisição do lead`token``string`nãoValor de um token esperado pela sua aplicação para caso precise de uma credencial extra de segurança. Será enviado no Header como `Authorization` conforme descrito [aqui](https://developers.olx.com.br/lead/leads.html)

A URL `https://seudominio.com.br/olx/lead/de42f9b4-6fdb-4d65-a8b8-30648ffa3685` é apenas um exemplo. Você deve substituí-la pela URL do seu endpoint único por cliente em que está sendo configurado para receber o lead.

Após a requisição ser processada com sucesso, você receberá uma resposta indicando que a configuração de lead foi criada. A resposta será semelhante a esta:

```
{
    "id": "154f10e7-2586-4699-be05-f3587ac7e4fe",
    "url": "https://seudominio.com.br/olx/lead/de42f9b4-6fdb-4d65-a8b8-30648ffa3685",
    "token": "b2x4OnVuZGVmaW5lZA"
}
```

O campo `id` é o identificador único da configuração de lead, que pode ser usado para consultar ou alterar a configuração no futuro.

## Consultar configuração do lead

A URL usada para fazer a requisição é https://apps.olx.com.br/autoservice/v1/lead/:id, método `GET`. Essa requisição deve conter o `access_token` de cada anunciante no header como: `Authorization: Bearer <access_token>`.

Exemplo de requisição usando o cURL:

```
curl -L \
--url 'https://apps.olx.com.br/autoservice/v1/lead/154f10e7-2586-4699-be05-f3587ac7e4fe' \
--header 'Authorization: Bearer <access_token>'
```

A resposta será semelhante a esta:

```
{
    "id": "154f10e7-2586-4699-be05-f3587ac7e4fe",
    "url": "https://seudominio.com.br/olx/lead/de42f9b4-6fdb-4d65-a8b8-30648ffa3685",
    "token": "b2x4OnVuZGVmaW5lZA"
}
```

## Alterar configuração de notificação

A URL usada para fazer a requisição é https://apps.olx.com.br/autoservice/v1/lead/:id, método `PUT`. Essa requisição deve conter o `access_token` de cada anunciante no header como: `Authorization: Bearer <access_token>`.

Exemplo de requisição usando o cURL:

```
curl -X PUT 'https://apps.olx.com.br/autoservice/v1/lead/154f10e7-2586-4699-be05-f3587ac7e4fe' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>' \
--data '{
  "url": "https://seudominio.com.br/olx/lead/de42f9b4-6fdb-4d65-a8b8-30648ffa3685"
}'
```

A URL `https://seudominio.com.br/olx/lead/de42f9b4-6fdb-4d65-a8b8-30648ffa3685` é apenas um exemplo. Você deve substituí-la pela URL do seu endpoint único por cliente em que está sendo configurado para receber o lead.

A resposta será semelhante a esta:

```
{
    "id": "154f10e7-2586-4699-be05-f3587ac7e4fe",
    "url": "https://seudominio.com.br/olx/lead/de42f9b4-6fdb-4d65-a8b8-30648ffa3685"
}
```

## Excluir configuração de notificação

A URL usada para fazer a requisição é https://apps.olx.com.br/autoservice/v1/lead/:id, método `DELETE`. Essa requisição deve conter o `access_token` de cada anunciante no header como: `Authorization: Bearer <access_token>`.

Aqui está um exemplo de como fazer essa requisição usando o cURL:

```
curl -X DELETE 'https://apps.olx.com.br/autoservice/v1/lead/154f10e7-2586-4699-be05-f3587ac7e4fe' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>'
```

Retorno com código de sucesso `204 No Content`.

## Códigos e motivos de erros da requisição retornados

Status Code

Descrição

MotivoMensagem

`401`

Token inválido ou vazioACCESS\_DENIEDCheck the client authentication token

`401`

Configuração de Lead não usa formato OLXUNAUTHORIZEDLead configuration does not use OLX format

`404`

URL e configuração não encontradaNOT\_FOUNDConfigurations not found

`429`

Requisição bloqueada por exceder a taxa máxima de requisições por minuto ([detalhes aqui](https://developers.olx.com.br/faq/rate_limit.html))RATE\_LIMITYou have exceeded the X requests in Y seconds limit!

`500`

Erro interno inesperadoUNEXPECTED\_INTERNAL\_ERRORUnexpected internal error. Try again later