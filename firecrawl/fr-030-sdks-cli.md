---
title: CLI | Firecrawl
url: https://docs.firecrawl.dev/fr/sdks/cli
source: sitemap
fetched_at: 2026-03-23T07:23:35.927202-03:00
rendered_js: false
word_count: 1242
summary: This document provides a comprehensive guide to installing, configuring, and utilizing the Firecrawl CLI for web scraping, site mapping, and web searching.
tags:
    - firecrawl
    - cli-reference
    - web-scraping
    - data-extraction
    - api-integration
    - automation
category: reference
---

## Installation

Si vous utilisez un agent IA comme Claude Code, vous pouvez installer le skill Firecrawl ci-dessous et l’agent pourra le configurer pour vous.

```
npx -y firecrawl-cli@latest init --all --browser
```

- `--all` installe le skill Firecrawl pour tous les agents de codage IA détectés
- `--browser` ouvre automatiquement le navigateur pour l’authentification Firecrawl

Vous pouvez également installer manuellement la CLI Firecrawl au niveau global avec npm :

```
# Installer globalement avec npm
npm install -g firecrawl-cli
```

## Authentification

Avant d’utiliser la CLI, vous devez vous authentifier avec votre clé API Firecrawl.

### Connexion

```
# Interactive login (opens browser or prompts for API key)
firecrawl login

# Connexion avec authentification par navigateur (recommandé pour les agents)
firecrawl login --browser

# Login with API key directly
firecrawl login --api-key fc-YOUR-API-KEY

# Or set via environment variable
export FIRECRAWL_API_KEY=fc-YOUR-API-KEY
```

### Afficher la configuration

```
# Voir la configuration actuelle et le statut d'authentification
firecrawl view-config
```

### Déconnexion

```
# Effacer les identifiants enregistrés
firecrawl logout
```

### Auto-hébergé / Développement local

Pour les instances Firecrawl auto-hébergées ou le développement local, utilisez l’option `--api-url` :

```
# Utiliser une instance locale de Firecrawl (aucune clé API requise)
firecrawl --api-url http://localhost:3002 scrape https://example.com

# Or set via environment variable
export FIRECRAWL_API_URL=http://localhost:3002
firecrawl scrape https://example.com

# Configure and persist the custom API URL
firecrawl config --api-url http://localhost:3002
```

Lorsque vous utilisez une URL d’API personnalisée (toute URL différente de `https://api.firecrawl.dev`), l’authentification par clé d’API est automatiquement contournée, ce qui vous permet d’utiliser des instances locales sans clé d’API.

### Vérifier l’état

Vérifiez l’installation, l’authentification et affichez les limites de débit :

Sortie une fois prête :

```
  🔥 firecrawl cli v1.1.1

  ● Authenticated via FIRECRAWL_API_KEY
  Concurrency: 0/100 jobs (parallel scrape limit)
  Credits: 500,000 remaining
```

- **Concurrence** : Nombre maximal de tâches en parallèle. Exécutez des opérations parallèles au plus près de cette limite, sans la dépasser.
- **Crédits** : Crédits API restants. Chaque opération de `scrape`/`crawl` consomme des crédits.

## Commandes

### Scrape

Analysez une seule URL et extrayez son contenu dans différents formats.

```
# Scraper une URL (par défaut : sortie markdown)
firecrawl https://example.com

# Ou utiliser la commande scrape explicite
firecrawl scrape https://example.com

# Recommandé : utiliser --only-main-content pour une sortie propre sans nav/footer
firecrawl https://example.com --only-main-content
```

#### Formats de sortie

```
# Obtenir la sortie HTML
firecrawl https://example.com --html

# Formats multiples (retourne du JSON)
firecrawl https://example.com --format markdown,links

# Obtenir les images d'une page
firecrawl https://example.com --format images

# Obtenir un résumé du contenu de la page
firecrawl https://example.com --format summary

# Suivre les modifications sur une page
firecrawl https://example.com --format changeTracking

# Formats disponibles : markdown, html, rawHtml, links, screenshot, json, images, summary, changeTracking, attributes, branding
```

#### Options de scraping

```
# Extraire uniquement le contenu principal (supprime les menus de navigation, pieds de page)
firecrawl https://example.com --only-main-content

# Wait for JavaScript rendering
firecrawl https://example.com --wait-for 3000

# Take a screenshot
firecrawl https://example.com --screenshot

# Include/exclude specific HTML tags
firecrawl https://example.com --include-tags article,main
firecrawl https://example.com --exclude-tags nav,footer

# Save output to file
firecrawl https://example.com -o output.md

# Pretty print JSON output
firecrawl https://example.com --format markdown,links --pretty

# Force JSON output even with single format
firecrawl https://example.com --json

# Show request timing information
firecrawl https://example.com --timing
```

**Options disponibles :**

OptionForme courteDescription`--url <url>``-u`URL à scraper (alternative à l’argument positionnel)`--format <formats>``-f`formats de sortie (séparés par des virgules) : `markdown`, `html`, `rawHtml`, `links`, `screenshot`, `json`, `images`, `summary`, `suiviDesModifications`, `attributes`, `branding``--html``-H`Raccourci pour `--format html``--only-main-content`Extraire uniquement le contenu principal`--wait-for <ms>`Temps d’attente en millisecondes pour le rendu JS`--screenshot`Prendre une capture d’écran`--include-tags <tags>`Balises HTML à inclure (séparées par des virgules)`--exclude-tags <tags>`Balises HTML à exclure (séparées par des virgules)`--output <path>``-o`Enregistrer la sortie dans un fichier`--json`Forcer la sortie JSON même avec un seul format`--pretty`Afficher la sortie JSON de manière lisible`--timing`Afficher le temps de la requête et d’autres informations utiles

* * *

### Recherche

Recherchez sur le Web et, si besoin, extrayez le contenu des résultats.

```
# Search the web
firecrawl search "web scraping tutorials"

# Limit results
firecrawl search "AI news" --limit 10

# Afficher les résultats avec formatage
firecrawl search "machine learning" --pretty
```

#### Options de recherche

```
# Search specific sources
firecrawl search "AI" --sources web,news,images

# Search with category filters
firecrawl search "react hooks" --categories github
firecrawl search "machine learning" --categories research,pdf

# Time-based filtering
firecrawl search "tech news" --tbs qdr:h   # Last hour
firecrawl search "tech news" --tbs qdr:d   # Last day
firecrawl search "tech news" --tbs qdr:w   # Dernière semaine
firecrawl search "tech news" --tbs qdr:m   # Last month
firecrawl search "tech news" --tbs qdr:y   # Last year

# Location-based search
firecrawl search "restaurants" --location "Berlin,Germany" --country DE

# Search and scrape results
firecrawl search "documentation" --scrape --scrape-formats markdown

# Save to file
firecrawl search "firecrawl" --pretty -o results.json
```

**Options disponibles :**

OptionDescription`--limit <number>`Nombre maximal de résultats (par défaut : 5, max : 100)`--sources <sources>`Sources à interroger : `web`, `images`, `news` (séparées par des virgules)`--categories <categories>`Filtrer par catégorie : `github`, `research`, `pdf` (séparées par des virgules)`--tbs <value>`Filtre temporel : `qdr:h` (heure), `qdr:d` (jour), `qdr:w` (semaine), `qdr:m` (mois), `qdr:y` (année)`--location <location>`Ciblage géographique (p. ex. “Berlin,Germany”)`--country <code>`Code de pays ISO (par défaut : US)`--timeout <ms>`Délai d’expiration en millisecondes (par défaut : 60000)`--ignore-invalid-urls`Exclure les URL invalides pour d’autres endpoints Firecrawl`--scrape`Scraper les résultats de recherche`--scrape-formats <formats>`Formats pour le contenu extrait (par défaut : markdown)`--only-main-content`Inclure uniquement le contenu principal lors du scraping (par défaut : true)`--json`Résultat au format JSON`--output <path>`Enregistrer le résultat dans un fichier`--pretty`Affichage JSON formaté

* * *

### Map

Découvrez rapidement toutes les URL d’un site.

```
# Découvrir toutes les URL d'un site web
firecrawl map https://example.com

# Output as JSON
firecrawl map https://example.com --json

# Limit number of URLs
firecrawl map https://example.com --limit 500
```

#### Options de la commande Map

```
# Filter URLs by search query
firecrawl map https://example.com --search "blog"

# Include subdomains
firecrawl map https://example.com --include-subdomains

# Contrôler l'utilisation du sitemap
firecrawl map https://example.com --sitemap include   # Utiliser le sitemap
firecrawl map https://example.com --sitemap skip      # Ignorer le sitemap
firecrawl map https://example.com --sitemap only      # Utiliser uniquement le sitemap

# Ignore query parameters (dedupe URLs)
firecrawl map https://example.com --ignore-query-parameters

# Wait for map to complete with timeout
firecrawl map https://example.com --wait --timeout 60

# Save to file
firecrawl map https://example.com -o urls.txt
firecrawl map https://example.com --json --pretty -o urls.json
```

**Options disponibles :**

OptionDescription`--url <url>`URL à cartographier (alternative à l’argument positionnel)`--limit <number>`Nombre maximal d’URL à découvrir`--search <query>`Filtrer les URL selon une requête de recherche`--sitemap <mode>`Gestion du sitemap : `include`, `skip`, `only``--include-subdomains`Inclure les sous-domaines`--ignore-query-parameters`Considérer les URL avec des paramètres différents comme identiques`--wait`Attendre la fin de l’opération de cartographie`--timeout <seconds>`Délai d’expiration en secondes`--json`Résultat au format JSON`--output <path>`Enregistrer le résultat dans un fichier`--pretty`Affichage JSON mis en forme

* * *

### Navigateur

Permettez à vos agents d’interagir avec le web à l’aide d’un navigateur en bac à sable sécurisé. Lancez des sessions de navigateur dans le cloud et exécutez du code Python, JavaScript ou bash à distance. Chaque session exécute une instance complète de Chromium — aucune installation de navigateur en local n’est requise. Le code s’exécute côté serveur avec un objet `page` [Playwright](https://playwright.dev/) préconfiguré et prêt à l’emploi.

```
# Launch a cloud browser session
firecrawl browser launch-session

# Exécuter des commandes agent-browser (par défaut - "agent-browser" est automatiquement préfixé)
firecrawl browser execute "open https://example.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "click @e5"
firecrawl browser execute "scrape"

# Execute Playwright Python code
firecrawl browser execute --python 'await page.goto("https://example.com")
print(await page.title())'

# Execute Playwright JavaScript code
firecrawl browser execute --node 'await page.goto("https://example.com"); console.log(await page.title());'

# List all sessions (or: list active / list destroyed)
firecrawl browser list

# Close the active session
firecrawl browser close
```

#### Options du navigateur

```
# Launch with custom TTL (10 minutes) and live view
firecrawl browser launch-session --ttl 600 --stream

# Launch with inactivity timeout
firecrawl browser launch-session --ttl 120 --ttl-inactivity 60

# Commandes agent-browser (par défaut - "agent-browser" est automatiquement préfixé)
firecrawl browser execute "open https://news.ycombinator.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "click @e3"
firecrawl browser execute "scrape"

# Playwright Python - navigate, interact, extract
firecrawl browser execute --python '
await page.goto("https://news.ycombinator.com")
items = await page.query_selector_all(".titleline > a")
for item in items[:5]:
    print(await item.text_content())
'

# Playwright JavaScript - same page object
firecrawl browser execute --node '
await page.goto("https://example.com");
const title = await page.title();
console.log(title);
'

# Explicit bash mode - runs in the sandbox
firecrawl browser execute --bash "agent-browser snapshot"

# Target a specific session
firecrawl browser execute --session <id> --python 'print(await page.title())'

# Save output to file
firecrawl browser execute "scrape" -o result.txt

# Close a specific session
firecrawl browser close --session <id>

# List sessions (all / active / destroyed)
firecrawl browser list
firecrawl browser list active --json
```

**Sous-commandes :**

Sous-commandeDescription`launch-session`Lance une nouvelle session de navigateur cloud (renvoie l’ID de session, l’URL CDP et l’URL de vue en direct)`execute <code>`Exécute du code Playwright Python/JS ou des commandes bash dans une session`list [status]`Répertorie les sessions de navigateur (filtrage par `active` ou `destroyed`)`close`Ferme une session de navigateur

**Options d’exécution :**

OptionDescription`--bash`Exécute des commandes bash à distance dans le bac à sable (par défaut). [agent-browser](https://github.com/vercel-labs/agent-browser) (40+ commandes) est préinstallé et automatiquement préfixé. `CDP_URL` est injecté automatiquement pour qu’agent-browser se connecte à votre session sans configuration supplémentaire. Option recommandée pour les agents d’IA.`--python`Exécute du code Playwright Python. Un objet Playwright `page` est disponible — utilisez `await page.goto()`, `await page.title()`, etc.`--node`Exécute du code Playwright JavaScript. Le même objet `page` est disponible.`--session <id>`Cible une session spécifique (par défaut : session active)

**Options de lancement :**

OptionDescription`--ttl <seconds>`TTL total de la session (par défaut : 600, plage : 30–3600)`--ttl-inactivity <seconds>`Fermeture automatique après inactivité (plage : 10–3600)`--profile <name>`Nom du profil (enregistre et réutilise l’état du navigateur entre les sessions)`--no-save-changes`Charge les données de profil existantes sans enregistrer les modifications`--stream`Active le streaming de la vue en direct

**Options communes :**

OptionDescription`--output <path>`Enregistre la sortie dans un fichier`--json`Produit la sortie au format JSON

* * *

### Crawl

Lancer un crawl sur l’ensemble d’un site web à partir d’une URL.

```
# Start a crawl (returns job ID immediately)
firecrawl crawl https://example.com

# Wait for crawl to complete
firecrawl crawl https://example.com --wait

# Attendre avec indicateur de progression
firecrawl crawl https://example.com --wait --progress
```

#### Consulter l’état du crawl

```
# Vérifier le statut du crawl avec l'ID de tâche
firecrawl crawl <job-id>

# Exemple avec un véritable ID de tâche
firecrawl crawl 550e8400-e29b-41d4-a716-446655440000
```

#### Options de crawl

```
# Limit crawl depth and pages
firecrawl crawl https://example.com --limit 100 --max-depth 3 --wait

# Include only specific paths
firecrawl crawl https://example.com --include-paths /blog,/docs --wait

# Exclude specific paths
firecrawl crawl https://example.com --exclude-paths /admin,/login --wait

# Include subdomains
firecrawl crawl https://example.com --allow-subdomains --wait

# Crawl entire domain
firecrawl crawl https://example.com --crawl-entire-domain --wait

# Rate limiting
firecrawl crawl https://example.com --delay 1000 --max-concurrency 2 --wait

# Intervalle de polling et délai d'expiration personnalisés
firecrawl crawl https://example.com --wait --poll-interval 10 --timeout 300

# Save results to file
firecrawl crawl https://example.com --wait --pretty -o results.json
```

**Options disponibles :**

OptionDescription`--url <url>`URL à explorer (alternative à l’argument positionnel)`--wait`Attendre la fin du crawl`--progress`Afficher un indicateur de progression pendant l’attente`--poll-interval <seconds>`Intervalle d’interrogation (par défaut : 5)`--timeout <seconds>`Délai d’expiration de l’attente`--status`Vérifier l’état d’une tâche de crawl existante`--limit <number>`Nombre maximal de pages à explorer`--max-depth <number>`Profondeur maximale du crawl`--include-paths <paths>`Chemins à inclure (séparés par des virgules)`--exclude-paths <paths>`Chemins à exclure (séparés par des virgules)`--sitemap <mode>`Gestion du sitemap : `include`, `skip`, `only``--allow-subdomains`Inclure les sous-domaines`--allow-external-links`Suivre les liens externes`--crawl-entire-domain`Explorer l’ensemble du domaine`--ignore-query-parameters`Considérer les URL avec des paramètres différents comme identiques`--delay <ms>`Délai entre les requêtes`--max-concurrency <n>`Nombre maximal de requêtes simultanées`--output <path>`Enregistrer le résultat dans un fichier`--pretty`Afficher la sortie JSON formatée

* * *

### Agent

Recherchez et collectez des données sur le web à l’aide de prompts en langage naturel.

```
# Basic usage - URLs are optional
firecrawl agent "Find the top 5 AI startups and their funding amounts" --wait

# Focus on specific URLs
firecrawl agent "Compare pricing plans" --urls https://slack.com/pricing,https://teams.microsoft.com/pricing --wait

# Use a schema for structured output
firecrawl agent "Obtenez des informations sur l'entreprise" --urls https://example.com --schema '{"name": "string", "founded": "number"}' --wait

# Use schema from a file
firecrawl agent "Get product details" --urls https://example.com --schema-file schema.json --wait
```

#### Options de l’agent

```
# Use Spark 1 Pro for higher accuracy
firecrawl agent "Competitive analysis across multiple domains" --model spark-1-pro --wait

# Set max credits to limit costs
firecrawl agent "Collecter les informations de contact des sites web d'entreprises" --max-credits 100 --wait

# Check status of an existing job
firecrawl agent <job-id> --status

# Custom polling interval and timeout
firecrawl agent "Summarize recent blog posts" --wait --poll-interval 10 --timeout 300

# Save output to file
firecrawl agent "Find pricing information" --urls https://example.com --wait -o pricing.json --pretty
```

**Options disponibles :**

OptionDescription`--urls <urls>`Liste facultative d’URL sur lesquelles concentrer l’agent (séparées par des virgules)`--model <model>`Modèle à utiliser : `spark-1-mini` (par défaut, 60 % moins cher) ou `spark-1-pro` (meilleure précision)`--schema <json>`Schéma JSON pour la sortie structurée (chaîne JSON intégrée)`--schema-file <path>`Chemin vers le fichier de schéma JSON pour la sortie structurée`--max-credits <number>`Nombre maximal de crédits à utiliser (la tâche échoue si la limite est atteinte)`--status`Consulter l’état d’une tâche d’agent existante`--wait`Attendre que l’agent ait terminé avant de renvoyer les résultats`--poll-interval <seconds>`Intervalle d’interrogation pendant l’attente (par défaut : 5)`--timeout <seconds>`Délai d’attente maximal (par défaut : aucun délai)`--output <path>`Enregistrer la sortie dans un fichier`--json`Sortie au format JSON

* * *

### Utilisation des crédits

Consultez le solde et l’utilisation des crédits de votre équipe.

```
# Voir l'utilisation des crédits
firecrawl credit-usage

# Sortie en JSON
firecrawl credit-usage --json --pretty
```

* * *

### Version

Afficher la version de la CLI.

```
firecrawl version
# ou
firecrawl --version
```

## Options globales

Ces options sont disponibles pour toutes les commandes :

OptionRaccourciDescription`--status`Afficher la version, l’état d’authentification, le niveau de parallélisme et les crédits`--api-key <key>``-k`Ignorer la clé d’API enregistrée pour cette commande`--api-url <url>`Utiliser une URL d’API personnalisée (pour l’auto-hébergement ou le développement local)`--help``-h`Afficher l’aide pour une commande`--version``-V`Afficher la version de la CLI

## Gestion de la sortie

La CLI écrit sur stdout par défaut, ce qui facilite l’utilisation de pipes ou la redirection :

```
# Pipe markdown to another command
firecrawl https://example.com | head -50

# Redirect to a file
firecrawl https://example.com > output.md

# Save JSON with pretty formatting
firecrawl https://example.com --format markdown,links --pretty -o data.json
```

### Comportement des formats

- **Un seul format** : renvoie le contenu brut (texte markdown, HTML, etc.)
- **Plusieurs formats** : renvoie du JSON avec toutes les données demandées

```
# Sortie markdown brute
firecrawl https://example.com --format markdown

# Sortie JSON avec plusieurs formats
firecrawl https://example.com --format markdown,links
```

## Exemples

### Scraping rapide

```
# Récupérer le contenu markdown d'une URL (utiliser --only-main-content pour une sortie épurée)
firecrawl https://docs.firecrawl.dev --only-main-content

# Get HTML content
firecrawl https://example.com --html -o page.html
```

### Exploration complète du site

```
# Crawle un site de docs avec des limites
firecrawl crawl https://docs.example.com --limit 50 --max-depth 2 --wait --progress -o docs.json
```

### Découverte de sites web

```
# Trouver tous les articles de blog
firecrawl map https://example.com --search "blog" -o blog-urls.txt
```

### Flux de recherche

```
# Rechercher et scraper les résultats pour la recherche
firecrawl search "machine learning best practices 2024" --scrape --scrape-formats markdown --pretty
```

### Agent

```
# Les URL sont facultatives
firecrawl agent "Find the top 5 AI startups and their funding amounts" --wait

# Se concentrer sur des URL spécifiques
firecrawl agent "Compare pricing plans" --urls https://slack.com/pricing,https://teams.microsoft.com/pricing --wait
```

### Automatisation du navigateur Web

```
# Launch a session, scrape a page, and close
firecrawl browser launch-session
firecrawl browser execute "open https://news.ycombinator.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "scrape"
firecrawl browser close

# Utiliser agent-browser via le mode bash (par défaut — recommandé pour les agents IA)
firecrawl browser launch-session
firecrawl browser execute "open https://example.com"
firecrawl browser execute "snapshot"
# snapshot returns @ref IDs — use them to interact
firecrawl browser execute "click @e5"
firecrawl browser execute "fill @e3 'search query'"
firecrawl browser execute "scrape"
# Run --help to see all 40+ commands
firecrawl browser execute --bash "agent-browser --help"
firecrawl browser close

# Extract URLs from search results
jq -r '.data.web[].url' search-results.json

# Récupérer les titres des résultats de recherche
jq -r '.data.web[] | "\(.title): \(.url)"' search-results.json

# Extract links and process with jq
firecrawl https://example.com --format links | jq '.links[].url'

# Count URLs from map
firecrawl map https://example.com | wc -l
```

## Télémétrie

La CLI collecte des données d’utilisation anonymes lors de l’authentification afin d’améliorer le produit :

- Version de la CLI, système d’exploitation et version de Node.js
- Détection de l’outil de développement (par exemple, Cursor, VS Code, Claude Code)

**Aucune donnée relative aux commandes, aux URL ou au contenu des fichiers n’est collectée via la CLI.** Pour désactiver la télémétrie, définissez la variable d’environnement :

```
export FIRECRAWL_NO_TELEMETRY=1
```

## Open Source

La CLI et la Skill Firecrawl sont open source et disponibles sur GitHub : [firecrawl/cli](https://github.com/firecrawl/cli)

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’onboarding automatisé.