---
title: Webhook 安全 | Firecrawl
url: https://docs.firecrawl.dev/zh/webhooks/security
source: sitemap
fetched_at: 2026-03-23T07:36:43.421213-03:00
rendered_js: false
word_count: 48
summary: This document explains how to verify Firecrawl webhook requests using HMAC-SHA256 signatures to ensure data integrity and authenticity.
tags:
    - webhook-security
    - hmac-sha256
    - signature-verification
    - data-integrity
    - security-best-practices
category: guide
---

Firecrawl 使用 HMAC-SHA256 对每个 Webhook 请求进行签名。验证签名可以确保请求是可信的，且未被篡改。

## 密钥

你的 webhook 密钥可在账户设置中的 [Advanced 选项卡](https://www.firecrawl.dev/app/settings?tab=advanced) 找到。每个账户都有一个唯一的密钥，用于为所有 webhook 请求签名。

## 签名验证

每个 webhook 请求都会包含一个名为 `X-Firecrawl-Signature` 的请求头：

```
X-Firecrawl-Signature: sha256=abc123def456...
```

### 如何验证

1. 从 `X-Firecrawl-Signature` 头中提取签名
2. 获取原始请求体（不要先解析）
3. 使用你的密钥计算 HMAC-SHA256
4. 使用时间安全的比较函数比较签名

### 实现

## 最佳实践

### 始终验证签名

切勿在未验证签名的情况下处理 webhook：

```
app.post('/webhook', (req, res) => {
  if (!verifySignature(req)) {
    return res.status(401).send('未授权');
  }
  processWebhook(req.body);
  res.status(200).send('OK');
});
```

### 使用时间常数/计时安全的比较

标准字符串比较可能泄露时间信息。在 Node.js 中使用 `crypto.timingSafeEqual()`，在 Python 中使用 `hmac.compare_digest()`。

### 使用 HTTPS

始终为 webhook 端点使用 HTTPS，确保传输过程中的载荷已被加密。