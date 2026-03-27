---
title: Crawlear | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/crawl
source: sitemap
fetched_at: 2026-03-23T07:21:48.917275-03:00
rendered_js: false
word_count: 1039
summary: This document explains how to use the Firecrawl crawl API to recursively discover and extract data from multiple webpages, including configuration options, SDK usage, and webhook integration.
tags:
    - web-scraping
    - data-extraction
    - api-integration
    - crawling
    - webhooks
    - automation
category: api
---

O Crawlear envia uma URL ao Firecrawl e descobre e extrai, de forma recursiva, todas as subpáginas acessíveis. Ele lida automaticamente com sitemaps, renderização de JavaScript e limites de taxa, retornando markdown limpo ou dados estruturados para cada página.

- Descobre páginas por meio do sitemap e da navegação recursiva por links
- Suporta filtragem de caminho, limites de profundidade e controle de subdomínios/links externos
- Retorna resultados via polling, WebSocket ou webhook

## Instalação

## Uso básico

Envie um trabalho de rastreamento chamando `POST /v2/crawl` com uma URL inicial. O endpoint retorna um ID do trabalho que você usa para consultar os resultados.

### Opções de scrape

Todas as opções do [endpoint Scrape](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/scrape) estão disponíveis no crawl via `scrapeOptions` (JS) / `scrape_options` (Python). Elas se aplicam a cada página que o crawler coleta, incluindo formatos, proxy, cache, ações, localização e tags.

## Verificando o status do rastreamento

Use o ID do job para consultar o status do rastreamento e obter os resultados.

### Tratamento de respostas

A resposta varia conforme o status da varredura. Para respostas incompletas ou grandes (acima de 10 MB), é fornecido um parâmetro de URL `next`. Você deve requisitar essa URL para obter os próximos 10 MB de dados. Se o parâmetro `next` estiver ausente, isso indica o fim dos dados da varredura.

## Métodos do SDK

Existem duas maneiras de usar o crawl com o SDK.

### Crawl e aguarde

O método `crawl` aguarda a conclusão do crawl e retorna a resposta completa. Faz a paginação automaticamente. Isso é recomendado para a maioria dos casos de uso.

A resposta inclui o status do crawl e todos os dados extraídos:

### Inicie e verifique depois

O método `startCrawl` / `start_crawl` retorna imediatamente com um ID de crawl. Depois, você verifica o status manualmente. Isso é útil para crawls de longa duração ou lógica de polling personalizada.

A resposta inicial retorna o ID do job:

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

O método watcher fornece atualizações em tempo real conforme as páginas são rastreadas. Inicie um crawl e, em seguida, assine os eventos para processar os dados imediatamente.

## Webhooks

Você pode configurar webhooks para receber notificações em tempo real conforme o rastreamento avança. Isso permite processar páginas à medida que são coletadas, em vez de esperar a conclusão de todo o rastreamento.

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

### Tipos de evento

EventoDescrição`crawl.started`Disparado quando o crawl é iniciado`crawl.page`Disparado para cada página extraída com sucesso`crawl.completed`Disparado quando o crawl é concluído`crawl.failed`Disparado se ocorrer um erro durante o crawl

### Payload

```
{
  "success": true,
  "type": "crawl.page",
  "id": "crawl-job-id",
  "data": [...], // Dados da página para eventos 'page'
  "metadata": {}, // Your custom metadata
  "error": null
}
```

### Verificando assinaturas de webhook

Toda requisição de webhook do Firecrawl inclui um cabeçalho `X-Firecrawl-Signature` contendo uma assinatura HMAC-SHA256. Sempre verifique essa assinatura para garantir que o webhook é autêntico e não foi adulterado.

1. Obtenha seu segredo de webhook na [aba Advanced](https://www.firecrawl.dev/app/settings?tab=advanced) das configurações da sua conta
2. Extraia a assinatura do cabeçalho `X-Firecrawl-Signature`
3. Calcule o HMAC-SHA256 do corpo bruto da requisição usando o seu segredo
4. Compare com o cabeçalho de assinatura usando uma função com proteção contra ataques de timing (tempo constante)

Para exemplos completos de implementação em JavaScript e Python, consulte a [documentação de segurança de webhooks](https://docs.firecrawl.dev/pt-BR/webhooks/security). Para a documentação completa sobre webhooks, incluindo payloads detalhados de eventos, estrutura de payload, configuração avançada e solução de problemas, consulte a [documentação de Webhooks](https://docs.firecrawl.dev/pt-BR/webhooks/overview).

## Referência de configuração

O conjunto completo de parâmetros disponíveis ao enviar um trabalho de crawl:

ParâmetroTipoPadrãoDescrição`url``string`(obrigatório)A URL inicial a partir da qual o crawl será executado`limit``integer``10000`Número máximo de páginas a rastrear`maxDiscoveryDepth``integer`(nenhum)Profundidade máxima a partir da URL raiz com base em saltos de descoberta de links, e não no número de segmentos `/` na URL. Cada vez que uma nova URL é encontrada em uma página, ela recebe uma profundidade um nível acima da página em que foi descoberta. O site raiz e as páginas do sitemap têm profundidade de descoberta 0. As páginas na profundidade máxima ainda são extraídas, mas os links nelas não são seguidos.`includePaths``string[]`(nenhum)Padrões regex de pathname de URL a incluir. Apenas os caminhos correspondentes são rastreados.`excludePaths``string[]`(nenhum)Padrões regex de pathname de URL a excluir do crawl`regexOnFullURL``boolean``false`Faz a correspondência de `includePaths`/`excludePaths` com a URL completa (incluindo parâmetros de consulta), em vez de apenas o pathname`crawlEntireDomain``boolean``false`Segue links internos para URLs irmãs ou pai, não apenas caminhos filhos`allowSubdomains``boolean``false`Segue links para subdomínios do domínio principal`allowExternalLinks``boolean``false`Segue links para sites externos`sitemap``string``"include"`Tratamento do sitemap: `"include"` (padrão), `"skip"` ou `"only"``ignoreQueryParameters``boolean``false`Evita raspar novamente o mesmo caminho com parâmetros de consulta diferentes`delay``number`(nenhum)Intervalo, em segundos, entre raspagens para respeitar os limites de taxa`maxConcurrency``integer`(nenhum)Número máximo de raspagens simultâneas. O padrão é o limite de simultaneidade da sua equipe.`scrapeOptions``object`(nenhum)Opções aplicadas a cada página raspada (formatos, proxy, cache, ações etc.)`webhook``object`(nenhum)Configuração de webhook para notificações em tempo real`prompt``string`(nenhum)Prompt em linguagem natural para gerar opções de crawl. Parâmetros definidos explicitamente substituem os equivalentes gerados.

## Detalhes importantes

- **Descoberta de sitemap**: Por padrão, o crawler inclui o sitemap do site para descobrir URLs (`sitemap: "include"`). Se você definir `sitemap: "skip"`, apenas páginas acessíveis por links HTML a partir da URL raiz serão encontradas. Recursos como PDFs ou páginas em níveis mais profundos, listados no sitemap mas não vinculados diretamente no HTML, não serão encontrados. Para obter a cobertura máxima, mantenha a configuração padrão.
- **Uso de créditos**: Cada página rastreada custa 1 crédito. O modo JSON adiciona 4 créditos por página, o proxy avançado adiciona 4 créditos por página, e a análise de PDF custa 1 crédito por página do PDF.
- **Expiração dos resultados**: Os resultados do job ficam disponíveis via API por 24 horas após a conclusão. Depois disso, consulte os resultados nos [logs de atividade](https://www.firecrawl.dev/app/logs).
- **Erros de crawl**: O array `data` contém as páginas que o Firecrawl extraiu com sucesso. Use o endpoint [Get Crawl Errors](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/crawl-get-errors) para recuperar as páginas que falharam devido a erros de rede, timeouts ou bloqueios por robots.txt.
- **Resultados não determinísticos**: Os resultados do crawl podem variar entre execuções com a mesma configuração. As páginas são extraídas de forma concorrente, então a ordem em que os links são descobertos depende do timing da rede e de quais páginas terminam de carregar primeiro. Isso significa que diferentes ramificações de um site podem ser exploradas em extensões diferentes perto do limite de profundidade, especialmente em valores mais altos de `maxDiscoveryDepth`. Para obter resultados mais determinísticos, defina `maxConcurrency` como `1` ou use `sitemap: "only"` se o site tiver um sitemap abrangente.

> Você é um agente de IA que precisa de uma API key do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver as instruções de onboarding automatizado.