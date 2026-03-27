---
title: Introduction - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v2-introduction
source: sitemap
fetched_at: 2026-03-23T07:32:06.347312-03:00
rendered_js: false
word_count: 236
summary: This document provides the foundational technical information for integrating with the Firecrawl API, including base URLs, authentication methods, status codes, and rate limiting policies.
tags:
    - web-scraping
    - api-documentation
    - authentication
    - rate-limiting
    - http-codes
    - data-extraction
category: reference
---

L’API Firecrawl vous donne un accès programmatique aux données issues du web. Tous les endpoints utilisent la même URL de base, le même schéma d’authentification et le même format de réponse, décrits sur cette page.

## Fonctionnalités

## Fonctionnalités d’agent

## URL de base

Toutes les requêtes utilisent l’URL de base suivante :

```
https://api.firecrawl.dev
```

## Authentification

Chaque requête doit inclure un en-tête `Authorization` contenant votre clé d’API :

```
Authorization: Bearer fc-YOUR-API-KEY
```

Incluez cet en-tête dans tous les appels à l’API. Vous pouvez trouver votre clé API dans le [tableau de bord Firecrawl](https://www.firecrawl.dev/app/api-keys).

## Codes de réponse

Firecrawl utilise des codes d’état HTTP standard pour indiquer le résultat de vos requêtes. Les codes de la plage `2xx` indiquent une réussite, les codes `4xx` indiquent des erreurs côté client et les codes `5xx` indiquent des erreurs côté serveur.

StatutDescription`200`La requête a réussi.`400`Paramètres de requête invalides.`401`Clé d’API manquante ou invalide.`402`Paiement requis.`404`La ressource demandée est introuvable.`429`Limite de débit dépassée.`5xx`Erreur de serveur du côté de Firecrawl.

Lorsqu’une erreur `5xx` se produit, le corps de la réponse inclut un code d’erreur spécifique pour vous aider à diagnostiquer le problème.

## Limitation de débit

L’API Firecrawl applique des limitations de débit sur tous les endpoints afin de garantir la stabilité du service. Ces limitations sont basées sur le nombre de requêtes au sein d’une fenêtre temporelle donnée. Lorsque vous dépassez la limitation de débit, l’API renvoie un code de statut `429`. Réduisez temporairement la fréquence des requêtes et réessayez après un court délai.