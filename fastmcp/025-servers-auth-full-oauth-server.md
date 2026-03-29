---
title: Full OAuth Server - FastMCP
url: https://gofastmcp.com/servers/auth/full-oauth-server
source: crawler
fetched_at: 2026-01-22T22:23:04.703047315-03:00
rendered_js: false
word_count: 129
summary: This document explains how to implement a Full OAuth Server pattern in FastMCP by subclassing the OAuthProvider class to handle the complete authentication lifecycle.
tags:
    - fastmcp
    - oauth-server
    - authentication
    - authorization
    - oauth-2-1
    - security
category: guide
---

New in version `2.11.0`

The Full OAuth Server pattern exists to support the MCP protocol specification’s requirements. Your FastMCP server becomes both an Authorization Server and Resource Server, handling the complete authentication lifecycle from user login to token validation. This documentation exists for completeness - the vast majority of applications should use external identity providers instead.

## OAuthProvider

FastMCP provides the `OAuthProvider` abstract class that implements the OAuth 2.1 specification. To use this pattern, you must subclass `OAuthProvider` and implement all required abstract methods.

## Required Implementation

You must implement these abstract methods to create a functioning OAuth server:

### Client Management

### Token Management

Each method must handle storage, validation, security, and error cases according to the OAuth 2.1 specification. The implementation complexity is substantial and requires expertise in OAuth security considerations.