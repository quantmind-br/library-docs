---
title: Modo JSON | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/llm-extract
source: sitemap
fetched_at: 2026-03-23T07:21:32.689102-03:00
rendered_js: false
word_count: 460
summary: This document explains how to use Firecrawl's JSON mode to extract structured data from web pages using AI, either by providing a specific JSON schema or a descriptive prompt.
tags:
    - web-scraping
    - ai-extraction
    - json-schema
    - data-parsing
    - firecrawl-api
    - structured-data
category: guide
---

O Firecrawl usa IA para obter dados estruturados de páginas da web em 3 etapas:

1. **Defina o esquema (opcional):** Defina um esquema JSON (no formato da OpenAI) para especificar os dados desejados, ou forneça apenas um `prompt` se não precisar de um esquema rígido, junto com a URL da página.
2. **Faça a requisição:** Envie sua URL e o esquema para nosso endpoint /scrape usando o modo JSON. Veja como aqui: [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
3. **Obtenha seus dados:** Receba dados limpos e estruturados que correspondem ao seu esquema, prontos para uso imediato.

Isso torna rápido e fácil obter dados da web no formato de que você precisa.

### Modo JSON via /scrape

Usado para extrair dados estruturados de páginas extraídas.

Saída:

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "Rastreamento e extração de dados na web com IA",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "Rastreamento e extração de dados na web com IA",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "Rastreamento e extração de dados na web com IA",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl"
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### Dados estruturados sem esquema

Você também pode extrair sem um esquema, apenas passando um `prompt` para o endpoint. O LLM escolhe a estrutura dos dados.

Resultado:

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "Raspagem e extração de dados na web com IA",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "Raspagem e extração de dados na web com IA",
        "robots": "seguir, indexar",
        "ogTitle": "Firecrawl",
        "ogDescription": "Raspagem e extração de dados na web com IA",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

Aqui está um exemplo completo de extração de informações estruturadas de empresas a partir de um site:

Resultado:

```
{
  "success": true,
  "data": {
    "json": {
      "company_mission": "Transformar sites em dados prontos para LLM",
      "supports_sso": true,
      "is_open_source": true,
      "is_in_yc": true
    }
  }
}
```

### Opções do formato JSON

Ao usar o modo JSON na v2, inclua um objeto em `formats` com o esquema incorporado diretamente: `formats: [{ type: 'json', schema: { ... }, prompt: '...' }]` Parâmetros:

- `schema`: JSON Schema que descreve a saída estruturada desejada (obrigatório para extração baseada em esquema).
- `prompt`: prompt opcional para orientar a extração (também usado para extração sem esquema).

**Importante:** Diferente da v1, não há um parâmetro separado `jsonOptions` na v2. O esquema deve ser incluído diretamente dentro do objeto de formato no array `formats`.

Se você estiver obtendo resultados inconsistentes ou incompletos na extração em JSON, estas práticas podem ajudar:

- **Mantenha os prompts curtos e focados.** Prompts longos com muitas regras aumentam a variabilidade. Em vez disso, mova restrições específicas (como valores permitidos) para o schema.
- **Use nomes de propriedades concisos.** Evite incluir instruções ou listas de enum nos nomes das propriedades. Use uma chave curta como `"installation_type"` e coloque os valores permitidos em um array `enum`.
- **Adicione arrays `enum` para campos com valores restritos.** Quando um campo tiver um conjunto fixo de valores, liste-os em `enum` e garanta que correspondam exatamente ao texto exibido na página.
- **Inclua tratamento de `null` nas descrições dos campos.** Adicione `"Return null if not found on the page."` à `description` de cada campo para que o modelo não tente deduzir valores ausentes.
- **Adicione dicas de localização.** Diga ao modelo onde encontrar os dados na página, por exemplo: `"Flow rate in GPM from the Specifications table."`.
- **Divida schemas grandes em solicitações menores.** Schemas com muitos campos (por exemplo, 30+) produzem resultados menos consistentes. Divida-os em 2–3 solicitações de 10–15 campos cada.

**Exemplo de um schema bem estruturado:**

```
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": ["string", "null"],
      "description": "Full descriptive product name as shown on the page. Return null if not found."
    },
    "installation_type": {
      "type": ["string", "null"],
      "description": "Installation type from the Specifications section. Return null if not found.",
      "enum": ["Deck-mount", "Wall-mount", "Countertop", "Drop-in", "Undermount"]
    },
    "flow_rate_gpm": {
      "type": ["string", "null"],
      "description": "Flow rate in GPM from the Specifications section. Return null if not found."
    }
  }
}
```

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Veja [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instruções de onboarding automatizado.