---
title: Alby Bitcoin Payments Extension | goose
url: https://block.github.io/goose/docs/mcp/alby-mcp
source: github_pages
fetched_at: 2026-01-22T22:14:37.554856677-03:00
rendered_js: true
word_count: 297
summary: This tutorial explains how to integrate and configure the Alby Bitcoin Payments MCP Server as an extension for the goose AI agent. It covers setting up NWC connections for both desktop and CLI environments to enable Lightning Network transactions.
tags:
    - bitcoin-lightning
    - alby
    - mcp-server
    - goose-extension
    - nwc
    - crypto-payments
category: tutorial
---

This tutorial covers how to add the [Alby Bitcoin Payments MCP Server](https://github.com/getalby/mcp) as a goose extension to interact with your lightning wallet, make and receive payments, list transactions, convert fiat amounts to sats, request invoices from lightning addresses, and interact with paid MCP tools (such as ones built with [PaidMCP](https://github.com/getAlby/paidmcp)).

info

You'll need a lightning wallet that supports [NWC](https://nwc.dev). If you don't have one yet, consider trying [Alby Hub](https://albyhub.com).

TLDR

- goose Desktop
- goose CLI

**Environment Variable**

```
NWC_CONNECTION_STRING: nostr+walletconnect://...
```

## Configuration[​](#configuration "Direct link to Configuration")

info

You'll need [Node.js](https://nodejs.org/) installed on your system to run this command, as it uses `npx`

**or** you can use the Alby-hosted MCP (see remote options below).

- goose Desktop
- goose CLI

<!--THE END-->

- Local
- Remote

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=npx&arg=-y&arg=%40getalby%2Fmcp&id=alby&name=Alby&description=Connect%20goose%20to%20your%20Bitcoin%20Lightning%20Wallet&env=NWC_CONNECTION_STRING%3DNWC%20Connection%20Secret)
2. Click `Yes` to confirm the installation
3. Obtain a NWC Connection secret from your lightning wallet (nostr+walletconnect://...) and paste it in to the 'NWC Connection Secret' field
4. Click `Add Extension`
5. Click the button in the top-left to open the sidebar
6. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

LLM

Claude Sonnet 3.7 was used for this task. A similarly capable model is recommended to ensure the tool is used correctly.

Memory Extension

Use the built-in memory extension to save your contacts. e.g. "My friend Rene's lightning address is [reneaaron@getalby.com](mailto:reneaaron@getalby.com). Please save it to your memory."

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

> *Pay Rene $1 USD, with message "Hi Rene, it's Roland. I'm making a goose tutorial!"*

### goose Output[​](#goose-output "Direct link to goose Output")

CLI

Tool Calls

✅ **Payment Successful!**

I've successfully sent $1 USD (935 sats) to Rene at `reneaaron@getalby.com` with your message: "Hi Rene, it's Roland. I'm making a goose tutorial!"

**Transaction Details:**

- Amount: 935 sats ($1 USD)
- Fees: 3 sats
- Total cost: 938 sats
- Message: "Hi Rene, it's Roland. I'm making a goose tutorial!"
- Payment hash: `cd30642470d81c2e8eb04c9ac95e679c53778537aecdf5554b15288ac42fe129`

Rene will receive the message "Thanks, sats received!" as confirmation of the payment.