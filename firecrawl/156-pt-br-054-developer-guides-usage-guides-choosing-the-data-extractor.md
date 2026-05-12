---
title: Escolhendo o Extrator de Dados | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/developer-guides/usage-guides/choosing-the-data-extractor
source: sitemap
fetched_at: 2026-03-23T07:30:00.812395-03:00
rendered_js: false
word_count: 1035
summary: This document provides a comparative analysis of Firecrawl's data extraction endpoints—agent, extract, and scrape—to help users choose the best tool based on automation needs, URL knowledge, and budget.
tags:
    - web-scraping
    - data-extraction
    - ai-agents
    - firecrawl
    - api-guide
    - json-schema
category: guide
---

Firecrawl oferece três abordagens para extrair dados estruturados de páginas da web. Cada uma atende a diferentes casos de uso, com distintos níveis de automação e controle.

## Comparação Rápida

Recurso`/agent``/extract``/scrape` (modo JSON)**Status**AtivoUse `/agent` em seu lugarAtivo**URL Obrigatória**Não (opcional)Sim (curingas suportados)Sim (URL única)**Escopo**Descoberta em toda a webMúltiplas páginas/domíniosPágina única**Descoberta de URL**Pesquisa autônoma na webRastreia a partir das URLs fornecidasNenhuma**Processamento**AssíncronoAssíncronoSíncrono**Schema Obrigatório**Não (prompt ou schema)Não (prompt ou schema)Não (prompt ou schema)**Preços**Dinâmico (5 execuções gratuitas/dia)Baseado em tokens (1 crédito = 15 tokens)1 crédito/página**Melhor Para**Pesquisa, descoberta, coleta complexaExtração em várias páginas (quando você sabe as URLs)Extração de uma única página conhecida

## 1. Endpoint `/agent`

O endpoint `/agent` é o recurso mais avançado do Firecrawl — o sucessor de `/extract`. Ele usa agentes de IA para pesquisar, navegar e coletar dados de forma autônoma em toda a web.

### Características principais

- **URLs opcionais**: Basta descrever o que você precisa no `prompt`; o uso de URLs é totalmente opcional
- **Navegação autônoma**: O agente pesquisa e navega profundamente em sites para encontrar seus dados
- **Busca profunda na web**: Descobre autonomamente informações em diversos domínios e páginas
- **Processamento paralelo**: Processa múltiplas fontes simultaneamente para resultados mais rápidos
- **Modelos disponíveis**: `spark-1-mini` (padrão, 60% mais barato) e `spark-1-pro` (maior precisão)

### Exemplo

### Melhor caso de uso: Pesquisa e descoberta autônomas

**Cenário**: Você precisa encontrar informações sobre startups de IA que captaram uma rodada de investimento Série A, incluindo seus fundadores e os valores investidos. **Por que `/agent`** : Você não sabe quais sites contêm essas informações. O agent irá pesquisar de forma autônoma na web, navegar até fontes relevantes (Crunchbase, sites de notícias, páginas das empresas) e compilar os dados estruturados para você. Para mais detalhes, consulte a [documentação do Agent](https://docs.firecrawl.dev/pt-BR/features/agent).

* * *

O endpoint `/extract` coleta dados estruturados de URLs especificadas ou de domínios inteiros usando extração com LLMs.

### Características principais

- **URLs normalmente necessárias**: Forneça pelo menos uma URL (aceita curingas como `example.com/*`)
- **Rastreamento de domínio**: Pode rastrear e analisar todas as URLs descobertas em um domínio
- **Aprimoramento com busca na web**: `enableWebSearch` opcional para seguir links fora dos domínios especificados
- **Schema opcional**: Suporta JSON Schema rígido OU prompts em linguagem natural
- **Processamento assíncrono**: Retorna um ID de tarefa para verificação de status

### A limitação de URLs

O desafio fundamental com `/extract` é que você normalmente precisa conhecer as URLs de antemão:

1. **Lacuna de descoberta**: para tarefas como “encontrar startups da YC W24”, você não sabe quais URLs contêm os dados. Você precisaria de uma etapa de pesquisa separada antes de chamar `/extract`.
2. **Busca na web pouco prática**: embora `enableWebSearch` exista, ele é limitado a começar pelas URLs que você fornece — um fluxo de trabalho pouco prático para tarefas de descoberta.
3. **Por que `/agent` foi criado**: `/extract` é bom em extrair de locais conhecidos, mas menos eficaz em descobrir onde os dados estão.

### Exemplo

**Cenário**: Você tem a URL da documentação de um concorrente e quer extrair todos os endpoints de API deles de `docs.competitor.com/*`. **Por que `/extract` funcionou aqui**: Você conhecia exatamente o domínio. Mas, mesmo assim, `/agent` com URLs fornecidas normalmente oferece resultados melhores hoje. Para mais detalhes, consulte a [documentação do Extract](https://docs.firecrawl.dev/pt-BR/features/extract).

* * *

O endpoint `/scrape` com modo JSON é a abordagem mais controlada — ele extrai dados estruturados de uma única URL conhecida usando um LLM para analisar o conteúdo da página no schema que você especificar.

### Características principais

- **Apenas uma URL**: Projetado para extrair dados de uma única página específica por vez
- **URL exata obrigatória**: Você deve conhecer a URL exata que contém os dados
- **Schema opcional**: Pode usar JSON Schema OU apenas um prompt (o LLM escolhe a estrutura)
- **Síncrono**: Retorna os dados imediatamente (sem necessidade de polling de jobs)
- **Formatos adicionais**: Pode combinar extração em JSON com markdown, HTML e capturas de tela em uma única requisição

### Exemplo

**Cenário**: Você está criando uma ferramenta de monitoramento de preços e precisa extrair o preço, o status de estoque e os detalhes do produto de uma página de produto específica para a qual você já tem a URL. **Por que usar `/scrape` com modo JSON**: Você sabe exatamente qual página contém os dados, precisa de uma extração precisa de uma única página e quer resultados síncronos sem a sobrecarga de gerenciar tarefas. Para mais detalhes, consulte a [documentação do modo JSON](https://docs.firecrawl.dev/pt-BR/features/llm-extract).

* * *

## Guia de decisão

**Você conhece a(s) URL(s) exata(s) que contém seus dados?**

- **NÃO** → Use `/agent` (descoberta autônoma na web)
- **SIM**
  
  - **Página única?** → Use `/scrape` com modo JSON
  - **Múltiplas páginas?** → Use `/agent` com URLs (ou `/scrape` em lote)

### Recomendações por Cenário

CenárioEndpoint Recomendado”Encontrar todas as startups de IA e seus financiamentos”`/agent`”Extrair dados desta página de produto específica”`/scrape` (modo JSON)“Obter todos os artigos do blog de competitor.com”`/agent` com URL”Monitorar preços em várias URLs conhecidas”`/scrape` com processamento em lote”Pesquisar empresas em um setor específico”`/agent`”Extrair informações de contato de 50 páginas de empresas conhecidas”`/scrape` com processamento em lote

* * *

## Preços

EndpointCustoObservações`/scrape` (modo JSON)1 crédito/páginaFixo, previsível`/extract`Cobrado por tokens (1 crédito = 15 tokens)Variável de acordo com o conteúdo`/agent`Dinâmico5 execuções gratuitas por dia; varia de acordo com a complexidade

### Exemplo: “Encontre os fundadores da Firecrawl”

EndpointComo funcionaCréditos usados`/scrape`Você encontra a URL manualmente e depois faz scrape de 1 página~1 crédito`/extract`Você fornece URL(s) e ele extrai dados estruturadosVariável (baseado em tokens)`/agent`Basta enviar o prompt — o agente encontra e extrai~100–500 créditos

**Trade-off**: `/scrape` é o mais barato, mas exige que você saiba a URL. `/agent` custa mais, mas cuida da descoberta automaticamente. Para preços detalhados, consulte [Firecrawl Pricing](https://firecrawl.dev/pricing).

* * *

Se você estiver usando `/extract` atualmente, a migração é simples: **Antes (extract):**

```
result = app.extract(
    urls=["https://example.com/*"],
    prompt="Extract product information",
    schema=schema
)
```

**Depois (agente):**

```
result = app.agent(
    urls=["https://example.com"],  # Opcional - pode omitir completamente
    prompt="Extrair informações de produtos de example.com",
    schema=schema,
    model="spark-1-mini"  # ou "spark-1-pro" para maior precisão
)
```

A principal vantagem é que, com `/agent`, você pode simplesmente descrever o que precisa, sem nem precisar informar URLs.

* * *

## Principais pontos

1. **Sabe a URL exata?** Use `/scrape` com modo JSON — é a opção mais barata (1 crédito/página), mais rápida (síncrona) e mais previsível.
2. **Precisa de pesquisa autônoma?** Use `/agent` — ele cuida da descoberta automaticamente, com 5 execuções grátis/dia e depois precificação dinâmica baseada na complexidade.
3. **Migrando de `/extract`** para `/agent` em novos projetos — `/agent` é o sucessor, com recursos mais avançados.
4. **Trade-off entre custo e conveniência**: `/scrape` é mais econômico quando você já conhece suas URLs; `/agent` custa mais, mas elimina a descoberta manual de URLs.

* * *

## Leituras adicionais

- [Documentação do Agent](https://docs.firecrawl.dev/pt-BR/features/agent)
- [Modelos do Agent](https://docs.firecrawl.dev/pt-BR/features/models)
- [Documentação do modo JSON](https://docs.firecrawl.dev/pt-BR/features/llm-extract)
- [Documentação do Extract](https://docs.firecrawl.dev/pt-BR/features/extract)
- [Raspagem em lote](https://docs.firecrawl.dev/pt-BR/features/batch-scrape)