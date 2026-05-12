---
title: SDK Node | Firecrawl
url: https://docs.firecrawl.dev/fr/sdks/node
source: sitemap
fetched_at: 2026-03-23T07:23:35.691045-03:00
rendered_js: false
word_count: 670
summary: This document provides a comprehensive guide on using the Firecrawl Node.js SDK to scrape web content, crawl entire sites, map URLs, and manage browser sessions.
tags:
    - node-sdk
    - web-scraping
    - web-crawling
    - automation
    - firecrawl
    - api-integration
category: guide
---

## Installation

Pour installer le SDK Firecrawl pour Node, vous pouvez utiliser npm :

```
# npm install @mendable/firecrawl-js

import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-VOTRE-CLÉ-API" });
```

## Utilisation

1. Récupérez une clé d’API sur [firecrawl.dev](https://firecrawl.dev)
2. Définissez la clé d’API comme variable d’environnement nommée `FIRECRAWL_API_KEY`, ou transmettez-la en paramètre à la classe `FirecrawlApp`.

Voici un exemple d’utilisation du SDK avec gestion des erreurs :

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

// Récupérer le contenu d’un site web
const scrapeResponse = await firecrawl.scrape('https://firecrawl.dev', {
  formats: ['markdown', 'html'],
});

console.log(scrapeResponse)

// Explorer un site web
const crawlResponse = await firecrawl.crawl('https://firecrawl.dev', {
  limit: 100,
  scrapeOptions: {
    formats: ['markdown', 'html'],
  }
});

console.log(crawlResponse)
```

### Scraper une URL

Pour récupérer le contenu d’une URL avec gestion des erreurs, utilisez la méthode `scrapeUrl`. Elle prend l’URL en paramètre et renvoie les données récupérées sous forme de dictionnaire.

```
// Extraire le contenu d’un site :
const scrapeResult = await firecrawl.scrape('firecrawl.dev', { formats: ['markdown', 'html'] });

console.log(scrapeResult)
```

### Explorer un site web

Pour explorer un site web avec gestion des erreurs, utilisez la méthode `crawlUrl`. Elle prend en arguments l’URL de départ et des paramètres optionnels. L’argument `params` vous permet de définir des options supplémentaires pour la tâche d’exploration, comme le nombre maximal de pages à explorer, les domaines autorisés et le format de sortie. Voir [Pagination](#pagination) pour la pagination automatique/manuelle et la limitation.

```
const job = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 5, pollInterval: 1, timeout: 120 });
console.log(job.status);
```

### Crawl uniquement via le sitemap

Utilisez `sitemap: "only"` pour explorer uniquement les URL du sitemap (l’URL de départ est toujours incluse et la découverte de liens HTML est désactivée).

```
const job = await firecrawl.crawl('https://docs.firecrawl.dev', {
  sitemap: 'only',
  limit: 25,
});
console.log(job.status, job.data.length);
```

### Démarrer un crawl

Lancez une tâche sans attendre avec `startCrawl`. Elle renvoie un `ID` de tâche que vous pouvez utiliser pour vérifier l’état. Utilisez `crawl` si vous voulez un « waiter » qui bloque jusqu’à la fin. Voir [Pagination](#pagination) pour le comportement de pagination et les limites.

```
const { id } = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 10 });
console.log(id);
```

### Vérifier l’état du crawl

Pour consulter l’état d’un job de crawl avec gestion des erreurs, utilisez la méthode `checkCrawlStatus`. Elle prend l’ID en paramètre et renvoie l’état actuel du job de crawl.

```
const status = await firecrawl.getCrawlStatus("<crawl-id>");
console.log(status);
```

### Annuler un crawl

Pour annuler une tâche de crawl, utilisez la méthode `cancelCrawl`. Elle prend l’ID de la tâche lancée par `startCrawl` en paramètre et renvoie l’état de l’annulation.

```
const ok = await firecrawl.cancelCrawl("<crawl-id>");
console.log("Annulé :", ok);
```

### Cartographier un site web

Pour cartographier un site web avec gestion des erreurs, utilisez la méthode `mapUrl`. Elle prend l’URL de départ en paramètre et renvoie les données cartographiées sous forme de dictionnaire.

```
const res = await firecrawl.map('https://firecrawl.dev', { limit: 10 });
console.log(res.links);
```

### Explorer un site web avec WebSockets

Pour explorer un site web avec WebSockets, utilisez la méthode `crawlUrlAndWatch`. Elle prend en arguments l’URL de départ et des paramètres optionnels. L’argument `params` permet de définir des options supplémentaires pour le job d’exploration, comme le nombre maximal de pages à explorer, les domaines autorisés et le format de sortie.

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

// Lancer un crawl puis le suivre
const { id } = await firecrawl.startCrawl('https://mendable.ai', {
  excludePaths: ['blog/*'],
  limit: 5,
});

const watcher = firecrawl.watcher(id, { kind: 'crawl', pollInterval: 2, timeout: 120 });

watcher.on('document', (doc) => {
  console.log('DOC', doc);
});

watcher.on('error', (err) => {
  console.error('ERR', err?.error || err);
});

watcher.on('done', (state) => {
  console.log('TERMINÉ', state.status);
});

// Démarrer l’observation (WS avec solution de repli HTTP)
await watcher.start();
```

Les points de terminaison Firecrawl pour crawl et batch renvoient une URL `next` lorsqu’il reste des données. Le SDK Node effectue, par défaut, une pagination automatique et agrège tous les documents ; dans ce cas, `next` vaut `null`. Vous pouvez désactiver la pagination automatique ou définir des limites.

#### Crawl

Utilisez la méthode d’attente `crawl` pour la solution la plus simple, ou démarrez un job et paginez manuellement.

- Voir le flux par défaut dans [Exploration d’un site web](#crawling-a-website).

<!--THE END-->

- Lancez un job, puis récupérez les pages une par une avec `autoPaginate: false`.

```
const crawlStart = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 5 });
const crawlJobId = crawlStart.id;

const crawlSingle = await firecrawl.getCrawlStatus(crawlJobId, { autoPaginate: false });
console.log('exploration d’une seule page :', crawlSingle.status, 'docs :', crawlSingle.data.length, 'suivant :', crawlSingle.next);
```

- Conservez la pagination automatique activée, mais arrêtez plus tôt avec `maxPages`, `maxResults` ou `maxWaitTime`.

```
const crawlLimited = await firecrawl.getCrawlStatus(crawlJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 50,
  maxWaitTime: 15,
});
console.log('exploration limitée :', crawlLimited.status, 'docs :', crawlLimited.data.length, 'suivant :', crawlLimited.next);
```

#### Scrape par lots

Utilisez la méthode du waiter `batchScrape`, ou lancez un job et paginez manuellement.

- Voir le flux par défaut dans [Batch Scrape](https://docs.firecrawl.dev/fr/features/batch-scrape).

<!--THE END-->

- Lancez un job, puis récupérez les pages une par une avec `autoPaginate: false`.

```
const batchStart = await firecrawl.startBatchScrape([
  'https://docs.firecrawl.dev',
  'https://firecrawl.dev',
], { options: { formats: ['markdown'] } });
const batchJobId = batchStart.id;

const batchSingle = await firecrawl.getBatchScrapeStatus(batchJobId, { autoPaginate: false });
console.log('lot page unique :', batchSingle.status, 'docs :', batchSingle.data.length, 'suivant :', batchSingle.next);
```

- Laissez la pagination automatique activée, mais arrêtez plus tôt avec `maxPages`, `maxResults` ou `maxWaitTime`.

```
const batchLimited = await firecrawl.getBatchScrapeStatus(batchJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 100,
  maxWaitTime: 20,
});
console.log('lot limité :', batchLimited.status, 'docs :', batchLimited.data.length, 'suivant :', batchLimited.next);
```

## Navigateur

Démarrez des sessions de navigateur dans le cloud et exécutez du code à distance.

### Créer une session

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const session = await firecrawl.browser({ ttl: 600 });
console.log(session.id);          // ID de session
console.log(session.cdpUrl);      // wss://cdp-proxy.firecrawl.dev/cdp/...
console.log(session.liveViewUrl); // https://liveview.firecrawl.dev/...
```

### Exécuter du code

```
const result = await firecrawl.browserExecute(session.id, {
  code: 'await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
});
console.log(result.result); // "Hacker News"
```

Exécutez du JavaScript plutôt que du Python :

```
const result = await firecrawl.browserExecute(session.id, {
  code: 'await page.goto("https://example.com"); const t = await page.title(); console.log(t);',
  language: "node",
});
```

Exécuter Bash avec agent-browser :

```
const result = await firecrawl.browserExecute(session.id, {
  code: "agent-browser open https://example.com && agent-browser snapshot",
  language: "bash",
});
```

### Profils

Enregistrez et réutilisez l’état du navigateur (cookies, localStorage, etc.) d’une session à l’autre :

```
const session = await firecrawl.browser({
  ttl: 600,
  profile: {
    name: "my-profile",
    saveChanges: true,
  },
});
```

### Connexion via le CDP

Pour bénéficier d’un contrôle complet via Playwright, connectez-vous directement à l’aide de l’URL CDP :

```
import { chromium } from "playwright";

const browser = await chromium.connectOverCDP(session.cdpUrl);
const context = browser.contexts()[0];
const page = context.pages()[0] || await context.newPage();

await page.goto("https://example.com");
console.log(await page.title());

await browser.close();
```

### Lister et fermer les sessions

```
// Lister les sessions actives
const { sessions } = await firecrawl.listBrowsers({ status: "active" });
for (const s of sessions) {
  console.log(s.id, s.status, s.createdAt);
}

// Fermer une session
await firecrawl.deleteBrowser(session.id);
```

## Gestion des erreurs

Le SDK gère les erreurs renvoyées par l’API Firecrawl et déclenche les exceptions appropriées. Si une erreur survient lors d’une requête, une exception est levée avec un message d’erreur explicite. Les exemples ci-dessus illustrent la gestion de ces erreurs au moyen de blocs `try/catch`.

> Êtes-vous un agent d’IA qui a besoin d’une clé d’API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.