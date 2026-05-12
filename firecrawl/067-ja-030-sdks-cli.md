---
title: CLI | Firecrawl
url: https://docs.firecrawl.dev/ja/sdks/cli
source: sitemap
fetched_at: 2026-03-23T07:22:36.190825-03:00
rendered_js: false
word_count: 318
summary: This document provides a comprehensive guide for installing, authenticating, and using the Firecrawl CLI to perform web scraping and search operations.
tags:
    - firecrawl
    - cli
    - web-scraping
    - authentication
    - api-tools
    - data-extraction
category: guide
---

## インストール

Claude Code のような AI エージェントを使用している場合は、以下の Firecrawl Skill をインストールすると、エージェントがセットアップしてくれます。

```
npx -y firecrawl-cli@latest init --all --browser
```

- `--all` は検出されたすべての AI コーディングエージェントに Firecrawl Skill をインストールします
- `--browser` は Firecrawl の認証のためにブラウザを自動的に開きます

npm を使って Firecrawl CLI をグローバルに手動でインストールすることもできます。

```
# npm でグローバルにインストール
npm install -g firecrawl-cli
```

## 認証

CLI を使用する前に、Firecrawl API キーを使って認証する必要があります。

### ログイン

```
# 対話型ログイン(ブラウザを開くか、APIキーの入力を求めます)
firecrawl login

# Login with browser authentication (recommended for agents)
firecrawl login --browser

# Login with API key directly
firecrawl login --api-key fc-YOUR-API-KEY

# Or set via environment variable
export FIRECRAWL_API_KEY=fc-YOUR-API-KEY
```

### 設定の表示

```
# 現在の設定と認証ステータスを表示
firecrawl view-config
```

### ログアウト

```
# 保存された認証情報をクリア
firecrawl logout
```

### セルフホスト / ローカル開発

セルフホスト環境の Firecrawl インスタンスやローカル開発では、`--api-url` オプションを使用してください:

```
# ローカルのFirecrawlインスタンスを使用(APIキー不要)
firecrawl --api-url http://localhost:3002 scrape https://example.com

# Or set via environment variable
export FIRECRAWL_API_URL=http://localhost:3002
firecrawl scrape https://example.com

# Configure and persist the custom API URL
firecrawl config --api-url http://localhost:3002
```

カスタム API URL（`https://api.firecrawl.dev` 以外のもの）を使用している場合、API キー認証は自動的にスキップされるため、ローカルインスタンスでは API キーなしで利用できます。

### ステータスの確認

インストールと認証が正しく行われているかを確認し、レート制限も確認します。

準備完了時の出力:

```
  🔥 firecrawl cli v1.1.1

  ● FIRECRAWL_API_KEYで認証済み
  同時実行数: 0/100ジョブ (並列スクレイプ制限)
  クレジット: 残り500,000
```

- **同時実行数 (Concurrency)**: 並列に実行できるジョブの最大数。この上限付近まで並列処理を行ってもよいが、超えないようにする。
- **クレジット (Credits)**: 残りの API クレジット数。各 `scrape`/`crawl` はクレジットを消費する。

## コマンド

### Scrape

1つのURLをスクレイピングし、そのコンテンツをさまざまなフォーマットで抽出します。

```
# Scrape a URL (default: markdown output)
firecrawl https://example.com

# Or use the explicit scrape command
firecrawl scrape https://example.com

# 推奨: ナビゲーションやフッターを除いたクリーンな出力には --only-main-content を使用
firecrawl https://example.com --only-main-content
```

#### 出力フォーマット

```
# Get HTML output
firecrawl https://example.com --html

# Multiple formats (returns JSON)
firecrawl https://example.com --format markdown,links

# Get images from a page
firecrawl https://example.com --format images

# Get a summary of the page content
firecrawl https://example.com --format summary

# Track changes on a page
firecrawl https://example.com --format changeTracking

# 利用可能なフォーマット: markdown, html, rawHtml, links, screenshot, json, images, summary, changeTracking, attributes, branding
```

#### スクレイプのオプション

```
# メインコンテンツのみを抽出(ナビゲーションとフッターを削除)
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

**利用可能なオプション:**

OptionShortDescription`--url <url>``-u`スクレイプする URL（位置引数の代わり）`--format <formats>``-f`出力フォーマット（カンマ区切り）：`markdown`, `html`, `rawHtml`, `links`, `screenshot`, `json`, `images`, `summary`, `changeTracking`, `attributes`, `branding``--html``-H``--format html` のショートカット`--only-main-content`メインのコンテンツのみを抽出`--wait-for <ms>`JS のレンダリングを待機する時間（ミリ秒）`--screenshot`スクリーンショットを撮影`--include-tags <tags>`含める HTML タグ（カンマ区切り）`--exclude-tags <tags>`除外する HTML タグ（カンマ区切り）`--output <path>``-o`出力をファイルに保存`--json`単一のフォーマット指定でも JSON 出力を強制`--pretty`JSON 出力を整形して表示`--timing`リクエストのタイミングやその他の有用な情報を表示

* * *

### Search

ウェブ検索を行い、必要に応じて結果をスクレイピングします。

```
# ウェブを検索する
firecrawl search "web scraping tutorials"

# 結果数を制限する
firecrawl search "AI news" --limit 10

# 結果を整形して表示する
firecrawl search "machine learning" --pretty
```

#### 検索オプション

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
firecrawl search "tech news" --tbs qdr:m   # 過去1ヶ月
firecrawl search "tech news" --tbs qdr:y   # Last year

# Location-based search
firecrawl search "restaurants" --location "Berlin,Germany" --country DE

# Search and scrape results
firecrawl search "documentation" --scrape --scrape-formats markdown

# Save to file
firecrawl search "firecrawl" --pretty -o results.json
```

**利用可能なオプション:**

オプション説明`--limit <number>`最大結果数（デフォルト: 5、最大: 100）`--sources <sources>`検索対象のソース: `web`、`images`、`news`（カンマ区切り）`--categories <categories>`カテゴリでフィルタリング: `github`、`research`、`pdf`（カンマ区切り）`--tbs <value>`時間フィルタ: `qdr:h`（時間）、`qdr:d`（日）、`qdr:w`（週）、`qdr:m`（月）、`qdr:y`（年）`--location <location>`ジオターゲティング（例: “Berlin,Germany”）`--country <code>`ISO 国コード（デフォルト: US）`--timeout <ms>`タイムアウト（ミリ秒単位、デフォルト: 60000）`--ignore-invalid-urls`他の Firecrawl エンドポイントで利用できない URL を除外`--scrape`検索結果をスクレイピング`--scrape-formats <formats>`スクレイピングしたコンテンツのフォーマット（デフォルト: markdown）`--only-main-content`スクレイピング時にメインコンテンツのみを含める（デフォルト: true）`--json`JSON として出力`--output <path>`出力をファイルに保存`--pretty`JSON 出力を見やすく整形して表示

* * *

### Map

ウェブサイト内のすべてのURLを迅速に検出します。

```
# ウェブサイト上のすべてのURLを検出
firecrawl map https://example.com

# Output as JSON
firecrawl map https://example.com --json

# Limit number of URLs
firecrawl map https://example.com --limit 500
```

#### Map オプション

```
# Filter URLs by search query
firecrawl map https://example.com --search "blog"

# Include subdomains
firecrawl map https://example.com --include-subdomains

# Control sitemap usage
firecrawl map https://example.com --sitemap include   # Use sitemap
firecrawl map https://example.com --sitemap skip      # Skip sitemap
firecrawl map https://example.com --sitemap only      # サイトマップのみを使用

# Ignore query parameters (dedupe URLs)
firecrawl map https://example.com --ignore-query-parameters

# Wait for map to complete with timeout
firecrawl map https://example.com --wait --timeout 60

# Save to file
firecrawl map https://example.com -o urls.txt
firecrawl map https://example.com --json --pretty -o urls.json
```

**利用可能なオプション:**

オプション説明`--url <url>`マッピング対象の URL（位置引数の代替）`--limit <number>`検出する最大 URL 数`--search <query>`検索クエリで URL を絞り込み`--sitemap <mode>`サイトマップの処理モード: `include`, `skip`, `only``--include-subdomains`サブドメインを含める`--ignore-query-parameters`クエリパラメータが異なる URL を同一として扱う`--wait`マップ処理の完了を待機`--timeout <seconds>`タイムアウト時間（秒）`--json`JSON 形式で出力`--output <path>`出力をファイルに保存`--pretty`JSON 出力を整形して表示

* * *

### Browser

安全なブラウザサンドボックスを使って、エージェントをWebとやり取りさせます。 クラウド上のブラウザセッションを起動し、Python、JavaScript、または bash のコードをリモートで実行します。各セッションでは完全な Chromium インスタンスが動作しており、ローカルにブラウザをインストールする必要はありません。コードはサーバー側で実行され、あらかじめ設定された [Playwright](https://playwright.dev/) の `page` オブジェクトをすぐに利用できます。

```
# Launch a cloud browser session
firecrawl browser launch-session

# agent-browserコマンドを実行(デフォルト - "agent-browser"が自動的にプレフィックスとして付与されます)
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

#### ブラウザオプション

```
# Launch with custom TTL (10 minutes) and live view
firecrawl browser launch-session --ttl 600 --stream

# 非アクティブタイムアウトを指定して起動
firecrawl browser launch-session --ttl 120 --ttl-inactivity 60

# agent-browser commands (default - "agent-browser" is auto-prefixed)
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

**サブコマンド:**

SubcommandDescription`launch-session`新しいクラウドブラウザセッションを起動します（セッション ID、CDP URL、ライブビュー URL を返します）`execute <code>`セッション内で Playwright の Python/JS コードまたは bash コマンドを実行します`list [status]`ブラウザセッションを一覧表示します（`active` または `destroyed`でフィルタ可能）`close`ブラウザセッションを閉じます

**Execute オプション:**

OptionDescription`--bash`サンドボックス内で bash コマンドをリモート実行します（デフォルト）。[agent-browser](https://github.com/vercel-labs/agent-browser)（40 以上のコマンド）がプリインストールされており、コマンドに自動でプレフィックスされます。`CDP_URL` は自動で設定されるため、agent-browser はセッションに自動的に接続します。AI エージェント向けの推奨手段です。`--python`Playwright の Python コードとして実行します。Playwright の `page` オブジェクトが利用可能で、`await page.goto()`, `await page.title()` などを使用できます。`--node`Playwright の JavaScript コードとして実行します。同じ `page` オブジェクトが利用可能です。`--session <id>`対象とする特定のセッションを指定します（デフォルト: アクティブなセッション）

**Launch オプション:**

OptionDescription`--ttl <seconds>`セッション全体の TTL（デフォルト: 600、範囲: 30–3600）`--ttl-inactivity <seconds>`一定時間操作がない場合に自動終了します（範囲: 10–3600）`--profile <name>`プロファイル名（ブラウザの状態をセッション間で保存・再利用します）`--no-save-changes`既存のプロファイルデータを読み込みますが、変更は保存しません`--stream`ライブビューのストリーミングを有効化します

**共通オプション:**

OptionDescription`--output <path>`出力をファイルに保存します`--json`JSON 形式で出力します

* * *

### クロール

指定した URL を起点に、ウェブサイト全体をクロールします。

```
# Start a crawl (returns job ID immediately)
firecrawl crawl https://example.com

# Wait for crawl to complete
firecrawl crawl https://example.com --wait

# 進行状況インジケーター付きで待機
firecrawl crawl https://example.com --wait --progress
```

#### クロールのステータスを確認する

```
# ジョブIDを使用してクロールステータスを確認
firecrawl crawl <job-id>

# 実際のジョブIDの例
firecrawl crawl 550e8400-e29b-41d4-a716-446655440000
```

#### クロールオプション

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

# カスタムポーリング間隔とタイムアウト
firecrawl crawl https://example.com --wait --poll-interval 10 --timeout 300

# Save results to file
firecrawl crawl https://example.com --wait --pretty -o results.json
```

**利用可能なオプション:**

OptionDescription`--url <url>`クロールするURL（位置引数の代わり）`--wait`クロールの完了を待機`--progress`待機中に進行状況インジケーターを表示`--poll-interval <seconds>`ポーリング間隔（デフォルト: 5）`--timeout <seconds>`待機時のタイムアウト時間`--status`既存のクロールジョブのステータスを確認`--limit <number>`クロールする最大ページ数`--max-depth <number>`クロールの最大深さ`--include-paths <paths>`含めるパス（カンマ区切り）`--exclude-paths <paths>`除外するパス（カンマ区切り）`--sitemap <mode>`サイトマップの処理モード: `include`、`skip`、`only``--allow-subdomains`サブドメインも対象に含める`--allow-external-links`外部リンクをたどる`--crawl-entire-domain`ドメイン全体をクロール`--ignore-query-parameters`クエリパラメーターが異なるURLを同一として扱う`--delay <ms>`リクエスト間の遅延時間`--max-concurrency <n>`最大同時リクエスト数`--output <path>`出力をファイルに保存`--pretty`JSON出力を整形して表示

* * *

### エージェント

自然言語プロンプトを使用して、Web上からデータを検索・収集します。

```
# 基本的な使い方 - URLは省略可能
firecrawl agent "Find the top 5 AI startups and their funding amounts" --wait

# Focus on specific URLs
firecrawl agent "Compare pricing plans" --urls https://slack.com/pricing,https://teams.microsoft.com/pricing --wait

# Use a schema for structured output
firecrawl agent "Get company information" --urls https://example.com --schema '{"name": "string", "founded": "number"}' --wait

# Use schema from a file
firecrawl agent "Get product details" --urls https://example.com --schema-file schema.json --wait
```

#### エージェントオプション

```
# より高精度な結果を得るにはSpark 1 Proを使用
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

**利用可能なオプション:**

OptionDescription`--urls <urls>`エージェントが対象とするURLの任意のリスト（カンマ区切り）`--model <model>`使用するモデル: `spark-1-mini`（デフォルト、60%安価）または `spark-1-pro`（高精度）`--schema <json>`構造化出力用のJSONスキーマ（インラインJSON文字列）`--schema-file <path>`構造化出力用のJSONスキーマファイルへのパス`--max-credits <number>`消費するクレジットの上限（上限に達するとジョブは失敗）`--status`既存のエージェントジョブのステータスを確認`--wait`結果を返す前にエージェントの完了を待つ`--poll-interval <seconds>`待機中のポーリング間隔（デフォルト: 5）`--timeout <seconds>`待機時のタイムアウト（デフォルト: タイムアウトなし）`--output <path>`出力をファイルに保存`--json`JSON形式で出力

* * *

### クレジット使用状況

チームのクレジット残高と利用状況を確認できます。

```
# クレジット使用量を確認
firecrawl credit-usage

# JSON形式で出力
firecrawl credit-usage --json --pretty
```

* * *

### Version

CLIのバージョンを表示します。

```
firecrawl version
# または
firecrawl --version
```

## グローバルオプション

これらのオプションはすべてのコマンドで利用できます。

オプション短縮形説明`--status`バージョン、認証情報、同時実行数、クレジット残高を表示する`--api-key <key>``-k`このコマンドで使用する API キーを、保存されているキーより優先して指定する`--api-url <url>`カスタム API URL を使用する（セルフホスト環境／ローカル開発向け）`--help``-h`コマンドのヘルプを表示する`--version``-V`CLI のバージョン情報を表示する

## 出力の処理

CLI はデフォルトで標準出力 (stdout) に出力するため、パイプやリダイレクトが容易です。

```
# マークダウンを別のコマンドにパイプする
firecrawl https://example.com | head -50

# ファイルにリダイレクトする
firecrawl https://example.com > output.md

# 整形されたJSON形式で保存する
firecrawl https://example.com --format markdown,links --pretty -o data.json
```

### フォーマットの挙動

- **単一フォーマット**: 生のコンテンツを出力します（markdown テキスト、HTML など）
- **複数フォーマット**: 要求されたすべてのデータを含む JSON を出力します

```
# Raw markdown output
firecrawl https://example.com --format markdown

# 複数フォーマットを使用したJSON出力
firecrawl https://example.com --format markdown,links
```

## 使用例

### クイックスクレイプ

```
# URLからMarkdownコンテンツを取得(クリーンな出力には --only-main-content を使用)
firecrawl https://docs.firecrawl.dev --only-main-content

# Get HTML content
firecrawl https://example.com --html -o page.html
```

### サイト全体クロール

```
# 制限付きでドキュメントサイトをクロールする
firecrawl crawl https://docs.example.com --limit 50 --max-depth 2 --wait --progress -o docs.json
```

### サイトの発見

```
# すべてのブログ投稿を検索
firecrawl map https://example.com --search "blog" -o blog-urls.txt
```

### 調査ワークフロー

```
# リサーチ用の検索とスクレイピング結果
firecrawl search "machine learning best practices 2024" --scrape --scrape-formats markdown --pretty
```

### エージェント

```
# URLs are optional
firecrawl agent "Find the top 5 AI startups and their funding amounts" --wait

# 特定のURLを対象にする
firecrawl agent "Compare pricing plans" --urls https://slack.com/pricing,https://teams.microsoft.com/pricing --wait
```

### ブラウザ自動化

```
# Launch a session, scrape a page, and close
firecrawl browser launch-session
firecrawl browser execute "open https://news.ycombinator.com"
firecrawl browser execute "snapshot"
firecrawl browser execute "scrape"
firecrawl browser close

# bashモード経由でagent-browserを使用(デフォルト — AIエージェント向けに推奨)
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

# リンクを抽出してjqで処理
firecrawl https://example.com --format links | jq '.links[].url'

# Count URLs from map
firecrawl map https://example.com | wc -l
```

## テレメトリー

CLI は、製品の改善のために認証時に匿名の利用状況データを収集します：

- CLI バージョン、OS、Node.js バージョン
- 開発ツールの検出（例：Cursor、VS Code、Claude Code）

**CLI を通じてコマンド内容、URL、ファイル内容が収集されることは一切ありません。** テレメトリーを無効にするには、次の環境変数を設定します：

```
export FIRECRAWL_NO_TELEMETRY=1
```

## オープンソース

Firecrawl CLI と Skill はオープンソースで、GitHub で公開されています: [firecrawl/cli](https://github.com/firecrawl/cli)

> Firecrawl API キーが必要な AI エージェントですか？ 自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。