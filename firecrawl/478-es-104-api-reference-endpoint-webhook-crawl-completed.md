---
title: Rastreo completado - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/webhook-crawl-completed
source: sitemap
fetched_at: 2026-03-23T07:17:08.407465-03:00
rendered_js: false
word_count: 108
summary: This document describes the structure and expected response format for webhook event notifications triggered by crawl completion jobs.
tags:
    - webhook
    - hmac-signature
    - event-notifications
    - api-integration
    - crawl-status
    - data-delivery
category: reference
---

[Saltar al contenido principal](#content-area)

#### Encabezados

Firma HMAC-SHA256 del cuerpo sin procesar de la solicitud, con el formato `sha256=<hex>`. Está presente cuando se configura un secreto HMAC en la [configuración de tu cuenta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulta [Seguridad de webhooks](https://docs.firecrawl.dev/webhooks/security) para obtener más detalles sobre la verificación.

Ejemplo:

`"sha256=abc123def456789..."`

#### Cuerpo

Siempre es `true` para este evento.

El tipo de evento.

Allowed value: `"crawl.completed"`

El ID del trabajo de rastreo.

Identificador único de esta entrega de webhook.

Array vacío. Recupera los resultados mediante `GET /crawl/{id}`.

El objeto de metadatos personalizado que proporcionaste en la configuración del webhook. Se devuelve en cada entrega.

#### Respuesta

Devuelve cualquier código de estado `2xx` para confirmar la recepción.