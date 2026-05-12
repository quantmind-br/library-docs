---
title: Proxies | Firecrawl
url: https://docs.firecrawl.dev/features/proxies
source: sitemap
fetched_at: 2026-03-23T07:24:25.26936-03:00
rendered_js: false
word_count: 291
summary: This document explains how to configure proxy settings in Firecrawl, including choosing specific geographic locations and selecting between basic or enhanced proxy types for web scraping.
tags:
    - firecrawl
    - web-scraping
    - proxy-configuration
    - scraping-reliability
    - geographic-routing
    - api-parameters
category: configuration
---

Firecrawl provides different proxy types to help you scrape websites with varying levels of complexity. The proxy type can be specified using the `proxy` parameter.

> By default, Firecrawl routes all requests through proxies to help ensure reliability and access, even if you do not specify a proxy type or location.

## Location-Based Proxy Selection

Firecrawl automatically selects the best proxy based on your specified or detected location. This helps optimize scraping performance and reliability. However, not all locations are currently supported. The following locations are available:

Country CodeCountry NameBasic Proxy SupportEnhanced Proxy SupportAEUnited Arab EmiratesYesNoAUAustraliaYesNoBRBrazilYesNoCACanadaYesNoCNChinaYesNoCZCzechiaYesNoDEGermanyYesNoEEEstoniaYesNoEGEgyptYesNoESSpainYesNoFRFranceYesNoGBUnited KingdomYesNoGRGreeceYesNoHUHungaryYesNoIDIndonesiaYesNoILIsraelYesNoINIndiaYesNoITItalyYesNoJPJapanYesNoMYMalaysiaYesNoNONorwayYesNoPLPolandYesNoPTPortugalYesNoQAQatarYesNoSGSingaporeYesNoUSUnited StatesYesYesVNVietnamYesNo

If you need proxies in a location not listed above, please [contact us](mailto:help@firecrawl.com) and let us know your requirements. If you do not specify a proxy or location, Firecrawl will automatically use US proxies.

## How to Specify Proxy Location

You can request a specific proxy location by setting the `location.country` parameter in your request. For example, to use a Brazilian proxy, set `location.country` to `BR`. For full details, see the [API reference for `location.country`](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-location).

## Proxy Types

Firecrawl supports three types of proxies:

- **basic**: Proxies for scraping most sites. Fast and usually works.
- **enhanced**: Enhanced proxies for scraping complex sites while maintaining privacy. Slower, but more reliable on certain sites. [Learn more about Enhanced Mode →](https://docs.firecrawl.dev/features/enhanced-mode)
- **auto**: Firecrawl will automatically retry scraping with enhanced proxies if the basic proxy fails. If the retry with enhanced is successful, 5 credits will be billed for the scrape. If the first attempt with basic is successful, only the regular cost will be billed.

* * *

> **Note:** For detailed information on using enhanced proxies, including credit costs and retry strategies, see the [Enhanced Mode documentation](https://docs.firecrawl.dev/features/enhanced-mode).

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.