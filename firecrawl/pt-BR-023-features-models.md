---
title: Modelos de Agentes | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/models
source: sitemap
fetched_at: 2026-03-23T07:21:36.396888-03:00
rendered_js: false
word_count: 329
summary: This document outlines the differences between the Spark 1 Mini and Spark 1 Pro models in Firecrawl, providing guidance on choosing the appropriate model based on task complexity, cost, and precision requirements.
tags:
    - firecrawl
    - data-extraction
    - model-selection
    - api-configuration
    - ai-agents
category: guide
---

O Firecrawl Agent oferece dois modelos otimizados para diferentes casos de uso. Escolha o modelo adequado de acordo com a complexidade da extração e suas necessidades de custo.

## Modelos Disponíveis

ModeloCustoPrecisãoIdeal para`spark-1-mini`**60% mais barato**PadrãoA maioria das tarefas (padrão)`spark-1-pro`PadrãoMais altaPesquisa complexa, extrações críticas

## Spark 1 Mini (Padrão)

`spark-1-mini` é nosso modelo eficiente, ideal para tarefas simples de extração de dados. **Use o Mini quando:**

- Estiver extraindo dados simples (informações de contato, preços, etc.)
- Estiver trabalhando com sites bem estruturados
- O custo-benefício for prioridade
- Estiver executando tarefas de extração em alto volume

**Exemplos de uso:**

- Extrair preços de produtos de sites de e-commerce
- Coletar informações de contato em páginas de empresas
- Obter metadados básicos de artigos
- Fazer consultas simples de dados

## Spark 1 Pro

`spark-1-pro` é nosso modelo carro-chefe, projetado para máxima precisão em tarefas de extração complexas. **Use o Pro quando:**

- Executar análises competitivas complexas
- Extrair dados que exigem raciocínio profundo
- A precisão for crítica para o seu caso de uso
- Lidar com dados ambíguos ou difíceis de encontrar

**Exemplos de casos de uso:**

- Análise competitiva em múltiplos domínios
- Tarefas de pesquisa complexas que exigem raciocínio
- Extração de informações detalhadas a partir de múltiplas fontes
- Coleta crítica de inteligência de negócios

## Especificando um modelo

Passe o parâmetro `model` para selecionar qual modelo será usado:

## Comparação de modelos

RecursoSpark 1 MiniSpark 1 Pro**Custo**60% mais baratoPadrão**Precisão**PadrãoMais alta**Velocidade**RápidaRápida**Melhor para**A maioria das tarefasTarefas complexas**Raciocínio**PadrãoAvançado**Multidomínio**BomExcelente

## Preços por modelo

Ambos os modelos usam um modelo de preços dinâmico baseado em créditos que escala com a complexidade da tarefa:

- **Spark 1 Mini**: Usa aproximadamente 60% menos créditos que o Pro para tarefas equivalentes
- **Spark 1 Pro**: Consumo padrão de créditos para máxima precisão

## Escolhendo o Modelo Adequado

```
                    ┌─────────────────────────────────┐
                    │   What type of task?            │
                    └─────────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  Simple/Direct  │           │ Complex/Research│
          │  extraction     │           │ multi-domain    │
          └─────────────────┘           └─────────────────┘
                    │                             │
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  spark-1-mini   │           │  spark-1-pro    │
          │  (60% mais barato) │        │  (maior precisão) │
          └─────────────────┘           └─────────────────┘
```

## Referência da API

Veja a [Referência da API do agente](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/agent) para conferir a documentação completa dos parâmetros. Tem dúvidas sobre qual modelo usar? Envie um e-mail para [help@firecrawl.com](mailto:help@firecrawl.com).

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Veja [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de integração automatizada.