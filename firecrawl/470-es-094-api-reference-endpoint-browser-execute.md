---
title: Ejecutar código en el navegador - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/browser-execute
source: sitemap
fetched_at: 2026-03-23T07:26:06.433871-03:00
rendered_js: false
word_count: 256
summary: This document provides the technical specification for an API endpoint designed to execute custom code within an isolated browser session.
tags:
    - api-reference
    - browser-automation
    - code-execution
    - http-requests
    - sandboxed-environment
category: api
---

[Saltar al contenido principal](#content-area)

Ejecutar código en una sesión de navegador

CabeceraValor`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Cuerpo de la solicitud

ParámetroTipoObligatorioPredeterminadoDescripción`code`stringSí-Código a ejecutar (1-100,000 caracteres)`language`stringNo`"node"`Idioma del código: `"python"`, `"node"` o `"bash"` (para comandos CLI de agent-browser)`timeout`numberNo-Tiempo máximo de ejecución en segundos (1-300)

## Respuesta

CampoTipoDescripción`success`booleanIndica si el código se ejecutó correctamente`stdout`stringSalida estándar de la ejecución del código`result`stringResultado estándar de la ejecución del código`stderr`stringSalida de error estándar de la ejecución del código`exitCode`numberCódigo de salida del proceso ejecutado`killed`booleanIndica si el proceso se terminó por exceder el tiempo de espera`error`stringMensaje de error si la ejecución falló (solo presente en caso de error)

### Ejemplo de solicitud

```
curl -X POST "https://api.firecrawl.dev/v2/browser/550e8400-e29b-41d4-a716-446655440000/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "await page.goto(\"https://example.com\")\ntitle = await page.title()\nprint(title)",
    "language": "python"
  }'
```

### Ejemplo de respuesta (Éxito)

```
{
  "success": true,
  "result": "Example Domain"
}
```

### Ejemplo de respuesta (error)

```
{
  "success": true,
  "error": "TimeoutError: page.goto: Timeout 30000ms exceeded."
}
```

> ¿Eres un agente de IA que necesita una clave de la API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

ID de la sesión del navegador

#### Cuerpo

Código que se ejecutará en el entorno aislado del navegador

Required string length: `1 - 100000`

language

enum&lt;string&gt;

predeterminado:node

Lenguaje del código que se va a ejecutar. Usa `node` para JavaScript o `bash` para comandos CLI de agent-browser.

Opciones disponibles:

`python`,

`node`,

`bash`

Tiempo máximo de ejecución en segundos

Rango requerido: `1 <= x <= 300`

#### Respuesta

Código ejecutado con éxito

Salida estándar de la ejecución del código

Salida de error estándar de la ejecución del código

Código de salida del proceso ejecutado

Indica si el proceso terminó por tiempo de espera (timeout)

Mensaje de error si el código generó una excepción