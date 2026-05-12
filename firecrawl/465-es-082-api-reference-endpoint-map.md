---
title: Mapear - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:17:16.31761-03:00
rendered_js: false
word_count: 264
summary: This document provides the API specifications and configuration parameters for mapping multiple URLs and managing web crawling behavior.
tags:
    - api-reference
    - url-mapping
    - web-crawling
    - sitemap-configuration
    - request-parameters
category: api
---

[Saltar al contenido principal](#content-area)

Mapear varias URL en función de las opciones

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Cuerpo

La URL base desde la que comenzar el rastreo

Especifica una consulta de búsqueda para ordenar los resultados según su relevancia. Ejemplo: "blog" devolverá las URL que contengan la palabra "blog" en la URL, ordenadas por relevancia.

sitemap

enum&lt;string&gt;

predeterminado:include

Modo de uso del sitemap al mapear. Si lo configuras en `skip`, el sitemap no se usará para encontrar URL. Si lo configuras en `only`, solo se devolverán las URL que estén en el sitemap. De forma predeterminada (`include`), el sitemap y otros métodos se usarán conjuntamente para encontrar URL.

Opciones disponibles:

`skip`,

`include`,

`only`

includeSubdomains

boolean

predeterminado:true

Incluir subdominios del sitio web

ignoreQueryParameters

boolean

predeterminado:true

No devuelvas direcciones URL con parámetros de consulta

ignoreCache

boolean

predeterminado:false

Omitir la caché del sitemap para obtener URLs actualizadas. Los datos del sitemap se almacenan en caché hasta 7 días; usa este parámetro cuando tu sitemap se haya actualizado recientemente.

limit

integer

predeterminado:5000

Número máximo de enlaces que se devolverán

Rango requerido: `x <= 100000`

Tiempo de espera en milisegundos. De forma predeterminada, no hay tiempo de espera.

Configuración de ubicación de la solicitud. Cuando se especifica, se utilizará un proxy adecuado si está disponible y se emularán la configuración de idioma y la zona horaria correspondientes. De manera predeterminada se usa 'US' si no se especifica.

#### Respuesta