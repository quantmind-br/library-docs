---
title: ChatGPT での MCP Web 検索とスクレイピング - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/mcp-setup-guides/chatgpt
source: sitemap
fetched_at: 2026-03-23T07:38:10.279542-03:00
rendered_js: false
word_count: 110
summary: This document provides step-by-step instructions for integrating Firecrawl MCP with ChatGPT to enable web scraping, crawling, and search capabilities.
tags:
    - firecrawl
    - mcp
    - chatgpt
    - web-scraping
    - api-integration
    - developer-mode
category: guide
---

Firecrawl MCP を使って、ChatGPT に Web スクレイピングと検索機能を追加しましょう。

## かんたんセットアップ

### 1. APIキーを取得する

[firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) にサインアップして、APIキーをコピーします。

### 2. 開発者モードを有効にする

画面左下のユーザー名をクリックして ChatGPT の設定を開くか、[chatgpt.com/#settings](https://chatgpt.com/#settings) に直接アクセスします。 設定画面で一番下までスクロールし、**Advanced Settings** を選択します。**Developer mode** をオンに切り替えます。

### 3. コネクタを作成する

Developer mode を有効にした状態で、同じ設定モーダル内の **Apps & Connectors** タブに移動します。 右上の **Create** ボタンをクリックします。

コネクタの詳細を入力します：

- **Name:** `Firecrawl MCP`
- **Description:** `Web scraping, crawling, search, and content extraction`（任意）
- **MCP Server URL:** `https://mcp.firecrawl.dev/YOUR_API_KEY_HERE/v2/mcp`
- **Authentication:** `None`

URL 中の `YOUR_API_KEY_HERE` を、実際の [Firecrawl API key](https://www.firecrawl.dev/app/api-keys) に置き換えてください。

**“I understand and want to continue”** チェックボックスをオンにしてから、**Create** をクリックします。

### 4. セットアップを確認する

ChatGPT のメイン画面に戻ってください。**Developer mode** と表示されていれば、MCP コネクタが有効になっています。 Developer mode が表示されない場合は、ページを再読み込みしてください。それでも表示されない場合は、もう一度設定を開き、Advanced Settings で Developer mode がオンになっていることを確認してください。

会話で Firecrawl を使用するには、チャット入力欄の **+** ボタンをクリックし、**More** を選択してから **Firecrawl MCP** をクリックします。

## クイックデモ

Firecrawl MCP を選択した状態で、次のプロンプトを試してみてください: **Search:**

```
Search for the latest React Server Components updates
```

**スクレイピング：**

```
Scrape firecrawl.dev and tell me what it does
```

**ドキュメントを取得：**

```
Vercelのエッジ関数のドキュメントをスクレイピングして要約する
```

ChatGPT が Firecrawl MCP ツールを使用する際、承認を求める確認プロンプトが表示されます。

同じチャットセッション中に毎回確認が表示されないようにするには、**“Remember for this conversation”** にチェックを入れます。これは、MCP ツールが意図しないアクションを実行しないようにするために OpenAI によって実装されているセキュリティ対策です。 承認すると、ChatGPT がリクエストを実行し、結果を返します。