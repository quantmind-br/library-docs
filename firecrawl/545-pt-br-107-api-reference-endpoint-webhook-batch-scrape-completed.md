---
title: Raspagem em lote concluída - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/webhook-batch-scrape-completed
source: sitemap
fetched_at: 2026-03-23T07:10:39.600908-03:00
rendered_js: false
word_count: 95
summary: This document outlines the structure and signature requirements for webhooks delivered upon the completion of batch scraping jobs.
tags:
    - webhook-payload
    - hmac-signature
    - batch-scraping
    - api-integration
    - data-delivery
category: reference
---

[Pular para o conteúdo principal](#content-area)

#### Cabeçalhos

Assinatura HMAC-SHA256 do corpo bruto da requisição, formatada como `sha256=<hex>`. Presente quando um segredo HMAC estiver configurado nas [configurações da sua conta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulte [Segurança de Webhooks](https://docs.firecrawl.dev/webhooks/security) para detalhes sobre a verificação.

Exemplo:

`"sha256=abc123def456789..."`

#### Corpo

Allowed value: `"batch_scrape.completed"`

O ID do job de extração em lote.

Identificador único desta entrega de webhook.

Array vazio. Recupere os resultados via `GET /batch/scrape/{id}`.

O objeto de metadados personalizado que você forneceu na configuração do webhook. Ele é retornado em todas as entregas.

#### Resposta

Retorne qualquer código de status `2xx` para confirmar o recebimento.