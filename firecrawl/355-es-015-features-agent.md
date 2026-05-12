---
title: Agent | Firecrawl
url: https://docs.firecrawl.dev/es/features/agent
source: sitemap
fetched_at: 2026-03-23T07:25:54.149466-03:00
rendered_js: false
word_count: 1215
summary: This document provides a technical overview and guide for using the Firecrawl Agent API, which leverages autonomous web browsing and search to extract structured data from various sources.
tags:
    - web-scraping
    - api-documentation
    - data-extraction
    - autonomous-agents
    - json-schema
    - firecrawl
category: api
---

Firecrawl `/agent` es una API mágica que busca, navega y recopila datos desde la gama más amplia de sitios web, encontrando datos en lugares de difícil acceso y descubriéndolos de formas que ninguna otra API puede. Consigue en pocos minutos lo que a una persona le llevaría muchas horas: recopilación de datos de extremo a extremo, sin necesidad de scripts ni trabajo manual. Tanto si necesitas un solo dato como conjuntos de datos completos a escala, Firecrawl `/agent` trabaja para obtener tus datos. **Piensa en `/agent` como una investigación profunda de datos, ¡estén donde estén!**

Agent se basa en todo lo bueno de `/extract` y lo lleva más allá:

- **No se requieren URL**: Describe lo que necesitas mediante el parámetro `prompt`. Las URL son opcionales
- **Búsqueda profunda en la web**: Busca y navega de forma autónoma, explorando en profundidad los sitios para encontrar tus datos
- **Fiable y preciso**: Funciona con una amplia variedad de consultas y casos de uso
- **Más rápido**: Procesa múltiples fuentes en paralelo para obtener resultados más rápidos

## Uso de `/agent`

El único parámetro obligatorio es `prompt`. Describe simplemente qué datos quieres extraer. Para obtener salida estructurada, proporciona un esquema JSON. Los SDK son compatibles con Pydantic (Python) y Zod (Node) para definiciones de esquemas con tipado seguro:

### Respuesta

```
{
  "success": true,
  "status": "completed",
  "data": {
    "founders": [
      {
        "name": "Eric Ciarla",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      },
      {
        "name": "Nicolas Camara",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      },
      {
        "name": "Caleb Peffer",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      }
    ]
  },
  "expiresAt": "2024-12-15T00:00:00.000Z",
  "creditsUsed": 15
}
```

## Proporcionar URLs (opcional)

Puedes proporcionar URLs opcionalmente para centrar al agente en páginas específicas:

## Estado y finalización de trabajos

Los trabajos de agente se ejecutan de forma asíncrona. Cuando envíes un trabajo, recibirás un ID de trabajo que podrás usar para comprobar su estado:

- **Método predeterminado**: `agent()` espera y devuelve los resultados finales
- **Iniciar y luego consultar**: Usa `start_agent` (Python) o `startAgent` (Node) para obtener un ID de trabajo de inmediato y luego consulta su estado con `get_agent_status` / `getAgentStatus`

### Posibles estados

EstadoDescripción`processing`El agente todavía está trabajando en tu solicitud`completed`La extracción finalizó correctamente`failed`Se produjo un error durante la extracción`cancelled`El trabajo fue cancelado por el usuario

#### Ejemplo en estado pendiente

```
{
  "success": true,
  "status": "processing",
  "expiresAt": "2024-12-15T00:00:00.000Z"
}
```

#### Ejemplo completado

```
{
  "success": true,
  "status": "completed",
  "data": {
    "founders": [
      {
        "name": "Eric Ciarla",
        "role": "Co-founder"
      },
      {
        "name": "Nicolas Camara",
        "role": "Co-founder"
      },
      {
        "name": "Caleb Peffer",
        "role": "Co-founder"
      }
    ]
  },
  "expiresAt": "2024-12-15T00:00:00.000Z",
  "creditsUsed": 15
}
```

Puedes compartir ejecuciones del agente directamente desde el Agent Playground. Los enlaces compartidos son públicos: cualquier persona que tenga el enlace puede ver la salida y la actividad de la ejecución, y puedes revocar el acceso en cualquier momento para desactivar el enlace. Los motores de búsqueda no indexan las páginas compartidas.

## Selección de modelo

Firecrawl Agent ofrece dos modelos. **Spark 1 Mini es un 60% más barato** y es el modelo predeterminado — perfecto para la mayoría de los casos de uso. Pásate a Spark 1 Pro cuando necesites la máxima precisión en tareas complejas.

ModeloCostePrecisiónIdeal para`spark-1-mini`**60% más barato**EstándarLa mayoría de las tareas (predeterminado)`spark-1-pro`EstándarMayorInvestigación compleja, extracción crítica

### Spark 1 Mini (predeterminado)

`spark-1-mini` es nuestro modelo eficiente, ideal para tareas sencillas de extracción de datos. **Usa Mini cuando:**

- Necesites extraer datos simples (información de contacto, precios, etc.)
- Trabajes con sitios web bien estructurados
- La eficiencia de costos sea una prioridad
- Debas ejecutar trabajos de extracción de alto volumen

### Spark 1 Pro

`spark-1-pro` es nuestro modelo insignia, diseñado para lograr la máxima precisión en tareas de extracción complejas. **Usa Pro cuando:**

- Realices análisis de la competencia complejos
- Extraigas datos que requieran razonamiento profundo
- La precisión sea crítica para tu caso de uso
- Trates con datos ambiguos o difíciles de encontrar

### Especificar un modelo

Pasa el parámetro `model` para seleccionar el modelo que quieres usar:

## Parámetros

ParámetroTipoObligatorioDescripción`prompt`string**Sí**Descripción en lenguaje natural de los datos que deseas extraer (máx. 10.000 caracteres)`model`stringNoModelo a utilizar: `spark-1-mini` (predeterminado) o `spark-1-pro``urls`arrayNoLista opcional de URLs en las que centrar la extracción`schema`objectNoEsquema JSON opcional para una salida estructurada`maxCredits`numberNoNúmero máximo de créditos que se pueden usar en esta tarea del agente. De forma predeterminada es **2,500** si no se especifica. El panel de control admite valores de hasta **2,500**; para límites superiores, configura `maxCredits` mediante la API (los valores por encima de 2,500 siempre se tratan como solicitudes de pago). Si se alcanza el límite, la tarea falla y **no se devuelve ningún dato**, aunque los créditos consumidos por el trabajo realizado se siguen cobrando.

CaracterísticaAgent (nuevo)ExtractURLs necesariasNoSíVelocidadMás rápidaEstándarCostoMás bajoEstándarFiabilidadMás altaEstándarFlexibilidad de las consultasAltaModerada

## Ejemplos de casos de uso

- **Investigación**: “Encuentra las 5 principales startups de IA y sus montos de financiación”
- **Análisis de la competencia**: “Compara los planes de precios entre Slack y Microsoft Teams”
- **Recopilación de datos**: “Extrae información de contacto de sitios web de empresas”
- **Resumen de contenido**: “Resume las últimas entradas de blog sobre web scraping”

## Carga de archivos CSV en Agent Playground

El [Agent Playground](https://www.firecrawl.dev/app/agent) admite la carga de archivos CSV para el procesamiento por lotes. Tu CSV puede contener una o más columnas de datos de entrada. Por ejemplo, una sola columna con nombres de empresas, o varias columnas como nombre de la empresa, producto y URL del sitio web. Cada fila representa un elemento que el agente debe procesar. Sube tu CSV, escribe un prompt que describa qué datos quieres que el agente obtenga para cada fila, define tus campos de salida y ejecútalo. El agente procesa cada fila en paralelo y completa los resultados.

## Referencia de la API

Consulta la [Agent API Reference](https://docs.firecrawl.dev/es/api-reference/endpoint/agent) para más detalles. ¿Tienes comentarios o necesitas ayuda? Escríbenos a [help@firecrawl.com](mailto:help@firecrawl.com).

## Precios

Firecrawl Agent usa **facturación dinámica** que se ajusta a la complejidad de tu solicitud de extracción de datos. Pagas según el trabajo real que realiza Agent, lo que garantiza un precio justo tanto si estás extrayendo datos simples como información estructurada compleja de múltiples fuentes.

### Cómo funcionan los precios de Agent

Los precios de Agent son **dinámicos y basados en créditos** durante la Research Preview:

- **Extracciones simples** (como obtener información de contacto de una sola página) suelen usar menos créditos y cuestan menos
- **Tareas de investigación complejas** (como análisis de la competencia en múltiples dominios) usan más créditos, pero reflejan el esfuerzo total involucrado
- **Uso transparente** te muestra exactamente cuántos créditos consumió cada solicitud
- **Conversión de créditos** convierte automáticamente el uso de créditos del agente en créditos para una facturación sencilla

### Precios de agentes en paralelo

Si estás ejecutando varios agentes en paralelo con Spark-1 Fast, el precio es mucho más predecible: 10 créditos por celda.

### Primeros pasos

**Todos los usuarios** reciben **5 ejecuciones gratuitas al día**, que pueden utilizarse tanto desde el playground como desde la API, para explorar las capacidades de Agent sin costo. El uso adicional se cobra en función del consumo de créditos y se convierte en créditos.

### Gestión de costos

Agent puede resultar costoso, pero hay algunas formas de reducir el costo:

- **Empieza con ejecuciones gratuitas**: Usa tus 5 solicitudes gratuitas diarias para entender los precios
- **Configura el parámetro `maxCredits`** : Limita tu gasto estableciendo un número máximo de créditos que estás dispuesto a usar. El panel de control limita esto a 2,500 créditos; para establecer un límite más alto, usa el parámetro `maxCredits` directamente a través de la API (nota: los valores por encima de 2,500 siempre se facturan como solicitudes pagadas)
- **Optimiza los prompts**: Los prompts más específicos suelen consumir menos créditos
- **Supervisa tu uso**: Haz seguimiento de tu consumo desde el panel de control
- **Define expectativas**: Las investigaciones complejas en múltiples dominios consumirán más créditos que las extracciones simples de una sola página

Prueba Agent ahora en [firecrawl.dev/app/agent](https://www.firecrawl.dev/app/agent) para ver cómo escala el consumo de créditos según tus casos de uso específicos.

> ¿Eres un Agent de IA que necesita una API key de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.