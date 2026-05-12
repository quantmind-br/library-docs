---
title: Mapa - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:16:22.172541-03:00
rendered_js: false
word_count: 189
summary: This document provides the API reference documentation for the map endpoint, detailing the request parameters and authentication requirements for crawling and mapping website URLs.
tags:
    - api-reference
    - web-crawling
    - url-mapping
    - endpoint-configuration
    - data-extraction
category: api
---

[Saltar al contenido principal](#content-area)

Mapear varias URL en función de las opciones

> Nota: Ya está disponible una nueva [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/map) con funciones y rendimiento mejorados.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Cuerpo

La URL base desde la que se iniciará el rastreo

Consulta de búsqueda que se utilizará para el mapeo. Durante la fase alfa, la parte «inteligente» de la funcionalidad de búsqueda está limitada a 500 resultados. Sin embargo, si map encuentra más resultados, no se impone ningún límite.

ignoreSitemap

boolean

predeterminado:true

Ignorar el mapa del sitio web al rastrear.

sitemapOnly

boolean

predeterminado:false

Devuelve únicamente los enlaces encontrados en el mapa del sitio web

includeSubdomains

boolean

predeterminado:true

Incluir subdominios del sitio web

limit

integer

predeterminado:5000

Número máximo de enlaces que se devolverán

Rango requerido: `x <= 30000`

Tiempo de espera en milisegundos. No hay tiempo de espera por defecto.

Configuración de ubicación de la solicitud. Si se especifica, usará un proxy adecuado si está disponible y emulará la configuración de idioma y zona horaria correspondientes. De forma predeterminada, se usa 'US' si no se especifica.

#### Respuesta