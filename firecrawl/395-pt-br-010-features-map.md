---
title: Mapa | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/map
source: sitemap
fetched_at: 2026-03-23T07:21:37.119801-03:00
rendered_js: false
word_count: 403
summary: This document describes the /map endpoint, which enables users to discover and list all URLs within a website using sitemaps, search engine results, and crawl data.
tags:
    - web-scraping
    - site-mapping
    - api-endpoint
    - url-discovery
    - data-extraction
category: api
---

## Apresentando o /map

A forma mais simples de ir de uma única URL para um mapa de todo o site. Isso é extremamente útil para:

- Quando você precisa pedir ao usuário final que escolha quais links devem ser coletados
- Quando você precisa saber rapidamente quais links existem em um site
- Quando você precisa coletar páginas de um site relacionadas a um tópico específico (use o parâmetro `search`)
- Quando você só precisa coletar páginas específicas de um site

## Mapeamento

### endpoint /map

Usado para mapear uma URL e obter as URLs do site. Retorna a maioria dos links presentes no site. As URLs são descobertas principalmente a partir do sitemap do site, complementadas com resultados de SERP (páginas de resultados de mecanismos de busca) e páginas rastreadas anteriormente para melhorar a cobertura. Você pode controlar o comportamento do sitemap com o parâmetro `sitemap`.

### Instalação

### Uso

### Resposta

Os SDKs retornarão o objeto de dados diretamente. O cURL retornará o payload exatamente como mostrado abaixo.

```
{
  "success": true,
  "links": [
    {
      "url": "https://docs.firecrawl.dev/features/scrape",
      "title": "Scrape | Firecrawl",
      "description": "Transforme qualquer URL em dados limpos"
    },
    {
      "url": "https://www.firecrawl.dev/blog/5_easy_ways_to_access_glm_4_5",
      "title": "5 Maneiras Fáceis de Acessar o GLM-4.5",
      "description": "Descubra como acessar os modelos GLM-4.5 localmente, por aplicativos de chat, via API oficial e usando a API de marketplaces de LLM para integração contínua..."
    },
    {
      "url": "https://www.firecrawl.dev/playground",
      "title": "Playground - Firecrawl",
      "description": "Pré-visualize a resposta da API e obtenha trechos de código para a API"
    },
    {
      "url": "https://www.firecrawl.dev/?testId=2a7e0542-077b-4eff-bec7-0130395570d6",
      "title": "Firecrawl - A API de Dados da Web para IA",
      "description": "A API de rastreamento, scraping e busca na web para IA. Feita para escala. A Firecrawl entrega toda a internet para agentes e desenvolvedores de IA. Limpos, estruturados e ..."
    },
    {
      "url": "https://www.firecrawl.dev/?testId=af391f07-ca0e-40d3-8ff2-b1ecf2e3fcde",
      "title": "Firecrawl - A API de Dados da Web para IA",
      "description": "A API de rastreamento, scraping e busca na web para IA. Feita para escala. A Firecrawl entrega toda a internet para agentes e desenvolvedores de IA. Limpos, estruturados e ..."
    },
    ...
  ]
}
```

#### Mapear com busca

Usar o parâmetro `search` no Map permite procurar URLs específicas dentro de um site.

```
curl -X POST https://api.firecrawl.dev/v2/map \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer SUA_CHAVE_DE_API' \
  -d '{
    "url": "https://firecrawl.dev",
    "search": "docs"
  }'
```

A resposta será uma lista ordenada da mais relevante para a menos relevante.

```
{
  "status": "sucesso",
  "links": [
    {
      "url": "https://docs.firecrawl.dev",
      "title": "Docs do Firecrawl",
      "description": "Documentação do Firecrawl",
    },
    {
      "url": "https://docs.firecrawl.dev/sdks/python",
      "title": "SDK do Firecrawl para Python",
      "description": "Documentação do SDK do Firecrawl para Python"
    },
    ...
  ]
}
```

## Localização e idioma

Especifique o país e os idiomas preferidos para obter conteúdo relevante com base no seu local de destino e nas preferências de idioma, de forma semelhante ao endpoint /scrape.

### Como funciona

Ao definir as configurações de localização, o Firecrawl usará um proxy apropriado, se disponível, e emulará o idioma e o fuso horário correspondentes. Por padrão, a localização é definida como “US” se nada for especificado.

### Uso

Para usar as configurações de localização e idioma, inclua o objeto `location` no corpo da requisição com as seguintes propriedades:

- `country`: código de país ISO 3166-1 alfa-2 (por exemplo, ‘US’, ‘AU’, ‘DE’, ‘JP’). Padrão: ‘US’.
- `languages`: um array de idiomas e localidades preferenciais para a requisição, em ordem de prioridade. Padrão: o idioma da localização especificada.

Para mais detalhes sobre as localizações compatíveis, consulte a [documentação de Proxies](https://docs.firecrawl.dev/pt-BR/features/proxies).

## Considerações

Este endpoint prioriza a velocidade, portanto, talvez não capture todos os links do site. Ele se baseia principalmente no sitemap do site, complementado por dados de rastreamento em cache e resultados de mecanismos de busca. Para obter uma lista de URLs mais completa e atualizada, considere usar o endpoint [/crawl](https://docs.firecrawl.dev/pt-BR/features/crawl).

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instruções de onboarding automatizado.