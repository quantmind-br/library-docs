---
title: Introducción - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v2-introduction
source: sitemap
fetched_at: 2026-03-23T07:32:01.623662-03:00
rendered_js: false
word_count: 250
summary: This document provides the foundational technical specifications for the Firecrawl API, covering authentication, base URL configuration, status codes, and rate limiting policies.
tags:
    - api-documentation
    - authentication
    - rate-limiting
    - http-status-codes
    - firecrawl-api
category: reference
---

La API de Firecrawl proporciona acceso programático a datos de la web. Todos los endpoints comparten la misma URL base, el mismo esquema de autenticación y el formato de respuesta descritos en esta página.

## Funcionalidades

## Capacidades de agente

## URL base

Todas las solicitudes utilizan la siguiente URL base:

```
https://api.firecrawl.dev
```

## Autenticación

Todas las solicitudes deben incluir un encabezado `Authorization` con tu clave de API:

```
Authorization: Bearer fc-YOUR-API-KEY
```

Incluye este encabezado en todas las llamadas a la API. Puedes encontrar tu clave de API en el [dashboard de Firecrawl](https://www.firecrawl.dev/app/api-keys).

## Códigos de respuesta

Firecrawl utiliza códigos de estado HTTP convencionales para indicar el resultado de tus solicitudes. Los códigos en el rango `2xx` indican éxito, los códigos `4xx` indican errores del cliente y los códigos `5xx` indican errores del servidor.

StatusDescription`200`La solicitud se realizó correctamente.`400`Parámetros de la solicitud no válidos.`401`Falta la clave de la API o no es válida.`402`Pago requerido.`404`No se encontró el recurso solicitado.`429`Se superó el límite de solicitudes.`5xx`Error del servidor en el lado de Firecrawl.

Cuando se produce un error `5xx`, el cuerpo de la respuesta incluye un código de error específico para ayudarte a diagnosticar el problema.

## Límite de solicitudes

La API de Firecrawl aplica límites de solicitudes (rate limits) en todos los endpoints para garantizar la estabilidad del servicio. Estos límites se basan en el número de solicitudes dentro de una ventana de tiempo determinada. Si superas el límite de solicitudes, la API devuelve un código de estado `429`. Espera un momento y vuelve a intentar la solicitud después de un breve retraso.