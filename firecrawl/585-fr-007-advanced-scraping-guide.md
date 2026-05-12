---
title: Guide avancé de scraping | Firecrawl
url: https://docs.firecrawl.dev/fr/advanced-scraping-guide
source: sitemap
fetched_at: 2026-03-23T07:28:01.959926-03:00
rendered_js: false
word_count: 1635
summary: This document provides a comprehensive reference for the Firecrawl scrape API, detailing configuration options for output formats, content filtering, PDF parsing strategies, and browser-based automation actions.
tags:
    - firecrawl
    - web-scraping
    - api-reference
    - data-extraction
    - automation
    - pdf-parsing
category: reference
---

Référence pour toutes les options disponibles sur les endpoints de scraping, crawling, mapping et agent de Firecrawl.

## Scraping basique

Pour extraire une seule page et obtenir un contenu Markdown propre, utilisez le point de terminaison `/scrape`.

Firecrawl prend en charge les PDF. Utilisez l’option `parsers` (par exemple `parsers: ["pdf"]`) lorsque vous voulez garantir l’analyse des PDF. Vous pouvez contrôler la stratégie d’analyse avec l’option `mode` :

- **`auto`** (par défaut) — tente d’abord une extraction rapide basée sur le texte, puis bascule vers l’OCR si nécessaire.
- **`fast`** — analyse basée uniquement sur le texte (texte intégré). La plus rapide, mais ignore les pages scannées ou très riches en images.
- **`ocr`** — force l’analyse par OCR sur chaque page. À utiliser pour les documents numérisés ou lorsque `auto` classe mal une page.

`{ type: "pdf" }` et `"pdf"` utilisent tous les deux `mode: "auto"` par défaut.

```
"parsers": [{ "type": "pdf", "mode": "fast", "maxPages": 50 }]
```

Lorsque vous utilisez le point de terminaison /scrape, vous pouvez personnaliser la requête avec les options ci-dessous.

### Formats (`formats`)

Le tableau `formats` contrôle les types de sortie que le scraper renvoie. Valeur par défaut : `["markdown"]`. **Formats de type chaîne de caractères** : passez le nom directement (par ex. `"markdown"`).

FormatDescription`markdown`Contenu de la page converti en Markdown propre.`html`HTML traité avec les éléments inutiles supprimés.`rawHtml`HTML original exactement tel que renvoyé par le serveur.`links`Tous les liens trouvés sur la page.`images`Toutes les images trouvées sur la page.`summary`Un résumé du contenu de la page généré par un LLM.`branding`Extrait l’identité de marque (couleurs, polices, typographie, espacements, composants d’UI).

**Formats objet** : passez un objet avec `type` et des options supplémentaires.

FormatOptionsDescription`json``prompt?: string`, `schema?: object`Extraire des données structurées à l’aide d’un LLM. Fournissez un schéma JSON et/ou un prompt en langage naturel (10 000 caractères max).`screenshot``fullPage?: boolean`, `quality?: number`, `viewport?: { width, height }`Prendre une capture d’écran. Maximum une par requête. La résolution maximale du viewport est 7680×4320. Les URL des captures d’écran expirent après 24 heures.`changeTracking``modes?: ("json" | "git-diff")[]`, `tag?: string`, `schema?: object`, `prompt?: string`Suivre les modifications entre les scrapes. Nécessite que `"markdown"` soit également présent dans le tableau `formats`.`attributes``selectors: [{ selector: string, attribute: string }]`Extraire des attributs HTML spécifiques à partir des éléments correspondant à des sélecteurs CSS.

### Filtrage du contenu

Ces paramètres contrôlent quelles parties de la page apparaissent dans le résultat. `onlyMainContent` s’exécute en premier pour supprimer le boilerplate (navigation, pied de page, etc.), puis `includeTags` et `excludeTags` affinent davantage le résultat. Si vous définissez `onlyMainContent: false`, le HTML complet de la page est utilisé comme point de départ pour le filtrage par balises.

ParamètreTypeValeur par défautDescription`onlyMainContent``boolean``true`Retourne uniquement le contenu principal. Définissez sur `false` pour la page complète.`includeTags``array`—Balises HTML, classes ou identifiants à inclure (par ex. `["h1", "p", ".main-content"]`).`excludeTags``array`—Balises HTML, classes ou identifiants à exclure (par ex. `["#ad", "#footer"]`).

### Timing et cache

ParamètreTypeValeur par défautDescription`waitFor``integer` (ms)`0`Temps d’attente supplémentaire avant le scraping, en plus du smart-wait. À utiliser avec parcimonie.`maxAge``integer` (ms)`172800000`Retourne une version mise en cache si elle est plus récente que cette valeur (2 jours par défaut). Définissez `0` pour toujours récupérer des données fraîches.`timeout``integer` (ms)`30000`Durée maximale d’une requête avant abandon (30 secondes par défaut). Le minimum est de 1000 (1 seconde).

### Analyse de PDF

ParamètreTypeValeur par défautDescription`parsers``array``["pdf"]`Contrôle le traitement des PDF. `[]` pour ignorer l’analyse et renvoyer le contenu en base64 (forfait de 1 crédit).

```
{ "type": "pdf", "mode": "fast" | "auto" | "ocr", "maxPages": 10 }
```

PropriétéTypeValeur par défautDescription`type``"pdf"`*(obligatoire)*Type d’analyseur.`mode``"fast" | "auto" | "ocr"``"auto"``fast` : extraction basée uniquement sur le texte. `auto` : rapide avec repli sur l’OCR. `ocr` : forcer l’OCR.`maxPages``integer`—Limiter le nombre de pages à analyser.

### Actions

Exécutez des actions dans le navigateur avant le scraping. Cela est utile pour le contenu dynamique, la navigation ou les pages nécessitant une interaction utilisateur. Vous pouvez inclure jusqu’à 50 actions par requête, et le temps d’attente cumulé sur toutes les actions `wait` et `waitFor` ne doit pas dépasser 60 secondes.

ActionParamètresDescription`wait``milliseconds?: number`, `selector?: string`Attendre une durée fixe **ou** qu’un élément soit visible (fournissez l’un ou l’autre, pas les deux). Lors de l’utilisation de `selector`, l’action expire au bout de 30 secondes.`click``selector: string`, `all?: boolean`Cliquer sur un élément correspondant au sélecteur CSS. Définissez `all: true` pour cliquer sur toutes les correspondances.`write``text: string`Saisir du texte dans le champ actuellement focalisé. Vous devez d’abord donner le focus à l’élément avec une action `click`.`press``key: string`Appuyer sur une touche du clavier (par ex. `"Enter"`, `"Tab"`, `"Escape"`).`scroll``direction?: "up" | "down"`, `selector?: string`Faire défiler la page ou un élément spécifique. La direction par défaut est `"down"`.`screenshot``fullPage?: boolean`, `quality?: number`, `viewport?: { width, height }`Prendre une capture d’écran. La résolution maximale du viewport est 7680×4320.`scrape`*(none)*Capturer le HTML de la page actuelle à ce point de la séquence d’actions.`executeJavascript``script: string`Exécuter du code JavaScript dans la page. Retourne `{ type, value }`.`pdf``format?: string`, `landscape?: boolean`, `scale?: number`Générer un PDF. Formats pris en charge : `"A0"` à `"A6"`, `"Letter"`, `"Legal"`, `"Tabloid"`, `"Ledger"`. La valeur par défaut est `"Letter"`.

#### Notes sur l’exécution des actions

- **Write** nécessite un `click` préalable pour placer le focus sur l’élément cible.
- **Scroll** accepte un `selector` optionnel pour faire défiler un élément spécifique plutôt que la page.
- **Wait** accepte soit `milliseconds` (délai fixe), soit `selector` (attendre jusqu’à ce que l’élément soit visible).
- Les actions s’exécutent **séquentiellement** : chaque étape se termine avant que la suivante ne commence.
- Les actions ne sont **pas prises en charge pour les PDF**. Si l’URL renvoie vers un PDF, la requête échouera.

#### Exemples d’actions avancées

**Prendre une capture d’écran :**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "click", "selector": "#load-more" },
      { "type": "wait", "milliseconds": 1000 },
      { "type": "screenshot", "fullPage": true, "quality": 80 }
    ]
  }'
```

**Clic sur plusieurs éléments :**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "click", "selector": ".expand-button", "all": true },
      { "type": "wait", "milliseconds": 500 }
    ],
    "formats": ["markdown"]
  }'
```

**Générer un PDF :**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "pdf", "format": "A4", "landscape": false }
    ]
  }'
```

La requête suivante combine plusieurs options d’extraction :

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "formats": [
        "markdown",
        "links",
        "html",
        "rawHtml",
        { "type": "screenshot", "fullPage": true, "quality": 80 }
      ],
      "includeTags": ["h1", "p", "a", ".main-content"],
      "excludeTags": ["#ad", "#footer"],
      "onlyMainContent": false,
      "waitFor": 1000,
      "timeout": 15000,
      "parsers": ["pdf"]
    }'
```

Cette requête renvoie du Markdown, du HTML, du HTML brut, des liens et une capture d’écran de la page entière. Elle limite le contenu à `<h1>`, `<p>`, `<a>` et `.main-content` tout en excluant `#ad` et `#footer`, attend 1 seconde avant l’extraction, définit un délai d’expiration de 15 secondes et active l’analyse des PDF. Consultez la [référence complète de l’API Scrape](https://docs.firecrawl.dev/api-reference/endpoint/scrape) pour plus de détails.

Utilisez l’objet de format JSON dans `formats` pour extraire des données structurées en une seule fois :

## Endpoint de l’agent

Utilisez l’endpoint `/v2/agent` pour effectuer une extraction autonome de données sur plusieurs pages. L’agent fonctionne de manière asynchrone : vous démarrez un job, puis interrogez périodiquement l’API pour récupérer les résultats.

### Options de l’agent

ParamètreTypeValeur par défautDescription`prompt``string`*(obligatoire)*Instructions en langage naturel décrivant les données à extraire (10 000 caractères maximum).`urls``array`—URL auxquelles limiter l’agent.`schema``object`—Schéma JSON pour structurer les données extraites.`maxCredits``number``2500`Nombre maximal de crédits que l’agent peut utiliser. Le tableau de bord prend en charge jusqu’à 2 500 ; pour des limites plus élevées, définissez cette valeur via l’API (les valeurs supérieures à 2 500 sont toujours facturées comme des requêtes payantes).`strictConstrainToURLs``boolean``false`Lorsque `true`, l’agent ne visite que les URL fournies.`model``string``"spark-1-mini"`Modèle d’IA à utiliser : `"spark-1-mini"` (par défaut, 60 % moins cher) ou `"spark-1-pro"` (meilleure précision).

### Vérifier l’état de l’agent

Envoyez des requêtes `GET /v2/agent/{jobId}` pour suivre l’avancement. Le champ `status` de la réponse vaudra `"processing"`, `"completed"` ou `"failed"`.

```
curl -X GET https://api.firecrawl.dev/v2/agent/YOUR-JOB-ID \
  -H 'Authorization: Bearer fc-YOUR-API-KEY'
```

Les SDK Python et Node fournissent également une méthode pratique (`firecrawl.agent()`) qui lance la tâche et interroge automatiquement son état jusqu’à son achèvement.

## Crawl de plusieurs pages

Pour crawler plusieurs pages, utilisez le point de terminaison `/v2/crawl`. Le crawl s’exécute de manière asynchrone et renvoie un ID de tâche. Utilisez le paramètre `limit` pour contrôler le nombre de pages crawlées. S’il est omis, le crawl traitera jusqu’à 10 000 pages.

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 10
    }'
```

### Réponse

```
{ "id": "1234-5678-9101" }
```

### Vérifier l’état d’une tâche de crawl

Utilisez l’ID de la tâche pour vérifier l’état du crawl et récupérer ses résultats.

```
curl -X GET https://api.firecrawl.dev/v2/crawl/1234-5678-9101 \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY'
```

Si le contenu dépasse 10 Mo ou si la tâche de crawl est toujours en cours d’exécution, la réponse peut inclure un paramètre `next` contenant l’URL de la page suivante de résultats.

### Aperçu du prompt et des paramètres de crawl

Vous pouvez fournir un `prompt` en langage naturel pour permettre à Firecrawl de déterminer les paramètres de crawl. Prévisualisez-les d’abord :

```
curl -X POST https://api.firecrawl.dev/v2/crawl/params-preview \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "prompt": "Extraire la doc et le blog"
  }'
```

### Options du crawler

Lorsque vous utilisez l’endpoint `/v2/crawl`, vous pouvez personnaliser le comportement du crawl à l’aide des options suivantes.

#### Filtrage des chemins

ParamètreTypeValeur par défautDescription`includePaths``array`—Motifs regex pour les URL à inclure (pathname uniquement par défaut).`excludePaths``array`—Motifs regex pour les URL à exclure (pathname uniquement par défaut).`regexOnFullURL``boolean``false`Faire correspondre les motifs sur l’URL complète plutôt que seulement sur le pathname.

#### Portée du crawl

ParamètreTypeValeur par défautDescription`maxDiscoveryDepth``integer`—Profondeur maximale de liens pour la découverte de nouvelles URL.`limit``integer``10000`Nombre maximal de pages à explorer.`crawlEntireDomain``boolean``false`Explorer les pages parentes et voisines pour couvrir l’ensemble du domaine.`allowExternalLinks``boolean``false`Suivre les liens vers des domaines externes.`allowSubdomains``boolean``false`Suivre les sous-domaines du domaine principal.`delay``number` (s)—Délai entre deux extractions.

#### Sitemap et déduplication

ParamètreTypeValeur par défautDescription`sitemap``string``"include"``"include"` : utiliser le sitemap + la découverte de liens. `"skip"` : ignorer le sitemap. `"only"` : explorer uniquement les URL du sitemap.`deduplicateSimilarURLs``boolean``true`Traite les variantes d’URL (`www.`, `https`, slash final, `index.html`) comme des doublons.`ignoreQueryParameters``boolean``false`Supprime les paramètres de requête avant la déduplication (par exemple `/page?a=1` et `/page?a=2` sont considérées comme une seule URL).

#### Options de scrape pour le crawl

ParamètreTypePar défautDescription`scrapeOptions``object``{ formats: ["markdown"] }`Configuration de scrape page par page. Accepte toutes les [options de scrape](#scrape-options) ci-dessus.

### Exemple de crawl

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-VOTRE-CLÉ-API' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "includePaths": ["^/blog/.*$", "^/docs/.*$"],
      "excludePaths": ["^/admin/.*$", "^/private/.*$"],
      "maxDiscoveryDepth": 2,
      "limit": 1000
    }'
```

## Cartographie des liens d’un site web

L’endpoint d’API `/v2/map` identifie les URL liées à un site web donné.

```
curl -X POST https://api.firecrawl.dev/v2/map \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
```

### Options de mappage

ParamètreTypeValeur par défautDescription`search``string`—Filtrer les liens en fonction d’une correspondance de texte.`limit``integer``100`Nombre maximal de liens à renvoyer.`sitemap``string``"include"``"include"`, `"skip"` ou `"only"`.`includeSubdomains``boolean``true`Inclure les sous-domaines.

Voici la référence de l’API correspondante : [Documentation du point de terminaison /map](https://docs.firecrawl.dev/api-reference/endpoint/map)

## Autoriser Firecrawl

### Autoriser Firecrawl à explorer votre site web

- **User Agent** : Autorisez `FirecrawlAgent` dans votre pare-feu ou vos règles de sécurité.
- **Adresses IP** : Firecrawl n’utilise pas un ensemble fixe d’adresses IP sortantes.

### Autoriser votre application à appeler l’API Firecrawl

Si votre pare-feu bloque les requêtes sortantes de votre application vers des services externes, vous devez ajouter l’adresse IP du serveur de l’API Firecrawl à la liste d’autorisation afin que votre application puisse atteindre l’API Firecrawl (`api.firecrawl.dev`) :

- **Adresse IP** : `35.245.250.27`

Ajoutez cette adresse IP à la liste d’autorisation des connexions sortantes de votre pare-feu afin que votre backend puisse envoyer à Firecrawl des requêtes de scraping, de crawling, de mapping et des requêtes d’agent.