---
title: Cómo crear un asistente de investigación con IA usando Firecrawl y el AI SDK - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/cookbooks/ai-research-assistant-cookbook
source: sitemap
fetched_at: 2026-03-23T07:36:31.653164-03:00
rendered_js: false
word_count: 707
summary: Este documento explica cómo construir un asistente de investigación con IA capaz de realizar búsquedas y scraping web en tiempo real utilizando el SDK de IA de Vercel, OpenAI y Firecrawl.
tags:
    - ai-sdk
    - web-scraping
    - chatbot-desarrollo
    - nextjs
    - herramientas-ia
    - api-integracion
category: tutorial
---

Crea un asistente de investigación completo con IA que pueda extraer datos de sitios web y buscar en la web para responder preguntas. El asistente decide automáticamente cuándo usar herramientas de web scraping o de búsqueda para recopilar información y luego ofrece respuestas completas basadas en los datos recopilados. ![Interfaz de chatbot de asistente de investigación con IA que muestra web scraping en tiempo real con Firecrawl y respuestas conversacionales generadas por OpenAI](https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif?s=cfcbad69aa3f087a474414c0763a260b)

## Qué vas a construir

Una interfaz de chat con IA donde los usuarios pueden hacer preguntas sobre cualquier tema. El asistente decide automáticamente cuándo usar scraping web o herramientas de búsqueda para recopilar información y luego ofrece respuestas completas basadas en los datos obtenidos.

## Requisitos previos

- Node.js 18 o posterior instalado
- Una clave de la API de OpenAI de [platform.openai.com](https://platform.openai.com)
- Una clave de la API de Firecrawl de [firecrawl.dev](https://firecrawl.dev)
- Conocimientos básicos de React y Next.js

## Cómo funciona

### Flujo de mensajes

1. **El usuario envía un mensaje**: El usuario escribe una pregunta y hace clic en Enviar
2. **El frontend envía la solicitud**: `useChat` envía el mensaje a `/api/chat` con el modelo seleccionado y el ajuste de búsqueda web
3. **El backend procesa el mensaje**: La ruta de la API recibe el mensaje y llama a `streamText`
4. **La IA decide qué herramientas usar**: El modelo analiza la pregunta y decide si usar `scrapeWebsite` o `searchWeb` (solo si la búsqueda web está habilitada)
5. **Ejecución de herramientas**: Si se invocan herramientas, Firecrawl hace scraping o busca en la web
6. **La IA genera la respuesta**: El modelo analiza los resultados de las herramientas y genera una respuesta en lenguaje natural
7. **El frontend muestra los resultados**: La interfaz muestra las llamadas a herramientas y la respuesta final en tiempo real

El sistema de llamadas a herramientas del AI SDK ([ai-sdk.dev/docs/foundations/tools](https://ai-sdk.dev/docs/foundations/tools)) funciona de la siguiente manera:

1. El modelo recibe el mensaje del usuario y las descripciones de las herramientas disponibles
2. Si el modelo determina que se necesita una herramienta, genera una llamada a la herramienta con parámetros
3. El SDK ejecuta la función de la herramienta con esos parámetros
4. El resultado de la herramienta se envía de vuelta al modelo
5. El modelo usa el resultado para generar su respuesta final

Todo esto ocurre automáticamente dentro de una única llamada a `streamText`, con los resultados transmitiéndose al frontend en tiempo real.

## Características clave

### Selección de modelo

La aplicación admite varios modelos de OpenAI:

- **GPT-5 Mini (Thinking)**: Modelo reciente de OpenAI con capacidades avanzadas de razonamiento
- **GPT-4o Mini**: Modelo rápido y rentable

Los usuarios pueden alternar entre modelos usando el selector desplegable.

### Interruptor de búsqueda web

El botón Search controla si la IA puede usar las herramientas de Firecrawl:

- **Enabled**: la IA puede invocar las herramientas `scrapeWebsite` y `searchWeb` según sea necesario
- **Disabled**: la IA responde solo con el conocimiento de su entrenamiento

Esto les da a los usuarios control sobre cuándo usar datos de la web frente al conocimiento incorporado del modelo.

## Ideas de personalización

Amplía el asistente con herramientas adicionales:

- Consultas a la base de datos para datos internos de la empresa
- Integración con el CRM para obtener información de clientes
- Envío de correos electrónicos
- Generación de documentos

Cada herramienta sigue el mismo patrón: define un esquema con Zod, implementa la función `execute` y regístrala en el objeto `tools`.

### Cambiar el modelo de IA

Sustituye OpenAI por otro proveedor:

```
import { anthropic } from "@ai-sdk/anthropic";

const result = streamText({
  model: anthropic("claude-4.5-sonnet"),
  // ... resto de config
});
```

El SDK de IA es compatible con más de 20 proveedores con la misma API. Más información: [ai-sdk.dev/docs/foundations/providers-and-models](https://ai-sdk.dev/docs/foundations/providers-and-models).

### Personalizar la UI

Los componentes de AI Elements están basados en shadcn/ui, por lo que puedes:

- Modificar los estilos de los componentes en sus archivos
- Agregar nuevas variantes a los componentes existentes
- Crear componentes personalizados que se ajusten al sistema de diseño

## Mejores prácticas

1. **Usa las herramientas adecuadas**: Elige `searchWeb` para encontrar primero páginas relevantes, `scrapeWebsite` para páginas individuales o deja que la IA decida
2. **Supervisa el uso de la API**: Controla tu uso de las API de Firecrawl y OpenAI para evitar costos inesperados
3. **Gestiona los errores con elegancia**: Las herramientas incluyen manejo de errores, pero considera añadir mensajes de error visibles para el usuario
4. **Optimiza el rendimiento**: Usa streaming para ofrecer retroalimentación inmediata y considera cachear el contenido de acceso frecuente
5. **Establece límites razonables**: `stopWhen: stepCountIs(5)` evita llamadas excesivas a herramientas y costos descontrolados

* * *