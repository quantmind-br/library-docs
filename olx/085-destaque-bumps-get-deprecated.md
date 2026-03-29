---
title: Consulta de anúncios destacados (deprecated)
url: https://developers.olx.com.br/destaque/bumps_get_deprecated.html
source: crawler
fetched_at: 2026-02-07T15:17:25.466225203-03:00
rendered_js: false
word_count: 403
summary: This document describes the legacy API endpoint for querying advertisement highlights (bumps), detailing request parameters, authentication requirements, and response structures.
tags:
    - olx-api
    - ad-highlights
    - bumps-api
    - legacy-version
    - endpoint-reference
    - api-integration
category: api
---

Dicas

Esta é a versão anterior da API de consulta de destaques. Para novas integrações, utilize a [versão atual por List ID](https://developers.olx.com.br/destaque/bumps_get.html).

A URL usada para fazer a requisição do arquivo JSON é https://apps.olx.com.br/autoupload/bump/ads?ad\_ids=\[{ad\_id},{ad\_id}], método `GET`. Essa requisição deve conter uma lista de até 10 identificadores de anúncios (separados por vírgula) e o `access_token` de cada anunciante no header como: `Authorization: Bearer <access_token>`.

> O campo `access_token` pode ser obtido seguindo a documentação [Autenticação na API olx.com.br](https://developers.olx.com.br/anuncio/api/oauth.html).

ParâmetroValoresObrigatórioDescrição`ad_id``array[string]`simLista de até 10 identificadores de anúncios.

**Obs:** se for enviada uma lista com mais de 10 identificadores, o 11º em diante será ignorado.

`access_token``string`simChave de acesso do anunciante

Se o anunciante possui anúncios destacados, a requisição retorna um `status code 200` e um JSON no corpo da resposta com a estrutura abaixo, podendo vir uma lista com até 10 itens:

## Retorno de sucesso esperado

ParâmetroValoresObrigatórioDescrição`id``string`simIdentificador do anúncio.`last_bumps``arrayOf[string (ISO Datetime)]`nãoÚltimas datas que o anúncio foi ao topo.`next_bumps``arrayOf[string (ISO Datetime)]`nãoPróximas datas agendadas para a volta do anúncio ao topo (ou seja, para a reaplicação do destaque).`reason``string`nãoMotivo do erro que ocorreu ao obter dados do anúncio específico.`message``string`nãoMensagem de erro que ocorreu ao obter dados do anúncio específico.

> A quantidade de datas retornadas nos campos *last\_bumps* e *next\_bumps*, dependerá do plano contratado, podendo ser de 1 a 5.

## Retorno de erro esperado

Caso ocorra algum erro ou o anunciante não possua plano profissional ativo, a consulta retorna um `status code > 400` e um JSON com o motivo e a mensagem do erro.

## Códigos e motivos de erros da requisição retornados

Status Code

Descrição

MotivoMensagem

`400`

Falta campo de `authorization` no header da requisiçãoBAD\_REQUESTCheck the header field(s)

`401`

Token inválidoACCESS\_DENIEDCheck the client authentication token

`429`

Rate Limit configurado quando o cliente fizer mais requisições por segundo do que deveriaRATE\_LIMITYou have exceeded the X requests in X seconds limit!

`500`

Erro interno inesperadoUNEXPECTED\_INTERNAL\_ERRORUnexpected internal error. Try again later

## Exemplos de retorno

> Consulta de 4 anúncios em situações diferentes, conforme condições abaixo:

AnúncioCondição do anúncio em relação a destaqueB124Todos os detaques aplicados e destaque ativo, ou seja, no período de 7 dias a partir da aplicação do destaque.D12342 datas de destaques ocorridas e 1 data ainda por ser aplicada e destaque ativo (no período de 7 dias a partir da aplicação do destaque).S995Sem destaque aplicado. Retornará Anúncio não encontrado.E4567Ocorreu uma indisponibilidade no momento da consulta deste anúncio. Por favor, tente mais tarde.

- Request
  
  ```
  curl "https://apps.olx.com.br/autoupload/bump/ads?ad_ids=B124,S995,D1234,E4567" -H "accept: application/json" -H "Content-Type: application/json" -H "authorization: Bearer {access_token}"
  ```
- Response
  
  ```
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  [
      {
          "id": "B124",
          "lastBumps": ['2022-09-01 00:00:00.00000', '2022-09-03 00:00:00.00000', '2022-09-05 00:00:00.00000'],
      },
      {
          "id": "D1234",
          "lastBumps": ['2022-09-04 00:00:00.00000', '2022-09-06 00:00:00.00000'],
          "nextBump": ['2022-09-08 00:00:00.00000']
      },
      {
          "id": "S995",
          "reason": "NOT_FOUND",
          "message": "Ad not found."
      },
      {
          "id": "E4567",
          "reason": "UNPROCESSABLE_AD",
          "message": "I couldn't get information for this ad. Please try again later"
      }
  ]
  ```

* * *

> Para uma requisição com `access_token` inválido:

- Request
  
  ```
  curl "https://apps.olx.com.br/autoupload/bump/ads?ad_ids=B124,S995,D1234,E4567" -H "accept: application/json" -H "Content-Type: application/json" -H "authorization: Bearer {access_token}"
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