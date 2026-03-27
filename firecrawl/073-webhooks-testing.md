---
title: Webhook Testing | Firecrawl
url: https://docs.firecrawl.dev/webhooks/testing
source: sitemap
fetched_at: 2026-03-23T07:37:11.524278-03:00
rendered_js: false
word_count: 134
summary: This document provides instructions for exposing a local development server for webhook testing and outlines solutions for common webhook implementation errors such as signature verification and connection issues.
tags:
    - webhooks
    - local-development
    - cloudflare-tunnels
    - signature-verification
    - debugging
    - network-connectivity
category: guide
---

## Local Development

Since webhooks need to reach your server from the internet, you’ll need to expose your local development server publicly.

### Using Cloudflare Tunnels

[Cloudflare Tunnels](https://github.com/cloudflare/cloudflared/releases) provide a free way to expose your local server without opening firewall ports:

```
cloudflared tunnel --url localhost:3000
```

You’ll get a public URL like `https://abc123.trycloudflare.com`. Use this in your webhook config:

```
{
  "url": "https://abc123.trycloudflare.com/webhook"
}
```

## Troubleshooting

### Webhooks Not Arriving

- **Endpoint not accessible** - Verify your server is publicly reachable and firewalls allow incoming connections
- **Using HTTP** - Webhook URLs must use HTTPS
- **Wrong events** - Check the `events` filter in your webhook config

### Signature Verification Failing

The most common cause is using the parsed JSON body instead of the raw request body.

```
// Wrong - using parsed body
const signature = crypto
  .createHmac('sha256', secret)
  .update(JSON.stringify(req.body))
  .digest('hex');

// Correct - using raw body
app.use('/webhook', express.raw({ type: 'application/json' }));
app.post('/webhook', (req, res) => {
  const signature = crypto
    .createHmac('sha256', secret)
    .update(req.body) // Raw buffer
    .digest('hex');
});
```

### Other Issues

- **Wrong secret** - Verify you’re using the correct secret from your [account settings](https://www.firecrawl.dev/app/settings?tab=advanced)
- **Timeout errors** - Ensure your endpoint responds within 10 seconds