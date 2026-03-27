---
title: Agente iniciado - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/webhook-agent-started
source: sitemap
fetched_at: 2026-03-23T07:16:57.672379-03:00
rendered_js: false
word_count: 99
summary: This document outlines the structure and signature verification requirements for webhook notifications, specifically detailing HMAC-SHA256 authentication and expected data fields.
tags:
    - webhook-security
    - hmac-signature
    - api-integration
    - data-delivery
    - security-verification
category: reference
---

[Saltar al contenido principal](#content-area)

#### Encabezados

Firma HMAC-SHA256 del cuerpo sin procesar de la solicitud, con el formato `sha256=<hex>`. Está presente cuando se configura un secreto HMAC en la [configuración de tu cuenta](https://www.firecrawl.dev/app/settings?tab=advanced). Consulta [Seguridad de webhooks](https://docs.firecrawl.dev/webhooks/security) para obtener más detalles sobre la verificación.

Ejemplo:

`"sha256=abc123def456789..."`

#### Cuerpo

Allowed value: `"agent.started"`

El ID del trabajo del agente, que coincide con el `id` devuelto por `POST /agent`.

Identificador único de esta entrega de webhook.

El objeto de metadatos personalizado que proporcionaste en la configuración del webhook. Se devuelve en cada entrega.

#### Respuesta

Devuelve cualquier código de estado `2xx` para confirmar la recepción.