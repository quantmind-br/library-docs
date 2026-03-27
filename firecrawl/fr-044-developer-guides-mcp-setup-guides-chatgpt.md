---
title: Recherche et scraping web MCP dans ChatGPT - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/mcp-setup-guides/chatgpt
source: sitemap
fetched_at: 2026-03-23T07:38:40.677469-03:00
rendered_js: false
word_count: 327
summary: This document provides step-by-step instructions for integrating Firecrawl's web scraping and search capabilities into ChatGPT using the Model Context Protocol (MCP).
tags:
    - chatgpt
    - firecrawl
    - mcp
    - web-scraping
    - integration
    - developer-mode
    - data-extraction
category: configuration
---

Ajoutez des fonctionnalités de scraping et de recherche web à ChatGPT avec Firecrawl MCP.

## Configuration rapide

### 1. Obtenir votre clé API

Inscrivez-vous sur [firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) et copiez votre clé API.

### 2. Activer le mode développeur

Ouvrez les paramètres de ChatGPT en cliquant sur votre nom d’utilisateur dans le coin inférieur gauche, ou accédez directement à [chatgpt.com/#settings](https://chatgpt.com/#settings). Dans la fenêtre des paramètres, faites défiler jusqu’en bas et sélectionnez **Advanced Settings**. Activez **Developer mode** en basculant l’interrupteur sur ON.

### 3. Créer le connecteur

Avec le mode Developer activé, allez dans l’onglet **Apps & Connectors** dans la même fenêtre de paramètres. Cliquez sur le bouton **Create** dans le coin supérieur droit.

Renseignez les détails du connecteur :

- **Name :** `Firecrawl MCP`
- **Description :** `Web scraping, crawling, search, and content extraction` (facultatif)
- **MCP Server URL :** `https://mcp.firecrawl.dev/YOUR_API_KEY_HERE/v2/mcp`
- **Authentication :** `None`

Remplacez `YOUR_API_KEY_HERE` dans l’URL par votre [clé API Firecrawl](https://www.firecrawl.dev/app/api-keys).

Cochez la case **“I understand and want to continue”**, puis cliquez sur **Create**.

### 4. Vérifier la configuration

Retournez à l’interface principale de ChatGPT. Vous devriez voir le **Mode développeur** affiché, ce qui indique que les connecteurs MCP sont actifs. Si vous ne voyez pas le Mode développeur, actualisez la page. S’il n’apparaît toujours pas, rouvrez les paramètres et vérifiez que le Mode développeur est bien activé dans les paramètres avancés.

Pour utiliser Firecrawl dans une conversation, cliquez sur le bouton **+** dans la zone de saisie du chat, puis sélectionnez **More**, puis **Firecrawl MCP**.

## Démo rapide

Avec Firecrawl MCP sélectionné, essayez les prompts suivants : **Recherche :**

```
Search for the latest React Server Components updates
```

**Scraping :**

```
Scrape firecrawl.dev and tell me what it does
```

**Obtenir la documentation :**

```
Extrais la documentation Vercel sur les edge functions et fais-en un résumé
```

Lorsque ChatGPT utilise les outils MCP de Firecrawl, une invite de confirmation s’affiche pour demander votre approbation.

Vous pouvez cocher **« Se souvenir pour cette conversation »** pour éviter les confirmations répétées au cours de la même session de chat. Cette mesure de sécurité est mise en place par OpenAI pour garantir que les outils MCP n’exécutent pas d’actions non intentionnelles. Une fois la demande confirmée, ChatGPT exécutera la requête et renverra les résultats.