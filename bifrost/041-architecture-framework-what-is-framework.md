---
title: What is framework?
url: https://docs.getbifrost.ai/architecture/framework/what-is-framework.md
source: llms
fetched_at: 2026-01-21T19:41:13.096859879-03:00
rendered_js: false
word_count: 412
summary: This document introduces the Bifrost Framework, a shared SDK that provides standardized storage interfaces and utility modules like ConfigStore and VectorStore for plugin development. It explains how the framework ensures consistency, data integrity, and reduced development overhead across the Bifrost ecosystem.
tags:
    - sdk
    - bifrost-framework
    - plugin-development
    - data-storage
    - configuration-management
    - vector-store
    - go-programming
category: concept
---

# What is framework?

> Framework is Bifrost's shared storage and utilities SDK package that provides common database interfaces and logic for the plugin ecosystem.

Framework serves as the foundation layer that enables plugins to implement consistent data management patterns without reinventing storage solutions.

## Installation

```bash  theme={null}
go get github.com/maximhq/bifrost/framework
```

## Purpose

The framework package was designed to solve a fundamental challenge in plugin development: providing standardized, reliable storage and utility interfaces that plugins can depend on. Instead of each plugin implementing its own database logic, configuration management, or logging systems, framework offers battle-tested, shared implementations.

## Core Components

### ConfigStore

A unified configuration persistence layer that provides consistent storage patterns for plugin settings, provider configurations, and system state. Plugins can leverage `ConfigStore` to manage their configuration data with built-in CRUD operations, transaction support, and schema management.

### LogStore

Standardized logging and audit trail capabilities that enable plugins to implement observability features. `LogStore` provides structured logging, search and filtering capabilities, pagination support, and automated data retention policies.

### VectorStore

Vector database operations designed for AI-powered plugins that need semantic capabilities. `VectorStore` handles embeddings management, similarity search operations, and namespace isolation, making it easy for plugins to add features like semantic caching, content search, and AI-powered recommendations.

### Pricing Module

Cost calculation and model pricing management tools that help plugins implement billing and usage tracking features. The pricing system supports multi-tier pricing models, real-time usage tracking, and dynamic pricing updates.

## Benefits for Plugin Developers

**Shared Logic**: Common patterns for configuration, logging, and data management are provided out-of-the-box, reducing development time and ensuring consistency across plugins.

**Standardized Interfaces**: All framework components use consistent APIs, making it easier for developers to work across different plugins and maintain code quality.

**Pluggable Architecture**: The interface-based design allows different storage backends to be used without changing plugin code, providing flexibility for different deployment scenarios.

**Transaction Support**: Built-in transaction management and error handling ensure data integrity and provide reliable rollback capabilities.

**Production Ready**: Framework components are battle-tested in production environments and include features like connection pooling, retry logic, and performance optimizations.

## Integration with Bifrost

Framework seamlessly integrates with the Bifrost ecosystem, providing the storage foundation that powers core features like provider management, request logging, semantic caching, and governance. When plugins use framework components, they automatically participate in Bifrost's unified data management strategy.

The framework package enables plugin developers to focus on their core business logic while relying on robust, shared infrastructure for all storage and utility needs.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt