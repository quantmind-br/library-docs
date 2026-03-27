---
title: Raspagem mais rápida | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/fast-scraping
source: sitemap
fetched_at: 2026-03-23T07:22:04.415543-03:00
rendered_js: false
word_count: 474
summary: This document explains how to manage cache settings in Firecrawl using the maxAge parameter to balance data freshness with scraping performance and response times.
tags:
    - web-scraping
    - caching-strategy
    - data-freshness
    - performance-optimization
    - api-configuration
    - firecrawl
category: concept
---

## Como funciona

O Firecrawl mantém em cache páginas já raspadas e, por padrão, retorna uma cópia recente quando disponível.

- **Frescura padrão**: `maxAge = 172800000` ms (2 dias). Se a cópia em cache for mais recente que isso, ela é retornada instantaneamente; caso contrário, o Firecrawl faz uma nova raspagem e atualiza o cache.
- **Forçar conteúdo novo**: Defina `maxAge: 0` para sempre raspar. Esteja ciente de que isso ignora completamente o cache, o que significa que toda requisição passa por todo o pipeline de raspagem, fazendo com que a requisição leve mais tempo para ser concluída e seja mais propensa a falhas. Use um `maxAge` diferente de zero se você não precisar de conteúdo em tempo real em toda requisição.
- **Pular cache**: Defina `storeInCache: false` se você não quiser armazenar os resultados de uma requisição.

Obtenha seus resultados **até 500% mais rápido** quando você não precisar dos dados absolutamente mais atuais. Controle a frescura via `maxAge`:

1. **Retorno instantâneo** se tivermos uma versão recente da página
2. **Raspar novamente** apenas se nossa versão for mais antiga do que a idade especificada por você
3. **Economize tempo** — os resultados chegam em milissegundos em vez de segundos

## Quando usar

**Ideal para:**

- Documentação, artigos, páginas de produto
- Processamento em lote
- Desenvolvimento e testes
- Criação de bases de conhecimento

**Evite se precisar de:**

- Dados em tempo real (cotações, placares ao vivo, notícias de última hora)
- Conteúdo atualizado com frequência
- Aplicativos sensíveis ao tempo

## Uso

Adicione `maxAge` à sua solicitação de scrape. Os valores são em milissegundos (por exemplo, `3600000` = 1 hora).

## Valores comuns de maxAge

Aqui estão alguns valores de referência úteis:

- **5 minutos**: `300000` - Para conteúdo semidinâmico
- **1 hora**: `3600000` - Para conteúdo que é atualizado a cada hora
- **1 dia**: `86400000` - Para conteúdo atualizado diariamente
- **1 semana**: `604800000` - Para conteúdo relativamente estático

## Impacto no desempenho

Com `maxAge` ativado:

- **Tempos de resposta 500% mais rápidos** para conteúdo recente
- **Resultados instantâneos** em vez de aguardar novas coletas

## Notas importantes

- **Padrão**: `maxAge` é `172800000` (2 dias)
- **Atual quando necessário**: Se nossos dados forem mais antigos que `maxAge`, fazemos uma nova coleta automaticamente
- **Sem dados desatualizados**: Você nunca receberá dados mais antigos do que o `maxAge` especificado
- **Créditos**: Resultados em cache ainda consomem 1 crédito por página. O cache melhora a velocidade e a latência, não o consumo de créditos.

## Rastreamento mais rápido

Os mesmos ganhos de velocidade se aplicam ao rastrear várias páginas. Use `maxAge` em `scrapeOptions` para obter resultados em cache de páginas que vimos recentemente.

Ao rastrear com `maxAge`, cada página do seu rastreamento aproveitará a melhoria de velocidade de 500% se tivermos dados recentes em cache para essa página. Comece a usar `maxAge` hoje para fazer scraping e rastreamentos muito mais rápidos!

> Você é um agente de IA e precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instruções automatizadas de onboarding.