---
title: Proxies | Firecrawl
url: https://docs.firecrawl.dev/es/features/proxies
source: sitemap
fetched_at: 2026-03-23T07:25:17.341382-03:00
rendered_js: false
word_count: 336
summary: This document explains how to configure proxy settings in Firecrawl, including selecting geographical locations and choosing between basic or enhanced proxy types for web scraping.
tags:
    - web-scraping
    - proxy-configuration
    - firecrawl
    - data-extraction
    - network-settings
category: configuration
---

Firecrawl ofrece diferentes tipos de proxy para ayudarte a extraer datos de sitios web con distintos niveles de complejidad. Puedes especificar el tipo de proxy con el parámetro `proxy`.

> De forma predeterminada, Firecrawl dirige todas las solicitudes a través de proxies para garantizar la fiabilidad y el acceso, incluso si no especificas un tipo de proxy o una ubicación.

## Selección de proxy por ubicación

Firecrawl selecciona automáticamente el mejor proxy según tu ubicación especificada o detectada. Esto ayuda a optimizar el rendimiento y la fiabilidad del scraping. Sin embargo, no todas las ubicaciones están disponibles por ahora. Las siguientes ubicaciones están disponibles:

Country CodeCountry NameSoporte básico de proxySoporte avanzado de proxyAEEmiratos Árabes UnidosSíNoAUAustraliaSíNoBRBrasilSíNoCACanadáSíNoCNChinaSíNoCZChequiaSíNoDEAlemaniaSíNoEEEstoniaSíNoEGEgiptoSíNoESEspañaSíNoFRFranciaSíNoGBReino UnidoSíNoGRGreciaSíNoHUHungríaSíNoIDIndonesiaSíNoILIsraelSíNoINIndiaSíNoITItaliaSíNoJPJapónSíNoMYMalasiaSíNoNONoruegaSíNoPLPoloniaSíNoPTPortugalSíNoQACatarSíNoSGSingapurSíNoUSEstados UnidosSíSíVNVietnamSíNo

Si necesitas proxies en una ubicación que no aparece arriba, por favor [contáctanos](mailto:help@firecrawl.com) y cuéntanos tus requisitos. Si no especificas un proxy o una ubicación, Firecrawl usará automáticamente proxies de Estados Unidos.

## Cómo especificar la ubicación del proxy

Puedes solicitar una ubicación de proxy específica estableciendo el parámetro `location.country` en tu solicitud. Por ejemplo, para usar un proxy de Brasil, configura `location.country` en `BR`. Para ver todos los detalles, consulta la [referencia de la API de `location.country`](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-location).

## Tipos de proxy

Firecrawl admite tres tipos de proxies:

- **basic**: Proxies para hacer scraping de la mayoría de los sitios. Son rápidos y suelen funcionar bien.
- **enhanced**: Proxies enhanced para hacer scraping de sitios complejos manteniendo la privacidad. Son más lentos, pero más fiables en determinados sitios. [Más información sobre Enhanced Mode →](https://docs.firecrawl.dev/es/features/enhanced-mode)
- **auto**: Firecrawl reintentará automáticamente el scraping con proxies enhanced si el proxy básico falla. Si el reintento con enhanced tiene éxito, se cobrarán 5 créditos por el scraping. Si el primer intento con basic tiene éxito, solo se cobrará el coste normal.

* * *

> **Nota:** Para obtener información detallada sobre el uso de proxies enhanced, incluidos los costes en créditos y las estrategias de reintento, consulta la [documentación de Enhanced Mode](https://docs.firecrawl.dev/es/features/enhanced-mode).

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.