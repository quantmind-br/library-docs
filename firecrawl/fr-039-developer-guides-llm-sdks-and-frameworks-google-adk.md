---
title: Agent Development Kit (ADK) - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/llm-sdks-and-frameworks/google-adk
source: sitemap
fetched_at: 2026-03-23T07:35:53.825727-03:00
rendered_js: false
word_count: 450
summary: Ce document explique comment intégrer Firecrawl au Google Agent Development Kit (ADK) via le Model Context Protocol pour permettre aux agents IA d'effectuer des tâches de web scraping et d'extraction de données.
tags:
    - firecrawl
    - google-adk
    - web-scraping
    - mcp
    - ai-agents
    - data-extraction
category: guide
---

Intégrez Firecrawl à l’Agent Development Kit (ADK) de Google pour créer des agents IA puissants dotés de capacités de web scraping via le Model Context Protocol (MCP).

## Vue d’ensemble

Firecrawl fournit un serveur MCP qui s’intègre de façon transparente à l’ADK de Google, permettant à vos agents d’extraire, de parcourir et d’aspirer efficacement des données structurées depuis n’importe quel site web. L’intégration prend en charge les instances Firecrawl hébergées dans le cloud comme auto‑hébergées, avec HTTP en streaming pour des performances optimales.

## Fonctionnalités

- Scraping, exploration et découverte de contenu web efficaces sur n’importe quel site
- Recherche avancée et extraction de contenu intelligente
- Recherche approfondie et scraping par lots à grande échelle
- Déploiement flexible (cloud ou auto‑hébergé)
- Optimisé pour les environnements web modernes avec prise en charge du streaming HTTP

## Prérequis

- Obtenez une clé d’API Firecrawl sur [firecrawl.dev](https://firecrawl.dev)
- Installez le SDK Google

## Configuration

OutilNomDescriptionOutil de scraping`firecrawl_scrape`Extraire le contenu d’une seule URL avec des options avancéesOutil de scraping par lot`firecrawl_batch_scrape`Extraire plusieurs URL efficacement avec limitation de débit intégrée et traitement paralléliséVérifier l’état du lot`firecrawl_check_batch_status`Vérifier l’état d’une opération par lotOutil de cartographie`firecrawl_map`Cartographier un site web pour découvrir toutes les URL indexées du siteOutil de recherche`firecrawl_search`Rechercher sur le web et, en option, extraire le contenu des résultats de rechercheOutil de crawl`firecrawl_crawl`Démarrer un crawl asynchrone avec des options avancéesVérifier l’état du crawl`firecrawl_check_crawl_status`Vérifier l’état d’une tâche de crawlOutil d’extraction`firecrawl_extract`Extraire des informations structurées à partir de pages web à l’aide de modèles LLM

## Configuration

### Configuration requise

**FIRECRAWL\_API\_KEY**: votre clé API Firecrawl

- Requise lors de l’utilisation de l’API cloud (par défaut)
- Facultative lors de l’utilisation d’une instance auto-hébergée avec FIRECRAWL\_API\_URL

### Configuration optionnelle

**URL de l’API Firecrawl (pour les instances auto-hébergées)** :

- `FIRECRAWL_API_URL` : Point de terminaison de l’API personnalisé
- Exemple : `https://firecrawl.your-domain.com`
- Si non renseigné, l’API cloud sera utilisée

**Configuration des tentatives de nouvelle exécution** :

- `FIRECRAWL_RETRY_MAX_ATTEMPTS` : Nombre maximal de tentatives (par défaut : 3)
- `FIRECRAWL_RETRY_INITIAL_DELAY` : Délai initial en millisecondes (par défaut : 1000)
- `FIRECRAWL_RETRY_MAX_DELAY` : Délai maximal en millisecondes (par défaut : 10000)
- `FIRECRAWL_RETRY_BACKOFF_FACTOR` : Facteur de backoff exponentiel (par défaut : 2)

**Suivi de l’utilisation des crédits** :

- `FIRECRAWL_CREDIT_WARNING_THRESHOLD` : Seuil d’avertissement (par défaut : 1000)
- `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD` : Seuil critique (par défaut : 100)

## Exemple : Agent de recherche sur le Web

```
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

FIRECRAWL_API_KEY = "YOUR-API-KEY"

# Créer un agent de recherche
research_agent = Agent(
    model="gemini-2.5-pro",
    name="research_agent",
    description='Un agent IA qui recherche des sujets en scrapant et en analysant du contenu web',
    instruction='''Vous êtes un assistant de recherche. Lorsqu'on vous donne un sujet ou une question :
    1. Utilisez l'outil de recherche pour trouver des sites web pertinents
    2. Scrapez les pages les plus pertinentes pour obtenir des informations détaillées
    3. Extrayez des données structurées si nécessaire
    4. Fournissez des réponses complètes et bien documentées''',
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=f"https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp",
            ),
        )
    ],
)

# Utiliser l'agent
response = research_agent.run("Quelles sont les dernières fonctionnalités de Python 3.13 ?")
print(response)
```

## Bonnes pratiques

1. **Utiliser le bon outil pour la tâche** :
   
   - `firecrawl_search` lorsque vous devez d’abord trouver les pages pertinentes
   - `firecrawl_scrape` pour une seule page
   - `firecrawl_batch_scrape` pour plusieurs URL connues
   - `firecrawl_crawl` pour découvrir et scraper des sites entiers
2. **Surveiller votre consommation** : configurez des seuils de crédit pour éviter des dépassements inattendus
3. **Gérer les erreurs proprement** : configurez les paramètres de retry en fonction de votre cas d’usage
4. **Optimiser les performances** : utilisez des opérations par lots lorsque vous scrapez plusieurs URL

* * *