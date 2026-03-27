---
title: Agente de IA FIRE-1 (Beta) | Firecrawl
url: https://docs.firecrawl.dev/es/agents/fire-1
source: sitemap
fetched_at: 2026-03-23T07:36:47.659542-03:00
rendered_js: false
word_count: 166
summary: This document introduces FIRE-1, an AI-powered agent designed for advanced web scraping and navigation within the Firecrawl platform, and outlines its functional capabilities, pricing model, and usage limitations.
tags:
    - fire-1
    - ai-agent
    - web-scraping
    - data-extraction
    - browser-automation
    - firecrawl
category: concept
---

FIRE-1 es un agente de IA que potencia las capacidades de scraping de Firecrawl. Puede controlar acciones del navegador y navegar por estructuras web complejas para permitir una extracción de datos más completa, más allá de los métodos tradicionales de scraping.

### Qué puede hacer FIRE-1:

- Planificar y ejecutar acciones para descubrir datos
- Interactuar con botones, enlaces, campos de entrada y elementos dinámicos.
- Obtener datos de múltiples páginas que requieren paginación, varios pasos, etc.

## Cómo usar FIRE-1

Puedes usar el agente FIRE-1 con el endpoint `/v1/extract` para tareas de extracción complejas que requieren navegar por múltiples páginas o interactuar con elementos. **Ejemplo:**

## Facturación

El costo de usar FIRE-1 es no determinista. Consulta nuestra [calculadora de créditos](https://www.firecrawl.dev/extract-calculator) para conocer el costo base de cada solicitud de Extract. **¿Por qué FIRE-1 es más costoso?**  
FIRE-1 utiliza automatización avanzada del navegador y planificación con IA para interactuar con páginas web complejas, lo que requiere más recursos de computación que la extracción estándar.

## Límites de tasa

- `/extract`: 10 solicitudes por minuto