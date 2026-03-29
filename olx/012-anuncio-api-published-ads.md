---
title: Listagem de Publicação
url: https://developers.olx.com.br/anuncio/api/published_ads.html
source: crawler
fetched_at: 2026-02-07T15:17:06.859502378-03:00
rendered_js: false
word_count: 587
summary: This document describes the OLX Publication Listing API, detailing how to systematically retrieve and manage advertisement data through status filtering and pagination.
tags:
    - olx-api
    - listing-api
    - pagination
    - ad-management
    - api-reference
    - json-api
category: api
---

A API de Listagem de Publicações tem como principal responsabilidade fornecer ao anunciante uma visão completa e atualizada de todos os seus anúncios na plataforma OLX. Ela foi projetada para permitir a recuperação sistemática de dados, oferecendo controle e flexibilidade na consulta.

- Consulta Abrangente de Status: A consulta não se limita apenas a anúncios ativos. Ela abrange todo o ciclo de vida de um anúncio, retornando registros com diversos status, como `published` (publicados/ativos), `pending_review` (aguardando aprovação), `deleted` (removidos) e `refused` (recusados). Isso permite um monitoramento completo do inventário.
- Paginação Eficiente: Para lidar com grandes volumes de dados de forma performática, a API implementa um sistema de paginação robusto. A navegação entre as páginas de resultados é controlada pelo page\_token (enviado na requisição para buscar uma página específica) e pelo `next_token` (recebido na resposta, que contém o identificador para a próxima página). Se o `next_token` retornar nulo, significa que não há mais resultados.
- Busca customizável: A consulta pode ser refinada utilizando parâmetros, como filtrar os anúncios por um status específico (`ads_status`) ou definir a quantidade de resultados por página (`fetch_size`), dando ao desenvolvedor maior controle sobre os dados retornados.

Em resumo, esta API é a ferramenta central para que um anunciante possa sincronizar, auditar e gerenciar programaticamente o estado de todos os seus anúncios publicados na OLX.

## Parâmetros de request

A URL usada para fazer a requisição do arquivo JSON é https://apps.olx.com.br/autoupload/v1/published, método `GET`. Essa requisição deve conter o `access_token` de cada anunciante no header como: `Authorization: Bearer <access_token>`. Com scope de `autoupload` ou `basic_user_info`

> O campo `access_token` pode ser obtido seguindo a documentação [Autenticação na API olx.com.br](https://developers.olx.com.br/anuncio/api/oauth.html).

Exemplo de chamada para a URL https://apps.olx.com.br/autoupload/v1/published e possíveis querys params:

```
curl --location 'https://apps.olx.com.br/autoupload/v1/published?page_token=YUV6cmwwWENKWl82UFE4VGg6OjoxNzQ5ODcxNTExMDgz&ads_status=published&fetch_size=10' \
--header 'Authorization: Bearer <access_token>'
```

ParâmetroObrigatórioDescrição`page_token`nãoHash da próxima página a ser pesquisada`ads_status`nãoStatus específico que a busca irá retornar`fetch_size`nãoQuantidade de dados por página, o default e máximo são 200 por página

## Retorno de sucesso esperado

Se o anunciante possui anúncios na conta, a consulta retornará o `status code 200` e um JSON no corpo da resposta com a seguinte estrutura:

ParâmetroValoresObrigatórioDescrição`data``array`simArray que irá conter os dados listados abaixo, pode vir vazio quando não tiver mais registros (retorna no máximo de 200 registros por página)`id``string`simIdentificador do anúncio definido pelo usuário`list_id``string`nãoid do anúncio na OLX, esse id quando não aparecer significa que é um anúncio novo que nunca foi publicado e está em fase de aprovação`status``string`simRetorna o status público do anúncio que é o mesmo que está na OLX. Valores possiveis `pending_review`, `published`, `deleted`, `refused`. A esta lista podem ser acrescentados novos valores, ou alguns podem deixar de existir no futuro.`current_token``string`nãoPágina atual dos dados`next_token``string`nãoValor hash para a proxima página de dados usando `page_token` por query params da requisição, caso não haja mais dados para buscar retornará null

Exemplo de retorno da primeira página:

```
{
    "data": [
        {
            "id": "1B",
            "list_id": "129987",
            "status": "pending_review"
        },
        {
            "id": "2B",
            "list_id": "129989",
            "status": "published"
        },
        {
            "id": "3B",
            "list_id": "129980",
            "status": "deleted"
        }
    ],
    "current_token": null,
    "next_token": "YUhvdTNxMHE4VXFBZ1A5THg6OjoxNzUyODM3ODU0MTg2"
}
```

Exemplo de retorno da segunda página e assim por diante:

```
{
    "data": [
        {
            "id": "4B",
            "list_id": "129865",
            "status": "pending_review"
        },
        {
            "id": "9B",
            "list_id": "12965",
            "status": "published"
        },
        {
            "id": "88B",
            "list_id": "129873",
            "status": "deleted"
        }
    ],
    "current_token": "YUhvdTNxMHE4VXFBZ1A5THg6OjoxNzUyODM3ODU0MTg2",
    "next_token": "IJigaiIHBygIIUGdTU6GKBJOIUjdrda193hojnag2"
}
```

Retorno quando é a última página

```
{
    "data": [
        {
            "id": "12B",
            "list_id": "12938",
            "status": "published"
        }
    ],
    "current_token": "IJigaiIHBygIIUGdTU6GKBJOIUjdrda193hojnag2",
    "next_token": null
}
```

Retorno quando é a última página com retorno vazio em data

```
{
    "data": [
    ],
    "current_token": "IJigaiIHBygIIUGdTU6GKBJOIUjdrda193hojnag2",
    "next_token": null
}
```

## Retorno de erro esperado

Caso ocorra algum erro, a consulta retorna um `status code > 200` e um JSON com o motivo e a mensagem do erro.

### Códigos e motivos de erros da requisição retornados

Status Code

DescriçãoMotivoMensagem

`400`

Falta campo `authorization` no header da requisiçãoBAD\_REQUESTCheck the header field(s)

`401`

Token inválido ou scope não permitidoACCESS\_DENIED ACCESS\_SCOPE\_DENIEDCheck the client authentication token Check the client authentication if scope configuration is correct.

`429`

Rate Limit configurado quando o cliente faz mais requisições por segundo do que o permitidoRATE\_LIMITYou have exceeded the X requests in X seconds limit!

`500`

Erro interno inesperadoUNEXPECTED\_INTERNAL\_ERRORUnexpected internal error. Try again later

Exemplo de retorno:

```
{
    "reason": "ACCESS_SCOPE_DENIED",
    "message": "Check the client authentication if scope configuration is correct."
}
```