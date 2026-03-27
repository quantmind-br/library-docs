---
title: Crawl iniciado - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/webhook-crawl-started
source: sitemap
fetched_at: 2026-03-23T07:10:57.336781-03:00
rendered_js: false
word_count: 118
summary: This document defines the webhook event structure for crawl job initiation, detailing the required headers, payload fields, and expected response codes.
tags:
    - webhook
    - api-reference
    - event-schema
    - hmac-security
    - crawl-service
category: api
---

[Pular para o conteúdo principal](#content-area)

#### Cabeçalhos

Assinatura HMAC-SHA256 do corpo bruto da requisição, formatada como `sha256=<hex>`. Presente quando um segredo HMAC estiver configurado nas [configurações da sua conta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulte [Segurança de Webhooks](https://docs.firecrawl.dev/webhooks/security) para detalhes sobre a verificação.

Exemplo:

`"sha256=abc123def456789..."`

#### Corpo

Sempre `true` para este evento.

O tipo do evento.

Allowed value: `"crawl.started"`

O ID do job de rastreamento, correspondente ao `id` retornado por `POST /crawl`.

Identificador único desta entrega de webhook. Use para deduplicação — o mesmo valor é enviado em novas tentativas.

Array vazio para este evento.

O objeto de metadados personalizado que você forneceu na configuração do webhook. Ele é retornado em todas as entregas.

#### Resposta

Retorne qualquer código de status `2xx` para confirmar o recebimento.