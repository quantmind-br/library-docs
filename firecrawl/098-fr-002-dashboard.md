---
title: Dashboard | Firecrawl
url: https://docs.firecrawl.dev/fr/dashboard
source: sitemap
fetched_at: 2026-03-23T07:26:28.395991-03:00
rendered_js: false
word_count: 460
summary: This document provides an overview of the Firecrawl dashboard, explaining how to manage account settings, monitor usage, and utilize the playground and browser tools.
tags:
    - firecrawl
    - dashboard-guide
    - web-scraping
    - account-management
    - api-tools
    - team-roles
category: guide
---

Le [dashboard Firecrawl](https://www.firecrawl.dev/app) vous permet de gérer votre compte, de tester des points de terminaison et de surveiller votre utilisation. Vous trouverez ci-dessous une présentation rapide de chaque section.

## Playground

Le playground vous permet de tester directement dans le navigateur les points de terminaison Firecrawl avant de les intégrer à votre code.

- [**Scrape**](https://www.firecrawl.dev/app/playground?endpoint=scrape) — Extraire le contenu d’une seule page.
- [**Search**](https://www.firecrawl.dev/app/playground?endpoint=search) — Effectuer une recherche sur le web et obtenir des résultats scrapés.
- [**Crawl**](https://www.firecrawl.dev/app/playground?endpoint=crawl) — Effectuer le crawl d’un site web entier et extraire le contenu de chaque page.
- [**Map**](https://www.firecrawl.dev/app/playground?endpoint=map) — Découvrir toutes les URL d’un site web.

## Browser

[Interagissez avec le web](https://www.firecrawl.dev/app/browser) via une session de navigateur en direct. Vous pouvez créer des profils persistants, exécuter des actions et faire des captures d’écran — idéal pour les pages qui nécessitent une authentification ou une interaction complexe.

## Agent

L’[Agent](https://www.firecrawl.dev/app/agent) est un outil de recherche propulsé par l’IA capable de naviguer sur le web de manière autonome, de suivre des liens et d’extraire des données structurées à partir d’un prompt.

## Journaux d’activité

Les [journaux d’activité](https://www.firecrawl.dev/app/logs) affichent l’historique de vos requêtes API récentes, y compris l’état, la durée et les crédits consommés.

## Usage

La page [Usage](https://www.firecrawl.dev/app/usage) affiche votre consommation de crédits au fil du temps ainsi que les totaux actuels du cycle de facturation.

## Clés API

Sur la page [API Keys](https://www.firecrawl.dev/app/api-keys), vous pouvez créer, consulter et révoquer les clés API de votre équipe.

## Paramètres

La page [Paramètres](https://www.firecrawl.dev/app/settings) comporte trois onglets :

- **Équipe** — Invitez des membres, attribuez des rôles et gérez votre équipe. Voir [Gestion d’équipe et rôles](#team-management--roles) ci-dessous.
- **Facturation** — Consultez votre offre actuelle, vos factures, les paramètres d’auto-recharge et appliquez des codes promo. Voir aussi [Facturation](https://docs.firecrawl.dev/fr/billing).
- **Avancé** — Secret de signature du Webhook et suppression de l’équipe.

* * *

## Gestion d’équipe et rôles

Firecrawl vous permet d’inviter des membres de votre équipe à collaborer au sein d’un compte partagé. Depuis l’onglet **Équipe** dans les paramètres, vous pouvez inviter des membres, attribuer des rôles et gérer votre équipe.

### Rôles

Chaque membre de l’équipe se voit attribuer l’un des deux rôles suivants : **Admin** ou **Member**. Vous choisissez ce rôle lors de l’envoi d’une invitation.

CapabilityAdminMember**Général**Utiliser les clés API de l’équipe et les ressources partagées✓✓**Gestion de l’équipe**Consulter la liste des membres de l’équipe✓✓Quitter l’équipe✓✓Inviter de nouveaux membres de l’équipe✓✗Supprimer des membres de l’équipe✓✗Modifier le rôle d’un membre✓✗Révoquer les invitations en attente✓✗Modifier le nom de l’équipe✓✗**Facturation**Consulter les factures et l’utilisation✓✓Appliquer des coupons de crédit✓✓Gérer l’abonnement et le portail de facturation✓✗**Paramètres**Consulter le secret de signature du Webhook✓✓Régénérer le secret de signature du Webhook✓✗Supprimer l’équipe✓✗

En bref, les **Admins** ont un contrôle total sur la gestion de l’équipe, la facturation et les paramètres, tandis que les **Members** peuvent utiliser les ressources de l’équipe, consulter l’utilisation et appliquer des coupons, mais ne peuvent pas modifier l’équipe ni l’abonnement.