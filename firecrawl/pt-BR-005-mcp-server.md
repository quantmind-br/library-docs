---
title: Servidor MCP do Firecrawl
url: https://docs.firecrawl.dev/pt-BR/mcp-server
source: sitemap
fetched_at: 2026-03-23T07:29:08.563443-03:00
rendered_js: false
word_count: 2113
summary: This document provides instructions for installing and configuring the Firecrawl Model Context Protocol (MCP) server to enable web scraping and data extraction capabilities within various IDEs and AI development environments.
tags:
    - mcp
    - firecrawl
    - web-scraping
    - integration
    - developer-tools
    - api-configuration
category: configuration
---

Uma implementação de servidor do Model Context Protocol (MCP) que integra o [Firecrawl](https://github.com/firecrawl/firecrawl) para recursos de web scraping. Nosso servidor MCP é de código aberto e está disponível no [GitHub](https://github.com/firecrawl/firecrawl-mcp-server).

## Recursos

- Web scraping, rastreamento e descoberta
- Busca e extração de conteúdo
- Pesquisa avançada com agente autônomo
- Gerenciamento de sessão de navegador
- Suporte em nuvem e auto-hospedado
- Suporte a HTTP com streaming

## Instalação

Você pode usar nossa URL hospedada ou executar o servidor localmente. Obtenha sua chave de API em [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)

### URL hospedada remotamente

```
https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp
```

### Executando com npx

```
env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

### Instalação manual

```
npm install -g firecrawl-mcp
```

### Executando no Cursor

[![Adicionar o servidor MCP do Firecrawl ao Cursor](https://cursor.com/deeplink/mcp-install-dark.png)](cursor://anysphere.cursor-deeplink/mcp/install?name=firecrawl&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImZpcmVjcmF3bC1tY3AiXSwiZW52Ijp7IkZJUkVDUkFXTF9BUElfS0VZIjoiWU9VUi1BUEktS0VZIn19)

#### Instalação manual

Configurando o Cursor 🖥️ Observação: requer o Cursor na versão 0.45.6 ou superior. Para obter as instruções de configuração mais atualizadas, consulte a documentação oficial do Cursor sobre como configurar servidores MCP: [Guia de configuração de servidor MCP do Cursor](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers) Para configurar o Firecrawl MCP no Cursor **v0.48.6**

1. Abra as Configurações do Cursor
2. Vá em Features &gt; MCP Servers
3. Clique em ”+ Add new global MCP server”
4. Insira o seguinte código:
   
   ```
   {
     "mcpServers": {
       "firecrawl-mcp": {
         "command": "npx",
         "args": ["-y", "firecrawl-mcp"],
         "env": {
           "FIRECRAWL_API_KEY": "YOUR-API-KEY"
         }
       }
     }
   }
   ```

Para configurar o Firecrawl MCP no Cursor **v0.45.6**

1. Abra as Configurações do Cursor
2. Vá em Features &gt; MCP Servers
3. Clique em ”+ Add New MCP Server”
4. Insira o seguinte:
   
   - Name: “firecrawl-mcp” (ou o nome de sua preferência)
   - Type: “command”
   - Command: `env FIRECRAWL_API_KEY=your-api-key npx -y firecrawl-mcp`

> Se você estiver no Windows e tiver problemas, tente `cmd /c "set FIRECRAWL_API_KEY=your-api-key && npx -y firecrawl-mcp"`

Substitua `your-api-key` pela sua chave de API do Firecrawl. Se você ainda não tiver uma, crie uma conta e obtenha-a em [https://www.firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) Após adicionar, atualize a lista de servidores MCP para ver as novas ferramentas. O Composer Agent usará automaticamente o Firecrawl MCP quando apropriado, mas você pode solicitá-lo explicitamente descrevendo suas necessidades de web scraping. Acesse o Composer com Command+L (Mac), selecione “Agent” ao lado do botão de envio e insira sua consulta.

### Executando no Windsurf

Adicione isto ao arquivo `./codeium/windsurf/model_config.json`:

```
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "SUA_API_KEY"
      }
    }
  }
}
```

### Executando no modo HTTP com streaming

Para executar o servidor localmente usando o transporte HTTP com streaming em vez do transporte `stdio` padrão:

```
env HTTP_STREAMABLE_SERVER=true FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

Use a URL: [http://localhost:3000/v2/mcp](http://localhost:3000/v2/mcp) ou [https://mcp.firecrawl.dev/{FIRECRAWL\_API\_KEY}/v2/mcp](https://mcp.firecrawl.dev/%7BFIRECRAWL_API_KEY%7D/v2/mcp)

### Instalação via Smithery (legado)

Para instalar o Firecrawl no Claude Desktop automaticamente usando o [Smithery](https://smithery.ai/server/@mendableai/mcp-server-firecrawl):

```
npx -y @smithery/cli install @mendableai/mcp-server-firecrawl --client claude
```

### Executando no VS Code

Para instalar com um clique, use um dos botões de instalação abaixo… [![Instalar com NPX no VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D) [![Instalar com NPX no VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D&quality=insiders) Para instalação manual, adicione o seguinte bloco JSON ao arquivo User Settings (JSON) no VS Code. Você pode fazer isso pressionando `Ctrl + Shift + P` e digitando `Preferences: Open User Settings (JSON)`.

```
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "apiKey",
        "description": "Chave de API do Firecrawl",
        "password": true
      }
    ],
    "servers": {
      "firecrawl": {
        "command": "npx",
        "args": ["-y", "firecrawl-mcp"],
        "env": {
          "FIRECRAWL_API_KEY": "${input:apiKey}"
        }
      }
    }
  }
}
```

Opcionalmente, você também pode adicioná-lo a um arquivo chamado `.vscode/mcp.json` no seu espaço de trabalho. Isso permitirá que você compartilhe essa configuração com outras pessoas:

```
{
  "inputs": [
    {
      "type": "promptString",
      "id": "apiKey",
      "description": "Chave da API do Firecrawl",
      "password": true
    }
  ],
  "servers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "${input:apiKey}"
      }
    }
  }
}
```

**Nota:** Alguns usuários relataram problemas ao adicionar o servidor MCP ao VS Code devido à forma como ele valida JSON com um formato de schema desatualizado ([microsoft/vscode#155379](https://github.com/microsoft/vscode/issues/155379)). Isso afeta várias ferramentas MCP, incluindo Firecrawl. **Solução alternativa:** Desative a validação de JSON no VS Code para permitir que o servidor MCP seja carregado corretamente. Consulte a referência: [directus/directus#25906 (comment)](https://github.com/directus/directus/issues/25906#issuecomment-3369169513). O servidor MCP continua funcionando normalmente quando invocado por outras extensões, mas o problema ocorre especificamente ao registrá-lo diretamente na lista de servidores MCP. Planejamos adicionar orientações assim que o VS Code atualizar a validação de schema.

### Executando no Claude Desktop

Adicione o seguinte ao arquivo de configuração do Claude:

```
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

### Executando no Claude Code

Adicione o servidor MCP do Firecrawl usando a CLI do Claude Code. Você pode usar a URL hospedada remotamente ou executar localmente:

```
# URL hospedada remotamente (recomendado)
claude mcp add firecrawl --url https://mcp.firecrawl.dev/your-api-key/v2/mcp

# Ou execute localmente via npx
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

### Executando no Google Antigravity

O Google Antigravity permite configurar servidores MCP diretamente pela interface do Agent. ![Instalação do MCP no Antigravity](https://mintcdn.com/firecrawl/rxzXygFiVc0TDh5X/images/guides/mcp/antigravity-mcp-installation.gif?s=19297c26dad5ed191862571618ce8c0a)

1. Abra a barra lateral do Agent no Editor ou na visualização Agent Manager
2. Clique no menu ”…” (More Actions) e selecione **MCP Servers**
3. Selecione **View raw config** para abrir o arquivo local `mcp_config.json`
4. Adicione a seguinte configuração:

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_FIRECRAWL_API_KEY"
      }
    }
  }
}
```

5. Salve o arquivo e clique em **Refresh** na interface Antigravity MCP para ver as novas ferramentas

Substitua `YOUR_FIRECRAWL_API_KEY` pela sua chave de API de [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys).

### Executando no n8n

Para conectar o servidor MCP do Firecrawl no n8n:

1. Obtenha sua chave de API da Firecrawl em [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)
2. No seu fluxo de trabalho do n8n, adicione um nó **AI Agent**
3. Na configuração do nó AI Agent, adicione uma nova **Tool**
4. Selecione **MCP Client Tool** como o tipo de ferramenta
5. Insira o endpoint do servidor MCP (substitua `{YOUR_FIRECRAWL_API_KEY}` pela sua chave de API real):

```
  https://mcp.firecrawl.dev/{SUA_CHAVE_API_FIRECRAWL}/v2/mcp
```

6. Defina **Server Transport** como **HTTP Streamable**
7. Defina **Authentication** como **None**
8. Em **Tools to include**, você pode selecionar **All**, **Selected** ou **All Except** – isso expõe as ferramentas do Firecrawl (scrape, crawl, map, search, extract, etc.)

Para implantações autohospedadas, execute o servidor MCP com npx e habilite o modo de transporte HTTP:

```
env HTTP_STREAMABLE_SERVER=true \
    FIRECRAWL_API_KEY=fc-YOUR_API_KEY \
    FIRECRAWL_API_URL=YOUR_FIRECRAWL_INSTANCE \
    npx -y firecrawl-mcp
```

Isso iniciará o servidor em `http://localhost:3000/v2/mcp`, que você pode usar no seu workflow do n8n como endpoint. A variável de ambiente `HTTP_STREAMABLE_SERVER=true` é obrigatória, já que o n8n precisa de transporte HTTP.

## Configuração

### Variáveis de Ambiente

#### Necessário para a API em nuvem

- `FIRECRAWL_API_KEY`: Sua chave de API do Firecrawl
  
  - Obrigatória ao usar a API em nuvem (padrão)
  - Opcional ao usar uma instância autogerenciada com `FIRECRAWL_API_URL`
- `FIRECRAWL_API_URL` (opcional): Endpoint de API personalizado para instâncias autogerenciadas
  
  - Exemplo: `https://firecrawl.seu-dominio.com`
  - Se não for fornecido, a API em nuvem será usada (requer chave de API)

#### Configurações opcionais

##### Configuração de tentativas

- `FIRECRAWL_RETRY_MAX_ATTEMPTS`: Número máximo de tentativas (padrão: 3)
- `FIRECRAWL_RETRY_INITIAL_DELAY`: Atraso inicial, em milissegundos, antes da primeira nova tentativa (padrão: 1000)
- `FIRECRAWL_RETRY_MAX_DELAY`: Atraso máximo, em milissegundos, entre novas tentativas (padrão: 10000)
- `FIRECRAWL_RETRY_BACKOFF_FACTOR`: Multiplicador de backoff exponencial (padrão: 2)

##### Monitoramento do uso de créditos

- `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: Limite de aviso para uso de créditos (padrão: 1000)
- `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: Limite crítico para uso de créditos (padrão: 100)

### Exemplos de configuração

Para uso da API em nuvem com tentativas personalizadas e monitoramento de créditos:

```
# Necessário para a API em nuvem
export FIRECRAWL_API_KEY=your-api-key

# Configuração opcional de tentativas
export FIRECRAWL_RETRY_MAX_ATTEMPTS=5        # Aumentar o número máximo de tentativas
export FIRECRAWL_RETRY_INITIAL_DELAY=2000    # Começar com atraso de 2s
export FIRECRAWL_RETRY_MAX_DELAY=30000       # Atraso máximo de 30s
export FIRECRAWL_RETRY_BACKOFF_FACTOR=3      # Backoff mais agressivo

# Monitoramento opcional de créditos
export FIRECRAWL_CREDIT_WARNING_THRESHOLD=2000    # Aviso a partir de 2000 créditos
export FIRECRAWL_CREDIT_CRITICAL_THRESHOLD=500    # Crítico a partir de 500 créditos
```

Para instâncias auto-hospedadas:

```
# Necessário para auto-hospedado
export FIRECRAWL_API_URL=https://firecrawl.seu-dominio.com

# Autenticação opcional para auto-hospedado
export FIRECRAWL_API_KEY=sua-api-key  # Se sua instância exigir autenticação

# Configuração personalizada de novas tentativas
export FIRECRAWL_RETRY_MAX_ATTEMPTS=10
export FIRECRAWL_RETRY_INITIAL_DELAY=500     # Comece com novas tentativas mais rápidas
```

### Configuração personalizada com o Claude Desktop

Adicione o seguinte ao seu `claude_desktop_config.json`:

```
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY_HERE",

        "FIRECRAWL_RETRY_MAX_ATTEMPTS": "5",
        "FIRECRAWL_RETRY_INITIAL_DELAY": "2000",
        "FIRECRAWL_RETRY_MAX_DELAY": "30000",
        "FIRECRAWL_RETRY_BACKOFF_FACTOR": "3",

        "FIRECRAWL_CREDIT_WARNING_THRESHOLD": "2000",
        "FIRECRAWL_CREDIT_CRITICAL_THRESHOLD": "500"
      }
    }
  }
}
```

### Configuração do sistema

O servidor inclui vários parâmetros configuráveis que podem ser definidos por meio de variáveis de ambiente. A seguir estão os valores padrão caso não sejam configurados:

```
const CONFIG = {
  retry: {
    maxAttempts: 3, // Number of retry attempts for rate-limited requests
    initialDelay: 1000, // Initial delay before first retry (in milliseconds)
    maxDelay: 10000, // Maximum delay between retries (in milliseconds)
    backoffFactor: 2, // Multiplier for exponential backoff
  },
  credit: {
    warningThreshold: 1000, // Warn when credit usage reaches this level
    criticalThreshold: 100, // Alerta crítico quando o uso de créditos atingir este nível
  },
};
```

Essas configurações controlam:

1. **Comportamento de tentativas (retries)**
   
   - Tenta novamente automaticamente as requisições que falharam devido a limites de taxa
   - Usa backoff exponencial para evitar sobrecarregar a API
   - Exemplo: com as configurações padrão, as novas tentativas serão feitas em:
     
     - 1ª tentativa: atraso de 1 segundo
     - 2ª tentativa: atraso de 2 segundos
     - 3ª tentativa: atraso de 4 segundos (limitado por maxDelay)
2. **Monitoramento do uso de créditos**
   
   - Acompanha o consumo de créditos da API para uso em nuvem
   - Fornece avisos em limites definidos
   - Ajuda a evitar interrupções inesperadas do serviço
   - Exemplo: com as configurações padrão:
     
     - Aviso com 1000 créditos restantes
     - Alerta crítico com 100 créditos restantes

### Limitação de Taxa e Processamento em Lote

O servidor utiliza os recursos integrados de limitação de taxa e processamento em lote do Firecrawl:

- Tratamento automático de limitação de taxa com backoff exponencial
- Processamento paralelo eficiente para operações em lote
- Enfileiramento e controle inteligente de requisições
- Novas tentativas automáticas em caso de erros transitórios

Extraia conteúdo de uma única URL com opções avançadas.

```
{
  "name": "firecrawl_scrape",
  "arguments": {
    "url": "https://example.com",
    "formatos": ["markdown"],
    "onlyMainContent": true,
    "waitFor": 1000,
    "mobile": false,
    "includeTags": ["article", "main"],
    "excludeTags": ["nav", "footer"],
    "skipTlsVerification": false
  }
}
```

Mapeie um site para descobrir todas as URLs indexadas do site.

```
{
  "name": "firecrawl_map",
  "arguments": {
    "url": "https://example.com",
    "search": "blog",
    "sitemap": "include",
    "includeSubdomains": false,
    "limit": 100,
    "ignoreQueryParameters": true
  }
}
```

- `url`: A URL base do site a ser mapeado
- `search`: Termo de pesquisa opcional para filtrar URLs
- `sitemap`: Controla o uso do sitemap — “include”, “skip” ou “only”
- `includeSubdomains`: Se deve incluir subdomínios no mapeamento
- `limit`: Número máximo de URLs a serem retornadas
- `ignoreQueryParameters`: Se deve ignorar parâmetros de consulta ao mapear

**Ideal para:** Descobrir URLs em um site antes de decidir o que extrair; encontrar seções específicas de um site. **Retorna:** Array de URLs encontradas no site.

Pesquise na web e, opcionalmente, extraia conteúdo dos resultados da busca.

```
{
  "name": "firecrawl_search",
  "arguments": {
    "query": "sua consulta de busca",
    "limit": 5,
    "location": "United States",
    "tbs": "qdr:m",
    "scrapeOptions": {
      "formats": ["markdown"],
      "onlyMainContent": true
    }
  }
}
```

- `query`: A string da consulta de busca (obrigatório)
- `limit`: Número máximo de resultados a serem retornados
- `location`: Localização geográfica para os resultados de busca
- `tbs`: Filtro de busca baseado em tempo (por exemplo, `qdr:d` para o último dia, `qdr:w` para a última semana, `qdr:m` para o último mês)
- `filter`: Filtro adicional de busca
- `sources`: Array de tipos de fonte a serem pesquisados (`web`, `images`, `news`)
- `scrapeOptions`: Opções para scraping das páginas de resultados de busca
- `enterprise`: Array de opções de enterprise (`default`, `anon`, `zdr`)

Inicia um rastreamento assíncrono com opções avançadas.

```
{
  "name": "firecrawl_crawl",
  "arguments": {
    "url": "https://example.com",
    "maxDiscoveryDepth": 2,
    "limit": 100,
    "allowExternalLinks": false,
    "deduplicateSimilarURLs": true
  }
}
```

### 5. Verificar status do crawl (`firecrawl_check_crawl_status`)

Verifique o status de uma tarefa de crawl.

```
{
  "name": "firecrawl_check_crawl_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

**Retorna:** Status e progresso da tarefa de rastreamento, incluindo os resultados, se disponíveis.

Extraia informações estruturadas de páginas da web usando LLMs. Suporta extração tanto com IA em nuvem quanto com LLMs auto-hospedados.

```
{
  "name": "firecrawl_extract",
  "arguments": {
    "urls": ["https://example.com/page1", "https://example.com/page2"],
    "prompt": "Extract product information including name, price, and description",
    "schema": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "price": { "type": "number" },
        "description": { "type": "string" }
      },
      "required": ["name", "price"]
    },
    "allowExternalLinks": false,
    "enableWebSearch": false,
    "includeSubdomains": false
  }
}
```

Exemplo de resposta:

```
{
  "content": [
    {
      "type": "text",
      "text": {
        "name": "Example Product",
        "price": 99.99,
        "description": "This is an example product description"
      }
    }
  ],
  "isError": false
}
```

- `urls`: Array de URLs das quais extrair informações
- `prompt`: Prompt personalizado para a extração pelo LLM
- `schema`: Esquema JSON para extração de dados estruturados
- `allowExternalLinks`: Permite extração a partir de links externos
- `enableWebSearch`: Habilita busca na web para contexto adicional
- `includeSubdomains`: Inclui subdomínios na extração

Ao usar uma instância auto-hospedada, a extração usará o LLM que você configurou. Na API em nuvem, ela usa o serviço de LLM gerenciado do Firecrawl.

Agente autônomo de pesquisa na web que navega independentemente pela internet, busca informações, percorre páginas e extrai dados estruturados com base na sua consulta. Esse agente é executado de forma assíncrona — ele retorna imediatamente um ID de job, e você faz polling em `firecrawl_agent_status` para verificar quando for concluído e recuperar os resultados.

```
{
  "name": "firecrawl_agent",
  "arguments": {
    "prompt": "Find the top 5 AI startups founded in 2024 and their funding amounts",
    "schema": {
      "type": "object",
      "properties": {
        "startups": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": { "type": "string" },
              "funding": { "type": "string" },
              "founded": { "type": "string" }
            }
          }
        }
      }
    }
  }
}
```

Você também pode fornecer URLs específicas nas quais o agente deve se concentrar:

```
{
  "name": "firecrawl_agent",
  "arguments": {
    "urls": ["https://docs.firecrawl.dev", "https://firecrawl.dev/pricing"],
    "prompt": "Compare the features and pricing information from these pages"
  }
}
```

- `prompt`: Descrição em linguagem natural dos dados que você quer (obrigatório, máx. 10.000 caracteres)
- `urls`: Array opcional de URLs para focar o agente em páginas específicas
- `schema`: Esquema JSON opcional para saída estruturada

**Melhor para:** Tarefas de pesquisa complexas quando você não sabe as URLs exatas; coleta de dados de múltiplas fontes; encontrar informações espalhadas pela web; extrair dados de SPAs pesadas em JavaScript que falham com a raspagem comum. **Retorna:** ID do job para verificação de status. Use `firecrawl_agent_status` para consultar os resultados periodicamente.

### 8. Verificar status do agente (`firecrawl_agent_status`)

Verifique o status de uma tarefa do agente e recupere os resultados quando ela for concluída. Faça verificações (polling) a cada 15–30 segundos e mantenha por pelo menos 2–3 minutos antes de considerar a solicitação como falha.

```
{
  "name": "firecrawl_agent_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

#### Opções de status do agente:

- `id`: O ID da tarefa do agente retornado por `firecrawl_agent` (obrigatório)

**Possíveis status:**

- `processing`: O agente ainda está pesquisando — continue consultando periodicamente
- `completed`: Pesquisa concluída — a resposta inclui os dados extraídos
- `failed`: Ocorreu um erro

**Retorna:** Status, progresso e resultados (se concluída) da tarefa do agente.

### 9. Criar sessão do navegador (`firecrawl_browser_create`)

Crie uma sessão de navegador persistente para execução de código por meio do CDP (Chrome DevTools Protocol).

```
{
  "name": "firecrawl_browser_create",
  "arguments": {
    "ttl": 120,
    "activityTtl": 60
  }
}
```

#### Opções de criação do Browser:

- `ttl`: Tempo de vida total da sessão em segundos (30-3600, opcional)
- `activityTtl`: Tempo limite de inatividade em segundos (10-3600, opcional)

**Melhor para:** Executar código (Python/JS) que interage com uma página de navegador em tempo real, automação de navegador em várias etapas, sessões com perfis que persistem entre múltiplas chamadas de ferramenta. **Retorna:** ID da sessão, URL do CDP e URL de visualização em tempo real.

### 10. Executar código no navegador (`firecrawl_browser_execute`)

Executa código em uma sessão de navegador ativa. Oferece suporte a comandos do agent-browser (bash), Python ou JavaScript.

```
{
  "name": "firecrawl_browser_execute",
  "arguments": {
    "sessionId": "session-id-here",
    "code": "agent-browser open https://example.com",
    "language": "bash"
  }
}
```

Exemplo em Python usando Playwright:

```
{
  "name": "firecrawl_browser_execute",
  "arguments": {
    "sessionId": "session-id-here",
    "code": "await page.goto('https://example.com')\ntitle = await page.title()\nprint(title)",
    "language": "python"
  }
}
```

#### Opções de execução do navegador:

- `sessionId`: O ID da sessão do navegador (obrigatório)
- `code`: O código a ser executado (obrigatório)
- `language`: `bash`, `python` ou `node` (opcional, padrão é `bash`)

**Comandos comuns do agent-browser (bash):**

- `agent-browser open <url>` — Navegar para a URL
- `agent-browser snapshot` — Obter árvore de acessibilidade com referências clicáveis
- `agent-browser click @e5` — Clicar em elemento pela referência do snapshot
- `agent-browser type @e3 "text"` — Digitar no elemento
- `agent-browser screenshot [path]` — Capturar screenshot
- `agent-browser scroll down` — Rolar a página
- `agent-browser wait 2000` — Aguardar 2 segundos

**Retorno:** Resultado da execução, incluindo stdout, stderr e código de saída.

### 11. Excluir sessão do navegador (`firecrawl_browser_delete`)

Encerra uma sessão do navegador.

```
{
  "name": "firecrawl_browser_delete",
  "arguments": {
    "sessionId": "session-id-here"
  }
}
```

#### Opções de exclusão do navegador:

- `sessionId`: O ID da sessão do navegador a ser encerrada (obrigatório)

**Retorna:** Confirmação de sucesso.

### 12. Listar sessões do navegador (`firecrawl_browser_list`)

Lista sessões do navegador, que podem ser filtradas por status.

```
{
  "name": "firecrawl_browser_list",
  "arguments": {
    "status": "ativo"
  }
}
```

#### Opções da lista de navegadores:

- `status`: Filtrar por status da sessão — `active` ou `destroyed` (opcional)

**Retorna:** Array de sessões de navegador.

## Sistema de Log

O servidor inclui registros abrangentes:

- Status e progresso da operação
- Métricas de desempenho
- Monitoramento do uso de créditos
- Acompanhamento de limites de taxa
- Condições de erro

Exemplos de mensagens de log:

```
[INFO] Firecrawl MCP Server initialized successfully
[INFO] Starting scrape for URL: https://example.com
[INFO] Starting crawl for URL: https://example.com
[WARNING] Credit usage has reached warning threshold
[ERROR] Limite de requisições excedido, tentando novamente em 2s...
```

## Tratamento de Erros

O servidor oferece um tratamento de erros robusto:

- Novas tentativas automáticas para erros transitórios
- Tratamento de rate limit com backoff
- Mensagens de erro detalhadas
- Alertas de uso de créditos
- Resiliência de rede

Exemplo de resposta de erro:

```
{
  "content": [
    {
      "type": "text",
      "text": "Error: Rate limit exceeded. Retrying in 2 seconds..."
    }
  ],
  "isError": true
}
```

## Desenvolvimento

```
# Instalar dependências
npm install

# Build
npm run build

# Executar testes
npm test
```

### Contribuindo

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Execute os testes: `npm test`
4. Envie um pull request

### Agradecimentos aos colaboradores

Obrigado a [@vrknetha](https://github.com/vrknetha) e [@cawstudios](https://caw.tech) pela implementação inicial! Obrigado à MCP.so e à Klavis AI pela hospedagem, e a [@gstarwd](https://github.com/gstarwd), [@xiangkaiz](https://github.com/xiangkaiz) e [@zihaolin96](https://github.com/zihaolin96) por integrarem nosso servidor.

## Licença

Licença MIT — consulte o arquivo LICENSE para mais detalhes