---
title: Raspagem em lote | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:21:56.559606-03:00
rendered_js: false
word_count: 516
summary: This document explains how to perform batch scraping tasks using Firecrawl, detailing synchronous and asynchronous operation modes, concurrency management, and webhook integration for real-time notifications.
tags:
    - web-scraping
    - api-documentation
    - batch-processing
    - webhooks
    - data-extraction
    - firecrawl
category: guide
---

A raspagem em lote permite raspar várias URLs em uma única tarefa. Passe uma lista de URLs e parâmetros opcionais, e o Firecrawl as processa simultaneamente e retorna todos os resultados de uma só vez.

- Funciona como `/crawl`, mas para uma lista explícita de URLs
- Modos síncrono e assíncrono
- Suporta todas as opções de raspagem, incluindo extração estruturada
- Concorrência configurável por tarefa

## Como funciona

Você pode executar um scrape em lote de duas formas:

ModoMétodo do SDK (JS / Python)ComportamentoSíncrono`batchScrape` / `batch_scrape`Inicia o lote e aguarda a conclusão, retornando todos os resultadosAssíncrono`startBatchScrape` / `start_batch_scrape`Inicia o lote e retorna um ID do job para consulta por polling ou webhooks

## Uso básico

### Resposta

Chamar `batchScrape` / `batch_scrape` retorna os resultados completos quando o lote é concluído.

```
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Página inicial da documentação do Firecrawl![logo claro](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Crie um ‘chat com o site’ usando Groq Llama 3 | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Aprenda a usar o Firecrawl, o Groq Llama 3 e o LangChain para criar um bot de ‘chat com o seu site’."
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

Chamar `startBatchScrape` / `start_batch_scrape` retorna um ID de job que você pode acompanhar via `getBatchScrapeStatus` / `get_batch_scrape_status`, o endpoint da API `/batch/scrape/{id}` ou webhooks. Os resultados do job ficam disponíveis via API por 24 horas após a conclusão. Depois desse período, você ainda pode visualizar o histórico e os resultados dos seus batch scrapes nos [activity logs](https://www.firecrawl.dev/app/logs).

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Concorrência

Por padrão, uma tarefa de raspagem em lote usa todo o limite de navegadores simultâneos da sua equipe (consulte [Rate Limits](https://docs.firecrawl.dev/pt-BR/rate-limits)). Você pode reduzir isso por tarefa com o parâmetro `maxConcurrency`. Por exemplo, `maxConcurrency: 50` limita essa tarefa a 50 raspagens simultâneas. Definir esse valor muito baixo em lotes grandes vai tornar o processamento significativamente mais lento, então só o reduza se você realmente precisar deixar capacidade para outras tarefas em execução simultânea.

Você pode usar a coleta em lote para extrair dados estruturados de cada página do lote. Isso é útil quando você quer aplicar o mesmo esquema a uma lista de URLs.

### Resposta

`batchScrape` / `batch_scrape` retorna resultados completos:

```
{
  "status": "concluído",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "json": {
        "title": "Crie um 'chat com o site' usando Groq Llama 3 | Firecrawl",
        "description": "Aprenda a usar Firecrawl, Groq Llama 3 e LangChain para criar um bot de 'chat com o seu site'."
      }
    },
    ...
  ]
}
```

`startBatchScrape` / `start_batch_scrape` retorna um ID de tarefa:

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Webhooks

Você pode configurar webhooks para receber notificações em tempo real conforme cada URL do seu lote é raspada. Isso permite processar os resultados imediatamente, em vez de esperar a conclusão de todo o lote.

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
        "events": ["iniciado", "página", "concluído"]
      }
    }'
```

### Tipos de evento

EventoDescrição`batch_scrape.started`O job de raspagem em lote foi iniciado`batch_scrape.page`Uma única URL foi raspada com sucesso`batch_scrape.completed`Todas as URLs foram processadas`batch_scrape.failed`O job de raspagem em lote encontrou um erro

### Payload

Cada envio de webhook inclui um corpo JSON com a seguinte estrutura:

```
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "batch-job-id",
  "data": [...],
  "metadata": {},
  "error": null
}
```

### Verificando assinaturas de webhook

Toda requisição de webhook do Firecrawl inclui o cabeçalho `X-Firecrawl-Signature` contendo uma assinatura HMAC-SHA256. Sempre verifique essa assinatura para garantir que o webhook é autêntico e não foi adulterado.

1. Obtenha o segredo do seu webhook na [aba Advanced](https://www.firecrawl.dev/app/settings?tab=advanced) das configurações da sua conta
2. Extraia a assinatura do cabeçalho `X-Firecrawl-Signature`
3. Calcule o HMAC-SHA256 do corpo bruto da requisição usando o seu segredo
4. Compare com o cabeçalho de assinatura usando uma função segura contra ataques de timing

Para exemplos completos de implementação em JavaScript e Python, consulte a [documentação de Segurança de Webhooks](https://docs.firecrawl.dev/pt-BR/webhooks/security). Para uma documentação abrangente sobre webhooks, incluindo payloads detalhados de eventos, configuração avançada e solução de problemas, consulte a [documentação de Webhooks](https://docs.firecrawl.dev/pt-BR/webhooks/overview).

> Você é um agente de IA que precisa de uma Firecrawl API key? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções automatizadas de onboarding.