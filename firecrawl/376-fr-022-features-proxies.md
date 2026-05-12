---
title: Proxys | Firecrawl
url: https://docs.firecrawl.dev/fr/features/proxies
source: sitemap
fetched_at: 2026-03-23T07:23:52.157747-03:00
rendered_js: false
word_count: 346
summary: This document explains how to configure proxy settings in Firecrawl, including choosing specific geographical locations and selecting between basic, enhanced, or automated proxy modes for web scraping.
tags:
    - firecrawl
    - web-scraping
    - proxy-configuration
    - data-extraction
    - proxy-locations
category: guide
---

Firecrawl propose différents types de proxy pour vous aider à scraper des sites web présentant des niveaux de complexité variés. Le type de proxy peut être spécifié à l’aide du paramètre `proxy`.

> Par défaut, Firecrawl achemine toutes les requêtes via des proxy afin d’assurer la fiabilité et l’accessibilité, même si vous ne spécifiez pas de type de proxy ni de localisation.

## Sélection de proxy selon la localisation

Firecrawl sélectionne automatiquement le meilleur proxy en fonction de votre localisation spécifiée ou détectée. Cela optimise les performances et la fiabilité du scraping. Cependant, toutes les localisations ne sont pas encore prises en charge. Les localisations suivantes sont disponibles :

Country CodeNom du paysPrise en charge proxy standardPrise en charge proxy avancéeAEÉmirats arabes unisOuiNonAUAustralieOuiNonBRBrésilOuiNonCACanadaOuiNonCNChineOuiNonCZTchéquieOuiNonDEAllemagneOuiNonEEEstonieOuiNonEGÉgypteOuiNonESEspagneOuiNonFRFranceOuiNonGBRoyaume-UniOuiNonGRGrèceOuiNonHUHongrieOuiNonIDIndonésieOuiNonILIsraëlOuiNonINIndeOuiNonITItalieOuiNonJPJaponOuiNonMYMalaisieOuiNonNONorvègeOuiNonPLPologneOuiNonPTPortugalOuiNonQAQatarOuiNonSGSingapourOuiNonUSÉtats-UnisOuiOuiVNVietnamOuiNon

Si vous avez besoin de proxies dans une localisation non répertoriée ci-dessus, veuillez [nous contacter](mailto:help@firecrawl.com) et nous indiquer vos besoins. Si vous ne spécifiez pas de proxy ou de localisation, Firecrawl utilisera automatiquement des proxies US.

Vous pouvez demander un emplacement de proxy spécifique en définissant le paramètre `location.country` dans votre requête. Par exemple, pour utiliser un proxy au Brésil, définissez `location.country` sur `BR`. Pour plus de détails, consultez la [référence de l’API pour `location.country`](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-location).

## Types de proxies

Firecrawl prend en charge trois types de proxies :

- **basic** : Proxies pour le scraping de la plupart des sites. Rapides et généralement efficaces.
- **enhanced** : Proxies avancés pour le scraping de sites complexes tout en préservant la confidentialité. Plus lents, mais plus fiables sur certains sites. [En savoir plus sur le mode avancé →](https://docs.firecrawl.dev/fr/features/enhanced-mode)
- **auto** : Firecrawl réessaiera automatiquement le scraping avec des proxies avancés si le proxy basic échoue. Si la nouvelle tentative avec avancé réussit, 5 crédits seront facturés pour le scraping. Si la première tentative avec basic réussit, seul le coût normal sera facturé.

* * *

> **Remarque :** Pour des informations détaillées sur l’utilisation des proxies avancés, y compris les coûts en crédits et les stratégies de nouvelle tentative, consultez la [documentation du mode avancé](https://docs.firecrawl.dev/fr/features/enhanced-mode).

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.