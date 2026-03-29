---
title: Consumo Saldos e Limites de Anúncios
url: https://developers.olx.com.br/destaque/balance_ads.html
source: crawler
fetched_at: 2026-02-07T15:17:24.889711084-03:00
rendered_js: false
word_count: 445
summary: This document explains how to use the OLX balance API to monitor ad insertion limits, available balances, and plan renewal dates for professional accounts.
tags:
    - olx-ads-api
    - balance-tracking
    - ad-insertion-limits
    - api-reference
    - endpoint-documentation
    - ad-bumps
category: api
---

## Consulta Saldos e Limites de Anúncios

A medida que os anúncios são publicados, o limite disponível em seu plano contratado é consumido. A API abaixo disponibiliza informações para acompanhamento do limite de inserção de um plano, a quantidade de inserções que já foram realizadas, o saldo disponível para inserções de novos anúncios, a data da última renovação do plano e a data que a próxima renovação do plano ocorrerá.

* * *

## Requisição de consulta de saldo e limite

A URL usada para fazer a requisição do arquivo JSON é https://apps.olx.com.br/autoupload/balance, método `GET`. Essa requisição deve conter o `access_token` de cada anunciante no header como: `Authorization: Bearer <access_token>`.

> O campo `access_token` pode ser obtido seguindo a documentação [Autenticação na API olx.com.br](https://developers.olx.com.br/anuncio/api/oauth.html).

## Retorno de sucesso esperado

Se o anunciante possui um plano profissional ativo, a consulta retorna um `status code 200` e um JSON no corpo da resposta com a estrutura:

ParâmetroValoresObrigatórioDescrição`id``string`simIdentificador único do plano profissinal`name``string`simDescrição do plano profissional`ads`[**balance**](#balance)simEstrutura contendo quantidade de inserções do cliente, saldo do cliente e limite de inserções do plano`bumps`[**bumps**](#bumps)simEstrutura contendo quantidade de bumps contratatos pelo cliente, saldo e limite do plano e a avulso`last_renew_date``string (ISO Datetime)`simData da última renovação de saldo de anúncios.

*Observe que esta data e hora estão no Zulu Time Zone. Para horário de Brasília, decremente três horas.*

`next_renew_date``string (ISO Datetime)`simData da próxima renovação de saldo de anúncios.

*Observe que esta data e hora estão no Zulu Time Zone. Para horário de Brasília, decremente três horas.*

### *bumps*

ParâmetroValoresObrigatórioDescrição`plan`[**balance**](#balance)simsaldo de bumps de ads contratados pelo plano PRO`additional`[**balance**](#balance)simsaldo de bumps de ads contratados pelo plano de forma avulsa

### *balance*

ParâmetroValoresObrigatórioDescrição`performed``integer`simInserções já realizadas`available``integer`simSaldo disponível para uso`total``integer`simLimite contratado pelo cliente

## Retorno de erro esperado

Caso ocorra algum erro ou o anunciante não possua plano profissional ativo, a consulta retorna um `status code > 200` e um JSON com o motivo e a mensagem do erro.

## Códigos e motivos de erros da requisição retornados

Status Code

DescriçãoMotivoMensagem

`400`

Falta campo de `authorization` no header da requisiçãoBAD\_REQUESTCheck the header field(s)

`401`

Token inválidoACCESS\_DENIEDCheck the client authentication token

`410`

Cliente não possui planos com limitesPRODUCT\_NOT\_FOUND\_BY\_ACCOUNTPlan does not control limits

`429`

Rate Limit configurado quando o cliente fazer mais requisições por segundo do que deveriaRATE\_LIMITYou have exceeded the X requests in X seconds limit!

`500`

Erro interno inesperadoUNEXPECTED\_INTERNAL\_ERRORUnexpected internal error. Try again later

## Exemplos de retorno

> Para um plano com limite de 20 inserções de anúncios no qual nenhum anúncio foi inserido: Saldos de bumps contratatos pelo plano e avulso.

- Request
  
  ```
  curl -A Mozila -H "Authorization: Bearer <access_token>" "https://apps.olx.com.br/autoupload/balance"
  ```
- Response
  
  ```
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  {
      "id": "cc07f89f5f9b691a4bc24d98614e54df",
      "name": "Plano Profissional - Carros 20",
      "ads": {
          "performed": 0,
          "available": 15,
          "total": 20
      },
      "bumps": {
          "plan": {
              "performed": 2,
              "available": 3,
              "total": 5,
          },
          "additional": {
              "performed": 2,
              "available": 3,
              "total": 5,
          }
      },
      "last_renew_date": "2022-06-30T16:36:32.069324",
      "next_renew_date": "2022-07-29T16:36:32.069324"
  }
  ```

* * *

> Para um plano com limite de 20 inserções de anúncios no qual 5 anúncios foram inseridos:

- Request
  
  ```
  curl -A Mozila -H "Authorization: Bearer <access_token>" "https://apps.olx.com.br/autoupload/balance"
  ```
- Response
  
  ```
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  {
      "id": "cc07f89f5f9b691a4bc24d98614e54df",
      "name": "Plano Profissional - Carros 20",
      "ads": {
          "performed": 5,
          "available": 15,
          "total": 20
      },
      "last_renew_date": "2022-06-30T16:36:32.069324",
      "next_renew_date": "2022-07-29T16:36:32.069324"
  }
  ```

* * *

> Para uma requisição com `access_token` inválido:

- Request
  
  ```
  curl -A Mozila -H "Authorization: Bearer <access_token>" "https://apps.olx.com.br/autoupload/balance"
  ```
- Response
  
  ```
  HTTP/1.1 401 
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  {
      "reason": "ACCESS_DENIED", 
      "message": "Check the client authentication token."
  }
  ```

* * *

> Para um anunciante que não possui plano profissional ativo:

- Request
  
  ```
  curl -A Mozila -H "Authorization: Bearer <access_token>" "https://apps.olx.com.br/autoupload/balance"
  ```
- Reponse
  
  ```
  HTTP/1.1 410
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  {
      "reason": "PRODUCT_NOT_FOUND_BY_ACCOUNT", 
      "message": "Plan does not control limits."
  }
  ```