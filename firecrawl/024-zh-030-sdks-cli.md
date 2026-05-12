---
title: CLI | Firecrawl
url: https://docs.firecrawl.dev/zh/sdks/cli
source: sitemap
fetched_at: 2026-03-23T07:20:17.101527-03:00
rendered_js: false
word_count: 341
summary: This document provides comprehensive instructions on installing, authenticating, and utilizing the Firecrawl command-line interface for web scraping, searching, and URL mapping tasks.
tags:
    - firecrawl
    - cli
    - web-scraping
    - automation
    - data-extraction
    - command-line-tools
category: guide
---

## 安装

如果你正在使用任何 AI 代理，例如 Claude Code，你可以安装下面的 Firecrawl 技能，代理将能够为你完成设置。

```
npx -y firecrawl-cli@latest init --all --browser
```

- `--all` 会将 Firecrawl 技能安装到所有检测到的 AI 编码代理中
- `--browser` 会自动打开浏览器以完成 Firecrawl 身份验证

你也可以使用 npm 手动全局安装 Firecrawl CLI：

```
# 使用 npm 全局安装
npm install -g firecrawl-cli
```

## 身份验证

在使用 CLI 之前，你需要先使用 Firecrawl API 密钥完成身份验证。

### 登录

```
# 交互式登录(打开浏览器或提示输入 API 密钥)
firecrawl login

# 使用浏览器身份验证登录(推荐用于代理)
firecrawl login --browser

# 直接使用 API 密钥登录
firecrawl login --api-key fc-YOUR-API-KEY

# 或通过环境变量设置
export FIRECRAWL_API_KEY=fc-YOUR-API-KEY
```

### 查看配置

```
# 查看当前配置和身份验证状态
firecrawl view-config
```

### 退出登录

```
# 清除已存储的凭据
firecrawl logout
```

### 自托管 / 本地开发

对于自托管的 Firecrawl 实例或本地开发，使用 `--api-url` 参数：

```
# 使用本地 Firecrawl 实例(无需 API 密钥)
firecrawl --api-url http://localhost:3002 scrape https://example.com

# Or set via environment variable
export FIRECRAWL_API_URL=http://localhost:3002
firecrawl scrape https://example.com

# Configure and persist the custom API URL
firecrawl config --api-url http://localhost:3002
```

当使用自定义 API URL（即不是 `https://api.firecrawl.dev`）时，会自动跳过 API 密钥验证，因此你在本地实例中可以在无需 API 密钥的情况下使用 Firecrawl。

### 检查状态

验证安装和身份验证，并查看速率限制：

就绪时的输出：

```
  🔥 firecrawl cli v1.1.1

  ● Authenticated via FIRECRAWL_API_KEY
  Concurrency: 0/100 jobs (parallel scrape limit)
  Credits: 500,000 remaining
```

- **并发数（Concurrency）**：最大并行任务数。并行操作应尽量接近该上限，但不要超过。
- **额度（Credits）**：剩余 API 额度。每次抓取/爬取都会消耗额度。

## 命令

### Scrape

抓取单个 URL，并以多种 formats 输出其内容。

```
# 抓取 URL(默认:markdown 输出)
firecrawl https://example.com

# 或使用显式的 scrape 命令
firecrawl scrape https://example.com

# 推荐:使用 --only-main-content 获取不含导航/页脚的干净输出
firecrawl https://example.com --only-main-content
```

#### 输出 formats 类型

```
# 获取 HTML 输出
firecrawl https://example.com --html

# 多种格式（返回 JSON）
firecrawl https://example.com --format markdown,links

# 从页面获取图片
firecrawl https://example.com --format images

# 获取页面内容摘要
firecrawl https://example.com --format summary

# 跟踪页面变化
firecrawl https://example.com --format changeTracking

# 可用格式：markdown, html, rawHtml, links, screenshot, json, images, summary, changeTracking, attributes, branding
```

#### 抓取选项

```
# 仅提取主要内容(移除导航和页脚)
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

**可用选项：**

选项简写描述`--url <url>``-u`要抓取的 URL（位置参数的替代方式）`--format <formats>``-f`输出 formats（逗号分隔）：`markdown`, `html`, `rawHtml`, `links`, `screenshot`, `json`, `images`, `summary`, `changeTracking`, `attributes`, `branding``--html``-H``--format html` 的快捷方式`--only-main-content`仅提取主要内容`--wait-for <ms>`等待 JS 渲染的时间（毫秒）`--screenshot`生成页面截图`--include-tags <tags>`要包含的 HTML 标签（逗号分隔）`--exclude-tags <tags>`要排除的 HTML 标签（逗号分隔）`--output <path>``-o`将输出保存到文件`--json`即使只有单一 format 也强制输出 JSON`--pretty`对 JSON 输出进行格式化打印`--timing`显示请求耗时和其他有用信息

* * *

### 搜索

搜索网页，并按需抓取结果。

```
# 搜索网络
firecrawl search "web scraping tutorials"

# 限制结果数量
firecrawl search "AI news" --limit 10

# 美化打印结果
firecrawl search "machine learning" --pretty
```

#### 搜索选项

```
# Search specific sources
firecrawl search "AI" --sources web,news,images

# Search with category filters
firecrawl search "react hooks" --categories github
firecrawl search "machine learning" --categories research,pdf

# Time-based filtering
firecrawl search "tech news" --tbs qdr:h   # Last hour
firecrawl search "tech news" --tbs qdr:d   # Last day
firecrawl search "tech news" --tbs qdr:w   # Last week
firecrawl search "tech news" --tbs qdr:m   # 过去一个月
firecrawl search "tech news" --tbs qdr:y   # Last year

# Location-based search
firecrawl search "restaurants" --location "Berlin,Germany" --country DE

# Search and scrape results
firecrawl search "documentation" --scrape --scrape-formats markdown

# Save to file
firecrawl search "firecrawl" --pretty -o results.json
```

**可用选项：**

选项描述`--limit <number>`结果数量上限（默认：5，最大：100）`--sources <sources>`要搜索的数据源：`web`、`images`、`news`（逗号分隔）`--categories <categories>`按类别过滤：`github`、`research`、`pdf`（逗号分隔）`--tbs <value>`时间过滤：`qdr:h`（小时）、`qdr:d`（天）、`qdr:w`（周）、`qdr:m`（月）、`qdr:y`（年）`--location <location>`地域定向（例如：“Berlin,Germany”）`--country <code>`ISO 国家代码（默认：US）`--timeout <ms>`以毫秒为单位的超时时间（默认：60000）`--ignore-invalid-urls`排除对其他 Firecrawl 端点无效的 URL`--scrape`抓取搜索结果`--scrape-formats <formats>`抓取内容的 formats（默认：markdown）`--only-main-content`抓取时仅包含主要内容（默认：true）`--json`以 JSON 格式输出`--output <path>`将输出保存到文件`--pretty`以易读格式打印 JSON 输出

* * *

### Map

快速发现站点中的所有 URL。

```
# 发现网站上的所有 URL
firecrawl map https://example.com

# Output as JSON
firecrawl map https://example.com --json

# Limit number of URLs
firecrawl map https://example.com --limit 500
```

#### Map 命令选项

```
# Filter URLs by search query
firecrawl map https://example.com --search "blog"

# Include subdomains
firecrawl map https://example.com --include-subdomains

# 控制站点地图使用方式
firecrawl map https://example.com --sitemap include   # 使用站点地图
firecrawl map https://example.com --sitemap skip      # 跳过站点地图
firecrawl map https://example.com --sitemap only      # 仅使用站点地图

# Ignore query parameters (dedupe URLs)
firecrawl map https://example.com --ignore-query-parameters

# Wait for map to complete with timeout
firecrawl map https://example.com --wait --timeout 60

# Save to file
firecrawl map https://example.com -o urls.txt
firecrawl map https://example.com --json --pretty -o urls.json
```

**可用选项：**

选项描述`--url <url>`要映射的 URL（可替代位置参数）`--limit <number>`要发现的最大 URL 数量`--search <query>`根据搜索查询筛选 URL`--sitemap <mode>`Sitemap 处理模式：`include`、`skip`、`only``--include-subdomains`包含子域名`--ignore-query-parameters`将带有不同参数的 URL 视为同一 URL`--wait`等待映射完成`--timeout <seconds>`超时时间（秒）`--json`以 JSON 格式输出`--output <path>`将输出保存到文件`--pretty`以易读格式打印 JSON 输出

* * *

### 浏览器

让您的代理通过安全的浏览器沙箱与网页交互。 启动云端浏览器会话，远程执行 Python、JavaScript 或 bash 代码。每个会话都会运行一个完整的 Chromium 实例——无需在本地安装浏览器。代码在服务器端运行，并预先配置好可直接使用的 [Playwright](https://playwright.dev/) `page` 对象。

```
# Launch a cloud browser session
firecrawl browser launch-session

# 执行 agent-browser 命令(默认 - 自动添加 "agent-browser" 前缀)
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

#### 浏览器选项

```
# Launch with custom TTL (10 minutes) and live view
firecrawl browser launch-session --ttl 600 --stream

# Launch with inactivity timeout
firecrawl browser launch-session --ttl 120 --ttl-inactivity 60

# agent-browser 命令(默认 - 自动添加 "agent-browser" 前缀)
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

**子命令：**

子命令说明`launch-session`启动一个新的云端浏览器会话（返回会话 ID、CDP URL 和实时视图 URL）`execute <code>`在会话中执行 Playwright Python/JS 代码或 bash 命令`list [status]`列出浏览器会话（可按 `active` 或 `destroyed` 过滤）`close`关闭浏览器会话

**执行选项：**

选项说明`--bash`在沙箱中远程执行 bash 命令（默认）。已预装 [agent-browser](https://github.com/vercel-labs/agent-browser)（40+ 命令）并自动加前缀。`CDP_URL` 会自动注入，因此 agent-browser 会自动连接到你的会话。是 AI 代理的最佳使用方式。`--python`以 Playwright Python 代码方式执行。会提供一个 Playwright `page` 对象——使用 `await page.goto()`、`await page.title()` 等。`--node`以 Playwright JavaScript 代码方式执行。同样提供 `page` 对象。`--session <id>`指定目标会话（默认：活动会话）

**启动选项：**

选项说明`--ttl <seconds>`会话总存活时间（TTL）（默认：600，范围：30–3600）`--ttl-inactivity <seconds>`空闲达到指定时间后自动关闭（范围：10–3600）`--profile <name>`配置文件名称（在会话之间保存并复用浏览器状态）`--no-save-changes`仅加载已有配置文件数据，不将更改写回保存`--stream`启用实时视图流式传输

**通用选项：**

选项说明`--output <path>`将输出保存到文件`--json`以 JSON 格式输出

* * *

### Crawl

从单个 URL 出发爬取整个网站。

```
# Start a crawl (returns job ID immediately)
firecrawl crawl https://example.com

# Wait for crawl to complete
firecrawl crawl https://example.com --wait

# 等待并显示进度指示器
firecrawl crawl https://example.com --wait --progress
```

#### 查看抓取状态

```
# 使用作业 ID 检查爬取状态
firecrawl crawl <job-id>

# 真实作业 ID 示例
firecrawl crawl 550e8400-e29b-41d4-a716-446655440000
```

#### Crawl 选项

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

# 自定义轮询间隔和超时时间
firecrawl crawl https://example.com --wait --poll-interval 10 --timeout 300

# Save results to file
firecrawl crawl https://example.com --wait --pretty -o results.json
```

**可用选项：**

选项描述`--url <url>`要爬取的 URL（位置参数的替代方式）`--wait`等待爬取完成`--progress`等待期间显示进度指示器`--poll-interval <seconds>`轮询间隔（默认：5 秒）`--timeout <seconds>`等待时的超时时长`--status`检查已有爬取任务的状态`--limit <number>`最大爬取页面数`--max-depth <number>`最大爬取深度`--include-paths <paths>`要包含的路径（逗号分隔）`--exclude-paths <paths>`要排除的路径（逗号分隔）`--sitemap <mode>`Sitemap 处理方式：`include`、`skip`、`only``--allow-subdomains`包含子域名`--allow-external-links`跟随外部链接`--crawl-entire-domain`爬取整个域名`--ignore-query-parameters`将具有不同参数的 URL 视为相同`--delay <ms>`请求之间的延迟`--max-concurrency <n>`最大并发请求数`--output <path>`将输出保存到文件`--pretty`以更易读的格式输出 JSON

* * *

### Agent

使用自然语言指令在网上搜索和获取数据。

```
# Basic usage - URLs are optional
firecrawl agent "Find the top 5 AI startups and their funding amounts" --wait

# Focus on specific URLs
firecrawl agent "Compare pricing plans" --urls https://slack.com/pricing,https://teams.microsoft.com/pricing --wait

# 使用 schema 实现结构化输出
firecrawl agent "Get company information" --urls https://example.com --schema '{"name": "string", "founded": "number"}' --wait

# Use schema from a file
firecrawl agent "Get product details" --urls https://example.com --schema-file schema.json --wait
```

#### Agent 选项

```
# 使用 Spark 1 Pro 提高准确性
firecrawl agent "Competitive analysis across multiple domains" --model spark-1-pro --wait

# Set max credits to limit costs
firecrawl agent "Gather contact information from company websites" --max-credits 100 --wait

# Check status of an existing job
firecrawl agent <job-id> --status

# Custom polling interval and timeout
firecrawl agent "Summarize recent blog posts" --wait --poll-interval 10 --timeout 300

# Save output to file
firecrawl agent "Find pricing information" --urls https://example.com --wait -o pricing.json --pretty
```

**可用选项：**

选项说明`--urls <urls>`可选的 URL 列表，用于限定 agent 的处理范围（用逗号分隔）`--model <model>`使用的模型：`spark-1-mini`（默认，成本低 60%）或 `spark-1-pro`（精度更高）`--schema <json>`用于结构化输出的 JSON schema（内联 JSON 字符串）`--schema-file <path>`用于结构化输出的 JSON schema 文件路径`--max-credits <number>`最多可消耗的 credits（达到上限时任务失败）`--status`检查已有 agent 任务的状态`--wait`等待 agent 任务完成后再返回结果`--poll-interval <seconds>`等待时的轮询间隔（默认：5）`--timeout <seconds>`等待时的超时时间（默认：无限制）`--output <path>`将输出保存到文件`--json`以 JSON 格式输出

* * *

### 额度使用情况

查看你团队的额度余额和使用明细。

```
# View credit usage
firecrawl credit-usage

# 以 JSON 格式输出
firecrawl credit-usage --json --pretty
```

* * *

### Version

显示 CLI 的版本。

```
firecrawl version
# 或
firecrawl --version
```

## 全局选项

以下选项适用于所有命令：

选项简写说明`--status`显示版本、认证状态、并发数和额度`--api-key <key>``-k`在此命令中临时覆盖已保存的 API 密钥`--api-url <url>`使用自定义 API URL（用于自托管/本地开发）`--help``-h`显示命令帮助信息`--version``-V`显示 CLI 版本

## 输出处理

CLI 默认将结果输出到 stdout，便于通过管道或重定向进行处理：

```
# 将 Markdown 通过管道传递给另一个命令
firecrawl https://example.com | head -50

# 重定向到文件
firecrawl https://example.com > output.md

# 保存格式化后的 JSON
firecrawl https://example.com --format markdown,links --pretty -o data.json
```

### formats 的行为

- **单一 format**：输出原始内容（markdown 文本、HTML 等）
- **多个 formats**：输出包含所有请求数据的 JSON

```
# 原始 markdown 输出
firecrawl https://example.com --format markdown

# 使用多个 formats 的 JSON 输出
firecrawl https://example.com --format markdown,links
```

## 示例

### 快速抓取

```
# 从 URL 获取 Markdown 内容(使用 --only-main-content 获取简洁输出)
firecrawl https://docs.firecrawl.dev --only-main-content

# Get HTML content
firecrawl https://example.com --html -o page.html
```

### 整站爬取

```
# 爬取文档站点并设置限制
firecrawl crawl https://docs.example.com --limit 50 --max-depth 2 --wait --progress -o docs.json
```

### 站点发现

```
# 查找所有博客文章
firecrawl map https://example.com --search "blog" -o blog-urls.txt
```

### 研究工作流

```
# 搜索并抓取结果用于研究
firecrawl search "machine learning best practices 2024" --scrape --scrape-formats markdown --pretty
```

### 智能体

```
# URL 可选
firecrawl agent "Find the top 5 AI startups and their funding amounts" --wait

# 针对特定 URL
firecrawl agent "Compare pricing plans" --urls https://slack.com/pricing,https://teams.microsoft.com/pricing --wait
```

### 浏览器自动化

```
# Launch a session, scrape a page, and close
firecrawl browser launch-session
firecrawl browser execute "open https://news.ycombinator.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "scrape"
firecrawl browser close

# 通过 bash 模式使用 agent-browser(默认 — 推荐用于 AI 智能体)
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

# Extract URLs from search results
jq -r '.data.web[].url' search-results.json

# Get titles from search results
jq -r '.data.web[] | "\(.title): \(.url)"' search-results.json

# 提取链接并使用 jq 处理
firecrawl https://example.com --format links | jq '.links[].url'

# Count URLs from map
firecrawl map https://example.com | wc -l
```

## 遥测

CLI 在身份验证过程中会收集匿名使用数据，以帮助改进产品：

- CLI 版本、操作系统和 Node.js 版本
- 检测到的开发工具（例如 Cursor、VS Code、Claude Code）

**CLI 不会收集任何命令数据、URL 或文件内容。** 如需禁用遥测，请设置以下环境变量：

```
export FIRECRAWL_NO_TELEMETRY=1
```

## 开源

Firecrawl CLI 和技能是开源的，可在 GitHub 上获取：[firecrawl/cli](https://github.com/firecrawl/cli)

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化入门说明。