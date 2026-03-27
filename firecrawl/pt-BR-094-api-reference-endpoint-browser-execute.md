---
title: Executar Código no Navegador - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/browser-execute
source: sitemap
fetched_at: 2026-03-23T07:22:12.46379-03:00
rendered_js: false
word_count: 249
summary: This document provides the API specifications for executing code within a browser session, detailing request parameters, authentication, and response structures.
tags:
    - api-documentation
    - browser-automation
    - code-execution
    - sandbox-environment
    - firecrawl-api
category: api
---

[Pular para o conteúdo principal](#content-area)

Executar código em uma sessão de navegador

CabeçalhoValor`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Corpo da requisição

ParâmetroTipoObrigatórioPadrãoDescrição`code`stringSim-Código a ser executado (1-100.000 caracteres)`language`stringNão`"node"`Idioma do código: `"python"`, `"node"` ou `"bash"` (para comandos de CLI do agent-browser)`timeout`numberNão-Tempo máximo de execução em segundos (1-300)

## Resposta

CampoTipoDescrição`success`booleanIndica se o código foi executado com sucesso`stdout`stringSaída padrão da execução do código`result`stringSaída padrão da execução do código`stderr`stringSaída de erro padrão da execução do código`exitCode`numberCódigo de saída do processo executado`killed`booleanIndica se o processo foi finalizado por tempo limite (timeout)`error`stringMensagem de erro caso a execução falhe (apenas em caso de falha)

### Exemplo de requisição

```
curl -X POST "https://api.firecrawl.dev/v2/browser/550e8400-e29b-41d4-a716-446655440000/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "await page.goto(\"https://example.com\")\ntitle = await page.title()\nprint(title)",
    "language": "python"
  }'
```

### Exemplo de resposta (sucesso)

```
{
  "success": true,
  "result": "Example Domain"
}
```

### Exemplo de resposta (erro)

```
{
  "success": true,
  "error": "TimeoutError: page.goto: Timeout 30000ms exceeded."
}
```

> Você é um agente de IA que precisa de uma Firecrawl API key? Veja [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de onboarding automatizado.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

ID da sessão do navegador

#### Corpo

Código a ser executado no sandbox do navegador

Required string length: `1 - 100000`

Linguagem do código a ser executado. Use `node` para JavaScript ou `bash` para comandos da CLI do agent-browser.

Opções disponíveis:

`python`,

`node`,

`bash`

Tempo máximo de execução, em segundos

Intervalo obrigatório: `1 <= x <= 300`

#### Resposta

Código executado com sucesso

Saída padrão da execução do código

Saída padrão (também conhecida como stdout)

Saída de erro padrão da execução do código

Código de saída do processo executado

Indica se o processo foi encerrado por tempo limite excedido (timeout)

Mensagem de erro caso o código tenha gerado uma exceção