---
title: Webhook 测试 | Firecrawl
url: https://docs.firecrawl.dev/zh/webhooks/testing
source: sitemap
fetched_at: 2026-03-23T07:36:48.449948-03:00
rendered_js: false
word_count: 50
summary: This document provides guidance on exposing local development servers for webhook integration and offers troubleshooting steps for common issues like connectivity, signature verification, and request timeouts.
tags:
    - webhook-configuration
    - local-development
    - troubleshooting
    - cloudflare-tunnels
    - signature-verification
    - api-integration
category: guide
---

## 本地开发

由于 Webhook 需要通过互联网访问你的服务器，你需要将本地开发服务器对外暴露。

### 使用 Cloudflare Tunnels

[Cloudflare Tunnels](https://github.com/cloudflare/cloudflared/releases) 提供了一种免费的方式，无需打开防火墙端口即可将本地服务器暴露到互联网：

```
cloudflared tunnel --url localhost:3000
```

你会获得一个类似 `https://abc123.trycloudflare.com` 的公网 URL。在你的 webhook 配置中使用该地址：

```
{
  "url": "https://abc123.trycloudflare.com/webhook"
}
```

## 故障排查

### Webhook 未到达

- **端点不可访问** - 确认你的服务器可以被公网访问，并且防火墙允许入站连接
- **使用 HTTP** - Webhook URL 必须使用 HTTPS
- **事件配置错误** - 检查 webhook 配置中的 `events` 过滤器

### 签名验证失败

最常见的原因是使用了解析后的 JSON 请求体，而不是原始请求体（raw body）。

```
// ❌ 错误——使用了解析后的请求体
const signature = crypto
  .createHmac('sha256', secret)
  .update(JSON.stringify(req.body))
  .digest('hex');

// ✅ 正确——使用原始请求体
app.use('/webhook', express.raw({ type: 'application/json' }));
app.post('/webhook', (req, res) => {
  const signature = crypto
    .createHmac('sha256', secret)
    .update(req.body) // 原始缓冲区
    .digest('hex');
});
```

### 其他问题

- **密钥错误** - 请在[账户设置](https://www.firecrawl.dev/app/settings?tab=advanced)中确认你使用的是正确的密钥
- **超时错误** - 确保你的接口能在 10 秒内返回响应