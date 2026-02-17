---
title: Jekyll
url: https://coolify.io/docs/applications/jekyll.md
source: llms
fetched_at: 2026-02-17T14:38:53.951566-03:00
rendered_js: false
word_count: 91
summary: This document explains how to deploy a Jekyll static site generator application using Nixpacks or a multi-stage Dockerfile configuration.
tags:
    - jekyll
    - static-site-generator
    - deployment
    - nixpacks
    - docker
    - dockerfile
    - ruby
    - nginx
category: guide
---

# Jekyll

Jekyll is a simple, blog-aware, static site generator for personal, project, or organization sites.

## Deploy with Nixpacks

Nixpacks needs a few prerequisites in your source code to deploy your Jekyll application. More info [here](https://nixpacks.com/docs/providers/ruby).

## Deploy with Dockerfile

If you want simplicity, you can use a Dockerfile to deploy your Jekyll application.

### Prerequisites

1. Set `Ports Exposes` field to `80`.
2. Create a `Dockerfile` in the root of your project with the following content:

```Dockerfile
FROM ruby:3.1.1 AS builder
RUN apt-get update -qq && apt-get install -y build-essential nodejs
WORKDIR /srv/jekyll
COPY Gemfile Gemfile.lock ./
RUN bundle install
COPY . .
RUN chown 1000:1000 -R /srv/jekyll
RUN bundle exec jekyll build -d /srv/jekyll/_site

FROM nginx:alpine
COPY --from=builder /srv/jekyll/_site /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

3. Make sure you have a `Gemfile` and `Gemfile.lock` in the root of your project.
4. Set the buildpack to `Dockerfile`.