---
title: Rastreio de mudanças | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/change-tracking
source: sitemap
fetched_at: 2026-03-23T07:21:53.846557-03:00
rendered_js: false
word_count: 1034
summary: This document explains how to use the change tracking feature in Firecrawl to monitor web pages for content updates, providing structured diffs and field-level comparisons across periodic scrapes.
tags:
    - web-scraping
    - change-detection
    - data-monitoring
    - api-integration
    - automation
    - diff-analysis
category: guide
---

![Rastreio de mudanças](https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=cc56c24d15e1b2ed4806ddb66d0f5c3f) O rastreio de mudanças compara o conteúdo atual de uma página com o da última vez em que você fez o scrape. Adicione `changeTracking` ao seu array de `formats` para detectar se uma página é nova, inalterada ou modificada e, opcionalmente, obter um diff estruturado do que mudou.

- Funciona com `/scrape`, `/crawl` e `/batch/scrape`
- Dois modos de diff: `git-diff` para mudanças em nível de linha e `json` para comparação em nível de campo
- Restrito à sua equipe e, opcionalmente, a uma tag que você especificar

## Como funciona

Cada scrape com `changeTracking` habilitado armazena um snapshot e o compara com o snapshot anterior para essa URL. Snapshots são armazenados de forma persistente e não expiram, por isso as comparações permanecem precisas, independentemente de quanto tempo se passou entre os scrapes.

ScrapeResultadoPrimeiro scrape`changeStatus: "new"` (nenhuma versão anterior existe)Conteúdo inalterado`changeStatus: "same"`Conteúdo modificado`changeStatus: "changed"` (dados de diff disponíveis)Página removida`changeStatus: "removed"`

A resposta inclui estes campos no objeto `changeTracking`:

CampoTipoDescrição`previousScrapeAt``string | null`Carimbo de data e hora do scrape anterior (`null` no primeiro scrape)`changeStatus``string``"new"`, `"same"`, `"changed"` ou `"removed"``visibility``string``"visible"` (localizável via links/sitemap) ou `"hidden"` (a URL funciona, mas não está mais linkada)`diff``object | undefined`Diff em nível de linha (presente apenas no modo `git-diff` quando o status é `"changed"`)`json``object | undefined`Comparação em nível de campo (presente apenas no modo `json` quando o status é `"changed"`)

## Uso básico

Inclua tanto `markdown` quanto `changeTracking` no array `formats`. O formato `markdown` é obrigatório porque o rastreio de mudanças compara as páginas com base no conteúdo em markdown.

### Resposta

No primeiro scrape, `changeStatus` é `"new"` e `previousScrapeAt` é `null`:

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $9/mo\nPro: $29/mo...",
    "changeTracking": {
      "previousScrapeAt": null,
      "changeStatus": "new",
      "visibility": "visible"
    }
  }
}
```

Em raspagens posteriores, `changeStatus` indica se o conteúdo foi alterado:

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $12/mo\nPro: $39/mo...",
    "changeTracking": {
      "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible"
    }
  }
}
```

## Modo git-diff

O modo `git-diff` retorna alterações linha a linha em um formato semelhante ao `git diff`. Passe um objeto no array `formats` com `modes: ["git-diff"]`:

### Resposta

O objeto `diff` contém um diff em texto simples e uma representação JSON estruturada:

```
{
  "rastreioDeMudanças": {
    "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "diff": {
      "text": "@@ -1,3 +1,3 @@\n # Pricing\n-Starter: $9/mo\n-Pro: $29/mo\n+Starter: $12/mo\n+Pro: $39/mo",
      "json": {
        "files": [{
          "chunks": [{
            "content": "@@ -1,3 +1,3 @@",
            "changes": [
              { "type": "normal", "content": "# Pricing" },
              { "type": "del", "ln": 2, "content": "Starter: $9/mo" },
              { "type": "del", "ln": 3, "content": "Pro: $29/mo" },
              { "type": "add", "ln": 2, "content": "Starter: $12/mo" },
              { "type": "add", "ln": 3, "content": "Pro: $39/mo" }
            ]
          }]
        }]
      }
    }
  }
}
```

O objeto estruturado `diff.json` contém:

- `files`: array de arquivos modificados (geralmente um por página da web)
- `chunks`: seções de alterações dentro de um arquivo
- `changes`: alterações individuais de linha com `type` (`"add"`, `"del"` ou `"normal"`), número da linha (`ln`) e `content`

## Modo JSON

O modo `json` extrai campos específicos tanto da versão atual quanto da versão anterior da página usando um schema que você define. Isso é útil para acompanhar mudanças em dados estruturados, como preços, níveis de estoque ou metadados, sem precisar analisar um diff completo. Passe `modes: ["json"]` com um `schema` definindo os campos a serem extraídos:

### Resposta

Cada campo do schema é retornado com os valores `previous` e `current`:

```
{
  "changeTracking": {
    "previousScrapeAt": "2025-06-05T08:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "json": {
      "price": {
        "previous": "$19.99",
        "current": "$24.99"
      },
      "availability": {
        "previous": "In Stock",
        "current": "In Stock"
      }
    }
  }
}
```

Você também pode fornecer um `prompt` opcional para orientar a extração do LLM em conjunto com o schema.

Por padrão, o rastreamento de mudanças compara com a raspagem mais recente da mesma URL feita pela sua equipe. Tags permitem que você mantenha **históricos de rastreamento separados** para a mesma URL, o que é útil quando você monitora a mesma página em intervalos diferentes ou em contextos distintos.

Adicione rastreio de mudanças às operações de crawl para monitorar um site inteiro em busca de alterações. Passe o formato `changeTracking` dentro de `scrapeOptions`:

## Raspagem em lote com rastreamento de mudanças

Use a [raspagem em lote](https://docs.firecrawl.dev/pt-BR/features/batch-scrape) para monitorar um conjunto específico de URLs:

## Agendando o rastreamento de alterações

O rastreamento de alterações é mais útil quando você faz scraping em uma agenda regular. Você pode automatizar isso com cron, agendadores em nuvem ou ferramentas de workflow.

### Cron job

Crie um script que extraia dados de uma URL e envie alertas quando houver alterações:

```
#!/bin/bash
RESPONSE=$(curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://competitor.com/pricing",
    "formats": [
      "markdown",
      {
        "type": "changeTracking",
        "modes": ["json"],
        "schema": {
          "type": "object",
          "properties": {
            "starter_price": { "type": "string" },
            "pro_price": { "type": "string" }
          }
        }
      }
    ]
  }')

STATUS=$(echo "$RESPONSE" | jq -r '.data.changeTracking.changeStatus')

if [ "$STATUS" = "changed" ]; then
  echo "$RESPONSE" | jq '.data.changeTracking.json'
  # Envie alerta por e-mail, Slack, etc.
fi
```

Agende isso com `crontab -e`:

```
0 */6 * * * /path/to/check-pricing.sh >> /var/log/price-monitor.log 2>&1
```

AgendamentoExpressãoA cada hora`0 * * * *`A cada 6 horas`0 */6 * * *`Diariamente às 9h`0 9 * * *`Toda segunda-feira às 8h`0 8 * * 1`

### Agendadores em ambientes cloud e serverless

- **AWS**: regra do EventBridge acionando uma função Lambda
- **GCP**: Cloud Scheduler acionando uma Cloud Function
- **Vercel / Netlify**: funções serverless acionadas por cron
- **GitHub Actions**: workflows agendados com gatilhos `schedule` e `cron`

### Automação de fluxos de trabalho

Plataformas no-code como **n8n**, **Zapier** e **Make** podem chamar a API do Firecrawl em intervalos programados e enviar os resultados para o Slack, e-mail ou bancos de dados. Veja os [guias de automação de fluxos de trabalho](https://docs.firecrawl.dev/pt-BR/developer-guides/workflow-automation/n8n).

## Webhooks

Para operações assíncronas como crawl e batch scrape, use [webhooks](https://docs.firecrawl.dev/pt-BR/webhooks/overview) para receber resultados de rastreio de mudanças assim que chegarem, em vez de fazer polling.

O payload do evento `crawl.page` inclui o objeto `changeTracking` para cada página:

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [{
    "markdown": "# Pricing\n\nStarter: $12/mo...",
    "metadata": {
      "title": "Pricing",
      "url": "https://example.com/pricing",
      "statusCode": 200
    },
    "changeTracking": {
      "previousScrapeAt": "2025-06-05T12:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible",
      "diff": {
        "text": "@@ -2,1 +2,1 @@\n-Starter: $9/mo\n+Starter: $12/mo"
      }
    }
  }]
}
```

Para obter detalhes sobre a configuração de webhooks (cabeçalhos, metadados, eventos, tentativas de nova entrega, verificação de assinatura), consulte a [documentação de webhooks](https://docs.firecrawl.dev/pt-BR/webhooks/overview).

## Referência de configuração

O conjunto completo de opções disponível ao passar um objeto no formato `changeTracking`:

ParâmetroTipoPadrãoDescrição`type``string`(obrigatório)Deve ser `"changeTracking"``modes``string[]``[]`Modos de diff a serem habilitados: `"git-diff"`, `"json"` ou ambos`schema``object`(nenhum)JSON Schema para comparação em nível de campo (obrigatório para o modo `json`)`prompt``string`(nenhum)Prompt personalizado para orientar a extração pelo LLM (usado com o modo `json`)`tag``string``null`Identificador separado para o histórico de rastreamento

### Modelos de dados

## Detalhes importantes

- **Retenção de snapshots**: Snapshots são armazenados de forma persistente e não expiram. Uma raspagem feita meses após a anterior ainda será comparada corretamente com o snapshot anterior.
- **Escopo**: As comparações são limitadas à sua equipe. Sua primeira raspagem de qualquer URL retorna `"new"`, mesmo que outros usuários já a tenham raspado.
- **Correspondência de URL**: Raspagens anteriores são associadas com base na URL de origem exata, ID da equipe, formato `markdown` e `tag`. Mantenha as URLs consistentes entre raspagens.
- **Consistência de parâmetros**: Usar configurações diferentes de `includeTags`, `excludeTags` ou `onlyMainContent` em raspagens da mesma URL produz comparações não confiáveis.
- **Algoritmo de comparação**: O algoritmo é resistente a mudanças em espaços em branco e na ordem do conteúdo. URLs de origem de iframes são ignoradas para lidar com a aleatoriedade de captcha/antibot.
- **Cache**: Solicitações com `changeTracking` contornam o cache do índice. O parâmetro `maxAge` é ignorado.
- **Tratamento de erros**: Monitore o campo `warning` nas respostas e esteja preparado para o caso de o objeto `changeTracking` estar ausente (isso pode ocorrer se a consulta ao banco de dados para a raspagem anterior exceder o tempo limite).

## Cobrança

ModoCustoRastreio básico de mudançasSem custo adicional (créditos padrão de scraping)`git-diff` modeSem custo adicional`json` mode5 créditos por página

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de integração automatizada.