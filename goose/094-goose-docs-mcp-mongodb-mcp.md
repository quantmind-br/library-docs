---
title: MongoDB Extension | goose
url: https://block.github.io/goose/docs/mcp/mongodb-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:28.040767064-03:00
rendered_js: true
word_count: 132
summary: This document explains how to integrate and use the MongoDB MCP Server extension with goose to manage databases and perform operations using natural language.
tags:
    - mongodb
    - mcp-server
    - goose
    - database-administration
    - natural-language-queries
category: guide
---

The [MongoDB MCP Server](https://github.com/mongodb-js/mongodb-mcp-server) extension allows goose to interact directly with your MongoDB databases, enabling comprehensive database operations including querying, document manipulation, collection management, and database administration. This makes it easy to work with your MongoDB databases through natural language interactions.

The MongoDB MCP server connects to a single MongoDB database instance using a connection string. The connection string must be specified using the `--connection-string` flag. We're using `mongodb://localhost:27017` as an example here to access a local MongoDB instance, but you can configure this for your own environment.

```
mongodb://username:password@hostname:27017/database
```

The MongoDB extension provides comprehensive database management capabilities through natural language interactions. You can perform a wide range of operations including:

Just describe what you want to accomplish in natural language, and goose will help you execute the appropriate MongoDB operations safely and efficiently.

```
Update all users in the premium tier who haven't logged in for more than 90 days - set their status to 'inactive' and add a note about when this change was made.
```

```
I've successfully updated inactive premium users using updateMany:

db.users.updateMany(
  {
    subscriptionTier: "premium",
    lastLogin: { $lt: new Date(Date.now() - 90 * 24 * 60 * 60 * 1000) }
  },
  {
    $set: {
      status: "inactive",
      inactiveNote: "Auto-updated to inactive on 2025-05-25 due to 90+ days of inactivity",
      lastModified: new Date()
    }
  }
)

Operation Result:
{
  acknowledged: true,
  matchedCount: 23,
  modifiedCount: 23,
  upsertedId: null,
  upsertedCount: 0
}

Updated 23 premium tier users who hadn't logged in since February 24, 2025. Each document now has:
• status: "inactive"
• inactiveNote: explains the automatic status change
• lastModified: timestamp of this operation

Consider sending re-engagement emails to these users or reviewing their subscription status.
```