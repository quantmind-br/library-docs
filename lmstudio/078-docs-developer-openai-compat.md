---
title: OpenAI Compatibility Endpoints
url: https://lmstudio.ai/docs/developer/openai-compat
source: sitemap
fetched_at: 2026-04-07T21:30:31.947456607-03:00
rendered_js: false
word_count: 127
summary: This document explains how to connect existing OpenAI client libraries—including Python, TypeScript, and cURL examples—to use LM Studio by adjusting the 'base URL' to point locally instead of to OpenAI's servers.
tags:
    - openai-compatibility
    - base-url-setting
    - api-endpoints
    - local-server
    - client-setup
category: guide
---

### Supported endpoints[](#supported-endpoints)

EndpointMethodDocs`/v1/models`GET[Models](https://lmstudio.ai/docs/developer/openai-compat/models)`/v1/responses`POST[Responses](https://lmstudio.ai/docs/developer/openai-compat/responses)`/v1/chat/completions`POST[Chat Completions](https://lmstudio.ai/docs/developer/openai-compat/chat-completions)`/v1/embeddings`POST[Embeddings](https://lmstudio.ai/docs/developer/openai-compat/embeddings)`/v1/completions`POST[Completions](https://lmstudio.ai/docs/developer/openai-compat/completions)

* * *

## Set the `base url` to point to LM Studio[](#set-the-base-url-to-point-to-lm-studio "Link to 'Set the ,[object Object], to point to LM Studio'")

You can reuse existing OpenAI clients (in Python, JS, C#, etc) by switching up the "base URL" property to point to your LM Studio instead of OpenAI's servers.

Note: The following examples assume the server port is `1234`

### Python Example[](#python-example)

```

from openai import OpenAI

client = OpenAI(
+    base_url="http://localhost:1234/v1"
)

# ... the rest of your code ...
```

### Typescript Example[](#typescript-example)

```

import OpenAI from 'openai';

const client = new OpenAI({
+  baseUrl: "http://localhost:1234/v1"
});

// ... the rest of your code ...
```

### cURL Example[](#curl-example)

```

- curl https://api.openai.com/v1/chat/completions \
+ curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
-     "model": "gpt-4o-mini",
+     "model": "use the model identifier from LM Studio here",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'
```

## Using Codex with LM Studio[](#using-codex-with-lm-studio "Link to 'Using Codex with LM Studio'")

Codex is supported because LM Studio implements the OpenAI-compatible `POST /v1/responses` endpoint.

See: [Use Codex with LM Studio](https://lmstudio.ai/docs/integrations/codex) and [Responses](https://lmstudio.ai/docs/developer/openai-compat/responses).

* * *

Other OpenAI client libraries should have similar options to set the base URL.

If you're running into trouble, hop onto our [Discord](https://discord.gg/lmstudio) and enter the `#🔨-developers` channel.