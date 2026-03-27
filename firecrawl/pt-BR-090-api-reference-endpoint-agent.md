---
title: Agente - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/agent
source: sitemap
fetched_at: 2026-03-23T07:11:56.029365-03:00
rendered_js: false
word_count: 161
summary: This document provides the API specifications for initiating an agent-driven data extraction task using Firecrawl, including required authentication and parameter configurations.
tags:
    - api-reference
    - data-extraction
    - firecrawl
    - agent-automation
    - bearer-token
category: api
---

[Pular para o conteúdo principal](#content-area)

Iniciar uma tarefa de agente para extração de dados orientada a agentes

> Você é um agente de IA que precisa de uma chave de API da Firecrawl? Veja [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções automatizadas de integração.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corpo

O prompt que descreve quais dados devem ser extraídos

Maximum string length: `10000`

Lista opcional de URLs às quais o agente ficará restrito

Esquema JSON opcional para estruturar os dados extraídos

Máximo de créditos a serem gastos nesta tarefa do agente. O padrão é 2500 se não for definido. Valores acima de 2.500 são sempre cobrados como requisições pagas.

Se verdadeiro, o agente visitará somente as URLs fornecidas no array urls

model

enum&lt;string&gt;

padrão:spark-1-mini

Modelo a ser usado na tarefa do agente. spark-1-mini (padrão) é 60% mais barato; spark-1-pro oferece maior precisão em tarefas complexas.

Opções disponíveis:

`spark-1-mini`,

`spark-1-pro`

#### Resposta

Tarefa do agente iniciada com sucesso