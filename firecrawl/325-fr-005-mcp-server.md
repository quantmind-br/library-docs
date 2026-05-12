---
title: Serveur MCP Firecrawl
url: https://docs.firecrawl.dev/fr/mcp-server
source: sitemap
fetched_at: 2026-03-23T07:29:17.03743-03:00
rendered_js: false
word_count: 2274
summary: This document provides instructions for installing and configuring the Firecrawl Model Context Protocol (MCP) server to enable web scraping and data extraction capabilities in various AI development environments.
tags:
    - mcp-server
    - firecrawl
    - web-scraping
    - ai-integration
    - cursor
    - vscode
    - claude-desktop
category: configuration
---

Une implémentation de serveur Model Context Protocol (MCP) intégrant [Firecrawl](https://github.com/firecrawl/firecrawl) pour le web scraping. Notre serveur MCP est open source et disponible sur [GitHub](https://github.com/firecrawl/firecrawl-mcp-server).

## Fonctionnalités

- Scraping, crawling et découverte du web
- Recherche et extraction de contenu
- Recherche approfondie avec agent autonome
- Gestion des sessions de navigateur
- Prise en charge du cloud et de l’auto‑hébergement
- Prise en charge du streaming HTTP

## Installation

Vous pouvez utiliser notre URL hébergée ou exécuter le serveur en local. Récupérez votre clé API sur [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)

### URL hébergée à distance

```
https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp
```

### Exécution via npx

```
env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

### Installation manuelle

```
npm install -g firecrawl-mcp
```

### Utilisation avec Cursor

[![Ajouter le serveur MCP Firecrawl à Cursor](https://cursor.com/deeplink/mcp-install-dark.png)](cursor://anysphere.cursor-deeplink/mcp/install?name=firecrawl&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImZpcmVjcmF3bC1tY3AiXSwiZW52Ijp7IkZJUkVDUkFXTF9BUElfS0VZIjoiWU9VUi1BUEktS0VZIn19)

#### Installation manuelle

Configuration de Cursor 🖥️ Remarque : nécessite Cursor version 0.45.6+ Pour des instructions de configuration à jour, consultez la documentation officielle de Cursor sur la configuration des serveurs MCP : [Guide de configuration du serveur MCP de Cursor](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers) Pour configurer Firecrawl MCP dans Cursor **v0.48.6**

1. Ouvrez les paramètres de Cursor
2. Allez dans Features &gt; MCP Servers
3. Cliquez sur ”+ Add new global MCP server”
4. Saisissez le code suivant :
   
   ```
   {
     "mcpServers": {
       "firecrawl-mcp": {
         "command": "npx",
         "args": ["-y", "firecrawl-mcp"],
         "env": {
           "FIRECRAWL_API_KEY": "YOUR-API-KEY"
         }
       }
     }
   }
   ```

Pour configurer Firecrawl MCP dans Cursor **v0.45.6**

1. Ouvrez les paramètres de Cursor
2. Allez dans Features &gt; MCP Servers
3. Cliquez sur ”+ Add New MCP Server”
4. Renseignez les éléments suivants :
   
   - Name: “firecrawl-mcp” (ou le nom de votre choix)
   - Type: “command”
   - Command: `env FIRECRAWL_API_KEY=your-api-key npx -y firecrawl-mcp`

> Si vous utilisez Windows et rencontrez des problèmes, essayez `cmd /c "set FIRECRAWL_API_KEY=your-api-key && npx -y firecrawl-mcp"`

Remplacez `your-api-key` par votre clé API Firecrawl. Si vous n’en avez pas encore, créez un compte et récupérez-la via [https://www.firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) Après l’ajout, actualisez la liste des serveurs MCP pour voir les nouveaux outils. Le Composer Agent utilisera automatiquement Firecrawl MCP lorsque c’est pertinent, mais vous pouvez aussi le demander explicitement en décrivant vos besoins en web scraping. Accédez au Composer via Command+L (Mac), sélectionnez « Agent » à côté du bouton d’envoi, puis saisissez votre requête.

### Exécuter sur Windsurf

Ajoutez ceci à votre `./codeium/windsurf/model_config.json` :

```
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "VOTRE_API_KEY"
      }
    }
  }
}
```

### Exécution avec le mode HTTP en streaming

Pour exécuter le serveur localement en utilisant le transport HTTP en streaming au lieu du transport `stdio` par défaut :

```
env HTTP_STREAMABLE_SERVER=true FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

Utilisez l’URL suivante : [http://localhost:3000/v2/mcp](http://localhost:3000/v2/mcp) ou [https://mcp.firecrawl.dev/{FIRECRAWL\_API\_KEY}/v2/mcp](https://mcp.firecrawl.dev/%7BFIRECRAWL_API_KEY%7D/v2/mcp)

### Installation via Smithery (ancienne méthode)

Pour installer Firecrawl pour Claude Desktop automatiquement via [Smithery](https://smithery.ai/server/@mendableai/mcp-server-firecrawl) :

```
npx -y @smithery/cli install @mendableai/mcp-server-firecrawl --client claude
```

### Utilisation avec VS Code

Pour une installation en un clic, cliquez sur l’un des boutons d’installation ci-dessous… [![Installer avec NPX dans VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D) [![Installer avec NPX dans VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D&quality=insiders) Pour une installation manuelle, ajoutez le bloc JSON suivant à votre fichier de paramètres utilisateur (JSON) dans VS Code. Vous pouvez le faire en appuyant sur `Ctrl + Shift + P` et en tapant `Preferences: Open User Settings (JSON)`.

```
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "apiKey",
        "description": "Clé API Firecrawl",
        "password": true
      }
    ],
    "servers": {
      "firecrawl": {
        "command": "npx",
        "args": ["-y", "firecrawl-mcp"],
        "env": {
          "FIRECRAWL_API_KEY": "${input:apiKey}"
        }
      }
    }
  }
}
```

Vous pouvez également l’ajouter à un fichier nommé `.vscode/mcp.json` dans votre espace de travail. Cela vous permettra de partager la configuration avec d’autres :

```
{
  "inputs": [
    {
      "type": "promptString",
      "id": "apiKey",
      "description": "Clé API Firecrawl",
      "password": true
    }
  ],
  "servers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "${input:apiKey}"
      }
    }
  }
}
```

**Remarque :** Certains utilisateurs ont signalé des problèmes lors de l’ajout du serveur MCP à VS Code, du fait que VS Code valide le JSON à l’aide d’un format de schéma obsolète ([microsoft/vscode#155379](https://github.com/microsoft/vscode/issues/155379)). Cela affecte plusieurs outils MCP, dont Firecrawl. **Solution de contournement :** Désactivez la validation JSON dans VS Code pour permettre au serveur MCP de se charger correctement. Voir la discussion : [directus/directus#25906 (commentaire)](https://github.com/directus/directus/issues/25906#issuecomment-3369169513). Le serveur MCP continue de fonctionner correctement lorsqu’il est invoqué via d’autres extensions, mais le problème se produit spécifiquement lors de son enregistrement directement dans la liste des serveurs MCP. Nous prévoyons d’ajouter des recommandations une fois que VS Code aura mis à jour la validation de son schéma.

### Utilisation avec Claude Desktop

Ajoutez ce qui suit au fichier de configuration de Claude :

```
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

### Utilisation avec Claude Code

Ajoutez le serveur MCP Firecrawl à l’aide de la CLI Claude Code. Vous pouvez utiliser l’URL hébergée à distance ou l’exécuter localement :

```
# URL hébergée à distance (recommandé)
claude mcp add firecrawl --url https://mcp.firecrawl.dev/your-api-key/v2/mcp

# Ou exécuter localement via npx
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

### Utilisation avec Google Antigravity

Google Antigravity vous permet de configurer des serveurs MCP directement depuis son interface Agent. ![Installation MCP Antigravity](https://mintcdn.com/firecrawl/rxzXygFiVc0TDh5X/images/guides/mcp/antigravity-mcp-installation.gif?s=19297c26dad5ed191862571618ce8c0a)

1. Ouvrez la barre latérale Agent dans l’Editor ou la vue Agent Manager
2. Cliquez sur le menu « … » (More Actions) et sélectionnez **MCP Servers**
3. Sélectionnez **View raw config** pour ouvrir votre fichier local `mcp_config.json`
4. Ajoutez la configuration suivante :

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_FIRECRAWL_API_KEY"
      }
    }
  }
}
```

5. Enregistrez le fichier et cliquez sur **Refresh** dans l’interface MCP d’Antigravity pour voir les nouveaux outils.

Remplacez `YOUR_FIRECRAWL_API_KEY` par votre clé API à partir de [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys).

### Utilisation avec n8n

Pour connecter le serveur MCP de Firecrawl dans n8n :

1. Récupérez votre clé API Firecrawl à partir de [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)
2. Dans votre workflow n8n, ajoutez un nœud **AI Agent**
3. Dans la configuration du nœud **AI Agent**, ajoutez un nouveau **Tool**
4. Sélectionnez **MCP Client Tool** comme type d’outil
5. Saisissez l’Endpoint du serveur MCP (remplacez `{YOUR_FIRECRAWL_API_KEY}` par votre clé API) :

```
  https://mcp.firecrawl.dev/{YOUR_FIRECRAWL_API_KEY}/v2/mcp
```

6. Définissez **Server Transport** sur **HTTP Streamable**
7. Définissez **Authentication** sur **None**
8. Pour **Tools to include**, vous pouvez sélectionner **All**, **Selected** ou **All Except** – cela rendra disponibles les outils Firecrawl (scrape, crawl, map, search, extract, etc.)

Pour les déploiements auto-hébergés, exécutez le serveur MCP avec npx et activez le mode de transport HTTP :

```
env HTTP_STREAMABLE_SERVER=true \
    FIRECRAWL_API_KEY=fc-YOUR_API_KEY \
    FIRECRAWL_API_URL=YOUR_FIRECRAWL_INSTANCE \
    npx -y firecrawl-mcp
```

Cela démarre le serveur sur `http://localhost:3000/v2/mcp`, que vous pouvez utiliser comme endpoint dans votre workflow n8n. La variable d’environnement `HTTP_STREAMABLE_SERVER=true` est requise, car n8n a besoin d’un transport via HTTP.

## Configuration

### Variables d’environnement

#### Requis pour l’API Cloud

- `FIRECRAWL_API_KEY` : votre clé API Firecrawl
  
  - Requise lors de l’utilisation de l’API cloud (par défaut)
  - Facultative lors de l’utilisation d’une instance auto-hébergée avec `FIRECRAWL_API_URL`
- `FIRECRAWL_API_URL` (facultatif) : point de terminaison API personnalisé pour les instances auto-hébergées
  
  - Exemple : `https://firecrawl.your-domain.com`
  - Si elle n’est pas renseignée, l’API cloud sera utilisée (nécessite une clé API)

#### Configuration facultative

##### Configuration des relances

- `FIRECRAWL_RETRY_MAX_ATTEMPTS`: Nombre maximal de tentatives de relance (par défaut : 3)
- `FIRECRAWL_RETRY_INITIAL_DELAY`: Délai initial en millisecondes avant la première relance (par défaut : 1000)
- `FIRECRAWL_RETRY_MAX_DELAY`: Délai maximal en millisecondes entre les relances (par défaut : 10000)
- `FIRECRAWL_RETRY_BACKOFF_FACTOR`: Facteur de backoff exponentiel (par défaut : 2)

##### Surveillance de l’utilisation des crédits

- `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: Seuil d’avertissement pour l’utilisation des crédits (par défaut : 1000)
- `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: Seuil critique pour l’utilisation des crédits (par défaut : 100)

### Exemples de configuration

Pour l’utilisation de l’API cloud avec des tentatives de reprise personnalisées et le suivi des crédits :

```
# Requis pour l’API cloud
export FIRECRAWL_API_KEY=your-api-key

# Paramètres de nouvelle tentative (facultatif)
export FIRECRAWL_RETRY_MAX_ATTEMPTS=5        # Augmenter le nombre maximal de tentatives
export FIRECRAWL_RETRY_INITIAL_DELAY=2000    # Commencer avec un délai de 2 s
export FIRECRAWL_RETRY_MAX_DELAY=30000       # Délai maximal de 30 s
export FIRECRAWL_RETRY_BACKOFF_FACTOR=3      # Backoff plus agressif

# Surveillance des crédits (facultatif)
export FIRECRAWL_CREDIT_WARNING_THRESHOLD=2000    # Avertissement à 2000 crédits
export FIRECRAWL_CREDIT_CRITICAL_THRESHOLD=500    # Seuil critique à 500 crédits
```

Pour une instance auto‑hébergée :

```
# Requis pour l’auto‑hébergement
export FIRECRAWL_API_URL=https://firecrawl.your-domain.com

# Authentification facultative pour l’auto‑hébergement
export FIRECRAWL_API_KEY=your-api-key  # Si votre instance requiert une authentification

# Configuration personnalisée des tentatives
export FIRECRAWL_RETRY_MAX_ATTEMPTS=10
export FIRECRAWL_RETRY_INITIAL_DELAY=500     # Démarrer avec des tentatives plus rapides
```

### Configuration personnalisée avec Claude Desktop

Ajoutez ceci dans votre `claude_desktop_config.json` :

```
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY_HERE",

        "FIRECRAWL_RETRY_MAX_ATTEMPTS": "5",
        "FIRECRAWL_RETRY_INITIAL_DELAY": "2000",
        "FIRECRAWL_RETRY_MAX_DELAY": "30000",
        "FIRECRAWL_RETRY_BACKOFF_FACTOR": "3",

        "FIRECRAWL_CREDIT_WARNING_THRESHOLD": "2000",
        "FIRECRAWL_CREDIT_CRITICAL_THRESHOLD": "500"
      }
    }
  }
}
```

### Configuration système

Le serveur comporte plusieurs paramètres configurables pouvant être définis via des variables d’environnement. Voici les valeurs par défaut lorsqu’ils ne sont pas configurés :

```
const CONFIG = {
  retry: {
    maxAttempts: 3, // Number of retry attempts for rate-limited requests
    initialDelay: 1000, // Initial delay before first retry (in milliseconds)
    maxDelay: 10000, // Maximum delay between retries (in milliseconds)
    backoffFactor: 2, // Multiplier for exponential backoff
  },
  credit: {
    warningThreshold: 1000, // Warn when credit usage reaches this level
    criticalThreshold: 100, // Alerte critique lorsque l'utilisation des crédits atteint ce niveau
  },
};
```

Ces paramètres contrôlent :

1. **Comportement de réessai**
   
   - Réessaie automatiquement les requêtes ayant échoué à cause des limites de débit
   - Utilise un backoff exponentiel pour éviter de surcharger l’API
   - Exemple : avec les paramètres par défaut, les réessais seront effectués aux intervalles suivants :
     
     - 1ʳᵉ tentative de réessai : délai de 1 seconde
     - 2ᵉ tentative de réessai : délai de 2 secondes
     - 3ᵉ tentative de réessai : délai de 4 secondes (plafonné par `maxDelay`)
2. **Suivi de la consommation de crédits**
   
   - Suit la consommation de crédits de l’API pour l’utilisation de l’API cloud
   - Fournit des avertissements à des seuils définis
   - Aide à éviter les interruptions de service inattendues
   - Exemple : avec les paramètres par défaut :
     
     - Avertissement à 1 000 crédits restants
     - Alerte critique à 100 crédits restants

### Limitation de débit et traitement par lots

Le serveur exploite les fonctionnalités intégrées de Firecrawl en matière de limitation de débit et de traitement par lots :

- Gestion automatique de la limitation de débit avec backoff exponentiel
- Traitement parallèle efficace pour les opérations par lots
- Mise en file d’attente et régulation intelligente des requêtes
- Réessais automatiques en cas d’erreurs transitoires

Extraire le contenu d’une URL unique avec des options avancées.

```
{
  "name": "firecrawl_scrape",
  "arguments": {
    "url": "https://example.com",
    "formats": ["markdown"],
    "onlyMainContent": true,
    "waitFor": 1000,
    "mobile": false,
    "includeTags": ["article", "main"],
    "excludeTags": ["nav", "footer"],
    "skipTlsVerification": false
  }
}
```

Cartographier un site web pour découvrir toutes les URL indexées du site.

```
{
  "name": "firecrawl_map",
  "arguments": {
    "url": "https://example.com",
    "search": "blog",
    "sitemap": "include",
    "includeSubdomains": false,
    "limit": 100,
    "ignoreQueryParameters": true
  }
}
```

- `url`: L’URL de base du site web à cartographier
- `search`: Terme de recherche facultatif pour filtrer les URL
- `sitemap`: Contrôle l’utilisation du sitemap : « include », « skip » ou « only »
- `includeSubdomains`: Indique s’il faut inclure les sous-domaines dans la cartographie
- `limit`: Nombre maximal d’URL à retourner
- `ignoreQueryParameters`: Indique s’il faut ignorer les paramètres de requête lors de la cartographie

**Idéal pour :** Découvrir les URL d’un site web avant de décider quoi extraire ; trouver des sections spécifiques d’un site. **Renvoie :** Tableau d’URL trouvées sur le site.

Effectuez une recherche sur le web et, si besoin, extrayez le contenu des résultats.

```
{
  "name": "firecrawl_search",
  "arguments": {
    "query": "votre requête de recherche",
    "limit": 5,
    "location": "United States",
    "tbs": "qdr:m",
    "scrapeOptions": {
      "formats": ["markdown"],
      "onlyMainContent": true
    }
  }
}
```

- `query` : chaîne de requête de recherche (obligatoire)
- `limit` : nombre maximal de résultats à retourner
- `location` : emplacement géographique pour les résultats de recherche
- `tbs` : filtre temporel de recherche (par exemple, `qdr:d` pour les dernières 24 heures, `qdr:w` pour la dernière semaine, `qdr:m` pour le dernier mois)
- `filter` : filtre de recherche supplémentaire
- `sources` : tableau des types de sources à interroger (`web`, `images`, `news`)
- `scrapeOptions` : options de scraping des pages de résultats de recherche
- `enterprise` : tableau d’options d’entreprise (`default`, `anon`, `zdr`)

Démarre un crawl asynchrone avec des options avancées.

```
{
  "name": "firecrawl_crawl",
  "arguments": {
    "url": "https://example.com",
    "maxDiscoveryDepth": 2,
    "limit": 100,
    "allowExternalLinks": false,
    "deduplicateSimilarURLs": true
  }
}
```

### 5. Vérifier l’état du crawl (`firecrawl_check_crawl_status`)

Vérifiez l’état d’une tâche de crawl.

```
{
  "name": "firecrawl_check_crawl_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

**Renvoie :** le statut et l’avancement du job de crawl, y compris les résultats le cas échéant.

Extrait des informations structurées depuis des pages web en utilisant les capacités des LLM. Prend en charge aussi bien l’IA dans le cloud que l’extraction avec des LLM auto-hébergés.

```
{
  "name": "firecrawl_extract",
  "arguments": {
    "urls": ["https://example.com/page1", "https://example.com/page2"],
    "prompt": "Extract product information including name, price, and description",
    "schema": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "price": { "type": "number" },
        "description": { "type": "string" }
      },
      "required": ["name", "price"]
    },
    "allowExternalLinks": false,
    "enableWebSearch": false,
    "includeSubdomains": false
  }
}
```

Exemple de réponse :

```
{
  "content": [
    {
      "type": "text",
      "text": {
        "name": "Example Product",
        "price": 99.99,
        "description": "This is an example product description"
      }
    }
  ],
  "isError": false
}
```

- `urls`: Liste d’URL à partir desquelles extraire des informations
- `prompt`: Prompt personnalisé pour l’extraction par le LLM
- `schema`: Schéma JSON pour l’extraction de données structurées
- `allowExternalLinks`: Autoriser l’extraction à partir de liens externes
- `enableWebSearch`: Activer la recherche sur le web pour obtenir un contexte supplémentaire
- `includeSubdomains`: Inclure les sous-domaines dans l’extraction

Lors de l’utilisation d’une instance auto‑hébergée, l’extraction utilisera le LLM que vous avez configuré. Pour l’API cloud, elle utilise le service LLM géré de Firecrawl.

Agent autonome de recherche web qui parcourt Internet de manière indépendante, recherche des informations, navigue entre les pages et extrait des données structurées en fonction de votre requête. Ce processus s’exécute de façon asynchrone : il renvoie immédiatement un ID de job, puis vous interrogez périodiquement `firecrawl_agent_status` pour savoir quand il est terminé et récupérer les résultats.

```
{
  "name": "firecrawl_agent",
  "arguments": {
    "prompt": "Find the top 5 AI startups founded in 2024 and their funding amounts",
    "schema": {
      "type": "object",
      "properties": {
        "startups": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": { "type": "string" },
              "funding": { "type": "string" },
              "founded": { "type": "string" }
            }
          }
        }
      }
    }
  }
}
```

Vous pouvez également fournir des URL spécifiques sur lesquelles l’agent devra se concentrer :

```
{
  "name": "firecrawl_agent",
  "arguments": {
    "urls": ["https://docs.firecrawl.dev", "https://firecrawl.dev/pricing"],
    "prompt": "Compare the features and pricing information from these pages"
  }
}
```

- `prompt`: Description en langage naturel des données dont vous avez besoin (obligatoire, 10 000 caractères maximum)
- `urls`: Tableau optionnel d’URL pour concentrer l’agent sur des pages spécifiques
- `schema`: Schéma JSON optionnel pour une sortie structurée

**Idéal pour :** Tâches de recherche complexes où vous ne connaissez pas les URL exactes ; collecte de données issues de multiples sources ; recherche d’informations dispersées sur le web ; extraction de données à partir de SPA lourdes en JavaScript qui échouent avec un scraping classique. **Retourne :** ID de tâche pour vérifier l’état d’avancement. Utilisez `firecrawl_agent_status` pour interroger les résultats.

### 8. Vérifier l’état de l’agent (`firecrawl_agent_status`)

Vérifiez l’état d’une tâche d’agent et récupérez les résultats une fois terminée. Effectuez un polling toutes les 15 à 30 secondes et continuez pendant au moins 2 à 3 minutes avant de considérer la requête comme échouée.

```
{
  "name": "firecrawl_agent_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

#### Options de statut de l’agent :

- `id`: L’ID de tâche d’agent renvoyé par `firecrawl_agent` (obligatoire)

**Statuts possibles :**

- `processing`: L’agent est encore en cours de recherche — continuer à interroger
- `completed`: Recherche terminée — la réponse inclut les données extraites
- `failed`: Une erreur s’est produite

**Retourne :** Le statut, la progression et les résultats (si terminé) de la tâche d’agent.

### 9. Créer une session de navigateur (`firecrawl_browser_create`)

Crée une session de navigateur persistante pour exécuter du code via CDP (Chrome DevTools Protocol).

```
{
  "name": "firecrawl_browser_create",
  "arguments": {
    "ttl": 120,
    "activityTtl": 60
  }
}
```

#### Options de création du navigateur :

- `ttl` : Durée de vie totale de la session en secondes (30-3600, facultatif)
- `activityTtl` : Délai d’inactivité en secondes (10-3600, facultatif)

**Idéal pour :** exécuter du code (Python/JS) qui interagit avec une page de navigateur active, l’automatisation du navigateur en plusieurs étapes, des sessions avec profils qui restent valides sur plusieurs appels d’outils. **Renvoie :** ID de session, URL CDP et URL de vue en direct.

### 10. Exécuter du code dans le navigateur (`firecrawl_browser_execute`)

Exécute du code dans une session de navigation active. Prend en charge les commandes agent-browser (bash), Python ou JavaScript.

```
{
  "name": "firecrawl_browser_execute",
  "arguments": {
    "sessionId": "session-id-here",
    "code": "agent-browser open https://example.com",
    "language": "bash"
  }
}
```

Exemple en Python avec Playwright :

```
{
  "name": "firecrawl_browser_execute",
  "arguments": {
    "sessionId": "session-id-here",
    "code": "await page.goto('https://example.com')\ntitle = await page.title()\nprint(title)",
    "language": "python"
  }
}
```

#### Options d’exécution du navigateur :

- `sessionId`: L’ID de session du navigateur (obligatoire)
- `code`: Le code à exécuter (obligatoire)
- `language`: `bash`, `python` ou `node` (optionnel, `bash` par défaut)

**Commandes courantes d’agent-browser (bash) :**

- `agent-browser open <url>` — Accéder à l’URL
- `agent-browser snapshot` — Récupérer l’arbre d’accessibilité avec références cliquables
- `agent-browser click @e5` — Cliquer sur un élément par référence issue du snapshot
- `agent-browser type @e3 "text"` — Saisir du texte dans l’élément
- `agent-browser screenshot [path]` — Prendre une capture d’écran
- `agent-browser scroll down` — Faire défiler la page vers le bas
- `agent-browser wait 2000` — Attendre 2 secondes

**Renvoie :** Le résultat de l’exécution, incluant `stdout`, `stderr` et le code de sortie.

### 11. Supprimer une session de navigateur (`firecrawl_browser_delete`)

Supprime une session de navigateur.

```
{
  "name": "firecrawl_browser_delete",
  "arguments": {
    "sessionId": "session-id-here"
  }
}
```

#### Options de suppression du navigateur :

- `sessionId`: L’ID de session navigateur à supprimer (obligatoire)

**Renvoie :** Une confirmation de réussite.

### 12. Lister les sessions de navigateur (`firecrawl_browser_list`)

Affiche la liste des sessions de navigateur, avec possibilité de filtrer par statut.

```
{
  "name": "firecrawl_browser_list",
  "arguments": {
    "status": "actif"
  }
}
```

#### Options de liste de navigateurs :

- `status`: Filtrer par statut de session — `active` ou `destroyed` (optionnel)

**Renvoie :** Tableau de sessions de navigateur.

## Système de journalisation

Le serveur inclut une journalisation complète :

- État et progression des opérations
- Indicateurs de performance
- Suivi de l’utilisation des crédits
- Suivi des limites de débit
- Conditions d’erreur

Exemples de messages de journal :

```
[INFO] Firecrawl MCP Server initialized successfully
[INFO] Starting scrape for URL: https://example.com
[INFO] Starting crawl for URL: https://example.com
[WARNING] L'utilisation des crédits a atteint le seuil d'alerte
[ERROR] Rate limit exceeded, retrying in 2s...
```

## Gestion des erreurs

Le serveur propose une gestion robuste des erreurs :

- Nouveaux essais automatiques en cas d’erreurs transitoires
- Gestion des limites de débit avec backoff
- Messages d’erreur détaillés
- Alertes sur l’utilisation des crédits
- Résilience du réseau

Exemple de réponse d’erreur :

```
{
  "content": [
    {
      "type": "text",
      "text": "Erreur : Limite de débit dépassée. Nouvelle tentative dans 2 secondes..."
    }
  ],
  "isError": true
}
```

## Développement

```
# Installer les dépendances
npm install

# Build
npm run build

# Run tests
npm test
```

### Contribution

1. Créez un fork du dépôt
2. Créez une branche pour votre fonctionnalité
3. Exécutez les tests : `npm test`
4. Ouvrez une pull request

### Merci aux contributeurs

Merci à [@vrknetha](https://github.com/vrknetha) et [@cawstudios](https://caw.tech) pour la mise en œuvre initiale ! Merci à MCP.so et Klavis AI pour l’hébergement, ainsi qu’à [@gstarwd](https://github.com/gstarwd), [@xiangkaiz](https://github.com/xiangkaiz) et [@zihaolin96](https://github.com/zihaolin96) d’avoir intégré notre serveur.

## Licence

Licence MIT — voir le fichier LICENSE pour plus de détails