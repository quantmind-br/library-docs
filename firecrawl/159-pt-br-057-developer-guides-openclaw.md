---
title: Usando o OpenClaw com o Firecrawl
url: https://docs.firecrawl.dev/pt-BR/developer-guides/openclaw
source: sitemap
fetched_at: 2026-03-23T07:33:44.43664-03:00
rendered_js: false
word_count: 385
summary: Este documento orienta sobre a integração da CLI do Firecrawl com agentes OpenClaw para habilitar funcionalidades de scraping, busca e navegação remota em sandbox.
tags:
    - firecrawl
    - openclaw
    - web-scraping
    - ai-agents
    - cli-tools
    - browser-automation
category: guide
---

Integre o Firecrawl com o OpenClaw para dar aos seus agentes a capacidade de fazer scraping, busca, crawling, extração e interação com a web — tudo por meio do [Firecrawl CLI](https://docs.firecrawl.dev/pt-BR/sdks/cli).

## Por que Firecrawl + OpenClaw

- **Nenhum navegador local necessário** — cada sessão é executada em um sandbox remoto e isolado. Sem instalações de Chromium, sem conflitos de drivers, sem pressão de RAM na sua máquina.
- **Paralelismo de verdade** — execute muitas sessões de navegador ao mesmo tempo, sem disputa por recursos locais. Os agentes podem navegar em lotes por vários sites simultaneamente.
- **Seguro por padrão** — navegação, avaliação do DOM e extração acontecem dentro de sandboxes descartáveis, não na sua estação de trabalho.
- **Melhor economia de tokens** — os agentes recebem artefatos limpos (snapshots, campos extraídos) em vez de arrastar DOMs gigantes e logs de drivers para dentro da janela de contexto.
- **Kit de ferramentas web completo** — scraping, busca e automação de navegador, tudo por meio de uma única CLI que seu agente já sabe usar.

## Configuração

Peça ao seu agente para instalar a Firecrawl CLI, fazer a autenticação e inicializar a skill com este comando:

```
npx -y firecrawl-cli init --browser --all
```

- `--all` instala a skill do Firecrawl em todos os agentes de codificação de IA detectados
- `--browser` abre o navegador automaticamente para autenticação do Firecrawl

ou instale tudo separadamente:

```
npm install -g firecrawl-cli
firecrawl init skills
firecrawl login --browser
# Ou, pule o navegador e forneça sua chave de API diretamente:
export FIRECRAWL_API_KEY="fc-YOUR-API-KEY"
```

Verifique se tudo está configurado corretamente:

## Scrape

Faça o scraping de uma única página e extraia seu conteúdo:

```
firecrawl https://example.com --only-main-content
```

Obtenha formatos específicos:

```
firecrawl https://example.com --format markdown,links --pretty
```

## Busca

Pesquise na web e, opcionalmente, extraia dados dos resultados:

```
firecrawl search "latest AI funding rounds 2025" --limit 10

# Pesquisar e extrair os resultados
firecrawl search "OpenClaw documentation" --scrape --scrape-formats markdown
```

## Browser

Inicie uma sessão remota de navegador para automação interativa. Cada sessão é executada em um sandbox isolado — não requer instalação local do Chromium. O `agent-browser` já vem pré-instalado com mais de 40 comandos.

```
# Atalho: inicia automaticamente uma sessão se nenhuma estiver ativa
firecrawl browser "open https://news.ycombinator.com"
firecrawl browser "snapshot"
firecrawl browser "scrape"
firecrawl browser close
```

Interaja com os elementos da página usando refs do snapshot:

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
# snapshot retorna IDs @ref — use-os para interagir
firecrawl browser "click @e5"
firecrawl browser "fill @e3 'search query'"
firecrawl browser "scrape"
firecrawl browser close
```

## Exemplo: diga ao seu agente

Aqui estão alguns prompts que você pode dar ao seu agente OpenClaw:

- *“Use Firecrawl para fazer scraping de [https://example.com](https://example.com) e resuma o conteúdo principal.”*
- *“Busque as notícias mais recentes sobre a OpenAI e me dê um resumo dos 5 principais resultados.”*
- *“Use o Firecrawl Browser para abrir o Hacker News, obter os 5 principais posts e os primeiros 10 comentários de cada um.”*
- *“Rastreie a documentação em [https://docs.firecrawl.dev](https://docs.firecrawl.dev) e salve tudo em um arquivo.”*

## Leituras adicionais

- [Referência da CLI do Firecrawl](https://docs.firecrawl.dev/pt-BR/sdks/cli)
- [Documentação do Browser Sandbox](https://docs.firecrawl.dev/pt-BR/features/browser)
- [Documentação do Agent](https://docs.firecrawl.dev/pt-BR/features/agent)