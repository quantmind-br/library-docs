---
title: Migrating from Firebase · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/migrations/migrating-from-firebase/index.md
source: llms
fetched_at: 2026-01-24T15:18:11.375101013-03:00
rendered_js: false
word_count: 305
summary: This tutorial provides a step-by-step guide on migrating an existing Firebase application to Cloudflare Pages, covering build configuration, repository setup, and domain management.
tags:
    - firebase
    - cloudflare-pages
    - migration
    - web-hosting
    - deployment
    - dns
category: tutorial
---

In this tutorial, you will learn how to migrate an existing Firebase application to Cloudflare Pages. You should already have an existing project deployed on Firebase that you would like to host on Cloudflare Pages.

## Finding your build command and build directory

To move your application to Cloudflare Pages, you will need to find your build command and build directory.

You will use these to tell Cloudflare Pages how to deploy your project. If you have been deploying manually from your local machine using the `firebase` command-line tool, the `firebase.json` configuration file should include a `public` key that will be your build directory:

```json
{
  "public": "public"
}
```

Firebase Hosting does not ask for your build command, so if you are running a standard JavaScript set up, you will probably be using `npm build` or a command specific to the framework or tool you are using (for example, `ng build`).

After you have found your build directory and build command, you can move your project to Cloudflare Pages.

## Creating a new Pages project

If you have not pushed your static site to GitHub before, you should do so before continuing. This will also give you access to features like automatic deployments, and [deployment previews](https://developers.cloudflare.com/pages/configuration/preview-deployments/).

You can create a new repository by visiting [repo.new](https://repo.new) and following the instructions to push your project up to GitHub.

Use the [Get started guide](https://developers.cloudflare.com/pages/get-started/) to add your project to Cloudflare Pages, using the **build command** and **build directory** that you saved earlier.

## Cleaning up your old application and assigning the domain

Once you have deployed your application, go to the Firebase dashboard and remove your old Firebase project. In your Cloudflare DNS settings for your domain, make sure to update the CNAME record for your domain from Firebase to Cloudflare Pages.

By completing this guide, you have successfully migrated your Firebase project to Cloudflare Pages.