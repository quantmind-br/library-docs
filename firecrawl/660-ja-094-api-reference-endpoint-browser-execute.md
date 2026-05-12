---
title: ブラウザーコードの実行 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/browser-execute
source: sitemap
fetched_at: 2026-03-23T07:23:16.284946-03:00
rendered_js: false
word_count: 65
summary: This document provides the API specifications for executing code within a browser sandbox environment using the Firecrawl platform.
tags:
    - api-reference
    - browser-sandbox
    - code-execution
    - http-request
    - firecrawl
category: api
---

ヘッダー値`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## リクエストボディ

パラメータ型必須デフォルト説明`code`stringはい-実行するコード（1〜100,000 文字）`language`stringいいえ`"node"`コードの言語：`"python"`、`"node"`、または `"bash"`（agent-browser CLI コマンド用）`timeout`numberいいえ-実行タイムアウト時間（秒、1〜300）

## レスポンス

FieldTypeDescription`success`booleanコードが正常に実行されたかどうか`stdout`stringコード実行時の標準出力`result`stringコード実行時の標準出力`stderr`stringコード実行時の標準エラー出力`exitCode`number実行されたプロセスの終了コード`killed`booleanプロセスがタイムアウトにより強制終了されたかどうか`error`string実行が失敗した場合のエラーメッセージ（失敗時のみ含まれる）

### リクエスト例

```
curl -X POST "https://api.firecrawl.dev/v2/browser/550e8400-e29b-41d4-a716-446655440000/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "await page.goto(\"https://example.com\")\ntitle = await page.title()\nprint(title)",
    "language": "python"
  }'
```

### 成功時のレスポンス例

```
{
  "success": true,
  "result": "Example Domain"
}
```

### エラー時のレスポンス例

```
{
  "success": true,
  "error": "TimeoutError: page.goto: Timeout 30000ms exceeded."
}
```

> Firecrawl API key が必要な AI agent ですか？自動オンボーディングの手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md)を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### ボディ

ブラウザーサンドボックス内で実行するコード

Required string length: `1 - 100000`

実行するコードの言語。JavaScript の場合は `node`、agent-browser の CLI コマンドの場合は `bash` を指定してください。

利用可能なオプション:

`python`,

`node`,

`bash`

実行タイムアウト（秒）

必須範囲: `1 <= x <= 300`

#### レスポンス

プロセスがタイムアウトにより強制終了されたかどうか