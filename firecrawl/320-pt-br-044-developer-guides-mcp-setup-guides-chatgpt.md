---
title: Pesquisa e scraping na Web com MCP no ChatGPT - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/mcp-setup-guides/chatgpt
source: sitemap
fetched_at: 2026-03-23T07:37:42.94847-03:00
rendered_js: false
word_count: 309
summary: This document provides step-by-step instructions for integrating the Firecrawl MCP server into ChatGPT, enabling web scraping and search capabilities via the Developer mode.
tags:
    - firecrawl
    - chatgpt
    - mcp
    - web-scraping
    - api-integration
    - developer-mode
category: configuration
---

Adicione recursos de scraping e busca na web ao ChatGPT com o Firecrawl MCP.

## Configuração rápida

### 1. Obtenha sua chave de API

Crie uma conta em [firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) e copie sua chave de API.

### 2. Ative o Modo Desenvolvedor

Abra as configurações do ChatGPT clicando no seu nome de usuário no canto inferior esquerdo ou acesse diretamente [chatgpt.com/#settings](https://chatgpt.com/#settings). Na janela de configurações, role até a parte inferior e selecione **Advanced Settings**. Ative o **Developer mode**.

### 3. Criar o Conector

Com o modo Developer habilitado, vá até a aba **Apps & Connectors** no mesmo modal de configurações. Clique no botão **Create** no canto superior direito.

Preencha os detalhes do conector:

- **Name:** `Firecrawl MCP`
- **Description:** `Web scraping, crawling, search, and content extraction` (opcional)
- **MCP Server URL:** `https://mcp.firecrawl.dev/YOUR_API_KEY_HERE/v2/mcp`
- **Authentication:** `None`

Substitua `YOUR_API_KEY_HERE` na URL pela sua [chave de API Firecrawl](https://www.firecrawl.dev/app/api-keys) real.

Marque a caixa de seleção **“I understand and want to continue”** e, em seguida, clique em **Create**.

### 4. Verificar a configuração

Volte para a interface principal do ChatGPT. Você deve ver **Modo Desenvolvedor** exibido, indicando que os conectores MCP estão ativos. Se você não vir o Modo Desenvolvedor, recarregue a página. Se ainda assim ele não aparecer, abra as configurações novamente e verifique se o Modo Desenvolvedor está ativado em Configurações Avançadas.

Para usar o Firecrawl em uma conversa, clique no botão **+** no campo de entrada do chat, depois selecione **More** e escolha **Firecrawl MCP**.

## Demonstração rápida

Com o Firecrawl MCP selecionado, experimente estes prompts: **Busca:**

```
Search for the latest React Server Components updates
```

**Scrape:**

```
Scrape firecrawl.dev and tell me what it does
```

**Acessar documentação:**

```
Extraia a documentação da Vercel sobre edge functions e resuma-a
```

Quando o ChatGPT utiliza as ferramentas MCP do Firecrawl, você verá um prompt de confirmação pedindo a sua aprovação.

Você pode marcar **“Lembrar desta conversa”** para evitar confirmações repetidas durante a mesma sessão de chat. Essa medida de segurança é implementada pela OpenAI para garantir que as ferramentas MCP não executem ações não intencionais. Depois de confirmar, o ChatGPT executará a solicitação e retornará os resultados.