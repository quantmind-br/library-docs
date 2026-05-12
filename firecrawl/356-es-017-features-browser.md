---
title: Navegador | Firecrawl
url: https://docs.firecrawl.dev/es/features/browser
source: sitemap
fetched_at: 2026-03-23T07:25:24.325213-03:00
rendered_js: false
word_count: 1009
summary: Firecrawl Browser Sandbox provides a secure, managed environment for AI agents to interact with the web using pre-installed tools like Playwright and agent-browser without local infrastructure setup.
tags:
    - browser-automation
    - ai-agents
    - headless-browser
    - playwright
    - web-scraping
    - sandbox-environment
    - api-integration
category: guide
---

Firecrawl Browser Sandbox ofrece a tus agentes un entorno de navegador seguro donde pueden interactuar con la web. Completa formularios, haz clic en botones, autentícate y mucho más. Sin configuración local, sin instalaciones de Chromium, sin problemas de compatibilidad de controladores. Agent Browser y Playwright ya vienen preinstalados. Disponible a través de [API](https://docs.firecrawl.dev/es/api-reference/endpoint/browser-create), [CLI](https://docs.firecrawl.dev/es/sdks/cli#browser) (Bash / agent-browser, Python, Node), [Node SDK](https://docs.firecrawl.dev/es/sdks/node#browser), [Python SDK](https://docs.firecrawl.dev/es/sdks/python#browser), [Vercel AI SDK](https://docs.firecrawl.dev/es/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk) y [MCP Server](https://docs.firecrawl.dev/es/mcp-server). Para añadir compatibilidad con navegador a un agente de programación de IA (Claude Code, Codex, Open Code, Cursor, etc.), instala la skill de Firecrawl:

```
npx -y firecrawl-cli@latest init --all --browser
```

Cada sesión se ejecuta en un sandbox aislado, desechable o persistente, que escala sin necesidad de gestionar infraestructura.

## Inicio rápido

Crea una sesión, ejecuta código y ciérrala:

- **Sin instalación de controladores** - Sin binario de Chromium, sin `playwright install`, sin problemas de compatibilidad de controladores
- **Python, JavaScript y Bash** - Envía código vía API, CLI o SDK y recibe los resultados. Los tres lenguajes se ejecutan de forma remota en el sandbox
- **agent-browser** - CLI preinstalada con más de 60 comandos. Los agentes de IA escriben comandos bash simples en lugar de código de Playwright
- **Playwright disponible** - Playwright viene preinstalado en el sandbox. Los agentes pueden escribir código con Playwright si lo prefieren.
- **Acceso CDP** - Conecta tu propia instancia de Playwright por WebSocket cuando necesites control completo
- **Vista en vivo** - Mira las sesiones en tiempo real mediante una URL de streaming integrable
- **Vista en vivo interactiva** - Permite que los usuarios interactúen directamente con el navegador a través de un stream interactivo integrable

## Iniciar una sesión

Devuelve un ID de sesión, una URL de CDP y una URL de vista en tiempo real.

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}
```

## Ejecutar código

Ejecuta código de Python, JavaScript o bash en tu sesión. La salida se devuelve a través de `stdout`; para Node.js, el valor de la última expresión también está disponible en `result`.

```
{
  "success": true,
  "stdout": "",
  "result": "Example Domain",
  "stderr": "",
  "exitCode": 0,
  "killed": false
}
```

### Gestión de descargas de archivos

Los archivos descargados dentro de una sesión se pueden capturar y devolver como base64. Usa la API de descargas de Playwright mediante el endpoint `execute`:

## agent-browser (Modo Bash)

[agent-browser](https://github.com/vercel-labs/agent-browser) es una CLI de navegador headless preinstalada en cada sandbox. En lugar de escribir código de Playwright, los agentes envían comandos de bash sencillos. La CLI inyecta automáticamente `--cdp` para que agent-browser se conecte a tu sesión activa.

### Atajo

La forma más rápida de usar `browser`. Tanto el atajo como `execute` envían comandos a `agent-browser` automáticamente. El atajo simplemente omite `execute` y abre una sesión automáticamente si es necesario:

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
firecrawl browser "click @e5"
```

### CLI

La forma explícita usa `execute`. Los comandos se envían automáticamente a agent-browser; no necesitas escribir `agent-browser` ni usar `--bash`:

### API y SDK

Utiliza `language: "bash"` para ejecutar comandos de agent-browser a través de la API o los SDK:

## Gestión de sesiones

### Sesiones persistentes

De forma predeterminada, cada sesión de navegador comienza desde cero. Con `profile`, puedes guardar el estado del navegador entre sesiones. Esto es útil para seguir conectado y mantener tus preferencias. Para guardar o seleccionar un perfil, usa el parámetro `profile` al crear una sesión.

ParámetroPredeterminadoDescripción`name`—Un nombre para el perfil persistente. Las sesiones con el mismo nombre comparten el almacenamiento.`saveChanges``true`Cuando es `true`, el estado del navegador se guarda de nuevo en el perfil al cerrarse. Establécelo en `false` para cargar datos existentes sin escribir, útil cuando necesitas varios lectores concurrentes.

El estado de la sesión del navegador solo se guarda cuando la sesión se cierra. Por ello, recomendamos cerrar la sesión de navegador cuando termines de usarla para que pueda reutilizarse. Una vez cerrada una sesión, su ID de sesión deja de ser válido; no puedes reutilizarlo. En su lugar, crea una nueva sesión con el mismo nombre de perfil y usa el nuevo ID de sesión devuelto en la respuesta. Para guardarla y cerrarla:

### Listar sesiones

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
      "liveViewUrl": "https://liveview.firecrawl.dev/...",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
      "createdAt": "2025-01-15T10:30:00Z",
      "lastActivity": "2025-01-15T10:35:00Z"
    }
  ]
}
```

### Configuración de TTL

Las sesiones tienen dos controles de TTL:

ParámetroPredeterminadoDescripción`ttl`600s (10 min)Vida útil máxima de la sesión (30-3600s)`activityTtl`300s (5 min)Cierre automático tras inactividad (10-3600s)

### Cerrar una sesión

## Vista en vivo

Cada sesión devuelve un `liveViewUrl` en la respuesta que puedes insertar para ver el navegador en tiempo real. Resulta útil para depuración, demostraciones o para crear interfaces de usuario basadas en el navegador.

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}

<iframe src="LIVE_VIEW_URL" width="100%" height="600" />
```

### Vista interactiva en vivo

La respuesta también incluye un `interactiveLiveViewUrl`. A diferencia de la vista en vivo estándar, que solo permite observar, la vista interactiva en vivo permite a los usuarios hacer clic, escribir e interactuar con la sesión del navegador directamente a través de la transmisión incrustada. Esto es útil para crear interfaces de navegador orientadas al usuario, depuración colaborativa o cualquier escenario en el que quien la visualiza necesite controlar el navegador.

```
<iframe src="INTERACTIVE_LIVE_VIEW_URL" width="100%" height="600" />
```

Cada sesión expone una URL de WebSocket de CDP. La API execute y la bandera `--bash` cubren la mayoría de los casos de uso, pero si necesitas control local completo puedes conectarte directamente.

## Cuándo usar navegador

Caso de usoHerramienta adecuadaExtraer contenido de una URL conocida[Scrape](https://docs.firecrawl.dev/es/features/scrape)Buscar en la web y obtener resultados[Search](https://docs.firecrawl.dev/es/features/search)Gestionar la paginación, completar formularios y hacer clic en flujos**navegador**Flujos de trabajo multietapa con interacción**navegador**Navegación en paralelo en muchos sitios**navegador** (cada sesión está aislada)

## Casos de uso

- **Inteligencia competitiva** - Explorar sitios de la competencia, navegar por formularios de búsqueda y filtros, y extraer precios y características en datos estructurados
- **Ingesta de base de conocimientos** - Navegar por centros de ayuda, documentación y portales de soporte que requieren clics, paginación o autenticación
- **Investigación de mercado** - Iniciar sesiones de navegador en paralelo para crear conjuntos de datos a partir de bolsas de trabajo, listados inmobiliarios o bases de datos legales

## Precios

El precio es sencillo: 2 créditos por minuto de navegador. Los usuarios del plan gratuito disponen de 5 horas de uso sin coste.

## Límites de uso

En el lanzamiento inicial, permitimos hasta 20 sesiones simultáneas de navegador en todos los planes.

## Referencia de la API

- [Crear sesión de navegador](https://docs.firecrawl.dev/es/api-reference/endpoint/browser-create)
- [Ejecutar código en el navegador](https://docs.firecrawl.dev/es/api-reference/endpoint/browser-execute)
- [Listar sesiones de navegador](https://docs.firecrawl.dev/es/api-reference/endpoint/browser-list)
- [Eliminar sesión de navegador](https://docs.firecrawl.dev/es/api-reference/endpoint/browser-delete)

* * *

¿Tienes comentarios o necesitas ayuda? Escríbenos a [help@firecrawl.com](mailto:help@firecrawl.com) o contáctanos por [Discord](https://discord.gg/firecrawl).

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.