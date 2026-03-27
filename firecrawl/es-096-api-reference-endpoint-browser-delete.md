---
title: Eliminar sesión del navegador - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/browser-delete
source: sitemap
fetched_at: 2026-03-23T07:25:52.223433-03:00
rendered_js: false
word_count: 106
summary: This document provides the API specification for terminating a browser session by sending a delete request with the session ID.
tags:
    - api-reference
    - browser-session
    - session-management
    - firecrawl-api
    - delete-request
category: api
---

[Saltar al contenido principal](#content-area)

Eliminar una sesión de navegador

CabeceraValor`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Cuerpo de la solicitud

ParámetroTipoObligatorioDescripción`id`stringSíEl ID de sesión que se va a eliminar

## Respuesta

CampoTipoDescripción`success`booleanIndica si la sesión se destruyó correctamente

### Ejemplo de solicitud

```
curl -X DELETE "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }'
```

### Ejemplo de respuesta

> ¿Eres un agente de IA que necesita una clave de la API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

ID de la sesión del navegador

#### Respuesta

Se eliminó correctamente la sesión del navegador

Duración total de la sesión en milisegundos

Cantidad de créditos facturados por la sesión