---
title: Aplicação de destaque em anúncio
url: https://developers.olx.com.br/destaque/bumps_put.html
source: crawler
fetched_at: 2026-02-07T15:17:24.697682315-03:00
rendered_js: false
word_count: 711
summary: This document provides technical specifications for the OLX Highlights API, detailing how to apply 'bumps' to advertisements to increase their visibility on the platform.
tags:
    - olx-api
    - ad-highlighting
    - bump-ads
    - rest-api
    - oauth-authentication
    - error-codes
category: api
---

Versão Atual

Esta é a versão mais recente da API de Destaques. Para a versão antiga (deprecated), [clique aqui](https://developers.olx.com.br/destaque/bumps_put_deprecated.html).

## Aplicação de destaque em anúncio

A URL usada para fazer a requisição do arquivo JSON é https://apps.olx.com.br/autoupload/v1/bump/ad/{list\_id}, método `PUT`. Essa requisição deve conter o `token` de cada anunciante no header como: `Authorization: Bearer <token>`.

> O campo `token` pode ser obtido seguindo a documentação [Autenticação na API olx.com.br](https://developers.olx.com.br/anuncio/api/oauth.html).

**Path Parameter:**

ParâmetroValoresObrigatórioDescrição`list_id``string`simIdentificador único do anúncio (list\_id).

**Headers:**

ParâmetroValoresObrigatórioDescrição`Authorization``Bearer <token>`simToken de acesso do anunciante (obtido via OAuth)

Se o anunciante possui um plano profissional ativo e o destaque for aplicado, a requisição retorna um `status code 200` e um JSON no corpo da resposta com a estrutura:

## Retorno de sucesso esperado

ParâmetroValoresObrigatórioDescrição`next_bumps``arrayOf[string (ISO Datetime)]`simPróximas datas agendadas para a volta do anúncio ao topo (ou seja, para a reaplicação do destaque).

> A quantidade de datas retornadas no campo *next\_bumps*, dependerá do plano contratado, podendo ser de 1 a 5.

## Retorno de erro esperado

Caso ocorra algum erro ou o anunciante não possua plano profissional ativo, a consulta retorna um `status code >= 400` e um JSON com o motivo e a mensagem do erro.

## Códigos e motivos de erros da requisição retornados

Status Code

DescriçãoMotivoMensagem

`400`

Falta campo de `authorization` no header da requisiçãoBAD\_REQUESTCheck the header field(s)

`401`

Token inválidoACCESS\_DENIEDCheck the client authentication token

`403`

Cliente não tem saldo disponível para aplicar o destaqueFORBIDDEN`{ "reason": "FORBIDDEN", "message": "Forbidden." }`

`404`

Anúncio não encontradoNOT FOUND`{ "reason": "NOT_FOUND", "message": "Ad not found." }`

`422`

Bump já aplicadoBUMP\_ALREADY\_APPLIED\_OR\_NOT\_SYNCHRONIZED`{ "reason": "BUMP_ALREADY_APPLIED_OR_NOT_SYNCHRONIZED", "message": "Bump already applied or Ad not synchronized." }`

`429`

Rate Limit configurado quando o cliente fizer mais requisições por segundo do que o permitidoRATE\_LIMITYou have exceeded the X requests in X seconds limit!

`500`

Erro interno inesperadoUNEXPECTED\_INTERNAL\_ERRORUnexpected internal error. Try again later

## Exemplos de retorno - Versão v1

> Ao aplicar destaque, o anúncio terá sua visibilidade aumentada indo para o topo da listagem de anúncios e retornaremos uma lista de datas futuras onde o destaque será novamente aplicado no período de 7 dias.

- Request
  
  ```
  curl -X PUT "https://apps.olx.com.br/autoupload/v1/bump/ad/{list_id}" -H "accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {token}"
  ```
- Response
  
  ```
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  {
      "next_bumps": ["2022-09-01 00:00:00.00000", "2022-09-05 00:00:00.00000"]
  }
  ```

* * *

> Em caso de erro

- Request
  
  ```
  curl -X PUT "https://apps.olx.com.br/autoupload/v1/bump/ad/{list_id}" -H "accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {token}"
  ```
- Response
  
  ```
  HTTP/1.1 404
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  {
      "reason": "NOT_FOUND",
      "message": "Ad not found."
  }
  ```

* * *

> Para o anúncio que já foi dado destaque:

> *Obs: Uma vez o destaque aplicado e ativo, só será permitida a re-aplicação de novo destaque no anúncio após o prazo de **7 dias.***

- Request
  
  ```
  curl -X PUT "https://apps.olx.com.br/autoupload/v1/bump/ad/{list_id}" -H "accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {token}"
  ```
- Response
  
  ```
  HTTP/1.1 422
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  { 
      "reason": "BUMP_ALREADY_APPLIED_OR_NOT_SYNCHRONIZED", 
      "message": "Bump already applied or Ad not synchronized." 
  }
  ```

## Versão Anterior (Deprecated)

**Path Parameter:**

ParâmetroValoresObrigatórioDescrição`ad_id``string`simIdentificador do anúncio (external\_ad\_id do cliente).

**Headers:**

ParâmetroValoresObrigatórioDescrição`Authorization``Bearer <token>`simToken de acesso do anunciante (obtido via OAuth)

Se o anunciante possui um plano profissional ativo e o destaque for aplicado, a requisição retorna um `status code 200` e um JSON no corpo da resposta com a estrutura:

#### Retorno de sucesso esperado - Versão Anterior

ParâmetroValoresObrigatórioDescrição`next_bumps``arrayOf[string (ISO Datetime)]`simPróximas datas agendadas para a volta do anúncio ao topo (ou seja, para a reaplicação do destaque).

> A quantidade de datas retornadas no campo *next\_bumps*, dependerá do plano contratado, podendo ser de 1 a 5.

#### Retorno de erro esperado - Versão Anterior

Caso ocorra algum erro ou o anunciante não possua plano profissional ativo, a consulta retorna um `status code >= 400` e um JSON com o motivo e a mensagem do erro.

#### Códigos e motivos de erros da requisição retornados - Versão Anterior

Status Code

DescriçãoMotivoMensagem

`400`

Falta campo de `authorization` no header da requisiçãoBAD\_REQUESTCheck the header field(s)

`401`

Token inválidoACCESS\_DENIEDCheck the client authentication token

`403`

Cliente não tem saldo disponível para aplicar o destaqueFORBIDDEN`{ "reason": "FORBIDDEN", "message": "Forbidden." }`

`404`

Anúncio não encontradoNOT FOUND`{ "reason": "NOT_FOUND", "message": "Ad not found." }`

`422`

Bump já aplicadoBUMP\_ALREADY\_APPLIED\_OR\_NOT\_SYNCHRONIZED`{ "reason": "BUMP_ALREADY_APPLIED_OR_NOT_SYNCHRONIZED", "message": "Bump already applied or Ad not synchronized." }`

`429`

Rate Limit configurado quando o cliente fizer mais requisições por segundo do que o permitidoRATE\_LIMITYou have exceeded the X requests in X seconds limit!

`500`

Erro interno inesperadoUNEXPECTED\_INTERNAL\_ERRORUnexpected internal error. Try again later

#### Exemplos de retorno - Versão Anterior

> Ao aplicar destaque, o anúncio terá sua visibilidade aumentada indo para o topo da listagem de anúncios e retornaremos uma lista de datas futuras onde o destaque será novamente aplicado no período de 7 dias.

- Request
  
  ```
  curl -X PUT "https://apps.olx.com.br/autoupload/bump/ad/{ad_id}" -H "accept: application/json" -H "Content-Type: application/json" -H "authorization: Bearer {token}"
  ```
- Response
  
  ```
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  {
      "next_bumps": ["2022-09-01 00:00:00.00000", "2022-09-05 00:00:00.00000"]
  }
  ```

* * *

> Em caso de erro

- Request
  
  ```
  curl -X PUT "https://apps.olx.com.br/autoupload/bump/ad/{ad_id}" -H "accept: application/json" -H "Content-Type: application/json" -H "authorization: Bearer {token}"
  ```
- Response
  
  ```
  HTTP/1.1 404
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  {
      "reason": "NOT_FOUND",
      "message": "Ad not found."
  }
  ```

* * *

> Para uma requisição com `token` inválido:

- Request
  
  ```
  curl -A Mozila -H "Authorization: Bearer <token>" "https://apps.olx.com.br/autoupload/balance"
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

> Para o anúncio que já foi dado destaque:

> *Obs: Uma vez o destaque aplicado e ativo, só será permitida a re-aplicação de novo destaque no anúncio após o prazo de **7 dias.***

- Request
  
  ```
  curl -X PUT "https://apps.olx.com.br/autoupload/bump/ad/{ad_id}" -H "accept: application/json" -H "Content-Type: application/json" -H "authorization: Bearer {token}"
  ```
- Reponse
  
  ```
  HTTP/1.1 422
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  
  { 
      "reason": "BUMP_ALREADY_APPLIED_OR_NOT_SYNCHRONIZED", 
      "message": "Bump already applied or Ad not synchronized." 
  }
  ```