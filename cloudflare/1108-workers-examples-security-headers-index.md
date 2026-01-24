---
title: Set security headers
url: https://developers.cloudflare.com/workers/examples/security-headers/index.md
source: llms
fetched_at: 2026-01-24T15:26:24.3979269-03:00
rendered_js: false
word_count: 66
summary: Demonstrates how to implement and manage common security headers, such as Content-Security-Policy and X-Frame-Options, using Cloudflare Workers.
tags:
    - cloudflare-workers
    - security-headers
    - http-security
    - javascript
    - typescript
    - python
category: tutorial
---

---
title: Set security headers · Cloudflare Workers docs
description: Set common security headers (X-XSS-Protection, X-Frame-Options,
  X-Content-Type-Options, Permissions-Policy, Referrer-Policy,
  Strict-Transport-Security, Content-Security-Policy).
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Security,Middleware,JavaScript,TypeScript,Python,Rust
source_url:
  html: https://developers.cloudflare.com/workers/examples/security-headers/
  md: https://developers.cloudflare.com/workers/examples/security-headers/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/security-headers)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      const DEFAULT_SECURITY_HEADERS = {
        /*
      Secure your application with Content-Security-Policy headers.
      Enabling these headers will permit content from a trusted domain and all its subdomains.
      @see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy
      "Content-Security-Policy": "default-src 'self' example.com *.example.com",
      */
        /*
      You can also set Strict-Transport-Security headers.
      These are not automatically set because your website might get added to Chrome's HSTS preload list.
      Here's the code if you want to apply it:
      "Strict-Transport-Security" : "max-age=63072000; includeSubDomains; preload",
      */
        /*
      Permissions-Policy header provides the ability to allow or deny the use of browser features, such as opting out of FLoC - which you can use below:
      "Permissions-Policy": "interest-cohort=()",
      */
        /*
      X-XSS-Protection header prevents a page from loading if an XSS attack is detected.
      @see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-XSS-Protection
      */
        "X-XSS-Protection": "0",
        /*
      X-Frame-Options header prevents click-jacking attacks.
      @see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options
      */
        "X-Frame-Options": "DENY",
        /*
      X-Content-Type-Options header prevents MIME-sniffing.
      @see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options
      */
        "X-Content-Type-Options": "nosniff",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Cross-Origin-Embedder-Policy": 'require-corp; report-to="default";',
        "Cross-Origin-Opener-Policy": 'same-site; report-to="default";',
        "Cross-Origin-Resource-Policy": "same-site",
      };
      const BLOCKED_HEADERS = [
        "Public-Key-Pins",
        "X-Powered-By",
        "X-AspNet-Version",
      ];


      let response = await fetch(request);
      let newHeaders = new Headers(response.headers);


      const tlsVersion = request.cf.tlsVersion;
      console.log(tlsVersion);
      // This sets the headers for HTML responses:
      if (
        newHeaders.has("Content-Type") &&
        !newHeaders.get("Content-Type").includes("text/html")
      ) {
        return new Response(response.body, {
          status: response.status,
          statusText: response.statusText,
          headers: newHeaders,
        });
      }


      Object.keys(DEFAULT_SECURITY_HEADERS).map((name) => {
        newHeaders.set(name, DEFAULT_SECURITY_HEADERS[name]);
      });


      BLOCKED_HEADERS.forEach((name) => {
        newHeaders.delete(name);
      });


      if (tlsVersion !== "TLSv1.2" && tlsVersion !== "TLSv1.3") {
        return new Response("You need to use TLS version 1.2 or higher.", {
          status: 400,
        });
      } else {
        return new Response(response.body, {
          status: response.status,
          statusText: response.statusText,
          headers: newHeaders,
        });
      }
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      const DEFAULT_SECURITY_HEADERS = {
        /*
      Secure your application with Content-Security-Policy headers.
      Enabling these headers will permit content from a trusted domain and all its subdomains.
      @see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy
      "Content-Security-Policy": "default-src 'self' example.com *.example.com",
      */
        /*
      You can also set Strict-Transport-Security headers.
      These are not automatically set because your website might get added to Chrome's HSTS preload list.
      Here's the code if you want to apply it:
      "Strict-Transport-Security" : "max-age=63072000; includeSubDomains; preload",
      */
        /*
      Permissions-Policy header provides the ability to allow or deny the use of browser features, such as opting out of FLoC - which you can use below:
      "Permissions-Policy": "interest-cohort=()",
      */
        /*
      X-XSS-Protection header prevents a page from loading if an XSS attack is detected.
      @see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-XSS-Protection
      */
        "X-XSS-Protection": "0",
        /*
      X-Frame-Options header prevents click-jacking attacks.
      @see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options
      */
        "X-Frame-Options": "DENY",
        /*
      X-Content-Type-Options header prevents MIME-sniffing.
      @see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options
      */
        "X-Content-Type-Options": "nosniff",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Cross-Origin-Embedder-Policy": 'require-corp; report-to="default";',
        "Cross-Origin-Opener-Policy": 'same-site; report-to="default";',
        "Cross-Origin-Resource-Policy": "same-site",
      };
      const BLOCKED_HEADERS = [
        "Public-Key-Pins",
        "X-Powered-By",
        "X-AspNet-Version",
      ];


      let response = await fetch(request);
      let newHeaders = new Headers(response.headers);


      const tlsVersion = request.cf.tlsVersion;
      console.log(tlsVersion);
      // This sets the headers for HTML responses:
      if (
        newHeaders.has("Content-Type") &&
        !newHeaders.get("Content-Type").includes("text/html")
      ) {
        return new Response(response.body, {
          status: response.status,
          statusText: response.statusText,
          headers: newHeaders,
        });
      }


      Object.keys(DEFAULT_SECURITY_HEADERS).map((name) => {
        newHeaders.set(name, DEFAULT_SECURITY_HEADERS[name]);
      });


      BLOCKED_HEADERS.forEach((name) => {
        newHeaders.delete(name);
      });


      if (tlsVersion !== "TLSv1.2" && tlsVersion !== "TLSv1.3") {
        return new Response("You need to use TLS version 1.2 or higher.", {
          status: 400,
        });
      } else {
        return new Response(response.body, {
          status: response.status,
          statusText: response.statusText,
          headers: newHeaders,
        });
      }
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response, fetch


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          default_security_headers = {
              # Secure your application with Content-Security-Policy headers.
              #Enabling these headers will permit content from a trusted domain and all its subdomains.
              #@see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy
              "Content-Security-Policy": "default-src 'self' example.com *.example.com",
              #You can also set Strict-Transport-Security headers.
              #These are not automatically set because your website might get added to Chrome's HSTS preload list.
              #Here's the code if you want to apply it:
              "Strict-Transport-Security" : "max-age=63072000; includeSubDomains; preload",
              #Permissions-Policy header provides the ability to allow or deny the use of browser features, such as opting out of FLoC - which you can use below:
              "Permissions-Policy": "interest-cohort=()",
              #X-XSS-Protection header prevents a page from loading if an XSS attack is detected.
              #@see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-XSS-Protection
              "X-XSS-Protection": "0",
              #X-Frame-Options header prevents click-jacking attacks.
              #@see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options
              "X-Frame-Options": "DENY",
              #X-Content-Type-Options header prevents MIME-sniffing.
              #@see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options
              "X-Content-Type-Options": "nosniff",
              "Referrer-Policy": "strict-origin-when-cross-origin",
              "Cross-Origin-Embedder-Policy": 'require-corp; report-to="default";',
              "Cross-Origin-Opener-Policy": 'same-site; report-to="default";',
              "Cross-Origin-Resource-Policy": "same-site",
          }
          blocked_headers = ["Public-Key-Pins", "X-Powered-By" ,"X-AspNet-Version"]


          res = await fetch(request)
          new_headers = res.headers


          # This sets the headers for HTML responses
          if "text/html" in new_headers["Content-Type"]:
              return Response(res.body, status=res.status, statusText=res.statusText, headers=new_headers)


          for name in default_security_headers:
              new_headers[name] = default_security_headers[name]


          for name in blocked_headers:
              del new_headers["name"]


          tls = request.cf.tlsVersion


          if not tls in ("TLSv1.2", "TLSv1.3"):
              return Response("You need to use TLS version 1.2 or higher.", status=400)
          return Response(res.body, status=res.status, statusText=res.statusText, headers=new_headers)
  ```

* Rust

  ```rs
  use std::collections::HashMap;
  use worker::*;


  #[event(fetch)]
  async fn fetch(req: Request, _env: Env, _ctx: Context) -> Result<Response> {
      let default_security_headers = HashMap::from([
          //Secure your application with Content-Security-Policy headers.
          //Enabling these headers will permit content from a trusted domain and all its subdomains.
          //@see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy
          (
              "Content-Security-Policy",
              "default-src 'self' example.com *.example.com",
          ),
          //You can also set Strict-Transport-Security headers.
          //These are not automatically set because your website might get added to Chrome's HSTS preload list.
          //Here's the code if you want to apply it:
          (
              "Strict-Transport-Security",
              "max-age=63072000; includeSubDomains; preload",
          ),
          //Permissions-Policy header provides the ability to allow or deny the use of browser features, such as opting out of FLoC - which you can use below:
          ("Permissions-Policy", "interest-cohort=()"),
          //X-XSS-Protection header prevents a page from loading if an XSS attack is detected.
          //@see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-XSS-Protection
          ("X-XSS-Protection", "0"),
          //X-Frame-Options header prevents click-jacking attacks.
          //@see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options
          ("X-Frame-Options", "DENY"),
          //X-Content-Type-Options header prevents MIME-sniffing.
          //@see https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options
          ("X-Content-Type-Options", "nosniff"),
          ("Referrer-Policy", "strict-origin-when-cross-origin"),
          (
              "Cross-Origin-Embedder-Policy",
              "require-corp; report-to='default';",
          ),
          (
              "Cross-Origin-Opener-Policy",
              "same-site; report-to='default';",
          ),
          ("Cross-Origin-Resource-Policy", "same-site"),
      ]);
      let blocked_headers = ["Public-Key-Pins", "X-Powered-By", "X-AspNet-Version"];
      let tls = req.cf().unwrap().tls_version();
      let res = Fetch::Request(req).send().await?;
      let mut new_headers = res.headers().clone();


      // This sets the headers for HTML responses
      if Some(String::from("text/html")) == new_headers.get("Content-Type")? {
          return Ok(Response::from_body(res.body().clone())?
              .with_headers(new_headers)
              .with_status(res.status_code()));
      }
      for (k, v) in default_security_headers {
          new_headers.set(k, v)?;
      }


      for k in blocked_headers {
          new_headers.delete(k)?;
      }


      if !vec!["TLSv1.2", "TLSv1.3"].contains(&tls.as_str()) {
          return Response::error("You need to use TLS version 1.2 or higher.", 400);
      }
      Ok(Response::from_body(res.body().clone())?
          .with_headers(new_headers)
          .with_status(res.status_code()))


  }
  ```

* Hono

  ```ts
  import { Hono } from 'hono';
  import { secureHeaders } from 'hono/secure-headers';


  const app = new Hono();
  app.use(secureHeaders());


  // Handle all other requests by passing through to origin
  app.all('*', async (c) => {
    return fetch(c.req.raw);
  });


  export default app;
  ```