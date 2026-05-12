---
title: Tipos de eventos de webhook | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/webhooks/events
source: sitemap
fetched_at: 2026-03-23T07:28:12.75742-03:00
rendered_js: false
word_count: 394
summary: This document outlines the webhook event system, providing a detailed reference for event types triggered by crawling, scraping, and agent operations, including their payload structures and configuration.
tags:
    - webhooks
    - api-reference
    - event-notifications
    - data-extraction
    - crawling-events
    - agent-automation
category: reference
---

## Referência rápida

EventoGatilho`crawl.started`O job de rastreamento começa a ser processado`crawl.page`Uma página é extraída durante um rastreamento`crawl.completed`O job de rastreamento é concluído e todas as páginas foram processadas`batch_scrape.started`O job de extração em lote começa a ser processado`batch_scrape.page`Uma URL é extraída durante uma extração em lote`batch_scrape.completed`Todas as URLs do lote foram processadas`extract.started`O job de extração começa a ser processado`extract.completed`A extração é concluída com sucesso`extract.failed`A extração falha`agent.started`O job do agente começa a ser processado`agent.action`O agente executa uma ferramenta (scraping, busca etc.)`agent.completed`O agente é concluído com sucesso`agent.failed`O agente encontra um erro`agent.cancelled`O job do agente é cancelado pelo usuário

## Estrutura do payload

Todos os eventos de webhook compartilham esta estrutura:

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [...],
  "metadata": {}
}
```

FieldTypeDescription`success`booleanSe a operação foi bem-sucedida`type`stringTipo de evento (por exemplo, `crawl.page`)`id`stringID da tarefa`data`arrayDados específicos do evento (veja exemplos abaixo)`metadata`objectMetadados personalizados da sua configuração de webhook`error`stringMensagem de erro (quando `success` é `false`)

## Eventos de Crawl

### `crawl.started`

Enviado quando a operação de rastreamento começa a ser processada.

```
{
  "success": true,
  "type": "crawl.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `crawl.page`

Enviado para cada página extraída. O array `data` contém o conteúdo da página e seus metadados.

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Page content...",
      "metadata": {
        "title": "Título da página",
        "description": "Descrição da página",
        "url": "https://example.com/page",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com/page",
        "proxyUsed": "basic",
        "cacheState": "hit",
        "cachedAt": "2025-09-03T21:11:25.636Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

### `crawl.completed`

Enviado quando toda a operação de rastreamento é concluída e todas as páginas foram processadas.

```
{
  "success": true,
  "type": "crawl.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

## Eventos de Scrape em Lote

### `batch_scrape.started`

Enviado quando a tarefa de raspagem em lote começa a ser processada.

```
{
  "success": true,
  "type": "batch_scrape.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `batch_scrape.page`

Enviado para cada URL processada na raspagem. O array `data` contém o conteúdo da página e seus metadados.

```
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Page content...",
      "metadata": {
        "title": "Page Title",
        "description": "Descrição da página",
        "url": "https://example.com",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com",
        "proxyUsed": "basic",
        "cacheState": "miss",
        "cachedAt": "2025-09-03T23:30:53.434Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

### `batch_scrape.completed`

Enviado quando todas as URLs do lote tiverem sido processadas.

```
{
  "success": true,
  "type": "batch_scrape.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

Enviado quando a tarefa de extração começa a ser processada.

```
{
  "success": true,
  "type": "extract.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

Enviado quando uma operação de extração é concluída com sucesso. O array `data` contém os dados extraídos e as informações de uso.

```
{
  "success": true,
  "type": "extract.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "success": true,
      "data": { "siteName": "Exemplo Site", "category": "Tecnologia" },
      "extractId": "550e8400-e29b-41d4-a716-446655440000",
      "llmUsage": 0.0020118,
      "totalUrlsScraped": 1,
      "sources": {
        "siteName": ["https://example.com"],
        "category": ["https://example.com"]
      }
    }
  ],
  "metadata": {}
}
```

Enviado quando a extração falha. O campo `error` contém o motivo do erro.

```
{
  "success": false,
  "type": "extract.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "error": "Falha na extração de dados: tempo limite excedido",
  "metadata": {}
}
```

## Eventos de agente

### `agent.started`

Enviado quando a tarefa do agente começa a ser processada.

```
{
  "success": true,
  "type": "agent.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `agent.action`

Enviado após cada execução de uma ferramenta (scrape, search, etc.).

```
{
  "success": true,
  "type": "agent.action",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 5,
      "action": "mcp__tools__scrape",
      "input": {
        "url": "https://example.com"
      }
    }
  ],
  "metadata": {}
}
```

### `agent.completed`

Enviado quando o agente conclui a execução com sucesso. O array `data` contém os dados extraídos e o total de créditos consumidos.

```
{
  "success": true,
  "type": "agent.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 15,
      "data": {
        "company": "Example Corp",
        "industry": "Technology",
        "founded": 2020
      }
    }
  ],
  "metadata": {}
}
```

### `agent.failed`

Enviado quando o agente encontra um erro. O campo `error` contém o motivo da falha.

```
{
  "success": false,
  "type": "agent.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 8
    }
  ],
  "error": "Créditos máximos excedidos",
  "metadata": {}
}
```

### `agent.cancelled`

Enviado quando a tarefa do agente é cancelada pelo usuário.

```
{
  "success": false,
  "type": "agent.cancelled",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 3
    }
  ],
  "metadata": {}
}
```

## Filtragem de eventos

Por padrão, você recebe todos os eventos. Para receber apenas eventos específicos, use o array `events` na configuração do seu webhook:

```
{
  "url": "https://your-app.com/webhook",
  "events": ["concluído", "falhou"]
}
```

Isso é útil se você se importa apenas com a conclusão da tarefa e não precisa de atualizações por página.