---
title: Límites de tasa | Firecrawl
url: https://docs.firecrawl.dev/es/rate-limits
source: sitemap
fetched_at: 2026-03-23T07:27:46.387762-03:00
rendered_js: false
word_count: 470
summary: This document outlines the billing model, concurrency limits, and API rate limits for the Firecrawl platform, explaining how resource allocation works across different subscription plans.
tags:
    - billing-model
    - api-limits
    - concurrency-limits
    - subscription-plans
    - rate-limiting
    - browser-sessions
category: reference
---

## Modelo de facturación

Firecrawl utiliza planes mensuales basados en suscripción. No ofrecemos un modelo estrictamente de pago por uso, pero nuestra **funcionalidad de recarga automática** permite un escalado flexible: una vez que te suscribes a un plan, puedes comprar automáticamente créditos adicionales cuando bajes de cierto umbral, con mejores precios en paquetes de recarga automática más grandes. Para hacer pruebas antes de comprometerte con un plan más grande, empieza con el plan Free o Hobby. Los cambios a un plan inferior se programan para entrar en vigor en la siguiente renovación; no se emiten créditos por el tiempo no utilizado.

## Límites de navegadores concurrentes

Los navegadores concurrentes indican cuántas páginas web puede procesar Firecrawl para ti al mismo tiempo. Tu plan determina cuántos de estos trabajos pueden ejecutarse en paralelo; si superas este límite, los trabajos adicionales esperarán en una cola hasta que haya recursos disponibles. Ten en cuenta que el tiempo que se pasa esperando en la cola se contabiliza en el parámetro [`timeout`](https://docs.firecrawl.dev/es/advanced-scraping-guide#timing-and-cache) de la solicitud, por lo que puedes configurar un timeout más bajo para fallar rápido en lugar de esperar. También puedes comprobar la disponibilidad actual mediante el endpoint [Queue Status](https://docs.firecrawl.dev/es/api-reference/endpoint/queue-status).

### Planes actuales

PlanNavegadores concurrentesMáximo de trabajos en colaFree250,000Hobby550,000estándar50100,000crecimiento100200,000escala / Enterprise150+300,000+

Cada equipo tiene un número máximo de trabajos que pueden estar esperando en la cola de concurrencia. Si superas este límite, los nuevos trabajos se rechazarán con un código de estado `429` hasta que finalicen los trabajos existentes. En los planes más grandes con límites de concurrencia personalizados, el máximo de trabajos en cola es 2,000 veces tu límite de concurrencia, con un tope de 2,000,000. Si necesitas límites de concurrencia más altos, [contáctanos sobre los planes Enterprise](https://firecrawl.dev/enterprise).

PlanConcurrent BrowsersMax Queued JobsFree250,000Starter50100,000Explorer100200,000Pro200400,000

## Límites de frecuencia de la API

Los límites de frecuencia se miden en peticiones por minuto y existen principalmente para evitar abusos. Cuando todo está correctamente configurado, tu verdadero cuello de botella serán los navegadores concurrentes.

### Planes actuales

Plan/scrape/map/crawl/search/agent/crawl/status/agent/statusGratis101015101500500Hobby1001001550100150025000Estándar50050050250500150025000Crecimiento5000500025025001000150025000Escala75007500750750010002500025000

Estos límites de uso se aplican para garantizar un uso justo y la disponibilidad de la API para todos los usuarios. Si necesitas límites más altos, contáctanos en [help@firecrawl.com](mailto:help@firecrawl.com) para analizar planes personalizados.

Los endpoints de extracción comparten los mismos límites de uso que los correspondientes a `/agent`.

### Endpoints de Batch Scrape

Los endpoints de Batch Scrape comparten los mismos límites de frecuencia que los endpoints correspondientes de `/crawl`.

### Sesiones del navegador

Mientras el endpoint `/browser` está en vista previa, cada equipo puede tener hasta 20 sesiones de navegador activas al mismo tiempo. Si superas este límite, las solicitudes de nuevas sesiones devolverán un código de estado `429` hasta que se cierren las sesiones existentes.

### Agente FIRE-1

Las solicitudes que usan el agente FIRE-1 tienen límites de uso independientes, que se contabilizan por separado para cada endpoint:

EndpointLímite de uso (solicitudes/min)/scrape10/extract10

Plan/extract (solicitudes/min)/extract/status (solicitudes/min)Starter10025000Explorer50025000Pro100025000