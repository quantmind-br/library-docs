---
title: Autenticação do chat na API olx.com.br
url: https://developers.olx.com.br/chat/oauth_chat.html
source: crawler
fetched_at: 2026-02-07T15:17:32.566261087-03:00
rendered_js: false
word_count: 272
summary: This document outlines the authentication and authorization process for OLX chat integration using the OAuth 2.0 protocol. It details the required parameters, scopes, and response handling for obtaining access tokens.
tags:
    - authentication
    - authorization
    - oauth-2-0
    - olx-api
    - chat-integration
    - access-token
category: guide
---

## Autenticação e Autorização

Para realizar a integração de chat, é necessário que o cliente autorize no portal OLX que o integrador administre suas mensagens de chat. Portanto, deve ser solicitado a inclusão do scope chat ao access-token.

> Para criação de um access\_token, siga [essa documentação](https://developers.olx.com.br/anuncio/api/oauth.html).

## Requisição

A autorização é requisitada pelo Integrador ao realizar a abertura de uma página no navegador incluindo parâmetros que indicam o tipo de acesso requerido.

### Exemplo:

https://auth.olx.com.br/oauth?client\_id=​1055d3e698d289f2af8663725127bd4b&redirect\_uri=https://yourserver.com/token&response\_type=code&scope=autoupload%20chat

## Lista de Parâmetros:

ParâmetroValoresObrigatórioDescrição`response_type`codeSimDetermina que o valor esperado pela requisição será um código de autorização.`client_id`chave em hash alfanuméricoSimIdentifica o cliente que está enviando a requisição. O valor do parâmetro tem que ser idêntico ao valor fornecido pelo olx.com.br durante o registro da aplicação.`redirect_uri`URISim (se integrador cadastrou múltiplas URIs)URL para onde a resposta da autorização será redirecionada após ter ocorrido a aprovação pelo cliente.`scope`  
`basic_user_info`  
`autoupload`  
`chat`SimIdentifica os acessos que estão sendo requisitados. Para solicitar mais de um scope, separe com espaço.`state`stringNãoFornece qualquer valor que pode ser útil a aplicação ao receber a resposta de requisição.

## Resposta

A resposta será enviada para o redirect\_uri,conforme especificado na URL da requisição. Se o usuário aprovar o acesso, a resposta conterá um código de autorização e o parâmetro state (se incluído na requisição). Se o usuário não aprovar, a resposta retornará uma mensagem de erro.

### Exemplo

https://yourserver.com/token?state=/profile&code=4gP7q7W91aoMsCeLvIaQm6bTrgtp7

ParâmetroValoresObrigatórioDescrição`code`Código de autorização gerado pelo servidor de autenticação.SimCódigo de autorização utilizado para solicitar permissão de acesso a recursos de um usuário. Expira 10 minutos após ter sido gerado e não pode ser reutilizado.`state`Mesmo valor enviado pelo cliente na requisição.Sim (se presente na requisição)Fornece qualquer valor que pode ser útil a aplicação ao receber a resposta de requisição.