---
title: Rastrear | Firecrawl
url: https://docs.firecrawl.dev/es/features/crawl
source: sitemap
fetched_at: 2026-03-23T07:25:43.987152-03:00
rendered_js: false
word_count: 1085
summary: This document explains how to use the Firecrawl crawl API to recursively discover, scrape, and extract structured data from web pages, including configuration options, SDK methods, and webhook integration.
tags:
    - web-scraping
    - api-documentation
    - recursive-crawling
    - data-extraction
    - firecrawl
    - webhooks
    - data-processing
category: api
---

Rastrear envía una URL a Firecrawl y descubre y extrae de forma recursiva todas las subpáginas accesibles. Gestiona automáticamente sitemaps, renderizado de JavaScript y límites de tasa, y devuelve Markdown limpio o datos estructurados para cada página.

- Descubre páginas mediante sitemap y recorrido recursivo de enlaces
- Admite filtrado por ruta, límites de profundidad y control de subdominios/enlaces externos
- Devuelve resultados mediante polling, WebSocket o webhook

## Instalación

## Uso básico

Envía un trabajo de rastreo llamando a `POST /v2/crawl` con una URL inicial. El endpoint devuelve un ID de trabajo que usas para consultar los resultados.

### Opciones de scraping

Todas las opciones del [endpoint Scrape](https://docs.firecrawl.dev/es/api-reference/endpoint/scrape) están disponibles en crawl mediante `scrapeOptions` (JS) / `scrape_options` (Python). Se aplican a cada página que el crawler raspa, incluidos formatos, proxy, caché, acciones, ubicación y etiquetas.

## Verificar el estado del rastreo

Usa el ID del trabajo para consultar el estado del rastreo y recuperar los resultados.

### Manejo de respuestas

La respuesta varía según el estado del rastreo. Para respuestas incompletas o de gran tamaño que superen los 10 MB, se proporciona un parámetro de URL `next`. Debes solicitar esta URL para obtener los siguientes 10 MB de datos. Si el parámetro `next` no está presente, indica el final de los datos del rastreo.

## Métodos del SDK

Hay dos maneras de usar `crawl` con el SDK.

### Rastrear y esperar

El método `crawl` espera a que el rastreo termine y devuelve la respuesta completa. Gestiona la paginación automáticamente. Esto se recomienda para la mayoría de los casos de uso.

La respuesta incluye el estado del rastreo y todos los datos extraídos:

### Iniciar y luego verificar el estado

El método `startCrawl` / `start_crawl` devuelve de inmediato un ID de rastreo. Luego puedes verificar el estado manualmente. Esto es útil para rastreos de larga duración o lógica de sondeo personalizada.

La respuesta inicial devuelve el ID del trabajo:

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

## Resultados en tiempo real con WebSocket

El método watcher proporciona actualizaciones en tiempo real a medida que se rastrean las páginas. Inicia un rastreo y luego suscríbete a los eventos para procesar los datos de inmediato.

## Webhooks

Puedes configurar webhooks para recibir notificaciones en tiempo real a medida que avanza el rastreo. Esto te permite procesar las páginas conforme se van extrayendo, en lugar de esperar a que finalice todo el rastreo.

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://tu-dominio.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### Tipos de eventos

EventoDescripción`crawl.started`Se emite cuando comienza el rastreo`crawl.page`Se emite por cada página extraída correctamente`crawl.completed`Se emite cuando finaliza el rastreo`crawl.failed`Se emite si el rastreo encuentra un error

### Carga útil

```
{
  "success": true,
  "type": "crawl.page",
  "id": "crawl-job-id",
  "data": [...], // Datos de página para eventos 'page'
  "metadata": {}, // Your custom metadata
  "error": null
}
```

### Verificación de firmas de webhooks

Cada solicitud de webhook de Firecrawl incluye un encabezado `X-Firecrawl-Signature` que contiene una firma HMAC-SHA256. Verifica siempre esta firma para asegurarte de que el webhook sea auténtico y no haya sido manipulado.

1. Obtén tu secreto de webhook en la [pestaña Advanced](https://www.firecrawl.dev/app/settings?tab=advanced) de la configuración de tu cuenta
2. Extrae la firma del encabezado `X-Firecrawl-Signature`
3. Calcula el HMAC-SHA256 del cuerpo sin procesar (raw) de la solicitud usando tu secreto
4. Compárala con el encabezado de la firma usando una función segura frente a ataques de temporización

Para ver ejemplos completos de implementación en JavaScript y Python, consulta la [documentación de seguridad de webhooks](https://docs.firecrawl.dev/es/webhooks/security). Para consultar la documentación completa sobre webhooks, incluidos payloads de eventos detallados, estructura de payloads, configuración avanzada y solución de problemas, consulta la [documentación de webhooks](https://docs.firecrawl.dev/es/webhooks/overview).

## Referencia de configuración

El conjunto completo de parámetros disponibles al enviar una tarea de rastreo:

ParámetroTipoPredeterminadoDescripción`url``string`(obligatorio)La URL inicial desde la que se realizará el rastreo`limit``integer``10000`Número máximo de páginas que se rastrearán`maxDiscoveryDepth``integer`(ninguno)Profundidad máxima desde la URL raíz según los saltos de descubrimiento de enlaces, no la cantidad de segmentos `/` en la URL. Cada vez que se encuentra una nueva URL en una página, se le asigna una profundidad una unidad mayor que la de la página en la que fue descubierta. El sitio raíz y las páginas del sitemap tienen una profundidad de descubrimiento de 0. Las páginas en la profundidad máxima igualmente se extraen, pero no se siguen los enlaces que contienen.`includePaths``string[]`(ninguno)Patrones regex de rutas de URL que se incluirán. Solo se rastrean las rutas que coinciden.`excludePaths``string[]`(ninguno)Patrones regex de rutas de URL que se excluirán del rastreo`regexOnFullURL``boolean``false`Hace coincidir `includePaths`/`excludePaths` con la URL completa (incluidos los parámetros de consulta) en lugar de solo con la ruta`crawlEntireDomain``boolean``false`Sigue enlaces internos a URL del mismo nivel o superiores, no solo a rutas hijas`allowSubdomains``boolean``false`Sigue enlaces a subdominios del dominio principal`allowExternalLinks``boolean``false`Sigue enlaces a sitios web externos`sitemap``string``"include"`Gestión del sitemap: `"include"` (predeterminado), `"skip"` o `"only"``ignoreQueryParameters``boolean``false`Evita volver a extraer la misma ruta con distintos parámetros de consulta`delay``number`(ninguno)Retraso en segundos entre extracciones para respetar los límites de tasa`maxConcurrency``integer`(ninguno)Número máximo de extracciones concurrentes. De forma predeterminada, usa el límite de concurrencia de tu equipo.`scrapeOptions``object`(ninguno)Opciones aplicadas a cada página extraída (formatos, proxy, caché, acciones, etc.)`webhook``object`(ninguno)Configuración del webhook para notificaciones en tiempo real`prompt``string`(ninguno)Prompt en lenguaje natural para generar opciones de rastreo. Los parámetros establecidos explícitamente anulan los equivalentes generados.

## Detalles importantes

- **Descubrimiento del sitemap**: De forma predeterminada, el crawler incluye el sitemap del sitio web para descubrir URL (`sitemap: "include"`). Si estableces `sitemap: "skip"`, solo se encontrarán las páginas accesibles mediante enlaces HTML desde la URL raíz. Recursos como PDF o páginas muy anidadas incluidas en el sitemap, pero no enlazadas directamente desde el HTML, no se encontrarán. Para obtener la máxima cobertura, mantén la configuración predeterminada.
- **Uso de créditos**: Cada página rastreada cuesta 1 crédito. El modo JSON añade 4 créditos por página, el proxy mejorado añade 4 créditos por página y el análisis de PDF cuesta 1 crédito por cada página del PDF.
- **Expiración de resultados**: Los resultados del trabajo están disponibles a través de la API durante 24 horas después de completarse. Después de ese plazo, consulta los resultados en los [registros de actividad](https://www.firecrawl.dev/app/logs).
- **Errores de crawl**: El array `data` contiene las páginas que Firecrawl extrajo correctamente. Usa el endpoint [Get Crawl Errors](https://docs.firecrawl.dev/es/api-reference/endpoint/crawl-get-errors) para recuperar las páginas que fallaron debido a errores de red, tiempos de espera o bloqueos de robots.txt.
- **Resultados no deterministas**: Los resultados de crawl pueden variar entre ejecuciones con la misma configuración. Las páginas se extraen de forma concurrente, por lo que el orden en que se descubren los enlaces depende de la latencia de la red y de qué páginas terminan de cargarse primero. Esto significa que diferentes ramas de un sitio pueden explorarse en distinta medida cerca del límite de profundidad, especialmente con valores altos de `maxDiscoveryDepth`. Para obtener resultados más deterministas, establece `maxConcurrency` en `1` o usa `sitemap: "only"` si el sitio tiene un sitemap completo.

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.