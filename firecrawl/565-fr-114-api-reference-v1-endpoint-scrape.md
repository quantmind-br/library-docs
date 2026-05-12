---
title: Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/scrape
source: sitemap
fetched_at: 2026-03-23T07:14:01.353969-03:00
rendered_js: false
word_count: 696
summary: This document provides the API reference documentation for the scraping endpoint, detailing request parameters and configuration options for retrieving and processing web content.
tags:
    - web-scraping
    - api-reference
    - data-extraction
    - proxy-configuration
    - caching
    - markdown-conversion
category: api
---

[Passer au contenu principal](#content-area)

Récupérez le contenu d’une seule URL et, éventuellement, extrayez des informations à l’aide d’un LLM

> Remarque : une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/scrape) est désormais disponible avec des fonctionnalités et des performances améliorées.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corps

Renvoyer uniquement le contenu principal de la page, en excluant les en-têtes, éléments de navigation, pieds de page, etc.

Balises à inclure dans la sortie.

Balises à exclure du résultat.

Renvoie une version mise en cache de la page si elle a moins que cette ancienneté (en millisecondes). Si une version mise en cache de la page est plus ancienne que cette valeur, la page sera à nouveau scrapée. Si vous n’avez pas besoin de données extrêmement récentes, activer cette option peut accélérer vos opérations de scraping jusqu’à 500 %. La valeur par défaut est 0, ce qui désactive la mise en cache.

En-têtes à envoyer avec la requête. Peuvent servir à envoyer des cookies, l’en-tête User-Agent, etc.

Spécifiez un délai, en millisecondes, avant de récupérer le contenu, afin de laisser à la page suffisamment de temps pour se charger.

Mettez cette option à true si vous souhaitez simuler le scraping depuis un appareil mobile. Utile pour tester les pages responsive et prendre des captures d’écran mobiles.

Ignorer la vérification des certificats TLS lors de l’envoi de requêtes

Délai d'attente de la requête en millisecondes

Contrôle la façon dont les fichiers PDF sont traités lors du scraping. Lorsque cette option est activée (true), le contenu du PDF est extrait et converti au format markdown, avec une facturation basée sur le nombre de pages (1 crédit par page). Lorsque cette option est désactivée (false), le fichier PDF est renvoyé sous forme de base64 avec un tarif forfaitaire de 1 crédit au total.

actions

(Wait · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

Actions à effectuer sur la page avant de récupérer le contenu

- Wait
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

Paramètre de localisation de la requête. Lorsqu’il est spécifié, un proxy approprié est utilisé si disponible et la langue ainsi que le fuseau horaire correspondants sont émulés. Par défaut, « US » est utilisé si aucun paramètre n’est spécifié.

Supprime toutes les images encodées en base64 de la sortie, qui peuvent être extrêmement longues. Le texte alternatif de l’image est conservé dans la sortie, mais l’URL est remplacée par un placeholder.

Active le blocage des publicités et des bannières de cookies.

Spécifie le type de proxy à utiliser.

- basic�a0: Proxys pour le scraping de sites sans protection anti-bot ou avec des protections basiques. Rapide et généralement fiable.
- enhanced�a0: Proxys avancés pour le scraping de sites avec des solutions anti-bot sophistiquées. Plus lents, mais plus fiables sur certains sites. Coût pouvant aller jusqu’à 5 crédits par requête.
- auto�a0: Firecrawl réessaie automatiquement le scraping avec des proxys enhanced si le proxy basic échoue. Si le nouvel essai avec enhanced réussit, 5 crédits seront facturés pour l’opération de scraping. Si la première tentative avec basic réussit, seul le coût normal sera facturé.

Si vous ne spécifiez pas de proxy, Firecrawl utilisera basic par défaut.

Options disponibles:

`basic`,

`enhanced`,

`auto`

Si ce paramètre est défini sur true, la page sera stockée dans l’index et le cache de Firecrawl. Le définir sur false est utile si votre activité de scraping peut soulever des enjeux de protection des données. L’utilisation de certains paramètres associés à un scraping sensible (actions, en-têtes) forcera ce paramètre à false.

Formats à inclure dans le résultat.

Options disponibles:

`markdown`,

`html`,

`rawHtml`,

`links`,

`screenshot`,

`screenshot@fullPage`,

`json`,

`changeTracking`

Options de suivi des modifications (bêta). Applicable uniquement lorsque « changeTracking » est inclus dans les formats. Le format « markdown » doit également être spécifié lors de l’utilisation du suivi des modifications.

Si cette valeur est définie sur true, cela activera l’absence de conservation des données pour cette opération de scraping. Pour activer cette fonctionnalité, veuillez contacter [help@firecrawl.dev](mailto:help@firecrawl.dev)

#### Réponse