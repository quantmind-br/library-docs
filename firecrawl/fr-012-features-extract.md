---
title: Extraction | Firecrawl
url: https://docs.firecrawl.dev/fr/features/extract
source: sitemap
fetched_at: 2026-03-23T07:23:42.773886-03:00
rendered_js: false
word_count: 831
summary: Ce document présente le point de terminaison /extract de Firecrawl, qui permet d'extraire des données structurées depuis des URL en utilisant des prompts en langage naturel, des schémas JSON ou une recherche web.
tags:
    - web-scraping
    - api
    - data-extraction
    - structured-data
    - firecrawl
    - web-crawling
category: api
---

Le point de terminaison `/extract` simplifie la collecte de données structurées depuis n’importe quel nombre d’URL ou de domaines entiers. Fournissez une liste d’URL, éventuellement avec des jokers (p. ex. `example.com/*`), ainsi qu’un prompt ou un schéma décrivant les informations souhaitées. Firecrawl gère l’exploration, l’analyse et l’agrégation, que l’ensemble de données soit petit ou volumineux.

Vous pouvez extraire des données structurées à partir d’une ou plusieurs URL, y compris avec des caractères génériques :

- **Page unique**  
  Exemple : `https://firecrawl.dev/some-page`
- **Pages multiples / Domaine complet**  
  Exemple : `https://firecrawl.dev/*`

Lorsque vous utilisez `/*`, Firecrawl va automatiquement explorer et analyser toutes les URL qu’il peut découvrir dans ce domaine, puis extraire les données demandées. Cette fonctionnalité est expérimentale ; envoyez un e-mail à [help@firecrawl.com](mailto:help@firecrawl.com) si vous rencontrez des problèmes.

### Exemple d’utilisation

**Paramètres clés :**

- **urls** : Tableau d’une ou plusieurs URL. Prend en charge les caractères génériques (`/*`) pour un crawl plus large.
- **prompt** (Optionnel sauf si aucun schéma) : Instruction en langage naturel décrivant les données souhaitées ou la manière dont vous voulez qu’elles soient structurées.
- **schema** (Optionnel sauf si aucun prompt) : Structure plus stricte si vous connaissez déjà le format JSON.
- **enableWebSearch** (Optionnel) : Lorsque `true`, l’extraction peut suivre des liens en dehors du domaine spécifié.

Voir la [référence de l’API](https://docs.firecrawl.dev/api-reference/endpoint/extract) pour plus de détails.

### Réponse (SDKs)

```
{
  "success": true,
  "data": {
    "company_mission": "Firecrawl est le moyen le plus simple d’extraire des données du web. Les développeurs l’utilisent pour convertir de façon fiable des URL en markdown prêt pour les LLM ou en données structurées avec un simple appel à l’API.",
    "supports_sso": false,
    "is_open_source": true,
    "is_in_yc": true
  }
}
```

## Statut et achèvement du job

Lorsque vous lancez un job d’extraction — directement via l’API ou via les méthodes de démarrage — vous recevez un ID de job. Vous pouvez utiliser cet ID pour :

- Consulter le statut du job : envoyez une requête au point de terminaison /extract/ pour vérifier s’il est toujours en cours ou terminé.
- Attendre les résultats : si vous utilisez la méthode par défaut `extract` (Python/Node), le SDK attend et renvoie les résultats finaux.
- Démarrer puis interroger : si vous utilisez les méthodes de démarrage — `start_extract` (Python) ou `startExtract` (Node) — le SDK renvoie immédiatement un ID de job. Utilisez `get_extract_status` (Python) ou `getExtractStatus` (Node) pour suivre l’avancement.

Ci-dessous, des exemples de code pour vérifier le statut d’un job d’extraction avec Python, Node.js et cURL :

### États possibles

- **completed**: L’extraction a réussi.
- **processing**: Firecrawl traite encore votre requête.
- **failed**: Une erreur s’est produite ; les données n’ont pas été entièrement extraites.
- **cancelled**: La tâche a été annulée par l’utilisateur.

#### Exemple en cours

```
{
  "success": true,
  "data": [],
  "status": "en cours de traitement",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

#### Exemple terminé

```
{
  "success": true,
  "data": {
      "company_mission": "Firecrawl est le moyen le plus simple d’extraire des données du Web. Les développeurs l’utilisent pour convertir de façon fiable des URL en markdown prêt pour les LLM ou en données structurées avec un seul appel à l’API.",
      "supports_sso": false,
      "is_open_source": true,
      "is_in_yc": true
    },
  "status": "terminée",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

Si vous préférez ne pas définir une structure stricte, vous pouvez simplement fournir un `prompt`. Le modèle sous-jacent choisira une structure pour vous, ce qui peut être utile pour des requêtes plus exploratoires ou plus flexibles.

```
{
  "success": true,
  "data": {
    "company_mission": "Transformez les sites web en données prêtes pour les LLM. Alimentez vos applications d’IA avec des données propres, collectées depuis n’importe quel site."
  }
}
```

## Améliorer les résultats avec la recherche web

Définir `enableWebSearch = true` dans votre requête étend l’exploration au-delà de l’ensemble d’URL fourni. Cela permet de récupérer des informations complémentaires ou liées depuis des pages référencées. Voici un exemple qui extrait des informations sur les caméras embarquées (dash cams), en enrichissant les résultats avec des données issues de pages connexes :

### Exemple de réponse avec recherche web

```
{
  "success": true,
  "data": {
    "dash_cams": [
      {
        "name": "Nextbase 622GW",
        "price": "$399.99",
        "features": [
          "Enregistrement vidéo 4K",
          "Stabilisation d’image",
          "Alexa intégrée",
          "Intégration What3Words"
        ],
        /* Informations ci-dessous enrichies à partir d’autres sites comme 
        https://www.techradar.com/best/best-dash-cam, trouvées 
        via le paramètre enableWebSearch */
        "pros": [
          "Excellente qualité vidéo",
          "Très bonne vision nocturne",
          "GPS intégré"
        ],
        "cons": ["Prix élevé", "L’application peut être capricieuse"]
      }
    ],
  }

```

La réponse inclut un contexte supplémentaire tiré de pages connexes, offrant des informations plus complètes et plus précises.

Le point de terminaison `/extract` prend désormais en charge l’extraction de données structurées à l’aide d’un prompt, sans avoir besoin d’URL spécifiques. C’est utile pour la recherche ou lorsque les URL exactes ne sont pas connues. Actuellement en alpha.

## Limitations connues (bêta)

1. **Couverture de sites à grande échelle**  
   La couverture complète de sites très volumineux (p. ex. « tous les produits sur Amazon ») en une seule requête n’est pas encore prise en charge.
2. **Requêtes logiques complexes**  
   Des requêtes comme « trouver toutes les publications de 2025 » peuvent ne pas renvoyer de manière fiable toutes les données attendues. Des capacités de requête plus avancées sont en cours de développement.
3. **Incohérences occasionnelles**  
   Les résultats peuvent varier d’une exécution à l’autre, en particulier pour les sites très vastes ou dynamiques. En général, les informations essentielles sont capturées, mais des variations sont possibles.
4. **État bêta**  
   Comme `/extract` est encore en bêta, les fonctionnalités et les performances continueront d’évoluer. Nous accueillons les signalements de bugs et vos retours pour nous aider à nous améliorer.

## Utiliser FIRE-1

FIRE-1 est un agent IA qui étend les capacités de scraping de Firecrawl. Il peut contrôler des actions du navigateur et naviguer dans des structures de sites web complexes pour permettre une extraction de données plus complète que les méthodes de scraping traditionnelles. Vous pouvez utiliser l’agent FIRE-1 avec le point de terminaison `/extract` pour des tâches d’extraction complexes nécessitant une navigation sur plusieurs pages ou une interaction avec des éléments. **Exemple (cURL) :**

```
curl -X POST https://api.firecrawl.dev/v2/extract \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer VOTRE_CLÉ_API' \
    -d '{
      "urls": ["https://example-forum.com/topic/123"],
      "prompt": "Extraire tous les commentaires des utilisateurs de ce fil de discussion.",
      "schema": {
        "type": "object",
        "properties": {
          "comments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "author": {"type": "string"},
                "comment_text": {"type": "string"}
              },
              "required": ["author", "comment_text"]
            }
          }
        },
        "required": ["comments"]
      },
      "agent": {
        "model": "FIRE-1"
      }
    }'
```

> FIRE-1 est déjà disponible et accessible en avant-première.

## Facturation et suivi de l’utilisation

Nous avons simplifié la facturation afin qu’Extract utilise désormais des crédits, comme tous les autres points de terminaison. Chaque crédit vaut 15 tokens. Vous pouvez suivre l’utilisation d’Extract via le [tableau de bord](https://www.firecrawl.dev/app/extract). Vous avez des retours ou besoin d’aide ? Envoyez un e-mail à [help@firecrawl.com](mailto:help@firecrawl.com).

> Êtes-vous un agent IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’intégration automatisée.