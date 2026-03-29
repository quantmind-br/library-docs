---
title: Renovação de Anúncios
url: https://developers.olx.com.br/renewals/renewals_deprecated.html
source: crawler
fetched_at: 2026-02-07T15:17:22.966064785-03:00
rendered_js: false
word_count: 371
summary: This document describes the API endpoint for programmatically renewing expired advertisements, detailing request parameters, response structures, and error handling.
tags:
    - olx-api
    - ad-renewal
    - patch-request
    - ads-management
    - integration
    - error-handling
category: api
---

## Documentação para a Renovação de Anúncios

A **Renovação de Anúncios** permite que os anunciantes renovem seus anúncios, sem precisar acessar manualmente a interface `Meus Anúncios`. Com essa funcionalidade, é possível reativar anúncios expirados, mantendo o histórico e o identificador original do anúncio.

## Como Funciona a Renovação de Anúncios?

A renovação de anúncios é feita por meio de uma requisição `PATCH` para a rota `https://apps.olx.com.br/autoupload/ads/renewals`, na qual é possível renovar um ou mais anúncios de acordo com a necessidade.

### Exemplo de Requisição

```
curl --location --request PATCH 'https://apps.olx.com.br/autoupload/ads/renewals' \
--header 'Content-Type: application/json' \
--header 'x-correlation-id: 123450987' \
--header 'Authorization: <access_token>' \
--data '{
    "ids": [
        "123456789",
        "987654321",
        "112233445"
    ]
}'
```

#### Parâmetros da Requisição

ParâmetroValoresObrigatórioDescrição`ids``array`simLista com os identificadores dos anúncios a serem renovados (de 1 a 100 anúncios)`access_token``string`simToken de autenticação

## Respostas da Requisição

A resposta indica que a renovação foi processada, e a quantidade de anúncios renovados com sucesso ou que apresentaram falha.

```
{
  "result": {
    "123456789": { "reason": "AD_NOT_FOUND", "message": "Ad not found." },
    "987654321": { "renewed": true },
    "112233445": { "renewed": true }
  },
  "meta": {
    "success": 2,
    "failed": 1
  }
}
```

Campos da Resposta:

CampoTipoDescrição`result``object`Contém os resultados individuais para cada anúncio`meta``object`Contém um resumo do total de sucessos e falhas`result.<id>``object`Status de renovação para cada anúncio com o `id` especificado`meta.success``integer`Número de anúncios renovados com sucesso`meta.failed``integer`Número de anúncios que falharam na renovação

### Resposta bem-sucedida

O status `"renewed": true` indica que o anúncio foi renovado com sucesso.

```
{
  "987654321": { "renewed": true }
}
```

### Resposta de erro (dentro do objeto `result`)

O campo `reason` indica que ocorreu um erro ao tentar renovar o anúncio. O campo `message` fornecerá mais detalhes sobre a falha.

```
{
  "123456789": { "reason": "AD_NOT_FOUND", "message": "Ad not found." }
}
```

> No exemplo acima, o erro foi causado porque o anúncio com o id 123456789 não foi encontrado.

```
{
  "123456789": { "reason": "AD_NOT_EXPIRED", "message": "Ad not expired." }
}
```

> No exemplo acima, o erro foi causado porque o anúncio com o id 123456789 não está expirado.

### Observações

- O campo `result` inclui a resposta para cada anúncio individualmente. Se a renovação de um anúncio falhar, o motivo estará descrito em `reason` e `message`.
- O campo `meta` apresenta um resumo de como a operação foi executada, mostrando quantos anúncios foram renovados com sucesso e quantos falharam, caso houver.

### Outros Erros de Resposta (HTTP Status Codes)

Além dos erros específicos por anúncio dentro de uma resposta bem-sucedida (HTTP 200), a API pode retornar os seguintes erros HTTP:

Este erro ocorre se o `access_token` não for fornecido, for inválido ou expirado.

```
{
    "reason": "ACCESS_TOKEN_NOT_FOUND",
    "message": "Check the client authentication token."
}
```

#### Erro 400 - Bad Request

Este erro pode ocorrer se houver um problema com a formatação da requisição, como um JSON inválido no corpo da requisição ou cabeçalhos ausentes/malformatados.

```
{
    "reason": "BAD_REQUEST",
    "message": "Check the header field(s)."
}
```

## Dúvidas e Sugestões

Se tiver dificuldades ou sugestões, entre em contato com: [suporteintegrador@olxbr.com](mailto:suporteintegrador@olxbr.com)