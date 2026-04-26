---
title: Dependency Injection | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/dependency_injection
source: sitemap
fetched_at: 2026-04-26T04:13:41.375904948-03:00
rendered_js: false
word_count: 325
summary: This document explains how to utilize dependency injection in workflows to manage, share, and lifecycle-optimize resources like database connections and API clients.
tags:
    - dependency-injection
    - workflow-management
    - resource-pooling
    - software-architecture
    - lifecycle-management
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Dependency injection provides a clean way to access shared resources in your workflows and activities. It automatically handles creation and management of resources like database connections, API clients, or configuration objects.

## Supported Provider Types

| Type | Use Case |
|------|----------|
| Synchronous functions | Simple configuration values or in-memory objects |
| Asynchronous functions | I/O-bound dependencies like database connections |
| Context managers | Resources requiring cleanup operations |
| Generators | Streaming data or complex resource management |

## Lifecycle

All dependencies defined with `Depends()` are initialized once when the worker starts up and then shared across all activity executions:

- **Single Instance**: The same instance is reused for every activity call
- **Resource Efficiency**: Reduces connection overhead and resource consumption
- **Connection Pooling**: Database connections, API clients, and other resources are maintained and reused

This approach is particularly beneficial for:
- **Database connections**: Avoids creating new connections for each query
- **API clients**: Maintains persistent connections and authentication
- **Configuration objects**: Loads configuration once and shares it across all activities

## Provider Examples

For simple configuration values or objects that don't require async initialization:

```python
```

For dependencies that require async initialization, like database connections:

```python
```

### Context Manager Provider

For resources that need proper cleanup, like sessions that require logout:

```python
Async Context Manager Provider
```

### Async Context Manager Provider

For async resources that need cleanup, like database connections:

```python
```

### Generator Provider

For streaming data or complex resource management:

```python
For async streaming data sources:
```

## Usage in Activities

Activities declare their dependencies using the `Depends()` marker. The system automatically provides these dependencies when the activity executes:

```python
```

A more complete database connection example with proper session management:

```python
```

Example of a payment service client with initialization:

```python
```