---
title: Consulta do status de Anúncios Publicados
url: https://developers.olx.com.br/anuncio/api/published_ads_status.html
source: crawler
fetched_at: 2026-02-07T15:17:07.714857932-03:00
rendered_js: false
word_count: 416
summary: This document provides technical specifications for the OLX API endpoint used to retrieve the current status, publication details, and error messages of a specific advertisement.
tags:
    - olx-api
    - ad-status
    - rest-api
    - authentication
    - json-response
    - http-get
    - error-handling
category: api
---

Esta API permite consultar o status atual de um anúncio publicado na OLX. Qual a vantagem?

## Requisição de Status

O cliente deve enviar uma requisição `GET`, informando o `list_id` no caminho da URL e deve conter o `token` de cada anunciante no header como: `Authorization: Bearer <token>`.

Exemplo de chamada para a URL `https://apps.olx.com.br/autoupload/ads/{list_id}`:

O `access_token` é necessário para autenticação e pode ser obtido conforme descrito na [documentação de Autenticação na API OLX](https://developers.olx.com.br/anuncio/api/anuncio/api/oauth.html).

ParâmetroTipoObrigatórioDescrição`access_token`stringSimChave de acesso do anunciante.

### Parâmetros de URL

ParâmetroTipoObrigatórioDescrição`list_id`1integerSimID do anúncio na OLX.

1 O `list_id` só é retornado quando o anúncio ja subiu pelo menos 1 vez na Plataforma da OLX. E pode ser recuperado das seguintes formas:

- Pela [Listagem de Publicação](https://developers.olx.com.br/anuncio/api/published_ads.html) que retorna todos os list\_id ja inseridos na conta do cliente.
- Ao fazer uma importação pela API, ao [Consulta de status da Importação](https://developers.olx.com.br/anuncio/api/publishing_status.html) temos o retorno do `list_id` quando a importação retornar com status `done` e com o status de cada anúncio está como `accepted` conforme no [Retorno Esperado](https://developers.olx.com.br/anuncio/api/published_ads_status.html#retorno-esperado)

```
curl --location --request GET 'https://apps.olx.com.br/autoupload/ads/1310831' \
--header 'authorization: Bearer access_token'
```

## Retorno Esperado

O formato do retorno de nosso servidor será do tipo JSON, que contém a seguinte estrutura:

ParâmetroValoresDescrição`status``pending`, `deleted`, `accepted`, `refused`Retorna o status dos anúncios.  
`pending`: o anúncio será processado.  
`deleted`: o anúncio foi removido  
`accepted`: o anúncio foi ativado. Caso a operação seja de deleção, significa que o anúncio foi deletado.  
`refused`: o anúncio não foi ativado`message`Exemplos: `REFUSED_GENERIC`Mensagens de aviso sobre erros ocorridos`url`stringUrl do anúncio gerada Olx1`last_update`timestampTimestamp (UTC) no formato ISO indicando a última atualização concluída feita no anúncio 2`list_id`stringRetorna o id do seu anúncio, caso o mesmo tenha sido aprovado`id`Regular expression: \[A-Za-z0-9\_{}-]{1,19}Identificador do anúncio definido pelo usuário

1 Para um anúncio novo, a url é gerada porém pode levar alguns minutos para aparecer no site.

2 Este timestamp é atualizado quando todas as etapas de importação ou edição forem concluídas. Enquanto houver alguma ação em execução, esse timestamp será correspondente da última atualização finalizada.

## Códigos e motivos de erros da requisição retornados

Status Code

NomeDescriçãoMensagem

`200`

OKSucessoDados referentes ao anúncio

`400`

Bad RequestFalta campo de `authorization` no header da requisição`{ "reason": "BAD_REQUEST", "message": "Check the header field(s)." }`

`401`

UnauthorizedToken inválido`{ "reason": "ACCESS_DENIED", "message": "Check the client authentication token." }`

`404`

Not FoundNOT FOUND

`429`

Rate Limit configurado quando o cliente fizer mais requisições por segundo do que deveriaRATE\_LIMITYou have exceeded the X requests in X seconds limit!

`500`

Internal Server ErrorErro interno inesperado`{ "reason": "UNEXPECTED_INTERNAL_ERROR", "message": "Unexpected internal error. Try again later." }`

## Exemplos de retorno:

Exemplo de retorno:

### Anúncio Pendente

```
{
    "status": "pending",
    "message": [],
    "url": "https://www.olx.com.br/vi/1234.htm",
    "last_update": "2024-07-05T11:08:27.843403",
    "list_id": "1234",
    "id": 9999
}
```

### Anúncio Removido

```
{
    "status": "deleted",
    "message": [],
    "url": "https://www.olx.com.br/vi/1234.htm",
    "last_update": "2024-07-05T11:08:27.843403",
    "list_id": "1234",
    "id": 9999
}
```

### Anúncio Aceito

```
{
    "status": "accepted",
    "message": [],
    "url": "https://www.olx.com.br/vi/1234.htm",
    "last_update": "2024-07-05T11:08:27.843403",
    "list_id": "1234",
    "id": 9999
}
```

### Anúncio Recusado

```
{
    "status": "refused",
    "message": [
        {
            "error": "REFUSED_GENERIC"
        }
    ],
    "url": "https://www.olx.com.br/vi/1234.htm",
    "last_update": "2024-07-05T11:08:27.843403",
    "list_id": "1234",
    "id": 9999
}
```