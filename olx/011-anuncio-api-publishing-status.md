---
title: Consulta de status da Importação
url: https://developers.olx.com.br/anuncio/api/publishing_status.html
source: crawler
fetched_at: 2026-02-07T15:17:07.892159429-03:00
rendered_js: false
word_count: 425
summary: Explains how to query the publication status of ads after an import process on the OLX platform, detailing request requirements and JSON response structures.
tags:
    - olx-api
    - publication-status
    - ad-import
    - autoupload
    - api-reference
    - error-handling
category: api
---

## Status de Publicação

Depois da importação, os anúncios vão para a fila de importação da OLX para serem processados. Essa consulta retorna a confirmação de inserção do anúncio com sucesso, bem como informa e detalha um eventual erro no processo de importação de um anúncio.  
Essa consulta de importação, lembrando que é o status daquela versão do anúncio por importação, ou seja, para uma atualização feita do anuncio, é criado um outro token. Caso o cliente OLX faça uma deleção ou alteração na OLX, não será refletido no mesmo token. Utilize a [Consulta do status de Anúncios Publicados](https://developers.olx.com.br/anuncio/api/published_ads_status.html)

## Requisição de Status

A URL usada para fazer a requisição do arquivo JSON: https://apps.olx.com.br/autoupload/import/{token}. O `token` a ser inserido no final da URL é o retorno mencionado na importação.

A requisição feita para esta URL deve conter o `access_token` de cada anunciante, usando o método `POST`:

```
{
     "access_token": "37812426ab5961d8a029b224b8e1288e192062ef"
}
```

## Retorno Esperado

O formato do retorno de nosso servidor será do tipo JSON, que contém a seguinte estrutura:

ParâmetroValoresDescrição`autoupload_status``done`, `pending`Retorna o status dos anúncios. `done`: todos os anúncios foram processados (inseridos ou deletados) `pending`: Pelo menos um anúncio ainda está na fila de importação`ads`array\[]Este parâmetro detalha o resultado de publicação de determinado anúncio, seguindo a descrição da tabela abaixo.

A tabela abaixo detalha o retorno do parâmetro `ads`, que de fato explica o que houve com o anúncio em si:

ParâmetroValoresDescrição`status``pending`, `error`, `queued`, `accepted`, `refused`Retorna o status dos anúncios.  
`pending`: o anúncio será processado.  
`error`: o anúncio está com erro(s).  
`queued`: o anúncio foi inserido e será ativado em breve  
`accepted`: o anúncio foi ativado. Caso a operação seja de deleção, significa que o anúncio foi deletado.  
`refused`: o anúncio não foi ativado`operation``insert`, `delete`Operação utilizada  
`insert`: inserção de anúncio  
`delete`: deleção de anúncio`message`Exemplos: `ERROR_IMAGE_TOO_SMALL`,  
`ERROR_DOWNLOADING_IMAGE`,  
`ERROR_UPLOADING_IMAGE`,  
`NOT_ENOUGH_AD_SLOTS`,  
`REFUSED_SUSPECT_CATEGORY`,  
`REFUSED_SUSPECT_REGION`,  
`REFUSED_DENOUNCE`,  
`REFUSED_SUSPECT_AUTOS`,  
`REFUSED_SUSPECT_DUPLICATES`,  
`REFUSED_GENERIC`Mensagens de aviso sobre erros ocorridos`list_id`stringRetorna o id do seu anúncio, caso o mesmo tenha sido aprovado 1`url`stringUrl do anúncio gerada Olx2

1 *ATENÇÃO*, é uma sugestão de armazenar esse campo `list_id` qualquer outra funcionalidade por API é o valor a ser utilizado.

2 Para um anúncio novo, a url é gerada porém pode levar alguns minutos para aparecer no site.

## Exemplos de retorno:

Para um anúncio inserido ou editado, que ainda não entrou na fila de ativação:

```
{
    "autoupload_status": "pending",
    "ads": {
        "1111111111": {
            "status": "pending",
            "operation": "insert"
        }
    }
}
```

Para um anúncio editado antes de ter sido ativado:

```
{
    "autoupload_status": "pending",
    "ads": {
        "1111111111": {
            "status": "queued",
            "operation": "edit",
            "list_id": "8000000",
            "message": []
        }
    }
}
```

Para anúncio inserido e aguardando ativação:

```
{
    "autoupload_status": "pending",
    "ads": {
        "1111111111": {
            "status": "queued",
            "operation": "insert",
            "message": []
        }
    }
}
```

Para um anúncio inserido com sucesso:

```
{
    "autoupload_status": "done",
    "ads": {
        "1111111111": {
            "status": "accepted",
            "operation": "insert",
            "message": [],
            "url": "http://www.olx.com.br/vi/8000005.htm"
        }
    }
}
```

Para um anúncio que não foi inserido por algum motivo:

```
{
    "autoupload_status": "done",
    "ads": {
        "1111111111": {
            "status": "refused",
            "operation": "insert",
            "message": [
                {
                    "error": "REFUSED_SUSPECT_PRICE"
                }
            ]
        }
    }
}
```

Para um anúncio editado com sucesso:

```
{
    "autoupload_status": "done",
    "ads": {
        "1111111111": {
            "status": "accept",
            "operation": "edit",
            "list_id": "8000000",
            "message": [],
            "url": "http://www.olx.com.br/vi/8000005.htm"
        }
    }
}
```

Para um anúncio que teve uma edição recusada:

```
{
    "autoupload_status": "done",
    "ads": {
        "1111111111": {
            "status": "refused",
            "operation": "edit",
            "message": [
                {
                    "error": "REFUSED_SUSPECT_DUPLICATES"
                }
            ]
        }
    }
}
```

Para um anúncio removido com sucesso:

```
{
    "autoupload_status": "done",
    "ads": {
        "1111111111": {
            "status": "accepted",
            "operation": "delete",
            "message": []
        }
    }
}
```