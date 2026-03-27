---
title: SDK Python | Firecrawl
url: https://docs.firecrawl.dev/fr/sdks/python
source: sitemap
fetched_at: 2026-03-23T07:23:41.994443-03:00
rendered_js: false
word_count: 807
summary: This document provides a comprehensive guide on using the Firecrawl Python SDK to scrape, crawl, and map web content, including asynchronous operations and pagination management.
tags:
    - python-sdk
    - web-scraping
    - web-crawling
    - data-extraction
    - api-integration
    - pagination
    - websockets
category: guide
---

## Installation

Pour installer le SDK Python Firecrawl, utilisez pip :

```
# pip install firecrawl-py

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-VOTRE-CLE-API")
```

## Utilisation

1. Récupérez une clé API sur [firecrawl.dev](https://firecrawl.dev)
2. Définissez la clé API comme variable d’environnement nommée `FIRECRAWL_API_KEY` ou passez-la en paramètre à la classe `Firecrawl`.

Voici un exemple d’utilisation du SDK :

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# Extraire le contenu d’un site :
scrape_status = firecrawl.scrape(
  'https://firecrawl.dev', 
  formats=['markdown', 'html']
)
print(scrape_status)

# Explorer un site :
crawl_status = firecrawl.crawl(
  'https://firecrawl.dev', 
  limit=100, 
  scrape_options={
    'formats': ['markdown', 'html']
  }
)
print(crawl_status)
```

Pour extraire une URL unique, utilisez la méthode `scrape`. Elle prend l’URL en paramètre et renvoie le document extrait.

```
# Extraire un site web :
scrape_result = firecrawl.scrape('firecrawl.dev', formats=['markdown', 'html'])
print(scrape_result)
```

### Explorer un site web

Pour explorer un site web, utilisez la méthode `crawl`. Elle prend en arguments l’URL de départ et des options facultatives. Ces options permettent de définir des paramètres supplémentaires pour la tâche d’exploration, comme le nombre maximal de pages à parcourir, les domaines autorisés et le format de sortie. Consultez [Pagination](#pagination) pour la pagination automatique/manuelle et les limites.

```
job = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=5, poll_interval=1, timeout=120)
print(job)
```

### Exploration du sitemap uniquement

Utilisez `sitemap="only"` pour explorer uniquement les URL du sitemap (l’URL de départ est toujours incluse et la découverte de liens HTML est ignorée).

```
job = firecrawl.crawl(url="https://docs.firecrawl.dev", sitemap="only", limit=25)
print(job.status, len(job.data))
```

### Démarrer un crawl

Lancez une tâche sans attendre avec `start_crawl`. Elle renvoie un `ID` de tâche que vous pouvez utiliser pour vérifier l’état. Utilisez `crawl` lorsque vous voulez un attenteur qui bloque jusqu’à la fin. Voir [Pagination](#pagination) pour le comportement et les limites de pagination.

```
job = firecrawl.start_crawl(url="https://docs.firecrawl.dev", limit=10)
print(job)
```

### Vérifier l’état d’un crawl

Pour connaître l’état d’un job de crawl, utilisez la méthode `get_crawl_status`. Elle prend l’ID du job en paramètre et renvoie l’état actuel du crawl.

```
status = firecrawl.get_crawl_status("<crawl-id>")
print(status)
```

### Annuler un crawl

Pour annuler une tâche de crawl, utilisez la méthode `cancel_crawl`. Elle prend l’ID du job renvoyé par `start_crawl` en paramètre et retourne l’état de l’annulation.

```
ok = firecrawl.cancel_crawl("<crawl-id>")
print("Annulation :", ok)
```

### Cartographier un site web

Utilisez `map` pour générer une liste d’URL à partir d’un site web. Les options permettent d’adapter le processus de cartographie, par exemple en excluant les sous-domaines ou en s’appuyant sur le sitemap.

```
res = firecrawl.map(url="https://firecrawl.dev", limit=10)
print(res)
```

### Exploration d’un site web avec WebSockets

Pour explorer un site web avec WebSockets, lancez la tâche avec `start_crawl` et abonnez-vous à l’aide du helper `watcher`. Créez un watcher avec l’ID de la tâche et attachez des gestionnaires (par exemple pour page, completed, failed) avant d’appeler `start()`.

```
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

    # Démarrer d'abord un crawl
    started = await firecrawl.start_crawl("https://firecrawl.dev", limit=5)

    # Surveiller les mises à jour (instantanés) jusqu'au statut final
    async for snapshot in firecrawl.watcher(started.id, kind="crawl", poll_interval=2, timeout=120):
        if snapshot.status == "completed":
            print("DONE", snapshot.status)
            for doc in snapshot.data:
                print("DOC", doc.metadata.source_url if doc.metadata else None)
        elif snapshot.status == "failed":
            print("ERR", snapshot.status)
        else:
            print("STATUS", snapshot.status, snapshot.completed, "/", snapshot.total)

asyncio.run(main())
```

Les points de terminaison Firecrawl pour crawl et batch scrape renvoient une URL `next` lorsqu’il reste des données. Le SDK Python effectue par défaut une pagination automatique et agrège tous les documents ; dans ce cas, `next` vaut `None`. Vous pouvez désactiver l’auto‑pagination ou définir des limites pour contrôler le comportement de la pagination.

Utilisez `PaginationConfig` pour contrôler le comportement de la pagination lorsque vous appelez `get_crawl_status` ou `get_batch_scrape_status` :

```
from firecrawl.v2.types import PaginationConfig
```

OptionTypePar défautDescription`auto_paginate``bool``True`Lorsque `True`, récupère automatiquement toutes les pages et agrège les résultats. Définissez sur `False` pour récupérer les pages une par une.`max_pages``int``None`S’arrête après avoir récupéré ce nombre de pages (s’applique uniquement lorsque `auto_paginate=True`).`max_results``int``None`S’arrête après avoir collecté ce nombre de documents (s’applique uniquement lorsque `auto_paginate=True`).`max_wait_time``int``None`S’arrête après ce nombre de secondes (s’applique uniquement lorsque `auto_paginate=True`).

Lorsque `auto_paginate=False`, la réponse inclut une URL `next` si davantage de données sont disponibles. Utilisez ces méthodes utilitaires pour récupérer les pages suivantes :

- **`get_crawl_status_page(next_url)`** - Récupère la page suivante des résultats de crawl en utilisant l’URL opaque `next` provenant d’une réponse précédente.
- **`get_batch_scrape_status_page(next_url)`** - Récupère la page suivante des résultats de scraping par lot en utilisant l’URL opaque `next` provenant d’une réponse précédente.

Ces méthodes renvoient le même type de réponse que l’appel de statut initial, y compris une nouvelle URL `next` s’il reste d’autres pages.

#### Crawl

Utilisez la méthode « waiter » `crawl` pour l’approche la plus simple, ou démarrez un job et paginez manuellement.

- Voir le flux par défaut dans [Explorer un site web](#crawl-a-website).

Démarrez un job, puis récupérez une page à la fois avec `auto_paginate=False`. Utilisez `get_crawl_status_page` pour récupérer les pages suivantes :

```
crawl_job = client.start_crawl("https://example.com", limit=100)

# Fetch first page
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(auto_paginate=False)
)
print("First page:", len(status.data), "docs")

# Récupérer les pages suivantes avec get_crawl_status_page
while status.next:
    status = client.get_crawl_status_page(status.next)
    print("Next page:", len(status.data), "docs")
```

Laissez la pagination automatique activée, mais arrêtez plus tôt avec `max_pages`, `max_results` ou `max_wait_time` :

```
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=50, max_wait_time=15),
)
print("crawl limité :", status.status, "docs :", len(status.data), "suivant :", status.next)
```

#### Scrape par lots

Utilisez la méthode de waiter `batch_scrape`, ou lancez un job et paginez manuellement.

- Voir le parcours par défaut dans [Batch Scrape](https://docs.firecrawl.dev/fr/features/batch-scrape).

Lancez une tâche, puis récupérez les résultats page par page avec `auto_paginate=False`. Utilisez `get_batch_scrape_status_page` pour récupérer les pages suivantes :

```
batch_job = client.start_batch_scrape(urls)

# Fetch first page
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(auto_paginate=False)
)
print("First page:", len(status.data), "docs")

# Récupérer les pages suivantes avec get_batch_scrape_status_page
while status.next:
    status = client.get_batch_scrape_status_page(status.next)
    print("Next page:", len(status.data), "docs")
```

Laissez la pagination automatique activée, mais arrêtez plus tôt avec `max_pages`, `max_results` ou `max_wait_time` :

```
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=100, max_wait_time=20),
)
print("lot limité :", status.status, "docs :", len(status.data), "suivant :", status.next)
```

## Gestion des erreurs

Le SDK gère les erreurs renvoyées par l’API Firecrawl et déclenche des exceptions appropriées. En cas d’erreur lors d’une requête, une exception est levée avec un message d’erreur explicite.

## Classe asynchrone

Pour les opérations asynchrones, utilisez la classe `AsyncFirecrawl`. Ses méthodes sont identiques à celles de `Firecrawl`, mais elles ne bloquent pas le thread principal.

```
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

    # Scraping
    doc = await firecrawl.scrape("https://firecrawl.dev", formats=["markdown"])  # type: ignore[arg-type]
    print(doc.get("markdown"))

    # Recherche
    results = await firecrawl.search("firecrawl", limit=2)
    print(results.get("web", []))

    # Crawl (démarrage + statut)
    started = await firecrawl.start_crawl("https://docs.firecrawl.dev", limit=3)
    status = await firecrawl.get_crawl_status(started.id)
    print(status.status)

    # Scraping par lot (attente)
    job = await firecrawl.batch_scrape([
        "https://firecrawl.dev",
        "https://docs.firecrawl.dev",
    ], formats=["markdown"], poll_interval=1, timeout=60)
    print(job.status, job.completed, job.total)

asyncio.run(main())
```

## Navigateur

Lancez des sessions de navigateur dans le cloud et exécutez du code à distance.

### Créer une session

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

session = app.browser()
print(session.id)             # ID de session
print(session.cdp_url)        # wss://cdp-proxy.firecrawl.dev/cdp/...
print(session.live_view_url)  # https://liveview.firecrawl.dev/...
```

### Exécuter du code

```
result = app.browser_execute(
    session.id,
    code='await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
    language="python",
)
print(result.result)  # "Hacker News"
```

Exécuter JavaScript plutôt que Python :

```
result = app.browser_execute(
    session.id,
    code='await page.goto("https://example.com"); const t = await page.title(); console.log(t);',
    language="node",
)
```

### Profils

Enregistrez et réutilisez l’état du navigateur (cookies, localStorage, etc.) d’une session à l’autre :

```
session = app.browser(
    ttl=600,
    profile={
        "name": "my-profile",
        "save_changes": True,
    },
)
```

### Connexion via le CDP

Pour un contrôle total de Playwright, connectez-vous directement en utilisant l’URL du CDP :

```
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(session.cdp_url)
    context = browser.contexts[0]
    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://example.com")
    print(page.title())

    browser.close()
```

### Lister & fermer des sessions

```
# Lister les sessions actives
sessions = app.list_browsers(status="active")
for s in sessions.sessions:
    print(s.id, s.status, s.created_at)

# Fermer une session
app.delete_browser(session.id)
```

> Êtes-vous un agent IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’onboarding automatisé.