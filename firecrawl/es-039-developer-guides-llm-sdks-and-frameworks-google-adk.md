---
title: Kit de desarrollo de agentes (ADK) - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/llm-sdks-and-frameworks/google-adk
source: sitemap
fetched_at: 2026-03-23T07:36:11.097542-03:00
rendered_js: false
word_count: 421
summary: This document provides instructions on integrating the Firecrawl MCP server with the Google Agent Development Kit (ADK) to enable web scraping and data extraction capabilities for AI agents.
tags:
    - firecrawl
    - mcp
    - google-adk
    - web-scraping
    - ai-agents
    - data-extraction
    - api-integration
category: guide
---

Integra Firecrawl con el Kit de desarrollo de agentes (ADK) de Google para crear agentes de IA potentes con capacidades de web scraping mediante el Model Context Protocol (MCP).

## Descripción general

Firecrawl ofrece un servidor MCP que se integra sin fricciones con el ADK de Google, permitiendo que tus agentes realicen scraping, crawling y extracción de datos estructurados de cualquier sitio web de manera eficiente. La integración es compatible tanto con instancias de Firecrawl en la nube como autogestionadas, con HTTP en streaming para un rendimiento óptimo.

## Funcionalidades

- Raspado web, rastreo y descubrimiento de contenido eficientes en cualquier sitio
- Búsqueda avanzada y extracción inteligente de contenido
- Investigación profunda y scraping por lotes a gran escala
- Despliegue flexible (en la nube o autogestionado)
- Optimizado para entornos web modernos con soporte HTTP por streaming

## Requisitos previos

- Obtén una clave de API para Firecrawl en [firecrawl.dev](https://firecrawl.dev)
- Instala el Google SDK

## Configuración

HerramientaNombreDescripciónHerramienta de scraping`firecrawl_scrape`Extrae contenido de una única URL con opciones avanzadasHerramienta de scraping por lotes`firecrawl_batch_scrape`Extrae múltiples URL de forma eficiente con limitación de tasa integrada y procesamiento en paraleloConsultar estado del lote`firecrawl_check_batch_status`Consulta el estado de una operación por lotesHerramienta de mapeo`firecrawl_map`Genera el mapa de un sitio para descubrir todas las URL indexadasHerramienta de búsqueda`firecrawl_search`Busca en la web y, opcionalmente, extrae contenido de los resultadosHerramienta de rastreo`firecrawl_crawl`Inicia un rastreo asíncrono con opciones avanzadasConsultar estado del rastreo`firecrawl_check_crawl_status`Consulta el estado de un trabajo de rastreoHerramienta de extracción`firecrawl_extract`Extrae información estructurada de páginas web usando capacidades de LLM

## Configuración

### Configuración requerida

**FIRECRAWL\_API\_KEY**: Tu clave de API de Firecrawl

- Obligatorio al usar la API en la nube (por defecto)
- Opcional al usar una instancia autogestionada con FIRECRAWL\_API\_URL

### Configuración opcional

**URL de la API de Firecrawl (para instancias autohospedadas)**:

- `FIRECRAWL_API_URL`: Endpoint de API personalizado
- Ejemplo: `https://firecrawl.your-domain.com`
- Si no se especifica, se usará la API en la nube

**Configuración de reintentos**:

- `FIRECRAWL_RETRY_MAX_ATTEMPTS`: Número máximo de reintentos (predeterminado: 3)
- `FIRECRAWL_RETRY_INITIAL_DELAY`: Espera inicial en milisegundos (predeterminado: 1000)
- `FIRECRAWL_RETRY_MAX_DELAY`: Espera máxima en milisegundos (predeterminado: 10000)
- `FIRECRAWL_RETRY_BACKOFF_FACTOR`: Multiplicador de backoff exponencial (predeterminado: 2)

**Monitoreo del uso de créditos**:

- `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: Umbral de advertencia (predeterminado: 1000)
- `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: Umbral crítico (predeterminado: 100)

## Ejemplo: agente de investigación web

```
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

FIRECRAWL_API_KEY = "YOUR-API-KEY"

# Crear un agente de investigación
research_agent = Agent(
    model="gemini-2.5-pro",
    name="research_agent",
    description='Un agente de IA que investiga temas mediante scraping y análisis de contenido web',
    instruction='''Eres un asistente de investigación. Cuando recibas un tema o pregunta:
    1. Usa la herramienta de búsqueda para encontrar sitios web relevantes
    2. Haz scraping de las páginas más relevantes para obtener información detallada
    3. Extrae datos estructurados cuando sea necesario
    4. Proporciona respuestas completas y bien fundamentadas''',
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=f"https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp",
            ),
        )
    ],
)

# Usar el agente
response = research_agent.run("¿Cuáles son las últimas características de Python 3.13?")
print(response)
```

## Mejores prácticas

1. **Usa la herramienta adecuada para cada tarea**:
   
   - `firecrawl_search` cuando primero necesites encontrar páginas relevantes
   - `firecrawl_scrape` para páginas individuales
   - `firecrawl_batch_scrape` para varias URL conocidas
   - `firecrawl_crawl` para descubrir y extraer sitios completos
2. **Supervisa tu uso**: Configura umbrales de consumo de créditos para evitar usos inesperados
3. **Gestiona los errores de forma adecuada**: Configura los reintentos según tu caso de uso
4. **Optimiza el rendimiento**: Usa operaciones por lotes al extraer varias URL

* * *