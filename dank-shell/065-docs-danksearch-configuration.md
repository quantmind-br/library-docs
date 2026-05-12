---
title: Configuration | Dank Linux
url: https://danklinux.com/docs/danksearch/configuration
source: sitemap
fetched_at: 2026-04-26T08:39:23.479874093-03:00
rendered_js: false
word_count: 450
summary: This document provides a comprehensive guide to configuring DankSearch, explaining how to manage index paths, performance settings, and directory exclusions using a TOML configuration file.
tags:
    - dsearch
    - configuration
    - indexing
    - toml
    - search-engine
    - system-settings
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# DankSearch Configuration

`dsearch` uses a TOML configuration file to control indexing behavior. On first run, it creates a default config at `~/.config/danksearch/config.toml`.

## Configuration File Location

| Platform | Path |
|---|---|
| Linux/macOS/BSD | `~/.config/danksearch/config.toml` |

Override with `-c`:

```bash
dsearch -c /path/to/config.toml
```

## Basic Settings

### `index_path`

Where DankSearch stores the index database.

**Default:** `~/.cache/danksearch/index` (Linux/macOS/BSD)

### `listen_addr`

HTTP server address and port.

**Default:** `:43654`

### `max_file_bytes`

Maximum file size to index (bytes). Larger files are skipped.

**Default:** `2097152` (2MB)

```toml
max_file_bytes = 2097152  # 2MB
```

### `worker_count`

Number of parallel indexing workers. More workers = faster indexing but higher CPU usage.

**Default:** Half your CPU cores (minimum 1)

### `index_all_files`

Index all file types, not just text files. Binary files are indexed by filename only.

**Default:** `true`

### `auto_reindex`

Automatically re-index on startup if the interval has passed.

**Default:** `false`

### `reindex_interval_hours`

How often to re-index (hours). Set `0` to disable periodic re-indexing.

**Default:** `24`

```toml
reindex_interval_hours = 24
```

### `text_extensions`

File extensions to extract text content from. Other files are indexed by filename only.

**Default:**

```toml
text_extensions = [
    ".txt", ".md", ".go", ".py", ".js", ".ts",
    ".jsx", ".tsx", ".json", ".yaml", ".yml",
    ".toml", ".html", ".css", ".rs", ".c",
    ".cpp", ".h", ".java", ".rb", ".php", ".sh",
]
```

## Index Paths

Index multiple directories with individual settings using `[[index_paths]]` blocks.

### Basic Example

```toml
[[index_paths]]
path = "/home/brandon"
max_depth = 6
exclude_hidden = true
exclude_dirs = ["node_modules", "venv", "target"]
```

### Configuration Options

| Option | Type | Default | Description |
|---|---|---|---|
| `path` | string | — | Directory to index |
| `max_depth` | integer | — | Maximum directory depth (0 = unlimited) |
| `exclude_hidden` | boolean | `true` | Skip hidden files/directories (starting with `.`) |
| `watch` | boolean | `true` | Enable inotify watchers for this path |
| `exclude_dirs` | array | — | Directory names to skip (exact match or regex) |

#### `exclude_dirs` Patterns

Supports exact names and regex patterns wrapped in `/` delimiters (e.g., `/^build-/`). Each pattern is matched against individual directory name components, not the full path. Invalid regex patterns are skipped with a warning.

```toml
exclude_dirs = [
    "node_modules",                        # Exact match
    "/^build-/",                            # Regex: excludes build-release, build-debug, etc.
    "/^out-\\d+$/",                         # Regex: excludes out-123, out-0, but not "output"
]
```

**Default excludes:**

```toml
exclude_dirs = [
    # JavaScript/Node.js
    "node_modules", "bower_components", ".npm", ".yarn",
    # Python
    "site-packages", "__pycache__", ".venv", "venv", ".tox", ".pytest_cache", ".eggs",
    # Build outputs
    "dist", "build", "out", "bin", "obj",
    # Rust
    "target",
    # Go
    "vendor",
    # Java/JVM
    ".gradle", ".m2",
    # Ruby
    "bundle",
    # Cache directories
    ".cache", ".parcel-cache", ".next", ".nuxt",
    # OS specific
    "Library", ".Trash-1000",
    # Databases
    ".postgresql", ".mysql", ".mongodb", ".redis",
    # Package manager caches
    "go", ".cargo", ".pyenv", ".rbenv", ".nvm", ".rustup",
    # IDE/Editor
    ".idea", ".vscode",
]
```

## Multiple Index Paths

Configure different indexing strategies for different directories:

```toml
# Index home with moderate depth
[[index_paths]]
path = "/home/brandon"
max_depth = 6
exclude_hidden = true
exclude_dirs = ["node_modules", "venv", "target", "dist"]

# Index repos with more depth, exclude VCS
[[index_paths]]
path = "/home/brandon/repos"
max_depth = 8
exclude_hidden = true
exclude_dirs = ["node_modules", "venv", "target", ".git"]

# Index documents fully, including hidden files
[[index_paths]]
path = "/home/brandon/Documents"
max_depth = 0            # No limit
exclude_hidden = false
exclude_dirs = []

# Index network mount without watchers
[[index_paths]]
path = "/mnt/nfs/documents"
max_depth = 5
watch = false             # Disable inotify (not supported on NFS)
```

## Example Configuration

```toml
# DankSearch Configuration
index_path = "/home/brandon/.cache/danksearch/index"
listen_addr = ":43654"
max_file_bytes = 2097152  # 2MB
worker_count = 4
index_all_files = true
auto_reindex = false
reindex_interval_hours = 24

text_extensions = [
    ".txt", ".md", ".go", ".py", ".js", ".ts",
    ".jsx", ".tsx", ".json", ".yaml", ".yml",
    ".toml", ".html", ".css", ".rs", ".c",
    ".cpp", ".h", ".java", ".rb", ".php", ".sh",
]

[[index_paths]]
path = "/home/brandon"
max_depth = 6
exclude_hidden = true
exclude_dirs = [
    "node_modules", "__pycache__", "venv", "target",
    "dist", "build", ".cache"
]
```

## Tips

- **Speed up indexing:** Increase `worker_count` if you have CPU cores to spare
- **Reduce index size:** Lower `max_file_bytes`, add more directories to `exclude_dirs`, or limit `max_depth`
- **Index everything:** Set `max_depth = 0` and `exclude_dirs = []` for a path
- **Skip binary files:** Set `index_all_files = false` to index only text files

## Troubleshooting

| Problem | Solution |
|---|---|
| Indexing is slow | Increase `worker_count`; add common build/cache directories to `exclude_dirs`; reduce `max_depth` for large directory trees |
| Search isn't finding files | Run `dsearch index generate` to rebuild; check file's directory is in an `index_paths` block; verify file isn't in an excluded directory; check `exclude_hidden = false` for hidden files |
| Port already in use | Change `listen_addr` to a different port; check what's using the port: `netstat -tlnp \| grep :43654` |

## Next Steps

See [[026-docs-danksearch-usage|DankSearch Usage]] for CLI commands and API usage.

#dsearch #indexing #toml #search-engine
