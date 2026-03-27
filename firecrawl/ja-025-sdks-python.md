---
title: Python SDK | Firecrawl
url: https://docs.firecrawl.dev/ja/sdks/python
source: sitemap
fetched_at: 2026-03-23T07:22:20.672128-03:00
rendered_js: false
word_count: 186
summary: This document provides a technical guide for using the Firecrawl Python SDK to scrape, crawl, and map websites, including details on asynchronous operations, status management, and pagination configurations.
tags:
    - python-sdk
    - web-scraping
    - web-crawling
    - api-integration
    - pagination
category: api
---

## インストール

Firecrawl の Python SDK をインストールするには、pip を使用します：

```
# pip install firecrawl-py

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
```

## 使い方

1. [firecrawl.dev](https://firecrawl.dev) で API キーを取得します
2. API キーを環境変数 `FIRECRAWL_API_KEY` に設定するか、`Firecrawl` クラスにパラメータとして渡します。

SDK の使用例:

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# ウェブサイトをスクレイプする：
scrape_status = firecrawl.scrape(
  'https://firecrawl.dev', 
  formats=['markdown', 'html']
)
print(scrape_status)

# ウェブサイトをクロールする：
crawl_status = firecrawl.crawl(
  'https://firecrawl.dev', 
  limit=100, 
  scrape_options={
    'formats': ['markdown', 'html']
  }
)
print(crawl_status)
```

### URLのスクレイピング

単一のURLをスクレイピングするには、`scrape` メソッドを使用します。URLをパラメータとして受け取り、スクレイピングされたドキュメントを返します。

```
# ウェブサイトをスクレイピングする:
scrape_result = firecrawl.scrape('firecrawl.dev', formats=['markdown', 'html'])
print(scrape_result)
```

### ウェブサイトをクロールする

ウェブサイトをクロールするには、`crawl` メソッドを使用します。開始URLと任意のオプションを引数に取ります。オプションでは、クロールするページ数の上限、許可するドメイン、出力フォーマットなど、クロールジョブの追加設定を指定できます。自動/手動のページネーションや制限については [Pagination](#pagination) を参照してください。

```
job = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=5, poll_interval=1, timeout=120)
print(job)
```

### サイトマップのみクロール

`sitemap="only"` を使用して、サイトマップの URL のみをクロールします（開始 URL は常に含まれ、HTML のリンク探索は行われません）。

```
job = firecrawl.crawl(url="https://docs.firecrawl.dev", sitemap="only", limit=25)
print(job.status, len(job.data))
```

### クロールを開始

`start_crawl` を使うと待たずにジョブを開始できます。ステータス確認に使えるジョブの `ID` を返します。完了までブロックして待機したい場合は `crawl` を使用してください。ページングの動作と制限は [Pagination](#pagination) を参照してください。

```
job = firecrawl.start_crawl(url="https://docs.firecrawl.dev", limit=10)
print(job)
```

### クロールのステータス確認

クロールジョブのステータスを確認するには、`get_crawl_status` メソッドを使用します。ジョブIDを引数に取り、クロールジョブの現在のステータスを返します。

```
status = firecrawl.get_crawl_status("<crawl-id>")
print(status)
```

### クロールのキャンセル

クロールジョブをキャンセルするには、`cancel_crawl` メソッドを使用します。`start_crawl` のジョブIDを引数に取り、キャンセル結果のステータスを返します。

```
ok = firecrawl.cancel_crawl("<crawl-id>")
print("キャンセル済み:", ok)
```

### ウェブサイトをマッピングする

`map` を使って、ウェブサイトから URL の一覧を生成します。オプションで、サブドメインの除外やサイトマップの利用など、マッピングの挙動をカスタマイズできます。

```
res = firecrawl.map(url="https://firecrawl.dev", limit=10)
print(res)
```

### WebSockets を使ったウェブサイトのクロール

WebSockets でウェブサイトをクロールするには、`start_crawl` でジョブを開始し、`watcher` ヘルパーで購読します。ジョブ ID を指定して watcher を作成し、`start()` を呼び出す前にハンドラー（例: page、completed、failed）を登録します。

```
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

    # 最初にクロールを開始
    started = await firecrawl.start_crawl("https://firecrawl.dev", limit=5)

    # 終了ステータスまで更新（スナップショット）を監視
    async for snapshot in firecrawl.watcher(started.id, kind="crawl", poll_interval=2, timeout=120):
        if snapshot.status == "completed":
            print("完了", snapshot.status)
            for doc in snapshot.data:
                print("DOC", doc.metadata.source_url if doc.metadata else None)
        elif snapshot.status == "failed":
            print("エラー", snapshot.status)
        else:
            print("ステータス", snapshot.status, snapshot.completed, "/", snapshot.total)

asyncio.run(main())
```

Firecrawl の /crawl および batch scrape の各エンドポイントは、追加のデータがある場合に `next` URL を返します。Python SDK はデフォルトで自動ページネーションを行い、すべてのドキュメントを集約します。この場合、`next` は `None` になります。自動ページネーションを無効化したり、ページネーションの動作を制御するための上限を設定することも可能です。

`get_crawl_status` または `get_batch_scrape_status` を呼び出す際のページネーション動作を制御するには、`PaginationConfig` を使用します。

```
from firecrawl.v2.types import PaginationConfig
```

オプション型デフォルト説明`auto_paginate``bool``True``True` の場合、すべてのページを自動的に取得して結果を集約します。1 ページずつ取得するには `False` に設定します。`max_pages``int``None`指定したページ数を取得したら終了します（`auto_paginate=True` の場合にのみ適用されます）。`max_results``int``None`指定したドキュメント数を収集したら終了します（`auto_paginate=True` の場合にのみ適用されます）。`max_wait_time``int``None`指定した秒数が経過したら終了します（`auto_paginate=True` の場合にのみ適用されます）。

`auto_paginate=False` の場合、追加のデータがあると、レスポンスに `next` URL が含まれます。次のページを取得するには、これらのヘルパーメソッドを使用します:

- **`get_crawl_status_page(next_url)`** - 前のレスポンスに含まれる不透明な `next` URL を使用して、クロール結果の次のページを取得します。
- **`get_batch_scrape_status_page(next_url)`** - 前のレスポンスに含まれる不透明な `next` URL を使用して、バッチスクレイプ結果の次のページを取得します。

これらのメソッドは、元のステータス呼び出しと同じ型のレスポンスを返し、さらにページが残っている場合は新しい `next` URL を含みます。

#### クロール

最も手軽なのはウェイター方式の `crawl` を使うことです。もしくはジョブを開始して手動でページ処理を行ってください。

- 既定のフローについては[ウェブサイトをクロールする](#crawl-a-website)を参照してください。

ジョブを開始し、`auto_paginate=False` を指定して 1 ページずつ取得します。後続のページを取得するには `get_crawl_status_page` を使用します。

```
crawl_job = client.start_crawl("https://example.com", limit=100)

# 最初のページを取得
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(auto_paginate=False)
)
print("First page:", len(status.data), "docs")

# get_crawl_status_pageを使用して後続のページを取得
while status.next:
    status = client.get_crawl_status_page(status.next)
    print("Next page:", len(status.data), "docs")
```

自動ページネーションは有効のまま、`max_pages`、`max_results`、または `max_wait_time` で早期停止します。

```
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=50, max_wait_time=15),
)
print("クロール制限:", status.status, "ドキュメント数:", len(status.data), "次のページ:", status.next)
```

#### バッチスクレイプ

waiter メソッド `batch_scrape` を使うか、ジョブを開始して手動でページングします。

- 既定のフローは [Batch Scrape](https://docs.firecrawl.dev/ja/features/batch-scrape) を参照してください。

`auto_paginate=False` を指定してジョブを開始し、1ページずつ取得します。後続のページを取得するには `get_batch_scrape_status_page` を使用します。

```
batch_job = client.start_batch_scrape(urls)

# 最初のページを取得
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(auto_paginate=False)
)
print("First page:", len(status.data), "docs")

# get_batch_scrape_status_pageを使用して後続のページを取得
while status.next:
    status = client.get_batch_scrape_status_page(status.next)
    print("Next page:", len(status.data), "docs")
```

自動ページネーションは有効にしたまま、`max_pages`、`max_results`、または `max_wait_time` で早期に停止します：

```
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=100, max_wait_time=20),
)
print("バッチ制限:", status.status, "ドキュメント数:", len(status.data), "次:", status.next)
```

## エラーハンドリング

SDK は Firecrawl API から返されるエラーを処理し、適切な例外をスローします。リクエスト中にエラーが発生した場合は、わかりやすいエラーメッセージ付きの例外がスローされます。

## 非同期クラス

非同期処理には `AsyncFirecrawl` クラスを使用します。メソッドは `Firecrawl` と同等ですが、メインスレッドをブロックしません。

```
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

    # スクレイピング
    doc = await firecrawl.scrape("https://firecrawl.dev", formats=["markdown"])  # type: ignore[arg-type]
    print(doc.get("markdown"))

    # 検索
    results = await firecrawl.search("firecrawl", limit=2)
    print(results.get("web", []))

    # クロール（開始とステータス）
    started = await firecrawl.start_crawl("https://docs.firecrawl.dev", limit=3)
    status = await firecrawl.get_crawl_status(started.id)
    print(status.status)

    # バッチスクレイピング（待機）
    job = await firecrawl.batch_scrape([
        "https://firecrawl.dev",
        "https://docs.firecrawl.dev",
    ], formats=["markdown"], poll_interval=1, timeout=60)
    print(job.status, job.completed, job.total)

asyncio.run(main())
```

## ブラウザ

クラウドブラウザセッションを起動し、リモートでコードを実行できます。

### セッションの作成

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

session = app.browser()
print(session.id)             # セッションID
print(session.cdp_url)        # wss://cdp-proxy.firecrawl.dev/cdp/...
print(session.live_view_url)  # https://liveview.firecrawl.dev/...
```

### コードの実行

```
result = app.browser_execute(
    session.id,
    code='await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
    language="python",
)
print(result.result)  # "Hacker News"
```

Python の代わりに JavaScript を実行する:

```
result = app.browser_execute(
    session.id,
    code='await page.goto("https://example.com"); const t = await page.title(); console.log(t);',
    language="node",
)
```

### プロファイル

セッション間でブラウザの状態（クッキーや localStorage など）を保存して再利用します：

```
session = app.browser(
    ttl=600,
    profile={
        "name": "my-profile",
        "save_changes": True,
    },
)
```

### CDP 経由で接続する

Playwright をフルに制御するには、CDP URL を使用して直接接続します。

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

### セッションの一覧表示とクローズ

```
# アクティブなセッションを一覧表示
sessions = app.list_browsers(status="active")
for s in sessions.sessions:
    print(s.id, s.status, s.created_at)

# セッションをクローズ
app.delete_browser(session.id)
```

> Firecrawl の API キーが必要な AI エージェントですか？ 自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。