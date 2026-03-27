---
title: Webhooks | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/webhooks/overview
source: sitemap
fetched_at: 2026-03-23T07:37:26.888196-03:00
rendered_js: false
word_count: 133
summary: This document explains how to configure and use webhooks to receive real-time notifications for API operations like crawling, batch scraping, and extraction.
tags:
    - webhooks
    - api-integration
    - real-time-notifications
    - data-scraping
    - asynchronous-processing
    - event-driven
category: configuration
---

Webhooks permitem que você receba notificações em tempo real conforme suas operações progridem, em vez de consultar o status periodicamente.

## Operações compatíveis

OperaçãoEventosCrawl`started`, `page`, `completed`Batch Scrape`started`, `page`, `completed`Extract`started`, `completed`, `failed`Agent`started`, `action`, `completed`, `failed`, `cancelled`

## Configuração

Adicione um objeto `webhook` à sua requisição:

```
{
  "webhook": {
    "url": "https://your-domain.com/webhook",
    "metadata": {
      "any_key": "any_value"
    },
    "events": ["iniciado", "página", "concluído", "fracassou"]
  }
}
```

CampoTipoObrigatórioDescrição`url`stringSimURL do endpoint do seu webhook (HTTPS)`headers`objectNãoCabeçalhos personalizados para incluir nas requisições do webhook`metadata`objectNãoDados personalizados incluídos nas cargas do webhook`events`arrayNãoTipos de evento a receber (padrão: todos)

## Uso

### Rastreamento com webhook

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["iniciado", "página", "concluído"]
      }
    }'
```

### Raspagem em lote com webhook

```
curl -X POST https://api.firecrawl.dev/v2/batch/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
      ],
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

## Timeouts e tentativas

Seu endpoint deve responder com um status `2xx` em até **10 segundos**. Se a entrega falhar (timeout, status não `2xx` ou erro de rede), o Firecrawl fará novas tentativas automaticamente:

TentativaAtraso após falha1ª1 minuto2ª5 minutos3ª15 minutos

Após 3 tentativas sem sucesso, o webhook é marcado como falho e nenhuma nova tentativa é feita.