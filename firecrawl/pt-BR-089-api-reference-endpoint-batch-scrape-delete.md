---
title: Cancelar raspagem em lote - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:11:52.420876-03:00
rendered_js: false
word_count: 79
summary: This document provides the API endpoint and authorization requirements for canceling a batch scraping job using the Firecrawl service.
tags:
    - api-endpoint
    - batch-scraping
    - job-cancellation
    - firecrawl-api
    - rest-api
category: api
---

[Pular para o conteúdo principal](#content-area)

Cancelar um job de raspagem em lote

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

Cancelar um job de raspagem em lote

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instruções automatizadas de integração inicial.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

ID do job de raspagem em lote

#### Resposta

Cancelamento concluído com sucesso

Exemplo:

`"Batch scrape job successfully cancelled."`