---
title: Proxies | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/proxies
source: sitemap
fetched_at: 2026-03-23T07:21:46.585358-03:00
rendered_js: false
word_count: 340
summary: This document explains how to configure proxy settings and geographic locations in Firecrawl to optimize web scraping performance and reliability.
tags:
    - web-scraping
    - proxy-configuration
    - firecrawl
    - data-extraction
    - geo-location
category: configuration
---

A Firecrawl oferece diferentes tipos de proxy para ajudar você a fazer scraping de sites com diversos níveis de complexidade. O tipo de proxy pode ser especificado usando o parâmetro `proxy`.

> Por padrão, a Firecrawl roteia todas as requisições por meio de proxies para garantir confiabilidade e acesso, mesmo que você não especifique um tipo de proxy ou localização.

## Seleção de proxy por localização

O Firecrawl seleciona automaticamente o melhor proxy com base na sua localização especificada ou detectada. Isso ajuda a otimizar o desempenho e a confiabilidade da extração. No entanto, nem todas as localidades são atualmente compatíveis. As seguintes localidades estão disponíveis:

Country CodeNome do paísSuporte básico de proxySuporte avançado de proxyAEEmirados Árabes UnidosSimNãoAUAustráliaSimNãoBRBrasilSimNãoCACanadáSimNãoCNChinaSimNãoCZTchéquiaSimNãoDEAlemanhaSimNãoEEEstôniaSimNãoEGEgitoSimNãoESEspanhaSimNãoFRFrançaSimNãoGBReino UnidoSimNãoGRGréciaSimNãoHUHungriaSimNãoIDIndonésiaSimNãoILIsraelSimNãoINÍndiaSimNãoITItáliaSimNãoJPJapãoSimNãoMYMalásiaSimNãoNONoruegaSimNãoPLPolôniaSimNãoPTPortugalSimNãoQACatarSimNãoSGSingapuraSimNãoUSEstados UnidosSimSimVNVietnãSimNão

Se você precisar de proxies em uma localidade não listada acima, por favor [entre em contato conosco](mailto:help@firecrawl.com) e informe suas necessidades. Se você não especificar um proxy ou uma localidade, o Firecrawl usará automaticamente proxies dos EUA.

## Como especificar a localização do proxy

Você pode solicitar uma localização específica de proxy definindo o parâmetro `location.country` na sua requisição. Por exemplo, para usar um proxy no Brasil, defina `location.country` como `BR`. Para ver todos os detalhes, consulte a [referência da API de `location.country`](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-location).

## Tipos de Proxy

Firecrawl oferece suporte a três tipos de proxy:

- **basic**: Proxies para scraping da maioria dos sites. Rápidos e geralmente funcionam.
- **enhanced**: Proxies aprimorados para scraping de sites complexos mantendo a privacidade. Mais lentos, mas mais confiáveis em certos sites. [Saiba mais sobre o Enhanced Mode →](https://docs.firecrawl.dev/pt-BR/features/enhanced-mode)
- **auto**: Firecrawl refará automaticamente o scraping usando proxies aprimorados se o proxy básico falhar. Se a nova tentativa com enhanced for bem-sucedida, 5 créditos serão cobrados pelo scraping. Se a primeira tentativa com basic for bem-sucedida, apenas o custo padrão será cobrado.

* * *

> **Observação:** Para informações detalhadas sobre o uso de proxies aprimorados, incluindo custos de créditos e estratégias de repetição de tentativas, consulte a [documentação do Enhanced Mode](https://docs.firecrawl.dev/pt-BR/features/enhanced-mode).

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções de onboarding automatizado.