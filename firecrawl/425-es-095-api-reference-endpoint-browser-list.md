---
title: Listar sesiones del navegador - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/browser-list
source: sitemap
fetched_at: 2026-03-23T07:25:48.597057-03:00
rendered_js: false
word_count: 151
summary: This document provides the API specification for listing and filtering browser sessions, including available query parameters and the structure of session response objects.
tags:
    - api-reference
    - browser-sessions
    - rest-api
    - firecrawl
    - session-management
category: api
---

[Saltar al contenido principal](#content-area)

Listar sesiones de navegador

CabeceraValor`Authorization``Bearer <API_KEY>`

## Parámetros de consulta

ParámetroTipoRequeridoDescripción`status`stringNoFiltra por el estado de la sesión: `"active"` o `"destroyed"`

## Respuesta

CampoTipoDescripción`success`booleanIndica si la petición se realizó correctamente`sessions`arrayLista de objetos de sesión

### Objeto de sesión

CampoTipoDescripción`id`stringIdentificador único de sesión`status`stringEstado actual de la sesión (`"active"` o `"destroyed"`)`cdpUrl`stringURL de WebSocket para conexiones CDP`liveViewUrl`stringURL para ver la sesión en tiempo real`interactiveLiveViewUrl`stringURL para interactuar con la sesión en tiempo real (hacer clic, escribir, desplazarse)`createdAt`stringMarca de tiempo ISO 8601 de la creación de la sesión`lastActivity`stringMarca de tiempo ISO 8601 de la última actividad

### Ejemplo de solicitud

```
curl -X GET "https://api.firecrawl.dev/v2/browser?status=active" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```

### Ejemplo de respuesta

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
      "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true",
      "createdAt": "2025-06-01T12:00:00Z",
      "lastActivity": "2025-06-01T12:05:30Z"
    }
  ]
}
```

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de consulta

Filtrar sesiones por estado

Opciones disponibles:

`active`,

`destroyed`

#### Respuesta

Lista de sesiones del navegador