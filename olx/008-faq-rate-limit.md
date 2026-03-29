---
title: Limitação de Taxa (Rate Limit) na API
url: https://developers.olx.com.br/faq/rate_limit.html
source: crawler
fetched_at: 2026-02-07T15:17:10.814734269-03:00
rendered_js: false
word_count: 88
summary: This document outlines the rate limiting policy for OLX APIs, specifying request thresholds, block durations, and the associated 429 error response.
tags:
    - olx-api
    - rate-limiting
    - api-throttling
    - status-429
    - ip-based-limit
category: reference
---

As APIs da OLX, com host `https://apps.olx.com.br`, tem configurado um rate limit de 5.000 requests por minuto. Portanto, caso você ultrapasse esse limite será bloqueado durante 10 minutos.

No caso de ultrapassar o limite você irá começar a receber um erro com `status code = 429` em todas as suas requisições feitas para o host: `https://apps.olx.com.br` durante todo tempo de bloqueio (10 minutos).

**IMPORTANTE**: O Limite de Taxa é baseado nos IPs que fazem as requisições. Ou seja, cada IP pode fazer no máximo 5.000 requests por minuto.