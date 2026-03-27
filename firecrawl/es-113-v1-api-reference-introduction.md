---
title: Introducción - Firecrawl Docs
url: https://docs.firecrawl.dev/es/v1/api-reference/introduction
source: sitemap
fetched_at: 2026-03-23T07:39:02.873056-03:00
rendered_js: false
word_count: 196
summary: This document provides the foundational technical specifications for the Firecrawl API, including authentication protocols, response codes, and rate limiting policies.
tags:
    - api-documentation
    - authentication
    - http-status-codes
    - rate-limiting
    - api-integration
category: reference
---

## Funciones

## Funciones de agentes

## URL base

Todas las solicitudes usan la siguiente URL base:

```
https://api.firecrawl.dev
```

## Autenticación

Para autenticarse, debes incluir un encabezado Authorization. Este encabezado debe contener `Bearer fc-123456789`, donde `fc-123456789` es tu clave de API.

```
Authorization: Bearer fc-123456789
```

​

## Códigos de respuesta

Firecrawl utiliza códigos de estado HTTP convencionales para indicar el resultado de tus solicitudes. Por lo general, los códigos de estado HTTP 2xx indican éxito, los códigos 4xx representan errores relacionados con el usuario y los códigos 5xx señalan problemas de infraestructura.

StatusDescription200La solicitud se completó correctamente.400Verifica que los parámetros sean correctos.401No se proporcionó la clave de API.402Se requiere pago404No se pudo encontrar el recurso solicitado.429Se superó el límite de tasa.5xxIndica un error del servidor de Firecrawl.

Consulta la sección de Códigos de error para una explicación detallada de todos los posibles errores de la API. ​

## Límite de tasa

La API de Firecrawl tiene un límite de tasa para garantizar la estabilidad y la fiabilidad del servicio. El límite de tasa se aplica a todos los puntos de conexión y se basa en la cantidad de solicitudes realizadas en un período de tiempo determinado. Cuando superes el límite de tasa, recibirás un código de respuesta 429.