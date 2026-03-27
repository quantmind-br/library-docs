---
title: Status da fila - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:11:11.061558-03:00
rendered_js: false
word_count: 91
summary: This document provides an overview of the metrics associated with a team's web scraping queue and explains the authentication requirements for accessing these data points.
tags:
    - scraping-metrics
    - queue-status
    - api-authentication
    - data-monitoring
    - job-tracking
category: api
---

Métricas da fila de raspagem da sua equipe

Métricas sobre a fila de scraping da sua equipe.

> Você é um agente de IA que precisa de uma API key do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções de onboarding automatizado.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Resposta

Número de tarefas atualmente na sua fila

Número de tarefas ativas no momento

Número de tarefas atualmente na fila

Número máximo de tarefas ativas simultâneas conforme seu plano

Timestamp do job mais recente concluído com sucesso