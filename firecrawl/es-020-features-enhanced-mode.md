---
title: Modo mejorado | Firecrawl
url: https://docs.firecrawl.dev/es/features/enhanced-mode
source: sitemap
fetched_at: 2026-03-23T07:25:30.060247-03:00
rendered_js: false
word_count: 144
summary: This document explains the available proxy strategies for web scraping with Firecrawl, detailing the performance and cost characteristics of basic, enhanced, and automatic modes.
tags:
    - web-scraping
    - proxy-configuration
    - firecrawl-api
    - network-settings
    - data-extraction
category: configuration
---

Firecrawl ofrece distintos tipos de proxy para ayudarte a hacer scraping de sitios web con diferentes niveles de complejidad. Configura el parámetro `proxy` para controlar qué estrategia de proxy se utiliza para una solicitud.

## Tipos de proxy

Firecrawl admite tres tipos de proxy:

TipoDescripciónVelocidadCosto`basic`Proxies estándar adecuados para la mayoría de los sitiosRápido1 crédito`enhanced`Proxies mejorados para sitios complejosMás lento5 créditos por solicitud`auto`Primero prueba `basic` y, si falla, vuelve a intentarlo con `enhanced`Varía1 crédito si `basic` funciona, 5 créditos si se necesita `enhanced`

Si no especificas ningún proxy, Firecrawl usa `auto` de forma predeterminada.

## Uso básico

Configura el parámetro `proxy` para elegir una estrategia de proxy. En el siguiente ejemplo se usa `auto`, lo que permite que Firecrawl decida cuándo pasar a proxies mejorados.

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.