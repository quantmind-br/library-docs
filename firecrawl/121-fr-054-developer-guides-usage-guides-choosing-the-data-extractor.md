---
title: Choisir l’extracteur de données | Firecrawl
url: https://docs.firecrawl.dev/fr/developer-guides/usage-guides/choosing-the-data-extractor
source: sitemap
fetched_at: 2026-03-23T07:30:13.720077-03:00
rendered_js: false
word_count: 1156
summary: This document provides a comparative guide to Firecrawl's three primary data extraction methods—agent, extract, and scrape—to help users choose the appropriate tool based on their discovery needs and knowledge of target URLs.
tags:
    - web-scraping
    - data-extraction
    - firecrawl
    - ai-agents
    - web-crawling
    - json-extraction
category: guide
---

Firecrawl propose trois approches pour extraire des données structurées à partir de pages web. Chacune couvre des cas d’utilisation différents, avec des niveaux d’automatisation et de contrôle variés.

## Comparaison rapide

Fonctionnalité`/agent``/extract``/scrape` (mode JSON)**Statut**ActifUtiliser `/agent` à la placeActif**URL requise**Non (facultative)Oui (caractères génériques pris en charge)Oui (URL unique)**Portée**Découverte à l’échelle du webPlusieurs pages/domainesPage unique**Découverte d’URL**Recherche autonome sur le webExploration à partir des URL fourniesAucune**Traitement**AsynchroneAsynchroneSynchrone**Schéma requis**Non (prompt ou schéma)Non (prompt ou schéma)Non (prompt ou schéma)**Tarification**Dynamique (5 exécutions gratuites/jour)Basée sur les tokens (1 crédit = 15 tokens)1 crédit/page**Idéal pour**Recherche, découverte, collecte complexeExtraction sur plusieurs pages (lorsque vous connaissez les URL)Extraction sur une page unique connue

## 1. `/agent` Endpoint

Le endpoint `/agent` est l’offre la plus avancée de Firecrawl, le successeur de `/extract`. Il utilise des agents IA pour rechercher, naviguer et collecter de manière autonome des données sur l’ensemble du web.

### Caractéristiques clés

- **URL facultatives** : décrivez simplement ce dont vous avez besoin via `prompt` ; les URL sont entièrement facultatives
- **Navigation autonome** : l’agent explore et navigue en profondeur dans les sites pour trouver vos données
- **Recherche web approfondie** : découvre de manière autonome des informations sur plusieurs domaines et pages
- **Traitement parallèle** : traite plusieurs sources simultanément pour des résultats plus rapides
- **Modèles disponibles** : `spark-1-mini` (par défaut, 60 % moins cher) et `spark-1-pro` (précision plus élevée)

### Exemple

### Cas d’usage idéal : recherche et découverte autonomes

**Scénario** : Vous devez trouver des informations sur des startups d’IA qui ont levé un tour de table de série A, y compris leurs fondateurs et les montants levés. **Pourquoi `/agent`**  : Vous ne savez pas quels sites web contiennent ces informations. L’agent va rechercher sur le web de manière autonome, naviguer vers les sources pertinentes (Crunchbase, sites d’actualités, pages d’entreprise) et compiler les données structurées pour vous. Pour plus de détails, consultez la [documentation de l’agent](https://docs.firecrawl.dev/fr/features/agent).

* * *

L’endpoint `/extract` collecte des données structurées à partir d’URL spécifiées ou de domaines entiers grâce à une extraction pilotée par des modèles de langage (LLM).

### Caractéristiques clés

- **URL généralement requises** : fournissez au moins une URL (prend en charge les caractères génériques comme `example.com/*`)
- **Exploration de domaine** : peut explorer et analyser toutes les URL découvertes dans un domaine
- **Amélioration via la recherche Web** : `enableWebSearch` (optionnel) pour suivre des liens en dehors des domaines spécifiés
- **Schéma facultatif** : prend en charge un schéma JSON strict OU des prompts en langage naturel
- **Traitement asynchrone** : renvoie un ID de tâche pour le suivi de l’état

### La limitation liée aux URL

Le défi fondamental avec `/extract` est que vous devez généralement connaître les URL à l’avance :

1. **Lacune en matière de découverte** : pour des tâches comme « trouver les entreprises YC W24 », vous ne savez pas quelles URL contiennent les données. Vous auriez besoin d’une étape de recherche séparée avant d’appeler `/extract`.
2. **Recherche sur le web peu fluide** : même si `enableWebSearch` existe, il se limite à démarrer à partir des URL que vous fournissez — un workflow peu adapté aux tâches de découverte.
3. **Pourquoi `/agent` a été créé** : `/extract` est efficace pour extraire à partir d’emplacements connus, mais moins performant pour découvrir où se trouvent les données.

### Exemple

**Scénario** : vous disposez de l’URL de la documentation de votre concurrent et vous voulez en extraire tous les endpoints d’API depuis `docs.competitor.com/*`. **Pourquoi `/extract` fonctionne ici** : vous connaissez précisément le domaine. Mais même dans ce cas, `/agent` avec les URL fournies donnera généralement de meilleurs résultats aujourd’hui. Pour plus de détails, consultez la [documentation Extract](https://docs.firecrawl.dev/fr/features/extract).

* * *

## 3. Endpoint `/scrape` avec mode JSON

L’endpoint `/scrape` en mode JSON est l’approche la plus contrôlée : il extrait des données structurées à partir d’une seule URL connue en utilisant un LLM pour analyser le contenu de la page selon le schéma que vous avez spécifié.

### Caractéristiques principales

- **Une seule URL** : Conçu pour extraire des données d’une page spécifique à la fois
- **URL exacte requise** : Vous devez connaître l’URL précise qui contient les données
- **Schéma facultatif** : Peut utiliser un schéma JSON OU simplement un prompt (le LLM choisit la structure)
- **Synchrone** : Retourne les données immédiatement (aucune interrogation de tâche nécessaire)
- **Formats supplémentaires** : Peut combiner l’extraction JSON avec du markdown, du HTML et des captures d’écran dans une seule requête

### Exemple

**Scénario** : Vous créez un outil de suivi des prix et devez extraire le prix, l’état du stock et les détails du produit à partir d’une page produit spécifique pour laquelle vous avez déjà l’URL. **Pourquoi `/scrape` avec le mode JSON** : Vous savez exactement quelle page contient les données, vous avez besoin d’une extraction précise sur une seule page et vous voulez des résultats synchrones sans la charge de gestion de jobs. Pour plus de détails, voir la [documentation du mode JSON](https://docs.firecrawl.dev/fr/features/llm-extract).

* * *

## Guide de décision

**Connaissez-vous la ou les URL exactes contenant vos données ?**

- **NON** → Utilisez `/agent` (découverte web autonome)
- **OUI**
  
  - **Page unique ?** → Utilisez `/scrape` avec le mode JSON
  - **Pages multiples ?** → Utilisez `/agent` avec les URL (ou `/scrape` en traitement par lot)

### Recommandations par scénario

ScénarioEndpoint recommandé« Trouver toutes les startups d’IA et leurs financements »`/agent`« Extraire les données de cette page produit spécifique »`/scrape` (mode JSON)« Récupérer tous les articles de blog de competitor.com »`/agent` avec URL« Surveiller les prix sur plusieurs URL connues »`/scrape` avec traitement par lots« Rechercher des entreprises dans un secteur spécifique »`/agent`« Extraire les coordonnées de contact depuis 50 pages d’entreprises connues »`/scrape` avec traitement par lots

* * *

## Tarification

EndpointCoûtRemarques`/scrape` (mode JSON)1 crédit/pageFixe et prévisible`/extract`Basé sur les jetons (1 crédit = 15 jetons)Variable en fonction du contenu`/agent`Dynamique5 exécutions gratuites/jour ; varie en fonction de la complexité

### Exemple : « Trouver les fondateurs de Firecrawl »

EndpointFonctionnementCrédits utilisés`/scrape`Vous trouvez l’URL manuellement, puis scrapez 1 page~1 crédit`/extract`Vous fournissez une ou plusieurs URL, il extrait des données structuréesVariable (en fonction des tokens)`/agent`Envoyez simplement le prompt — l’agent trouve et extrait~100–500 crédits

**Compromis** : `/scrape` est le moins cher mais nécessite que vous connaissiez l’URL. `/agent` coûte plus cher mais gère la découverte automatiquement. Pour consulter les tarifs détaillés, voir [Tarifs Firecrawl](https://firecrawl.dev/pricing).

* * *

Si vous utilisez actuellement `/extract`, la migration est simple : **Avant (/extract) :**

```
result = app.extract(
    urls=["https://example.com/*"],
    prompt="Extraire les informations sur le produit",
    schema=schema
)
```

**Après (agent) :**

```
result = app.agent(
    urls=["https://example.com"],  # Optionnel - peut être omis entièrement
    prompt="Extract product information from example.com",
    schema=schema,
    model="spark-1-mini"  # ou "spark-1-pro" pour une meilleure précision
)
```

L’avantage principal : avec `/agent`, vous pouvez complètement vous passer des URL et simplement décrire ce dont vous avez besoin.

* * *

## Points clés à retenir

1. **Vous connaissez l’URL exacte ?** Utilisez `/scrape` avec le mode JSON — c’est l’option la moins chère (1 crédit/page), la plus rapide (synchrone) et la plus prévisible.
2. **Besoin de recherche automatisée ?** Utilisez `/agent` — il gère la découverte automatiquement avec 5 exécutions gratuites/jour, puis une tarification dynamique selon la complexité.
3. **Migrez de `/extract`** vers `/agent` pour les nouveaux projets — `/agent` est le successeur avec de meilleures fonctionnalités.
4. **Compromis coût vs praticité** : `/scrape` est le plus économique lorsque vous connaissez vos URL ; `/agent` coûte plus cher mais élimine la découverte manuelle des URL.

* * *

## Pour aller plus loin

- [Documentation de l’agent](https://docs.firecrawl.dev/fr/features/agent)
- [Modèles d’agent](https://docs.firecrawl.dev/fr/features/models)
- [Documentation du mode JSON](https://docs.firecrawl.dev/fr/features/llm-extract)
- [Documentation d’Extract](https://docs.firecrawl.dev/fr/features/extract)
- [Scraping par lots](https://docs.firecrawl.dev/fr/features/batch-scrape)