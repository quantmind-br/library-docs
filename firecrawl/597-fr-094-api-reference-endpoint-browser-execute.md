---
title: Exécuter du code dans le navigateur - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/browser-execute
source: sitemap
fetched_at: 2026-03-23T07:24:21.802128-03:00
rendered_js: false
word_count: 244
summary: This document provides the API specification for executing custom code within an isolated browser session via the Firecrawl browser execution endpoint.
tags:
    - api-documentation
    - browser-automation
    - code-execution
    - sandbox-environment
    - http-request
category: api
---

[Passer au contenu principal](#content-area)

Exécuter du code dans une session de navigateur

En-têteValeur`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Corps de la requête

ParamètreTypeObligatoireValeur par défautDescription`code`stringOui-Code à exécuter (1-100 000 caractères)`language`stringNon`"node"`Langage du code : `"python"`, `"node"` ou `"bash"` (pour les commandes CLI d’agent-browser)`timeout`numberNon-Durée maximale d’exécution en secondes (1-300)

## Réponse

ChampTypeDescription`success`booleanIndique si le code s’est exécuté avec succès`stdout`stringSortie standard de l’exécution du code`result`stringSortie standard de l’exécution du code`stderr`stringSortie d’erreur standard de l’exécution du code`exitCode`numberCode de sortie du processus exécuté`killed`booleanIndique si le processus a été interrompu en raison d’un dépassement de délai`error`stringMessage d’erreur si l’exécution a échoué (présent uniquement en cas d’échec)

### Exemple de requête

```
curl -X POST "https://api.firecrawl.dev/v2/browser/550e8400-e29b-41d4-a716-446655440000/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "await page.goto(\"https://example.com\")\ntitle = await page.title()\nprint(title)",
    "language": "python"
  }'
```

### Exemple de réponse (réussite)

```
{
  "success": true,
  "result": "Example Domain"
}
```

### Exemple de réponse (erreur)

```
{
  "success": true,
  "error": "TimeoutError: page.goto: Timeout 30000ms exceeded."
}
```

> Êtes-vous un agent d’IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

ID de la session de navigateur

#### Corps

Code à exécuter dans l’environnement isolé (sandbox) du navigateur

Required string length: `1 - 100000`

Langage du code à exécuter. Utilisez `node` pour JavaScript ou `bash` pour les commandes CLI d’agent-browser.

Options disponibles:

`python`,

`node`,

`bash`

Délai d’exécution maximal en secondes

Plage requise: `1 <= x <= 300`

#### Réponse

Sortie standard de l’exécution du code

Sortie standard (alias stdout)

Sortie d’erreur standard de l’exécution du code

Code de sortie du processus exécuté

Indique si le processus a été interrompu pour dépassement du temps limite

Message d’erreur si le code a déclenché une exception