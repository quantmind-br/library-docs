---
title: Map - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:11:07.482634-03:00
rendered_js: false
word_count: 238
summary: This document describes the parameters and configuration options for mapping multiple URLs, including settings for sitemap handling, subdomain inclusion, and request timeouts.
tags:
    - url-mapping
    - web-crawling
    - api-configuration
    - sitemap-settings
    - proxy-settings
    - firecrawl-api
category: api
---

[Pular para o conteúdo principal](#content-area)

Mapear várias URLs com base em opções

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções automatizadas de onboarding.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corpo

URL base de onde o rastreamento será iniciado

Especifique uma consulta de pesquisa para ordenar os resultados por relevância. Exemplo: "blog" retornará URLs que contenham a palavra "blog" na URL, ordenadas por relevância.

sitemap

enum&lt;string&gt;

padrão:include

Modo de uso do sitemap durante o mapeamento. Se você definir como `skip`, o sitemap não será usado para encontrar URLs. Se você definir como `only`, apenas URLs que estiverem no sitemap serão retornadas. Por padrão (`include`), o sitemap e outros métodos serão usados em conjunto para encontrar URLs.

Opções disponíveis:

`skip`,

`include`,

`only`

Incluir subdomínios do site

Não retorne URLs com parâmetros de query

Ignora o cache do sitemap para obter URLs atualizadas. Os dados do sitemap ficam em cache por até 7 dias; use este parâmetro quando o seu sitemap tiver sido atualizado recentemente.

Número máximo de links retornados

Intervalo obrigatório: `x <= 100000`

Tempo limite, em milissegundos. Não há tempo limite definido por padrão.

Configurações de localização para a requisição. Quando especificadas, será usado um proxy apropriado, se disponível, e serão emulados o idioma e o fuso horário correspondentes. O padrão é 'US' caso não seja especificado.

#### Resposta