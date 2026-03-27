---
title: Agente concluído - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/webhook-agent-completed
source: sitemap
fetched_at: 2026-03-23T07:10:51.49033-03:00
rendered_js: false
word_count: 79
summary: This document describes the structure and expected response format for agent-completed webhook notifications, including security signature verification.
tags:
    - webhook-delivery
    - hmac-signature
    - data-payload
    - api-integration
    - security-verification
category: api
---

[Pular para o conteúdo principal](#content-area)

#### Cabeçalhos

Assinatura HMAC-SHA256 do corpo bruto da requisição, formatada como `sha256=<hex>`. Presente quando um segredo HMAC estiver configurado nas [configurações da sua conta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulte [Segurança de Webhooks](https://docs.firecrawl.dev/webhooks/security) para detalhes sobre a verificação.

Exemplo:

`"sha256=abc123def456789..."`

#### Corpo

Allowed value: `"agent.completed"`

Identificador único desta entrega de webhook.

O objeto de metadados personalizado que você forneceu na configuração do webhook. Ele é retornado em todas as entregas.

#### Resposta

Retorne qualquer código de status `2xx` para confirmar o recebimento.