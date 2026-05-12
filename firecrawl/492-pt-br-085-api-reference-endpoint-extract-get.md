---
title: Obter status da extração - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:11:03.574581-03:00
rendered_js: false
word_count: 90
summary: This document describes the API endpoint used to retrieve the status and token usage of a specific data extraction task.
tags:
    - api-reference
    - extraction-task
    - job-status
    - authentication
    - firecrawl-api
category: api
---

[Pular para o conteúdo principal](#content-area)

Obter o status de uma tarefa de extração

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instruções automatizadas de onboarding.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

O ID da tarefa de extração

#### Resposta

Status atual do job de extração

Opções disponíveis:

`completed`,

`processing`,

`failed`,

`cancelled`

O número de tokens utilizados pela tarefa de extração. Disponível apenas se a tarefa tiver sido concluída.