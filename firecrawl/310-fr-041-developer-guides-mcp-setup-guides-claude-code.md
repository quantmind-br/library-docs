---
title: Recherche web et scraping MCP dans Claude Code - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/mcp-setup-guides/claude-code
source: sitemap
fetched_at: 2026-03-23T07:29:20.678582-03:00
rendered_js: false
word_count: 114
summary: This document provides instructions on how to integrate web scraping and search capabilities into Claude Code using the Firecrawl MCP server.
tags:
    - claude-code
    - firecrawl
    - mcp-server
    - web-scraping
    - web-search
    - api-integration
category: configuration
---

Ajoutez des fonctionnalités de scraping et de recherche web à Claude Code avec Firecrawl MCP.

## Configuration rapide

### 1. Obtenez votre clé d’API

Inscrivez-vous sur [firecrawl.dev/app](https://firecrawl.dev/app) et copiez votre clé d’API.

### 2. Ajouter le serveur MCP Firecrawl

**Option A : URL hébergée sur un serveur distant (recommandée)**

```
claude mcp add firecrawl --url https://mcp.firecrawl.dev/your-api-key/v2/mcp
```

**Option B : En local (npx)**

```
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

Remplacez `your-api-key` par votre clé d’API Firecrawl. C’est tout ! Vous pouvez maintenant effectuer des recherches et extraire des données du web depuis Claude Code.

## Démonstration rapide

Essayez ceci dans Claude Code : **Rechercher sur le Web :**

```
Search for the latest Next.js 15 features
```

**Extraire le contenu d’une page :**

```
Scrape firecrawl.dev and tell me what it does
```

**Obtenir la documentation :**

```
Find and scrape the Stripe API docs for payment intents
```

Claude utilisera automatiquement les outils de recherche et de scraping de Firecrawl pour obtenir les informations.