---
title: ブラウザ | Firecrawl
url: https://docs.firecrawl.dev/ja/features/browser
source: sitemap
fetched_at: 2026-03-23T07:23:11.614337-03:00
rendered_js: false
word_count: 253
summary: Firecrawl Browser Sandbox provides a secure, managed infrastructure for AI agents to perform web operations like browsing, form interaction, and authentication without local driver setup.
tags:
    - browser-automation
    - agent-framework
    - web-scraping
    - headless-browser
    - playwright
    - cloud-sandbox
category: guide
---

Firecrawl Browser Sandbox は、エージェントが Web を操作できる安全なブラウザ環境を提供します。フォームへの入力、ボタンのクリック、認証などを実行できます。 ローカルでのセットアップは不要で、Chromium のインストールやドライバーの互換性の問題もありません。agent browser と Playwright はプリインストール済みです。 [API](https://docs.firecrawl.dev/ja/api-reference/endpoint/browser-create)、[CLI](https://docs.firecrawl.dev/ja/sdks/cli#browser) (Bash / agent-browser、Python、Node)、[Node SDK](https://docs.firecrawl.dev/ja/sdks/node#browser)、[Python SDK](https://docs.firecrawl.dev/ja/sdks/python#browser)、[Vercel AI SDK](https://docs.firecrawl.dev/ja/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk)、および [MCP Server](https://docs.firecrawl.dev/ja/mcp-server) 経由で利用できます。 AI コーディングエージェント (Claude Code、Codex、Open Code、Cursor など) にブラウザ対応を追加するには、Firecrawl スキルをインストールします。

```
npx -y firecrawl-cli@latest init --all --browser
```

各セッションは、インフラを管理することなくスケールする、分離された使い捨てまたは永続的なサンドボックス内で実行されます。

## クイックスタート

セッションを作成し、コードを実行して終了します。

- **ドライバーのインストール不要** - Chromium バイナリ不要、`playwright install` 不要、ドライバー互換性の問題なし
- **Python、JavaScript、Bash 対応** - API、CLI、または SDK 経由でコードを送信して結果を取得。3 つの言語すべてがサンドボックス環境上でリモート実行されます
- **agent-browser** - 60 以上のコマンドがプリインストール済みの CLI。AI エージェントは Playwright コードではなくシンプルな bash コマンドを書くことで操作できます
- **Playwright ロード済み** - サンドボックス環境には Playwright がプリインストール済み。必要であればエージェントは Playwright コードを記述することもできます
- **CDP へのアクセス** - 完全な制御が必要なときは、独自の Playwright インスタンスを WebSocket 経由で接続可能
- **ライブビュー** - 埋め込み可能なストリーム URL を使って、セッションをリアルタイムで監視可能
- **インタラクティブ ライブビュー** - 埋め込み可能なインタラクティブなストリームを通じて、ユーザーがブラウザを直接操作できるようにします

## セッションを開始する

セッションID、CDP URL、ライブビューのURLを返します。

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}
```

## コードの実行

セッション内で Python、JavaScript、または bash のコードを実行します。Output は `stdout` 経由で返されます。Node.js では、最後の式の値も `result` として利用できます。

```
{
  "success": true,
  "stdout": "",
  "result": "Example Domain",
  "stderr": "",
  "exitCode": 0,
  "killed": false
}
```

### ファイルダウンロードの処理

セッション内でダウンロードされたファイルはキャプチャして、base64 として返すことができます。execute エンドポイントから Playwright の download API を使用します。

## agent-browser (Bash モード)

[agent-browser](https://github.com/vercel-labs/agent-browser) は、すべてのサンドボックスにプリインストールされているヘッドレスブラウザ CLI です。Playwright のコードを書く代わりに、エージェントはシンプルな bash コマンドを送信します。CLI は自動的に `--cdp` フラグを付与し、agent-browser がアクティブなセッションに自動で接続できるようにします。

### 省略記法

`browser` コマンドを使う最速の方法です。省略記法も `execute` も、どちらも自動的に agent-browser にコマンドを送信します。省略記法は単に `execute` を省略し、必要に応じてセッションを自動的に開始します。

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
firecrawl browser "click @e5"
```

### CLI

明示的な形では `execute` を使用します。コマンドは自動的に agent-browser に送信されるので、`agent-browser` と入力したり、`--bash` を付けたりする必要はありません。

### API と SDK

API または SDK を使って agent-browser コマンドを実行するには、`language: "bash"` を指定します：

## セッション管理

### 永続セッション

デフォルトでは、各ブラウザセッションは常にまっさらな状態から始まります。`profile` を使うと、セッション間でブラウザの状態を保存し再利用できます。ログイン状態の維持や設定の保持に役立ちます。 プロファイルを保存または選択するには、セッション作成時に `profile` パラメータを使用します。

パラメータデフォルト説明`name`—永続プロファイルの名前です。同じ名前のセッションはストレージを共有します。`saveChanges``true``true` の場合、ブラウザの状態は終了時にプロファイルへ保存されます。`false` に設定すると、既存データを読み込むだけで書き込みは行いません — 複数の同時読み取りが必要な場合に便利です。

ブラウザセッションの状態は、セッションがクローズされたときにのみ保存されます。そのため、再利用できるよう、使い終わったらブラウザセッションをクローズすることを推奨します。セッションがクローズされると、そのセッション ID は無効になり、再利用できなくなります。代わりに、同じプロファイル名で新しいセッションを作成し、レスポンスで返される新しいセッション ID を使用してください。保存してクローズするには:

### セッション一覧を取得する

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
      "liveViewUrl": "https://liveview.firecrawl.dev/...",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
      "createdAt": "2025-01-15T10:30:00Z",
      "lastActivity": "2025-01-15T10:35:00Z"
    }
  ]
}
```

### TTL 設定

セッションには 2 種類の TTL 設定があります:

ParameterDefaultDescription`ttl`600s (10 min)セッションの最大存続時間 (30-3600s)`activityTtl`300s (5 min)非アクティブ時の自動クローズまでの時間 (10-3600s)

### セッションを終了する

## ライブビュー

各セッションのレスポンスには `liveViewUrl` が含まれており、これを埋め込むことでブラウザーの状態をリアルタイムで確認できます。デバッグ、デモ、ブラウザー駆動型 UI の構築などに便利です。

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}

<iframe src="LIVE_VIEW_URL" width="100%" height="600" />
```

### インタラクティブ Live View

レスポンスには `interactiveLiveViewUrl` も含まれます。閲覧専用の標準的な Live View と異なり、インタラクティブ Live View では、埋め込みストリームを通じてユーザーがブラウザセッションを直接操作できます (クリックや文字入力など) 。これは、ユーザー向けのブラウザ UI の構築、共同でのデバッグ、あるいは閲覧者がブラウザを操作する必要があるあらゆるシナリオに有用です。

```
<iframe src="INTERACTIVE_LIVE_VIEW_URL" width="100%" height="600" />
```

## CDP 経由での接続

すべてのセッションは CDP WebSocket URL を提供します。`execute` API と `--bash` フラグでほとんどのユースケースはカバーできますが、完全にローカルで制御したい場合は、直接接続することもできます。

## Browser を使うべきタイミング

ユースケース適切なツール既知の URL からコンテンツを抽出する[Scrape](https://docs.firecrawl.dev/ja/features/scrape)Web を検索して結果を取得する[Search](https://docs.firecrawl.dev/ja/features/search)ページネーションの操作、フォーム入力、クリックを伴うフローの操作**Browser**インタラクションを伴うマルチステップのワークフロー**Browser**複数のサイトを並列にブラウジングする**Browser** (各セッションは分離されている)

## ユースケース

- **競合分析** - 競合サイトを閲覧し、検索フォームやフィルターを操作して、価格や機能を構造化データとして抽出する
- **ナレッジベースの取り込み** - クリック操作、ページネーション、認証が必要なヘルプセンター、ドキュメント、サポートポータルを辿る
- **市場調査** - 複数のブラウザーセッションを並列で起動し、求人サイト、不動産リスティング、法的データベースなどからデータセットを構築する

## 料金

料金体系はシンプルで、ブラウザの稼働1分あたり2クレジットです。無料プランでは最大5時間まで無料で利用できます。

## レート制限

初期リリースでは、すべてのプランで最大 20 個のブラウザーセッションを同時に稼働させることができます。

## API リファレンス

- [ブラウザセッションを作成](https://docs.firecrawl.dev/ja/api-reference/endpoint/browser-create)
- [ブラウザコードを実行](https://docs.firecrawl.dev/ja/api-reference/endpoint/browser-execute)
- [ブラウザセッションの一覧を取得](https://docs.firecrawl.dev/ja/api-reference/endpoint/browser-list)
- [ブラウザセッションを削除](https://docs.firecrawl.dev/ja/api-reference/endpoint/browser-delete)

* * *

ご意見やご不明な点がありましたら、[help@firecrawl.com](mailto:help@firecrawl.com) までメールいただくか、[Discord](https://discord.gg/firecrawl) でご連絡ください。

> Firecrawl API key が必要な AI agent の方は、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) の自動オンボーディング手順をご覧ください。