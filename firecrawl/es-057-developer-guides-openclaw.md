---
title: Uso de OpenClaw con Firecrawl
url: https://docs.firecrawl.dev/es/developer-guides/openclaw
source: sitemap
fetched_at: 2026-03-23T07:33:47.896484-03:00
rendered_js: false
word_count: 381
summary: This document explains how to integrate Firecrawl with OpenClaw to enable web scraping, searching, and browser automation capabilities for AI agents through a secure, sandbox-based CLI.
tags:
    - web-scraping
    - ai-agents
    - browser-automation
    - firecrawl
    - openclaw
    - command-line-interface
    - sandbox-environment
category: guide
---

Integra Firecrawl con OpenClaw para darles a tus agentes la capacidad de realizar scraping, búsquedas, rastreo, extracción e interactuar con la web, todo a través de la [Firecrawl CLI](https://docs.firecrawl.dev/es/sdks/cli).

- **No necesitas un navegador local** — cada sesión se ejecuta en un sandbox remoto y aislado. Sin instalaciones de Chromium, sin conflictos de controladores, sin presión de RAM en tu máquina.
- **Paralelismo real** — ejecuta muchas sesiones de navegador a la vez sin contención por recursos locales. Los agentes pueden navegar en lotes a través de varios sitios simultáneamente.
- **Seguro por defecto** — la navegación, la evaluación del DOM y la extracción suceden dentro de sandboxes desechables, no en tu estación de trabajo.
- **Mejor eficiencia en el uso de tokens** — los agentes reciben artefactos limpios (snapshots, campos extraídos) en lugar de arrastrar DOMs gigantes y logs de controladores dentro de la ventana de contexto.
- **Kit completo para la web** — scraping, búsqueda y automatización del navegador, todo a través de una sola CLI que tu agente ya sabe usar.

## Configuración

Indica a tu agente que instale la CLI de Firecrawl, se autentique e inicialice la habilidad con este comando:

```
npx -y firecrawl-cli init --browser --all
```

- `--all` instala la habilidad de Firecrawl en todos los agentes de programación con IA detectados
- `--browser` abre el navegador automáticamente para la autenticación de Firecrawl

o instala todo por separado:

```
npm install -g firecrawl-cli
firecrawl init skills
firecrawl login --browser
# O bien, omite el navegador y proporciona tu clave de API directamente:
export FIRECRAWL_API_KEY="fc-YOUR-API-KEY"
```

Comprueba que todo esté configurado correctamente:

## Scrape

Extrae el contenido de una sola página:

```
firecrawl https://example.com --only-main-content
```

Obtener formatos específicos:

```
firecrawl https://example.com --format markdown,links --pretty
```

## Búsqueda

Busca en la web y, opcionalmente, realiza scraping de los resultados:

```
firecrawl search "latest AI funding rounds 2025" --limit 10

# Buscar y extraer los resultados
firecrawl search "OpenClaw documentation" --scrape --scrape-formats markdown
```

## Navegador

Inicia una sesión remota de navegador para automatización interactiva. Cada sesión se ejecuta en un sandbox aislado: no necesitas tener Chromium instalado localmente. `agent-browser` ya viene preinstalado con más de 40 comandos.

```
# Forma abreviada: inicia automáticamente una sesión si no hay ninguna activa
firecrawl browser "open https://news.ycombinator.com"
firecrawl browser "snapshot"
firecrawl browser "scrape"
firecrawl browser close
```

Interactúa con elementos de la página usando refs de la instantánea:

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
# snapshot devuelve IDs @ref — úsalos para interactuar
firecrawl browser "click @e5"
firecrawl browser "fill @e3 'search query'"
firecrawl browser "scrape"
firecrawl browser close
```

## Ejemplo: dile a tu agente

Aquí tienes algunos prompts que puedes darle a tu agente de OpenClaw:

- *“Usa Firecrawl para hacer scraping de [https://example.com](https://example.com) y resume el contenido principal.”*
- *“Busca las últimas noticias de OpenAI y dame un resumen de los 5 mejores resultados.”*
- *“Usa Firecrawl Browser para abrir Hacker News, obtener las 5 principales publicaciones y los primeros 10 comentarios de cada una.”*
- *“Rastrea la documentación en [https://docs.firecrawl.dev](https://docs.firecrawl.dev) y guárdala en un archivo.”*

## Lecturas adicionales

- [Referencia de la CLI de Firecrawl](https://docs.firecrawl.dev/es/sdks/cli)
- [Documentación de Browser Sandbox](https://docs.firecrawl.dev/es/features/browser)
- [Documentación de Agent](https://docs.firecrawl.dev/es/features/agent)