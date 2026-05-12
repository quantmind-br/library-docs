---
title: Busca | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/search
source: sitemap
fetched_at: 2026-03-23T07:21:40.180934-03:00
rendered_js: false
word_count: 918
summary: This document describes the Firecrawl search API endpoint, which allows users to perform web searches, filter by source and category, and optionally scrape result content in a single operation.
tags:
    - api
    - web-scraping
    - search-engine
    - data-extraction
    - ai-agents
    - firecrawl
category: api
---

A API de busca do Firecrawl permite realizar pesquisas na web e, opcionalmente, fazer scraping dos resultados em uma única operação.

- Escolha formatos de saída específicos (markdown, HTML, links, screenshots)
- Pesquise na web com parâmetros personalizáveis (localização, etc.)
- Opcionalmente, recupere o conteúdo dos resultados em vários formatos
- Controle a quantidade de resultados e defina limites de tempo

Para mais detalhes, consulte a [Referência da API do endpoint /search](https://docs.firecrawl.dev/api-reference/endpoint/search).

### endpoint /search

Usado para realizar pesquisas na web e, opcionalmente, obter conteúdo dos resultados.

### Instalação

### Uso básico

### Resposta

Os SDKs retornarão o objeto de dados diretamente. O cURL retornará a carga completa.

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - The Web Data API for AI",
        "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders.",
        "position": 1
      },
      {
        "url": "https://github.com/firecrawl/firecrawl",
        "title": "mendableai/firecrawl: Turn entire websites into LLM-ready ... - GitHub",
        "description": "Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data.",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "Quickstart | Firecrawl",
        "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
        "imageWidth": 5814,
        "imageHeight": 1200,
        "url": "https://docs.firecrawl.dev/",
        "position": 1
      },
      ...
    ],
    "news": [
      {
        "title": "Y Combinator startup Firecrawl is ready to pay $1M to hire three AI agents as employees",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "It's now placed three new ads on YC's job board for “AI agents only” and has set aside a $1 million budget total to make it happen.",
        "date": "3 months ago",
        "position": 1
      },
      ...
    ]
  }
}
```

## Tipos de resultados de busca

Além dos resultados da web padrão, o Search oferece tipos de resultados especializados por meio do parâmetro `sources`:

- `web`: resultados da web padrão (padrão)
- `news`: resultados focados em notícias
- `images`: resultados de busca de imagens

Você pode solicitar várias fontes em uma única chamada (por exemplo, `sources: ["web", "news"]`). Quando fizer isso, o parâmetro `limit` é aplicado **por tipo de fonte** — assim, `limit: 5` com `sources: ["web", "news"]` retorna até 5 resultados da web e até 5 resultados de notícias (10 no total). Se você precisar de parâmetros diferentes por fonte (por exemplo, valores diferentes de `limit` ou `scrapeOptions` diferentes), faça chamadas separadas.

## Categorias de pesquisa

Filtre os resultados por categorias específicas usando o parâmetro `categories`:

- `github`: Pesquise em repositórios do GitHub, código, issues e documentação
- `research`: Pesquise em sites acadêmicos e de pesquisa (arXiv, Nature, IEEE, PubMed, etc.)
- `pdf`: Pesquise por PDFs

### Pesquisa por categoria no GitHub

Pesquise especificamente em repositórios do GitHub:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "web scraping em Python",
    "categories": ["github"],
    "limit": 10
  }'
```

### Pesquisa por categoria de pesquisa

Pesquise sites acadêmicos e de pesquisa:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "transformers em aprendizado de máquina",
    "categories": ["pesquisa"],
    "limit": 10
  }'
```

### Pesquisa com categorias mistas

Combine várias categorias em uma única pesquisa:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "redes neurais",
    "categories": ["github", "pesquisa"],
    "limit": 15
  }'
```

### Formato de resposta de categoria

Cada resultado de pesquisa inclui um campo `category` indicando sua fonte:

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/neural-network",
        "title": "Implementação de Rede Neural",
        "description": "Uma implementação de redes neurais em PyTorch",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "Avanços na Arquitetura de Redes Neurais",
        "description": "Artigo científico sobre melhorias em redes neurais",
        "category": "research"
      }
    ]
  }
}
```

Exemplos:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "openai",
    "sources": ["news"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-SUA_CHAVE_DE_API" \
  -d '{
    "query": "Júpiter",
    "sources": ["imagens"],
    "limit": 8
  }'
```

### Pesquisa de imagens em alta definição com filtro por tamanho

Use operadores de imagem para encontrar imagens em alta resolução:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "pôr do sol imagesize:1920x1080",
    "sources": ["images"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-SUA_API_KEY" \
  -d '{
    "query": "papel de parede de montanha larger:2560x1440",
    "sources": ["images"],
    "limit": 8
  }'
```

**Resoluções HD comuns:**

- `imagesize:1920x1080` - Full HD (1080p)
- `imagesize:2560x1440` - QHD (1440p)
- `imagesize:3840x2160` - 4K UHD
- `larger:1920x1080` - HD ou superior
- `larger:2560x1440` - QHD ou superior

Pesquise e recupere conteúdo dos resultados de busca em uma única operação.

Todas as opções do endpoint /scrape são compatíveis neste endpoint de busca por meio do parâmetro `scrapeOptions`.

```
{
  "success": true,
  "data": [
    {
      "title": "Firecrawl - A API definitiva de web scraping",
      "description": "A Firecrawl é uma poderosa API de web scraping que transforma qualquer site em dados limpos e estruturados para IA e análise.",
      "url": "https://firecrawl.dev/",
      "markdown": "# Firecrawl\n\nA API definitiva de web scraping\n\n## Transforme qualquer site em dados limpos e estruturados\n\nA Firecrawl facilita a extração de dados de sites para aplicações de IA, pesquisa de mercado, agregação de conteúdo e muito mais...",
      "links": [
        "https://firecrawl.dev/pricing",
        "https://firecrawl.dev/docs",
        "https://firecrawl.dev/guides"
      ],
      "metadata": {
        "title": "Firecrawl - A API definitiva de web scraping",
        "description": "A Firecrawl é uma poderosa API de web scraping que transforma qualquer site em dados limpos e estruturados para IA e análise.",
        "sourceURL": "https://firecrawl.dev/",
        "statusCode": 200
      }
    }
  ]
}
```

## Opções avançadas de busca

A API de busca do Firecrawl oferece diversos parâmetros para personalizar suas buscas:

### Personalização de localização

### Busca por período

Use o parâmetro `tbs` para filtrar resultados por período. Observe que `tbs` se aplica apenas a resultados da fonte `web` — ele não filtra resultados de `news` ou `images`. Se você precisar de notícias com filtro de tempo, considere usar a fonte `web` com o operador `site:` para direcionar domínios de notícias específicos.

Valores comuns de `tbs`:

- `qdr:h` - Última hora
- `qdr:d` - Últimas 24 horas
- `qdr:w` - Última semana
- `qdr:m` - Último mês
- `qdr:y` - Último ano
- `sbd:1` - Ordenar por data (mais recentes primeiro)

Para um filtro temporal mais preciso, você pode especificar intervalos de datas exatos usando o formato de intervalo personalizado:

Você pode combinar `sbd:1` com filtros de tempo para obter resultados ordenados por data dentro de um intervalo de tempo. Por exemplo, `sbd:1,qdr:w` retorna resultados da última semana ordenados do mais recente para o mais antigo, e `sbd:1,cdr:1,cd_min:12/1/2024,cd_max:12/31/2024` retorna resultados de dezembro de 2024 ordenados por data.

### Tempo limite personalizado

Defina um tempo limite personalizado para operações de pesquisa:

## Zero Data Retention (ZDR)

Para equipes com requisitos rigorosos de tratamento de dados, a Firecrawl oferece opções de Zero Data Retention (ZDR) para o endpoint `/search` por meio do parâmetro `enterprise`. A busca com ZDR está disponível nos planos Enterprise — visite [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) para começar.

### ZDR de ponta a ponta

Com o ZDR de ponta a ponta, tanto o Firecrawl quanto nosso provedor de busca upstream aplicam retenção zero de dados. Nenhum dado de consulta ou de resultado é armazenado em nenhum ponto do pipeline.

- **Custo:** 10 créditos por 10 resultados
- **Parâmetro:** `enterprise: ["zdr"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["zdr"]
  }'
```

### ZDR anonimizado

Com o ZDR anonimizado, o Firecrawl aplica retenção zero total de dados do nosso lado. Nosso provedor de busca pode armazenar a consulta em cache, mas ela é totalmente anonimizada — nenhuma informação identificável é anexada.

- **Custo:** 2 créditos por 10 resultados
- **Parâmetro:** `enterprise: ["anon"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["anon"]
  }'
```

### Combinando ZDR de busca com ZDR de scraping

Se você estiver usando busca com scraping de conteúdo (`scrapeOptions`), o parâmetro `enterprise` cobre a parte da busca, enquanto `zeroDataRetention` em `scrapeOptions` cobre a parte do scraping. Para obter ZDR completo em ambos, defina os dois:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 5,
    "enterprise": ["zdr"],
    "scrapeOptions": {
      "formats": ["markdown"],
      "zeroDataRetention": true
    }
  }'
```

## Implicações de custos

O custo de uma pesquisa é de 2 créditos por 10 resultados de pesquisa. Se as opções de scraping estiverem ativadas, os custos padrão de scraping se aplicam a cada resultado de pesquisa:

- **Basic scrape**: 1 crédito por página da web
- **PDF parsing**: 1 crédito por página de PDF
- **Enhanced proxy mode**: 4 créditos adicionais por página da web
- **JSON mode**: 4 créditos adicionais por página da web

Para ajudar a controlar os custos:

- Defina `parsers: []` se a análise de PDF não for necessária
- Use `proxy: "basic"` em vez de `"enhanced"` quando possível, ou defina como `"auto"`
- Limite o número de resultados de pesquisa com o parâmetro `limit`

## Opções avançadas de scraping

Para mais detalhes sobre as opções de scraping, consulte a [documentação do recurso Scrape](https://docs.firecrawl.dev/features/scrape). Tudo, exceto o Agente FIRE-1 e os recursos de rastreamento de alterações, é compatível com este endpoint de busca.

> Você é um agente de IA que precisa de uma chave de API da Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções de onboarding automatizado.