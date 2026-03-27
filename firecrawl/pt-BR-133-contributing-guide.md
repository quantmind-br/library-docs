---
title: Executando Localmente | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/contributing/guide
source: sitemap
fetched_at: 2026-03-23T07:31:42.610264-03:00
rendered_js: false
word_count: 362
summary: Este guia fornece instruções detalhadas para configurar, instalar dependências e executar o servidor da API Firecrawl em um ambiente de desenvolvimento local.
tags:
    - firecrawl
    - api-setup
    - node-js
    - postgresql
    - redis
    - docker
    - local-development
category: guide
---

Este guia explica como executar o servidor da API do Firecrawl na sua máquina local. Siga estas etapas para configurar o ambiente de desenvolvimento, iniciar os serviços e enviar sua primeira requisição. Se você estiver contribuindo, o processo segue as convenções padrão de código aberto: faça um fork do repositório, faça alterações, execute os testes e abra um pull request. Para tirar dúvidas ou obter ajuda para começar, entre em contato pelo e-mail [help@firecrawl.com](mailto:help@firecrawl.com) ou [envie uma issue](https://github.com/mendableai/firecrawl/issues).

## Pré-requisitos

Instale o seguinte antes de prosseguir:

DependênciaObrigatórioGuia de instalaçãoNode.jsSim[nodejs.org](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)pnpm (v9+)Sim[pnpm.io](https://pnpm.io/installation)RedisSim[redis.io](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)PostgreSQLSimVia Docker (veja abaixo) ou instalado diretamenteDockerOpcionalNecessário para a configuração do contêiner do PostgreSQL

## Configure o banco de dados

Você precisa de um banco de dados PostgreSQL inicializado com o esquema definido em `apps/nuq-postgres/nuq.sql`. A maneira mais simples é usar a imagem Docker em `apps/nuq-postgres`. Com o Docker em execução, faça o build e inicie o contêiner:

```
docker build -t nuq-postgres apps/nuq-postgres

docker run --name nuqdb \
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  -v nuq-data:/var/lib/postgresql/data \
  -d nuq-postgres
```

## Configurar variáveis de ambiente

Copie o modelo para criar o arquivo `.env` no diretório `apps/api/`:

```
cp apps/api/.env.example apps/api/.env
```

Para uma configuração local mínima, sem autenticação nem serviços opcionais (processamento de PDF, bloqueio de JavaScript, recursos de IA), use a seguinte configuração:

```
# ===== Obrigatório =====
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0
REDIS_URL=redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379

## Para ativar a autenticação do banco de dados, você precisa configurar o supabase.
USE_DB_AUTHENTICATION=false

## Conexão PostgreSQL para filas — altere se as credenciais, host ou banco de dados forem diferentes
NUQ_DATABASE_URL=postgres://postgres:postgres@localhost:5433/postgres

# ===== Opcional =====
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=
# TEST_API_KEY=               # Defina se você configurou autenticação e deseja testar com uma chave de API real
# OPENAI_API_KEY=             # Obrigatório para recursos dependentes de LLM (geração de texto alternativo de imagem, etc.)
# BULL_AUTH_KEY=@
# PLAYWRIGHT_MICROSERVICE_URL= # Defina para executar um fallback do Playwright
# LLAMAPARSE_API_KEY=         # Defina para processar PDFs com o LlamaParse
# SLACK_WEBHOOK_URL=          # Defina para enviar mensagens de status de saúde do servidor para o Slack
# POSTHOG_API_KEY=            # Defina para enviar eventos do PostHog como logs de tarefas
# POSTHOG_HOST=               # Defina para enviar eventos do PostHog como logs de tarefas
```

## Instalar dependências

No diretório `apps/api/`, instale os pacotes com pnpm:

## Inicie os serviços

Você precisa de três sessões de terminal rodando simultaneamente: Redis, o servidor de API e um terminal para enviar requisições.

### Terminal 1 — Redis

Inicie o servidor Redis em qualquer lugar dentro do projeto:

### Terminal 2 — servidor da API

Acesse `apps/api/` e inicie o serviço:

Isso inicia o servidor da API e os workers responsáveis por processar as tarefas de crawl.

### Terminal 3 — Enviar uma requisição de teste

Verifique se o servidor está em execução com uma verificação de integridade:

```
curl -X GET http://localhost:3002/test
```

Isso deve retornar `Hello, world!`. Para testar o endpoint de crawl:

```
curl -X POST http://localhost:3002/v1/crawl \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://mendable.ai"
  }'
```

## Alternativa: Docker Compose

Para uma configuração mais simples, o Docker Compose executa todos os serviços (Redis, servidor da API e workers) com um único comando.

1. Certifique-se de que o Docker e o Docker Compose estejam instalados.
2. Copie `.env.example` para `.env` no diretório `apps/api/` e configure conforme necessário.
3. No diretório raiz do projeto, execute:

Isso inicia automaticamente todos os serviços com a configuração correta.

## Executando testes

Execute a suíte de testes com o comando: