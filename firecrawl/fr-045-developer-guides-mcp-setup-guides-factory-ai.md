---
title: Recherche web et scraping MCP dans Factory AI - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/mcp-setup-guides/factory-ai
source: sitemap
fetched_at: 2026-03-23T07:35:40.189922-03:00
rendered_js: false
word_count: 129
summary: Ce guide explique comment intégrer Firecrawl MCP à Factory AI pour permettre les capacités de recherche web et de scraping de contenu directement dans l'interface de l'outil.
tags:
    - factory-ai
    - firecrawl
    - mcp-server
    - web-scraping
    - web-search
    - automation-tool
category: configuration
---

Ajoutez des capacités de scraping et de recherche web à Factory AI avec Firecrawl MCP.

## Configuration rapide

### 1. Récupérer votre clé d’API

Inscrivez-vous sur [firecrawl.dev/app](https://firecrawl.dev/app) et copiez votre clé d’API.

### 2. Installer la CLI Factory AI

Installez la [CLI Factory AI](https://docs.factory.ai/cli/getting-started/quickstart) si ce n’est pas déjà fait : **macOS/Linux :**

```
curl -fsSL https://app.factory.ai/cli | sh
```

**Windows :**

```
iwr https://app.factory.ai/cli/install.ps1 -useb | iex
```

### 3. Ajouter le serveur MCP Firecrawl

Dans le CLI de Factory Droid, ajoutez Firecrawl avec la commande `/mcp add` :

```
/mcp add firecrawl "npx -y firecrawl-mcp" -e FIRECRAWL_API_KEY=votre-clé-api-ici
```

Remplacez `your-api-key-here` par votre clé d’API Firecrawl.

### 4. C’est fait !

Les outils Firecrawl sont désormais disponibles dans votre session Factory AI !

## Démo rapide

Essayez ceci dans Factory AI : **Rechercher sur le Web :**

```
Recherchez les dernières fonctionnalités de Next.js 15
```

**Extraire une page :**

```
Scrape firecrawl.dev et dis-moi ce que c'est
```

**Accéder à la documentation :**

```
Trouve et scrape la documentation de l'API Stripe pour les intentions de paiement
```

Factory utilisera automatiquement les outils de recherche et de scraping de Firecrawl pour obtenir les informations.