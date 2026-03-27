---
title: Raspagem em lote iniciada - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/webhook-batch-scrape-started
source: sitemap
fetched_at: 2026-03-23T07:10:55.171014-03:00
rendered_js: false
word_count: 94
summary: This document specifies the structure and security requirements for receiving webhook notifications from the batch scrape service.
tags:
    - webhooks
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

Allowed value: `"batch_scrape.started"`

O ID do job de extração em lote, correspondente ao `id` retornado por `POST /batch/scrape`.

Identificador único desta entrega de webhook.

O objeto de metadados personalizado que você forneceu na configuração do webhook. Ele é retornado em todas as entregas.

#### Resposta

Retorne qualquer código de status `2xx` para confirmar o recebimento.