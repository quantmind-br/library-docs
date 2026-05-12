---
title: Seguridad de los webhooks | Firecrawl
url: https://docs.firecrawl.dev/es/webhooks/security
source: sitemap
fetched_at: 2026-03-23T07:38:55.2785-03:00
rendered_js: false
word_count: 165
summary: This document explains how to verify Firecrawl webhook signatures using HMAC-SHA256 to ensure data authenticity and prevent tampering.
tags:
    - webhooks
    - api-security
    - hmac-sha256
    - signature-verification
    - data-integrity
category: guide
---

Firecrawl firma todas las solicitudes de webhook mediante HMAC-SHA256. Verificar estas firmas garantiza que las solicitudes sean auténticas y no hayan sido manipuladas.

## Clave secreta

Tu secreto de webhook está disponible en la [pestaña Advanced](https://www.firecrawl.dev/app/settings?tab=advanced) de la configuración de tu cuenta. Cada cuenta tiene un secreto único que se utiliza para firmar todas las solicitudes de webhook.

## Verificación de firmas

Cada solicitud de webhook incluye un encabezado `X-Firecrawl-Signature`:

```
X-Firecrawl-Signature: sha256=abc123def456...
```

### Cómo verificar

1. Extrae la firma del encabezado `X-Firecrawl-Signature`
2. Obtén el cuerpo sin procesar de la solicitud (antes de analizarlo)
3. Calcula el HMAC-SHA256 usando tu clave secreta
4. Compara las firmas usando una función de comparación segura frente al tiempo

### Implementación

## Prácticas recomendadas

### Valida siempre las firmas

Nunca proceses un webhook sin verificar primero su firma:

```
app.post('/webhook', (req, res) => {
  if (!verifySignature(req)) {
    return res.status(401).send('No autorizado');
  }
  processWebhook(req.body);
  res.status(200).send('OK');
});
```

### Usa comparaciones seguras en tiempo constante

Las comparaciones de cadenas estándar pueden filtrar información por temporización. Usa `crypto.timingSafeEqual()` en Node.js o `hmac.compare_digest()` en Python.

### Usa HTTPS

Usa siempre un endpoint HTTPS para tu webhook para garantizar que los datos estén cifrados en tránsito.