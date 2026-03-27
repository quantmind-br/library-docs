---
title: Auto-hébergement | Firecrawl
url: https://docs.firecrawl.dev/fr/contributing/self-host
source: sitemap
fetched_at: 2026-03-23T07:30:32.597823-03:00
rendered_js: false
word_count: 1019
summary: This document provides instructions for self-hosting Firecrawl, detailing the technical requirements, configuration steps, and trade-offs compared to the cloud service.
tags:
    - self-hosting
    - docker
    - firecrawl
    - scraping
    - deployment
    - configuration
    - open-source
category: guide
---

#### Vous souhaitez contribuer ?

Bienvenue sur [Firecrawl](https://firecrawl.dev) 🔥 ! Voici quelques instructions pour récupérer le projet en local afin de l’exécuter vous-même et d’y contribuer. Si vous contribuez, notez que le processus est similaire à celui d’autres dépôts open source : forkez Firecrawl, apportez vos modifications, exécutez les tests, puis ouvrez une PR. Si vous avez des questions ou souhaitez de l’aide pour démarrer, rejoignez notre communauté Discord [ici](https://discord.gg/firecrawl) pour en savoir plus, ou ouvrez une issue sur GitHub [ici](https://github.com/firecrawl/firecrawl/issues/new/choose) !

Consultez [SELF\_HOST.md](https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md) pour savoir comment l’exécuter en local.

## Pourquoi ?

L’auto‑hébergement de Firecrawl est particulièrement utile pour les organisations dont les politiques de sécurité exigent que les données restent dans des environnements contrôlés. Voici quelques raisons majeures d’envisager l’auto‑hébergement :

- **Sécurité et conformité renforcées :** En auto‑hébergeant, vous garantissez que l’ensemble de la gestion et du traitement des données respecte les réglementations internes et externes, en conservant les informations sensibles au sein de votre infrastructure sécurisée. Notez que Firecrawl est un produit Mendable et s’appuie sur la certification SOC 2 Type II, ce qui signifie que la plateforme respecte des normes élevées du secteur en matière de sécurité des données.
- **Services personnalisables :** L’auto‑hébergement vous permet d’adapter des services, comme Playwright, pour répondre à des besoins spécifiques ou couvrir des cas d’usage particuliers qui ne sont pas forcément pris en charge par l’offre cloud standard.
- **Apprentissage et contribution à la communauté :** En configurant et en maintenant votre propre instance, vous approfondissez votre compréhension du fonctionnement de Firecrawl, ce qui peut également conduire à des contributions plus significatives au projet.

### Considérations

Cependant, il existe certaines limites et des responsabilités supplémentaires à garder à l’esprit :

1. **Accès limité à Fire-engine :** Actuellement, les instances auto-hébergées de Firecrawl n’ont pas accès à Fire-engine, qui comprend des fonctionnalités avancées pour gérer les blocages d’IP, les mécanismes de détection des robots, et plus encore. Cela signifie que, même si vous pouvez traiter des tâches de scraping de base, des cas plus complexes peuvent nécessiter une configuration supplémentaire ou ne pas être pris en charge.
2. **Configuration manuelle requise :** Si vous devez utiliser des méthodes de scraping au-delà des options de base `fetch` et Playwright, vous devrez les configurer manuellement dans le fichier `.env`. Cela nécessite une compréhension plus approfondie des technologies et peut impliquer davantage de temps de mise en place.

Fonctionnalité — Cloud — Auto-hébergement

- Tous les endpoints d’API pris en charge — Oui — Pas toujours ; `/agent` et `/browser` ne sont pas pris en charge en auto-hébergement
- Prise en charge des captures d’écran — Oui — Oui, lorsque le service Playwright est en cours d’exécution
- LLM locaux (par ex. Ollama) — Non pris en charge — Pris en charge via `OLLAMA_BASE_URL` (expérimental)

L’auto-hébergement de Firecrawl est idéal pour ceux qui ont besoin d’un contrôle total sur leurs environnements de scraping et de traitement des données, mais il s’accompagne du revers d’une charge supplémentaire de maintenance et de configuration.

## Étapes

1. Commencez par installer les dépendances

<!--THE END-->

- Docker [instructions](https://docs.docker.com/get-docker/)

<!--THE END-->

2. Définissez les variables d’environnement

Créez un fichier `.env` à la racine du projet. Vous pouvez copier le modèle situé dans `apps/api/.env.example`. Pour commencer, nous ne configurerons ni l’authentification ni aucun sous-service optionnel (parsing PDF, prise en charge du blocage de JS, fonctionnalités IA)

```
# .env

# ===== Required ENVS ======
PORT=3002
HOST=0.0.0.0

# Note: PORT is used by both the main API server and worker liveness check endpoint

# To turn on DB authentication, you need to set up Supabase.
USE_DB_AUTHENTICATION=false

# ===== Optional ENVS ======

## === AI features (JSON format on scrape, /extract API) ===
# Provide your OpenAI API key here to enable AI features
# OPENAI_API_KEY=

# Experimental: Use Ollama
# OLLAMA_BASE_URL=http://localhost:11434/api
# MODEL_NAME=deepseek-r1:7b
# MODEL_EMBEDDING_NAME=nomic-embed-text

# Experimental: Use any OpenAI-compatible API
# OPENAI_BASE_URL=https://example.com/v1
# OPENAI_API_KEY=

## === Proxy ===
# PROXY_SERVER can be a full URL (e.g. http://0.1.2.3:1234) or just an IP and port combo (e.g. 0.1.2.3:1234)
# Do not uncomment PROXY_USERNAME and PROXY_PASSWORD if your proxy is unauthenticated
# PROXY_SERVER=
# PROXY_USERNAME=
# PROXY_PASSWORD=

## === API /search ===

# Vous pouvez spécifier un serveur SearXNG avec le format JSON activé, si vous souhaitez l'utiliser à la place de Google direct.
# Vous pouvez également personnaliser les paramètres engines et categories, mais les valeurs par défaut devraient également fonctionner correctement.
# SEARXNG_ENDPOINT=http://your.searxng.server
# SEARXNG_ENGINES=
# SEARXNG_CATEGORIES=

## === Other ===

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=

# Use if you've set up authentication and want to test with a real API key
# TEST_API_KEY=

# This key lets you access the queue admin panel. Change this if your deployment is publicly accessible.
BULL_AUTH_KEY=CHANGEME

# This is now autoconfigured by the docker-compose.yaml. You shouldn't need to set it.
# PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/scrape
# REDIS_URL=redis://redis:6379
# REDIS_RATE_LIMIT_URL=redis://redis:6379

# Set if you have a llamaparse key you'd like to use to parse pdfs
# LLAMAPARSE_API_KEY=

# Set if you'd like to send server health status messages to Slack
# SLACK_WEBHOOK_URL=

# Set if you'd like to send posthog events like job logs
# POSTHOG_API_KEY=
# POSTHOG_HOST=

## === System Resource Configuration ===
# Maximum CPU usage threshold (0.0-1.0). Worker will reject new jobs when CPU usage exceeds this value.
# Default: 0.8 (80%)
# MAX_CPU=0.8

# Maximum RAM usage threshold (0.0-1.0). Worker will reject new jobs when memory usage exceeds this value.
# Default: 0.8 (80%)
# MAX_RAM=0.8

# Set if you'd like to allow local webhooks to be sent to your self-hosted instance
# ALLOW_LOCAL_WEBHOOKS=true
```

3. *(Optionnel) Exécuter avec le service Playwright en TypeScript*
   
   - Mettez à jour le fichier `docker-compose.yml` pour modifier le service Playwright :
     
     ```
         build: apps/playwright-service
     ```
     
     EN
     
     ```
         build: apps/playwright-service-ts
     ```
   - Définissez la variable `PLAYWRIGHT_MICROSERVICE_URL` dans votre fichier `.env` :
     
     ```
     PLAYWRIGHT_MICROSERVICE_URL=http://localhost:3000/scrape
     ```
   - N’oubliez pas de configurer le serveur proxy dans votre fichier `.env` si nécessaire.
4. Construisez et lancez les conteneurs Docker :
   
   ```
   docker compose build
   docker compose up
   ```

Cela démarre une instance locale de Firecrawl accessible à l’adresse `http://localhost:3002`. Vous devriez voir l’interface Bull Queue Manager à l’adresse `http://localhost:3002/admin/{BULL_AUTH_KEY}/queues`.

5. *(Optionnel)* Tester l’API

Si vous souhaitez tester l’endpoint de crawl, vous pouvez exécuter la commande suivante :

```
  curl -X POST http://localhost:3002/v2/crawl \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://docs.firecrawl.dev"
      }'
```

## Dépannage

Cette section propose des solutions aux problèmes courants que vous pouvez rencontrer lors de la configuration ou de l’exécution de votre instance Firecrawl auto-hébergée.

### Le client Supabase n’est pas configuré

**Symptôme :**

```
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Tentative d’accès au client Supabase alors qu’il n’est pas configuré.
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Erreur lors de l’insertion de l’événement de scraping : Erreur : le client Supabase n’est pas configuré.
```

**Explication :** Cette erreur se produit parce que la configuration du client Supabase n’est pas finalisée. Vous devriez pouvoir lancer des opérations de scraping et de crawling sans problème. À l’heure actuelle, il n’est pas possible de configurer Supabase sur des instances auto‑hébergées.

### Vous contournez le mécanisme d’authentification

**Symptôme :**

```
[YYYY-MM-DDTHH:MM:SS.SSSz]WARN - You're bypassing authentication
```

**Explication :** Cette erreur se produit parce que la configuration du client Supabase n’est pas finalisée. Vous pouvez tout de même effectuer du scraping et du crawling sans problème. Pour le moment, il n’est pas possible de configurer Supabase sur des instances auto-hébergées.

### Les conteneurs Docker ne démarrent pas

**Symptôme :** Les conteneurs Docker s’arrêtent de manière inattendue ou ne parviennent pas à démarrer. **Solution :** Vérifiez les logs Docker pour détecter d’éventuels messages d’erreur en utilisant la commande :

```
docker logs [container_name]
```

- Assurez-vous que toutes les variables d’environnement nécessaires sont correctement définies dans le fichier .env.
- Vérifiez que tous les services Docker définis dans docker-compose.yml sont correctement configurés et que les images requises sont disponibles.

### Problèmes de connexion avec Redis

**Symptôme :** Erreurs liées à la connexion à Redis, telles que des délais d’attente dépassés ou des erreurs « Connection refused ». **Solution :**

- Assurez-vous que le service Redis est démarré et fonctionne dans votre environnement Docker.
- Vérifiez que les variables REDIS\_URL et REDIS\_RATE\_LIMIT\_URL dans votre fichier .env pointent vers la bonne instance Redis.
- Vérifiez les paramètres réseau et les règles de pare-feu susceptibles de bloquer la connexion au port Redis.

### Le point de terminaison API ne répond pas

**Symptôme :** Les requêtes API vers l’instance Firecrawl expirent ou ne renvoient aucune réponse. **Solution :**

- Assurez-vous que le service Firecrawl est en cours d’exécution en vérifiant l’état du conteneur Docker.
- Vérifiez que les variables PORT et HOST dans votre fichier .env sont correctes et qu’aucun autre service n’utilise le même port.
- Contrôlez la configuration réseau pour vous assurer que l’hôte est accessible depuis le client qui effectue la requête API.

En résolvant ces problèmes courants, vous faciliterez la configuration et le fonctionnement de votre instance Firecrawl auto-hébergée.

## Installer Firecrawl sur un cluster Kubernetes (version simple)

Consultez le fichier [examples/kubernetes-cluster-install/README.md](https://github.com/firecrawl/firecrawl/tree/main/examples/kubernetes/cluster-install#readme) pour savoir comment installer Firecrawl sur un cluster Kubernetes.