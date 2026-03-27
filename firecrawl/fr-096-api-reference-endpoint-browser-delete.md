---
title: Supprimer une session de navigateur - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/browser-delete
source: sitemap
fetched_at: 2026-03-23T07:24:29.398094-03:00
rendered_js: false
word_count: 99
summary: This document describes the API endpoint for terminating an active browser session by providing its unique session identifier.
tags:
    - api-endpoint
    - browser-session
    - session-management
    - delete-request
    - firecrawl-api
category: api
---

[Passer au contenu principal](#content-area)

Supprimer une session de navigateur

En-têteValeur`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Corps de la requête

ParamètreTypeObligatoireDescription`id`stringOuiL’identifiant de session à détruire

## Réponse

ChampTypeDescription`success`booleanIndique si la session a été détruite avec succès

### Exemple de requête

```
curl -X DELETE "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }'
```

### Exemple de réponse

> Êtes-vous un agent IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

ID de session du navigateur

#### Réponse

Session de navigateur supprimée avec succès

Durée totale de la session (en millisecondes)

Nombre de crédits facturés pour la session