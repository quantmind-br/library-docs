---
title: Criando um Assistente de Pesquisa com IA usando Firecrawl e AI SDK - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/cookbooks/ai-research-assistant-cookbook
source: sitemap
fetched_at: 2026-03-23T07:34:45.064637-03:00
rendered_js: false
word_count: 697
summary: This document provides a guide on building an AI-powered research assistant that utilizes web scraping and search tools via the AI SDK, Firecrawl, and OpenAI models.
tags:
    - ai-agent
    - web-scraping
    - chatbot-development
    - tool-calling
    - next-js
    - firecrawl
    - ai-sdk
category: guide
---

Crie um assistente de pesquisa com IA completo que possa fazer scraping de sites e buscar na web para responder perguntas. O assistente decide automaticamente quando usar ferramentas de scraping ou de busca para reunir informações e, em seguida, fornece respostas abrangentes com base nos dados coletados. ![Interface de chatbot de assistente de pesquisa com IA mostrando scraping em tempo real na web com Firecrawl e respostas conversacionais impulsionadas pela OpenAI](https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif?s=cfcbad69aa3f087a474414c0763a260b)

## O que você vai construir

Uma interface de chat com IA em que os usuários podem fazer perguntas sobre qualquer assunto. O assistente de IA decide automaticamente quando usar ferramentas de scraping ou de busca na web para reunir informações e, então, fornece respostas completas com base nos dados coletados.

## Pré-requisitos

- Node.js 18 ou posterior instalado
- Uma chave de API da OpenAI em [platform.openai.com](https://platform.openai.com)
- Uma chave de API do Firecrawl em [firecrawl.dev](https://firecrawl.dev)
- Conhecimentos básicos de React e Next.js

## Como funciona

### Fluxo de mensagens

1. **Usuário envia uma mensagem**: O usuário digita uma pergunta e clica em Enviar
2. **Frontend envia a solicitação**: `useChat` envia a mensagem para `/api/chat` com o modelo selecionado e a configuração de busca na web
3. **Backend processa a mensagem**: A rota da API recebe a mensagem e chama `streamText`
4. **IA decide sobre as ferramentas**: O modelo analisa a pergunta e decide se deve usar `scrapeWebsite` ou `searchWeb` (apenas se a busca na web estiver ativada)
5. **Ferramentas executam**: Se as ferramentas forem chamadas, o Firecrawl faz o scraping ou realiza a busca na web
6. **IA gera a resposta**: O modelo analisa os resultados das ferramentas e gera uma resposta em linguagem natural
7. **Frontend exibe os resultados**: A UI mostra as chamadas de ferramentas e a resposta final em tempo real

O sistema de chamada de ferramentas do AI SDK ([ai-sdk.dev/docs/foundations/tools](https://ai-sdk.dev/docs/foundations/tools)) funciona da seguinte forma:

1. O modelo recebe a mensagem do usuário e as descrições das ferramentas disponíveis
2. Se o modelo determinar que é necessário usar uma ferramenta, ele gera uma chamada de ferramenta com parâmetros
3. O SDK executa a função da ferramenta com esses parâmetros
4. O resultado da ferramenta é enviado de volta ao modelo
5. O modelo usa o resultado para gerar sua resposta final

Tudo isso acontece automaticamente em uma única chamada a `streamText`, com os resultados sendo transmitidos para o frontend em tempo real.

## Principais recursos

### Seleção de modelo

O aplicativo oferece suporte a vários modelos da OpenAI:

- **GPT-5 Mini (Thinking)**: Modelo recente da OpenAI com capacidades avançadas de raciocínio
- **GPT-4o Mini**: Modelo rápido e econômico

Os usuários podem alternar entre os modelos usando o seletor suspenso.

### Alternância de busca na web

O botão Search controla se a IA pode usar as ferramentas do Firecrawl:

- **Ativado**: a IA pode chamar as ferramentas `scrapeWebsite` e `searchWeb` conforme necessário
- **Desativado**: a IA responde apenas com o conhecimento com o qual foi treinada

Isso dá aos usuários controle sobre quando usar dados da web versus o conhecimento embutido no modelo.

## Ideias de customização

Amplie o assistente com ferramentas adicionais:

- Consultas ao banco de dados para dados internos da empresa
- Integração ao CRM para buscar informações de clientes
- Envio de e-mails
- Geração de documentos

Cada ferramenta segue o mesmo padrão: defina um schema com Zod, implemente a função execute e registre-a no objeto `tools`.

### Alterar o modelo de IA

Substitua o OpenAI por outro provedor:

```
import { anthropic } from "@ai-sdk/anthropic";

const result = streamText({
  model: anthropic("claude-4.5-sonnet"),
  // ... restante da config
});
```

O SDK de IA oferece suporte a mais de 20 provedores com a mesma API. Saiba mais: [ai-sdk.dev/docs/foundations/providers-and-models](https://ai-sdk.dev/docs/foundations/providers-and-models).

### Personalizar a interface

Os componentes de AI Elements são construídos com base em shadcn/ui, portanto você pode:

- Modificar os estilos dos componentes nos arquivos de componente
- Adicionar novas variantes a componentes existentes
- Criar componentes personalizados que sigam o sistema de design

## Melhores práticas

1. **Use as ferramentas certas**: Escolha `searchWeb` para primeiro encontrar páginas relevantes, `scrapeWebsite` para páginas individuais ou deixe a IA decidir
2. **Monitore o uso da API**: Acompanhe o uso das APIs da Firecrawl e da OpenAI para evitar custos inesperados
3. **Trate erros de forma adequada**: As ferramentas incluem tratamento de erros, mas considere adicionar mensagens voltadas ao usuário
4. **Otimize o desempenho**: Use streaming para fornecer feedback imediato e considere colocar em cache conteúdo acessado com frequência
5. **Defina limites razoáveis**: `stopWhen: stepCountIs(5)` evita chamadas excessivas de ferramentas e custos fora de controle

* * *