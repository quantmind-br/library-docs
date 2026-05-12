---
title: Alojamiento propio | Firecrawl
url: https://docs.firecrawl.dev/es/contributing/self-host
source: sitemap
fetched_at: 2026-03-23T07:30:36.276441-03:00
rendered_js: false
word_count: 964
summary: This document provides guidelines for contributing to the Firecrawl project and instructions for setting up and managing a self-hosted instance using Docker.
tags:
    - self-hosting
    - docker
    - scraping
    - contribution
    - deployment
    - configuration
    - firecrawl
category: guide
---

#### ¿Quieres contribuir?

¡Bienvenido a [Firecrawl](https://firecrawl.dev) 🔥! Aquí tienes instrucciones para obtener el proyecto en local, ejecutarlo por tu cuenta y contribuir. Si vas a contribuir, ten en cuenta que el proceso es similar al de otros repositorios de código abierto: haz un fork de Firecrawl, realiza cambios, ejecuta las pruebas y abre un PR. Si tienes preguntas o necesitas ayuda para empezar, únete a nuestra comunidad de Discord [aquí](https://discord.gg/firecrawl) para más información o crea un issue en GitHub [aquí](https://github.com/firecrawl/firecrawl/issues/new/choose).

## Autohospedar Firecrawl

Consulta [SELF\_HOST.md](https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md) para obtener instrucciones sobre cómo ejecutarlo localmente.

## ¿Por qué?

Alojar Firecrawl por tu cuenta es especialmente útil para organizaciones con políticas de seguridad estrictas que requieren mantener los datos en entornos controlados. Estas son algunas razones clave para considerar el autoalojamiento:

- **Mayor seguridad y cumplimiento:** Al autoalojar, garantizas que el manejo y procesamiento de datos cumplan con normativas internas y externas, manteniendo la información sensible dentro de tu infraestructura segura. Ten en cuenta que Firecrawl es un producto de Mendable y cuenta con certificación SOC 2 Type II, lo que significa que la plataforma cumple con altos estándares del sector para la gestión de la seguridad de los datos.
- **Servicios personalizables:** El autoalojamiento permite adaptar servicios como Playwright a necesidades específicas o a casos de uso particulares que quizá no estén cubiertos por la oferta estándar en la nube.
- **Aprendizaje y contribución a la comunidad:** Al configurar y mantener tu propia instancia, obtienes una comprensión más profunda de cómo funciona Firecrawl, lo que también puede traducirse en contribuciones más valiosas al proyecto.

### Consideraciones

Sin embargo, hay algunas limitaciones y responsabilidades adicionales que debes tener en cuenta:

1. **Acceso limitado a Fire-engine:** Actualmente, las instancias autoalojadas de Firecrawl no tienen acceso a Fire-engine, que incluye funciones avanzadas para manejar bloqueos de IP, mecanismos de detección de bots y más. Esto significa que, aunque puedes gestionar tareas básicas de scraping, los escenarios más complejos podrían requerir configuración adicional o puede que no estén admitidos.
2. **Se requiere configuración manual:** Si necesitas usar métodos de scraping más allá de las opciones básicas de `fetch` y Playwright, deberás configurarlos manualmente en el archivo `.env`. Esto requiere un conocimiento más profundo de las tecnologías y podría implicar más tiempo de configuración.

<!--THE END-->

- Capacidad: Todos los endpoints de la API admitidos — Cloud: Sí — Autoalojado: No siempre; `/agent` y `/browser` no son compatibles en autoalojado
- Capacidad: Compatibilidad con capturas de pantalla — Cloud: Sí — Autoalojado: Sí, cuando el servicio de Playwright está en ejecución
- Capacidad: LLM locales (p. ej., Ollama) — Cloud: No compatible — Autoalojado: Compatible mediante `OLLAMA_BASE_URL` (experimental)

Autoalojar Firecrawl es ideal para quienes necesitan control total sobre sus entornos de scraping y procesamiento de datos, pero conlleva el coste de un mantenimiento y una configuración adicionales.

## Pasos

1. Primero, instala las dependencias

<!--THE END-->

- Docker [instrucciones](https://docs.docker.com/get-docker/)

<!--THE END-->

2. Configura las variables de entorno

Crea un archivo `.env` en el directorio raíz; puedes copiar la plantilla desde `apps/api/.env.example` Para empezar, no configuraremos la autenticación ni ningún servicio opcional (análisis de PDF, bloqueo de JS, funcionalidades de IA)

```
# .env

# ===== Required ENVS ======
PORT=3002
HOST=0.0.0.0

# Note: PORT is used by both the main API server and worker liveness check endpoint

# To turn on DB authentication, you need to set up Supabase.
USE_DB_AUTHENTICATION=false

# ===== Optional ENVS ======

## === AI features (JSON format on scrape, /extract API) ===
# Provide your OpenAI API key here to enable AI features
# OPENAI_API_KEY=

# Experimental: Use Ollama
# OLLAMA_BASE_URL=http://localhost:11434/api
# MODEL_NAME=deepseek-r1:7b
# MODEL_EMBEDDING_NAME=nomic-embed-text

# Experimental: Use any OpenAI-compatible API
# OPENAI_BASE_URL=https://example.com/v1
# OPENAI_API_KEY=

## === Proxy ===
# PROXY_SERVER can be a full URL (e.g. http://0.1.2.3:1234) or just an IP and port combo (e.g. 0.1.2.3:1234)
# Do not uncomment PROXY_USERNAME and PROXY_PASSWORD if your proxy is unauthenticated
# PROXY_SERVER=
# PROXY_USERNAME=
# PROXY_PASSWORD=

## === /search API ===

# Puedes especificar un servidor SearXNG con el formato JSON habilitado, si prefieres usarlo en lugar de Google directo.
# También puedes personalizar los parámetros de engines y categories, pero los valores predeterminados también deberían funcionar bien.
# SEARXNG_ENDPOINT=http://your.searxng.server
# SEARXNG_ENGINES=
# SEARXNG_CATEGORIES=

## === Other ===

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=

# Use if you've set up authentication and want to test with a real API key
# TEST_API_KEY=

# This key lets you access the queue admin panel. Change this if your deployment is publicly accessible.
BULL_AUTH_KEY=CHANGEME

# This is now autoconfigured by the docker-compose.yaml. You shouldn't need to set it.
# PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/scrape
# REDIS_URL=redis://redis:6379
# REDIS_RATE_LIMIT_URL=redis://redis:6379

# Set if you have a llamaparse key you'd like to use to parse pdfs
# LLAMAPARSE_API_KEY=

# Set if you'd like to send server health status messages to Slack
# SLACK_WEBHOOK_URL=

# Set if you'd like to send posthog events like job logs
# POSTHOG_API_KEY=
# POSTHOG_HOST=

## === System Resource Configuration ===
# Maximum CPU usage threshold (0.0-1.0). Worker will reject new jobs when CPU usage exceeds this value.
# Default: 0.8 (80%)
# MAX_CPU=0.8

# Maximum RAM usage threshold (0.0-1.0). Worker will reject new jobs when memory usage exceeds this value.
# Default: 0.8 (80%)
# MAX_RAM=0.8

# Set if you'd like to allow local webhooks to be sent to your self-hosted instance
# ALLOW_LOCAL_WEBHOOKS=true
```

3. *(Opcional) Ejecutar con el servicio de Playwright en TypeScript*
   
   - Actualiza el archivo `docker-compose.yml` para cambiar el servicio de Playwright:
     
     ```
         build: apps/playwright-service
     ```
     
     A
     
     ```
         build: apps/playwright-service-ts
     ```
   - Define `PLAYWRIGHT_MICROSERVICE_URL` en tu archivo `.env`:
     
     ```
     PLAYWRIGHT_MICROSERVICE_URL=http://localhost:3000/scrape
     ```
   - No olvides configurar el servidor proxy en tu archivo `.env` según sea necesario.
4. Compila y ejecuta los contenedores de Docker:
   
   ```
   docker compose build
   docker compose up
   ```

Esto iniciará una instancia local de Firecrawl accesible en `http://localhost:3002`. Deberías poder ver la interfaz de Bull Queue Manager en `http://localhost:3002/admin/{BULL_AUTH_KEY}/queues`.

5. *(Opcional)* Prueba la API

Si quieres probar el endpoint de rastreo, puedes ejecutar lo siguiente:

```
  curl -X POST http://localhost:3002/v2/crawl \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://docs.firecrawl.dev"
      }'
```

## Resolución de problemas

Esta sección ofrece soluciones a problemas comunes que puedes encontrar al configurar o ejecutar tu instancia autohospedada de Firecrawl.

### El cliente de Supabase no está configurado

**Síntoma:**

```
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Se intentó acceder al cliente de Supabase cuando no está configurado.
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Error al insertar el evento de scraping: Error: el cliente de Supabase no está configurado.
```

**Explicación:** Este error ocurre porque la configuración del cliente de Supabase no está completa. Deberías poder hacer scraping y crawling sin problemas. Actualmente no es posible configurar Supabase en instancias autogestionadas.

### Se está omitiendo la autenticación

**Síntoma:**

```
[YYYY-MM-DDTHH:MM:SS.SSSz]WARN - You're bypassing authentication
```

**Explicación:** Este error ocurre porque la configuración del cliente de Supabase no se ha completado. Deberías poder hacer scraping y rastreo sin problemas. Actualmente no es posible configurar Supabase en instancias autoalojadas.

### Los contenedores de Docker no se inician

**Síntoma:** Los contenedores de Docker terminan inesperadamente o fallan al iniciarse. **Solución:** Consulta los registros de Docker para ver si hay mensajes de error usando el comando:

```
docker logs [container_name]
```

- Asegúrate de que todas las variables de entorno necesarias estén definidas correctamente en el archivo .env.
- Verifica que todos los servicios de Docker definidos en docker-compose.yml estén correctamente configurados y que las imágenes necesarias estén disponibles.

### Problemas de conexión con Redis

**Síntoma:** Errores relacionados con la conexión a Redis, como timeouts o “Connection refused”. **Solución:**

- Asegúrate de que el servicio de Redis esté activo y en ejecución en tu entorno Docker.
- Verifica que `REDIS_URL` y `REDIS_RATE_LIMIT_URL` en tu archivo `.env` apunten a la instancia correcta de Redis.
- Revisa la configuración de red y las reglas de firewall que puedan estar bloqueando la conexión al puerto de Redis.

### El punto de conexión de la API no responde

**Síntoma:** Las solicitudes a la API de la instancia de Firecrawl se agotan por tiempo de espera o no devuelven respuesta. **Solución:**

- Asegúrate de que el servicio de Firecrawl esté en ejecución comprobando el estado del contenedor de Docker.
- Verifica que las variables PORT y HOST en tu archivo .env sean correctas y que ningún otro servicio esté usando el mismo puerto.
- Revisa la configuración de red para garantizar que el host sea accesible desde el cliente que realiza la solicitud a la API.

Al resolver estos problemas comunes, podrás lograr una configuración y operación más fluidas de tu instancia autogestionada de Firecrawl.

## Instalar Firecrawl en un clúster de Kubernetes (versión simple)

Consulta el [examples/kubernetes-cluster-install/README.md](https://github.com/firecrawl/firecrawl/tree/main/examples/kubernetes/cluster-install#readme) para ver las instrucciones de instalación de Firecrawl en un clúster de Kubernetes.