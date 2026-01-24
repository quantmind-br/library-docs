---
title: Static Assets · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/static-assets/
source: llms
fetched_at: 2026-01-24T15:28:22.054308867-03:00
rendered_js: false
word_count: 580
summary: This document explains how to host and manage static assets within Cloudflare Workers, covering deployment methods, routing logic, and automatic caching behavior.
tags:
    - cloudflare-workers
    - static-assets
    - wrangler-configuration
    - caching
    - routing
    - single-page-applications
category: guide
---

You can upload static assets (HTML, CSS, images and other files) as part of your Worker, and Cloudflare will handle caching and serving them to web browsers.

**Start from CLI** - Scaffold a React SPA with an API Worker, and use the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/).

- [npm](#tab-panel-3886)
- [yarn](#tab-panel-3887)
- [pnpm](#tab-panel-3888)

```

npmcreatecloudflare@latest--my-react-app--framework=react
```

* * *

**Or just deploy to Cloudflare**

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://dash.cloudflare.com/?to=%2F%3Aaccount%2Fworkers-and-pages%2Fcreate%2Fdeploy-to-workers&repository=https%3A%2F%2Fgithub.com%2Fcloudflare%2Ftemplates%2Ftree%2Fmain%2Fvite-react-template)

Learn more about supported frameworks on Workers.

### How it works

When you deploy your project, Cloudflare deploys both your Worker code and your static assets in a single operation. This deployment operates as a tightly integrated "unit" running across Cloudflare's network, combining static file hosting, custom logic, and global caching.

The **assets directory** specified in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/#assets) is central to this design. During deployment, Wrangler automatically uploads the files from this directory to Cloudflare's infrastructure. Once deployed, requests for these assets are routed efficiently to locations closest to your users.

- [wrangler.jsonc](#tab-panel-3891)
- [wrangler.toml](#tab-panel-3892)

```

{
"$schema":"./node_modules/wrangler/config-schema.json",
"name":"my-spa",
"main":"src/index.js",
"compatibility_date":"2025-01-01",
"assets":{
"directory":"./dist",
"binding":"ASSETS"
}
}
```

By adding an [**assets binding**](https://developers.cloudflare.com/workers/static-assets/binding/#binding), you can directly fetch and serve assets within your Worker code.

- [JavaScript](#tab-panel-3884)
- [Python](#tab-panel-3885)

```

// index.js
exportdefault{
asyncfetch(request,env){
consturl=newURL(request.url);
if (url.pathname.startsWith("/api/")) {
returnnewResponse(JSON.stringify({ name:"Cloudflare"}),{
headers:{"Content-Type":"application/json"},
});
}
returnenv.ASSETS.fetch(request);
},
};
```

### Routing behavior

By default, if a requested URL matches a file in the static assets directory, that file will be served — without invoking Worker code. If no matching asset is found and a Worker script is present, the request will be processed by the Worker. The Worker can return a response or choose to defer again to static assets by using the [assets binding](https://developers.cloudflare.com/workers/static-assets/binding/) (e.g. `env.ASSETS.fetch(request)`). If no Worker script is present, a `404 Not Found` response is returned.

The default behavior for requests which don't match a static asset can be changed by setting the [`not_found_handling` option under `assets`](https://developers.cloudflare.com/workers/wrangler/configuration/#assets) in your Wrangler configuration file:

- [`not_found_handling = "single-page-application"`](https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/): Sets your application to return a `200 OK` response with `index.html` for requests which don't match a static asset. Use this if you have a Single Page Application. We recommend pairing this with selective routing using `run_worker_first` for [advanced routing control](https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/#advanced-routing-control).
- [`not_found_handling = "404-page"`](https://developers.cloudflare.com/workers/static-assets/routing/static-site-generation/#custom-404-pages): Sets your application to return a `404 Not Found` response with the nearest `404.html` for requests which don't match a static asset.

<!--THE END-->

- [wrangler.jsonc](#tab-panel-3889)
- [wrangler.toml](#tab-panel-3890)

```

{
"$schema":"./node_modules/wrangler/config-schema.json",
"assets":{
"directory":"./dist",
"not_found_handling":"single-page-application"
}
}
```

If you want the Worker code to execute before serving assets, you can use the `run_worker_first` option. This can be set to `true` to invoke the Worker script for all requests, or configured as an array of route patterns for selective Worker-script-first routing:

**Invoking your Worker script on specific paths:**

- [wrangler.jsonc](#tab-panel-3893)
- [wrangler.toml](#tab-panel-3894)

```

{
"name":"my-spa-worker",
"compatibility_date":"2026-01-24",
"main":"./src/index.ts",
"assets":{
"directory":"./dist/",
"not_found_handling":"single-page-application",
"binding":"ASSETS",
"run_worker_first":["/api/*","!/api/docs/*"]
}
}
```

### Caching behavior

Cloudflare provides automatic caching for static assets across its network, ensuring fast delivery to users worldwide. When a static asset is requested, it is automatically cached for future requests.

- **First Request:** When an asset is requested for the first time, it is fetched from storage and cached at the nearest Cloudflare location.
- **Subsequent Requests:** If a request for the same asset reaches a data center that does not have it cached, Cloudflare's [tiered caching system](https://developers.cloudflare.com/cache/how-to/tiered-cache/) allows it to be retrieved from a nearby cache rather than going back to storage. This improves cache hit ratio, reduces latency, and reduces unnecessary origin fetches.

## Try it out

[Vite + React SPA tutorial](https://developers.cloudflare.com/workers/vite-plugin/tutorial/) Learn how to build and deploy a full-stack Single Page Application with static assets and API routes.

## Learn more

## Was this helpful?

- **Resources**
- [API](https://developers.cloudflare.com/api/)
- [New to Cloudflare?](https://developers.cloudflare.com/fundamentals/)
- [Directory](https://developers.cloudflare.com/directory/)
- [Sponsorships](https://developers.cloudflare.com/sponsorships/)
- [Open Source](https://github.com/cloudflare)

<!--THE END-->

- **Support**
- [Help Center](https://support.cloudflare.com/)
- [System Status](https://www.cloudflarestatus.com/)
- [Compliance](https://www.cloudflare.com/trust-hub/compliance-resources/)
- [GDPR](https://www.cloudflare.com/trust-hub/gdpr/)

<!--THE END-->

- **Company**
- [cloudflare.com](https://www.cloudflare.com/)
- [Our team](https://www.cloudflare.com/people/)
- [Careers](https://www.cloudflare.com/careers/)

<!--THE END-->

- **Tools**
- [Cloudflare Radar](https://radar.cloudflare.com/)
- [Speed Test](https://speed.cloudflare.com/)
- [Is BGP Safe Yet?](https://isbgpsafeyet.com/)
- [RPKI Toolkit](https://rpki.cloudflare.com/)
- [Certificate Transparency](https://ct.cloudflare.com/)

<!--THE END-->

- **Community**
- [X](https://x.com/cloudflare)
- [Discord](http://discord.cloudflare.com/)
- [YouTube](https://www.youtube.com/cloudflare)
- [GitHub](https://github.com/cloudflare/cloudflare-docs)