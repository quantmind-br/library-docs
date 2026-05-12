---
title: Introduction - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/v1/api-reference/introduction
source: sitemap
fetched_at: 2026-03-23T07:38:25.689672-03:00
rendered_js: false
word_count: 177
summary: This document provides the foundational technical information for integrating with the Firecrawl API, including base URL, authentication methods, HTTP status codes, and rate limiting policies.
tags:
    - api-basics
    - authentication
    - http-status-codes
    - rate-limiting
    - api-documentation
category: reference
---

## Fonctionnalités

## Fonctions agentiques

## URL de base

Toutes les requêtes utilisent l’URL de base suivante :

```
https://api.firecrawl.dev
```

## Authentification

Pour s’authentifier, vous devez inclure un en-tête Authorization. Cet en-tête doit contenir `Bearer fc-123456789`, où `fc-123456789` correspond à votre clé d’API.

```
Authorization: Bearer fc-123456789
```

​

## Codes de réponse

Firecrawl utilise des codes d’état HTTP standard pour indiquer l’issue de vos requêtes. En général, les codes d’état HTTP 2xx indiquent une réussite, les codes 4xx des erreurs côté client, et les codes 5xx des problèmes d’infrastructure.

StatusDescription200Requête effectuée avec succès.400Vérifiez l’exactitude des paramètres.401La clé API n’a pas été fournie.402Paiement requis404La ressource demandée est introuvable.429La limite de débit a été dépassée.5xxIndique une erreur serveur chez Firecrawl.

Reportez-vous à la section Error Codes pour une explication détaillée de toutes les erreurs API possibles. ​

## Limite de débit

L’API Firecrawl applique une limite de débit pour garantir la stabilité et la fiabilité du service. Cette limite s’applique à tous les points de terminaison et dépend du nombre de requêtes effectuées sur une période donnée. Si vous dépassez la limite de débit, vous recevrez un code de réponse 429.