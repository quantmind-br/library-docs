---
title: Configuration · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/ci-cd/builds/configuration/index.md
source: llms
fetched_at: 2026-01-24T15:28:03.725973602-03:00
rendered_js: false
word_count: 1057
summary: This document explains how to configure build and deployment settings for Cloudflare Workers when integrated with a Git repository. it covers customizable parameters such as build commands, deployment scripts, root directories, and API tokens.
tags:
    - cloudflare-workers
    - build-settings
    - git-integration
    - deployment-configuration
    - wrangler
    - ci-cd
category: configuration
---

When connecting your Git repository to your Worker, you can customize the configurations needed to build and deploy your Worker.

## Build settings

Build settings can be found by navigating to **Settings** > **Build** within your Worker.

Note that when you update and save build settings, the updated settings will be applied to your *next* build. When you *retry* a build, the build configurations that exist when the build is retried will be applied.

### Overview

| Setting | Description |
| - | - |
| **Git account** | Select the Git account you would like to use. After the initial connection, you can continue to use this Git account for future projects. |
| **Git repository** | Choose the Git repository you would like to connect your Worker to. |
| **Git branch** | Select the branch you would like Cloudflare to listen to for new commits. This will be defaulted to `main`. |
| **Build command** *(Optional)* | Set a build command if your project requires a build step (e.g. `npm run build`). This is necessary, for example, when using a [front-end framework](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#framework-support) such as Next.js or Remix. |
| **[Deploy command](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#deploy-command)** | The deploy command lets you set the [specific Wrangler command](https://developers.cloudflare.com/workers/wrangler/commands/#deploy) used to deploy your Worker. Your deploy command will default to `npx wrangler deploy` but you may customize this command. Workers Builds will use the Wrangler version set in your `package json`. |
| **[Non-production branch deploy command](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#non-production-branch-deploy-command)** | Set a command to run when executing [a build for commit on a non-production branch](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds). This will default to `npx wrangler versions upload` but you may customize this command. Workers Builds will use the Wrangler version set in your `package json`. |
| **Root directory** *(Optional)* | Specify the path to your project. The root directory defines where the build command will be run and can be helpful in [monorepos](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#monorepos) to isolate a specific project within the repository for builds. |
| **[API token](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#api-token)** *(Optional)* | The API token is used to authenticate your build request and authorize the upload and deployment of your Worker to Cloudflare. By default, Cloudflare will automatically generate an API token for your account when using Workers Builds, and continue to use this API token for all subsequent builds. Alternatively, you can [create your own API token](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/authentication/#generate-tokens), or select one that you already own. |
| **Build variables and secrets** *(Optional)* | Add environment variables and secrets accessible only to your build. Build variables will not be accessible at runtime. If you would like to configure runtime variables you can do so in **Settings** > **Variables & Secrets** |

Note

Currently, Workers Builds does not honor the configurations set in [Custom Builds](https://developers.cloudflare.com/workers/wrangler/custom-builds/) within your wrangler.toml file.

### Deploy command

You can run your deploy command using the package manager of your choice.

If you have added a Wrangler deploy command as a script in your `package.json`, then you can run it by setting it as your deploy command. For example, `npm run deploy`.

Examples of other deploy commands you can set include:

| Example Command | Description |
| - | - |
| `npx wrangler deploy --assets ./public/` | Deploy your Worker along with static assets from the specified directory. Alternatively, you can use the [assets binding](https://developers.cloudflare.com/workers/static-assets/binding/). |
| `npx wrangler deploy --env staging` | If you have a [Wrangler environment](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#wrangler-environments) Worker, you should set your deploy command with the environment flag. For more details, see [Advanced Setups](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#wrangler-environments). |

### Non-production branch deploy command

The non-production branch deploy command is only applicable when you have enabled [non-production branch builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds).

It defaults to `npx wrangler versions upload`, producing a [preview URL](https://developers.cloudflare.com/workers/configuration/previews/). Like the build and deploy commands, it can be customized to instead run anything.

Examples of other non-production branch deploy commands you can set include:

| Example Command | Description |
| - | - |
| `yarn exec wrangler versions upload` | You can customize the package manager used to run Wrangler. |
| `npx wrangler versions upload --env staging` | If you have a [Wrangler environment](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#wrangler-environments) Worker, you should set your non-production branch deploy command with the environment flag. For more details, see [Advanced Setups](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#wrangler-environments). |

### API token

The API token in Workers Builds defines the access granted to Workers Builds for interacting with your account's resources. Currently, only user tokens are supported, with account-owned token support coming soon.

When you select **Create new token**, a new API token will be created automatically with the following permissions:

* **Account:** Account Settings (read), Workers Scripts (edit), Workers KV Storage (edit), Workers R2 Storage (edit)
* **Zone:** Workers Routes (edit) for all zones on the account
* **User:** User Details (read), Memberships (read)

You can configure the permissions of this API token by navigating to **My Profile** > **API Tokens** for user tokens.

It is recommended to consistently use the same API token across all uploads and deployments of your Worker to maintain consistent access permissions.

## Framework support

[Static assets](https://developers.cloudflare.com/workers/static-assets/) and [frameworks](https://developers.cloudflare.com/workers/framework-guides/) are now supported in Cloudflare Workers. Learn to set up Workers projects and the commands for each framework in the framework guides:

* [AI & agents](https://developers.cloudflare.com/workers/framework-guides/ai-and-agents/)

  * [Agents SDK](https://developers.cloudflare.com/agents/)
  * [LangChain](https://developers.cloudflare.com/workers/languages/python/packages/langchain/)

* [Web applications](https://developers.cloudflare.com/workers/framework-guides/web-apps/)

  * [React + Vite](https://developers.cloudflare.com/workers/framework-guides/web-apps/react/)

  * [Astro](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/)

  * [React Router (formerly Remix)](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/)

  * [Next.js](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/)

  * [Vue](https://developers.cloudflare.com/workers/framework-guides/web-apps/vue/)

  * [RedwoodSDK](https://developers.cloudflare.com/workers/framework-guides/web-apps/redwoodsdk/)

  * [TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/)

  * [SvelteKit](https://developers.cloudflare.com/workers/framework-guides/web-apps/sveltekit/)

  * [More guides...](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/)

    * [Analog](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/analog/)
    * [Angular](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/angular/)
    * [Docusaurus](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/docusaurus/)
    * [Gatsby](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/gatsby/)
    * [Hono](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/hono/)
    * [Nuxt](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/nuxt/)
    * [Qwik](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/qwik/)
    * [Solid](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/solid/)
    * [Waku](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/waku/)

* [Mobile applications](https://developers.cloudflare.com/workers/framework-guides/mobile-apps/)
  * [Expo](https://docs.expo.dev/eas/hosting/reference/worker-runtime/)

* [APIs](https://developers.cloudflare.com/workers/framework-guides/apis/)

  * [FastAPI](https://developers.cloudflare.com/workers/languages/python/packages/fastapi/)
  * [Hono](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/hono/)

## Environment variables

You can provide custom environment variables to your build.

* Dashboard

  To add environment variables via the dashboard:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

  [Go to **Workers & Pages**](https://dash.cloudflare.com/?to=/:account/workers-and-pages)

  1. In **Overview**, select your Worker.
  2. Select **Settings** > **Environment variables**.

* Wrangler

  To add env variables using Wrangler, define text and JSON via the `[vars]` configuration in your Wrangler file.

  * wrangler.jsonc

    ```jsonc
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "my-worker-dev",
      "vars": {
        "API_HOST": "example.com",
        "API_ACCOUNT_ID": "example_user",
        "SERVICE_X_DATA": {
          "URL": "service-x-api.dev.example",
          "MY_ID": 123
        }
      }
    }
    ```

  * wrangler.toml

    ```toml
    name = "my-worker-dev"


    [vars]
    API_HOST = "example.com"
    API_ACCOUNT_ID = "example_user"
    SERVICE_X_DATA = { URL = "service-x-api.dev.example", MY_ID = 123 }
    ```

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "name": "my-worker-dev",
    "vars": {
      "API_HOST": "example.com",
      "API_ACCOUNT_ID": "example_user",
      "SERVICE_X_DATA": {
        "URL": "service-x-api.dev.example",
        "MY_ID": 123
      }
    }
  }
  ```

* wrangler.toml

  ```toml
  name = "my-worker-dev"


  [vars]
  API_HOST = "example.com"
  API_ACCOUNT_ID = "example_user"
  SERVICE_X_DATA = { URL = "service-x-api.dev.example", MY_ID = 123 }
  ```

### Default variables

The following system environment variables are injected by default (but can be overridden):

| Environment Variable | Injected value | Example use-case |
| - | - | - |
| `CI` | `true` | Changing build behaviour when run on CI versus locally |
| `WORKERS_CI` | `1` | Changing build behaviour when run on Workers Builds versus locally |
| `WORKERS_CI_BUILD_UUID` | `<build-uuid-of-current-build>` | Passing the Build UUID along to custom workflows |
| `WORKERS_CI_COMMIT_SHA` | `<sha1-hash-of-current-commit>` | Passing current commit ID to error reporting, for example, Sentry |
| `WORKERS_CI_BRANCH` | `<branch-name-from-push-event` | Customizing build based on branch, for example, disabling debug logging on `production` |