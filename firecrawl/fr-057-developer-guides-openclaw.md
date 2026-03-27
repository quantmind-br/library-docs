---
title: Utiliser OpenClaw avec Firecrawl
url: https://docs.firecrawl.dev/fr/developer-guides/openclaw
source: sitemap
fetched_at: 2026-03-23T07:33:40.185448-03:00
rendered_js: false
word_count: 404
summary: This document provides instructions on integrating the Firecrawl CLI with OpenClaw to enable web scraping, searching, and browser automation capabilities for AI agents using a sandboxed environment.
tags:
    - web-scraping
    - ai-agents
    - automation
    - browser-sandbox
    - cli-integration
    - data-extraction
category: guide
---

Intégrez Firecrawl à OpenClaw pour donner à vos agents la capacité d’effectuer du scraping, de la recherche, du crawling, de l’extraction et d’interagir avec le web — le tout via la [Firecrawl CLI](https://docs.firecrawl.dev/fr/sdks/cli).

## Pourquoi Firecrawl + OpenClaw

- **Aucun navigateur local nécessaire** — chaque session s’exécute dans un bac à sable distant et isolé. Pas d’installation de Chromium, pas de conflits de pilotes, pas de pression mémoire sur votre machine.
- **Véritable parallélisme** — exécutez de nombreuses sessions de navigateur en parallèle sans conflit sur les ressources locales. Les agents peuvent explorer plusieurs sites en parallèle, par lots.
- **Sécurisé par défaut** — la navigation, l’évaluation du DOM et l’extraction se font entièrement dans des bacs à sable jetables, et non sur votre station de travail.
- **Meilleure utilisation des tokens** — les agents reçoivent des artefacts propres (instantanés, champs extraits) au lieu de faire entrer d’énormes DOM et journaux de pilotes dans la fenêtre de contexte.
- **Boîte à outils web complète** — scraping, recherche et automatisation du navigateur, le tout via une seule CLI que votre agent sait déjà utiliser.

## Configuration

Demandez à votre agent d’installer le CLI Firecrawl, de s’authentifier, puis d’initialiser la compétence avec cette commande :

```
npx -y firecrawl-cli init --browser --all
```

- `--all` installe la compétence Firecrawl sur chaque agent de codage IA détecté
- `--browser` ouvre automatiquement le navigateur pour l’authentification Firecrawl

ou installez tout séparément :

```
npm install -g firecrawl-cli
firecrawl init skills
firecrawl login --browser
# Ou, ignorez le navigateur et fournissez votre clé API directement :
export FIRECRAWL_API_KEY="fc-YOUR-API-KEY"
```

Assurez-vous que tout est correctement configuré :

## Scraping

Scraper une seule page et en extraire le contenu :

```
firecrawl https://example.com --only-main-content
```

Obtenir des formats spécifiques :

```
firecrawl https://example.com --format markdown,links --pretty
```

## Recherche

Recherchez sur le Web et, si besoin, effectuez un scraping des résultats :

```
firecrawl search "latest AI funding rounds 2025" --limit 10

# Rechercher et extraire les résultats
firecrawl search "OpenClaw documentation" --scrape --scrape-formats markdown
```

## Navigateur

Lancez une session de navigateur à distance pour l’automatisation interactive. Chaque session s’exécute dans un environnement sandbox isolé — aucune installation locale de Chromium n’est nécessaire. `agent-browser` est préinstallé avec plus de 40 commandes intégrées.

```
# Raccourci : lance automatiquement une session si aucune n'est active
firecrawl browser "open https://news.ycombinator.com"
firecrawl browser "snapshot"
firecrawl browser "scrape"
firecrawl browser close
```

Interagissez avec les éléments de la page à l’aide des refs du snapshot :

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
# snapshot retourne des IDs @ref — utilisez-les pour interagir
firecrawl browser "click @e5"
firecrawl browser "fill @e3 'search query'"
firecrawl browser "scrape"
firecrawl browser close
```

## Exemple : donner des instructions à votre agent

Voici quelques prompts que vous pouvez donner à votre agent OpenClaw :

- *« Utilise Firecrawl pour scraper [https://example.com](https://example.com) et résume le contenu principal. »*
- *« Recherche les dernières actualités d’OpenAI et donne-moi un résumé des 5 principaux résultats. »*
- *« Utilise Firecrawl Browser pour ouvrir Hacker News, récupère les 5 principaux articles et les 10 premiers commentaires de chacun. »*
- *« Parcours la documentation sur [https://docs.firecrawl.dev](https://docs.firecrawl.dev) et enregistre-la dans un fichier. »*

## Pour aller plus loin

- [Référence de la CLI Firecrawl](https://docs.firecrawl.dev/fr/sdks/cli)
- [Documentation de Browser Sandbox](https://docs.firecrawl.dev/fr/features/browser)
- [Documentation de l’Agent](https://docs.firecrawl.dev/fr/features/agent)