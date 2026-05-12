---
title: Sécurité des webhooks | Firecrawl
url: https://docs.firecrawl.dev/fr/webhooks/security
source: sitemap
fetched_at: 2026-03-23T07:38:25.979521-03:00
rendered_js: false
word_count: 173
summary: This document outlines the security procedures for verifying incoming webhook requests from Firecrawl using HMAC-SHA256 signatures.
tags:
    - webhooks
    - security
    - hmac-sha256
    - signature-verification
    - api-security
    - data-integrity
category: guide
---

Firecrawl signe chaque requête de webhook à l’aide du HMAC-SHA256. La vérification des signatures garantit que les requêtes sont authentiques et n’ont pas été altérées.

## Clé secrète

Le secret de votre webhook est disponible dans l’[onglet Avancé](https://www.firecrawl.dev/app/settings?tab=advanced) des paramètres de votre compte. Chaque compte dispose d’un secret unique utilisé pour signer toutes les requêtes webhook.

## Vérification de la signature

Chaque requête de webhook inclut un en-tête `X-Firecrawl-Signature` :

```
X-Firecrawl-Signature: sha256=abc123def456...
```

1. Extraire la signature de l’en-tête `X-Firecrawl-Signature`
2. Récupérer le corps brut de la requête (ne le parsez pas au préalable)
3. Calculer le HMAC-SHA256 avec votre clé secrète
4. Comparer les signatures à l’aide d’une fonction de comparaison à durée constante

### Implémentation

## Bonnes pratiques

### Toujours vérifier les signatures

Ne traitez jamais une requête de webhook sans avoir d’abord vérifié sa signature :

```
app.post('/webhook', (req, res) => {
  if (!verifySignature(req)) {
    return res.status(401).send('Accès non autorisé');
  }
  processWebhook(req.body);
  res.status(200).send('OK');
});
```

### Utilisez des comparaisons à temps constant

La comparaison de chaînes standard peut révéler des informations temporelles. Utilisez `crypto.timingSafeEqual()` dans Node.js ou `hmac.compare_digest()` en Python.

### Utiliser HTTPS

Utilisez toujours un point de terminaison HTTPS pour votre webhook afin de garantir que les données sont chiffrées en transit.