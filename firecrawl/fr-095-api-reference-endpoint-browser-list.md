---
title: Lister les sessions de navigateur - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/browser-list
source: sitemap
fetched_at: 2026-03-23T07:24:17.672554-03:00
rendered_js: false
word_count: 144
summary: This document provides technical documentation for the browser sessions API endpoint, detailing request parameters, response structures, and authentication requirements for retrieving session data.
tags:
    - api-documentation
    - browser-sessions
    - rest-api
    - authentication
    - session-management
    - web-scraping
category: api
---

[Passer au contenu principal](#content-area)

Lister les sessions de navigateur

En-têteValeur`Authorization``Bearer <API_KEY>`

## Paramètres de requête

ParamètreTypeObligatoireDescription`status`stringNonFiltre par statut de session : `"active"` ou `"destroyed"`

## Réponse

ChampTypeDescription`success`booleanIndique si la requête a réussi`sessions`arrayListe d’objets de session

### Objet de session

ChampTypeDescription`id`stringIdentifiant unique de la session`status`stringStatut actuel de la session (`"active"` ou `"destroyed"`)`cdpUrl`stringURL WebSocket pour les connexions CDP`liveViewUrl`stringURL pour afficher la session en temps réel`interactiveLiveViewUrl`stringURL pour interagir avec la session en temps réel (clic, saisie, défilement)`createdAt`stringHorodatage ISO 8601 de la création de la session`lastActivity`stringHorodatage ISO 8601 de la dernière activité

### Exemple de requête

```
curl -X GET "https://api.firecrawl.dev/v2/browser?status=active" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```

### Exemple de réponse

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
      "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true",
      "createdAt": "2025-06-01T12:00:00Z",
      "lastActivity": "2025-06-01T12:05:30Z"
    }
  ]
}
```

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de requête

Filtrer les sessions par statut

Options disponibles:

`active`,

`destroyed`

#### Réponse

Liste des sessions de navigateur