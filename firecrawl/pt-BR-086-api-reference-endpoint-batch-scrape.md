---
title: Raspar em lote - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:11:58.840562-03:00
rendered_js: false
word_count: 951
summary: This document provides technical documentation for the Firecrawl batch scraping API, detailing parameters for URL processing, output formats, caching, and proxy settings.
tags:
    - api-documentation
    - web-scraping
    - firecrawl
    - batch-processing
    - proxy-configuration
    - data-extraction
category: reference
---

[Pular para o conteúdo principal](#content-area)

Raspe várias URLs e, opcionalmente, extraia informações com um LLM

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de onboarding automatizado.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corpo

Objeto de especificação de webhook.

Número máximo de scrapes simultâneos. Este parâmetro permite definir um limite de concorrência para este scrape em lote. Se não for especificado, o scrape em lote seguirá o limite de concorrência da sua equipe.

Se URLs inválidas forem especificadas no array urls, elas serão ignoradas. Em vez de fazer com que toda a requisição falhe, será criada uma raspagem em lote usando apenas as URLs válidas restantes, e as URLs inválidas serão retornadas no campo invalidURLs da resposta.

formats

(Markdown · object | Summary · object | HTML · object | Raw HTML · object | Links · object | Images · object | Screenshot · object | JSON · object | Change Tracking · object | Branding · object)\[]

Formatos de saída que devem ser incluídos na resposta. Você pode especificar um ou mais formatos, como strings (por exemplo, `'markdown'`) ou como objetos com opções adicionais (por exemplo, `{ type: 'json', schema: {...} }`). Alguns formatos exigem que opções específicas sejam configuradas. Exemplo: `['markdown', { type: 'json', schema: {...} }]`.

- Markdown
- Summary
- HTML
- Raw HTML
- Links
- Images
- Screenshot
- JSON
- Change Tracking
- Branding

Retorne somente o conteúdo principal da página, excluindo cabeçalhos, elementos de navegação, rodapés etc.

Tags a serem incluídas no resultado.

Tags a serem excluídas da saída.

Retorna uma versão em cache da página se ela for mais recente do que essa idade em milissegundos. Se a versão em cache da página for mais antiga do que esse valor, a página será novamente coletada. Se você não precisa de dados extremamente atualizados, ativar isso pode acelerar suas coletas em até 500%. O padrão é 2 dias.

Quando definido, a requisição verifica apenas o cache e nunca aciona uma nova extração. O valor está em milissegundos e especifica a idade mínima que os dados em cache devem ter. Se houver dados em cache correspondentes, eles serão retornados instantaneamente. Se nenhum dado em cache for encontrado, será retornado um 404 com o código de erro SCRAPE\_NO\_CACHED\_DATA. Defina como 1 para aceitar qualquer dado em cache, independentemente da idade.

Cabeçalhos a serem enviados na requisição. Podem ser usados para enviar cookies, user-agent etc.

Defina um atraso, em milissegundos, antes de buscar o conteúdo, permitindo que a página tenha tempo suficiente para carregar. Esse tempo de espera é somado ao recurso de espera inteligente do Firecrawl.

Defina como true se quiser emular a extração a partir de um dispositivo móvel. Útil para testar páginas responsivas e capturar screenshots da versão mobile.

Ignorar a verificação de certificado TLS ao realizar requisições.

Tempo limite, em milissegundos, para a requisição. O mínimo é 1000 (1 segundo). O default é 30000 (30 segundos). O máximo é 300000 (300 segundos).

Intervalo obrigatório: `1000 <= x <= 300000`

Controla como os arquivos são processados durante o scraping. Quando "pdf" é incluído (padrão), o conteúdo do PDF é extraído e convertido em markdown, com cobrança baseada no número de páginas (1 crédito por página). Quando um array vazio é fornecido, o arquivo PDF é retornado em codificação base64 com uma taxa fixa de 1 crédito para todo o PDF.

actions

(Wait by Duration · object | Wait for Element · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

Ações a serem executadas na página antes de extrair o conteúdo

- Wait by Duration
- Wait for Element
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

Configurações de localização da requisição. Quando definidas, será usado um proxy apropriado, se disponível, e serão emuladas as configurações correspondentes de idioma e fuso horário. O padrão é "US" se não for especificado.

Remove todas as imagens em base64 do resultado em markdown, que pode se tornar excessivamente longo. Isso não afeta os formatos html nem rawHtml. O texto alternativo da imagem permanece no resultado, mas a URL é substituída por um placeholder.

Habilita o bloqueio de anúncios e de pop-ups de cookies.

Especifica o tipo de proxy a ser utilizado.

- basic: Proxies para scraping de sites sem soluções anti‑bot ou apenas com soluções anti‑bot básicas. Rápido e geralmente funciona.
- enhanced: Proxies avançados para scraping de sites com soluções anti‑bot avançadas. Mais lento, porém mais confiável em alguns sites. Pode custar até 5 créditos por requisição.
- auto: O Firecrawl tentará automaticamente refazer o scraping com proxies enhanced se o proxy basic falhar. Se a nova tentativa com enhanced for bem-sucedida, 5 créditos serão cobrados pelo scraping. Se a primeira tentativa com basic for bem-sucedida, apenas o custo regular será cobrado.

Opções disponíveis:

`basic`,

`enhanced`,

`auto`

Se definido como true, a página será armazenada no índice e no cache do Firecrawl. Definir isso como false é útil se sua atividade de scraping puder levantar preocupações relacionadas à proteção de dados. O uso de alguns parâmetros associados a scraping sensível (por exemplo, ações, headers) fará com que esse parâmetro seja definido automaticamente como false.

Se definido como true, isso ativará a política de não retenção de dados para esta execução de scraping em lote. Para habilitar esse recurso, entre em contato com [help@firecrawl.dev](mailto:help@firecrawl.dev)

#### Resposta

Se ignoreInvalidURLs for true, este será um array com as URLs inválidas especificadas na requisição. Se não houver URLs inválidas, será um array vazio. Se ignoreInvalidURLs for false, este campo permanecerá undefined.