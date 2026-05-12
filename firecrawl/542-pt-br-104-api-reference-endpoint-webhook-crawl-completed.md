---
title: Rastreamento concluído - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/webhook-crawl-completed
source: sitemap
fetched_at: 2026-03-23T07:11:06.15075-03:00
rendered_js: false
word_count: 102
summary: This document specifies the structure, security requirements, and expected response format for webhooks triggered upon the completion of a crawl job.
tags:
    - webhooks
    - api-integration
    - hmac-security
    - data-delivery
    - crawl-service
category: reference
---

[Pular para o conteúdo principal](#content-area)

#### Cabeçalhos

Assinatura HMAC-SHA256 do corpo bruto da requisição, formatada como `sha256=<hex>`. Presente quando um segredo HMAC estiver configurado nas [configurações da sua conta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulte [Segurança de Webhooks](https://docs.firecrawl.dev/webhooks/security) para detalhes sobre a verificação.

Exemplo:

`"sha256=abc123def456789..."`

#### Corpo

Sempre `true` para este evento.

O tipo do evento.

Allowed value: `"crawl.completed"`

O ID do job de rastreamento.

Identificador único desta entrega de webhook.

Array vazio. Recupere os resultados via `GET /crawl/{id}`.

O objeto de metadados personalizado que você forneceu na configuração do webhook. Ele é retornado em todas as entregas.

#### Resposta

Retorne qualquer código de status `2xx` para confirmar o recebimento.