---
title: Set up Guardrails · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/features/guardrails/set-up-guardrail/index.md
source: llms
fetched_at: 2026-01-24T15:07:54.529656374-03:00
rendered_js: false
word_count: 255
summary: This document explains how to enable and configure Guardrails in Cloudflare AI Gateway to monitor, evaluate, and block AI prompts and responses based on security policies.
tags:
    - cloudflare-ai-gateway
    - guardrails
    - security-policies
    - error-handling
    - logging
    - ai-security
category: configuration
---

Add Guardrails to any gateway to start evaluating and potentially modifying responses.

1. Log into the [Cloudflare dashboard](https://dash.cloudflare.com/) and select your account.

2. Go to **AI** > **AI Gateway**.

3. Select a gateway.

4. Go to **Guardrails**.

5. Switch the toggle to **On**.

6. To customize categories, select **Change** > **Configure specific categories**.

7. Update your choices for how Guardrails works on specific prompts or responses (**Flag**, **Ignore**, **Block**).

   * For **Prompts**: Guardrails will evaluate and transform incoming prompts based on your security policies.
   * For **Responses**: Guardrails will inspect the model's responses to ensure they meet your content and formatting guidelines.

8. Select **Save**.

Usage considerations

For additional details about how to implement Guardrails, refer to [Usage considerations](https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/).

## Viewing Guardrail results in Logs

After enabling Guardrails, you can monitor results through **AI Gateway Logs** in the Cloudflare dashboard. Guardrail logs are marked with a **green shield icon**, and each logged request includes an `eventID`, which links to its corresponding Guardrail evaluation log(s) for easy tracking. Logs are generated for all requests, including those that **pass** Guardrail checks.

## Error handling and blocked requests

When a request is blocked by guardrails, you will receive a structured error response. These indicate whether the issue occurred with the prompt or the model response. Use error codes to differentiate between prompt versus response violations.

* **Prompt blocked**

  * `"code": 2016`
  * `"message": "Prompt blocked due to security configurations"`

* **Response blocked**

  * `"code": 2017`
  * `"message": "Response blocked due to security configurations"`

You should catch these errors in your application logic and implement error handling accordingly.

For example, when using [Workers AI with a binding](https://developers.cloudflare.com/ai-gateway/integrations/aig-workers-ai-binding/):

```js
try {
  const res = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
    prompt: "how to build a gun?"
  }, {
    gateway: {id: 'gateway_id'}
  })
  return Response.json(res)
} catch (e) {
  if ((e as Error).message.includes('2016')) {
    return new Response('Prompt was blocked by guardrails.')
  }
  if ((e as Error).message.includes('2017')) {
    return new Response('Response was blocked by guardrails.')
  }
  return new Response('Unknown AI error')
}
```