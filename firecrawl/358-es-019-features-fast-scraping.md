---
title: Scraping más rápido | Firecrawl
url: https://docs.firecrawl.dev/es/features/fast-scraping
source: sitemap
fetched_at: 2026-03-23T07:25:44.850597-03:00
rendered_js: false
word_count: 480
summary: This document explains how to manage data freshness and performance in Firecrawl using the maxAge parameter to control cache behavior and retrieval speed.
tags:
    - caching
    - performance-optimization
    - data-freshness
    - web-scraping
    - latency-reduction
    - api-configuration
category: configuration
---

## Cómo funciona

Firecrawl guarda en caché las páginas previamente extraídas y, de forma predeterminada, devuelve una copia reciente cuando está disponible.

- **Frescura predeterminada**: `maxAge = 172800000` ms (2 días). Si la copia en caché es más reciente que ese valor, se devuelve al instante; de lo contrario, Firecrawl vuelve a extraer y actualiza la caché.
- **Forzar datos frescos**: configura `maxAge: 0` para extraer siempre. Ten en cuenta que esto omite por completo la caché, por lo que cada solicitud pasa por todo el pipeline de scraping; esto hará que tarde más en completarse y tenga más probabilidades de fallar. Usa un `maxAge` distinto de cero si no necesitas contenido en tiempo real en cada solicitud.
- **Omitir caché**: configura `storeInCache: false` si no quieres almacenar los resultados de una solicitud.

Obtén tus resultados **hasta un 500% más rápido** cuando no necesites los datos más recientes. Controla la frescura con `maxAge`:

1. **Devuelve al instante** si tenemos una versión reciente de la página
2. **Extrae de nuevo** solo si nuestra versión es más antigua que la edad que especifiques
3. **Ahorra tiempo**: los resultados llegan en milisegundos en lugar de segundos

## Cuándo usarlo

**Ideal para:**

- Documentación, artículos, páginas de producto
- Procesamiento por lotes
- Desarrollo y pruebas
- Creación de bases de conocimiento

**Evitar en:**

- Datos en tiempo real (precios de acciones, resultados en vivo, noticias de última hora)
- Contenido que se actualiza con frecuencia
- Aplicaciones sensibles al tiempo

## Uso

Añade `maxAge` a tu solicitud de scraping. Los valores se expresan en milisegundos (p. ej., `3600000` = 1 hora).

## Valores comunes de maxAge

Aquí tienes algunos valores de referencia útiles:

- **5 minutos**: `300000` - Para contenido semidinámico
- **1 hora**: `3600000` - Para contenido que se actualiza cada hora
- **1 día**: `86400000` - Para contenido que se actualiza a diario
- **1 semana**: `604800000` - Para contenido relativamente estático

## Impacto en el rendimiento

Con `maxAge` habilitado:

- **Respuestas hasta 5 veces más rápidas** para contenido reciente
- **Resultados instantáneos** en lugar de esperar a nuevas extracciones

## Notas importantes

- **Predeterminado**: `maxAge` es `172800000` (2 días)
- **Actual cuando haga falta**: Si nuestros datos son más antiguos que `maxAge`, hacemos un scraping nuevo automáticamente
- **Sin datos obsoletos**: Nunca recibirás datos más antiguos que el `maxAge` que especifiques
- **Créditos**: Los resultados almacenados en caché siguen costando 1 crédito por página. La caché mejora la velocidad y la latencia, no el consumo de créditos.

## Rastreo más rápido

Los mismos beneficios de velocidad se aplican al rastrear varias páginas. Usa `maxAge` dentro de `scrapeOptions` para obtener resultados en caché de páginas que hemos visto recientemente.

Al rastrear con `maxAge`, cada página de tu rastreo se beneficiará de una mejora de velocidad del 500% si tenemos datos recientes en caché para esa página. ¡Empieza a usar `maxAge` hoy para obtener scrapes y rastreos muchísimo más rápidos!

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.