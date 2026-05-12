---
title: Limites de débit | Firecrawl
url: https://docs.firecrawl.dev/fr/rate-limits
source: sitemap
fetched_at: 2026-03-23T07:27:38.535899-03:00
rendered_js: false
word_count: 498
summary: This document outlines the billing model, concurrency limits, and rate limits for using the Firecrawl platform across different subscription tiers.
tags:
    - billing-model
    - api-rate-limits
    - concurrency-limits
    - subscription-plans
    - browser-sessions
category: reference
---

## Modèle de facturation

Firecrawl utilise des abonnements mensuels. Nous ne proposons pas de modèle de paiement à l’usage, mais notre **fonction de rechargement automatique** offre une mise à l’échelle flexible : une fois que vous avez souscrit à une offre, vous pouvez acheter automatiquement des crédits supplémentaires lorsque vous passez sous un certain seuil, avec de meilleurs tarifs sur les packs de rechargement automatique plus importants. Pour tester avant de vous engager sur une offre de niveau supérieur, commencez par l’offre Free ou Hobby. Les changements vers une offre inférieure sont programmés pour prendre effet au prochain renouvellement, et aucun avoir correspondant au temps non utilisé n’est émis.

## Limites de navigateurs concurrents

Les navigateurs concurrents correspondent au nombre de pages web que Firecrawl peut traiter pour vous en parallèle. Votre offre détermine combien de ces tâches peuvent s’exécuter simultanément — si vous dépassez cette limite, les tâches supplémentaires patienteront dans une file d’attente jusqu’à ce que des ressources se libèrent. Notez que le temps passé dans la file d’attente est décompté du paramètre [`timeout`](https://docs.firecrawl.dev/fr/advanced-scraping-guide#timing-and-cache) de la requête, vous pouvez donc définir un délai d’expiration plus court pour provoquer un échec rapide plutôt que d’attendre. Vous pouvez également vérifier la disponibilité actuelle via l’endpoint [Queue Status](https://docs.firecrawl.dev/fr/api-reference/endpoint/queue-status).

### offre actuelle

offreNavigateurs concurrentsNombre maximal de tâches en file d’attenteFree250,000Hobby550,000Standard50100,000Growth100200,000Scale / Enterprise150+300,000+

Chaque équipe a un nombre maximal de tâches pouvant attendre dans la file d’attente de concurrence. Si vous dépassez cette limite, les nouvelles tâches seront rejetées avec un code d’état `429` jusqu’à ce que les tâches existantes soient terminées. Pour les offres plus élevées avec des limites de concurrence personnalisées, le nombre maximal de tâches en file d’attente est égal à 2 000 fois votre limite de concurrence, avec un plafond de 2 000 000. Si vous avez besoin de limites de concurrence plus élevées, [contactez-nous pour les offres Enterprise](https://firecrawl.dev/enterprise).

offreNavigateurs concurrentsNombre maximal de tâches en file d’attenteFree250,000Starter50100,000Explorer100200,000Pro200400,000

Les limites de débit sont mesurées en requêtes par minute et servent principalement à prévenir les abus. Lorsqu’elles sont correctement configurées, votre véritable goulot d’étranglement sera le nombre de navigateurs exécutés en parallèle.

### Offres actuelles

Plan/scrape/map/crawl/search/agent/crawl/status/agent/statusFree101015101500500Hobby1001001550100150025000Standard50050050250500150025000Growth5000500025025001000150025000Scale75007500750750010002500025000

Ces limites de débit sont appliquées afin de garantir une utilisation équitable de l’API et sa disponibilité pour tous les utilisateurs. Si vous avez besoin de limites plus élevées, veuillez nous contacter à [help@firecrawl.com](mailto:help@firecrawl.com) pour discuter d’offres personnalisées.

Les endpoints d’extraction partagent les mêmes limites de débit que les limites de débit correspondantes de `/agent`.

Les endpoints d’extraction par lots partagent les mêmes limites de débit que les limites de `/crawl` correspondantes.

### Sessions de navigateur

Tant que le point de terminaison `/browser` est en préversion, chaque équipe peut avoir jusqu’à 20 sessions de navigateur actives à la fois. Si vous dépassez cette limite, les nouvelles requêtes de session renverront un code d’état `429` jusqu’à ce que les sessions existantes soient détruites.

### Agent FIRE-1

Les requêtes impliquant l’agent FIRE-1 ont des limites de débit distinctes, calculées séparément pour chaque endpoint :

EndpointLimite de débit (requêtes/min)/scrape10/extract10

Offre/extract (requêtes/min)/extract/status (requêtes/min)Starter10025000Explorer50025000Pro100025000