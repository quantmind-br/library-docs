---
title: Modo Aprimorado | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/enhanced-mode
source: sitemap
fetched_at: 2026-03-23T07:21:57.66655-03:00
rendered_js: false
word_count: 148
summary: This document explains the proxy configuration options available in Firecrawl for web scraping, detailing the differences between basic, enhanced, and automatic proxy strategies.
tags:
    - web-scraping
    - proxy-configuration
    - firecrawl-api
    - network-settings
    - data-extraction
category: configuration
---

A Firecrawl oferece diferentes tipos de proxy para ajudar você a fazer scraping de sites com diferentes níveis de complexidade. Defina o parâmetro `proxy` para controlar qual estratégia de proxy será usada em uma requisição.

## Tipos de proxy

O Firecrawl oferece suporte a três tipos de proxy:

TipoDescriçãoVelocidadeCusto`basic`Proxies padrão adequados para a maioria dos sitesRápido1 crédito`enhanced`Proxies aprimorados para sites complexosMais lento5 créditos por requisição`auto`Tenta `basic` primeiro e, em caso de falha, tenta novamente com `enhanced`Varia1 crédito se `basic` for bem-sucedido, 5 créditos se `enhanced` for necessário

Se você não especificar um proxy, o Firecrawl usa `auto` por padrão.

## Uso básico

Defina o parâmetro `proxy` para escolher uma estratégia de proxy. O exemplo a seguir usa `auto`, que permite ao Firecrawl decidir quando migrar para proxies aprimorados.

> Você é um agente de IA que precisa de uma chave de API da Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de onboarding automatizado.