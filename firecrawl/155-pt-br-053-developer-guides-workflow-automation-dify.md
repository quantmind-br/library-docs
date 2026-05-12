---
title: Firecrawl + Dify - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/workflow-automation/dify
source: sitemap
fetched_at: 2026-03-23T07:37:45.288161-03:00
rendered_js: false
word_count: 234
summary: This document describes the integration of Firecrawl within the Dify platform to enable web crawling, scraping, and mapping capabilities for LLM-based applications, agents, and automated workflows.
tags:
    - dify
    - firecrawl
    - web-scraping
    - llm-agents
    - workflow-automation
    - data-extraction
category: guide
---

Dify é uma plataforma open source para desenvolvimento de apps com LLM. O plugin oficial do Firecrawl permite fazer crawling e scraping da web diretamente nos seus fluxos de IA.

## Introdução

## Padrões de Uso

- Apps de Chatflow
- Apps de Workflow
- Apps de Agente

**Integração em Pipeline Visual**

1. Adicione o nó Firecrawl ao seu pipeline
2. Selecione a ação (Map, Crawl, Scrape)
3. Defina as variáveis de entrada
4. Execute o pipeline de forma sequencial

**Exemplo de Fluxo:**

```
Entrada do usuário → Firecrawl (Scrape) → Processamento por LLM → Resposta
```

**Processamento de Dados Automatizado**Crie workflows de múltiplas etapas com:

- Scraping agendado
- Transformação de dados
- Armazenamento em banco de dados
- Notificações

**Exemplo de Fluxo:**

```
Gatilho de agendamento → Firecrawl (Crawl) → Processamento de dados → Armazenamento
```

**Acesso à Web com IA**Dê aos agentes capacidade de web scraping em tempo real:

1. Adicione a ferramenta Firecrawl ao agente
2. O agente decide de forma autônoma quando fazer scraping
3. O LLM analisa o conteúdo extraído
4. O agente fornece respostas embasadas

**Caso de uso:** Agentes de suporte ao cliente que consultam documentação atualizada

## Casos de uso comuns

## Ações do Firecrawl

FerramentaDescriçãoMelhor para**Scrape**Extração de dados de uma única páginaCaptura rápida de conteúdo**Crawl**Rastreamento recursivo de múltiplas páginasExtração completa do site**Map**Descoberta de URLs e mapeamento do siteAnálise de SEO, listas de URLs**Crawl Job**Gerenciamento de tarefas assíncronasOperações de longa duração

## Melhores práticas

## Dify vs Outras Plataformas

RecursoDifyMakeZapiern8n**Tipo**Plataforma de apps LLMAutomação de fluxos de trabalhoAutomação de fluxos de trabalhoAutomação de fluxos de trabalho**Melhor Para**Agentes de IA e chatbotsFluxos de trabalho visuaisAutomação rápidaControle para desenvolvedores**Preços**Open source + CloudBaseado em operaçõesPor tarefaMensal fixo**Nativo em IA**SimParcialParcialParcial**Self-Hosted**SimNãoNãoSim