---
title: CLI | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/sdks/cli
source: sitemap
fetched_at: 2026-03-23T07:21:34.442647-03:00
rendered_js: false
word_count: 1155
summary: This document provides a comprehensive guide to installing, configuring, and using the Firecrawl command-line interface for web scraping, site mapping, and web searching.
tags:
    - firecrawl
    - web-scraping
    - cli
    - automation
    - data-extraction
    - api-integration
category: reference
---

## Instalação

Se você estiver usando algum agente de IA, como o Claude Code, poderá instalar a Firecrawl Skill abaixo, e o agente conseguirá configurá-la para você.

```
npx -y firecrawl-cli@latest init --all --browser
```

- `--all` instala a Firecrawl Skill em todos os agentes de codificação de IA detectados
- `--browser` abre o navegador automaticamente para autenticação do Firecrawl

Você também pode instalar manualmente a CLI do Firecrawl globalmente usando npm:

```
# Instale globalmente com npm
npm install -g firecrawl-cli
```

## Autenticação

Antes de usar a CLI, você precisa autenticar-se com sua chave de API do Firecrawl.

### Login

```
# Login interativo (abre o navegador ou solicita a chave da API)
firecrawl login

# Login com autenticação do navegador (recomendado para agentes)
firecrawl login --browser

# Login com chave da API diretamente
firecrawl login --api-key fc-YOUR-API-KEY

# Ou defina via variável de ambiente
export FIRECRAWL_API_KEY=fc-YOUR-API-KEY
```

### Visualizar configuração

```
# Ver configuração atual e status de autenticação
firecrawl view-config
```

### Logout

```
# Limpar credenciais armazenadas
firecrawl logout
```

### Auto-hospedado / Desenvolvimento local

Para instâncias auto-hospedadas do Firecrawl ou para desenvolvimento local, use a opção `--api-url`:

```
# Use uma instância local do Firecrawl (nenhuma chave de API necessária)
firecrawl --api-url http://localhost:3002 scrape https://example.com

# Or set via environment variable
export FIRECRAWL_API_URL=http://localhost:3002
firecrawl scrape https://example.com

# Configure and persist the custom API URL
firecrawl config --api-url http://localhost:3002
```

Ao usar uma URL de API personalizada (qualquer endereço diferente de `https://api.firecrawl.dev`), a autenticação por chave de API é automaticamente ignorada, permitindo que você use instâncias locais sem uma chave de API.

### Verificar status

Verifique se a instalação e a autenticação estão corretas e consulte os limites de taxa:

Resultado quando estiver pronto:

```
  🔥 firecrawl cli v1.1.1

  ● Authenticated via FIRECRAWL_API_KEY
  Concurrency: 0/100 jobs (parallel scrape limit)
  Credits: 500,000 remaining
```

- **Concorrência**: Máximo de tarefas em paralelo. Execute operações paralelas próximas a esse limite, mas sem ultrapassá-lo.
- **Créditos**: Créditos de API disponíveis. Cada operação de scrape/crawl consome créditos.

## Comandos

### Scrape

Faça scraping de uma única URL e extraia seu conteúdo em vários formatos.

```
# Faz scrape de uma URL (padrão: saída em markdown)
firecrawl https://example.com

# Ou use o comando explícito de scrape
firecrawl scrape https://example.com

# Recomendado: use --only-main-content para saída limpa sem navegação/rodapé
firecrawl https://example.com --only-main-content
```

#### Formatos de saída

```
# Obter saída em HTML
firecrawl https://example.com --html

# Múltiplos formatos (retorna JSON)
firecrawl https://example.com --format markdown,links

# Obter imagens de uma página
firecrawl https://example.com --format images

# Obter um resumo do conteúdo da página
firecrawl https://example.com --format summary

# Rastrear mudanças em uma página
firecrawl https://example.com --format changeTracking

# Formatos disponíveis: markdown, html, rawHtml, links, screenshot, json, images, summary, changeTracking, attributes, branding
```

#### Opções de Scrape

```
# Extrai apenas o conteúdo principal (remove navegação e rodapés)
firecrawl https://example.com --only-main-content

# Wait for JavaScript rendering
firecrawl https://example.com --wait-for 3000

# Take a screenshot
firecrawl https://example.com --screenshot

# Include/exclude specific HTML tags
firecrawl https://example.com --include-tags article,main
firecrawl https://example.com --exclude-tags nav,footer

# Save output to file
firecrawl https://example.com -o output.md

# Pretty print JSON output
firecrawl https://example.com --format markdown,links --pretty

# Force JSON output even with single format
firecrawl https://example.com --json

# Show request timing information
firecrawl https://example.com --timing
```

**Opções disponíveis:**

OpçãoAtalhoDescrição`--url <url>``-u`URL para extrair conteúdo (alternativa ao argumento posicional)`--format <formats>``-f`formatos de saída (separados por vírgula): `markdown`, `html`, `rawHtml`, `links`, `screenshot`, `json`, `images`, `summary`, `rastreioDeMudanças`, `attributes`, `branding``--html``-H`Atalho para `--format html``--only-main-content`Extrair apenas o conteúdo principal`--wait-for <ms>`Tempo de espera, em milissegundos, para renderização de JS`--screenshot`Fazer uma captura de tela`--include-tags <tags>`Tags HTML a incluir (separadas por vírgula)`--exclude-tags <tags>`Tags HTML a excluir (separadas por vírgula)`--output <path>``-o`Salvar o resultado em um arquivo`--json`Forçar saída em JSON mesmo com um único formato`--pretty`Imprimir a saída JSON formatada`--timing`Mostrar tempo da requisição e outras informações úteis

* * *

### Pesquisar

Pesquise na web e, opcionalmente, faça o scraping dos resultados.

```
# Pesquisar na web
firecrawl search "web scraping tutorials"

# Limitar resultados
firecrawl search "AI news" --limit 10

# Imprimir resultados formatados
firecrawl search "machine learning" --pretty
```

#### Opções de busca

```
# Search specific sources
firecrawl search "AI" --sources web,news,images

# Buscar com filtros de categoria
firecrawl search "react hooks" --categories github
firecrawl search "machine learning" --categories research,pdf

# Time-based filtering
firecrawl search "tech news" --tbs qdr:h   # Last hour
firecrawl search "tech news" --tbs qdr:d   # Last day
firecrawl search "tech news" --tbs qdr:w   # Last week
firecrawl search "tech news" --tbs qdr:m   # Last month
firecrawl search "tech news" --tbs qdr:y   # Last year

# Location-based search
firecrawl search "restaurants" --location "Berlin,Germany" --country DE

# Search and scrape results
firecrawl search "documentation" --scrape --scrape-formats markdown

# Save to file
firecrawl search "firecrawl" --pretty -o results.json
```

**Opções disponíveis:**

OpçãoDescrição`--limit <number>`Número máximo de resultados (padrão: 5, máx.: 100)`--sources <sources>`Fontes de pesquisa: `web`, `images`, `news` (separadas por vírgula)`--categories <categories>`Filtrar por categoria: `github`, `research`, `pdf` (separadas por vírgula)`--tbs <value>`Filtro de tempo: `qdr:h` (hora), `qdr:d` (dia), `qdr:w` (semana), `qdr:m` (mês), `qdr:y` (ano)`--location <location>`Segmentação geográfica (ex.: “Berlin,Germany”)`--country <code>`Código de país ISO (padrão: US)`--timeout <ms>`Tempo limite em milissegundos (padrão: 60000)`--ignore-invalid-urls`Excluir URLs inválidas para outros endpoints do Firecrawl`--scrape`Fazer scraping dos resultados da pesquisa`--scrape-formats <formats>`Formatos para o conteúdo extraído (padrão: markdown)`--only-main-content`Incluir apenas o conteúdo principal ao fazer scraping (padrão: true)`--json`Saída em JSON`--output <path>`Salvar saída em arquivo`--pretty`Imprimir saída JSON formatada

* * *

### Mapear

Descubra rapidamente todas as URLs de um site.

```
# Descobre todas as URLs de um site
firecrawl map https://example.com

# Output as JSON
firecrawl map https://example.com --json

# Limit number of URLs
firecrawl map https://example.com --limit 500
```

#### Opções do Map

```
# Filtrar URLs por consulta de pesquisa
firecrawl map https://example.com --search "blog"

# Incluir subdomínios
firecrawl map https://example.com --include-subdomains

# Controlar uso do sitemap
firecrawl map https://example.com --sitemap include   # Usar sitemap
firecrawl map https://example.com --sitemap skip      # Pular sitemap
firecrawl map https://example.com --sitemap only      # Usar apenas sitemap

# Ignorar parâmetros de consulta (dedupe URLs)
firecrawl map https://example.com --ignore-query-parameters

# Aguardar conclusão do mapeamento com timeout
firecrawl map https://example.com --wait --timeout 60

# Salvar em arquivo
firecrawl map https://example.com -o urls.txt
firecrawl map https://example.com --json --pretty -o urls.json
```

**Opções disponíveis:**

OpçãoDescrição`--url <url>`URL a ser mapeada (alternativa ao argumento posicional)`--limit <number>`Número máximo de URLs a serem descobertas`--search <query>`Filtra URLs pela consulta de busca`--sitemap <mode>`Tratamento de sitemap: `include`, `skip`, `only``--include-subdomains`Inclui subdomínios`--ignore-query-parameters`Trata URLs com parâmetros diferentes como iguais`--wait`Aguarda o término do mapeamento`--timeout <seconds>`Tempo máximo de espera, em segundos`--json`Saída em JSON`--output <path>`Salva a saída em um arquivo`--pretty`Imprime a saída JSON formatada

* * *

### Navegador

Faça seus agentes interagirem com a web usando um sandbox seguro de navegador. Inicie sessões de navegador na nuvem e execute código Python, JavaScript ou bash remotamente. Cada sessão executa uma instância completa do Chromium — sem necessidade de instalar um navegador local. O código é executado no servidor com um objeto `page` do [Playwright](https://playwright.dev/) pré-configurado e pronto para uso.

```
# Launch a cloud browser session
firecrawl browser launch-session

# Executar comandos agent-browser (padrão - "agent-browser" é prefixado automaticamente)
firecrawl browser execute "open https://example.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "click @e5"
firecrawl browser execute "scrape"

# Execute Playwright Python code
firecrawl browser execute --python 'await page.goto("https://example.com")
print(await page.title())'

# Execute Playwright JavaScript code
firecrawl browser execute --node 'await page.goto("https://example.com"); console.log(await page.title());'

# List all sessions (or: list active / list destroyed)
firecrawl browser list

# Close the active session
firecrawl browser close
```

#### Opções do navegador

```
# Launch with custom TTL (10 minutes) and live view
firecrawl browser launch-session --ttl 600 --stream

# Launch with inactivity timeout
firecrawl browser launch-session --ttl 120 --ttl-inactivity 60

# comandos agent-browser (padrão - "agent-browser" é prefixado automaticamente)
firecrawl browser execute "open https://news.ycombinator.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "click @e3"
firecrawl browser execute "scrape"

# Playwright Python - navigate, interact, extract
firecrawl browser execute --python '
await page.goto("https://news.ycombinator.com")
items = await page.query_selector_all(".titleline > a")
for item in items[:5]:
    print(await item.text_content())
'

# Playwright JavaScript - same page object
firecrawl browser execute --node '
await page.goto("https://example.com");
const title = await page.title();
console.log(title);
'

# Explicit bash mode - runs in the sandbox
firecrawl browser execute --bash "agent-browser snapshot"

# Target a specific session
firecrawl browser execute --session <id> --python 'print(await page.title())'

# Save output to file
firecrawl browser execute "scrape" -o result.txt

# Close a specific session
firecrawl browser close --session <id>

# List sessions (all / active / destroyed)
firecrawl browser list
firecrawl browser list active --json
```

**Subcomandos:**

SubcommandDescription`launch-session`Inicia uma nova sessão de navegador na nuvem (retorna o ID da sessão, a URL CDP e a URL de visualização ao vivo)`execute <code>`Executa código Playwright Python/JS ou comandos bash em uma sessão`list [status]`Lista sessões de navegador (filtra por `active` ou `destroyed`)`close`Encerra uma sessão de navegador

**Opções de execução:**

OptionDescription`--bash`Executa comandos bash remotamente no sandbox (padrão). O [agent-browser](https://github.com/vercel-labs/agent-browser) (40+ comandos) vem pré-instalado e com prefixo automático. `CDP_URL` é injetado automaticamente para que o agent-browser se conecte à sua sessão automaticamente. Melhor abordagem para agentes de IA.`--python`Executa como código Playwright Python. Um objeto `page` do Playwright está disponível — use `await page.goto()`, `await page.title()`, etc.`--node`Executa como código Playwright JavaScript. Mesmo objeto `page` disponível.`--session <id>`Usa uma sessão específica (padrão: sessão ativa)

**Opções de inicialização:**

OptionDescription`--ttl <seconds>`TTL total da sessão (padrão: 600, intervalo: 30–3600)`--ttl-inactivity <seconds>`Fecha automaticamente após inatividade (intervalo: 10–3600)`--profile <name>`Nome de um perfil (salva e reutiliza o estado do navegador entre sessões)`--no-save-changes`Carrega dados de perfil existentes sem salvar as alterações de volta`--stream`Habilita streaming de visualização ao vivo

**Opções comuns:**

OptionDescription`--output <path>`Salva a saída em arquivo`--json`Saída em formato JSON

* * *

### Crawl

Rastreia um site inteiro a partir de uma URL.

```
# Inicia um crawl (retorna o ID do job imediatamente)
firecrawl crawl https://example.com

# Aguarda a conclusão do crawl
firecrawl crawl https://example.com --wait

# Aguarda com indicador de progresso
firecrawl crawl https://example.com --wait --progress
```

#### Verificar status do crawl

```
# Verificar o status do crawl usando o ID do job
firecrawl crawl <job-id>

# Exemplo com um ID de job real
firecrawl crawl 550e8400-e29b-41d4-a716-446655440000
```

#### Opções de Crawl

```
# Limit crawl depth and pages
firecrawl crawl https://example.com --limit 100 --max-depth 3 --wait

# Include only specific paths
firecrawl crawl https://example.com --include-paths /blog,/docs --wait

# Exclude specific paths
firecrawl crawl https://example.com --exclude-paths /admin,/login --wait

# Include subdomains
firecrawl crawl https://example.com --allow-subdomains --wait

# Crawl entire domain
firecrawl crawl https://example.com --crawl-entire-domain --wait

# Rate limiting
firecrawl crawl https://example.com --delay 1000 --max-concurrency 2 --wait

# Intervalo de polling e timeout personalizados
firecrawl crawl https://example.com --wait --poll-interval 10 --timeout 300

# Save results to file
firecrawl crawl https://example.com --wait --pretty -o results.json
```

**Opções disponíveis:**

OpçãoDescrição`--url <url>`URL para rastrear (alternativa ao argumento posicional)`--wait`Aguardar a conclusão do crawl`--progress`Mostrar indicador de progresso enquanto aguarda`--poll-interval <seconds>`Intervalo de consulta (polling) (padrão: 5)`--timeout <seconds>`Tempo limite ao aguardar`--status`Verificar o status de uma tarefa de crawl existente`--limit <number>`Número máximo de páginas a rastrear`--max-depth <number>`Profundidade máxima do crawl`--include-paths <paths>`Caminhos a incluir (separados por vírgula)`--exclude-paths <paths>`Caminhos a excluir (separados por vírgula)`--sitemap <mode>`Tratamento de sitemap: `include`, `skip`, `only``--allow-subdomains`Incluir subdomínios`--allow-external-links`Seguir links externos`--crawl-entire-domain`Rastrear o domínio inteiro`--ignore-query-parameters`Tratar URLs com parâmetros diferentes como iguais`--delay <ms>`Atraso entre requisições`--max-concurrency <n>`Máximo de requisições concorrentes`--output <path>`Salvar resultado em arquivo`--pretty`Imprimir saída JSON formatada

* * *

### Agent

Busque e colete dados na web usando prompts em linguagem natural.

```
# Basic usage - URLs are optional
firecrawl agent "Encontre as 5 principais startups de IA e seus valores de financiamento" --wait

# Focus on specific URLs
firecrawl agent "Compare pricing plans" --urls https://slack.com/pricing,https://teams.microsoft.com/pricing --wait

# Use a schema for structured output
firecrawl agent "Get company information" --urls https://example.com --schema '{"name": "string", "founded": "number"}' --wait

# Use schema from a file
firecrawl agent "Get product details" --urls https://example.com --schema-file schema.json --wait
```

#### Opções do Agente

```
# Use Spark 1 Pro for higher accuracy
firecrawl agent "Competitive analysis across multiple domains" --model spark-1-pro --wait

# Set max credits to limit costs
firecrawl agent "Gather contact information from company websites" --max-credits 100 --wait

# Check status of an existing job
firecrawl agent <job-id> --status

# Intervalo de polling e timeout personalizados
firecrawl agent "Summarize recent blog posts" --wait --poll-interval 10 --timeout 300

# Save output to file
firecrawl agent "Find pricing information" --urls https://example.com --wait -o pricing.json --pretty
```

**Opções disponíveis:**

OptionDescription`--urls <urls>`Lista opcional de URLs nas quais o agente deve focar (separadas por vírgula)`--model <model>`Modelo a ser usado: `spark-1-mini` (padrão, 60% mais barato) ou `spark-1-pro` (maior precisão)`--schema <json>`Esquema JSON para saída estruturada (string JSON inline)`--schema-file <path>`Caminho para o arquivo de esquema JSON para saída estruturada`--max-credits <number>`Máximo de créditos a consumir (a tarefa falha se o limite for atingido)`--status`Verificar o status de uma tarefa de agente existente`--wait`Aguardar o agente concluir antes de retornar os resultados`--poll-interval <seconds>`Intervalo de polling enquanto aguarda (padrão: 5)`--timeout <seconds>`Tempo limite (timeout) enquanto aguarda (padrão: sem limite)`--output <path>`Salvar a saída em arquivo`--json`Saída em formato JSON

* * *

### Uso de créditos

Verifique o saldo de créditos e o uso pela sua equipe.

```
# Ver uso de créditos
firecrawl credit-usage

# Saída em JSON
firecrawl credit-usage --json --pretty
```

* * *

### Versão

Exibe a versão da CLI.

```
firecrawl version
# ou
firecrawl --version
```

## Opções globais

Essas opções estão disponíveis para todos os comandos:

OpçãoAtalhoDescrição`--status`Exibe a versão, autenticação, concorrência e créditos`--api-key <key>``-k`Substitui a chave de API armazenada para este comando`--api-url <url>`Usa uma URL de API personalizada (para self-hosting/desenvolvimento local)`--help``-h`Exibe a ajuda de um comando`--version``-V`Exibe a versão da CLI

## Manipulação da saída

A CLI envia a saída para stdout por padrão, facilitando o uso de pipes ou redirecionamentos:

```
# Pipe markdown para outro comando
firecrawl https://example.com | head -50

# Redirecionar para um arquivo
firecrawl https://example.com > output.md

# Salvar JSON com formatação legível
firecrawl https://example.com --format markdown,links --pretty -o data.json
```

### Comportamento dos formatos

- **Formato único**: Retorna o conteúdo bruto (texto markdown, HTML, etc.)
- **Múltiplos formatos**: Retorna um JSON com todos os dados solicitados

```
# Raw markdown output
firecrawl https://example.com --format markdown

# Saída JSON com múltiplos formatos
firecrawl https://example.com --format markdown,links
```

## Exemplos

### Raspagem rápida

```
# Obter conteúdo markdown de uma URL (use --only-main-content para saída limpa)
firecrawl https://docs.firecrawl.dev --only-main-content

# Get HTML content
firecrawl https://example.com --html -o page.html
```

### Rastreamento completo do site

```
# Rastreia um site de docs com limites
firecrawl crawl https://docs.example.com --limit 50 --max-depth 2 --wait --progress -o docs.json
```

### Descoberta de sites

```
# Encontre todas as postagens do blog
firecrawl map https://example.com --search "blog" -o blog-urls.txt
```

### Fluxo de Pesquisa

```
# Buscar e raspar resultados para pesquisa
firecrawl search "machine learning best practices 2024" --scrape --scrape-formats markdown --pretty
```

### Agente

```
# URLs are optional
firecrawl agent "Encontre as 5 principais startups de IA e seus valores de financiamento" --wait

# Focus on specific URLs
firecrawl agent "Compare pricing plans" --urls https://slack.com/pricing,https://teams.microsoft.com/pricing --wait
```

### Automação de navegadores

```
# Launch a session, scrape a page, and close
firecrawl browser launch-session
firecrawl browser execute "open https://news.ycombinator.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "scrape"
firecrawl browser close

# Usa agent-browser via modo bash (padrão — recomendado para agentes de IA)
firecrawl browser launch-session
firecrawl browser execute "open https://example.com"
firecrawl browser execute "snapshot"
# snapshot returns @ref IDs — use them to interact
firecrawl browser execute "click @e5"
firecrawl browser execute "fill @e3 'search query'"
firecrawl browser execute "scrape"
# Run --help to see all 40+ commands
firecrawl browser execute --bash "agent-browser --help"
firecrawl browser close

# Extrair URLs dos resultados de pesquisa
jq -r '.data.web[].url' search-results.json

# Get titles from search results
jq -r '.data.web[] | "\(.title): \(.url)"' search-results.json

# Extract links and process with jq
firecrawl https://example.com --format links | jq '.links[].url'

# Count URLs from map
firecrawl map https://example.com | wc -l
```

## Telemetria

A CLI coleta dados de uso anônimos durante a autenticação para ajudar a melhorar o produto:

- Versão da CLI, sistema operacional e versão do Node.js
- Detecção de ferramenta de desenvolvimento (como Cursor, VS Code, Claude Code)

**Nenhum dado relacionado a comandos, URLs ou conteúdo de arquivos é coletado via CLI.** Para desativar a telemetria, defina a seguinte variável de ambiente:

```
export FIRECRAWL_NO_TELEMETRY=1
```

## Open Source

A CLI e a Skill do Firecrawl são de código aberto e estão disponíveis no GitHub: [firecrawl/cli](https://github.com/firecrawl/cli)

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instruções de integração automatizada.