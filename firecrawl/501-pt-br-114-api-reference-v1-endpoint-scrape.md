---
title: Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/scrape
source: sitemap
fetched_at: 2026-03-23T07:10:16.238892-03:00
rendered_js: false
word_count: 641
summary: This document provides the API specification for the scrape endpoint, detailing parameters for content extraction, proxy management, cache control, and browser actions.
tags:
    - api-reference
    - web-scraping
    - data-extraction
    - proxy-configuration
    - automation-tools
category: api
---

[Pular para o conteúdo principal](#content-area)

Raspar uma única URL e, opcionalmente, extrair informações usando um LLM

> Observação: uma nova [versão v2 desta API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/scrape) já está disponível, com recursos e desempenho aprimorados.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corpo

Retorne apenas o conteúdo principal da página, excluindo cabeçalhos, áreas de navegação, rodapés etc.

Tags para incluir na saída.

Tags a serem excluídas da saída.

Retorna uma versão em cache da página se ela tiver menos que essa idade, em milissegundos. Se a versão em cache da página for mais antiga que esse valor, a página será raspada novamente. Se você não precisar de dados extremamente atualizados, ativar essa opção pode acelerar suas raspagens em até 500%. O padrão é 0, o que desativa o cache.

Cabeçalhos a serem enviados com a requisição. Podem ser usados para enviar cookies, user-agent etc.

Defina um atraso, em milissegundos, antes de buscar o conteúdo, permitindo que a página tenha tempo suficiente para carregar.

Defina como true para emular a raspagem de dados a partir de um dispositivo móvel. Útil para testar páginas responsivas e gerar capturas de tela da versão mobile.

Ignorar a verificação do certificado TLS ao fazer requisições

Tempo limite da requisição em milissegundos

Controla como os arquivos PDF são processados durante o scraping. Quando definido como true, o conteúdo do PDF é extraído e convertido para o formato Markdown, com cobrança baseada no número de páginas (1 crédito por página). Quando definido como false, o arquivo PDF é retornado codificado em base64, com uma tarifa fixa de 1 crédito no total.

actions

(Wait · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

Ações a serem realizadas na página antes de extrair o conteúdo

- Wait
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

Configurações de localização para a requisição. Quando especificadas, será usado um proxy apropriado, se disponível, e serão emuladas as configurações correspondentes de idioma e fuso horário. O padrão é "US" se não for especificado.

Remove todas as imagens em base64 da saída, que podem ser excessivamente longas. O texto alternativo (alt) da imagem permanece na saída, mas a URL é substituída por um espaço reservado.

Habilita o bloqueio de anúncios e de pop-ups de cookies.

Especifica o tipo de proxy a ser usado.

- basic: Proxies para scraping de sites sem ou com soluções anti-bot básicas. Rápido e geralmente funciona.
- enhanced: Proxies avançados para scraping de sites com soluções anti-bot mais sofisticadas. Mais lento, mas mais confiável em certos sites. Custa até 5 créditos por requisição.
- auto: O Firecrawl tentará automaticamente fazer o scraping novamente com proxies enhanced se o proxy basic falhar. Se a nova tentativa com enhanced for bem-sucedida, 5 créditos serão cobrados pelo scraping. Se a primeira tentativa com basic for bem-sucedida, apenas o custo normal será cobrado.

Se você não especificar um proxy, o Firecrawl usará basic por padrão.

Opções disponíveis:

`basic`,

`enhanced`,

`auto`

Se definido como true, a página será armazenada no índice e no cache do Firecrawl. Definir isso como false é útil se sua atividade de scraping puder levantar preocupações relacionadas à proteção de dados. O uso de alguns parâmetros associados a scraping sensível (ações, headers) fará com que esse parâmetro seja definido como false.

Formatos a serem incluídos no resultado.

Opções disponíveis:

`markdown`,

`html`,

`rawHtml`,

`links`,

`screenshot`,

`screenshot@fullPage`,

`json`,

`changeTracking`

Opções de rastreio de mudanças (Beta). Aplicável somente quando 'changeTracking' estiver incluído em formatos. O formato 'markdown' também deve ser especificado ao usar o rastreio de mudanças.

Se definido como true, isso ativará retenção zero de dados para este scrape. Para ativar esse recurso, entre em contato com [help@firecrawl.dev](mailto:help@firecrawl.dev)

#### Resposta