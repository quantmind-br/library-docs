---
title: Firecrawl + Dify - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/workflow-automation/dify
source: sitemap
fetched_at: 2026-03-23T07:39:14.041999-03:00
rendered_js: false
word_count: 243
summary: This document provides an overview of integrating the Firecrawl platform with Dify to enable web scraping and data extraction capabilities within LLM-powered workflows and AI agents.
tags:
    - dify
    - firecrawl
    - ai-agents
    - web-scraping
    - llm-workflows
    - data-extraction
    - automation
category: guide
---

## Descripción general de la integración con Dify

Dify es una plataforma de código abierto para desarrollar aplicaciones con LLM. El complemento oficial de Firecrawl permite rastrear y extraer datos de la web directamente en tus flujos de trabajo de IA.

## Primeros pasos

## Patrones de uso

- Chatflow Apps
- Workflow Apps
- Agent Apps

**Integración visual de pipelines**

1. Agrega el nodo de Firecrawl a tu pipeline
2. Selecciona la acción (Map, Crawl, Scrape)
3. Define las variables de entrada
4. Ejecuta el pipeline secuencialmente

**Flujo de ejemplo:**

```
Entrada del usuario → Firecrawl (Scrape) → Procesamiento con LLM → Respuesta
```

**Procesamiento de datos automatizado**Crea flujos de trabajo de varios pasos con:

- Scraping programado
- Transformación de datos
- Almacenamiento en base de datos
- Notificaciones

**Flujo de ejemplo:**

```
Disparador programado → Firecrawl (Crawl) → Procesamiento de datos → Almacenamiento
```

**Acceso web con IA**Da a los agentes capacidades de web scraping en tiempo real:

1. Agrega la herramienta de Firecrawl al agente
2. El agente decide de forma autónoma cuándo hacer scraping
3. El LLM analiza el contenido extraído
4. El agente ofrece respuestas fundamentadas

**Caso de uso:** Agentes de soporte al cliente que consultan documentación actualizada

## Casos de uso comunes

## Acciones de Firecrawl

HerramientaDescripciónIdeal para**Scrape**Extracción de datos de una sola páginaCaptura rápida de contenido**Crawl**Rastreo recursivo de múltiples páginasExtracción completa del sitio**Map**Descubrimiento de URL y mapeo del sitioAnálisis SEO, listas de URL**Crawl Job**Gestión de trabajos asíncronosOperaciones de larga duración

## Mejores prácticas

## Dify vs Otras Plataformas

FunciónDifyMakeZapiern8n**Tipo**Plataforma de apps LLMAutomatización de flujos de trabajoAutomatización de flujos de trabajoAutomatización de flujos de trabajo**Ideal para**Agentes de IA y chatbotsFlujos de trabajo visualesAutomatizaciones rápidasControl para desarrolladores**Precios**Código abierto + nubeBasado en operacionesPor tareaMensual fijo**Nativa de IA**SíParcialParcialParcial**Autogestionada**SíNoNoSí