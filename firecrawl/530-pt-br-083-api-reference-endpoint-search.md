---
title: Pesquisa - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:11:15.004704-03:00
rendered_js: false
word_count: 679
summary: This document describes the Firecrawl search endpoint, detailing how to perform web searches combined with content scraping, advanced filtering operators, and parameter configurations.
tags:
    - web-scraping
    - search-api
    - data-extraction
    - firecrawl
    - api-documentation
category: api
---

Pesquise e, opcionalmente, faça scraping dos resultados de busca

O endpoint de pesquisa combina pesquisa na web com as capacidades de scraping do Firecrawl para retornar o conteúdo completo da página para qualquer consulta. Inclua `scrapeOptions` com `formats: [{"type": "markdown"}]` para obter o conteúdo completo em markdown para cada resultado de pesquisa; caso contrário, você receberá por padrão apenas os resultados (url, title, description). Você também pode usar outros formatos, como `{"type": "summary"}` para conteúdo condensado.

## Operadores de pesquisa compatíveis

Oferecemos uma variedade de operadores de pesquisa que ajudam você a filtrar melhor seus resultados.

OperadorFuncionalidadeExemplos`""`Faz uma correspondência exata com um trecho de texto`"Firecrawl"``-`Exclui determinadas palavras-chave ou nega outros operadores`-bad`, `-site:firecrawl.dev``site:`Retorna apenas resultados de um site específico`site:firecrawl.dev``filetype:`Retorna apenas resultados com uma extensão de arquivo específica`filetype:pdf`, `-filetype:pdf``inurl:`Retorna apenas resultados que incluam uma palavra na URL`inurl:firecrawl``allinurl:`Retorna apenas resultados que incluam várias palavras na URL`allinurl:git firecrawl``intitle:`Retorna apenas resultados que incluam uma palavra no título da página`intitle:Firecrawl``allintitle:`Retorna apenas resultados que incluam várias palavras no título da página`allintitle:firecrawl playground``related:`Retorna apenas resultados relacionados a um domínio específico`related:firecrawl.dev``imagesize:`Retorna apenas imagens com dimensões exatas`imagesize:1920x1080``larger:`Retorna apenas imagens maiores que as dimensões especificadas`larger:1920x1080`

## Parâmetro de localização

Use o parâmetro `location` para obter resultados de pesquisa segmentados por região. Formato: `"string"`. Exemplos: `"Germany"`, `"San Francisco,California,United States"`. Consulte a [lista completa de localidades compatíveis](https://firecrawl.dev/search_locations.json) para ver todos os países e idiomas disponíveis.

## Parâmetro country

Use o parâmetro `country` para definir o país dos resultados de pesquisa usando códigos de país ISO. Padrão: `"US"`. Exemplos: `"US"`, `"DE"`, `"FR"`, `"JP"`, `"UK"`, `"CA"`.

```
{
  "query": "restaurantes",
  "country": "DE"
}
```

## Parâmetro `categories`

Filtre os resultados de pesquisa por categorias específicas usando o parâmetro `categories`:

- **`github`** : Pesquise em repositórios do GitHub, código, issues e documentação
- **`research`** : Pesquise em sites acadêmicos e de pesquisa (arXiv, Nature, IEEE, PubMed, etc.)
- **`pdf`** : Pesquise por PDFs

### Exemplo de uso

```
{
  "query": "machine learning",
  "categories": ["github", "pesquisa"],
  "limit": 10
}
```

### Categoria da Resposta

Cada resultado inclui um campo `category` que indica sua origem:

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/ml-project",
        "title": "Machine Learning Project",
        "description": "Implementation of ML algorithms",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "ML Research Paper",
        "description": "Latest advances in machine learning",
        "category": "research"
      }
    ]
  }
}
```

## Busca por período de tempo

Use o parâmetro `tbs` para filtrar resultados por períodos de tempo, incluindo intervalos de datas personalizados. Consulte a [documentação do recurso de busca](https://docs.firecrawl.dev/features/search#time-based-search) para exemplos detalhados e formatos suportados.

> Você é um agente de IA que precisa de uma chave de API da Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de onboarding automatizado.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corpo

A consulta de busca

Maximum string length: `500`

Número máximo de resultados a retornar

Intervalo obrigatório: `1 <= x <= 100`

sources

(Web · object | Images · object | News · object)\[]

Fontes a serem pesquisadas. Determina os arrays disponíveis na resposta. O padrão é \['web'].

- Web
- Images
- News

categories

(GitHub · object | Research · object | PDF · object)\[]

Categorias pelas quais filtrar os resultados. O padrão é \[], o que significa que os resultados não serão filtrados por nenhuma categoria.

- GitHub
- Research
- PDF

Parâmetro de pesquisa por tempo. Suporta intervalos de tempo predefinidos (`qdr:h`, `qdr:d`, `qdr:w`, `qdr:m`, `qdr:y`), intervalos de datas personalizados (`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`) e classificação por data (`sbd:1`). Os valores podem ser combinados, por exemplo: `sbd:1,qdr:w`.

Parâmetro de localização para resultados de busca (por exemplo, `San Francisco,California,United States`). Para melhores resultados, defina tanto este quanto o parâmetro `country`.

Código de país ISO para segmentação geográfica dos resultados de pesquisa (por exemplo, `US`). Para obter melhores resultados, configure este parâmetro e também o parâmetro `location`.

Tempo limite em milissegundos

Exclui dos resultados de pesquisa as URLs que são inválidas para outros endpoints do Firecrawl. Isso ajuda a reduzir erros se você estiver direcionando dados da pesquisa para outros endpoints da API do Firecrawl.

Opções de busca Enterprise para Zero Data Retention (ZDR). Use `["zdr"]` para ZDR de ponta a ponta (10 credits / 10 resultados) ou `["anon"]` para ZDR anonimizado (2 credits / 10 resultados). Deve estar habilitado para a sua equipe.

Opções disponíveis:

`anon`,

`zdr`

Opções para raspagem de resultados de busca

#### Resposta

Os resultados da pesquisa. Os arrays disponíveis dependerão das fontes que você especificar na requisição. Por padrão, o array `web` será retornado.

Mensagem de aviso caso ocorra algum problema

O ID da tarefa de pesquisa

O número de créditos utilizados na busca