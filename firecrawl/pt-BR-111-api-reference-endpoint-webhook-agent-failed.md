---
title: Falha do agente - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/webhook-agent-failed
source: sitemap
fetched_at: 2026-03-23T07:10:43.818945-03:00
rendered_js: false
word_count: 94
summary: This document defines the structure and requirements for the webhook event payload triggered when an agent process fails.
tags:
    - webhook
    - event-payload
    - api-integration
    - error-handling
    - hmac-signature
    - data-delivery
category: reference
---

[Pular para o conteúdo principal](#content-area)

#### Cabeçalhos

Assinatura HMAC-SHA256 do corpo bruto da requisição, formatada como `sha256=<hex>`. Presente quando um segredo HMAC estiver configurado nas [configurações da sua conta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulte [Segurança de Webhooks](https://docs.firecrawl.dev/webhooks/security) para detalhes sobre a verificação.

Exemplo:

`"sha256=abc123def456789..."`

#### Corpo

Sempre `false` para este evento.

Allowed value: `"agent.failed"`

Identificador único desta entrega de webhook.

Mensagem de erro legível por humanos que descreve a falha.

O objeto de metadados personalizado que você forneceu na configuração do webhook. Ele é retornado em todas as entregas.

#### Resposta

Retorne qualquer código de status `2xx` para confirmar o recebimento.