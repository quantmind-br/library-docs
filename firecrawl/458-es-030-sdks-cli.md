---
title: CLI | Firecrawl
url: https://docs.firecrawl.dev/es/sdks/cli
source: sitemap
fetched_at: 2026-03-23T07:25:08.970806-03:00
rendered_js: false
word_count: 1244
summary: This document provides a comprehensive guide on installing, authenticating, and using the Firecrawl CLI to perform web scraping, searching, and site mapping tasks.
tags:
    - firecrawl-cli
    - web-scraping
    - data-extraction
    - command-line-interface
    - api-integration
    - automation
category: reference
---

## Instalación

Si estás usando cualquier agente de IA como Claude Code, puedes instalar el Skill de Firecrawl a continuación y el agente podrá configurarlo por ti.

```
npx -y firecrawl-cli@latest init --all --browser
```

- `--all` instala el Skill de Firecrawl en todos los agentes de codificación con IA detectados
- `--browser` abre el navegador automáticamente para la autenticación de Firecrawl

También puedes instalar manualmente la CLI de Firecrawl de forma global usando npm:

```
# Instalar globalmente con npm
npm install -g firecrawl-cli
```

## Autenticación

Antes de usar la CLI, primero debes autenticarte con tu clave de API de Firecrawl.

### Inicio de sesión

```
# Inicio de sesión interactivo (abre el navegador o solicita la clave API)
firecrawl login

# Inicio de sesión con autenticación por navegador (recomendado para agentes)
firecrawl login --browser

# Inicio de sesión con clave API directamente
firecrawl login --api-key fc-YOUR-API-KEY

# O establecer mediante variable de entorno
export FIRECRAWL_API_KEY=fc-YOUR-API-KEY
```

### Ver la configuración

```
# Ver configuración actual y estado de autenticación
firecrawl view-config
```

### Cerrar sesión

```
# Borrar credenciales almacenadas
firecrawl logout
```

### Autohospedado / Desarrollo local

Para instancias de Firecrawl autohospedadas o desarrollo local, usa la opción `--api-url`:

```
# Usa una instancia local de Firecrawl (no requiere clave de API)
firecrawl --api-url http://localhost:3002 scrape https://example.com

# Or set via environment variable
export FIRECRAWL_API_URL=http://localhost:3002
firecrawl scrape https://example.com

# Configure and persist the custom API URL
firecrawl config --api-url http://localhost:3002
```

Cuando uses una URL de la API personalizada (cualquier valor distinto de `https://api.firecrawl.dev`), la autenticación con clave de API se omite automáticamente, lo que te permite usar instancias locales sin una clave de API.

### Comprobar estado

Comprueba la instalación, la autenticación y consulta los límites de velocidad (rate limits):

Genera la salida cuando esté listo:

```
  🔥 firecrawl cli v1.1.1

  ● Authenticated via FIRECRAWL_API_KEY
  Concurrency: 0/100 jobs (parallel scrape limit)
  Credits: 500,000 remaining
```

- **Concurrencia**: Máximo de tareas en paralelo. Ejecuta operaciones en paralelo lo más cerca posible de este límite, pero sin superarlo.
- **Créditos**: Créditos de API restantes. Cada operación de scrape/crawl consume créditos.

## Comandos

### Scrape

Extrae el contenido de una única URL en distintos formatos.

```
# Extraer datos de una URL (predeterminado: salida en markdown)
firecrawl https://example.com

# O usar el comando explícito de scrape
firecrawl scrape https://example.com

# Recomendado: usar --only-main-content para obtener una salida limpia sin navegación/pie de página
firecrawl https://example.com --only-main-content
```

#### Formatos de salida

```
# Obtener salida HTML
firecrawl https://example.com --html

# Múltiples formatos (devuelve JSON)
firecrawl https://example.com --format markdown,links

# Obtener imágenes de una página
firecrawl https://example.com --format images

# Obtener un resumen del contenido de la página
firecrawl https://example.com --format summary

# Rastrear cambios en una página
firecrawl https://example.com --format changeTracking

# Formatos disponibles: markdown, html, rawHtml, links, screenshot, json, images, summary, changeTracking, attributes, branding
```

#### Opciones de Scrape

```
# Extraer solo el contenido principal (elimina navegación y pies de página)
firecrawl https://example.com --only-main-content

# Wait for JavaScript rendering
firecrawl https://example.com --wait-for 3000

# Take a screenshot
firecrawl https://example.com --screenshot

# Include/exclude specific HTML tags
firecrawl https://example.com --include-tags article,main
firecrawl https://example.com --exclude-tags nav,footer

# Save output to file
firecrawl https://example.com -o output.md

# Pretty print JSON output
firecrawl https://example.com --format markdown,links --pretty

# Force JSON output even with single format
firecrawl https://example.com --json

# Show request timing information
firecrawl https://example.com --timing
```

**Opciones disponibles:**

OpciónAliasDescripción`--url <url>``-u`URL para hacer scrape (alternativa al argumento posicional)`--format <formats>``-f`Formatos de salida (separados por comas): `markdown`, `html`, `rawHtml`, `links`, `screenshot`, `json`, `images`, `summary`, `seguimientoDeCambios`, `attributes`, `branding``--html``-H`Atajo para `--format html``--only-main-content`Extraer solo el contenido principal`--wait-for <ms>`Tiempo de espera en milisegundos para el renderizado de JS`--screenshot`Tomar una captura de pantalla`--include-tags <tags>`Etiquetas HTML a incluir (separadas por comas)`--exclude-tags <tags>`Etiquetas HTML a excluir (separadas por comas)`--output <path>``-o`Guardar la salida en un archivo`--json`Forzar salida JSON incluso con un solo formato`--pretty`Imprimir el JSON de salida con formato`--timing`Mostrar el tiempo de la solicitud y otra información útil

* * *

### Buscar

Busca en la web y, opcionalmente, hace scraping de los resultados.

```
# Buscar en la web
firecrawl search "web scraping tutorials"

# Limitar resultados
firecrawl search "AI news" --limit 10

# Imprimir resultados con formato
firecrawl search "machine learning" --pretty
```

#### Opciones de búsqueda

```
# Search specific sources
firecrawl search "AI" --sources web,news,images

# Search with category filters
firecrawl search "react hooks" --categories github
firecrawl search "machine learning" --categories research,pdf

# Time-based filtering
firecrawl search "tech news" --tbs qdr:h   # Last hour
firecrawl search "tech news" --tbs qdr:d   # Last day
firecrawl search "tech news" --tbs qdr:w   # Última semana
firecrawl search "tech news" --tbs qdr:m   # Last month
firecrawl search "tech news" --tbs qdr:y   # Last year

# Location-based search
firecrawl search "restaurants" --location "Berlin,Germany" --country DE

# Search and scrape results
firecrawl search "documentation" --scrape --scrape-formats markdown

# Save to file
firecrawl search "firecrawl" --pretty -o results.json
```

**Opciones disponibles:**

OpciónDescripción`--limit <number>`Número máximo de resultados (predeterminado: 5, máximo: 100)`--sources <sources>`Fuentes de búsqueda: `web`, `images`, `news` (separadas por comas)`--categories <categories>`Filtrar por categoría: `github`, `research`, `pdf` (separadas por comas)`--tbs <value>`Filtro de tiempo: `qdr:h` (hora), `qdr:d` (día), `qdr:w` (semana), `qdr:m` (mes), `qdr:y` (año)`--location <location>`Segmentación geográfica (p. ej., “Berlin,Germany”)`--country <code>`Código de país ISO (predeterminado: US)`--timeout <ms>`Tiempo de espera en milisegundos (predeterminado: 60000)`--ignore-invalid-urls`Excluir URLs no válidas para otros endpoints de Firecrawl`--scrape`Extraer resultados de búsqueda`--scrape-formats <formats>`formatos para contenido extraído (predeterminado: markdown)`--only-main-content`Incluir solo el contenido principal al extraer (predeterminado: true)`--json`Salida como JSON`--output <path>`Guardar la salida en un archivo`--pretty`Imprimir salida JSON con formato legible

* * *

### Map

Obtén rápidamente todas las URL de un sitio web.

```
# Descubre todas las URLs de un sitio web
firecrawl map https://example.com

# Output as JSON
firecrawl map https://example.com --json

# Limit number of URLs
firecrawl map https://example.com --limit 500
```

#### Opciones de mapeo

```
# Filter URLs by search query
firecrawl map https://example.com --search "blog"

# Include subdomains
firecrawl map https://example.com --include-subdomains

# Control sitemap usage
firecrawl map https://example.com --sitemap include   # Use sitemap
firecrawl map https://example.com --sitemap skip      # Skip sitemap
firecrawl map https://example.com --sitemap only      # Solo usar sitemap

# Ignore query parameters (dedupe URLs)
firecrawl map https://example.com --ignore-query-parameters

# Wait for map to complete with timeout
firecrawl map https://example.com --wait --timeout 60

# Save to file
firecrawl map https://example.com -o urls.txt
firecrawl map https://example.com --json --pretty -o urls.json
```

**Opciones disponibles:**

OpciónDescripción`--url <url>`URL que se va a mapear (alternativa al argumento posicional)`--limit <number>`Número máximo de URLs a descubrir`--search <query>`Filtrar URLs por consulta de búsqueda`--sitemap <mode>`Manejo del sitemap: `include`, `skip`, `only``--include-subdomains`Incluir subdominios`--ignore-query-parameters`Tratar URLs con distintos parámetros de consulta como la misma`--wait`Esperar a que finalice el mapeo`--timeout <seconds>`Tiempo de espera en segundos`--json`Salida en formato JSON`--output <path>`Guardar la salida en un archivo`--pretty`Imprimir la salida JSON con formato legible

* * *

### Navegador

Haz que tus agentes interactúen con la web usando un entorno aislado de navegador seguro. Inicia sesiones de navegador en la nube y ejecuta código en Python, JavaScript o bash de forma remota. Cada sesión ejecuta una instancia completa de Chromium — no necesitas tener un navegador instalado localmente. El código se ejecuta del lado del servidor con un objeto `page` de [Playwright](https://playwright.dev/) preconfigurado y listo para usar.

```
# Launch a cloud browser session
firecrawl browser launch-session

# Ejecutar comandos de agent-browser (por defecto - "agent-browser" se añade automáticamente como prefijo)
firecrawl browser execute "open https://example.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "click @e5"
firecrawl browser execute "scrape"

# Execute Playwright Python code
firecrawl browser execute --python 'await page.goto("https://example.com")
print(await page.title())'

# Execute Playwright JavaScript code
firecrawl browser execute --node 'await page.goto("https://example.com"); console.log(await page.title());'

# List all sessions (or: list active / list destroyed)
firecrawl browser list

# Close the active session
firecrawl browser close
```

#### Opciones del navegador

```
# Launch with custom TTL (10 minutes) and live view
firecrawl browser launch-session --ttl 600 --stream

# Launch with inactivity timeout
firecrawl browser launch-session --ttl 120 --ttl-inactivity 60

# Comandos de agent-browser (por defecto - "agent-browser" se agrega automáticamente como prefijo)
firecrawl browser execute "open https://news.ycombinator.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "click @e3"
firecrawl browser execute "scrape"

# Playwright Python - navigate, interact, extract
firecrawl browser execute --python '
await page.goto("https://news.ycombinator.com")
items = await page.query_selector_all(".titleline > a")
for item in items[:5]:
    print(await item.text_content())
'

# Playwright JavaScript - same page object
firecrawl browser execute --node '
await page.goto("https://example.com");
const title = await page.title();
console.log(title);
'

# Explicit bash mode - runs in the sandbox
firecrawl browser execute --bash "agent-browser snapshot"

# Target a specific session
firecrawl browser execute --session <id> --python 'print(await page.title())'

# Save output to file
firecrawl browser execute "scrape" -o result.txt

# Close a specific session
firecrawl browser close --session <id>

# List sessions (all / active / destroyed)
firecrawl browser list
firecrawl browser list active --json
```

**Subcomandos:**

SubcomandoDescripción`launch-session`Inicia una nueva sesión de navegador en la nube (devuelve el ID de sesión, la URL de CDP y la URL de vista en vivo)`execute <code>`Ejecuta código Playwright en Python/JS o comandos bash en una sesión`list [status]`Lista las sesiones de navegador (filtra por `active` o `destroyed`)`close`Cierra una sesión de navegador

**Opciones de ejecución:**

OpciónDescripción`--bash`Ejecuta comandos bash de forma remota en el entorno aislado (sandbox) (predeterminado). [agent-browser](https://github.com/vercel-labs/agent-browser) (más de 40 comandos) viene preinstalado y se añade automáticamente como prefijo. `CDP_URL` se inyecta automáticamente para que agent-browser se conecte a tu sesión de forma automática. La mejor opción para agentes de IA.`--python`Ejecuta como código Playwright en Python. Hay disponible un objeto `page` de Playwright — usa `await page.goto()`, `await page.title()`, etc.`--node`Ejecuta como código Playwright en JavaScript. El mismo objeto `page` está disponible.`--session <id>`Apunta a una sesión específica (predeterminado: sesión activa)

**Opciones de lanzamiento:**

OpciónDescripción`--ttl <seconds>`TTL total de la sesión (predeterminado: 600, rango: 30–3600)`--ttl-inactivity <seconds>`Cierre automático tras inactividad (rango: 10–3600)`--profile <name>`Nombre del perfil (guarda y reutiliza el estado del navegador entre sesiones)`--no-save-changes`Carga los datos de un perfil existente sin guardar los cambios`--stream`Habilita la transmisión de la vista en vivo

**Opciones comunes:**

OpciónDescripción`--output <path>`Guarda la salida en un archivo`--json`Genera la salida en formato JSON

* * *

### Rastrear

Rastrea todo un sitio web a partir de una URL.

```
# Iniciar un rastreo (devuelve el ID del trabajo inmediatamente)
firecrawl crawl https://example.com

# Wait for crawl to complete
firecrawl crawl https://example.com --wait

# Wait with progress indicator
firecrawl crawl https://example.com --wait --progress
```

#### Consultar el estado del rastreo

```
# Verificar estado del crawl usando el ID del trabajo
firecrawl crawl <job-id>

# Ejemplo con un ID de trabajo real
firecrawl crawl 550e8400-e29b-41d4-a716-446655440000
```

#### Opciones de rastreo

```
# Limit crawl depth and pages
firecrawl crawl https://example.com --limit 100 --max-depth 3 --wait

# Include only specific paths
firecrawl crawl https://example.com --include-paths /blog,/docs --wait

# Exclude specific paths
firecrawl crawl https://example.com --exclude-paths /admin,/login --wait

# Include subdomains
firecrawl crawl https://example.com --allow-subdomains --wait

# Crawl entire domain
firecrawl crawl https://example.com --crawl-entire-domain --wait

# Rate limiting
firecrawl crawl https://example.com --delay 1000 --max-concurrency 2 --wait

# Intervalo de consulta y tiempo de espera personalizados
firecrawl crawl https://example.com --wait --poll-interval 10 --timeout 300

# Save results to file
firecrawl crawl https://example.com --wait --pretty -o results.json
```

**Opciones disponibles:**

OpciónDescripción`--url <url>`URL a rastrear (alternativa al argumento posicional)`--wait`Esperar a que el rastreo termine`--progress`Mostrar indicador de progreso mientras se espera`--poll-interval <seconds>`Intervalo de sondeo (por defecto: 5)`--timeout <seconds>`Tiempo máximo de espera`--status`Consultar el estado de un trabajo de rastreo existente`--limit <number>`Número máximo de páginas a rastrear`--max-depth <number>`Profundidad máxima de rastreo`--include-paths <paths>`Rutas a incluir (separadas por comas)`--exclude-paths <paths>`Rutas a excluir (separadas por comas)`--sitemap <mode>`Manejo del sitemap: `include`, `skip`, `only``--allow-subdomains`Incluir subdominios`--allow-external-links`Seguir enlaces externos`--crawl-entire-domain`Rastrear todo el dominio`--ignore-query-parameters`Considerar URLs con distintos parámetros como iguales`--delay <ms>`Retraso entre solicitudes`--max-concurrency <n>`Número máximo de solicitudes concurrentes`--output <path>`Guardar el resultado en un archivo`--pretty`Imprimir la salida JSON con formato legible

* * *

### Agente

Busca y recopila datos de la web usando indicaciones en lenguaje natural.

```
# Basic usage - URLs are optional
firecrawl agent "Encuentra las 5 principales startups de IA y sus montos de financiamiento" --wait

# Focus on specific URLs
firecrawl agent "Compare pricing plans" --urls https://slack.com/pricing,https://teams.microsoft.com/pricing --wait

# Use a schema for structured output
firecrawl agent "Get company information" --urls https://example.com --schema '{"name": "string", "founded": "number"}' --wait

# Use schema from a file
firecrawl agent "Get product details" --urls https://example.com --schema-file schema.json --wait
```

#### Opciones del agente

```
# Use Spark 1 Pro for higher accuracy
firecrawl agent "Competitive analysis across multiple domains" --model spark-1-pro --wait

# Set max credits to limit costs
firecrawl agent "Gather contact information from company websites" --max-credits 100 --wait

# Check status of an existing job
firecrawl agent <job-id> --status

# Custom polling interval and timeout
firecrawl agent "Summarize recent blog posts" --wait --poll-interval 10 --timeout 300

# Save output to file
firecrawl agent "Encontrar información de precios" --urls https://example.com --wait -o pricing.json --pretty
```

**Opciones disponibles:**

OpciónDescripción`--urls <urls>`Lista opcional de URL en las que enfocar el agente (separadas por comas)`--model <model>`Modelo a utilizar: `spark-1-mini` (predeterminado, 60% más barato) o `spark-1-pro` (mayor precisión)`--schema <json>`Esquema JSON para salida estructurada (cadena JSON en línea)`--schema-file <path>`Ruta al archivo de esquema JSON para salida estructurada`--max-credits <number>`Créditos máximos que se pueden gastar (el trabajo falla si se alcanza el límite)`--status`Verificar el estado de un trabajo de agente existente`--wait`Esperar a que el agente termine antes de devolver los resultados`--poll-interval <seconds>`Intervalo de sondeo mientras se espera (predeterminado: 5)`--timeout <seconds>`Tiempo máximo de espera (predeterminado: sin límite)`--output <path>`Guardar la salida en un archivo`--json`Salida en formato JSON

* * *

### Uso de créditos

Consulta el saldo y el uso de créditos de tu equipo.

```
# View credit usage
firecrawl credit-usage

# Salida en formato JSON
firecrawl credit-usage --json --pretty
```

* * *

### Versión

Mostrar la versión de la CLI.

```
firecrawl version
# o
firecrawl --version
```

## Opciones globales

Estas opciones están disponibles para todos los comandos:

OpciónAbrev.Descripción`--status`Muestra la versión, el estado de autenticación, la concurrencia y los créditos`--api-key <key>``-k`Sobrescribe la clave de API almacenada para este comando`--api-url <url>`Usa una URL de API personalizada (para entornos autoalojados/desarrollo local)`--help``-h`Muestra la ayuda para un comando`--version``-V`Muestra la versión de la CLI

## Manejo de la salida

La CLI envía la salida a stdout de forma predeterminada, lo que facilita usarla en pipes o redirigirla:

```
# Canalizar markdown a otro comando
firecrawl https://example.com | head -50

# Redirigir a un archivo
firecrawl https://example.com > output.md

# Guardar JSON con formato legible
firecrawl https://example.com --format markdown,links --pretty -o data.json
```

### Comportamiento de los formatos

- **Un solo formato**: Devuelve contenido sin procesar (texto markdown, HTML, etc.)
- **Varios formatos**: Devuelve JSON con todos los datos solicitados

```
# Salida de markdown sin procesar
firecrawl https://example.com --format markdown

# Salida JSON con múltiples formatos
firecrawl https://example.com --format markdown,links
```

## Ejemplos

### Scrape rápido

```
# Obtener contenido markdown de una URL (usar --only-main-content para una salida limpia)
firecrawl https://docs.firecrawl.dev --only-main-content

# Get HTML content
firecrawl https://example.com --html -o page.html
```

### Rastreo completo del sitio web

```
# Rastrear un sitio de documentación con límites
firecrawl crawl https://docs.example.com --limit 50 --max-depth 2 --wait --progress -o docs.json
```

### Descubrimiento de sitios web

```
# Buscar todas las publicaciones del blog
firecrawl map https://example.com --search "blog" -o blog-urls.txt
```

### Flujo de trabajo de investigación

```
# Buscar y extraer resultados para investigación
firecrawl search "machine learning best practices 2024" --scrape --scrape-formats markdown --pretty
```

### Agente

```
# URLs are optional
firecrawl agent "Encuentra las 5 principales startups de IA y sus montos de financiación" --wait

# Focus on specific URLs
firecrawl agent "Compare pricing plans" --urls https://slack.com/pricing,https://teams.microsoft.com/pricing --wait
```

### Automatización del navegador

```
# Launch a session, scrape a page, and close
firecrawl browser launch-session
firecrawl browser execute "open https://news.ycombinator.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "scrape"
firecrawl browser close

# Usar agent-browser mediante modo bash (predeterminado — recomendado para agentes de IA)
firecrawl browser launch-session
firecrawl browser execute "open https://example.com"
firecrawl browser execute "snapshot"
# snapshot returns @ref IDs — use them to interact
firecrawl browser execute "click @e5"
firecrawl browser execute "fill @e3 'search query'"
firecrawl browser execute "scrape"
# Run --help to see all 40+ commands
firecrawl browser execute --bash "agent-browser --help"
firecrawl browser close

# Extract URLs from search results
jq -r '.data.web[].url' search-results.json

# Obtener títulos de resultados de búsqueda
jq -r '.data.web[] | "\(.title): \(.url)"' search-results.json

# Extract links and process with jq
firecrawl https://example.com --format links | jq '.links[].url'

# Count URLs from map
firecrawl map https://example.com | wc -l
```

## Telemetría

La CLI recopila datos de uso anónimos durante la autenticación para ayudar a mejorar el producto:

- Versión de la CLI, sistema operativo y versión de Node.js
- Detección de herramientas de desarrollo (por ejemplo, Cursor, VS Code, Claude Code)

**No se recopilan datos de comandos, URL ni contenido de archivos a través de la CLI.** Para desactivar la telemetría, configura la siguiente variable de entorno:

```
export FIRECRAWL_NO_TELEMETRY=1
```

## Código abierto

La CLI y la Skill de Firecrawl son de código abierto y están disponibles en GitHub: [firecrawl/cli](https://github.com/firecrawl/cli)

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.