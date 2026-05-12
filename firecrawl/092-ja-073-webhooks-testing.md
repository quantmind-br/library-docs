---
title: Webhook のテスト | Firecrawl
url: https://docs.firecrawl.dev/ja/webhooks/testing
source: sitemap
fetched_at: 2026-03-23T07:37:50.491107-03:00
rendered_js: false
word_count: 52
summary: This document provides instructions for setting up a local development environment for webhooks using Cloudflare Tunnels and troubleshooting common delivery and signature verification issues.
tags:
    - webhook-setup
    - local-development
    - cloudflare-tunnels
    - signature-verification
    - troubleshooting
    - api-integration
category: guide
---

## ローカル開発

Webhook はインターネット経由であなたのサーバーに到達する必要があるため、ローカルの開発サーバーを公開する必要があります。

### Cloudflare Tunnels の利用

[Cloudflare Tunnels](https://github.com/cloudflare/cloudflared/releases) は、ファイアウォールのポートを開放することなくローカルサーバーを公開できる無料の手段です。

```
cloudflared tunnel --url localhost:3000
```

`https://abc123.trycloudflare.com` のような公開 URL が発行されます。この URL を Webhook の設定で使用してください：

```
{
  "url": "https://abc123.trycloudflare.com/webhook"
}
```

## トラブルシューティング

### Webhook が届かない

- **エンドポイントにアクセスできない** - サーバーがインターネットから到達可能であり、ファイアウォールが受信接続を許可していることを確認してください
- **HTTP を使用している** - Webhook の URL は HTTPS を使用する必要があります
- **イベントが間違っている** - Webhook 設定の `events` フィルターを確認してください

### 署名検証が失敗する

最もよくある原因は、生のリクエストボディではなく、パース済みの JSON ボディを使用していることです。

```
// ❌ 誤り - 解析後のボディを使用している
const signature = crypto
  .createHmac('sha256', secret)
  .update(JSON.stringify(req.body))
  .digest('hex');

// ✅ 正解 - 生のボディを使用する
app.use('/webhook', express.raw({ type: 'application/json' }));
app.post('/webhook', (req, res) => {
  const signature = crypto
    .createHmac('sha256', secret)
    .update(req.body) // 生のバッファ
    .digest('hex');
});
```

### その他の問題

- **シークレットが誤っている** - [アカウント設定](https://www.firecrawl.dev/app/settings?tab=advanced) から取得した正しいシークレットを使用していることを確認してください
- **タイムアウトエラー** - エンドポイントが 10 秒以内に応答するようにしてください