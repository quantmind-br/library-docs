---
title: Développeurs & MCP - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/use-cases/developers-mcp
source: sitemap
fetched_at: 2026-03-23T07:28:41.819206-03:00
rendered_js: false
word_count: 263
summary: This document explains how to integrate the Firecrawl MCP server with AI assistants to enable automated web scraping, crawling, and data extraction capabilities.
tags:
    - firecrawl
    - model-context-protocol
    - web-scraping
    - ai-assistants
    - automation
    - data-extraction
category: guide
---

Les développeurs utilisent le serveur MCP de Firecrawl pour ajouter des capacités de scraping web à Claude Desktop, Cursor et d’autres assistants de programmation IA.

## Démarrer avec un modèle

Intégrez Firecrawl directement à votre flux de travail de développement IA via le Model Context Protocol. Une fois configuré, votre assistant IA a accès à un ensemble d’outils de scraping web qu’il peut appeler en votre nom :

OutilCe qu’il fait**Scrape**Extrait du contenu ou des données structurées à partir d’une seule URL**extraction par lot**Extrait du contenu de plusieurs URL connues en parallèle**Map**Découvre toutes les URL indexées d’un site web**Crawl**Parcourt une section d’un site et extrait le contenu de chaque page**Search**Effectue une recherche sur le web et, éventuellement, extrait le contenu des résultats

Votre assistant choisit automatiquement le bon outil : demandez-lui de « lire la documentation Next.js » et il effectuera un scraping ; demandez-lui de « trouver tous les articles de blog sur example.com » et il utilisera d’abord Map, puis l’extraction par lot.

## Pourquoi les développeurs choisissent Firecrawl MCP

### Créez des assistants IA plus performants

Offrez à votre IA un accès en temps réel à la documentation, aux API et aux ressources du Web. Réduisez les informations obsolètes et les hallucinations en lui fournissant les données les plus récentes.

### Aucune infrastructure requise

Aucun serveur à gérer, aucun crawler à maintenir. Configurez-le une fois et votre assistant IA pourra accéder instantanément aux sites web via le Model Context Protocol.

## Témoignages clients

## FAQ

- [AI Platforms](https://docs.firecrawl.dev/fr/use-cases/ai-platforms) - Outils de développement alimentés par l’IA
- [Deep Research](https://docs.firecrawl.dev/fr/use-cases/deep-research) - Recherche technique avancée
- [Content Generation](https://docs.firecrawl.dev/fr/use-cases/content-generation) - Génération de documentation