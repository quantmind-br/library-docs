---
title: Extracción | Firecrawl
url: https://docs.firecrawl.dev/es/features/scrape
source: sitemap
fetched_at: 2026-03-23T07:25:16.707909-03:00
rendered_js: false
word_count: 1419
summary: Documentación técnica sobre el endpoint /scrape de Firecrawl, diseñado para convertir contenido web en formatos estructurados como Markdown, JSON y perfiles de marca para aplicaciones LLM.
tags:
    - firecrawl
    - web-scraping
    - markdown-conversion
    - llm-integration
    - data-extraction
    - api-reference
category: api
---

Firecrawl convierte páginas web en markdown, ideal para aplicaciones con LLM.

- Gestiona las complejidades: proxies, caché, límites de velocidad, contenido bloqueado por JS
- Maneja contenido dinámico: sitios dinámicos, sitios renderizados con JS, PDF, imágenes
- Genera markdown limpio, datos estructurados, capturas de pantalla o HTML.

Para más detalles, consulta la [referencia de la API del endpoint Scrape](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

### punto de conexión /scrape

Se utiliza para extraer el contenido de una URL.

### Instalación

### Uso

Para más información sobre los parámetros, consulta la [Referencia de la API](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

### Respuesta

Los SDK devolverán el objeto de datos directamente. cURL devolverá el payload exactamente como se muestra a continuación.

```
{
  "success": true,
  "data" : {
    "markdown": "¡Launch Week I ya está aquí! [Consulta nuestro lanzamiento del Día 2 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Obtén 2 meses gratis...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Inicio - Firecrawl",
      "description": "Firecrawl rastrea y convierte cualquier sitio web en Markdown limpio.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "seguir, indexar",
      "ogTitle": "Firecrawl",
      "ogDescription": "Convierte cualquier sitio web en datos listos para LLM.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

Ahora puedes elegir en qué formatos quieres el resultado. Puedes especificar múltiples formatos de salida. Los formatos compatibles son:

- Markdown (`markdown`)
- Resumen (`summary`)
- HTML (`html`) - versión limpia del HTML de la página
- HTML sin procesar (`rawHtml`) - HTML sin modificar tal como se recibe de la página
- Captura de pantalla (`screenshot`, con opciones como `fullPage`, `quality`, `viewport`) — las URL de las capturas de pantalla caducan después de 24 horas
- Enlaces (`links`)
- JSON (`json`) - salida estructurada
- Imágenes (`images`) - extrae todas las URL de imágenes de la página
- Identidad de marca (`branding`) - extrae la identidad de marca y el sistema de diseño

Las claves de salida coincidirán con el formato que elijas.

### punto de conexión /scrape (con json)

Se usa para extraer datos estructurados de páginas rastreadas.

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

Ahora puedes extraer sin un esquema con solo pasar un `prompt` al punto de conexión. El LLM elige la estructura de los datos.

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

### Opciones del formato JSON

Al usar el formato `json`, pasa un objeto dentro de `formats` con los siguientes parámetros:

- `schema`: JSON Schema para la salida estructurada.
- `prompt`: Prompt opcional para ayudar a guiar la extracción cuando hay un esquema o cuando prefieras una guía ligera.

### endpoint /scrape (con branding)

El formato de branding extrae información completa sobre la identidad de marca de una página web, incluidos colores, fuentes, tipografía, espaciado, componentes de la UI y más. Es útil para analizar sistemas de diseño, monitorear marcas o crear herramientas que necesiten comprender la identidad visual de un sitio web.

### Respuesta

El formato de marca devuelve un objeto `BrandingProfile` completo con la siguiente estructura:

```
{
  "success": true,
  "data": {
    "branding": {
      "colorScheme": "dark",
      "logo": "https://firecrawl.dev/logo.svg",
      "colors": {
        "primary": "#FF6B35",
        "secondary": "#004E89",
        "accent": "#F77F00",
        "background": "#1A1A1A",
        "textPrimary": "#FFFFFF",
        "textSecondary": "#B0B0B0"
      },
      "fonts": [
        {
          "family": "Inter"
        },
        {
          "family": "Roboto Mono"
        }
      ],
      "typography": {
        "fontFamilies": {
          "primary": "Inter",
          "heading": "Inter",
          "code": "Roboto Mono"
        },
        "fontSizes": {
          "h1": "48px",
          "h2": "36px",
          "h3": "24px",
          "body": "16px"
        },
        "fontWeights": {
          "regular": 400,
          "medium": 500,
          "bold": 700
        }
      },
      "spacing": {
        "baseUnit": 8,
        "borderRadius": "8px"
      },
      "components": {
        "buttonPrimary": {
          "background": "#FF6B35",
          "textColor": "#FFFFFF",
          "borderRadius": "8px"
        },
        "buttonSecondary": {
          "background": "transparent",
          "textColor": "#FF6B35",
          "borderColor": "#FF6B35",
          "borderRadius": "8px"
        }
      },
      "images": {
        "logo": "https://firecrawl.dev/logo.svg",
        "favicon": "https://firecrawl.dev/favicon.ico",
        "ogImage": "https://firecrawl.dev/og-image.png"
      }
    }
  }
}
```

### Estructura del perfil de marca

El objeto `branding` contiene las siguientes propiedades:

- `colorScheme`: El esquema de color detectado (“light” o “dark”)
- `logo`: URL del logotipo principal
- `colors`: Objeto que contiene los colores de la marca:
  
  - `primary`, `secondary`, `accent`: Colores principales de la marca
  - `background`, `textPrimary`, `textSecondary`: Colores de la interfaz
  - `link`, `success`, `warning`, `error`: Colores semánticos
- `fonts`: Lista de familias tipográficas usadas en la página
- `typography`: Información tipográfica detallada:
  
  - `fontFamilies`: Familias tipográficas principal, de encabezados y de código
  - `fontSizes`: Definiciones de tamaños para encabezados y cuerpo de texto
  - `fontWeights`: Definiciones de grosor (light, regular, medium, bold)
  - `lineHeights`: Valores de interlineado para distintos tipos de texto
- `spacing`: Información de espaciado y maquetación:
  
  - `baseUnit`: Unidad base de espaciado en píxeles
  - `borderRadius`: Radio de borde predeterminado
  - `padding`, `margins`: Valores de espaciado
- `components`: Estilos de componentes de la interfaz:
  
  - `buttonPrimary`, `buttonSecondary`: Estilos de botones
  - `input`: Estilos de campos de entrada
- `icons`: Información sobre el estilo de los íconos
- `images`: Imágenes de marca (logo, favicon, og:image)
- `animations`: Configuración de animaciones y transiciones
- `layout`: Configuración de distribución (grid, alturas de encabezado/pie)
- `personality`: Rasgos de personalidad de la marca (tono, energía, público objetivo)

### Combinar con otros formatos

Puedes combinar el formato de branding con otros formatos para obtener datos completos de la página:

Firecrawl te permite realizar varias acciones en una página web antes de extraer su contenido. Esto es especialmente útil para interactuar con contenido dinámico, navegar entre páginas o acceder a contenido que requiera interacción del usuario. Aquí tienes un ejemplo de cómo usar acciones para ir a google.com, buscar Firecrawl, hacer clic en el primer resultado y tomar una captura de pantalla. Es importante usar casi siempre la acción `wait` antes y/o después de ejecutar otras acciones para dar tiempo suficiente a que la página cargue.

### Ejemplo

### Salida

Para más información sobre los parámetros de las acciones, consulta la [Referencia de la API](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## Ubicación e idioma

Especifica el país y los idiomas preferidos para obtener contenido relevante según tu ubicación de destino y tus preferencias de idioma.

### Cómo funciona

Cuando especificas la ubicación, Firecrawl usará un proxy adecuado si está disponible y emulará el idioma y la zona horaria correspondientes. De forma predeterminada, la ubicación se establece en “US” si no se indica lo contrario.

### Uso

Para usar la configuración de ubicación e idioma, incluye el objeto `location` en el cuerpo de la solicitud con las siguientes propiedades:

- `country`: código de país ISO 3166-1 alfa-2 (p. ej., ‘US’, ‘AU’, ‘DE’, ‘JP’). Por defecto: ‘US’.
- `languages`: una lista de idiomas y configuraciones regionales preferidas para la solicitud en orden de prioridad. Por defecto, usa el idioma de la ubicación especificada.

Para más información sobre las ubicaciones compatibles, consulta la [documentación de proxies](https://docs.firecrawl.dev/es/features/proxies).

## Caché y maxAge

Para acelerar las solicitudes, Firecrawl sirve resultados desde la caché por defecto cuando hay una copia reciente disponible.

- **Ventana de frescura predeterminada**: `maxAge = 172800000` ms (2 días). Si la copia en caché es más reciente que esto, se devuelve al instante; de lo contrario, la página se vuelve a extraer y luego se almacena en caché.
- **Rendimiento**: Esto puede acelerar las extracciones hasta 5× cuando los datos no necesitan estar ultra frescos.
- **Obtener siempre contenido fresco**: Establece `maxAge` en `0`. Ten en cuenta que esto evita el uso de la caché por completo, por lo que cada solicitud recorre todo el pipeline de scraping, lo que significa que la solicitud tardará más en completarse y es más probable que falle. Utiliza un `maxAge` distinto de cero si la frescura en cada solicitud no es crítica.
- **Evitar almacenamiento**: Establece `storeInCache` en `false` si no quieres que Firecrawl almacene/guarde los resultados de esta solicitud en la caché.
- **Consulta solo en caché**: Establece `minAge` para realizar una consulta solo en caché sin activar una nueva extracción. El valor está en milisegundos y especifica la antigüedad mínima que deben tener los datos en caché. Si no se encuentran datos en caché, se devuelve un `404` con el código de error `SCRAPE_NO_CACHED_DATA`. Establece `minAge` en `1` para aceptar cualquier dato en caché independientemente de su antigüedad.
- **Seguimiento de cambios**: Las solicitudes que incluyen `changeTracking` omiten la caché, por lo que se ignora `maxAge`.

Ejemplo (forzar contenido fresco):

Ejemplo (usar una ventana de caché de 10 minutos):

## Raspado por lotes de múltiples URL

Ahora puedes raspar varias URL en lote al mismo tiempo. Recibe las URL iniciales y parámetros opcionales como argumentos. El argumento params te permite especificar opciones adicionales para el trabajo de raspado por lotes, como los formatos de salida.

### Cómo funciona

Es muy similar al funcionamiento del punto de conexión `/crawl`. Envía un trabajo de scraping por lotes y devuelve un ID de trabajo para consultar el estado del scraping por lotes. El SDK ofrece 2 métodos: sincrónico y asincrónico. El método sincrónico devuelve los resultados del trabajo de scraping por lotes, mientras que el asincrónico devuelve un ID de trabajo que puedes usar para consultar el estado del scraping por lotes.

### Uso

### Respuesta

Si usas los métodos síncronos de los SDK, devolverá los resultados del scraping por lotes. De lo contrario, devolverá un ID de tarea que puedes usar para consultar el estado del scraping por lotes.

#### Sincronía

```
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Página principal de la documentación de Firecrawl![logotipo claro](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Crea un «chat con el sitio web» usando Groq Llama 3 | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Aprende a usar Firecrawl, Groq Llama 3 y LangChain para crear un bot de «chat con tu sitio web»."
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

#### Asíncrono

Luego puedes usar el ID del trabajo para consultar el estado del scrape por lotes llamando al punto de conexión `/batch/scrape/{id}`. Este punto de conexión está pensado para usarse mientras el trabajo sigue en ejecución o justo después de que haya finalizado, **ya que los trabajos de scrape por lotes expiran a las 24 horas**.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Modo mejorado

Para sitios web complejos, Firecrawl ofrece un modo mejorado que proporciona mayores tasas de éxito a la vez que mantiene la privacidad. Obtén más información sobre el [Modo mejorado](https://docs.firecrawl.dev/es/features/enhanced-mode).

## Retención cero de datos (ZDR)

Firecrawl admite la Retención cero de datos (ZDR) para equipos con requisitos estrictos de gestión de datos. Cuando está habilitada, Firecrawl no conservará ningún contenido de la página ni datos extraídos más allá de la duración de la solicitud. Para habilitar ZDR, establece `zeroDataRetention: true` en tu solicitud:

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "url": "https://example.com",
    "formats": ["markdown"],
    "zeroDataRetention": true
  }'
```

ZDR está disponible en los planes Enterprise y debe estar habilitado para tu equipo. Visita [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) para comenzar. ZDR añade **1 crédito adicional por página** además del costo base del scrape.

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.