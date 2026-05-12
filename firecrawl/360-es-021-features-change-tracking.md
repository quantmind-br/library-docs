---
title: Change Tracking | Firecrawl
url: https://docs.firecrawl.dev/es/features/change-tracking
source: sitemap
fetched_at: 2026-03-23T07:25:28.498931-03:00
rendered_js: false
word_count: 1065
summary: This document explains how to use the change tracking feature in Firecrawl to detect, monitor, and report modifications in website content compared to previous scrapes.
tags:
    - change-tracking
    - web-scraping
    - diff-analysis
    - data-monitoring
    - automation
    - api-reference
category: guide
---

![Seguimiento de cambios](https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=cc56c24d15e1b2ed4806ddb66d0f5c3f) El seguimiento de cambios compara el contenido actual de una página con el de la última vez que la extrajiste con scraping. Añade `changeTracking` a tu array de `formats` para detectar si una página es nueva, no ha cambiado o se ha modificado y, opcionalmente, obtener un diff estructurado de lo que cambió.

- Funciona con `/scrape`, `/crawl` y `/batch/scrape`
- Dos modos de diff: `git-diff` para cambios a nivel de línea y `json` para comparación a nivel de campo
- Acotado a tu equipo y, opcionalmente, a una etiqueta que especifiques

## Cómo funciona

Cada extracción con `changeTracking` habilitado almacena una captura y la compara con la captura anterior para esa URL. Las capturas se almacenan de forma persistente y no caducan, por lo que las comparaciones se mantienen precisas sin importar cuánto tiempo haya pasado entre extracciones.

ExtracciónResultadoPrimera vez`changeStatus: "new"` (no existe una versión anterior)Contenido sin cambios`changeStatus: "same"`Contenido modificado`changeStatus: "changed"` (datos de diff disponibles)Página eliminada`changeStatus: "removed"`

La respuesta incluye estos campos en el objeto `changeTracking`:

CampoTipoDescripción`previousScrapeAt``string | null`Marca de tiempo de la extracción anterior (`null` en la primera extracción)`changeStatus``string``"new"`, `"same"`, `"changed"` o `"removed"``visibility``string``"visible"` (detectable a través de enlaces/sitemap) o `"hidden"` (la URL funciona pero ya no está enlazada)`diff``object | undefined`Diff a nivel de línea (solo presente en modo `git-diff` cuando el estado es `"changed"`)`json``object | undefined`Comparación a nivel de campo (solo presente en modo `json` cuando el estado es `"changed"`)

## Uso básico

Incluye tanto `markdown` como `changeTracking` en el array `formats`. El formato `markdown` es obligatorio porque el seguimiento de cambios compara las páginas según su contenido en markdown.

### Respuesta

En el primer scraping, `changeStatus` es `"new"` y `previousScrapeAt` es `null`:

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $9/mo\nPro: $29/mo...",
    "changeTracking": {
      "previousScrapeAt": null,
      "changeStatus": "new",
      "visibility": "visible"
    }
  }
}
```

En scrapes posteriores, `changeStatus` indica si el contenido ha cambiado:

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $12/mo\nPro: $39/mo...",
    "changeTracking": {
      "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible"
    }
  }
}
```

## Modo git-diff

El modo `git-diff` retorna cambios línea por línea en un formato similar a `git diff`. Pasa un objeto dentro del array `formats` con `modes: ["git-diff"]`:

### Respuesta

El objeto `diff` contiene tanto un diff en texto plano como una representación JSON estructurada:

```
{
  "changeTracking": {
    "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "diff": {
      "text": "@@ -1,3 +1,3 @@\n # Pricing\n-Starter: $9/mo\n-Pro: $29/mo\n+Starter: $12/mo\n+Pro: $39/mo",
      "json": {
        "files": [{
          "chunks": [{
            "content": "@@ -1,3 +1,3 @@",
            "changes": [
              { "type": "normal", "content": "# Pricing" },
              { "type": "del", "ln": 2, "content": "Starter: $9/mo" },
              { "type": "del", "ln": 3, "content": "Pro: $29/mo" },
              { "type": "add", "ln": 2, "content": "Starter: $12/mo" },
              { "type": "add", "ln": 3, "content": "Pro: $39/mo" }
            ]
          }]
        }]
      }
    }
  }
}
```

El objeto estructurado `diff.json` contiene:

- `files`: matriz de archivos modificados (generalmente uno por página web)
- `chunks`: secciones de cambios dentro de un archivo
- `changes`: cambios de líneas individuales con `type` (`"add"`, `"del"` o `"normal"`), número de línea (`ln`) y `content`

## modo JSON

El modo `json` extrae campos específicos tanto de la versión actual como de la versión anterior de la página usando un esquema que defines. Esto es útil para hacer un seguimiento de cambios en datos estructurados como precios, niveles de stock o metadatos sin tener que analizar un diff completo. Pasa `modes: ["json"]` con un `schema` que defina los campos a extraer:

### Respuesta

Cada campo del esquema se devuelve con valores `previous` y `current`:

```
{
  "changeTracking": {
    "previousScrapeAt": "2025-06-05T08:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "json": {
      "price": {
        "previous": "$19.99",
        "current": "$24.99"
      },
      "availability": {
        "previous": "In Stock",
        "current": "In Stock"
      }
    }
  }
}
```

También puedes proporcionar un `prompt` opcional para guiar la extracción mediante el LLM junto con el esquema.

De forma predeterminada, el seguimiento de cambios se compara con el scrape más reciente de la misma URL realizado por tu equipo. Las etiquetas te permiten mantener **historiales de seguimiento independientes** para la misma URL, lo cual es útil cuando supervisas la misma página en diferentes intervalos o en distintos contextos.

## Rastreo con seguimiento de cambios

Añade seguimiento de cambios a las operaciones de rastreo para supervisar un sitio completo en busca de cambios. Pasa el formato `changeTracking` dentro de `scrapeOptions`:

Usa [batch scrape](https://docs.firecrawl.dev/es/features/batch-scrape) para supervisar un conjunto específico de URL:

## Programar el seguimiento de cambios

El seguimiento de cambios es más útil cuando haces scraping a intervalos regulares. Puedes automatizarlo con cron, planificadores en la nube o herramientas de orquestación de flujos de trabajo.

### Tarea cron

Crea un script que haga scraping de una URL y notifique cuando haya cambios:

```
#!/bin/bash
RESPONSE=$(curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://competitor.com/pricing",
    "formats": [
      "markdown",
      {
        "type": "changeTracking",
        "modes": ["json"],
        "schema": {
          "type": "object",
          "properties": {
            "starter_price": { "type": "string" },
            "pro_price": { "type": "string" }
          }
        }
      }
    ]
  }')

STATUS=$(echo "$RESPONSE" | jq -r '.data.changeTracking.changeStatus')

if [ "$STATUS" = "changed" ]; then
  echo "$RESPONSE" | jq '.data.changeTracking.json'
  # Envía alerta por correo electrónico, Slack, etc.
fi
```

Programa la tarea con `crontab -e`:

```
0 */6 * * * /path/to/check-pricing.sh >> /var/log/price-monitor.log 2>&1
```

ProgramaciónExpresiónCada hora`0 * * * *`Cada 6 horas`0 */6 * * *`Todos los días a las 09:00`0 9 * * *`Todos los lunes a las 08:00`0 8 * * 1`

### Planificadores en la nube y sin servidor

- **AWS**: regla de EventBridge que invoca una función Lambda
- **GCP**: Cloud Scheduler que invoca una Cloud Function
- **Vercel / Netlify**: funciones serverless activadas mediante cron
- **GitHub Actions**: flujos de trabajo programados con los desencadenadores `schedule` y `cron`

### Automatización de flujos de trabajo

Plataformas sin código como **n8n**, **Zapier** y **Make** pueden llamar periódicamente a la API de Firecrawl y enrutar los resultados a Slack, correo electrónico o bases de datos. Consulta las [guías sobre automatización de flujos de trabajo](https://docs.firecrawl.dev/es/developer-guides/workflow-automation/n8n).

## Webhooks

Para operaciones asíncronas como `crawl` y *batch scrape*, usa [webhooks](https://docs.firecrawl.dev/es/webhooks/overview) para recibir resultados de seguimientoDeCambios a medida que llegan en lugar de hacer *polling*.

El payload del evento `crawl.page` incluye el objeto `changeTracking` para cada página:

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [{
    "markdown": "# Pricing\n\nStarter: $12/mo...",
    "metadata": {
      "title": "Pricing",
      "url": "https://example.com/pricing",
      "statusCode": 200
    },
    "changeTracking": {
      "previousScrapeAt": "2025-06-05T12:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible",
      "diff": {
        "text": "@@ -2,1 +2,1 @@\n-Starter: $9/mo\n+Starter: $12/mo"
      }
    }
  }]
}
```

Para más detalles sobre la configuración de webhooks (encabezados, metadatos, eventos, reintentos, verificación de firma), consulta la [documentación de webhooks](https://docs.firecrawl.dev/es/webhooks/overview).

## Referencia de configuración

El conjunto completo de opciones disponibles al pasar un objeto de formato `seguimientoDeCambios`:

ParameterTypeDefaultDescription`type``string`(required)Debe ser `"changeTracking"``modes``string[]``[]`Modos de diff a habilitar: `"git-diff"`, `"json"` o ambos`schema``object`(none)JSON Schema para la comparación a nivel de campo (requerido para el modo `json`)`prompt``string`(none)Prompt personalizado para guiar la extracción del LLM (usado con el modo `json`)`tag``string``null`Identificador independiente para el historial de seguimiento

### Modelos de datos

## Detalles importantes

- **Retención de snapshots**: Los snapshots se almacenan de forma persistente y no caducan. Una extracción realizada meses después de la anterior seguirá comparándose correctamente con el snapshot anterior.
- **Alcance**: Las comparaciones se limitan a tu equipo. La primera extracción de cualquier URL devuelve `"new"`, incluso si otros usuarios ya la han extraído.
- **Coincidencia de URL**: Las extracciones anteriores se asocian por la URL de origen exacta, el ID de equipo, el formato `markdown` y la `tag`. Mantén las URLs consistentes entre extracciones.
- **Consistencia de parámetros**: Usar configuraciones diferentes de `includeTags`, `excludeTags` u `onlyMainContent` en extracciones de la misma URL produce comparaciones poco fiables.
- **Algoritmo de comparación**: El algoritmo es resistente a cambios en espacios en blanco y en el orden del contenido. Se ignoran las URLs de origen de iframes para manejar la aleatorización de captcha/antibot.
- **Caché**: Las solicitudes con `changeTracking` omiten la caché del índice. Se ignora el parámetro `maxAge`.
- **Manejo de errores**: Supervisa el campo `warning` en las respuestas y contempla el caso en que el objeto `changeTracking` pueda estar ausente (esto puede ocurrir si la consulta a la base de datos para la extracción previa excede el tiempo de espera).

## Facturación

ModoCostoSeguimiento básico de cambiosSin costo adicional (créditos de scraping estándar)Modo `git-diff`Sin costo adicionalModo `json`5 créditos por página

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de onboarding automatizado.