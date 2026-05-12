---
title: SDK de Python | Firecrawl
url: https://docs.firecrawl.dev/es/sdks/python
source: sitemap
fetched_at: 2026-03-23T07:24:57.473348-03:00
rendered_js: false
word_count: 804
summary: This document provides a comprehensive guide on installing and using the Firecrawl Python SDK to scrape, crawl, and map websites, including advanced features like pagination control and asynchronous monitoring.
tags:
    - python-sdk
    - web-scraping
    - web-crawling
    - data-extraction
    - api-integration
    - pagination
category: guide
---

## Instalación

Para instalar el SDK de Python de Firecrawl, puedes usar pip:

```
# pip install firecrawl-py

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-TU-API-KEY")
```

## Uso

1. Obtén una clave de API en [firecrawl.dev](https://firecrawl.dev)
2. Define la clave de API como una variable de entorno llamada `FIRECRAWL_API_KEY` o pásala como parámetro a la clase `Firecrawl`.

Aquí tienes un ejemplo de cómo usar el SDK:

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# Extraer datos de un sitio web:
scrape_status = firecrawl.scrape(
  'https://firecrawl.dev', 
  formats=['markdown', 'html']
)
print(scrape_status)

# Rastrear un sitio web:
crawl_status = firecrawl.crawl(
  'https://firecrawl.dev', 
  limit=100, 
  scrape_options={
    'formats': ['markdown', 'html']
  }
)
print(crawl_status)
```

Para extraer una sola URL, usa el método `scrape`. Recibe la URL como parámetro y devuelve el documento extraído.

```
# Extraer un sitio web:
scrape_result = firecrawl.scrape('firecrawl.dev', formats=['markdown', 'html'])
print(scrape_result)
```

### Rastrear un sitio web

Para rastrear un sitio web, usa el método `crawl`. Recibe la URL inicial y opciones opcionales como argumentos. Estas opciones te permiten definir ajustes adicionales para el trabajo de rastreo, como el número máximo de páginas a rastrear, los dominios permitidos y el formato de salida. Consulta [Paginación](#pagination) para la paginación automática/manual y los límites.

```
job = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=5, poll_interval=1, timeout=120)
print(job)
```

### Rastreo solo del sitemap

Usa `sitemap="only"` para rastrear únicamente las URLs del sitemap (la URL inicial siempre se incluye y se omite la detección de enlaces HTML).

```
job = firecrawl.crawl(url="https://docs.firecrawl.dev", sitemap="only", limit=25)
print(job.status, len(job.data))
```

### Iniciar un rastreo

Inicia un trabajo sin esperar con `start_crawl`. Devuelve un `ID` de trabajo que puedes usar para consultar el estado. Usa `crawl` cuando quieras un “waiter” que bloquee hasta completarse. Consulta [Paginación](#pagination) para el comportamiento y los límites de paginado.

```
job = firecrawl.start_crawl(url="https://docs.firecrawl.dev", limit=10)
print(job)
```

### Comprobar el estado del rastreo

Para comprobar el estado de un job de rastreo, usa el método `get_crawl_status`. Recibe el ID del job como parámetro y devuelve el estado actual del rastreo.

```
estado = firecrawl.get_crawl_status("<crawl-id>")
print(estado)
```

### Cancelar un rastreo

Para cancelar un trabajo de rastreo, usa el método `cancel_crawl`. Recibe el ID del trabajo iniciado con `start_crawl` como parámetro y devuelve el estado de la cancelación.

```
ok = firecrawl.cancel_crawl("<crawl-id>")
print("Cancelado:", ok)
```

### Mapear un sitio web

Usa `map` para generar una lista de URL de un sitio web. Las opciones te permiten personalizar el proceso de mapeo, como excluir subdominios o aprovechar el sitemap.

```
res = firecrawl.map(url="https://firecrawl.dev", limit=10)
print(res)
```

### Rastreo de un sitio web con WebSockets

Para rastrear un sitio web con WebSockets, inicia el trabajo con `start_crawl` y suscríbete usando el helper `watcher`. Crea un watcher con el ID del trabajo y adjunta handlers (p. ej., para page, completed, failed) antes de llamar a `start()`.

```
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

    # Iniciar un rastreo primero
    started = await firecrawl.start_crawl("https://firecrawl.dev", limit=5)

    # Monitorear actualizaciones (snapshots) hasta estado terminal
    async for snapshot in firecrawl.watcher(started.id, kind="crawl", poll_interval=2, timeout=120):
        if snapshot.status == "completed":
            print("COMPLETADO", snapshot.status)
            for doc in snapshot.data:
                print("DOC", doc.metadata.source_url if doc.metadata else None)
        elif snapshot.status == "failed":
            print("ERROR", snapshot.status)
        else:
            print("ESTADO", snapshot.status, snapshot.completed, "/", snapshot.total)

asyncio.run(main())
```

Los puntos de conexión de Firecrawl para crawl y batch scrape devuelven una URL `next` cuando hay más datos disponibles. El SDK de Python paginá automáticamente por defecto y agrega todos los documentos; en ese caso `next` será `None`. Puedes desactivar la paginación automática o establecer límites para controlar el comportamiento de la paginación.

Utiliza `PaginationConfig` para controlar el comportamiento de la paginación al llamar a `get_crawl_status` o `get_batch_scrape_status`:

```
from firecrawl.v2.types import PaginationConfig
```

OpciónTipoValor predeterminadoDescripción`auto_paginate``bool``True`Cuando es `True`, obtiene automáticamente todas las páginas y agrupa los resultados. Establécelo en `False` para obtener una página a la vez.`max_pages``int``None`Se detiene después de obtener esta cantidad de páginas (solo se aplica cuando `auto_paginate=True`).`max_results``int``None`Se detiene después de recopilar esta cantidad de documentos (solo se aplica cuando `auto_paginate=True`).`max_wait_time``int``None`Se detiene después de esta cantidad de segundos (solo se aplica cuando `auto_paginate=True`).

Cuando `auto_paginate=False`, la respuesta incluye una URL `next` si hay más datos disponibles. Utiliza estos métodos auxiliares para obtener las páginas siguientes:

- **`get_crawl_status_page(next_url)`** - Obtiene la siguiente página de resultados de `crawl` usando la URL opaca `next` de una respuesta anterior.
- **`get_batch_scrape_status_page(next_url)`** - Obtiene la siguiente página de resultados de `batch scrape` usando la URL opaca `next` de una respuesta anterior.

Estos métodos devuelven el mismo tipo de respuesta que la llamada de estado original, incluida una nueva URL `next` si quedan más páginas.

#### Rastreo

Usa el método auxiliar `crawl` para la forma más sencilla, o inicia un job y pagina manualmente.

- Consulta el flujo por defecto en [Rastrear un sitio web](#crawl-a-website).

Inicia un job y luego recupera una página a la vez con `auto_paginate=False`. Usa `get_crawl_status_page` para recuperar las páginas posteriores:

```
crawl_job = client.start_crawl("https://example.com", limit=100)

# Fetch first page
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(auto_paginate=False)
)
print("First page:", len(status.data), "docs")

# Obtener páginas siguientes usando get_crawl_status_page
while status.next:
    status = client.get_crawl_status_page(status.next)
    print("Next page:", len(status.data), "docs")
```

Mantén la paginación automática activada, pero deténla antes con `max_pages`, `max_results` o `max_wait_time`:

```
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=50, max_wait_time=15),
)
print("rastreo limitado:", status.status, "docs:", len(status.data), "siguiente:", status.next)
```

Usa el método de espera `batch_scrape` o inicia un job y pagina manualmente.

- Consulta el flujo por defecto en [Batch Scrape](https://docs.firecrawl.dev/es/features/batch-scrape).

Inicia un trabajo y luego obtén una página a la vez con `auto_paginate=False`. Usa `get_batch_scrape_status_page` para obtener las páginas siguientes:

```
batch_job = client.start_batch_scrape(urls)

# Obtener la primera página
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(auto_paginate=False)
)
print("Primera página:", len(status.data), "docs")

# Obtener las páginas siguientes usando get_batch_scrape_status_page
while status.next:
    status = client.get_batch_scrape_status_page(status.next)
    print("Siguiente página:", len(status.data), "docs")
```

Mantén la paginación automática activada, pero detén antes con `max_pages`, `max_results` o `max_wait_time`:

```
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=100, max_wait_time=20),
)
print("lote limitado:", status.status, "docs:", len(status.data), "siguiente:", status.next)
```

## Manejo de errores

El SDK gestiona los errores que devuelve la API de Firecrawl y genera las excepciones correspondientes. Si se produce un error durante una solicitud, se lanzará una excepción con un mensaje descriptivo.

## Clase asíncrona

Para operaciones asíncronas, utiliza la clase `AsyncFirecrawl`. Sus métodos son equivalentes a los de `Firecrawl`, pero no bloquean el hilo principal.

```
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-TU-API-KEY")

    # Extraer
    doc = await firecrawl.scrape("https://firecrawl.dev", formats=["markdown"])  # type: ignore[arg-type]
    print(doc.get("markdown"))

    # Buscar
    results = await firecrawl.search("firecrawl", limit=2)
    print(results.get("web", []))

    # Rastreo (inicio y estado)
    started = await firecrawl.start_crawl("https://docs.firecrawl.dev", limit=3)
    status = await firecrawl.get_crawl_status(started.id)
    print(status.status)

    # Extracción por lotes (en espera)
    job = await firecrawl.batch_scrape([
        "https://firecrawl.dev",
        "https://docs.firecrawl.dev",
    ], formats=["markdown"], poll_interval=1, timeout=60)
    print(job.status, job.completed, job.total)

asyncio.run(main())
```

## Navegador

Inicia sesiones de navegador en la nube y ejecuta código de forma remota.

### Crear una sesión

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

session = app.browser()
print(session.id)             # ID de sesión
print(session.cdp_url)        # wss://cdp-proxy.firecrawl.dev/cdp/...
print(session.live_view_url)  # https://liveview.firecrawl.dev/...
```

### Ejecutar código

```
result = app.browser_execute(
    session.id,
    code='await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
    language="python",
)
print(result.result)  # "Hacker News"
```

Ejecutar JavaScript en lugar de Python:

```
result = app.browser_execute(
    session.id,
    code='await page.goto("https://example.com"); const t = await page.title(); console.log(t);',
    language="node",
)
```

### Perfiles

Guarda y reutiliza el estado del navegador (cookies, localStorage, etc.) entre sesiones:

```
session = app.browser(
    ttl=600,
    profile={
        "name": "my-profile",
        "save_changes": True,
    },
)
```

### Conectar vía CDP

Para tener control total de Playwright, conéctate directamente mediante la URL de CDP:

```
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(session.cdp_url)
    context = browser.contexts[0]
    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://example.com")
    print(page.title())

    browser.close()
```

### Listar y cerrar sesiones

```
# List active sessions
sessions = app.list_browsers(status="active")
for s in sessions.sessions:
    print(s.id, s.status, s.created_at)

# Close a session
app.delete_browser(session.id)
```

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.