---
title: GraphQL · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/functions/plugins/graphql/index.md
source: llms
fetched_at: 2026-01-24T15:18:52.407791878-03:00
rendered_js: false
word_count: 70
summary: This document provides instructions on how to install and integrate the GraphQL Pages Plugin to create a GraphQL server within a Cloudflare Pages application.
tags:
    - cloudflare-pages
    - graphql
    - plugin
    - serverless
    - api-development
category: guide
---

The GraphQL Pages Plugin creates a GraphQL server which can respond to `application/json` and `application/graphql` `POST` requests. It responds with [the GraphQL Playground](https://github.com/graphql/graphql-playground) for `GET` requests.

## Installation

* npm

  ```sh
  npm i @cloudflare/pages-plugin-graphql
  ```

* yarn

  ```sh
  yarn add @cloudflare/pages-plugin-graphql
  ```

* pnpm

  ```sh
  pnpm add @cloudflare/pages-plugin-graphql
  ```

## Usage

```typescript
import graphQLPlugin from "@cloudflare/pages-plugin-graphql";
import {
  graphql,
  GraphQLSchema,
  GraphQLObjectType,
  GraphQLString,
} from "graphql";


const schema = new GraphQLSchema({
  query: new GraphQLObjectType({
    name: "RootQueryType",
    fields: {
      hello: {
        type: GraphQLString,
        resolve() {
          return "Hello, world!";
        },
      },
    },
  }),
});


export const onRequest: PagesFunction = graphQLPlugin({
  schema,
  graphql,
});
```

This Plugin only exposes a single route, so wherever it is mounted is wherever it will be available. In the above example, because it is mounted in `functions/graphql.ts`, the server will be available on `/graphql` of your Pages project.