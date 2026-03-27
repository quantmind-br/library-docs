---
title: Exécuter en local | Firecrawl
url: https://docs.firecrawl.dev/fr/contributing/guide
source: sitemap
fetched_at: 2026-03-23T07:31:46.281702-03:00
rendered_js: false
word_count: 372
summary: Ce guide décrit les étapes nécessaires pour configurer et exécuter localement le serveur d'API Firecrawl, incluant la gestion des dépendances, la configuration de la base de données et le démarrage des services.
tags:
    - installation
    - firecrawl
    - api
    - developpement-local
    - postgresql
    - redis
    - docker
category: guide
---

Ce guide vous explique comment exécuter le serveur d’API Firecrawl sur votre machine locale. Suivez ces étapes pour configurer l’environnement de développement, démarrer les services et envoyer votre première requête. Si vous contribuez au projet, le processus suit les conventions standard de l’open source : faites un fork du dépôt, apportez vos modifications, exécutez les tests, puis ouvrez une pull request. Pour toute question ou pour obtenir de l’aide pour démarrer, contactez [help@firecrawl.com](mailto:help@firecrawl.com) ou [soumettez une issue](https://github.com/mendableai/firecrawl/issues).

## Prérequis

Installez les éléments suivants avant de continuer :

DépendanceObligatoireGuide d’installationNode.jsOui[nodejs.org](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)pnpm (v9+)Oui[pnpm.io](https://pnpm.io/installation)RedisOui[redis.io](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)PostgreSQLOuiVia Docker (voir ci-dessous) ou installation directeDockerFacultatifNécessaire pour configurer le conteneur PostgreSQL

## Configurer la base de données

Vous devez disposer d’une base de données PostgreSQL initialisée avec le schéma situé à `apps/nuq-postgres/nuq.sql`. Le moyen le plus simple consiste à utiliser l’image Docker dans `apps/nuq-postgres`. Une fois Docker lancé, construisez et démarrez le conteneur :

```
docker build -t nuq-postgres apps/nuq-postgres

docker run --name nuqdb \
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  -v nuq-data:/var/lib/postgresql/data \
  -d nuq-postgres
```

## Configurer les variables d’environnement

Copiez le modèle suivant pour créer votre fichier `.env` dans le répertoire `apps/api/` :

```
cp apps/api/.env.example apps/api/.env
```

Pour une configuration locale minimale sans authentification ni services optionnels (analyse de PDF, blocage de JS, fonctionnalités d’IA), utilisez la configuration suivante :

```
# ===== Requis =====
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0
REDIS_URL=redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379

## Pour activer l'authentification DB, vous devez configurer supabase.
USE_DB_AUTHENTICATION=false

## Connexion PostgreSQL pour la file d'attente — à modifier si les identifiants, l'hôte ou la base de données diffèrent
NUQ_DATABASE_URL=postgres://postgres:postgres@localhost:5433/postgres

# ===== Optionnel =====
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=
# TEST_API_KEY=               # À définir si vous avez configuré l'authentification et souhaitez tester avec une vraie clé API
# OPENAI_API_KEY=             # Requis pour les fonctionnalités dépendant des LLM (génération d'attributs alt d'image, etc.)
# BULL_AUTH_KEY=@
# PLAYWRIGHT_MICROSERVICE_URL= # À définir pour utiliser un fallback Playwright
# LLAMAPARSE_API_KEY=         # À définir pour analyser les PDF avec LlamaParse
# SLACK_WEBHOOK_URL=          # À définir pour envoyer des messages d'état du serveur sur Slack
# POSTHOG_API_KEY=            # À définir pour envoyer des événements PostHog comme les journaux de tâches
# POSTHOG_HOST=               # À définir pour envoyer des événements PostHog comme les journaux de tâches
```

## Installer les dépendances

Depuis le répertoire `apps/api/`, installez les packages avec pnpm :

## Démarrer les services

Vous avez besoin de trois sessions de terminal ouvertes simultanément : Redis, le serveur d’API et un terminal pour envoyer des requêtes.

### Terminal 1 — Redis

Démarrez le serveur Redis depuis n’importe où dans le projet :

### Terminal 2 — Serveur API

Placez-vous dans `apps/api/` puis démarrez le service :

Cela démarre le serveur API et les workers responsables du traitement des jobs de crawl.

### Terminal 3 — Envoyer une requête de test

Vérifiez que le serveur est en cours d’exécution avec un « health check » :

```
curl -X GET http://localhost:3002/test
```

Cela devrait renvoyer `Hello, world!`. Pour tester l’endpoint de crawl :

```
curl -X POST http://localhost:3002/v1/crawl \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://mendable.ai"
  }'
```

## Alternative : Docker Compose

Pour une mise en place plus simple, Docker Compose exécute tous les services (Redis, serveur d’API et workers) avec une seule commande.

1. Assurez-vous que Docker et Docker Compose sont installés.
2. Copiez `.env.example` vers `.env` dans le répertoire `apps/api/` et configurez-le selon vos besoins.
3. Depuis la racine du projet, exécutez :

Cela lance automatiquement tous les services avec la configuration adéquate.

## Exécuter les tests

Exécutez la suite de tests avec :