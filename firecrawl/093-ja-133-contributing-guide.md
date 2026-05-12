---
title: Running Locally | Firecrawl
url: https://docs.firecrawl.dev/ja/contributing/guide
source: sitemap
fetched_at: 2026-03-23T07:31:50.770771-03:00
rendered_js: false
word_count: 96
summary: このガイドは、Firecrawl API サーバーをローカル環境で構築および実行するためのセットアップ手順と開発環境の構築方法を解説しています。
tags:
    - firecrawl
    - local-development
    - api-setup
    - docker-configuration
    - environment-variables
    - server-installation
category: guide
---

このガイドでは、ローカル環境で Firecrawl API サーバーを実行する手順を説明します。以下のステップに従って、開発環境をセットアップし、サービスを起動し、最初のリクエストを送信してみてください。 Firecrawl にコントリビュートする場合、プロセスは一般的なオープンソースの慣習に従います。リポジトリをフォークし、変更を加え、テストを実行し、プルリクエストを送信してください。質問やセットアップのサポートが必要な場合は [help@firecrawl.com](mailto:help@firecrawl.com) までお問い合わせいただくか、[issue を作成](https://github.com/mendableai/firecrawl/issues)してください。

## 前提条件

続行する前に、次をインストールしてください：

依存関係必須インストールガイドNode.jsはい[nodejs.org](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)pnpm (v9+)はい[pnpm.io](https://pnpm.io/installation)Redisはい[redis.io](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)PostgreSQLはいDocker 経由（下記参照）またはローカルに直接インストールDocker任意PostgreSQL コンテナ環境のセットアップに必要

## データベースをセットアップする

`apps/nuq-postgres/nuq.sql` のスキーマで初期化された PostgreSQL データベースが必要です。最も簡単な方法は、`apps/nuq-postgres` 内の Docker イメージを使用することです。 Docker を起動した状態で、イメージをビルドしてコンテナを起動します：

```
docker build -t nuq-postgres apps/nuq-postgres

docker run --name nuqdb \
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  -v nuq-data:/var/lib/postgresql/data \
  -d nuq-postgres
```

## 環境変数を設定する

テンプレートをコピーして、`apps/api/` ディレクトリ内に `.env` ファイルを作成します。

```
cp apps/api/.env.example apps/api/.env
```

認証やオプションのサブサービス（PDF 解析、JS ブロック、AI 機能）を使わない最小限のローカルセットアップには、次の設定を使用します：

```
# ===== 必須 =====
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0
REDIS_URL=redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379

## DB認証を有効にするには、supabaseをセットアップする必要があります。
USE_DB_AUTHENTICATION=false

## キューイング用のPostgreSQL接続 — 認証情報、ホスト、またはDBが異なる場合は変更してください
NUQ_DATABASE_URL=postgres://postgres:postgres@localhost:5433/postgres

# ===== オプション =====
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=
# TEST_API_KEY=               # 認証を設定済みで実際のAPIキーでテストしたい場合に設定
# OPENAI_API_KEY=             # LLM依存機能（画像alt生成など）に必要
# BULL_AUTH_KEY=@
# PLAYWRIGHT_MICROSERVICE_URL= # Playwrightフォールバックを実行する場合に設定
# LLAMAPARSE_API_KEY=         # LlamaParseでPDFを解析する場合に設定
# SLACK_WEBHOOK_URL=          # Slackにサーバーのヘルスステータスメッセージを送信する場合に設定
# POSTHOG_API_KEY=            # ジョブログなどのPostHogイベントを送信する場合に設定
# POSTHOG_HOST=               # ジョブログなどのPostHogイベントを送信する場合に設定
```

## 依存関係をインストールする

`apps/api/` ディレクトリで pnpm を使ってパッケージをインストールします。

## サービスを起動する

Redis、API サーバー、リクエスト送信用のターミナルの 3 つのターミナルセッションを同時に起動しておく必要があります。

### ターミナル 1 — Redis

プロジェクト内の任意のディレクトリから Redis サーバーを起動します:

### Terminal 2 — API サーバー

`apps/api/` ディレクトリに移動し、サービスを起動します：

これにより、API サーバーとクロールジョブの処理を担当するワーカーが起動されます。

### ターミナル 3 — テストリクエストを送信する

サーバーが正常に起動しているか、ヘルスチェックで確認します。

```
curl -X GET http://localhost:3002/test
```

これで `Hello, world!` というレスポンスが返ってくれば OK です。 `crawl` エンドポイントをテストするには:

```
curl -X POST http://localhost:3002/v1/crawl \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://mendable.ai"
  }'
```

## 代替案：Docker Compose

よりシンプルなセットアップを行うには、Docker Compose を使うことで、すべてのサービス（Redis、API サーバー、ワーカー）を 1 つのコマンドで実行できます。

1. Docker と Docker Compose がインストールされていることを確認します。
2. `apps/api/` ディレクトリ内で `.env.example` を `.env` にコピーし、必要に応じて設定します。
3. プロジェクトルートから次を実行します：

これにより、すべてのサービスが正しい構成で自動的に起動されます。

## テストの実行

テストスイートを実行するには、次のコマンドを実行します：