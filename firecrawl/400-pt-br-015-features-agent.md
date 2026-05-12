---
title: Agente | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/agent
source: sitemap
fetched_at: 2026-03-23T07:22:11.470848-03:00
rendered_js: false
word_count: 1170
summary: The Firecrawl /agent API enables autonomous web research and structured data extraction by processing natural language prompts to navigate, find, and collect data across the web.
tags:
    - web-scraping
    - data-extraction
    - ai-agent
    - api-documentation
    - data-collection
    - autonomous-research
category: api
---

Firecrawl `/agent` é uma API mágica que pesquisa, navega e coleta dados da mais ampla variedade de sites, encontrando dados em locais de difícil acesso e descobrindo dados de maneiras que nenhuma outra API consegue. Ele realiza em poucos minutos o que levaria muitas horas para um humano — coleta de dados de ponta a ponta, sem scripts ou trabalho manual. Seja para obter um único dado ou conjuntos de dados completos em escala, o Firecrawl `/agent` trabalha para obter seus dados. **Pense no `/agent` como uma pesquisa profunda por dados, onde quer que eles estejam!**

Agent aproveita tudo o que há de melhor no `/extract` e leva isso além:

- **Nenhuma URL necessária**: Basta descrever o que você precisa via parâmetro `prompt`. URLs são opcionais
- **Pesquisa aprofundada na web**: Pesquisa e navega autonomamente em profundidade em sites para encontrar seus dados
- **Confiável e preciso**: Funciona com uma grande variedade de consultas e casos de uso
- **Mais rápido**: Processa múltiplas fontes em paralelo para resultados mais rápidos

## Usando `/agent`

O único parâmetro obrigatório é `prompt`. Basta descrever quais dados deseja extrair. Para obter uma saída estruturada, forneça um schema JSON. Os SDKs oferecem suporte a Pydantic (Python) e Zod (Node) para definições de schema com segurança de tipos:

### Resposta

```
{
  "success": true,
  "status": "completed",
  "data": {
    "founders": [
      {
        "name": "Eric Ciarla",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      },
      {
        "name": "Nicolas Camara",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      },
      {
        "name": "Caleb Peffer",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      }
    ]
  },
  "expiresAt": "2024-12-15T00:00:00.000Z",
  "creditsUsed": 15
}
```

## Fornecendo URLs (Opcional)

Opcionalmente, você pode fornecer URLs para que o agente se concentre em páginas específicas:

## Status e conclusão de jobs

Jobs de agente são executados de forma assíncrona. Ao enviar um job, você recebe um Job ID que pode usar para verificar o status:

- **Método padrão**: `agent()` aguarda e retorna os resultados finais
- **Iniciar e depois consultar**: use `start_agent` (Python) ou `startAgent` (Node) para obter um Job ID imediatamente e depois verificar o status com `get_agent_status` / `getAgentStatus`

### Estados possíveis

StatusDescrição`processing`O agente ainda está trabalhando na sua requisição`completed`Extração concluída com sucesso`failed`Ocorreu um erro durante a extração`cancelled`O job foi cancelado pelo usuário

#### Exemplo pendente

```
{
  "success": true,
  "status": "processing",
  "expiresAt": "2024-12-15T00:00:00.000Z"
}
```

#### Exemplo concluído

```
{
  "success": true,
  "status": "completed",
  "data": {
    "founders": [
      {
        "name": "Eric Ciarla",
        "role": "Co-founder"
      },
      {
        "name": "Nicolas Camara",
        "role": "Co-founder"
      },
      {
        "name": "Caleb Peffer",
        "role": "Co-founder"
      }
    ]
  },
  "expiresAt": "2024-12-15T00:00:00.000Z",
  "creditsUsed": 15
}
```

Você pode compartilhar execuções de agentes diretamente no Agent Playground. Os links compartilhados são públicos — qualquer pessoa com o link pode ver a saída e a atividade da execução — e você pode revogar o acesso a qualquer momento para desativar o link. As páginas compartilhadas não são indexadas por mecanismos de busca.

## Seleção de modelos

O Firecrawl Agent oferece dois modelos. **O Spark 1 Mini é 60% mais barato** e é o padrão — perfeito para a maioria dos casos de uso. Atualize para o Spark 1 Pro quando precisar de máxima precisão em tarefas complexas.

ModelCostAccuracyBest For`spark-1-mini`**60% mais barato**PadrãoA maioria das tarefas (padrão)`spark-1-pro`PadrãoMais altaPesquisa complexa, extrações críticas

### Spark 1 Mini (Padrão)

`spark-1-mini` é nosso modelo eficiente, ideal para tarefas simples de extração de dados. **Use o Mini quando:**

- Extraindo dados simples (informações de contato, preços, etc.)
- Trabalhando com sites bem estruturados
- Custo-benefício é uma prioridade
- Executando trabalhos de extração em grande escala

### Spark 1 Pro

`spark-1-pro` é o nosso principal modelo, projetado para máxima precisão em tarefas complexas de extração. **Use o Pro quando:**

- Realizar análises competitivas complexas
- Extrair dados que exigem raciocínio profundo
- A precisão for crítica para o seu caso de uso
- Lidar com dados ambíguos ou difíceis de encontrar

### Especificando um modelo

Informe o parâmetro `model` para selecionar qual modelo usar:

## Parâmetros

ParâmetroTipoObrigatórioDescrição`prompt`string**Sim**Descrição em linguagem natural dos dados que você quer extrair (máx. 10.000 caracteres)`model`stringNãoModelo a ser utilizado: `spark-1-mini` (padrão) ou `spark-1-pro``urls`arrayNãoLista opcional de URLs para direcionar a extração`schema`objectNãoschema JSON opcional para saída estruturada`maxCredits`numberNãoNúmero máximo de créditos a serem usados nesta tarefa de agente. O padrão é **2.500** se não for definido. O painel suporta valores de até **2.500**; para limites mais altos, defina `maxCredits` via API (valores acima de 2.500 são sempre tratados como requisições pagas). Se o limite for atingido, o job falha e **nenhum dado é retornado**, mas os créditos consumidos pelo trabalho já realizado ainda serão cobrados.

RecursoAgent (Novo)ExtractURLs obrigatóriasNãoSimVelocidadeMais rápidaPadrãoCustoMais baixoPadrãoConfiabilidadeMaiorPadrãoFlexibilidade das consultasAltaModerada

## Exemplos de Casos de Uso

- **Pesquisa**: “Encontre as 5 principais startups de IA e seus valores de financiamento”
- **Análise de concorrência**: “Compare os planos de preços do Slack e do Microsoft Teams”
- **Coleta de dados**: “Extraia informações de contato de sites de empresas”
- **Resumo de conteúdo**: “Resuma as postagens de blog mais recentes sobre web scraping”

## Upload de CSV no Agent Playground

O [Agent Playground](https://www.firecrawl.dev/app/agent) oferece suporte a upload de CSV para processamento em lote. Seu CSV pode conter uma ou mais colunas de dados de entrada. Por exemplo, uma única coluna com nomes de empresas, ou múltiplas colunas como nome da empresa, produto e URL do site. Cada linha representa um item para o agente processar. Envie seu arquivo CSV, escreva um prompt descrevendo quais dados deseja que o agente encontre para cada linha, defina seus campos de saída e execute. O agente processa cada linha em paralelo e preenche os resultados.

## Referência da API

Confira a [referência da Agent API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/agent) para mais detalhes. Tem alguma sugestão ou precisa de ajuda? Envie um e-mail para [help@firecrawl.com](mailto:help@firecrawl.com).

## Preços

O Firecrawl Agent usa **cobrança dinâmica**, que acompanha a complexidade da sua solicitação de extração de dados. Você paga com base no trabalho efetivamente realizado pelo Agent, garantindo preços justos tanto ao extrair dados simples quanto informações estruturadas complexas de múltiplas fontes.

### Como funciona o preço do Agent

Os preços do Agent são **dinâmicos e baseados em créditos** durante o Research Preview:

- **Extrações simples** (como informações de contato de uma única página) normalmente consomem menos créditos e custam menos
- **Tarefas de pesquisa complexas** (como análise de concorrência em vários domínios) consomem mais créditos, mas refletem o esforço total envolvido
- **Uso transparente** mostra exatamente quantos créditos cada requisição consumiu
- **Conversão de créditos** converte automaticamente o uso de créditos do Agent em créditos para facilitar a cobrança

### Preços para Agentes em Paralelo

Se você estiver executando vários agentes em paralelo com o Spark-1 Fast, o custo se torna muito mais previsível: 10 créditos por célula.

### Começando

**Todos os usuários** recebem **5 execuções gratuitas por dia**, que podem ser usadas tanto no playground quanto na API, para explorar os recursos do Agent sem nenhum custo. O uso adicional é cobrado com base no consumo de créditos e convertido em créditos.

### Gerenciando custos

Agent pode ser caro, mas há algumas maneiras de reduzir o custo:

- **Comece com execuções gratuitas**: Use suas 5 requisições gratuitas diárias para entender os preços
- **Defina o parâmetro `maxCredits`** : Limite seus gastos definindo um número máximo de créditos que você está disposto a usar. O painel limita isso a 2.500 créditos; para definir um limite maior, use o parâmetro `maxCredits` diretamente via API (observação: valores acima de 2.500 são sempre cobrados como requisições pagas)
- **Otimize os prompts**: Prompts mais específicos geralmente usam menos créditos
- **Monitore o uso**: Acompanhe seu consumo pelo painel
- **Ajuste expectativas**: Pesquisas complexas em múltiplos domínios vão consumir mais créditos do que extrações simples de uma única página

Teste o Agent agora em [firecrawl.dev/app/agent](https://www.firecrawl.dev/app/agent) para ver como o uso de créditos escala com seus casos de uso específicos.

> Você é um agente de IA que precisa de uma API key da Firecrawl? Veja [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de onboarding automatizado.