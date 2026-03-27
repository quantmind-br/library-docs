---
title: Segurança de Webhooks | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/webhooks/security
source: sitemap
fetched_at: 2026-03-23T07:37:31.543205-03:00
rendered_js: false
word_count: 164
summary: This document explains how to verify the authenticity of Firecrawl webhook requests by validating HMAC-SHA256 signatures provided in the request headers.
tags:
    - webhooks
    - api-security
    - hmac-sha256
    - signature-verification
    - data-integrity
    - security-best-practices
category: guide
---

Firecrawl assina todas as requisições de webhook usando HMAC-SHA256. Verificar essas assinaturas garante que as requisições sejam autênticas e não tenham sido adulteradas.

## Chave secreta

Seu segredo de webhook está disponível na [aba Advanced](https://www.firecrawl.dev/app/settings?tab=advanced) das configurações da sua conta. Cada conta tem um segredo exclusivo usado para assinar todas as solicitações de webhook.

## Verificação de assinatura

Cada requisição de webhook inclui um cabeçalho `X-Firecrawl-Signature`:

```
X-Firecrawl-Signature: sha256=abc123def456...
```

### Como verificar

1. Extraia a assinatura do cabeçalho `X-Firecrawl-Signature`
2. Obtenha o corpo bruto da requisição exatamente como recebido (não faça parsing antes)
3. Calcule o HMAC-SHA256 usando sua chave secreta
4. Compare as assinaturas usando uma função de comparação segura a timing (timing-safe)

### Implementação

## Práticas recomendadas

### Sempre valide as assinaturas

Nunca processe um webhook sem verificar a assinatura antes:

```
app.post('/webhook', (req, res) => {
  if (!verifySignature(req)) {
    return res.status(401).send('Não autorizado');
  }
  processWebhook(req.body);
  res.status(200).send('OK');
});
```

### Use comparações seguras em termos de tempo

Comparações padrão de strings podem revelar informações por tempo de execução. Use `crypto.timingSafeEqual()` no Node.js ou `hmac.compare_digest()` no Python.

### Use HTTPS

Sempre use HTTPS no endpoint do webhook para garantir que os dados sejam criptografados em trânsito.