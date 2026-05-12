---
title: Running Locally | Firecrawl
url: https://docs.firecrawl.dev/contributing/guide
source: sitemap
fetched_at: 2026-03-23T07:31:49.945316-03:00
rendered_js: false
word_count: 311
summary: This document provides instructions for setting up and running the Firecrawl API server locally, including prerequisites, environment configuration, and service initialization.
tags:
    - firecrawl
    - local-development
    - api-setup
    - docker
    - environment-configuration
    - postgresql
    - redis
category: guide
---

This guide walks you through running the Firecrawl API server on your local machine. Follow these steps to set up the development environment, start the services, and send your first request. If you’re contributing, the process follows standard open-source conventions: fork the repo, make changes, run tests, and open a pull request. For questions or help getting started, reach out to [help@firecrawl.com](mailto:help@firecrawl.com) or [submit an issue](https://github.com/mendableai/firecrawl/issues).

## Prerequisites

Install the following before proceeding:

DependencyRequiredInstall guideNode.jsYes[nodejs.org](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)pnpm (v9+)Yes[pnpm.io](https://pnpm.io/installation)RedisYes[redis.io](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)PostgreSQLYesVia Docker (see below) or installed directlyDockerOptionalRequired for the PostgreSQL container setup

## Set up the database

You need a PostgreSQL database initialized with the schema at `apps/nuq-postgres/nuq.sql`. The easiest approach is to use the Docker image inside `apps/nuq-postgres`. With Docker running, build and start the container:

```
docker build -t nuq-postgres apps/nuq-postgres

docker run --name nuqdb \
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  -v nuq-data:/var/lib/postgresql/data \
  -d nuq-postgres
```

## Configure environment variables

Copy the template to create your `.env` file in the `apps/api/` directory:

```
cp apps/api/.env.example apps/api/.env
```

For a minimal local setup without authentication or optional sub-services (PDF parsing, JS blocking, AI features), use the following configuration:

```
# ===== Required =====
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0
REDIS_URL=redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379

## To turn on DB authentication, you need to set up supabase.
USE_DB_AUTHENTICATION=false

## PostgreSQL connection for queuing — change if credentials, host, or DB differ
NUQ_DATABASE_URL=postgres://postgres:postgres@localhost:5433/postgres

# ===== Optional =====
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=
# TEST_API_KEY=               # Set if you've configured authentication and want to test with a real API key
# OPENAI_API_KEY=             # Required for LLM-dependent features (image alt generation, etc.)
# BULL_AUTH_KEY=@
# PLAYWRIGHT_MICROSERVICE_URL= # Set to run a Playwright fallback
# LLAMAPARSE_API_KEY=         # Set to parse PDFs with LlamaParse
# SLACK_WEBHOOK_URL=          # Set to send Slack server health status messages
# POSTHOG_API_KEY=            # Set to send PostHog events like job logs
# POSTHOG_HOST=               # Set to send PostHog events like job logs
```

## Install dependencies

From the `apps/api/` directory, install packages with pnpm:

## Start the services

You need three terminal sessions running simultaneously: Redis, the API server, and a terminal for sending requests.

### Terminal 1 — Redis

Start the Redis server from anywhere in the project:

### Terminal 2 — API server

Navigate to `apps/api/` and start the service:

This starts the API server and the workers responsible for processing crawl jobs.

### Terminal 3 — Send a test request

Verify the server is running with a health check:

```
curl -X GET http://localhost:3002/test
```

This should return `Hello, world!`. To test the crawl endpoint:

```
curl -X POST http://localhost:3002/v1/crawl \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://mendable.ai"
  }'
```

## Alternative: Docker Compose

For a simpler setup, Docker Compose runs all services (Redis, API server, and workers) in a single command.

1. Make sure Docker and Docker Compose are installed.
2. Copy `.env.example` to `.env` in the `apps/api/` directory and configure as needed.
3. From the project root, run:

This starts all services automatically in the correct configuration.

## Running tests

Run the test suite with: