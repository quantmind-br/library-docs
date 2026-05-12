---
title: Search - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:16:14.424464-03:00
rendered_js: false
word_count: 374
summary: This document describes the /search endpoint functionality, which enables web searching combined with automated scraping, including support for search operators, geolocation filtering, and time-based parameters.
tags:
    - api-reference
    - web-scraping
    - search-engine
    - data-extraction
    - geo-targeting
    - url-parsing
category: api
---

Buscar y, opcionalmente, hacer scraping de los resultados de búsqueda

> Nota: Ya está disponible una [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/search) con funciones y rendimiento mejorados.

El punto de conexión /search combina la búsqueda web con las capacidades de scraping de Firecrawl para devolver el contenido completo de la página para cualquier consulta. Incluye `scrapeOptions` con `formats: ["markdown"]` para obtener el contenido completo en Markdown de cada resultado de búsqueda; de lo contrario, de forma predeterminada recibirás los resultados (url, title, description).

## Operadores de consulta compatibles

Ofrecemos una variedad de operadores de consulta que te permiten filtrar mejor tus búsquedas.

OperadorFuncionalidadEjemplos`""`Hace una coincidencia exacta de una cadena de texto`"Firecrawl"``-`Excluye ciertas palabras clave o niega otros operadores`-bad`, `-site:firecrawl.dev``site:`Devuelve solo resultados de un sitio web específico`site:firecrawl.dev``inurl:`Devuelve solo resultados que incluyan una palabra en la URL`inurl:firecrawl``allinurl:`Devuelve solo resultados que incluyan varias palabras en la URL`allinurl:git firecrawl``intitle:`Devuelve solo resultados que incluyan una palabra en el título de la página`intitle:Firecrawl``allintitle:`Devuelve solo resultados que incluyan varias palabras en el título de la página`allintitle:firecrawl playground``related:`Devuelve solo resultados relacionados con un dominio específico`related:firecrawl.dev`

## Parámetro de ubicación

Usa el parámetro `location` para obtener resultados de búsqueda con orientación geográfica. Formato: `"string"`. Ejemplos: `"Germany"`, `"San Francisco,California,United States"`. Consulta la [lista completa de ubicaciones admitidas](https://firecrawl.dev/search_locations.json) para ver todos los países e idiomas disponibles.

## Búsqueda por tiempo

Usa el parámetro `tbs` para filtrar los resultados por periodos de tiempo, incluidos los rangos de fechas personalizados. Consulta la [documentación de la función de búsqueda](https://docs.firecrawl.dev/features/search#time-based-search) para ver ejemplos detallados y los formatos compatibles.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Cuerpo

Número máximo de resultados que se devolverán

Rango requerido: `1 <= x <= 100`

Parámetro de búsqueda temporal. Admite intervalos de tiempo predefinidos (`qdr:h`, `qdr:d`, `qdr:w`, `qdr:m`, `qdr:y`) y rangos de fechas personalizados (`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`).

Parámetro de ubicación para los resultados de búsqueda

timeout

integer

predeterminado:60000

Tiempo de espera en milisegundos

ignoreInvalidURLs

boolean

predeterminado:false

Excluye de los resultados de búsqueda las URLs que no son válidas para otros endpoints de Firecrawl. Esto ayuda a reducir errores si canalizas datos de la búsqueda hacia otros endpoints de la API de Firecrawl.

Opciones para extraer resultados de búsqueda

#### Respuesta

Mensaje de advertencia si ocurre algún problema

El ID de la tarea de búsqueda