---
title: Recherche et scraping web MCP dans Cursor - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/mcp-setup-guides/cursor
source: sitemap
fetched_at: 2026-03-23T07:32:12.714738-03:00
rendered_js: false
word_count: 181
summary: Ce guide explique comment intégrer Firecrawl MCP dans l'éditeur Cursor pour permettre le scraping et la recherche web directement via l'assistant IA.
tags:
    - cursor
    - firecrawl
    - mcp
    - web-scraping
    - web-search
    - configuration
category: configuration
---

Ajoutez des capacités de scraping et de recherche web à Cursor avec Firecrawl MCP.

## Configuration rapide

### 1. Obtenez votre clé d’API

Inscrivez-vous sur [firecrawl.dev/app](https://firecrawl.dev/app) et copiez votre clé d’API.

### 2. Ajouter à Cursor

Ouvrez les préférences (`Cmd+,`), recherchez « MCP », puis ajoutez :

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "votre_cle_api_ici"
      }
    }
  }
}
```

Remplacez `your_api_key_here` par votre clé API Firecrawl.

### 3. Redémarrer Cursor

C’est tout ! Vous pouvez maintenant rechercher et scraper le web directement depuis Cursor.

## Démo rapide

Essayez ceci dans Cursor Chat (`Cmd+K`) : **Recherche :**

```
Rechercher les bonnes pratiques TypeScript 2025
```

**Extraction :**

```
Scrape firecrawl.dev et dis-moi ce que c'est
```

**Obtenir la doc :**

```
Scrape la documentation des hooks React et explique useEffect
```

Cursor utilisera automatiquement les outils de Firecrawl.

## Dépannage sous Windows

Si vous voyez l’erreur `spawn npx ENOENT` ou « No server info found » sous Windows, cela signifie que Cursor ne trouve pas `npx` dans votre PATH. Essayez l’une de ces solutions : **Option A : utiliser le chemin complet vers `npx.cmd`** Exécutez `where npx` dans l’Invite de commandes pour obtenir le chemin complet, puis mettez à jour votre configuration :

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "C:\\Program Files\\nodejs\\npx.cmd",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

Remplacez le chemin `command` par le résultat de `where npx`. **Option B : Utiliser l’URL hébergée à distance (Node.js non requis)**

```
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/YOUR-API-KEY/v2/mcp"
    }
  }
}
```

Remplacez `YOUR-API-KEY` par votre clé API Firecrawl.