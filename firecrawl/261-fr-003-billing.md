---
title: Facturation | Firecrawl
url: https://docs.firecrawl.dev/fr/billing
source: sitemap
fetched_at: 2026-03-23T07:27:01.38975-03:00
rendered_js: false
word_count: 1409
summary: This document outlines the credit-based billing system used by Firecrawl, detailing how various API endpoints consume credits, how to track usage, and how subscription plans and automatic recharges function.
tags:
    - api-billing
    - credit-usage
    - firecrawl-pricing
    - subscription-plans
    - api-costs
    - usage-tracking
category: concept
---

## Vue d’ensemble

Firecrawl utilise un **système de facturation basé sur des crédits**. Chaque appel à l’API que vous effectuez consomme des crédits, et le nombre de crédits consommés dépend de l’endpoint et des options que vous utilisez. Vous disposez d’un quota mensuel de crédits en fonction de votre offre, et vous pouvez acheter des crédits supplémentaires via des packs de rechargement automatique si vous avez besoin de plus. Pour consulter les tarifs actuels, rendez-vous sur la [page de tarification Firecrawl](https://www.firecrawl.dev/pricing).

## Crédits

Les crédits sont l’unité d’utilisation dans Firecrawl. Chaque offre inclut un quota mensuel de crédits qui est réinitialisé au début de chaque cycle de facturation. Différents endpoints d’API consomment un nombre de crédits différent.

### Coût en crédits par point de terminaison

Point de terminaisonCoût en créditsNotes**Scrape**1 crédit / pageConvertit une URL unique en markdown propre, HTML ou données structurées. Des crédits supplémentaires s’appliquent lors de l’utilisation des options d’extraction (voir ci-dessous).**Crawl**1 crédit / pageScrape un site web entier en suivant les liens à partir d’une URL de départ. Les mêmes coûts des options d’extraction par page s’appliquent à chaque page explorée.**Map**1 crédit / appelDécouvre toutes les URL d’un site web sans scraper leur contenu.**Search**2 crédits / 10 résultatsRecherche sur le web et, en option, scrape les résultats. Des coûts supplémentaires de scraping par page s’appliquent à chaque résultat qui est scrapé. Les coûts de recherche ZDR Enterprise sont de 10 crédits / 10 résultats (voir [ZDR Search](https://docs.firecrawl.dev/fr/features/search#zero-data-retention-zdr)).**Browser**2 crédits / minute de navigateurSession de bac à sable navigateur interactive, facturée à la minute.**Agent**DynamiqueAgent autonome de recherche web. 5 exécutions quotidiennes gratuites ; tarification à l’usage au-delà de ce quota.

Certaines options d’extraction ajoutent des crédits en plus du coût de base par page :

OptionCoût supplémentaireDescriptionPDF parsing+1 crédit / page PDFExtraire le contenu de documents PDFJSON format (LLM extraction)+4 crédits / pageUtiliser un LLM pour extraire des données JSON structurées à partir de la pageEnhanced Mode+4 crédits / pageScrape amélioré pour les pages difficiles d’accèsZero Data Retention (ZDR)+1 crédit / pageGarantit qu’aucune donnée n’est conservée au-delà de la requête (voir [Scrape ZDR](https://docs.firecrawl.dev/fr/features/scrape#zero-data-retention-zdr))

Ces modificateurs se cumulent. Par exemple, scraper une page avec à la fois le format JSON et le mode Enhanced coûte **1 + 4 + 4 = 9 crédits** par page. Ces mêmes modificateurs s’appliquent aux points de terminaison Crawl et Search, puisqu’ils utilisent `scrape` en interne pour chaque page.

### Quand les crédits sont débités

Pour les tâches de **batch scrape** et de **crawl**, les crédits sont facturés de manière asynchrone à mesure que chaque page est traitée — et non au moment où la tâche est soumise. Cela signifie qu’il peut y avoir un délai entre l’envoi d’une tâche et le moment où le coût total en crédits apparaît sur votre compte. Si un batch contient de nombreuses URL ou si des pages sont mises en file d’attente pendant des périodes de fort trafic, des crédits peuvent continuer à être débités et à apparaître minutes ou heures après la soumission. Le polling ou la consultation du statut d’un batch ne consomment pas de crédits.

### Suivi de votre consommation de crédits

Vous pouvez suivre votre consommation de crédits de deux manières :

- **Tableau de bord** : consultez votre consommation actuelle et historique sur [firecrawl.dev/app](https://www.firecrawl.dev/app)
- **API** : utilisez les points de terminaison [Credit Usage](https://docs.firecrawl.dev/fr/api-reference/endpoint/credit-usage) et [Credit Usage Historical](https://docs.firecrawl.dev/fr/api-reference/endpoint/credit-usage-historical) pour vérifier votre consommation par programmation

## Formules

Firecrawl propose des formules mensuelles par abonnement. Il n’existe pas d’offre purement à l’usage, mais la recharge automatique (décrite ci‑dessous) permet une mise à l’échelle flexible au‑delà de votre formule de base.

### Forfaits disponibles

ForfaitCrédits mensuelsNavigateurs simultanés**Free**500 (une seule fois)2**Hobby**3,0005**Standard**100,00050**Growth**500,000100

Tous les forfaits payants sont disponibles avec une facturation **mensuelle** ou **annuelle**. La facturation annuelle propose une remise par rapport au paiement mensuel. Pour les tarifs actuels de chaque forfait, consultez la [page de tarification](https://www.firecrawl.dev/pricing).

### Navigateurs simultanés

Les navigateurs simultanés correspondent au nombre de pages web que Firecrawl peut traiter en parallèle pour vous. Votre offre détermine cette limite. Si vous la dépassez, les tâches supplémentaires attendent dans une file d’attente jusqu’à ce qu’un créneau se libère. Consultez [Limites de débit](https://docs.firecrawl.dev/fr/rate-limits) pour tous les détails sur la concurrence et les limites de débit de l’API.

## Recharge automatique

Si vous avez occasionnellement besoin de plus de crédits que ceux inclus dans votre offre, vous pouvez activer la **recharge automatique** depuis le tableau de bord. Lorsque vos crédits restants passent sous un seuil configurable, Firecrawl achète automatiquement un pack de crédits supplémentaire et l’ajoute à votre solde.

- Les packs de recharge automatique sont disponibles avec toutes les offres payantes
- La taille et le prix des packs varient selon l’offre (consultables sur la [page de tarification](https://www.firecrawl.dev/pricing))
- Vous pouvez configurer le seuil de recharge et activer ou désactiver la recharge automatique à tout moment
- La recharge automatique est limitée à **4 packs par mois**
- Les crédits des packs de recharge automatique **ne sont pas réinitialisés chaque mois** — ils sont conservés d’un cycle de facturation à l’autre et expirent **1 an** après l’achat, contrairement aux crédits mensuels de votre offre qui sont réinitialisés à chaque période.

La recharge automatique est idéale pour gérer des pics d’utilisation ponctuels. Si vous dépassez régulièrement le quota inclus dans votre offre, passer à une offre supérieure vous offrira un meilleur tarif par crédit.

## Coupons

Firecrawl prend en charge deux types de coupons :

- **Les coupons d’abonnement** appliquent une réduction à votre abonnement (par ex. un pourcentage de réduction sur votre tarif mensuel ou annuel). Ils peuvent **uniquement** être appliqués pendant le processus de paiement Stripe, lorsque vous souscrivez pour la première fois à une offre payante ou changez d’offre. Vous ne pouvez pas appliquer un coupon d’abonnement une fois le paiement terminé.
- **Les coupons de crédit** ajoutent des crédits bonus à votre compte. Ils peuvent être utilisés depuis la section **Facturation** de votre tableau de bord à l’adresse [firecrawl.dev/app/billing](https://www.firecrawl.dev/app/billing). Recherchez le champ de saisie du coupon sur la page de facturation pour appliquer votre code. Les crédits bonus issus des coupons de crédit sont distincts du quota mensuel de votre offre et sont conservés même si vous passez à une offre supérieure ou inférieure.

Si vous avez un code promo et ne savez pas de quel type il s’agit, essayez d’abord de l’appliquer dans la section de facturation de votre tableau de bord. S’il s’agit d’un coupon d’abonnement, vous devrez l’utiliser à la place sur la page de paiement Stripe.

## Cycle de facturation

- **Offres mensuelles** : les crédits sont réinitialisés à votre date de renouvellement mensuelle
- **Offres annuelles** : vous êtes facturé une fois par an, mais les crédits sont tout de même réinitialisés chaque mois à votre date de renouvellement mensuelle virtuelle
- **Les crédits d’offre inutilisés ne sont pas reportés** — votre quota mensuel est réinitialisé au montant prévu par l’offre au début de chaque période de facturation. Les crédits des packs de recharge automatique ne sont pas liés à votre cycle de facturation — ils restent disponibles et expirent **1 an** à compter de la date d’achat.

## Mise à niveau et rétrogradation

- Les **mises à niveau** prennent effet immédiatement. Vous êtes facturé au prorata pour le reste de la période de facturation en cours, et votre quota de crédits ainsi que vos limites sont mis à jour immédiatement.
- Les **rétrogradations** sont programmées pour prendre effet à votre prochaine date de renouvellement. Vous conservez les crédits et limites de votre offre actuelle jusqu’à cette date.

## Que se passe-t-il lorsque vous n’avez plus de crédits

Si vous épuisez votre quota de crédits et que la recharge automatique n’est pas activée, les requêtes API qui consomment des crédits renverront une erreur **HTTP 402 (Payment Required)**. Si la recharge automatique est activée, l’utilisation se poursuivra pendant que des packs de recharge sont achetés automatiquement — mais si la limite mensuelle de packs est atteinte ou si une recharge échoue, votre solde peut devenir négatif jusqu’au prochain cycle de facturation ou jusqu’à un rechargement manuel. Pour reprendre l’utilisation après un arrêt complet, vous pouvez :

1. Activer la recharge automatique pour acheter automatiquement plus de crédits
2. Passer à une formule supérieure
3. Attendre la réinitialisation de vos crédits au prochain cycle de facturation

## Offre gratuite

L’offre gratuite propose un **crédit unique de 500 crédits** sans nécessiter de carte de crédit. Ces crédits ne se renouvellent pas : une fois qu’ils sont épuisés, vous devrez passer à une offre payante pour continuer à utiliser Firecrawl. L’offre gratuite impose également des limites de débit et de parallélisme plus basses que les offres payantes (voir [Limitations de débit](https://docs.firecrawl.dev/fr/rate-limits)).

## FAQ