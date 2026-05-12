---
title: Scrape par lot - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:15:45.456211-03:00
rendered_js: false
word_count: 1035
summary: This document provides technical documentation for the Firecrawl batch scraping API, detailing parameters for authentication, output formats, caching strategies, proxy configuration, and browser-side interaction actions.
tags:
    - api-reference
    - web-scraping
    - batch-processing
    - proxy-configuration
    - caching-strategies
    - data-extraction
category: api
---

[Passer au contenu principal](#content-area)

Scraper plusieurs URL et, au besoin, extraire des informations à l’aide d’un LLM

> Êtes-vous un agent IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour les instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corps

Un objet de spécification de webhook.

Nombre maximal d’opérations de scraping simultanées. Ce paramètre vous permet de définir une limite du nombre de scrapes exécutés en parallèle pour ce lot. S’il n’est pas renseigné, ce lot de scraping utilisera la limite de parallélisme définie pour votre équipe.

Si des URL non valides sont spécifiées dans le tableau `urls`, elles seront ignorées. Au lieu de faire échouer l’ensemble de la requête, une opération de scraping par lot sera créée avec les URL valides restantes, et les URL non valides seront renvoyées dans le champ `invalidURLs` de la réponse.

formats

(Markdown · object | Summary · object | HTML · object | Raw HTML · object | Links · object | Images · object | Screenshot · object | JSON · object | Change Tracking · object | Branding · object)\[]

Formats de sortie à inclure dans la réponse. Vous pouvez spécifier un ou plusieurs formats, soit sous forme de chaînes (par ex. `'markdown'`), soit sous forme d’objets avec des options supplémentaires (par ex. `{ type: 'json', schema: {...} }`). Certains formats requièrent la définition d’options spécifiques. Exemple : `['markdown', { type: 'json', schema: {...} }]`.

- Markdown
- Summary
- HTML
- Raw HTML
- Links
- Images
- Screenshot
- JSON
- Change Tracking
- Branding

Ne renvoyez que le contenu principal de la page, en excluant les en-têtes, éléments de navigation, pieds de page, etc.

Balises à inclure dans le résultat.

Balises à exclure du résultat.

Retourne une version mise en cache de la page si elle est plus récente que cette durée (en millisecondes). Si une version mise en cache de la page est plus ancienne que cette valeur, la page sera à nouveau explorée (scrapée). Si vous n’avez pas besoin de données extrêmement récentes, activer cette option peut accélérer vos opérations de scraping de 500 %. Par défaut : 2 jours.

Lorsqu’elle est définie, la requête vérifie uniquement le cache et ne déclenche jamais une nouvelle opération de scraping. La valeur est exprimée en millisecondes et indique l’âge minimal que doivent avoir les données en cache. Si des données en cache correspondantes existent, elles sont renvoyées instantanément. Si aucune donnée en cache n’est trouvée, une réponse 404 avec le code d’erreur SCRAPE\_NO\_CACHED\_DATA est renvoyée. Définissez-la sur 1 pour accepter n’importe quelle donnée en cache, quel que soit son âge.

En-têtes à inclure dans la requête. Peuvent être utilisés pour envoyer des cookies, un user-agent, etc.

Indiquez un délai en millisecondes avant de récupérer le contenu, afin de laisser à la page suffisamment de temps pour se charger. Ce temps d’attente s’ajoute à la fonction d’attente intelligente de Firecrawl.

Définissez cette option sur true pour simuler le scraping depuis un appareil mobile. Utile pour tester des pages responsives et prendre des captures d’écran en mode mobile.

Ignorer la vérification du certificat TLS lors des requêtes.

Délai d’expiration de la requête en millisecondes. Le minimum est de 1000 (1 seconde). La valeur par défaut est de 30000 (30 secondes). Le maximum est de 300000 (300 secondes).

Plage requise: `1000 <= x <= 300000`

Contrôle la façon dont les fichiers sont traités lors du scraping. Lorsque « pdf » est inclus (valeur par défaut), le contenu du PDF est extrait et converti au format Markdown, avec une facturation basée sur le nombre de pages (1 crédit par page). Lorsqu’un tableau vide est envoyé, le fichier PDF est renvoyé en encodage base64 avec un tarif fixe de 1 crédit pour l’ensemble du PDF.

actions

(Wait by Duration · object | Wait for Element · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

Actions à effectuer sur la page avant de récupérer le contenu

- Wait by Duration
- Wait for Element
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

Paramètres de localisation pour la requête. Lorsqu’ils sont définis, un proxy approprié sera utilisé si disponible et les paramètres de langue et de fuseau horaire correspondants seront simulés. La valeur par défaut est « US » si aucun n’est spécifié.

&lt;\[ { "key": "0", "translation": "Supprime toutes les images encodées en base64 de la sortie markdown, qui peut devenir excessivement longue. Cela n’affecte pas les formats html ou rawHtml. Le texte alternatif de l’image reste dans la sortie, mais l’URL est remplacée par un espace réservé." } ]&lt;/&gt;

Active le blocage des publicités et des fenêtres contextuelles de cookies.

Spécifie le type de proxy à utiliser.

- basic : Proxies pour le scraping de sites avec des solutions anti‑bots inexistantes ou basiques. Rapides et généralement efficaces.
- enhanced : Proxies renforcés pour le scraping de sites avec des solutions anti‑bots avancées. Plus lents, mais plus fiables sur certains sites. Peut coûter jusqu’à 5 crédits par requête.
- auto : Firecrawl réessaiera automatiquement le scraping avec des proxies renforcés si le proxy basic échoue. Si la nouvelle tentative avec le proxy renforcé réussit, 5 crédits seront facturés pour l’opération de scraping. Si la première tentative avec le proxy basic réussit, seul le coût standard sera facturé.

Options disponibles:

`basic`,

`enhanced`,

`auto`

Si ce paramètre est défini sur true, la page sera stockée dans l’index et le cache de Firecrawl. Le définir sur false est utile si votre activité de scraping peut soulever des problèmes de protection des données. L’utilisation de certains paramètres associés à un scraping sensible (par ex. actions, headers) forcera ce paramètre à false.

Si cette option est définie sur true, cela activera l’absence totale de conservation des données pour cette opération de scraping par lot. Pour activer cette fonctionnalité, veuillez contacter [help@firecrawl.dev](mailto:help@firecrawl.dev)

#### Réponse

Si ignoreInvalidURLs vaut true, ce champ est un tableau contenant les URL non valides qui ont été spécifiées dans la requête. S’il n’y a aucune URL non valide, ce sera un tableau vide. Si ignoreInvalidURLs vaut false, ce champ sera undefined.