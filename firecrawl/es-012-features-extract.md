---
title: Extracción | Firecrawl
url: https://docs.firecrawl.dev/es/features/extract
source: sitemap
fetched_at: 2026-03-23T07:25:40.897116-03:00
rendered_js: false
word_count: 775
summary: This document explains how to use the Firecrawl /extract API endpoint to scrape and structure web data from URLs using natural language prompts or predefined schemas.
tags:
    - api-documentation
    - web-scraping
    - data-extraction
    - structured-data
    - firecrawl
    - web-crawling
    - json-schema
category: api
---

El endpoint `/extract` simplifica la recopilación de datos estructurados desde cualquier número de URL o dominios completos. Proporciona una lista de URL, opcionalmente con comodines (p. ej., `example.com/*`), y un prompt o un esquema que describa la información que deseas. Firecrawl se encarga de los detalles de rastreo, análisis y compilación de conjuntos de datos grandes o pequeños.

Puedes extraer datos estructurados de una o varias URL, incluyendo comodines:

- **Página única**  
  Ejemplo: `https://firecrawl.dev/some-page`
- **Múltiples páginas / Dominio completo**  
  Ejemplo: `https://firecrawl.dev/*`

Cuando usas `/*`, Firecrawl rastreará y analizará automáticamente todas las URL que pueda encontrar en ese dominio y luego extraerá los datos solicitados. Esta función es experimental; envía un correo a [help@firecrawl.com](mailto:help@firecrawl.com) si tienes problemas.

### Ejemplo de uso

**Parámetros clave:**

- **urls**: Una lista de una o más URL. Admite comodines (`/*`) para un rastreo más amplio.
- **prompt** (Opcional salvo que no haya schema): Un prompt en lenguaje natural que describe los datos que quieres o especifica cómo quieres estructurarlos.
- **schema** (Opcional salvo que no haya prompt): Una estructura más rígida si ya conoces el esquema JSON.
- **enableWebSearch** (Opcional): Si es `true`, la extracción puede seguir enlaces fuera del dominio especificado.

Consulta la [Referencia de la API](https://docs.firecrawl.dev/api-reference/endpoint/extract) para más detalles.

### Respuesta (SDKs)

```
{
  "success": true,
  "data": {
    "company_mission": "Firecrawl es la forma más sencilla de extraer datos de la web. Los desarrolladores nos utilizan para convertir de forma confiable URLs en markdown apto para LLM o en datos estructurados con una sola llamada a la API.",
    "supports_sso": false,
    "is_open_source": true,
    "is_in_yc": true
  }
}
```

## Estado del trabajo y finalización

Cuando envías un trabajo de extracción —ya sea directamente mediante la API o a través de los métodos de inicio— recibirás un ID de trabajo. Puedes usar este ID para:

- Obtener el estado del trabajo: Envía una solicitud al punto de conexión /extract/ para ver si el trabajo sigue en ejecución o ya finalizó.
- Esperar los resultados: Si usas el método predeterminado `extract` (Python/Node), el SDK espera y devuelve los resultados finales.
- Iniciar y luego consultar: Si usas los métodos de inicio —`start_extract` (Python) o `startExtract` (Node)— el SDK devuelve un ID de trabajo de inmediato. Usa `get_extract_status` (Python) o `getExtractStatus` (Node) para consultar el progreso.

A continuación, se muestran ejemplos de código para comprobar el estado de un trabajo de extracción usando Python, Node.js y cURL:

### Posibles estados

- **completed**: La extracción se completó correctamente.
- **processing**: Firecrawl aún está procesando tu solicitud.
- **failed**: Ocurrió un error; los datos no se extrajeron por completo.
- **cancelled**: El trabajo fue cancelado por el usuario.

#### Ejemplo pendiente

```
{
  "success": true,
  "data": [],
  "status": "en_proceso",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

#### Ejemplo completado

```
{
  "success": true,
  "data": {
      "company_mission": "Firecrawl es la forma más sencilla de extraer datos de la web. Los desarrolladores nos utilizan para convertir, de forma confiable, URLs en markdown listo para LLM o en datos estructurados con una sola llamada a la API.",
      "supports_sso": false,
      "is_open_source": true,
      "is_in_yc": true
    },
  "status": "completado"
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

Si prefieres no definir una estructura estricta, puedes simplemente proporcionar un `prompt`. El modelo subyacente elegirá una estructura por ti, lo que puede ser útil para solicitudes más exploratorias o flexibles.

```
{
  "success": true,
  "data": {
    "company_mission": "Convierte sitios web en datos listos para LLM. Impulsa tus aplicaciones de IA con datos limpios extraídos de cualquier sitio web."
  }
}
```

## Mejora de resultados con búsqueda web

Establecer `enableWebSearch = true` en tu solicitud ampliará el rastreo más allá del conjunto de URL proporcionado. Esto puede capturar información de respaldo o relacionada de páginas enlazadas. Aquí tienes un ejemplo que extrae información sobre cámaras para tablero (dash cams), enriqueciendo los resultados con datos de páginas relacionadas:

### Respuesta de ejemplo con búsqueda en la web

```
{
  "success": true,
  "data": {
    "dash_cams": [
      {
        "name": "Nextbase 622GW",
        "price": "$399.99",
        "features": [
          "Grabación de video en 4K",
          "Estabilización de imagen",
          "Alexa integrado",
          "Integración con What3Words"
        ],
        /* Información de abajo enriquecida con otros sitios web como 
        https://www.techradar.com/best/best-dash-cam, encontrada 
        mediante el parámetro enableWebSearch */
        "pros": [
          "Excelente calidad de video",
          "Muy buena visión nocturna",
          "GPS integrado"
        ],
        "cons": ["Precio elevado", "La app puede ser inestable"]
      }
    ],
  }

```

La respuesta incluye contexto adicional obtenido de páginas relacionadas, lo que ofrece información más completa y precisa.

El punto de conexión `/extract` ahora permite extraer datos estructurados con un prompt sin necesidad de URLs específicas. Es útil para investigación o cuando se desconocen las URLs exactas. Actualmente en alfa.

## Limitaciones conocidas (Beta)

1. **Cobertura de sitios a gran escala**  
   Aún no se admite cubrir por completo sitios masivos (p. ej., “todos los productos de Amazon”) en una sola solicitud.
2. **Consultas lógicas complejas**  
   Solicitudes como “encontrar todas las publicaciones de 2025” pueden no devolver de forma fiable todos los datos esperados. Estamos trabajando en capacidades de consulta más avanzadas.
3. **Inconsistencias ocasionales**  
   Los resultados pueden variar entre ejecuciones, especialmente en sitios muy grandes o dinámicos. Por lo general se capturan los detalles clave, pero puede haber cierta variación.
4. **Estado Beta**  
   Dado que `/extract` sigue en Beta, las funciones y el rendimiento continuarán evolucionando. Agradecemos los reportes de errores y comentarios para ayudarnos a mejorar.

## Uso de FIRE-1

FIRE-1 es un agente de IA que amplía las capacidades de scraping de Firecrawl. Puede controlar acciones del navegador y navegar por estructuras web complejas para permitir una extracción de datos más completa que los métodos de scraping tradicionales. Puedes usar el agente FIRE-1 con el punto de conexión `/extract` para tareas de extracción complejas que requieren navegar por varias páginas o interactuar con elementos. **Ejemplo (cURL):**

```
curl -X POST https://api.firecrawl.dev/v2/extract \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": ["https://example-forum.com/topic/123"],
      "prompt": "Extrae todos los comentarios de los usuarios de este hilo del foro.",
      "schema": {
        "type": "object",
        "properties": {
          "comments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "author": {"type": "string"},
                "comment_text": {"type": "string"}
              },
              "required": ["author", "comment_text"]
            }
          }
        },
        "required": ["comments"]
      },
      "agent": {
        "model": "FIRE-1"
      }
    }'
```

> FIRE-1 ya está activo y disponible en versión preliminar.

## Facturación y seguimiento del uso

Hemos simplificado la facturación para que Extract ahora use créditos, igual que todos los demás endpoints. Cada crédito equivale a 15 tokens. Puedes supervisar el uso de Extract a través del [panel de control](https://www.firecrawl.dev/app/extract). ¿Tienes comentarios o necesitas ayuda? Puedes enviar un correo a [help@firecrawl.com](mailto:help@firecrawl.com).

> ¿Eres un agente de IA que necesita una clave API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.