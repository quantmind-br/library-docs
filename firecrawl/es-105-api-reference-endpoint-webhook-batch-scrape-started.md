---
title: Inicio del scraping por lotes - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/webhook-batch-scrape-started
source: sitemap
fetched_at: 2026-03-23T07:16:49.601714-03:00
rendered_js: false
word_count: 101
summary: This document outlines the structure and signature requirements for receiving and validating webhook events from the Firecrawl service.
tags:
    - webhook-security
    - hmac-signature
    - api-integration
    - event-delivery
    - data-scraping
category: reference
---

[Saltar al contenido principal](#content-area)

#### Encabezados

Firma HMAC-SHA256 del cuerpo sin procesar de la solicitud, con el formato `sha256=<hex>`. Está presente cuando se configura un secreto HMAC en la [configuración de tu cuenta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulta [Seguridad de webhooks](https://docs.firecrawl.dev/webhooks/security) para obtener más detalles sobre la verificación.

Ejemplo:

`"sha256=abc123def456789..."`

#### Cuerpo

Allowed value: `"batch_scrape.started"`

El ID del trabajo de extracción por lotes, que coincide con el `id` devuelto por `POST /batch/scrape`.

Identificador único de esta entrega de webhook.

El objeto de metadatos personalizado que proporcionaste en la configuración del webhook. Se devuelve en cada entrega.

#### Respuesta

Devuelve cualquier código de estado `2xx` para confirmar la recepción.