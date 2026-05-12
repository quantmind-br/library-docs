---
title: Scraping plus rapide | Firecrawl
url: https://docs.firecrawl.dev/fr/features/fast-scraping
source: sitemap
fetched_at: 2026-03-23T07:23:47.320842-03:00
rendered_js: false
word_count: 508
summary: This document explains how to configure caching mechanisms in Firecrawl using the maxAge parameter to optimize performance and reduce latency for data retrieval.
tags:
    - caching
    - performance-optimization
    - data-scraping
    - latency-reduction
    - api-configuration
    - firecrawl
category: configuration
---

## Fonctionnement

Firecrawl met en cache les pages déjà extraites et, par défaut, renvoie une copie récente lorsqu’elle est disponible.

- **Actualisation par défaut** : `maxAge = 172800000` ms (2 jours). Si la copie en cache est plus récente, elle est renvoyée instantanément ; sinon, Firecrawl relance une extraction et met à jour le cache.
- **Forcer du frais** : Définissez `maxAge: 0` pour toujours ré-extraire. Notez que cela contourne entièrement le cache : chaque requête passe alors par l’intégralité du pipeline d’extraction, prendra plus de temps à se terminer et aura plus de risques d’échouer. Utilisez une valeur de `maxAge` non nulle si vous n’avez pas besoin de contenu en temps réel pour chaque requête.
- **Ignorer le cache** : Définissez `storeInCache: false` si vous ne souhaitez pas stocker les résultats d’une requête.

Obtenez vos résultats **jusqu’à 500 % plus rapidement** lorsque vous n’avez pas besoin des données les plus récentes. Contrôlez l’actualité via `maxAge` :

1. **Retour instantané** si une version récente de la page est disponible
2. **Extraction à jour** uniquement si notre version est plus ancienne que l’âge spécifié
3. **Gagnez du temps** — les résultats reviennent en millisecondes plutôt qu’en secondes

## Quand l’utiliser

**Idéal pour :**

- Documentation, articles, pages produit
- Traitements par lots
- Développement et tests
- Création de bases de connaissances

**À éviter :**

- Données en temps réel (cours boursiers, scores en direct, dernières actualités)
- Contenu fréquemment mis à jour
- Applications sensibles au facteur temps

## Utilisation

Ajoutez `maxAge` à votre requête de scraping. Les valeurs sont en millisecondes (p. ex. `3600000` = 1 heure).

## Valeurs courantes de maxAge

Voici quelques valeurs de référence utiles :

- **5 minutes** : `300000` — pour du contenu semi‑dynamique
- **1 heure** : `3600000` — pour du contenu mis à jour chaque heure
- **1 jour** : `86400000` — pour du contenu mis à jour quotidiennement
- **1 semaine** : `604800000` — pour du contenu relativement statique

## Impact sur les performances

Avec `maxAge` activé :

- **Des temps de réponse jusqu’à 500 % plus rapides** pour le contenu récent
- **Des résultats instantanés** plutôt que d’attendre de nouveaux scrapes

## Notes importantes

- **Par défaut** : `maxAge` est `172800000` (2 jours)
- **Actualisé si nécessaire** : si nos données sont plus anciennes que `maxAge`, nous réexécutons automatiquement le scraping
- **Aucune donnée périmée** : vous ne recevrez jamais de données plus anciennes que le `maxAge` que vous avez spécifié
- **Crédits** : les résultats mis en cache coûtent toujours 1 crédit par page. La mise en cache améliore les performances et la latence, pas l’utilisation des crédits.

## Crawl plus rapide

Les mêmes gains de vitesse s’appliquent lors du crawl de plusieurs pages. Utilisez `maxAge` dans `scrapeOptions` pour obtenir des résultats en cache pour les pages que nous avons vues récemment.

Lors d’un crawl avec `maxAge`, chaque page de votre crawl bénéficiera d’une amélioration de vitesse de 500 % si nous disposons de données récentes en cache pour cette page. Commencez à utiliser `maxAge` dès aujourd’hui pour des scrapes et des crawls nettement plus rapides !

> Êtes-vous un agent d’IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.