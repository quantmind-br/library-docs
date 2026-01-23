---
title: "\U0001F680 Crawl4AI v0.7.2: CI/CD & Dependency Optimization Update"
url: https://docs.crawl4ai.com/blog/releases/0.7.2/
source: sitemap
fetched_at: 2026-01-22T22:22:39.714481971-03:00
rendered_js: false
word_count: 230
summary: This document outlines the updates in Crawl4AI version 0.7.2, specifically the implementation of automated CI/CD pipelines and the optimization of package dependencies for a lighter installation.
tags:
    - release-notes
    - cicd
    - github-actions
    - docker
    - dependency-management
    - crawl4ai
category: other
---

*July 25, 2025 • 3 min read*

* * *

This release introduces automated CI/CD pipelines for seamless releases and optimizes dependencies for a lighter, more efficient package.

## 🎯 What's New

### 🔄 Automated Release Pipeline

- **GitHub Actions CI/CD**: Automated PyPI and Docker Hub releases on tag push
- **Multi-platform Docker images**: Support for both AMD64 and ARM64 architectures
- **Version consistency checks**: Ensures tag, package, and Docker versions align
- **Automated release notes**: GitHub releases created automatically

### 📦 Dependency Optimization

- **Moved sentence-transformers to optional dependencies**: Significantly reduces default installation size
- **Lighter Docker images**: Optimized Dockerfile for faster builds and smaller images
- **Better dependency management**: Core vs. optional dependencies clearly separated

## 🏗️ CI/CD Pipeline

The new automated release process ensures consistent, reliable releases:

```
# Trigger releases with a simple tag
git tag v0.7.2
git push origin v0.7.2

# Automatically:
# ✅ Validates version consistency
# ✅ Builds and publishes to PyPI
# ✅ Builds multi-platform Docker images
# ✅ Pushes to Docker Hub with proper tags
# ✅ Creates GitHub release
```

## 💾 Lighter Installation

Default installation is now significantly smaller:

```
# Core installation (smaller, faster)
pipinstallcrawl4ai==0.7.2

# With ML features (includes sentence-transformers)
pipinstallcrawl4ai[transformer]==0.7.2

# Full installation
pipinstallcrawl4ai[all]==0.7.2
```

## 🐳 Docker Improvements

Enhanced Docker support with multi-platform images:

```
# Pull the latest version
dockerpullunclecode/crawl4ai:0.7.2
dockerpullunclecode/crawl4ai:latest

# Available tags:
# - unclecode/crawl4ai:0.7.2 (specific version)
# - unclecode/crawl4ai:0.7 (minor version)
# - unclecode/crawl4ai:0 (major version)
# - unclecode/crawl4ai:latest
```

## 🔧 Technical Details

### Dependency Changes

- `sentence-transformers` moved from required to optional dependencies
- Reduces default installation by ~500MB
- No impact on functionality when transformer features aren't needed

### CI/CD Configuration

- GitHub Actions workflows for automated releases
- Version validation before publishing
- Parallel PyPI and Docker Hub deployments
- Automatic tagging strategy for Docker images

## 🚀 Installation

```
pipinstallcrawl4ai==0.7.2
```

No breaking changes - direct upgrade from v0.7.0 or v0.7.1.

* * *

Questions? Issues? - GitHub: [github.com/unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) - Discord: [discord.gg/crawl4ai](https://discord.gg/jP8KfhDhyN) - Twitter: [@unclecode](https://x.com/unclecode)

*P.S. The new CI/CD pipeline will make future releases faster and more reliable. Thanks for your patience as we improve our release process!*