---
title: Ejecución local | Firecrawl
url: https://docs.firecrawl.dev/es/contributing/guide
source: sitemap
fetched_at: 2026-03-23T07:31:55.733601-03:00
rendered_js: false
word_count: 367
summary: Esta guía detalla el proceso para instalar, configurar y ejecutar el servidor de la API de Firecrawl en un entorno de desarrollo local.
tags:
    - firecrawl
    - local-development
    - api-setup
    - docker-configuration
    - environment-variables
    - backend-installation
category: guide
---

Esta guía te explica cómo ejecutar el servidor de la API de Firecrawl en tu máquina local. Sigue estos pasos para configurar el entorno de desarrollo, iniciar los servicios y enviar tu primera solicitud. Si vas a contribuir, el proceso sigue las convenciones estándar de código abierto: haz un fork del repositorio, realiza cambios, ejecuta las pruebas y abre un pull request. Si tienes dudas o necesitas ayuda para comenzar, escribe a [help@firecrawl.com](mailto:help@firecrawl.com) o [abre un issue](https://github.com/mendableai/firecrawl/issues).

## Requisitos previos

Instala lo siguiente antes de continuar:

DependenciaObligatorioGuía de instalaciónNode.jsSí[nodejs.org](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)pnpm (v9+)Sí[pnpm.io](https://pnpm.io/installation)RedisSí[redis.io](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)PostgreSQLSíMediante Docker (ver más abajo) o instalado directamenteDockerOpcionalNecesario para la configuración del contenedor de PostgreSQL

## Configura la base de datos

Necesitas una base de datos PostgreSQL inicializada con el esquema en `apps/nuq-postgres/nuq.sql`. La forma más sencilla es usar la imagen de Docker dentro de `apps/nuq-postgres`. Con Docker en ejecución, construye y arranca el contenedor:

```
docker build -t nuq-postgres apps/nuq-postgres

docker run --name nuqdb \
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  -v nuq-data:/var/lib/postgresql/data \
  -d nuq-postgres
```

## Configurar variables de entorno

Copia la plantilla para crear el archivo `.env` en el directorio `apps/api/`:

```
cp apps/api/.env.example apps/api/.env
```

Para una configuración local mínima sin autenticación ni servicios opcionales (análisis de PDF, bloqueo de JS, funciones de IA), usa la siguiente configuración:

```
# ===== Requerido =====
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0
REDIS_URL=redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379

## Para activar la autenticación de BD, necesitas configurar supabase.
USE_DB_AUTHENTICATION=false

## Conexión PostgreSQL para colas — cambia si las credenciales, el host o la BD difieren
NUQ_DATABASE_URL=postgres://postgres:postgres@localhost:5433/postgres

# ===== Opcional =====
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=
# TEST_API_KEY=               # Configura si habilitaste autenticación y quieres probar con una clave API real
# OPENAI_API_KEY=             # Necesario para funciones que dependen de LLM (generación de texto alternativo de imágenes, etc.)
# BULL_AUTH_KEY=@
# PLAYWRIGHT_MICROSERVICE_URL= # Configura para ejecutar un fallback de Playwright
# LLAMAPARSE_API_KEY=         # Configura para procesar PDFs con LlamaParse
# SLACK_WEBHOOK_URL=          # Configura para enviar mensajes de estado del servidor a Slack
# POSTHOG_API_KEY=            # Configura para enviar eventos de PostHog como registros de trabajos
# POSTHOG_HOST=               # Configura para enviar eventos de PostHog como registros de trabajos
```

## Instala las dependencias

Desde el directorio `apps/api/`, instala los paquetes con pnpm:

## Inicia los servicios

Necesitas tres sesiones de terminal en ejecución simultánea: Redis, el servidor de la API y otra terminal para enviar solicitudes.

### Terminal 1 — Redis

Inicia el servidor de Redis desde cualquier parte del proyecto:

### Terminal 2 — Servidor de la API

Ve a `apps/api/` y inicia el servicio:

Esto inicia el servidor de la API y los workers encargados de procesar las tareas de rastreo.

### Terminal 3 — Enviar una petición de prueba

Verifica que el servidor esté en ejecución mediante una comprobación de estado (health check):

```
curl -X GET http://localhost:3002/test
```

Esto debería devolver `Hello, world!`. Para probar el endpoint de rastreo:

```
curl -X POST http://localhost:3002/v1/crawl \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://mendable.ai"
  }'
```

## Alternativa: Docker Compose

Para una configuración más sencilla, Docker Compose ejecuta todos los servicios (Redis, servidor de la API y workers) con un solo comando.

1. Asegúrate de que Docker y Docker Compose estén instalados.
2. Copia `.env.example` a `.env` en el directorio `apps/api/` y configura las variables según sea necesario.
3. Desde la raíz del proyecto, ejecuta:

Esto inicia todos los servicios automáticamente en la configuración adecuada.

## Ejecutar pruebas

Ejecuta la suite de pruebas con: