---
title: Testes de webhooks | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/webhooks/testing
source: sitemap
fetched_at: 2026-03-23T07:37:23.105714-03:00
rendered_js: false
word_count: 159
summary: This document provides instructions for exposing local development servers for webhook testing and outlines troubleshooting steps for common connection and signature verification errors.
tags:
    - webhooks
    - local-development
    - cloudflare-tunnels
    - signature-verification
    - debugging
    - network-configuration
category: guide
---

## Desenvolvimento local

Como os webhooks precisam alcançar seu servidor pela internet, você terá que expor publicamente seu servidor de desenvolvimento local.

### Usando o Cloudflare Tunnels

O [Cloudflare Tunnels](https://github.com/cloudflare/cloudflared/releases) oferece uma forma gratuita de expor seu servidor local sem abrir portas no firewall:

```
cloudflared tunnel --url localhost:3000
```

Você receberá uma URL pública como `https://abc123.trycloudflare.com`. Use essa URL na configuração do seu webhook:

```
{
  "url": "https://abc123.trycloudflare.com/webhook"
}
```

## Solução de problemas

### Webhooks Não Estão Chegando

- **Endpoint inacessível** - Verifique se seu servidor é acessível publicamente e se os firewalls permitem conexões de entrada
- **Usando HTTP** - URLs de webhook devem usar HTTPS
- **Eventos incorretos** - Verifique o filtro de `events` na configuração do seu webhook

### Falha na verificação de assinatura

A causa mais comum é usar o corpo JSON já parseado em vez do corpo bruto da requisição.

```
// ❌ Incorreto – usando o corpo já parseado
const signature = crypto
  .createHmac('sha256', secret)
  .update(JSON.stringify(req.body))
  .digest('hex');

// ✅ Correto – usando o corpo bruto (raw)
app.use('/webhook', express.raw({ type: 'application/json' }));
app.post('/webhook', (req, res) => {
  const signature = crypto
    .createHmac('sha256', secret)
    .update(req.body) // Buffer bruto (raw)
    .digest('hex');
});
```

### Outros problemas

- **Secret incorreta** - Verifique se você está usando o secret correto nas suas [configurações de conta](https://www.firecrawl.dev/app/settings?tab=advanced)
- **Erros de timeout** - Certifique-se de que seu endpoint responda em até 10 segundos