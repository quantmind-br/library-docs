---
title: Agent IA FIRE-1 (bêta) | Firecrawl
url: https://docs.firecrawl.dev/fr/agents/fire-1
source: sitemap
fetched_at: 2026-03-23T07:36:12.057063-03:00
rendered_js: false
word_count: 181
summary: This document introduces FIRE-1, an AI agent for Firecrawl designed to automate complex web scraping tasks and browser interactions.
tags:
    - ai-agent
    - web-scraping
    - browser-automation
    - data-extraction
    - firecrawl
category: concept
---

FIRE-1 est un agent d’IA qui renforce les capacités de scraping de Firecrawl. Il peut contrôler des actions du navigateur et naviguer dans des architectures de sites web complexes afin de permettre une extraction de données plus complète que les méthodes de scraping traditionnelles.

### Ce que FIRE-1 peut faire :

- Planifier et exécuter des actions pour extraire des données
- Interagir avec des boutons, des liens, des champs de saisie et des éléments dynamiques.
- Récupérer plusieurs pages de données nécessitant une pagination, plusieurs étapes, etc.

Vous pouvez exploiter l’agent FIRE-1 avec l’endpoint `/v1/extract` pour des tâches d’extraction complexes nécessitant une navigation sur plusieurs pages ou des interactions avec des éléments. **Exemple :**

## Facturation

Le coût d’utilisation de FIRE-1 n’est pas déterministe. Consultez notre [calculateur de crédits](https://www.firecrawl.dev/extract-calculator) pour connaître le coût de base de chaque requête Extract. **Pourquoi FIRE-1 est-il plus coûteux ?**  
FIRE-1 s’appuie sur une automatisation avancée du navigateur et une planification par IA pour interagir avec des pages web complexes, ce qui nécessite davantage de ressources de calcul qu’une extraction standard.

## Limites de débit

- `/extract` : 10 requêtes par minute