---
title: Búsqueda - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:17:28.033605-03:00
rendered_js: false
word_count: 715
summary: This document outlines the API endpoint for performing web searches with integrated scraping capabilities, detailing supported query operators, geographic filters, and time-based search parameters.
tags:
    - api-reference
    - web-scraping
    - search-engine
    - query-operators
    - data-extraction
category: api
---

Buscar y, opcionalmente, scrapear los resultados de búsqueda

El endpoint de búsqueda combina la búsqueda web con las capacidades de scraping de Firecrawl para devolver el contenido completo de la página para cualquier consulta. Incluye `scrapeOptions` con `formats: [{"type": "markdown"}]` para obtener el contenido completo en markdown de cada resultado de búsqueda; de lo contrario, por defecto solo obtendrás los resultados (url, title, description). También puedes usar otros formatos como `{"type": "summary"}` para obtener contenido condensado.

## Operadores de consulta admitidos

Admitimos una variedad de operadores de consulta que te permiten filtrar mejor tus búsquedas.

OperadorFuncionalidadEjemplos`""`Coincidencia exacta de una cadena de texto (no difusa)`"Firecrawl"``-`Excluye ciertas palabras clave o niega otros operadores`-bad`, `-site:firecrawl.dev``site:`Devuelve solo resultados de un sitio web específico`site:firecrawl.dev``filetype:`Devuelve solo resultados con una extensión de archivo específica`filetype:pdf`, `-filetype:pdf``inurl:`Devuelve solo resultados que incluyan una palabra en la URL`inurl:firecrawl``allinurl:`Devuelve solo resultados que incluyan varias palabras en la URL`allinurl:git firecrawl``intitle:`Devuelve solo resultados que incluyan una palabra en el título de la página`intitle:Firecrawl``allintitle:`Devuelve solo resultados que incluyan varias palabras en el título de la página`allintitle:firecrawl playground``related:`Devuelve solo resultados relacionados con un dominio específico`related:firecrawl.dev``imagesize:`Devuelve solo imágenes con dimensiones exactas`imagesize:1920x1080``larger:`Devuelve solo imágenes más grandes que las dimensiones especificadas`larger:1920x1080`

## Parámetro de ubicación

Usa el parámetro `location` para obtener resultados de búsqueda geodirigidos. Formato: `"string"`. Ejemplos: `"Germany"`, `"San Francisco,California,United States"`. Consulta la [lista completa de ubicaciones compatibles](https://firecrawl.dev/search_locations.json) para ver todos los países e idiomas disponibles.

## Parámetro country

Usa el parámetro `country` para especificar el país de los resultados de búsqueda usando códigos de país ISO. Valor predeterminado: `"US"`. Ejemplos: `"US"`, `"DE"`, `"FR"`, `"JP"`, `"UK"`, `"CA"`.

```
{
  "query": "restaurantes",
  "country": "DE"
}
```

## Parámetro `categories`

Filtra los resultados de búsqueda por categorías específicas usando el parámetro `categories`:

- **`github`** : Busca en repositorios de GitHub, código, issues y documentación
- **`research`** : Busca en sitios web académicos y de investigación (arXiv, Nature, IEEE, PubMed, etc.)
- **`pdf`** : Busca archivos PDF

### Ejemplo de uso

```
{
  "query": "aprendizaje automático",
  "categories": ["github", "investigación"],
  "limit": 10
}
```

### Respuesta de categoría

Cada resultado incluye un campo `category` que indica su origen:

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/ml-project",
        "title": "Machine Learning Project",
        "description": "Implementation of ML algorithms",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "ML Research Paper",
        "description": "Latest advances in machine learning",
        "category": "research"
      }
    ]
  }
}
```

## Búsqueda por tiempo

Usa el parámetro `tbs` para filtrar los resultados por períodos de tiempo, incluidos rangos de fechas personalizados. Consulta la [documentación de la funcionalidad de búsqueda](https://docs.firecrawl.dev/features/search#time-based-search) para ver ejemplos detallados y formatos compatibles.

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones para la incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Cuerpo

Consulta de búsqueda

Maximum string length: `500`

Número máximo de resultados que se devolverán

Rango requerido: `1 <= x <= 100`

sources

(Web · object | Images · object | News · object)\[]

Fuentes en las que buscar. Determinarán los arrays disponibles en la respuesta. Por defecto es \['web'].

- Web
- Images
- News

categories

(GitHub · object | Research · object | PDF · object)\[]

Categorías por las que filtrar los resultados. De forma predeterminada se establece en \[], lo que significa que los resultados no se filtrarán por ninguna categoría.

- GitHub
- Research
- PDF

Parámetro de búsqueda por tiempo. Admite rangos de tiempo predefinidos (`qdr:h`, `qdr:d`, `qdr:w`, `qdr:m`, `qdr:y`), rangos de fechas personalizados (`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`) y ordenación por fecha (`sbd:1`). Los valores se pueden combinar, p. ej. `sbd:1,qdr:w`.

Parámetro de ubicación para los resultados de la búsqueda (por ejemplo, `San Francisco,California,United States`). Para obtener mejores resultados, configura tanto este parámetro como el parámetro `country`.

Código de país ISO para la segmentación geográfica de los resultados de búsqueda (por ejemplo, `US`). Para obtener mejores resultados, establece tanto este parámetro como el parámetro `location`.

timeout

integer

predeterminado:60000

Tiempo de espera en milisegundos

ignoreInvalidURLs

boolean

predeterminado:false

Excluye de los resultados de búsqueda las URLs que no son válidas para otros endpoints de Firecrawl. Esto ayuda a reducir errores si estás enviando datos desde la búsqueda a otros endpoints de la API de Firecrawl.

Opciones de search para Enterprise con Zero Data Retention (ZDR). Usa `["zdr"]` para ZDR de extremo a extremo (10 credits / 10 resultados) o `["anon"]` para ZDR anonimizado (2 credits / 10 resultados). Debe estar habilitado para tu equipo.

Opciones disponibles:

`anon`,

`zdr`

Opciones para scrapear resultados de búsqueda

#### Respuesta

Los resultados de la búsqueda. Los arrays disponibles dependerán de las fuentes que especifiques en la solicitud. De forma predeterminada, se devolverá el array `web`.

Mensaje de advertencia si ocurre algún problema

El ID de la tarea de búsqueda

El número de créditos consumidos en la búsqueda