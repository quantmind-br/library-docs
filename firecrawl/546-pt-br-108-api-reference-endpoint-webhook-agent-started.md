---
title: Agente iniciado - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/webhook-agent-started
source: sitemap
fetched_at: 2026-03-23T07:10:56.727446-03:00
rendered_js: false
word_count: 92
summary: This document specifies the structure and security requirements for webhooks, including the HMAC-SHA256 signature header and the expected request body format for agent jobs.
tags:
    - webhooks
    - api-integration
    - security
    - hmac
    - webhook-payload
category: api
---

[Pular para o conteúdo principal](#content-area)

#### Cabeçalhos

Assinatura HMAC-SHA256 do corpo bruto da requisição, formatada como `sha256=<hex>`. Presente quando um segredo HMAC estiver configurado nas [configurações da sua conta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulte [Segurança de Webhooks](https://docs.firecrawl.dev/webhooks/security) para detalhes sobre a verificação.

Exemplo:

`"sha256=abc123def456789..."`

#### Corpo

Allowed value: `"agent.started"`

O ID do job do agente, correspondente ao `id` retornado por `POST /agent`.

Identificador único desta entrega de webhook.

O objeto de metadados personalizado que você forneceu na configuração do webhook. Ele é retornado em todas as entregas.

#### Resposta

Retorne qualquer código de status `2xx` para confirmar o recebimento.