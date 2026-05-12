---
title: Agent - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/agent
source: sitemap
fetched_at: 2026-03-23T07:15:59.976724-03:00
rendered_js: false
word_count: 179
summary: This document provides the API specifications and configuration parameters for initiating an agent-driven data extraction task using Firecrawl.
tags:
    - api-reference
    - data-extraction
    - firecrawl
    - agent-task
    - authentication
category: api
---

[Passer au contenu principal](#content-area)

Démarrer une tâche d’agent pour l’extraction de données pilotée par un agent

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corps

Le prompt décrivant les données à extraire

Maximum string length: `10000`

Liste facultative d’URL servant à limiter l’agent

Schéma JSON facultatif pour structurer les données extraites

&lt;\[ { "key": "0", "translation": "Nombre maximal de crédits à utiliser pour cette tâche d’agent. La valeur par défaut est de 2500 si elle n’est pas spécifiée. Les valeurs supérieures à 2 500 sont toujours facturées comme des requêtes payantes." } ]&lt;/&gt;

Si la valeur est true, l’agent ne visitera que les URL fournies dans le tableau urls

model

enum&lt;string&gt;

défaut:spark-1-mini

Le modèle à utiliser pour les tâches d’agent. spark-1-mini (par défaut) coûte 60 % de moins, tandis que spark-1-pro offre une meilleure précision pour les tâches complexes.

Options disponibles:

`spark-1-mini`,

`spark-1-pro`

#### Réponse

La tâche de l’agent a démarré avec succès