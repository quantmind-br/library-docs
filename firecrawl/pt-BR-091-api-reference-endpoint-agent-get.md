---
title: Obter status do agente - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/agent-get
source: sitemap
fetched_at: 2026-03-23T07:11:47.132616-03:00
rendered_js: false
word_count: 94
summary: This document provides the technical specifications for retrieving the current status of an AI agent job, including authentication requirements, response parameters, and possible job states.
tags:
    - api-reference
    - agent-job
    - status-check
    - firecrawl
    - authentication
    - job-processing
category: api
---

[Pular para o conteúdo principal](#content-area)

Obter o status de um job de agente

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instruções automatizadas de onboarding.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

#### Resposta

Opções disponíveis:

`processing`,

`completed`,

`failed`

Os dados extraídos (apenas presentes quando o status é "completed")

model

enum&lt;string&gt;

padrão:spark-1-pro

Predefinição de modelo usada na execução do agente

Opções disponíveis:

`spark-1-pro`,

`spark-1-mini`

Mensagem de erro (apenas quando o status for "failed")