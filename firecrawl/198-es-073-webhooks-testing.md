---
title: Pruebas de webhooks | Firecrawl
url: https://docs.firecrawl.dev/es/webhooks/testing
source: sitemap
fetched_at: 2026-03-23T07:38:47.654345-03:00
rendered_js: false
word_count: 169
summary: This document explains how to expose a local development server for testing webhooks using Cloudflare Tunnels and provides troubleshooting steps for common issues like delivery failures and signature verification errors.
tags:
    - webhooks
    - local-development
    - cloudflare-tunnels
    - webhook-troubleshooting
    - signature-verification
    - api-integration
category: guide
---

## Desarrollo local

Como los webhooks deben acceder a tu servidor desde Internet, tendrás que exponer públicamente tu servidor de desarrollo local.

### Uso de Cloudflare Tunnels

[Cloudflare Tunnels](https://github.com/cloudflare/cloudflared/releases) ofrece una forma gratuita de exponer tu servidor local sin necesidad de abrir puertos en el firewall:

```
cloudflared tunnel --url localhost:3000
```

Obtendrás una URL pública como `https://abc123.trycloudflare.com`. Utiliza esta URL en la configuración de tu webhook:

```
{
  "url": "https://abc123.trycloudflare.com/webhook"
}
```

## Resolución de problemas

### Los webhooks no llegan

- **Endpoint no accesible**: Comprueba que tu servidor sea accesible públicamente y que los firewalls permitan conexiones entrantes
- **Uso de HTTP**: Las URLs de webhook deben usar HTTPS
- **Eventos incorrectos**: Revisa el filtro de `events` en la configuración de tu webhook

### Error en la verificación de la firma

La causa más común es usar el cuerpo JSON ya parseado en lugar del cuerpo bruto de la solicitud.

```
// Incorrecto: usando el body parseado
const signature = crypto
  .createHmac('sha256', secret)
  .update(JSON.stringify(req.body))
  .digest('hex');

// Correcto: usando el body en crudo
app.use('/webhook', express.raw({ type: 'application/json' }));
app.post('/webhook', (req, res) => {
  const signature = crypto
    .createHmac('sha256', secret)
    .update(req.body) // Buffer en crudo
    .digest('hex');
});
```

### Otros problemas

- **Secreto incorrecto** - Verifica que estés usando la clave secreta correcta en la [configuración de tu cuenta](https://www.firecrawl.dev/app/settings?tab=advanced)
- **Errores de tiempo de espera (timeout)** - Asegúrate de que tu endpoint responda en menos de 10 segundos