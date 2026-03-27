---
title: Agente de IA FIRE-1 (Beta) | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/agents/fire-1
source: sitemap
fetched_at: 2026-03-23T07:34:56.82342-03:00
rendered_js: false
word_count: 176
summary: This document introduces FIRE-1, an AI-powered agent designed for complex web scraping tasks that require browser interaction and multi-page navigation.
tags:
    - fire-1
    - ai-scraping
    - browser-automation
    - data-extraction
    - firecrawl
category: concept
---

FIRE-1 é um agente de IA que potencializa os recursos de scraping do Firecrawl. Ele pode controlar ações do navegador e navegar por estruturas complexas de sites para possibilitar uma extração de dados mais completa do que os métodos tradicionais de scraping.

### O que o FIRE-1 pode fazer:

- Planejar e executar ações para descobrir dados
- Interagir com botões, links, campos de entrada e elementos dinâmicos.
- Obter várias páginas de dados que precisam de paginação, várias etapas etc.

## Como usar o FIRE-1

Você pode aproveitar o agente FIRE-1 com o endpoint `/v1/extract` para tarefas de extração complexas que exigem navegação por várias páginas ou interação com elementos. **Exemplo:**

## Cobrança

O custo de usar o FIRE-1 é não determinístico. Veja nossa [calculadora de créditos](https://www.firecrawl.dev/extract-calculator) para entender o custo básico de cada solicitação de Extract. **Por que o FIRE-1 é mais caro?**  
O FIRE-1 utiliza automação avançada de navegador e planejamento com IA para interagir com páginas da web complexas, o que exige mais recursos computacionais do que a extração padrão.

## Limites de uso

- `/extract`: 10 solicitações por minuto