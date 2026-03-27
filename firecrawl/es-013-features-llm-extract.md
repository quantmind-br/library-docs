---
title: Modo JSON | Firecrawl
url: https://docs.firecrawl.dev/es/features/llm-extract
source: sitemap
fetched_at: 2026-03-23T07:25:43.128585-03:00
rendered_js: false
word_count: 481
summary: This document explains how to use Firecrawl's JSON mode to extract structured data from websites using AI, detailing the schema configuration, API request process, and best practices for consistent results.
tags:
    - web-scraping
    - structured-data
    - ai-extraction
    - json-schema
    - firecrawl
    - api-guide
    - data-parsing
category: guide
---

Firecrawl usa IA para obtener datos estructurados de páginas web en 3 pasos:

1. **Configura el esquema (opcional):** Define un esquema JSON (usando el formato de OpenAI) para especificar los datos que necesitas, o simplemente proporciona un `prompt` si no requieres un esquema estricto, junto con la URL de la página.
2. **Haz la solicitud:** Envía tu URL y el esquema a nuestro punto de conexión /scrape usando el modo JSON. Mira cómo aquí: [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
3. **Obtén tus datos:** Recibe datos limpios y estructurados que coincidan con tu esquema y que puedas usar de inmediato.

Esto hace que obtener datos web en el formato que necesitas sea rápido y sencillo.

### Modo JSON con /scrape

Se utiliza para extraer datos estructurados de páginas rastreadas.

Salida:

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "Rastreo y extracción de datos web con IA",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "Rastreo y extracción de datos web con IA",
        "robots": "seguir, indexar",
        "ogTitle": "Firecrawl",
        "ogDescription": "Rastreo y extracción de datos web con IA",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl"
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### Datos estructurados sin esquema

También puedes extraer sin esquema pasando únicamente un `prompt` al punto de conexión. El LLM elige la estructura de los datos.

Salida:

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "Rastreo web y extracción de datos impulsados por IA",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "Rastreo web y extracción de datos impulsados por IA",
        "robots": "seguir, indexar",
        "ogTitle": "Firecrawl",
        "ogDescription": "Rastreo web y extracción de datos impulsados por IA",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

A continuación, un ejemplo completo que extrae información estructurada de un sitio web sobre una empresa:

Salida:

```
{
  "success": true,
  "data": {
    "json": {
      "company_mission": "Convertir sitios web en datos listos para LLM",
      "supports_sso": true,
      "is_open_source": true,
      "is_in_yc": true
    }
  }
}
```

### Opciones del formato JSON

Al usar el modo JSON en v2, incluye un objeto en `formats` con el esquema incorporado directamente: `formats: [{ type: 'json', schema: { ... }, prompt: '...' }]` Parámetros:

- `schema`: JSON Schema que describe la salida estructurada que deseas (obligatorio para la extracción basada en un esquema).
- `prompt`: Indicaciones opcionales para guiar la extracción (también se usa para la extracción sin esquema).

**Importante:** A diferencia de v1, en v2 no existe un parámetro independiente `jsonOptions`. El esquema debe incluirse directamente dentro del objeto de formato en el array `formats`.

Si obtienes resultados inconsistentes o incompletos al extraer JSON, estas prácticas pueden ayudar:

- **Mantén los prompts cortos y enfocados.** Los prompts largos con muchas reglas aumentan la variabilidad. En su lugar, mueve las restricciones específicas (como los valores permitidos) al esquema.
- **Usa nombres de propiedades concisos.** Evita incrustar instrucciones o listas de `enum` en los nombres de las propiedades. Usa una clave corta como `"installation_type"` y coloca los valores permitidos en un array `enum`.
- **Agrega arrays `enum` para campos restringidos.** Cuando un campo tiene un conjunto fijo de valores, enuméralos en `enum` y asegúrate de que coincidan con el texto exacto que aparece en la página.
- **Incluye manejo de valores null en las descripciones de los campos.** Agrega `"Return null if not found on the page."` a la `description` de cada campo para que el modelo no adivine valores faltantes.
- **Agrega indicaciones de ubicación.** Indica al modelo dónde encontrar los datos en la página, por ejemplo: `"Flow rate in GPM from the Specifications table."`.
- **Divide esquemas grandes en solicitudes más pequeñas.** Los esquemas con muchos campos (p. ej., 30 o más) producen resultados menos consistentes. Divídelos en 2–3 solicitudes de 10–15 campos cada una.

**Ejemplo de un esquema bien estructurado:**

```
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": ["string", "null"],
      "description": "Full descriptive product name as shown on the page. Return null if not found."
    },
    "installation_type": {
      "type": ["string", "null"],
      "description": "Installation type from the Specifications section. Return null if not found.",
      "enum": ["Deck-mount", "Wall-mount", "Countertop", "Drop-in", "Undermount"]
    },
    "flow_rate_gpm": {
      "type": ["string", "null"],
      "description": "Flow rate in GPM from the Specifications section. Return null if not found."
    }
  }
}
```

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.