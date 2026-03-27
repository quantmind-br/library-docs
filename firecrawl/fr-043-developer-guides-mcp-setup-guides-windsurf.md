---
title: Recherche web et scraping MCP dans Windsurf - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/mcp-setup-guides/windsurf
source: sitemap
fetched_at: 2026-03-23T07:35:36.296655-03:00
rendered_js: false
word_count: 83
summary: This document provides instructions for integrating the Firecrawl MCP server into the Windsurf IDE to enable web scraping and search capabilities for AI agents.
tags:
    - windsurf-ide
    - firecrawl-mcp
    - web-scraping
    - ai-agents
    - mcp-configuration
    - search-tools
category: configuration
---

Ajoutez des fonctionnalités de scraping et de recherche web à Windsurf avec Firecrawl MCP.

## Configuration rapide

### 1. Obtenez votre clé API

Inscrivez-vous sur [firecrawl.dev/app](https://firecrawl.dev/app) et copiez votre clé API.

### 2. Ajouter à Windsurf

Ajoutez ceci à votre `./codeium/windsurf/model_config.json` :

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "VOTRE_CLE_API"
      }
    }
  }
}
```

Remplacez `YOUR_API_KEY` par votre clé API Firecrawl.

### 3. Redémarrez Windsurf

Terminé ! Windsurf peut maintenant rechercher et explorer le Web.

## Démonstration rapide

Essayez ceci dans Windsurf : **Recherche :**

```
Rechercher les dernières fonctionnalités de Tailwind CSS
```

**Extraction :**

```
Scraper firecrawl.dev et expliquer ce que c'est
```

**Accéder à la documentation :**

```
Trouver et scraper la documentation d'authentification Supabase
```

Les agents IA de Windsurf utiliseront automatiquement les outils de Firecrawl.