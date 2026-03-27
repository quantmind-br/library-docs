---
title: Créer une session de navigateur - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/browser-create
source: sitemap
fetched_at: 2026-03-23T07:24:24.890366-03:00
rendered_js: false
word_count: 305
summary: This document describes the API endpoint for creating and configuring remote browser sessions, including parameters for session duration, inactivity timeouts, and persistent storage profiles.
tags:
    - api-endpoint
    - browser-session
    - web-automation
    - cdp-integration
    - session-management
category: api
---

[Passer au contenu principal](#content-area)

Créer une session de navigateur

En-têteValeur`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Corps de la requête

ParamètreTypeObligatoireValeur par défautDescription`ttl`numberNon600Durée de vie totale de la session en secondes (30-3600)`activityTtl`numberNon300Nombre de secondes d’inactivité avant la destruction de la session (10-3600)`profile`objectNon—Active un stockage persistant d’une session à l’autre. Voir ci-dessous.`profile.name`stringOui\*—Nom du profil (1-128 caractères). Les sessions portant le même nom partagent le stockage.`profile.saveChanges`booleanNon`true`Lorsque `true`, l’état du navigateur est enregistré dans le profil à la fermeture. Définissez sur `false` pour charger les données existantes sans écriture. Un seul enregistreur est autorisé à la fois.

## Réponse

ChampTypeDescription`success`booleanIndique si la session a bien été créée`id`stringIdentifiant unique de la session`cdpUrl`stringURL WebSocket pour les connexions CDP`liveViewUrl`stringURL pour afficher la session en temps réel`interactiveLiveViewUrl`stringURL pour interagir avec la session en temps réel (clics, saisie, défilement)`expiresAt`stringDate d’expiration de la session en fonction du TTL

### Exemple de requête

```
curl -X POST "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "ttl": 120
  }'
```

### Exemple de réponse

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true"
}
```

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corps

Durée de vie totale de la session de navigateur, en secondes

Plage requise: `30 <= x <= 3600`

Temps en secondes avant la destruction de la session pour cause d’inactivité

Plage requise: `10 <= x <= 3600`

Indique s’il faut diffuser un flux en direct du navigateur

Activez la persistance du stockage entre les sessions du navigateur. Les données enregistrées lors d’une session peuvent être rechargées dans une session ultérieure en utilisant le même nom.

#### Réponse

Session de navigateur créée avec succès

Identifiant unique de la session

URL WebSocket pour accéder au protocole Chrome DevTools

URL permettant d’afficher la session de navigateur en temps réel

URL permettant d’interagir en temps réel avec la session du navigateur (clic, saisie, défilement)

Date et heure d’expiration de la session en fonction du TTL