---
title: Watch Paths | Dokploy
url: https://docs.dokploy.com/docs/core/watch-paths
source: crawler
fetched_at: 2026-02-14T14:18:11.622119-03:00
rendered_js: true
word_count: 287
summary: This document explains how to configure and use watch paths to automate deployments by monitoring specific files or directories for changes in standalone applications or Docker Compose.
tags:
    - watch-paths
    - auto-deploy
    - dokploy
    - glob-patterns
    - deployment-automation
    - git-integration
category: guide
---

Learn how to use watch paths in your application or docker compose.

Watch paths are a feature that allows you to monitor specific directories or files for changes and automatically trigger actions when modifications occur.

Watch paths functionality is available for both standalone applications and Docker Compose configurations. This feature helps automate deployments based on file changes in your repository.

The following source control providers are supported:

- GitHub
- GitLab
- Bitbucket
- Git (works with Bitbucket, Github, and GitLab repositories)

Let's say you have a project with the following directory structure:

```
my-app/	
├── src/	
│   ├── index.js	
├── public/	
```

By default, dokploy accepts an array of paths, allowing you to monitor multiple locations. For example:

- To trigger deployments when any file in the `src/` directory changes, use the pattern: `src/*`
- To monitor a specific file, simply specify its path: `src/index.js`

Watch Paths works out of the box with zero configuration when using GitHub as your provider. For other providers, you'll need to first set up auto-deploys as explained in:

- [Auto Deploy](https://docs.dokploy.com/docs/core/auto-deploy)
- [Bitbucket Integration](https://docs.dokploy.com/docs/core/bitbucket)
- [GitLab Integration](https://docs.dokploy.com/docs/core/gitlab)
- [GitHub Integration](https://docs.dokploy.com/docs/core/github)
- [Gitea Integration](https://docs.dokploy.com/docs/core/gitea)

Note: When using the Git provider, the functionality will only work with GitHub, GitLab, Bitbucket, or Gitea repositories.

We support a wide range of pattern matching features:

- Multiple glob patterns
- Wildcards:
  
  - `**` (matches any number of directories)
  - `*.js` (matches all JavaScript files)
- Negation patterns:
  
  - `!a/*.js` (excludes JavaScript files in directory 'a')
  - `*!(b).js` (matches all JavaScript files except those ending with 'b')
- Extended glob patterns:
  
  - `+(x|y)` (matches 'x' or 'y' one or more times)
  - `!(a|b)` (matches anything except 'a' or 'b')
- POSIX character classes:
  
  - `[[:alpha:][:digit:]]` (matches any letter or number)
- Brace expansion:
  
  - `foo/{1..5}.md` (matches foo/1.md through foo/5.md)
  - `bar/{a,b,c}.js` (matches bar/a.js, bar/b.js, bar/c.js)
- Regex character classes:
  
  - `foo-[1-5].js` (matches foo-1.js through foo-5.js)
- Regex logical "or":
  
  - `foo/(abc|xyz).js` (matches foo/abc.js or foo/xyz.js)

Normal