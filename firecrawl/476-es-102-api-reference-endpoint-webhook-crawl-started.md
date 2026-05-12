---
title: Rastreo iniciado - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/webhook-crawl-started
source: sitemap
fetched_at: 2026-03-23T07:17:04.250462-03:00
rendered_js: false
word_count: 126
summary: This document outlines the webhook payload structure and security requirements for a crawl-started event notification.
tags:
    - webhook-payload
    - hmac-security
    - crawl-event
    - data-integration
    - api-documentation
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

Allowed value: `"crawl.started"`

El ID del trabajo de rastreo, que coincide con el `id` devuelto por `POST /crawl`.

Identificador único de esta entrega de webhook. Úsalo para la deduplicación: se envía el mismo valor en los reintentos.

Array vacío para este evento.

El objeto de metadatos personalizado que proporcionaste en la configuración del webhook. Se devuelve en cada entrega.

#### Respuesta

Devuelve cualquier código de estado `2xx` para confirmar la recepción.