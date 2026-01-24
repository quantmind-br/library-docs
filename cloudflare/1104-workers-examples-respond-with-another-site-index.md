---
title: Respond with another site
url: https://developers.cloudflare.com/workers/examples/respond-with-another-site/index.md
source: llms
fetched_at: 2026-01-24T15:26:20.244513309-03:00
rendered_js: false
word_count: 89
summary: This document demonstrates how to use Cloudflare Workers to act as a proxy by fetching content from an external website and returning the response to the client. It provides implementation examples in JavaScript, TypeScript, and Python, including basic request method validation.
tags:
    - cloudflare-workers
    - proxy
    - fetch-api
    - request-handling
    - javascript
    - typescript
    - python
category: tutorial
---

---
title: Respond with another site · Cloudflare Workers docs
description: Respond to the Worker request with the response from another
  website (example.com in this example).
lastUpdated: 2025-10-17T07:10:47.000Z
chatbotDeprioritize: false
tags: Middleware,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/respond-with-another-site/
  md: https://developers.cloudflare.com/workers/examples/respond-with-another-site/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/respond-with-another-site)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      function MethodNotAllowed(request) {
        return new Response(`Method ${request.method} not allowed.`, {
          status: 405,
          headers: {
            Allow: "GET",
          },
        });
      }
      // Only GET requests work with this proxy.
      if (request.method !== "GET") return MethodNotAllowed(request);
      return fetch(`https://example.com`);
    },
  };
  ```

  [Run Worker in Playground](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwAOACwB2AGyiAzJICcogIwAmAFwsWbYBzhcafASInS5i1QFgAUAGF0VCAFMH2ACJQAzjHQeo0e2ok2ngExCRUcMCODABEUDSOAB4AdABWHjGkqFBgzpHRcQkp6THWdg7OENgAKnQwjoFwMDBgfARQ9sipcABucB68CLAQANTA6LjgjtbWSd5IJLiOqHDgECQA3lYkJP10VLxBjhC8ABYAFAiOAI4gjh4QAJSb2ztB1Lz+VCQAssenEwAcugIABBMBgdAAd0cuEuNzuD2eWzebyuEBACG+VEcUJIACV7t4qB5HOcAAZ-CAA3AkAAkGyut3uEGSUWpEwAvuEQbsIdDYclyQAaF6o1EPAggDyBUSCACswte4pIp0ccCWCBlYpVb3BkKhgRiAHEAKLVGJK3UkTlW8Wcx5EZU253IZAkADyVDAdBIZuqJCZiIgHhIUMwAGsw35TiRqZ4SDAEOhEnRks6oKgSPDmQ82f8JiQAIQMBgkE3mmLPdGY75UmnAsH8mFwoMsx3OmtYo4nC7k04QCAwGVupKRFqOZK8dDAckdna2qycojWTTMbS6fQ8fhCMRSWQKZQqMr2JwudxeHx+DpUQLBXSkCJRWLsjWhTJBHJ5Z8xMiQsilLYp6VDUdQNLszStLw7SdOk9gzFYGwxMAcDxAA+uMky5DEaiFEsxQZJyq5rhuoRboYu4mAe5gqMw1hAA)

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      function MethodNotAllowed(request) {
        return new Response(`Method ${request.method} not allowed.`, {
          status: 405,
          headers: {
            Allow: "GET",
          },
        });
      }
      // Only GET requests work with this proxy.
      if (request.method !== "GET") return MethodNotAllowed(request);
      return fetch(`https://example.com`);
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response, fetch


  class Default(WorkerEntrypoint):
      def fetch(self, request):
          def method_not_allowed(request):
              msg = f'Method {request.method} not allowed.'
              headers = {"Allow": "GET"}
              return Response(msg, headers=headers, status=405)


          # Only GET requests work with this proxy.
          if request.method != "GET":
              return method_not_allowed(request)


          return fetch("https://example.com")
  ```