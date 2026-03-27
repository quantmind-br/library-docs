---
title: 本地运行 | Firecrawl
url: https://docs.firecrawl.dev/zh/contributing/guide
source: sitemap
fetched_at: 2026-03-23T07:31:45.200513-03:00
rendered_js: false
word_count: 105
summary: 本指南提供了在本地开发环境中设置、配置并运行 Firecrawl API 服务器的完整步骤，涵盖了依赖安装、数据库初始化及服务启动方法。
tags:
    - firecrawl
    - local-development
    - api-setup
    - docker-compose
    - web-scraping
    - environment-configuration
category: guide
---

本指南将引导你在本地机器上运行 Firecrawl API 服务器。请按照以下步骤完成开发环境的设置、启动相关服务，并发送你的第一个请求。 如果你要参与贡献，流程遵循标准的开源规范：fork 仓库、进行修改、运行测试并提交 pull request。如有问题或需要入门帮助，请联系 [help@firecrawl.com](mailto:help@firecrawl.com) 或 [提交 issue](https://github.com/mendableai/firecrawl/issues)。

## 前置条件

继续之前，请先安装以下组件：

依赖是否必需安装指南Node.js是[nodejs.org](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)pnpm (v9+)是[pnpm.io](https://pnpm.io/installation)Redis是[redis.io](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)PostgreSQL是通过 Docker（见下文）或直接安装Docker可选用于创建 PostgreSQL 容器

## 设置数据库

你需要一个使用 `apps/nuq-postgres/nuq.sql` 中的 schema 初始化好的 PostgreSQL 数据库。最简单的方法是使用 `apps/nuq-postgres` 目录下的 Docker 镜像。 在 Docker 已启动的情况下，构建并启动该容器：

```
docker build -t nuq-postgres apps/nuq-postgres

docker run --name nuqdb \
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  -v nuq-data:/var/lib/postgresql/data \
  -d nuq-postgres
```

## 配置环境变量

复制模板，在 `apps/api/` 目录下创建 `.env` 文件：

```
cp apps/api/.env.example apps/api/.env
```

对于本地最小化部署且不启用身份验证或可选附加服务（PDF 解析、JS 阻塞、AI 功能）的情况，请使用以下配置：

```
# ===== 必填 =====
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0
REDIS_URL=redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379

## 要启用数据库身份验证，需要配置 supabase。
USE_DB_AUTHENTICATION=false

## 用于队列的 PostgreSQL 连接 — 如凭据、主机或数据库不同请修改
NUQ_DATABASE_URL=postgres://postgres:postgres@localhost:5433/postgres

# ===== 可选 =====
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=
# TEST_API_KEY=               # 如已配置身份验证并希望使用真实 API 密钥进行测试，请设置此项
# OPENAI_API_KEY=             # LLM 相关功能（图片 alt 生成等）必填
# BULL_AUTH_KEY=@
# PLAYWRIGHT_MICROSERVICE_URL= # 设置以启用 Playwright 回退
# LLAMAPARSE_API_KEY=         # 设置以使用 LlamaParse 解析 PDF
# SLACK_WEBHOOK_URL=          # 设置以发送 Slack 服务器健康状态消息
# POSTHOG_API_KEY=            # 设置以发送 PostHog 事件（如任务日志）
# POSTHOG_HOST=               # 设置以发送 PostHog 事件（如任务日志）
```

## 安装依赖项

在 `apps/api/` 目录下使用 pnpm 安装依赖包：

## 启动服务

你需要同时开启三个终端会话：一个运行 Redis、一个运行 API 服务器，另一个用于发送请求。

### 终端 1 — Redis

在项目中的任意目录启动 Redis 服务器：

### Terminal 2 — API 服务器

进入 `apps/api/` 目录并启动服务：

这将启动 API 服务器以及负责处理抓取任务的工作进程。

### 终端 3 — 发送测试请求

运行健康检查以验证服务器是否正常运行：

```
curl -X GET http://localhost:3002/test
```

这应该返回 `Hello, world!`。 要测试 crawl 端点：

```
curl -X POST http://localhost:3002/v1/crawl \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://mendable.ai"
  }'
```

## 替代方案：Docker Compose

为了更简单的搭建方式，Docker Compose 可以通过一条命令运行所有服务（Redis、API 服务器和工作进程）。

1. 确保已安装 Docker 和 Docker Compose。
2. 在 `apps/api/` 目录下将 `.env.example` 复制为 `.env`，并根据需要进行配置。
3. 在项目根目录运行：

这将自动以正确的配置启动所有服务。

## 运行测试

使用以下命令运行测试套件：