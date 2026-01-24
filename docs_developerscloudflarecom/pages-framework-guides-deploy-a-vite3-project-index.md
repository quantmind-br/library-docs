---
title: Vite 3 · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/framework-guides/deploy-a-vite3-project/index.md
source: llms
fetched_at: 2026-01-24T15:17:47.601215104-03:00
rendered_js: false
word_count: 313
summary: This guide provides instructions on how to initialize a new Vite 3 project and deploy it to Cloudflare Pages via a GitHub repository. It covers local project creation, version control setup, and the build configuration process within the Cloudflare dashboard.
tags:
    - vite
    - cloudflare-pages
    - deployment
    - frontend-development
    - git-integration
    - vue
category: guide
---

[Vite](https://vitejs.dev) is a next-generation build tool for front-end developers. With [the release of Vite 3](https://vitejs.dev/blog/announcing-vite3.html), developers can make use of new command line (CLI) improvements, starter templates, and [more](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#300-2022-07-13) to help build their front-end applications.

Cloudflare Pages has native support for Vite 3 projects. Refer to the blog post on [improvements to the Pages build process](https://blog.cloudflare.com/cloudflare-pages-build-improvements/), including sub-second build initialization, for more information on using Vite 3 and Cloudflare Pages to optimize your application's build tooling.

In this guide, you will learn how to start a new project using Vite 3, and deploy it to Cloudflare Pages.

* npm

  ```sh
  npm create vite@latest
  ```

* yarn

  ```sh
  yarn create vite
  ```

* pnpm

  ```sh
  pnpm create vite@latest
  ```

```sh
✔ Project name: … vite-on-pages
✔ Select a framework: › vue
✔ Select a variant: › vue


Scaffolding project in ~/src/vite-on-pages...


Done. Now run:


  cd vite-on-pages
  npm install
  npm run dev
```

You will now create a new GitHub repository, and push your code using [GitHub's `gh` command line (CLI)](https://cli.github.com):

```sh
git init
```

```sh
Initialized empty Git repository in ~/vite-vue3-on-pages/.git/
```

```sh
git add .
git commit -m "Initial commit"                                           vite-vue3-on-pages/git/main +
```

```sh
[main (root-commit) dad4177] Initial commit
 14 files changed, 1452 insertions(+)
```

```sh
gh repo create
```

```sh
✓ Created repository kristianfreeman/vite-vue3-on-pages on GitHub
✓ Added remote git@github.com:kristianfreeman/vite-vue3-on-pages.git
```

```sh
git push
```

To deploy your site to Pages:

1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

   [Go to **Workers & Pages**](https://dash.cloudflare.com/?to=/:account/workers-and-pages)

2. Select **Create application** > **Pages** > **Import from an existing Git repository**.

3. Select your new GitHub repository.

4. In the **Set up builds and deployments**, set `npm run build` as the **Build command**, and `dist` as the **Build output directory**.

After completing configuration, select **Save and Deploy**.

You will see your first deploy pipeline in progress. Pages installs all dependencies and builds the project as specified. After you have deployed your project, it will be available at the `<YOUR_PROJECT_NAME>.pages.dev` subdomain. Find your project's subdomain in **Workers & Pages** > select your Pages project > **Deployments**.

Cloudflare Pages will automatically rebuild your project and deploy it on every new pushed commit.

Additionally, you will have access to [preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/), which repeat the build-and-deploy process for pull requests. With these, you can preview changes to your project with a real URL before deploying them to production.

## Learn more

By completing this guide, you have successfully deployed your Vite 3 site to Cloudflare Pages. To get started with other frameworks, [refer to the list of Framework guides](https://developers.cloudflare.com/pages/framework-guides/).