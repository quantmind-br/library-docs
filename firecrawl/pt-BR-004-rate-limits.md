---
title: Limites de taxa | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/rate-limits
source: sitemap
fetched_at: 2026-03-23T07:27:30.405123-03:00
rendered_js: false
word_count: 456
summary: This document outlines the billing model, concurrency limits for web browsers, and API rate limits associated with the Firecrawl service plans.
tags:
    - billing-policy
    - api-rate-limits
    - concurrent-browsers
    - subscription-plans
    - service-limits
category: reference
---

## Modelo de cobrança

Firecrawl usa planos mensais por assinatura. Não oferecemos um modelo exclusivamente pay-as-you-go, mas nosso **recurso de recarga automática** oferece escala flexível — após assinar um plano, você pode comprar créditos adicionais automaticamente quando ficar abaixo de um limite predefinido, com preços melhores em pacotes maiores de recarga automática. Para testar antes de assumir um plano maior, comece pelo plano Free ou Hobby. Downgrades de plano são agendados para entrar em vigor na próxima renovação, e não são concedidos créditos proporcionais pelo tempo não utilizado.

## Limites de navegadores concorrentes

“Navegadores concorrentes” indica quantas páginas da web o Firecrawl pode processar ao mesmo tempo. Seu plano determina quantos desses trabalhos podem ser executados simultaneamente — se você exceder esse limite, trabalhos adicionais ficarão em fila de espera até que haja recursos disponíveis. Observe que o tempo gasto esperando na fila é contabilizado no parâmetro [`timeout`](https://docs.firecrawl.dev/pt-BR/advanced-scraping-guide#timing-and-cache) da requisição, portanto você pode definir um timeout menor para falhar mais rápido em vez de esperar. Você também pode verificar a disponibilidade atual por meio do endpoint [Queue Status](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/queue-status).

### Planos atuais

PlanoConcurrent BrowsersMáximo de jobs na filaFree250,000Hobby550,000Standard50100,000Growth100200,000Scale / Enterprise150+300,000+

Cada equipe tem um número máximo de jobs que podem ficar aguardando na fila de concorrência. Se você exceder esse limite, novos jobs serão rejeitados com o código de status `429` até que os jobs existentes sejam concluídos. Para planos maiores com limites de concorrência personalizados, o máximo de jobs na fila é 2.000 vezes o seu limite de concorrência, com teto de 2.000.000. Se você precisar de limites de concorrência mais altos, [entre em contato conosco sobre os planos Enterprise](https://firecrawl.dev/enterprise).

PlanoNavegadores concorrentesMáximo de jobs na filaFree250,000Starter50100,000Explorer100200,000Pro200400,000

## Limites de Taxa da API

Os limites de taxa são medidos em solicitações por minuto e existem principalmente para prevenir abusos. Quando tudo estiver configurado corretamente, o seu verdadeiro gargalo será o número de navegadores em execução simultânea.

### Planos atuais

Plano/scrape/map/crawl/search/agent/crawl/status/agent/statusGratuito101015101500500Hobby1001001550100150025000Padrão50050050250500150025000Crescimento5000500025025001000150025000Escala75007500750750010002500025000

Esses limites de uso são aplicados para garantir o uso justo e a disponibilidade da API para todos os usuários. Se você precisar de limites mais altos, entre em contato conosco pelo e-mail [help@firecrawl.com](mailto:help@firecrawl.com) para discutir planos personalizados.

Os endpoints de extração compartilham os mesmos rate limits dos endpoints /agent correspondentes.

### Endpoints de Batch Scrape

Os endpoints de batch scrape compartilham os mesmos limites de taxa dos endpoints /crawl correspondentes.

### Sessões do navegador

Enquanto o endpoint /browser estiver em prévia, cada equipe pode ter até 20 sessões de navegador ativas ao mesmo tempo. Se você exceder esse limite, novas requisições de sessão retornarão um código de status `429` até que as sessões existentes sejam encerradas.

### Agente FIRE-1

Solicitações que envolvem o agente FIRE-1 têm limites de uso separados, contabilizados de forma independente para cada endpoint:

EndpointLimite de uso (requisições/min)/scrape10/extract10

Plano/extract (requisições/min)/extract/status (requisições/min)Starter10025000Explorer50025000Pro100025000