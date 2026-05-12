---
title: Modelos de agente | Firecrawl
url: https://docs.firecrawl.dev/es/features/models
source: sitemap
fetched_at: 2026-03-23T07:25:18.64122-03:00
rendered_js: false
word_count: 345
summary: This document outlines the differences between Firecrawl Agent's two models, Spark 1 Mini and Spark 1 Pro, to help users select the appropriate model based on task complexity, cost, and accuracy requirements.
tags:
    - firecrawl-agent
    - data-extraction
    - ai-models
    - cost-optimization
    - model-selection
    - spark-1-mini
    - spark-1-pro
category: guide
---

Firecrawl Agent ofrece dos modelos optimizados para distintos casos de uso. Elige el modelo adecuado en función de la complejidad de la extracción y tus requisitos de costos.

## Modelos disponibles

ModelCostAccuracyBest For`spark-1-mini`**60% más económico**EstándarLa mayoría de las tareas (predeterminado)`spark-1-pro`EstándarMás altaInvestigación compleja, extracción crítica

## Spark 1 Mini (por defecto)

`spark-1-mini` es nuestro modelo eficiente, ideal para tareas sencillas de extracción de datos. **Usa Mini cuando:**

- Necesites extraer datos simples (información de contacto, precios, etc.)
- Trabajes con sitios web bien estructurados
- El ahorro de costos sea una prioridad
- Debas ejecutar trabajos de extracción de alto volumen

**Ejemplos de casos de uso:**

- Extraer precios de productos de sitios de comercio electrónico
- Recopilar información de contacto de páginas de empresas
- Extraer metadatos básicos de artículos
- Realizar consultas sencillas de datos específicos

## Spark 1 Pro

`spark-1-pro` es nuestro modelo insignia, diseñado para lograr la máxima precisión en tareas de extracción complejas. **Usa Pro cuando:**

- Realices análisis de la competencia complejos
- Extraigas datos que requieran razonamiento profundo
- La precisión sea crítica para tu caso de uso
- Tengas que manejar datos ambiguos o difíciles de encontrar

**Ejemplos de casos de uso:**

- Análisis de la competencia en múltiples dominios
- Tareas de investigación complejas que requieran razonamiento
- Extracción de información detallada y matizada desde múltiples fuentes
- Obtención de inteligencia empresarial crítica

## Especificar un modelo

Pasa el parámetro `model` para seleccionar el modelo que quieras usar:

## Comparación de modelos

CaracterísticaSpark 1 MiniSpark 1 Pro**Costo**60% más baratoEstándar**Precisión**EstándarMás alta**Velocidad**RápidaRápida**Mejor para**La mayoría de las tareasTareas complejas**Razonamiento**EstándarAvanzado**Multidominio**BuenoExcelente

## Precios por modelo

Ambos modelos usan precios dinámicos basados en créditos que se adaptan a la complejidad de la tarea:

- **Spark 1 Mini**: Usa aproximadamente un 60 % menos de créditos que Pro para tareas equivalentes
- **Spark 1 Pro**: Consumo estándar de créditos para máxima precisión

## Seleccionar el modelo adecuado

```
                    ┌─────────────────────────────────┐
                    │   What type of task?            │
                    └─────────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  Simple/Directa │           │ Compleja/Investigación│
          │  extracción     │           │ multidominio    │
          └─────────────────┘           └─────────────────┘
                    │                             │
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  spark-1-mini   │           │  spark-1-pro    │
          │  (60% cheaper)  │           │  (higher acc.)  │
          └─────────────────┘           └─────────────────┘
```

## Referencia de la API

Consulta la [Referencia de la API del agente](https://docs.firecrawl.dev/es/api-reference/endpoint/agent) para obtener la documentación completa de los parámetros. ¿Tienes preguntas sobre qué modelo usar? Envía un correo a [help@firecrawl.com](mailto:help@firecrawl.com).

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizadas.