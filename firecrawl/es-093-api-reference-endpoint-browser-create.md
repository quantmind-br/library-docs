---
title: Crear sesión de navegador - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/browser-create
source: sitemap
fetched_at: 2026-03-23T07:25:58.680961-03:00
rendered_js: false
word_count: 313
summary: This document provides the API specifications for creating a managed browser session, including configuration parameters for session duration, inactivity timeouts, and persistent storage profiles.
tags:
    - api-reference
    - browser-automation
    - session-management
    - http-request
    - web-scraping
category: api
---

[Saltar al contenido principal](#content-area)

Crear una sesión de navegador

CabeceraValor`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Cuerpo de la solicitud

ParámetroTipoObligatorioValor predeterminadoDescripción`ttl`numberNo600Duración total de la sesión en segundos (30-3600)`activityTtl`numberNo300Segundos de inactividad antes de que la sesión se elimine (10-3600)`profile`objectNo—Habilita el almacenamiento persistente entre sesiones. Consulta más abajo.`profile.name`stringSí\*—Nombre del perfil (1-128 caracteres). Las sesiones con el mismo nombre comparten almacenamiento.`profile.saveChanges`booleanNo`true`Cuando es `true`, el estado del navegador se guarda de nuevo en el perfil al cerrar. Establécelo en `false` para cargar los datos existentes sin escribir. Solo se permite un proceso de guardado a la vez.

## Respuesta

CampoTipoDescripción`success`booleanIndica si se creó la sesión`id`stringIdentificador único de la sesión`cdpUrl`stringURL de WebSocket para conexiones CDP`liveViewUrl`stringURL para ver la sesión en tiempo real`interactiveLiveViewUrl`stringURL para interactuar con la sesión en tiempo real (hacer clic, escribir, desplazarse)`expiresAt`stringMomento en que la sesión expirará según el TTL

### Ejemplo de solicitud

```
curl -X POST "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "ttl": 120
  }'
```

### Ejemplo de respuesta

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true"
}
```

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automática.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Cuerpo

ttl

integer

predeterminado:300

Tiempo de vida total de la sesión de navegador, en segundos

Rango requerido: `30 <= x <= 3600`

Tiempo en segundos antes de que la sesión se destruya por inactividad

Rango requerido: `10 <= x <= 3600`

streamWebView

boolean

predeterminado:true

Indica si se debe transmitir una vista en tiempo real del navegador

Habilita el almacenamiento de datos persistente entre sesiones del navegador. Los datos guardados en una sesión se pueden volver a cargar en una sesión posterior usando el mismo nombre.

#### Respuesta

Sesión de navegador creada correctamente

Identificador único de la sesión

URL de WebSocket para acceder al protocolo Chrome DevTools

URL para visualizar la sesión del navegador en tiempo real

URL para interactuar en tiempo real con la sesión del navegador (clics, escritura, desplazamiento)

Momento en que la sesión expirará según el TTL