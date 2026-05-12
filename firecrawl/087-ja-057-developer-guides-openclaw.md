---
title: Firecrawl と OpenClaw の利用方法
url: https://docs.firecrawl.dev/ja/developer-guides/openclaw
source: sitemap
fetched_at: 2026-03-23T07:31:12.855107-03:00
rendered_js: false
word_count: 98
summary: This document explains how to integrate Firecrawl CLI with OpenClaw agents to perform remote web scraping, search, and browser automation within secure sandboxed environments.
tags:
    - firecrawl
    - cli
    - web-scraping
    - browser-automation
    - ai-agents
    - sandbox
category: guide
---

Firecrawl を OpenClaw と統合し、エージェントにスクレイピング、検索、クロール、抽出、そして Web との対話を行う機能を、すべて [Firecrawl CLI](https://docs.firecrawl.dev/ja/sdks/cli) 経由で利用できるようにします。

- **ローカルブラウザは不要** — すべてのセッションはリモートの分離されたサンドボックス上で実行されます。Chromium のインストールも、ドライバーの競合も、マシン上のメモリ負荷もありません。
- **真の並列処理** — 多数のブラウザセッションを同時に実行してもローカルリソースの取り合いがありません。エージェントは複数サイトをまたいでバッチでブラウズできます。
- **標準でセキュア** — ナビゲーション、DOM の評価、抽出はすべて使い捨てサンドボックス内で行われ、あなたのワークステーション上では実行されません。
- **より良いトークン効率** — エージェントは巨大な DOM やドライバーログをコンテキストウィンドウに持ち込むのではなく、クリーンな成果物 (スナップショットや抽出済みフィールド) だけを受け取ります。
- **Web 向けのフル機能ツールキット** — スクレイピング、検索、ブラウザ自動化を、エージェントがすでに使い方を理解している単一の CLI から実行できます。

## セットアップ

エージェントに対して、Firecrawl CLI のインストール、認証、およびスキルの初期化を次のコマンドで実行するよう指示してください。

```
npx -y firecrawl-cli init --browser --all
```

- `--all` は検出されたすべての AI コーディングエージェントに Firecrawl スキルをインストールします
- `--browser` は Firecrawl 認証のためにブラウザを自動的に開きます

または、すべてを個別にインストールすることもできます：

```
npm install -g firecrawl-cli
firecrawl init skills
firecrawl login --browser
# または、ブラウザを使わずAPIキーを直接指定する:
export FIRECRAWL_API_KEY="fc-YOUR-API-KEY"
```

すべてが正しく設定されているか確認します：

## スクレイプ

単一のページをスクレイピングし、その内容を抽出します：

```
firecrawl https://example.com --only-main-content
```

特定のフォーマットを取得する：

```
firecrawl https://example.com --format markdown,links --pretty
```

## 検索

ウェブを検索し、必要に応じて結果をスクレイピングできます。

```
firecrawl search "latest AI funding rounds 2025" --limit 10

# 検索結果をスクレイプする
firecrawl search "OpenClaw documentation" --scrape --scrape-formats markdown
```

## ブラウザ

インタラクティブな自動化のためにリモートブラウザーセッションを開始します。各セッションは分離されたサンドボックス環境で実行されるため、ローカル環境に Chromium をインストールする必要はありません。`agent-browser` には 40 以上のコマンドがあらかじめインストールされています。

```
# 短縮形: アクティブなセッションがない場合、自動的にセッションを起動
firecrawl browser "open https://news.ycombinator.com"
firecrawl browser "snapshot"
firecrawl browser "scrape"
firecrawl browser close
```

スナップショットから取得した ref を使ってページ要素を操作します:

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
# snapshot は @ref ID を返します — それらを使って操作します
firecrawl browser "click @e5"
firecrawl browser "fill @e3 'search query'"
firecrawl browser "scrape"
firecrawl browser close
```

## 例: エージェントへの指示

OpenClaw エージェントに対して、次のようなプロンプトを指示できます:

- *「Firecrawl を使って [https://example.com](https://example.com) をスクレイピングし、主要なコンテンツを要約してください。」*
- *「最新の OpenAI ニュースを検索して、上位 5 件の結果を要約して教えてください。」*
- *「Firecrawl Browser を使って Hacker News を開き、トップ 5 件の記事と、それぞれの最初の 10 件のコメントを取得してください。」*
- *「[https://docs.firecrawl.dev](https://docs.firecrawl.dev) のドキュメントをクロールして、ファイルに保存してください。」*

## さらに詳しく読む

- [Firecrawl CLI リファレンス](https://docs.firecrawl.dev/ja/sdks/cli)
- [Browser Sandbox ドキュメント](https://docs.firecrawl.dev/ja/features/browser)
- [エージェント ドキュメント](https://docs.firecrawl.dev/ja/features/agent)