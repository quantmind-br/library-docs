---
title: Agente finalizado - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/webhook-agent-completed
source: sitemap
fetched_at: 2026-03-23T07:17:31.540922-03:00
rendered_js: false
word_count: 90
summary: This document describes the structure, authentication, and expected response format for webhooks sent by the Firecrawl platform.
tags:
    - webhook-delivery
    - hmac-security
    - api-integration
    - event-payload
    - request-verification
category: reference
---

[Saltar al contenido principal](#content-area)

#### Encabezados

Firma HMAC-SHA256 del cuerpo sin procesar de la solicitud, con el formato `sha256=<hex>`. Está presente cuando se configura un secreto HMAC en la [configuración de tu cuenta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulta [Seguridad de webhooks](https://docs.firecrawl.dev/webhooks/security) para obtener más detalles sobre la verificación.

Ejemplo:

`"sha256=abc123def456789..."`

#### Cuerpo

Allowed value: `"agent.completed"`

El ID del trabajo del agente.

Identificador único de esta entrega del webhook.

El objeto de metadatos personalizado que proporcionaste en la configuración del webhook. Se devuelve en cada entrega.

#### Respuesta

Devuelve cualquier código de estado `2xx` para confirmar la recepción.