---
title: Servidor MCP de Firecrawl
url: https://docs.firecrawl.dev/es/mcp-server
source: sitemap
fetched_at: 2026-03-23T07:29:31.93427-03:00
rendered_js: false
word_count: 2175
summary: This document provides instructions for installing and configuring the Firecrawl Model Context Protocol (MCP) server to enable web scraping and data extraction capabilities in various development environments.
tags:
    - mcp
    - firecrawl
    - web-scraping
    - integration
    - developer-tools
    - api-configuration
category: guide
---

Una implementación de servidor del Model Context Protocol (MCP) que integra [Firecrawl](https://github.com/firecrawl/firecrawl) para web scraping. Nuestro servidor MCP es de código abierto y está disponible en [GitHub](https://github.com/firecrawl/firecrawl-mcp-server).

## Características

- Web scraping, rastreo y descubrimiento
- Búsqueda y extracción de contenido
- Investigación avanzada con un agente autónomo
- Gestión de sesiones del navegador
- Compatibilidad en la nube y autogestionado
- Compatibilidad con HTTP por streaming

## Instalación

Puedes usar nuestra URL alojada de forma remota o ejecutar el servidor localmente. Obtén tu clave de API en [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)

### URL alojada remotamente

```
https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp
```

### Ejecutar con npx

```
env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

### Instalación manual

```
npm install -g firecrawl-mcp
```

### Ejecutar en Cursor

[![Añadir el servidor MCP de Firecrawl a Cursor](https://cursor.com/deeplink/mcp-install-dark.png)](cursor://anysphere.cursor-deeplink/mcp/install?name=firecrawl&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImZpcmVjcmF3bC1tY3AiXSwiZW52Ijp7IkZJUkVDUkFXTF9BUElfS0VZIjoiWU9VUi1BUEktS0VZIn19)

#### Instalación manual

Configuración de Cursor 🖥️ Nota: Requiere Cursor versión 0.45.6+ Para ver las instrucciones de configuración más actualizadas, consulta la documentación oficial de Cursor sobre cómo configurar servidores MCP: [Guía de configuración de servidores MCP de Cursor](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers) Para configurar Firecrawl MCP en Cursor **v0.48.6**

1. Abre la configuración de Cursor
2. Ve a Features &gt; MCP Servers
3. Haz clic en ”+ Add new global MCP server”
4. Ingresa el siguiente código:
   
   ```
   {
     "mcpServers": {
       "firecrawl-mcp": {
         "command": "npx",
         "args": ["-y", "firecrawl-mcp"],
         "env": {
           "FIRECRAWL_API_KEY": "YOUR-API-KEY"
         }
       }
     }
   }
   ```

Para configurar Firecrawl MCP en Cursor **v0.45.6**

1. Abre la configuración de Cursor
2. Ve a Features &gt; MCP Servers
3. Haz clic en ”+ Add New MCP Server”
4. Ingresa lo siguiente:
   
   - Name: “firecrawl-mcp” (o el nombre que prefieras)
   - Type: “command”
   - Command: `env FIRECRAWL_API_KEY=your-api-key npx -y firecrawl-mcp`

> Si usas Windows y tienes problemas, prueba `cmd /c "set FIRECRAWL_API_KEY=your-api-key && npx -y firecrawl-mcp"`

Reemplaza `your-api-key` por tu clave de API de Firecrawl. Si aún no tienes una, puedes crear una cuenta y obtenerla en [https://www.firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) Después de agregarlo, actualiza la lista de servidores MCP para ver las nuevas tools. El Composer Agent usará Firecrawl MCP automáticamente cuando corresponda, pero puedes solicitarlo explícitamente describiendo tus necesidades de web scraping. Accede al Composer con Command+L (Mac), selecciona “Agent” junto al botón de envío e ingresa tu consulta.

### Ejecutar en Windsurf

Añade esto a tu `./codeium/windsurf/model_config.json`:

```
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "TU_CLAVE_API"
      }
    }
  }
}
```

### Ejecución en modo HTTP con streaming

Para ejecutar el servidor localmente usando transporte HTTP con streaming en lugar del transporte `stdio` predeterminado:

```
env HTTP_STREAMABLE_SERVER=true FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

Utiliza la URL: [http://localhost:3000/v2/mcp](http://localhost:3000/v2/mcp) o [https://mcp.firecrawl.dev/{FIRECRAWL\_API\_KEY}/v2/mcp](https://mcp.firecrawl.dev/%7BFIRECRAWL_API_KEY%7D/v2/mcp)

### Instalación con Smithery (versión anterior)

Para instalar Firecrawl para Claude Desktop automáticamente mediante [Smithery](https://smithery.ai/server/@mendableai/mcp-server-firecrawl):

```
npx -y @smithery/cli install @mendableai/mcp-server-firecrawl --client claude
```

### Ejecutar en VS Code

Para una instalación con un solo clic, haz clic en uno de los botones de instalación de abajo… [![Instalar con NPX en VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D) [![Instalar con NPX en VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D&quality=insiders) Para una instalación manual, añade el siguiente bloque JSON a tu archivo de configuración de usuario (JSON) en VS Code. Puedes hacerlo pulsando `Ctrl + Shift + P` y escribiendo `Preferences: Open User Settings (JSON)`.

```
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "apiKey",
        "description": "Clave de API de Firecrawl",
        "password": true
      }
    ],
    "servers": {
      "firecrawl": {
        "command": "npx",
        "args": ["-y", "firecrawl-mcp"],
        "env": {
          "FIRECRAWL_API_KEY": "${input:apiKey}"
        }
      }
    }
  }
}
```

Opcionalmente, también puedes añadirlo a un archivo llamado `.vscode/mcp.json` en tu espacio de trabajo. Esto te permitirá compartir la configuración con otras personas:

```
{
  "inputs": [
    {
      "type": "promptString",
      "id": "apiKey",
      "description": "Clave de API de Firecrawl",
      "password": true
    }
  ],
  "servers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "${input:apiKey}"
      }
    }
  }
}
```

**Nota:** Algunos usuarios han informado de problemas al añadir el servidor MCP a VS Code debido a cómo valida JSON con un formato de esquema obsoleto ([microsoft/vscode#155379](https://github.com/microsoft/vscode/issues/155379)). Esto afecta a varias herramientas MCP, incluida Firecrawl. **Solución alternativa:** Desactiva la validación de JSON en VS Code para permitir que el servidor MCP se cargue correctamente. Consulta la referencia: [directus/directus#25906 (comment)](https://github.com/directus/directus/issues/25906#issuecomment-3369169513). El servidor MCP sigue funcionando correctamente cuando se invoca a través de otras extensiones, pero el problema se produce específicamente al registrarlo directamente en la lista de servidores MCP. Planeamos añadir instrucciones una vez que VS Code actualice su validación de esquemas.

### Ejecución en Claude Desktop

Añade lo siguiente al archivo de configuración de Claude:

```
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

### Ejecutar en Claude Code

Agrega el servidor MCP de Firecrawl usando la CLI de Claude Code. Puedes usar la URL alojada remotamente o ejecutarlo localmente:

```
# URL alojada remotamente (recomendado)
claude mcp add firecrawl --url https://mcp.firecrawl.dev/your-api-key/v2/mcp

# O ejecutarlo localmente mediante npx
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

### Ejecutar en Google Antigravity

Google Antigravity te permite configurar servidores MCP directamente a través de la interfaz de Agent. ![Instalación de MCP en Antigravity](https://mintcdn.com/firecrawl/rxzXygFiVc0TDh5X/images/guides/mcp/antigravity-mcp-installation.gif?s=19297c26dad5ed191862571618ce8c0a)

1. Abre el panel lateral de Agent en el Editor o en la vista de Agent Manager
2. Haz clic en el menú ”…” (Más acciones) y selecciona **MCP Servers**
3. Selecciona **View raw config** para abrir tu archivo local `mcp_config.json`
4. Añade la siguiente configuración:

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_FIRECRAWL_API_KEY"
      }
    }
  }
}
```

5. Guarda el archivo y haz clic en **Refresh** en la interfaz de Antigravity MCP para ver las nuevas herramientas

Reemplaza `YOUR_FIRECRAWL_API_KEY` con tu clave de API de [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys).

### Ejecución en n8n

Para conectar el servidor MCP de Firecrawl en n8n:

1. Obtén tu clave de API de Firecrawl en [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)
2. En tu flujo de trabajo de n8n, agrega un nodo **AI Agent**
3. En la configuración de **AI Agent**, agrega una nueva **Tool**
4. Selecciona **MCP Client Tool** como tipo de herramienta
5. Ingresa el endpoint del servidor MCP (reemplaza `{YOUR_FIRECRAWL_API_KEY}` con tu clave de API real):

```
  https://mcp.firecrawl.dev/{YOUR_FIRECRAWL_API_KEY}/v2/mcp
```

6. Configura **Server Transport** en **HTTP Streamable**
7. Configura **Authentication** en **None**
8. En **Tools to include**, puedes seleccionar **All**, **Selected** o **All Except**: esto pondrá a disposición las herramientas de Firecrawl (`scrape`, `crawl`, `map`, `search`, `extract`, etc.)

Para implementaciones autohospedadas, ejecuta el servidor MCP con npx y habilita el modo de transporte HTTP:

```
env HTTP_STREAMABLE_SERVER=true \
    FIRECRAWL_API_KEY=fc-YOUR_API_KEY \
    FIRECRAWL_API_URL=YOUR_FIRECRAWL_INSTANCE \
    npx -y firecrawl-mcp
```

Esto iniciará el servidor en `http://localhost:3000/v2/mcp`, que puedes usar en tu flujo de trabajo de n8n como endpoint. La variable de entorno `HTTP_STREAMABLE_SERVER=true` es necesaria, ya que n8n requiere transporte HTTP.

## Configuración

### Variables de entorno

#### Requisitos para la API en la nube

- `FIRECRAWL_API_KEY`: Tu clave de API de Firecrawl
  
  - Requerida al usar la API en la nube (por defecto)
  - Opcional al usar una instancia autogestionada con `FIRECRAWL_API_URL`
- `FIRECRAWL_API_URL` (opcional): Endpoint de API personalizado para instancias autogestionadas
  
  - Ejemplo: `https://firecrawl.your-domain.com`
  - Si no se proporciona, se usará la API en la nube (requiere clave de API)

#### Configuración opcional

##### Configuración de reintentos

- `FIRECRAWL_RETRY_MAX_ATTEMPTS`: Número máximo de reintentos (predeterminado: 3)
- `FIRECRAWL_RETRY_INITIAL_DELAY`: Espera inicial en milisegundos antes del primer reintento (predeterminado: 1000)
- `FIRECRAWL_RETRY_MAX_DELAY`: Espera máxima en milisegundos entre reintentos (predeterminado: 10000)
- `FIRECRAWL_RETRY_BACKOFF_FACTOR`: Multiplicador de backoff exponencial (predeterminado: 2)

##### Monitoreo del uso de créditos

- `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: Umbral de advertencia para el uso de créditos (predeterminado: 1000)
- `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: Umbral crítico para el uso de créditos (predeterminado: 100)

### Ejemplos de configuración

Para usar la API en la nube con reintentos personalizados y seguimiento de créditos:

```
# Requerido para la API en la nube
export FIRECRAWL_API_KEY=your-api-key

# Configuración opcional de reintentos
export FIRECRAWL_RETRY_MAX_ATTEMPTS=5        # Aumenta el número máximo de reintentos
export FIRECRAWL_RETRY_INITIAL_DELAY=2000    # Comienza con un retraso de 2 s
export FIRECRAWL_RETRY_MAX_DELAY=30000       # Retraso máximo de 30 s
export FIRECRAWL_RETRY_BACKOFF_FACTOR=3      # Retroceso más agresivo

# Monitoreo opcional de créditos
export FIRECRAWL_CREDIT_WARNING_THRESHOLD=2000    # Advertencia a los 2000 créditos
export FIRECRAWL_CREDIT_CRITICAL_THRESHOLD=500    # Crítico a los 500 créditos
```

Para instancias autoalojadas:

```
# Requerido para instalaciones autogestionadas
export FIRECRAWL_API_URL=https://firecrawl.tu-dominio.com

# Autenticación opcional para instalaciones autogestionadas
export FIRECRAWL_API_KEY=your-api-key  # Si tu instancia requiere autenticación

# Configuración personalizada de reintentos
export FIRECRAWL_RETRY_MAX_ATTEMPTS=10
export FIRECRAWL_RETRY_INITIAL_DELAY=500     # Comienza con reintentos más rápidos
```

### Configuración personalizada con Claude Desktop

Añade lo siguiente a tu `claude_desktop_config.json`:

```
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY_HERE",

        "FIRECRAWL_RETRY_MAX_ATTEMPTS": "5",
        "FIRECRAWL_RETRY_INITIAL_DELAY": "2000",
        "FIRECRAWL_RETRY_MAX_DELAY": "30000",
        "FIRECRAWL_RETRY_BACKOFF_FACTOR": "3",

        "FIRECRAWL_CREDIT_WARNING_THRESHOLD": "2000",
        "FIRECRAWL_CREDIT_CRITICAL_THRESHOLD": "500"
      }
    }
  }
}
```

### Configuración del sistema

El servidor incluye varios parámetros configurables que se pueden establecer mediante variables de entorno. Estos son los valores predeterminados en caso de no configurarse:

```
const CONFIG = {
  retry: {
    maxAttempts: 3, // Number of retry attempts for rate-limited requests
    initialDelay: 1000, // Initial delay before first retry (in milliseconds)
    maxDelay: 10000, // Maximum delay between retries (in milliseconds)
    backoffFactor: 2, // Multiplier for exponential backoff
  },
  credit: {
    warningThreshold: 1000, // Warn when credit usage reaches this level
    criticalThreshold: 100, // Alerta crítica cuando el uso de créditos alcance este nivel
  },
};
```

Estas configuraciones controlan:

1. **Comportamiento de reintentos**
   
   - Reintenta automáticamente las solicitudes fallidas debido a límites de velocidad (rate limits)
   - Usa backoff exponencial para evitar sobrecargar la API
   - Ejemplo: con la configuración predeterminada, los reintentos se realizarán en:
     
     - 1.er reintento: 1 segundo de espera
     - 2.º reintento: 2 segundos de espera
     - 3.er reintento: 4 segundos de espera (limitado por maxDelay)
2. **Monitoreo del uso de créditos**
   
   - Supervisa el consumo de créditos de la API para uso en la nube
   - Proporciona avisos al alcanzar umbrales específicos
   - Ayuda a prevenir interrupciones inesperadas del servicio
   - Ejemplo: con la configuración predeterminada:
     
     - Aviso con 1000 créditos restantes
     - Alerta crítica con 100 créditos restantes

### Limitación de tasa y procesamiento por lotes

El servidor utiliza las capacidades integradas de limitación de tasa y procesamiento por lotes de Firecrawl:

- Gestión automática de límites de tasa con backoff exponencial
- Procesamiento paralelo eficiente para operaciones por lotes
- Encolado y regulación inteligente de solicitudes
- Reintentos automáticos ante errores transitorios

Extrae contenido de una única URL con opciones avanzadas.

```
{
  "name": "firecrawl_scrape",
  "arguments": {
    "url": "https://example.com",
    "formatos": ["markdown"],
    "onlyMainContent": true,
    "waitFor": 1000,
    "mobile": false,
    "includeTags": ["article", "main"],
    "excludeTags": ["nav", "footer"],
    "skipTlsVerification": false
  }
}
```

Mapea un sitio web para descubrir todas las URL indexadas del sitio.

```
{
  "name": "firecrawl_map",
  "arguments": {
    "url": "https://example.com",
    "search": "blog",
    "sitemap": "include",
    "includeSubdomains": false,
    "limit": 100,
    "ignoreQueryParameters": true
  }
}
```

- `url`: La URL base del sitio web a mapear
- `search`: Término de búsqueda opcional para filtrar URL
- `sitemap`: Controla el uso del sitemap: “include”, “skip” o “only”
- `includeSubdomains`: Indica si se deben incluir subdominios en el mapeo
- `limit`: Número máximo de URL a devolver
- `ignoreQueryParameters`: Indica si se deben ignorar los parámetros de consulta al mapear

**Mejor para:** Descubrir URL en un sitio web antes de decidir qué datos extraer; encontrar secciones específicas de un sitio web. **Devuelve:** Array de URL encontradas en el sitio.

Busca en la web y, opcionalmente, extrae contenido de los resultados de búsqueda.

```
{
  "name": "firecrawl_search",
  "arguments": {
    "query": "tu consulta de búsqueda",
    "limit": 5,
    "location": "United States",
    "tbs": "qdr:m",
    "scrapeOptions": {
      "formats": ["markdown"],
      "onlyMainContent": true
    }
  }
}
```

- `query`: La cadena de consulta (obligatorio)
- `limit`: Número máximo de resultados a devolver
- `location`: Ubicación geográfica para los resultados de búsqueda
- `tbs`: Filtro de búsqueda basado en tiempo (por ejemplo, `qdr:d` para el último día, `qdr:w` para la última semana, `qdr:m` para el último mes)
- `filter`: Filtro de búsqueda adicional
- `sources`: Array de tipos de fuentes a buscar (`web`, `images`, `news`)
- `scrapeOptions`: Opciones de scraping de las páginas de resultados de búsqueda
- `enterprise`: Array de opciones de enterprise (`default`, `anon`, `zdr`)

Inicia un rastreo asíncrono con opciones avanzadas.

```
{
  "name": "firecrawl_crawl",
  "arguments": {
    "url": "https://example.com",
    "maxDiscoveryDepth": 2,
    "limit": 100,
    "allowExternalLinks": false,
    "deduplicateSimilarURLs": true
  }
}
```

### 5. Comprobar el estado del rastreo (`firecrawl_check_crawl_status`)

Comprueba el estado de una tarea de rastreo.

```
{
  "name": "firecrawl_check_crawl_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

**Devuelve:** Estado y progreso de la tarea de rastreo, incluidos los resultados si están disponibles.

Extrae información estructurada de páginas web usando capacidades de LLM. Es compatible tanto con extracción mediante IA en la nube como con LLM autoalojados.

```
{
  "name": "firecrawl_extract",
  "arguments": {
    "urls": ["https://example.com/page1", "https://example.com/page2"],
    "prompt": "Extract product information including name, price, and description",
    "schema": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "price": { "type": "number" },
        "description": { "type": "string" }
      },
      "required": ["name", "price"]
    },
    "allowExternalLinks": false,
    "enableWebSearch": false,
    "includeSubdomains": false
  }
}
```

Ejemplo de respuesta:

```
{
  "content": [
    {
      "type": "text",
      "text": {
        "name": "Example Product",
        "price": 99.99,
        "description": "This is an example product description"
      }
    }
  ],
  "isError": false
}
```

- `urls`: Matriz de URLs de las que extraer información
- `prompt`: Prompt personalizado para la extracción con el LLM
- `schema`: Esquema JSON para la extracción de datos estructurados
- `allowExternalLinks`: Permite la extracción desde enlaces externos
- `enableWebSearch`: Habilita la búsqueda web para obtener contexto adicional
- `includeSubdomains`: Incluye subdominios en la extracción

Al usar una instancia autogestionada (self-hosted), la extracción utilizará tu LLM configurado. Para la API en la nube, se usa el servicio de LLM gestionado de Firecrawl.

Agente autónomo de investigación web que navega de forma independiente por internet, busca información, recorre páginas y extrae datos estructurados a partir de tu consulta. Se ejecuta de forma asíncrona: devuelve inmediatamente un ID de tarea y haces *polling* a `firecrawl_agent_status` para comprobar cuándo se completa y recuperar los resultados.

```
{
  "name": "firecrawl_agent",
  "arguments": {
    "prompt": "Find the top 5 AI startups founded in 2024 and their funding amounts",
    "schema": {
      "type": "object",
      "properties": {
        "startups": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": { "type": "string" },
              "funding": { "type": "string" },
              "founded": { "type": "string" }
            }
          }
        }
      }
    }
  }
}
```

También puedes proporcionar URL específicas para que el agente se centre en ellas:

```
{
  "name": "firecrawl_agent",
  "arguments": {
    "urls": ["https://docs.firecrawl.dev", "https://firecrawl.dev/pricing"],
    "prompt": "Compare the features and pricing information from these pages"
  }
}
```

- `prompt`: Descripción en lenguaje natural de los datos que quieres (obligatorio, máximo 10.000 caracteres)
- `urls`: Matriz opcional de URLs para enfocar el agente en páginas específicas
- `schema`: Esquema JSON opcional para una salida estructurada

**Mejor para:** Tareas de investigación complejas donde no conoces las URLs exactas; recopilación de datos desde múltiples fuentes; encontrar información dispersa en la web; extraer datos de aplicaciones de una sola página (SPA) con mucho JavaScript que fallan con el `scrape` normal. **Devuelve:** ID de la tarea para comprobación del estado. Usa `firecrawl_agent_status` para consultar periódicamente los resultados.

### 8. Comprobar el estado del agente (`firecrawl_agent_status`)

Comprueba el estado de una tarea de agente y recupera los resultados cuando haya finalizado. Realiza consultas (polling) cada 15-30 segundos y sigue haciéndolas durante al menos 2-3 minutos antes de considerar que la solicitud ha fallado.

```
{
  "name": "firecrawl_agent_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

#### Opciones de estado del agente:

- `id`: El ID del trabajo del agente devuelto por `firecrawl_agent` (obligatorio)

**Posibles estados:**

- `processing`: El agente sigue investigando; continúa consultando
- `completed`: Investigación finalizada; la respuesta incluye los datos extraídos
- `failed`: Se produjo un error

**Devuelve:** Estado, progreso y resultados (si está completado) del trabajo del agente.

### 9. Crear sesión de navegador (`firecrawl_browser_create`)

Crea una sesión persistente de navegador para ejecutar código mediante CDP (Chrome DevTools Protocol).

```
{
  "name": "firecrawl_browser_create",
  "arguments": {
    "ttl": 120,
    "activityTtl": 60
  }
}
```

#### Opciones de creación del navegador:

- `ttl`: Duración total de la sesión en segundos (30-3600, opcional)
- `activityTtl`: Tiempo de inactividad en segundos (10-3600, opcional)

**Ideal para:** Ejecutar código (Python/JS) que interactúa con una página del navegador en tiempo real, automatización del navegador en múltiples pasos, sesiones con perfiles que se mantienen a través de múltiples llamadas a la herramienta. **Devuelve:** ID de sesión, URL de CDP y URL de vista en vivo.

### 10. Ejecutar código en el navegador (`firecrawl_browser_execute`)

Ejecuta código en una sesión de navegador activa. Permite comandos de agente del navegador (bash), Python o JavaScript.

```
{
  "name": "firecrawl_browser_execute",
  "arguments": {
    "sessionId": "session-id-here",
    "code": "agent-browser open https://example.com",
    "language": "bash"
  }
}
```

Ejemplo de Python con Playwright:

```
{
  "name": "firecrawl_browser_execute",
  "arguments": {
    "sessionId": "session-id-here",
    "code": "await page.goto('https://example.com')\ntitle = await page.title()\nprint(title)",
    "language": "python"
  }
}
```

#### Opciones de ejecución del navegador:

- `sessionId`: El ID de la sesión del navegador (requerido)
- `code`: El código a ejecutar (requerido)
- `language`: `bash`, `python` o `node` (opcional, valor predeterminado: `bash`)

**Comandos comunes de agent-browser (bash):**

- `agent-browser open <url>` — Navegar a la URL
- `agent-browser snapshot` — Obtener el árbol de accesibilidad con referencias en las que se puede hacer clic
- `agent-browser click @e5` — Hacer clic en el elemento por referencia obtenida del snapshot
- `agent-browser type @e3 "text"` — Escribir en el elemento
- `agent-browser screenshot [path]` — Tomar una captura de pantalla
- `agent-browser scroll down` — Desplazar la página hacia abajo
- `agent-browser wait 2000` — Esperar 2 segundos

**Devuelve:** Resultado de la ejecución que incluye stdout, stderr y el código de salida.

### 11. Eliminar sesión del navegador (`firecrawl_browser_delete`)

Elimina una sesión de navegador.

```
{
  "name": "firecrawl_browser_delete",
  "arguments": {
    "sessionId": "session-id-here"
  }
}
```

#### Opciones de eliminación del navegador:

- `sessionId`: El ID de la sesión del navegador que se va a destruir (obligatorio)

**Devuelve:** Confirmación de éxito.

### 12. Listar sesiones de navegador (`firecrawl_browser_list`)

Muestra las sesiones de navegador, opcionalmente filtradas por estado.

```
{
  "name": "firecrawl_browser_list",
  "arguments": {
    "status": "activo"
  }
}
```

#### Opciones de la lista de navegadores:

- `status`: Filtra por estado de la sesión: `active` o `destroyed` (opcional)

**Devuelve:** Array de sesiones de navegador.

## Sistema de registro

El servidor incluye un sistema de registro completo:

- Estado y progreso de las operaciones
- Métricas de rendimiento
- Monitoreo del uso de créditos
- Seguimiento de los límites de tasa
- Condiciones de error

Ejemplos de mensajes de registro:

```
[INFO] Servidor MCP de Firecrawl inicializado correctamente
[INFO] Starting scrape for URL: https://example.com
[INFO] Starting crawl for URL: https://example.com
[WARNING] Credit usage has reached warning threshold
[ERROR] Rate limit exceeded, retrying in 2s...
```

## Manejo de errores

El servidor ofrece un manejo de errores sólido:

- Reintentos automáticos para errores transitorios
- Manejo de límites de solicitudes con backoff
- Mensajes de error detallados
- Avisos sobre consumo de créditos
- Resiliencia ante errores de red

Ejemplo de respuesta de error:

```
{
  "content": [
    {
      "type": "text",
      "text": "Error: Límite de velocidad excedido. Reintentando en 2 segundos..."
    }
  ],
  "isError": true
}
```

## Desarrollo

```
# Instalar dependencias
npm install

# Construir
npm run build

# Ejecutar tests
npm test
```

### Cómo contribuir

1. Haz un fork del repositorio
2. Crea una rama para tu funcionalidad
3. Ejecuta las pruebas: `npm test`
4. Envía un pull request

### Gracias a los colaboradores

Gracias a [@vrknetha](https://github.com/vrknetha) y [@cawstudios](https://caw.tech) por la implementación inicial. Gracias a MCP.so y Klavis AI por alojar el servicio, y a [@gstarwd](https://github.com/gstarwd), [@xiangkaiz](https://github.com/xiangkaiz) y [@zihaolin96](https://github.com/zihaolin96) por integrar nuestro servidor.

## Licencia

Licencia MIT: consulta el archivo LICENSE para más detalles