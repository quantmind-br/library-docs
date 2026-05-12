---
title: Agent Development Kit (ADK) - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/llm-sdks-and-frameworks/google-adk
source: sitemap
fetched_at: 2026-03-23T07:34:38.371606-03:00
rendered_js: false
word_count: 402
summary: Este documento orienta sobre a integração do Firecrawl ao Google Agent Development Kit (ADK) via Model Context Protocol (MCP), permitindo que agentes de IA realizem tarefas avançadas de web scraping e extração de dados.
tags:
    - firecrawl
    - google-adk
    - mcp
    - web-scraping
    - ai-agents
    - data-extraction
category: guide
---

Integre o Firecrawl ao Agent Development Kit (ADK) do Google para criar agentes de IA avançados com recursos de web scraping por meio do Model Context Protocol (MCP).

## Visão geral

O Firecrawl oferece um servidor MCP que se integra perfeitamente ao ADK do Google, permitindo que seus agentes façam scraping, crawling e extraiam dados estruturados de qualquer site com eficiência. A integração é compatível tanto com instâncias do Firecrawl em nuvem quanto auto-hospedadas, com HTTP transmissível (streaming) para desempenho ideal.

## Funcionalidades

- Raspagem, rastreamento e descoberta de conteúdo eficientes em qualquer site
- Busca avançada e extração inteligente de conteúdo
- Pesquisa aprofundada e raspagem em lote de alto volume
- Implantação flexível (na nuvem ou auto-hospedada)
- Otimizado para a web moderna com suporte a HTTP por streaming

## Pré-requisitos

- Obtenha uma chave de API do Firecrawl em [firecrawl.dev](https://firecrawl.dev)
- Instale o Google SDK

## Configuração

FerramentaNomeDescriçãoScrape Tool`firecrawl_scrape`Extrair conteúdo de uma única URL com opções avançadasBatch Scrape Tool`firecrawl_batch_scrape`Extrair múltiplas URLs de forma eficiente com controle de taxa integrado e processamento paraleloCheck Batch Status`firecrawl_check_batch_status`Verificar o status de uma operação em loteMap Tool`firecrawl_map`Mapear um site para descobrir todas as URLs indexadasSearch Tool`firecrawl_search`Pesquisar na web e, opcionalmente, extrair conteúdo dos resultados de pesquisaCrawl Tool`firecrawl_crawl`Iniciar um rastreamento assíncrono com opções avançadasCheck Crawl Status`firecrawl_check_crawl_status`Verificar o status de um trabalho de rastreamentoExtract Tool`firecrawl_extract`Extrair informações estruturadas de páginas da web usando recursos de LLM

## Configuração

### Configuração obrigatória

**FIRECRAWL\_API\_KEY**: Sua chave de API do Firecrawl

- Obrigatório ao usar a API em nuvem (padrão)
- Opcional ao usar uma instância auto-hospedada com FIRECRAWL\_API\_URL

### Configuração opcional

**URL da API do Firecrawl (para instâncias self-hosted)**:

- `FIRECRAWL_API_URL`: Endpoint de API personalizado
- Exemplo: `https://firecrawl.your-domain.com`
- Se não for informada, a API em nuvem será utilizada

**Configuração de tentativas (retry)**:

- `FIRECRAWL_RETRY_MAX_ATTEMPTS`: Número máximo de tentativas (padrão: 3)
- `FIRECRAWL_RETRY_INITIAL_DELAY`: Atraso inicial em milissegundos (padrão: 1000)
- `FIRECRAWL_RETRY_MAX_DELAY`: Atraso máximo em milissegundos (padrão: 10000)
- `FIRECRAWL_RETRY_BACKOFF_FACTOR`: Multiplicador de backoff exponencial (padrão: 2)

**Monitoramento do uso de créditos**:

- `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: Limite de aviso (padrão: 1000)
- `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: Limite crítico (padrão: 100)

## Exemplo: Agente de pesquisa na web

```
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

FIRECRAWL_API_KEY = "YOUR-API-KEY"

# Criar um agente de pesquisa
research_agent = Agent(
    model="gemini-2.5-pro",
    name="research_agent",
    description='Um agente de IA que pesquisa tópicos através de scraping e análise de conteúdo web',
    instruction='''Você é um assistente de pesquisa. Quando receber um tópico ou pergunta:
    1. Use a ferramenta de busca para encontrar sites relevantes
    2. Faça scraping das páginas mais relevantes para obter informações detalhadas
    3. Extraia dados estruturados quando necessário
    4. Forneça respostas abrangentes e bem fundamentadas''',
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=f"https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp",
            ),
        )
    ],
)

# Usar o agente
response = research_agent.run("Quais são os recursos mais recentes do Python 3.13?")
print(response)
```

## Boas práticas

1. **Use a ferramenta certa para a tarefa**:
   
   - `firecrawl_search` quando você precisar encontrar primeiro as páginas relevantes
   - `firecrawl_scrape` para páginas individuais
   - `firecrawl_batch_scrape` para múltiplas URLs conhecidas
   - `firecrawl_crawl` para descobrir e extrair sites inteiros
2. **Monitore seu uso**: Configure limites de créditos para evitar consumo inesperado
3. **Lide com erros de forma adequada**: Configure tentativas de repetição (retries) com base no seu caso de uso
4. **Otimize o desempenho**: Use operações em lote ao extrair múltiplas URLs

* * *