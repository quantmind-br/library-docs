---
title: Python SDK | Firecrawl
url: https://docs.firecrawl.dev/zh/sdks/python
source: sitemap
fetched_at: 2026-03-23T07:20:07.661878-03:00
rendered_js: false
word_count: 221
summary: This document provides a comprehensive guide on installing and using the Firecrawl Python SDK to scrape, crawl, and map websites. It covers key features such as asynchronous operations, pagination control, and error handling for interacting with the Firecrawl API.
tags:
    - python-sdk
    - web-scraping
    - web-crawling
    - api-integration
    - pagination
category: guide
---

## 安装

要安装 Firecrawl 的 Python SDK，可以使用 pip：

```
# 使用 pip 安装 firecrawl-py

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
```

## 使用

1. 在 [firecrawl.dev](https://firecrawl.dev) 获取 API key
2. 将该 API key 设置为名为 `FIRECRAWL_API_KEY` 的环境变量，或在实例化 `Firecrawl` 类时作为参数传入。

以下是使用 SDK 的示例：

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# 抓取网站：
scrape_status = firecrawl.scrape(
  'https://firecrawl.dev', 
  formats=['markdown', 'html']
)
print(scrape_status)

# 爬取网站：
crawl_status = firecrawl.crawl(
  'https://firecrawl.dev', 
  limit=100, 
  scrape_options={
    'formats': ['markdown', 'html']
  }
)
print(crawl_status)
```

### 抓取单个 URL

要抓取单个 URL，请使用 `scrape` 方法。它将该 URL 作为参数并返回抓取到的文档。

```
# 抓取网站：
scrape_result = firecrawl.scrape('firecrawl.dev', formats=['markdown', 'html'])
print(scrape_result)
```

### 爬取网站

要爬取网站，请使用 `crawl` 方法。它接收起始 URL 和可选的 options 作为参数。通过 options，你可以为爬取任务指定其他设置，例如爬取的最大页面数、允许的域名，以及输出 formats。有关自动/手动分页与限制，请参见 [Pagination](#pagination)。

```
job = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=5, poll_interval=1, timeout=120)
print(job)
```

### 仅站点地图抓取

使用 `sitemap="only"` 只抓取站点地图中的 URL（起始 URL 始终会被包含，并且不会进行 HTML 链接发现）。

```
job = firecrawl.crawl(url="https://docs.firecrawl.dev", sitemap="only", limit=25)
print(job.status, len(job.data))
```

### 开始 Crawl

使用 `start_crawl` 启动任务，无需等待。它会返回一个用于检查状态的任务 `ID`。需要直到完成才返回的阻塞式等待器时，请使用 `crawl`。分页行为与限制见[分页](#pagination)。

```
job = firecrawl.start_crawl(url="https://docs.firecrawl.dev", limit=10)
print(job)
```

### 检查爬取状态

要查看爬取任务的状态，请使用 `get_crawl_status` 方法。该方法接收任务 ID 作为参数，并返回该爬取任务的当前状态。

```
status = firecrawl.get_crawl_status("<crawl-id>")
print(status)
```

### 取消爬取

要取消一个爬取任务，使用 `cancel_crawl` 方法。传入由 `start_crawl` 返回的任务 ID 作为参数，该方法会返回取消结果。

```
ok = firecrawl.cancel_crawl("<crawl-id>")
print("已取消：", ok)
```

### 网站映射

使用 `map` 生成网站的 URL 列表。你可以通过选项自定义映射过程，例如排除子域或利用 sitemap。

```
res = firecrawl.map(url="https://firecrawl.dev", limit=10)
print(res)
```

### 使用 WebSockets 爬取网站

要通过 WebSockets 爬取网站，先用 `start_crawl` 启动任务，并使用 `watcher` 辅助工具订阅。调用 `start()` 之前，使用任务 ID 创建一个 watcher，并附加处理器（例如：page、completed、failed）。

```
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

    # 首先启动爬取
    started = await firecrawl.start_crawl("https://firecrawl.dev", limit=5)

    # 监听更新（快照）直到终止状态
    async for snapshot in firecrawl.watcher(started.id, kind="crawl", poll_interval=2, timeout=120):
        if snapshot.status == "completed":
            print("完成", snapshot.status)
            for doc in snapshot.data:
                print("文档", doc.metadata.source_url if doc.metadata else None)
        elif snapshot.status == "failed":
            print("错误", snapshot.status)
        else:
            print("状态", snapshot.status, snapshot.completed, "/", snapshot.total)

asyncio.run(main())
```

当有更多数据可用时，Firecrawl 的 crawl 和 batch scrape 端点会返回一个 `next` URL。Python SDK 默认会自动分页并汇总所有文档；此时 `next` 为 `None`。你可以禁用自动分页或设置限制来控制分页行为。

在调用 `get_crawl_status` 或 `get_batch_scrape_status` 时，使用 `PaginationConfig` 来控制分页行为：

```
from firecrawl.v2.types import PaginationConfig
```

OptionTypeDefaultDescription`auto_paginate``bool``True`当为 `True` 时，会自动获取所有页面并聚合结果。将其设为 `False` 以每次仅获取一页。`max_pages``int``None`在获取到指定页数后停止（仅在 `auto_paginate=True` 时生效）。`max_results``int``None`在收集到指定数量的文档后停止（仅在 `auto_paginate=True` 时生效）。`max_wait_time``int``None`在经过指定秒数后停止（仅在 `auto_paginate=True` 时生效）。

当 `auto_paginate=False` 时，如果还有更多数据可用，响应中会包含一个 `next` URL。使用以下辅助方法来获取后续页面：

- **`get_crawl_status_page(next_url)`** - 使用前一次响应中的不透明 `next` URL 获取爬取结果的下一页。
- **`get_batch_scrape_status_page(next_url)`** - 使用前一次响应中的不透明 `next` URL 获取批量抓取结果的下一页。

这些方法返回的响应类型与最初的状态查询调用相同，如果还有更多页面，将包含新的 `next` URL。

#### 爬取

使用 waiter 方法 `crawl` 可获得最简便的体验，或者启动一个作业并手动翻页。

- 参见[抓取网站](#crawl-a-website)中的默认流程。

先启动一个任务，然后将 `auto_paginate` 设为 `False`，一次获取一页。使用 `get_crawl_status_page` 获取后续页面：

```
crawl_job = client.start_crawl("https://example.com", limit=100)

# 获取第一页
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(auto_paginate=False)
)
print("First page:", len(status.data), "docs")

# 使用 get_crawl_status_page 获取后续页面
while status.next:
    status = client.get_crawl_status_page(status.next)
    print("Next page:", len(status.data), "docs")
```

保持自动分页开启，但可通过 `max_pages`、`max_results` 或 `max_wait_time` 提前停止：

```
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=50, max_wait_time=15),
)
print("爬取受限：", status.status, "文档数：", len(status.data), "下一页：", status.next)
```

#### 批量抓取

使用 waiter 方法 `batch_scrape`，或启动任务后手动分页处理。

- 参见默认流程：[Batch Scrape](https://docs.firecrawl.dev/zh/features/batch-scrape)。

先启动一个任务，然后将 `auto_paginate=False`，每次只获取一页。使用 `get_batch_scrape_status_page` 获取后续页面：

```
batch_job = client.start_batch_scrape(urls)

# 获取第一页
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(auto_paginate=False)
)
print("第一页:", len(status.data), "文档")

# 使用 get_batch_scrape_status_page 获取后续页面
while status.next:
    status = client.get_batch_scrape_status_page(status.next)
    print("下一页:", len(status.data), "文档")
```

保持自动分页开启，但可通过 `max_pages`、`max_results` 或 `max_wait_time` 提前停止：

```
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=100, max_wait_time=20),
)
print("批处理受限：", status.status, "文档数：", len(status.data), "下一页：", status.next)
```

## 错误处理

SDK 会处理 Firecrawl API 返回的错误并抛出相应异常。如果在请求过程中发生错误，将抛出包含详细错误信息的异常。

## 异步类

进行异步操作时，请使用 `AsyncFirecrawl` 类。其方法与 `Firecrawl` 一致，但不会阻塞主线程。

```
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

    # 抓取
    doc = await firecrawl.scrape("https://firecrawl.dev", formats=["markdown"])  # type: ignore[arg-type]
    print(doc.get("markdown"))

    # 搜索
    results = await firecrawl.search("firecrawl", limit=2)
    print(results.get("web", []))

    # 爬取（启动与状态）
    started = await firecrawl.start_crawl("https://docs.firecrawl.dev", limit=3)
    status = await firecrawl.get_crawl_status(started.id)
    print(status.status)

    # 批量抓取（等待完成）
    job = await firecrawl.batch_scrape([
        "https://firecrawl.dev",
        "https://docs.firecrawl.dev",
    ], formats=["markdown"], poll_interval=1, timeout=60)
    print(job.status, job.completed, job.total)

asyncio.run(main())
```

## 浏览器

启动云浏览器会话并远程执行代码。

### 创建会话

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

session = app.browser()
print(session.id)             # 会话 ID
print(session.cdp_url)        # wss://cdp-proxy.firecrawl.dev/cdp/...
print(session.live_view_url)  # https://liveview.firecrawl.dev/...
```

### 运行代码

```
result = app.browser_execute(
    session.id,
    code='await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
    language="python",
)
print(result.result)  # "Hacker News"
```

改用 JavaScript，而不是 Python：

```
result = app.browser_execute(
    session.id,
    code='await page.goto("https://example.com"); const t = await page.title(); console.log(t);',
    language="node",
)
```

### 配置文件

跨会话保存并复用浏览器状态（cookies、localStorage 等）：

```
session = app.browser(
    ttl=600,
    profile={
        "name": "my-profile",
        "save_changes": True,
    },
)
```

### 通过 CDP 连接

要获得对 Playwright 的完全控制，请使用 CDP URL 直接连接：

```
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(session.cdp_url)
    context = browser.contexts[0]
    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://example.com")
    print(page.title())

    browser.close()
```

### 查看和关闭会话

```
# 列出活跃会话
sessions = app.list_browsers(status="active")
for s in sessions.sessions:
    print(s.id, s.status, s.created_at)

# 关闭会话
app.delete_browser(session.id)
```

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化入门说明。