---
title: Tests des webhooks | Firecrawl
url: https://docs.firecrawl.dev/fr/webhooks/testing
source: sitemap
fetched_at: 2026-03-23T07:38:22.118182-03:00
rendered_js: false
word_count: 170
summary: This document provides instructions for exposing local development servers to the internet using Cloudflare Tunnels and troubleshooting common issues related to webhook connectivity and signature verification.
tags:
    - webhooks
    - local-development
    - cloudflare-tunnels
    - signature-verification
    - debugging
    - api-integration
category: guide
---

## Développement local

Étant donné que les webhooks doivent accéder à votre serveur depuis Internet, vous devrez rendre votre serveur de développement local accessible publiquement.

### Utiliser Cloudflare Tunnels

[Cloudflare Tunnels](https://github.com/cloudflare/cloudflared/releases) offre un moyen gratuit d’exposer votre serveur local sans ouvrir de ports sur le pare-feu :

```
cloudflared tunnel --url localhost:3000
```

Vous obtiendrez une URL publique de la forme `https://abc123.trycloudflare.com`. Utilisez-la dans la configuration de votre webhook :

```
{
  "url": "https://abc123.trycloudflare.com/webhook"
}
```

## Résolution des problèmes

### Les webhooks n’arrivent pas

- **Endpoint inaccessible** - Vérifiez que votre serveur est accessible publiquement et que les pare-feu autorisent les connexions entrantes
- **Utilisation de HTTP** - Les URL de webhook doivent utiliser HTTPS
- **Mauvais types d’événements** - Vérifiez le filtre `events` dans la configuration de votre webhook

### Échec de la vérification de la signature

La cause la plus fréquente est l’utilisation du corps JSON parsé au lieu du corps brut de la requête.

```
// ❌ Incorrect — utilisation du corps parsé
const signature = crypto
  .createHmac('sha256', secret)
  .update(JSON.stringify(req.body))
  .digest('hex');

// ✅ Correct — utilisation du corps brut
app.use('/webhook', express.raw({ type: 'application/json' }));
app.post('/webhook', (req, res) => {
  const signature = crypto
    .createHmac('sha256', secret)
    .update(req.body) // Buffer brut
    .digest('hex');
});
```

### Autres problèmes

- **Mauvais secret** - Vérifiez que vous utilisez le bon secret depuis vos [paramètres de compte](https://www.firecrawl.dev/app/settings?tab=advanced)
- **Erreurs de délai d’attente** - Assurez-vous que votre endpoint répond en moins de 10 secondes