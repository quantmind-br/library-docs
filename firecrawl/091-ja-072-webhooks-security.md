---
title: Webhook セキュリティ | Firecrawl
url: https://docs.firecrawl.dev/ja/webhooks/security
source: sitemap
fetched_at: 2026-03-23T07:37:54.862202-03:00
rendered_js: false
word_count: 45
summary: This document explains how to verify the authenticity and integrity of Firecrawl webhook requests using HMAC-SHA256 signatures.
tags:
    - webhooks
    - security
    - hmac-sha256
    - signature-verification
    - api-security
    - data-integrity
category: guide
---

Firecrawl はすべての Webhook リクエストに HMAC-SHA256 で署名します。署名を検証することで、リクエストが正当なものであり、改ざんされていないことを確認できます。

## シークレットキー

webhook シークレットは、アカウント設定の[Advanced タブ](https://www.firecrawl.dev/app/settings?tab=advanced)で確認できます。各アカウントには、すべての webhook リクエストに署名するために使用される固有のシークレットが割り当てられています。

## 署名の検証

各 webhook リクエストには、`X-Firecrawl-Signature` ヘッダーが含まれます：

```
X-Firecrawl-Signature: sha256=abc123def456...
```

### 検証方法

1. `X-Firecrawl-Signature` ヘッダーから署名を取り出す
2. パース前の生のリクエストボディを取得する
3. シークレットキーを使って HMAC-SHA256 を計算する
4. タイミングセーフな比較関数を使って署名を比較する

### 実装

## ベストプラクティス

### 署名は必ず検証する

署名を検証せずに webhook を処理してはいけません。

```
app.post('/webhook', (req, res) => {
  if (!verifySignature(req)) {
    return res.status(401).send('認可されていません');
  }
  processWebhook(req.body);
  res.status(200).send('OK');
});
```

### タイミングセーフな比較を使う

標準的な文字列比較はタイミング情報を漏えいするおそれがあります。Node.js では `crypto.timingSafeEqual()` を、Python では `hmac.compare_digest()` を使ってください。

### HTTPS を使用する

ペイロードが通信中も暗号化されるよう、Webhook エンドポイントには必ず HTTPS を使用してください。