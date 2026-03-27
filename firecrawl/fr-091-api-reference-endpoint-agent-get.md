---
title: Récupérer l’état de l’agent - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/agent-get
source: sitemap
fetched_at: 2026-03-23T07:15:49.250773-03:00
rendered_js: false
word_count: 98
summary: This document describes the API endpoint used to retrieve the status, extracted data, and error information for a specific agent task.
tags:
    - api-reference
    - agent-tasks
    - status-retrieval
    - firecrawl-api
    - task-status
category: api
---

[Passer au contenu principal](#content-area)

Récupérer l’état d’une tâche d’agent

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’ID de la tâche de l’agent

#### Réponse

Options disponibles:

`processing`,

`completed`,

`failed`

Les données extraites (uniquement présentes lorsque le statut est « completed »)

model

enum&lt;string&gt;

défaut:spark-1-pro

Préréglage du modèle utilisé lors de l’exécution de l’agent

Options disponibles:

`spark-1-pro`,

`spark-1-mini`

Message d’erreur (présent uniquement lorsque le statut est « failed »)