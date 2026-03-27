---
title: Acción del agente - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/webhook-agent-action
source: sitemap
fetched_at: 2026-03-23T07:17:07.554668-03:00
rendered_js: false
word_count: 100
summary: This document specifies the structure, security requirements, and expected response format for webhook events in the Firecrawl platform.
tags:
    - webhook-security
    - hmac-signature
    - api-integration
    - event-payload
    - webhook-configuration
category: reference
---

[Saltar al contenido principal](#content-area)

#### Encabezados

Firma HMAC-SHA256 del cuerpo sin procesar de la solicitud, con el formato `sha256=<hex>`. Está presente cuando se configura un secreto HMAC en la [configuración de tu cuenta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulta [Seguridad de webhooks](https://docs.firecrawl.dev/webhooks/security) para obtener más detalles sobre la verificación.

Ejemplo:

`"sha256=abc123def456789..."`

#### Cuerpo

Allowed value: `"agent.action"`

El ID del trabajo del agente.

Identificador único de esta entrega de webhook.

Array con un único objeto que describe la acción realizada.

El objeto de metadatos personalizado que proporcionaste en la configuración del webhook. Se devuelve en cada entrega.

#### Respuesta

Devuelve cualquier código de estado `2xx` para confirmar la recepción.