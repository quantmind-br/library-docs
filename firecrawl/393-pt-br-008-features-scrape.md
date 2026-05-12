---
title: Raspar | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/scrape
source: sitemap
fetched_at: 2026-03-23T07:21:46.759483-03:00
rendered_js: false
word_count: 1382
summary: This document describes the Firecrawl API, which allows users to extract and convert website content into structured data, markdown, or branding profiles for use in LLM applications.
tags:
    - web-scraping
    - api-reference
    - data-extraction
    - markdown
    - structured-data
    - llm-integration
    - branding-analysis
category: api
---

Firecrawl converte páginas da web em Markdown, ideal para aplicações com LLMs.

- Gerencia complexidades: proxies, cache, limites de taxa, conteúdo bloqueado por JS
- Lida com conteúdo dinâmico: sites dinâmicos, sites renderizados em JS, PDFs, imagens
- Gera Markdown limpo, dados estruturados, capturas de tela ou HTML.

Para mais detalhes, consulte a [Referência da API do endpoint Scrape](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

### endpoint /scrape

Usado para extrair o conteúdo de uma URL.

### Instalação

### Uso

Para mais detalhes sobre os parâmetros, consulte a [Referência da API](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

### Resposta

Os SDKs retornarão o objeto de dados diretamente. O cURL retornará o payload exatamente como mostrado abaixo.

```
{
  "success": true,
  "data" : {
    "markdown": "A Launch Week I chegou! [Confira nosso lançamento do Dia 2 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Ganhe 2 meses grátis...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "O Firecrawl rastreia e converte qualquer site em markdown limpo.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Dados,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Transforme qualquer site em dados prontos para LLM.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

## Formatos de Scrape

Agora você pode escolher em quais formatos deseja sua saída. Você pode especificar vários formatos de saída. Os formatos suportados são:

- Markdown (`markdown`)
- Resumo (`summary`)
- HTML (`html`) - versão limpa do HTML da página
- HTML bruto (`rawHtml`) - HTML não modificado conforme recebido da página
- Captura de tela (`screenshot`, com opções como `fullPage`, `quality`, `viewport`) — as URLs das capturas de tela expiram após 24 horas
- Links (`links`)
- JSON (`json`) - saída estruturada
- Imagens (`images`) - extrair todas as URLs de imagens da página
- Branding (`branding`) - extrair identidade da marca e sistema de design

As chaves de saída corresponderão ao formato que você escolher.

### endpoint /scrape (com json)

Usado para extrair dados estruturados de páginas extraídas.

Resultado:

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

Agora é possível extrair sem um esquema, bastando enviar um `prompt` para o endpoint. O LLM escolhe a estrutura dos dados.

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

### Opções do formato JSON

Ao usar o formato `json`, passe um objeto dentro de `formats` com os seguintes parâmetros:

- `schema`: JSON Schema para a saída estruturada.
- `prompt`: Prompt opcional para orientar a extração quando houver um schema ou quando você preferir uma orientação leve.

### endpoint /scrape (com branding)

O formato de branding extrai informações completas sobre a identidade de marca de uma página da web, incluindo cores, fontes, tipografia, espaçamento, componentes de UI e mais. Isso é útil para análise de design systems, monitoramento de marca ou para criar ferramentas que precisam compreender a identidade visual de um site.

### Resposta

O formato de branding retorna um objeto `BrandingProfile` completo com a seguinte estrutura:

```
{
  "success": true,
  "data": {
    "branding": {
      "colorScheme": "dark",
      "logo": "https://firecrawl.dev/logo.svg",
      "colors": {
        "primary": "#FF6B35",
        "secondary": "#004E89",
        "accent": "#F77F00",
        "background": "#1A1A1A",
        "textPrimary": "#FFFFFF",
        "textSecondary": "#B0B0B0"
      },
      "fonts": [
        {
          "family": "Inter"
        },
        {
          "family": "Roboto Mono"
        }
      ],
      "typography": {
        "fontFamilies": {
          "primary": "Inter",
          "heading": "Inter",
          "code": "Roboto Mono"
        },
        "fontSizes": {
          "h1": "48px",
          "h2": "36px",
          "h3": "24px",
          "body": "16px"
        },
        "fontWeights": {
          "regular": 400,
          "medium": 500,
          "bold": 700
        }
      },
      "spacing": {
        "baseUnit": 8,
        "borderRadius": "8px"
      },
      "components": {
        "buttonPrimary": {
          "background": "#FF6B35",
          "textColor": "#FFFFFF",
          "borderRadius": "8px"
        },
        "buttonSecondary": {
          "background": "transparent",
          "textColor": "#FF6B35",
          "borderColor": "#FF6B35",
          "borderRadius": "8px"
        }
      },
      "images": {
        "logo": "https://firecrawl.dev/logo.svg",
        "favicon": "https://firecrawl.dev/favicon.ico",
        "ogImage": "https://firecrawl.dev/og-image.png"
      }
    }
  }
}
```

### Estrutura do Perfil de Branding

O objeto `branding` contém as seguintes propriedades:

- `colorScheme`: Esquema de cores detectado (`"light"` ou `"dark"`)
- `logo`: URL do logotipo principal
- `colors`: Objeto com as cores da marca:
  
  - `primary`, `secondary`, `accent`: Cores principais da marca
  - `background`, `textPrimary`, `textSecondary`: Cores de UI
  - `link`, `success`, `warning`, `error`: Cores semânticas
- `fonts`: Lista (array) de famílias tipográficas usadas na página
- `typography`: Informações detalhadas de tipografia:
  
  - `fontFamilies`: Famílias tipográficas primária, de títulos e de código
  - `fontSizes`: Definições de tamanho para títulos e corpo do texto
  - `fontWeights`: Definições de espessura (leve, regular, média, negrito)
  - `lineHeights`: Valores de altura de linha para diferentes tipos de texto
- `spacing`: Informações de espaçamento e layout:
  
  - `baseUnit`: Unidade base de espaçamento em pixels
  - `borderRadius`: Raio de borda padrão
  - `padding`, `margins`: Valores de espaçamento
- `components`: Estilos de componentes de UI:
  
  - `buttonPrimary`, `buttonSecondary`: Estilos de botões
  - `input`: Estilos de campos de entrada
- `icons`: Informações de estilo de ícones
- `images`: Imagens da marca (logo, favicon, og:image)
- `animations`: Configurações de animação e transição
- `layout`: Configuração de layout (grid, alturas de cabeçalho/rodapé)
- `personality`: Traços de personalidade da marca (tom, energia, público-alvo)

### Combinando com outros formatos

Você pode combinar o formato de branding com outros formatos para obter dados completos da página:

O Firecrawl permite executar várias ações em uma página da web antes de fazer o scraping do conteúdo. Isso é especialmente útil para interagir com conteúdo dinâmico, navegar entre páginas ou acessar conteúdo que exige interação do usuário. Veja um exemplo de como usar ações para acessar google.com, pesquisar por Firecrawl, clicar no primeiro resultado e fazer uma captura de tela. É importante, quase sempre, usar a ação `wait` antes/depois de executar outras ações para dar tempo suficiente para a página carregar.

### Exemplo

### Saída

Para mais detalhes sobre os parâmetros de ações, consulte a [referência da API](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## Localização e idioma

Especifique o país e os idiomas preferidos para obter conteúdo relevante com base no seu local de destino e nas suas preferências de idioma.

### Como funciona

Quando você define as configurações de localização, o Firecrawl usará um proxy apropriado, se disponível, e emulará as configurações correspondentes de idioma e fuso horário. Por padrão, a localização é definida como “US” se não for especificada.

### Uso

Para usar as configurações de localização e idioma, inclua o objeto `location` no corpo da sua requisição com as seguintes propriedades:

- `country`: Código de país ISO 3166-1 alpha-2 (por exemplo, ‘US’, ‘AU’, ‘DE’, ‘JP’). O padrão é ‘US’.
- `languages`: Uma lista (array) de idiomas e localidades preferidos para a requisição, em ordem de prioridade. O padrão é o idioma da localização especificada.

Para mais detalhes sobre as localizações compatíveis, consulte a [documentação de proxies](https://docs.firecrawl.dev/pt-BR/features/proxies).

## Cache e maxAge

Para acelerar as requisições, o Firecrawl retorna resultados do cache por padrão quando há uma cópia recente disponível.

- **Janela de frescor padrão**: `maxAge = 172800000` ms (2 dias). Se a página em cache for mais recente do que isso, ela é retornada instantaneamente; caso contrário, a página é coletada novamente e então armazenada em cache.
- **Desempenho**: Pode acelerar as coletas em até 5x quando os dados não precisam estar ultra recentes.
- **Sempre buscar conteúdo novo**: Defina `maxAge` como `0`. Observe que isso ignora totalmente o cache, então toda requisição passa por todo o pipeline de coleta, o que significa que a requisição levará mais tempo para ser concluída e terá maior chance de falhar. Use um `maxAge` diferente de zero se a atualização em toda requisição não for crítica.
- **Evitar armazenamento**: Defina `storeInCache` como `false` se você não quiser que o Firecrawl armazene em cache os resultados desta requisição.
- **Consulta somente no cache**: Defina `minAge` para fazer uma consulta somente no cache sem acionar uma nova coleta. O valor está em milissegundos e especifica a idade mínima que os dados em cache devem ter. Se nenhum dado em cache for encontrado, um `404` com o código de erro `SCRAPE_NO_CACHED_DATA` é retornado. Defina `minAge` como `1` para aceitar qualquer dado em cache, independentemente da idade.
- **Rastreio de mudanças**: Requisições que incluem `changeTracking` ignoram o cache, então `maxAge` é desconsiderado.

Exemplo (forçar conteúdo novo):

Exemplo (usar uma janela de cache de 10 minutos):

## Scraping em lote de várias URLs

Agora é possível fazer scraping em lote de várias URLs ao mesmo tempo. A função recebe as URLs iniciais e parâmetros opcionais como argumentos. O parâmetro params permite definir opções adicionais para a tarefa de scraping em lote, como os formatos de saída.

### Como funciona

Funciona de forma muito semelhante ao endpoint `/crawl`. Ele cria um job de raspagem em lote e retorna um ID do job para você acompanhar o status da raspagem em lote. O SDK oferece 2 métodos: síncrono e assíncrono. O método síncrono retorna os resultados do job de raspagem em lote, enquanto o método assíncrono retorna um ID do job que você pode usar para verificar o status da raspagem em lote.

### Como usar

### Resposta

Se você estiver usando os métodos síncronos dos SDKs, eles retornarão os resultados do job de scraping em lote. Caso contrário, será retornado um ID de job que você pode usar para verificar o status do scraping em lote.

#### Sincronamente

```
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Página inicial da documentação do Firecrawl![logo claro](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Crie um ‘chat com o site’ usando Groq Llama 3 | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Aprenda a usar o Firecrawl, o Groq Llama 3 e o LangChain para criar um bot de ‘chat com o seu site’."
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

#### Assíncrono

Você pode usar o ID da tarefa para verificar o status do batch scrape chamando o endpoint `/batch/scrape/{id}`. Este endpoint deve ser usado enquanto a tarefa ainda estiver em execução ou logo após sua conclusão, **pois as tarefas de batch scrape expiram após 24 horas**.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Modo Enhanced

Para sites complexos, o Firecrawl oferece um modo enhanced que aumenta as taxas de sucesso ao mesmo tempo em que preserva a privacidade. Saiba mais sobre o [Modo Enhanced](https://docs.firecrawl.dev/pt-BR/features/enhanced-mode).

## Retenção zero de dados (ZDR)

O Firecrawl oferece Retenção zero de dados (ZDR) para equipes com requisitos rigorosos de tratamento de dados. Quando ativado, o Firecrawl não persistirá nenhum conteúdo de página nem dados extraídos além da duração da requisição. Para ativar o ZDR, defina `zeroDataRetention: true` na sua requisição:

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "url": "https://example.com",
    "formats": ["markdown"],
    "zeroDataRetention": true
  }'
```

O ZDR está disponível nos planos Enterprise e precisa ser habilitado para a sua equipe. Acesse [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) para começar. O ZDR adiciona **1 crédito adicional por página** ao custo base de scraping.

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções automatizadas de integração.