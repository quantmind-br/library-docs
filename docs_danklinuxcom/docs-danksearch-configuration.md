---
title: Configuration | Dank Linux
url: https://danklinux.com/docs/danksearch/configuration
source: sitemap
fetched_at: 2026-01-24T13:33:56.61019961-03:00
rendered_js: false
word_count: 413
summary: This document details the TOML configuration options for DankSearch, covering global settings, indexing behaviors, and directory-specific inclusion rules. It explains how to manage index paths, exclude files, and optimize search performance through configuration settings.
tags:
    - danksearch
    - toml-configuration
    - indexing-settings
    - file-search
    - performance-optimization
    - directory-exclusion
category: configuration
---

```
██████╗ ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██║  ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
██║  ██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██████╔╝███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                      
```

`dsearch` uses a TOML configuration file to control indexing behavior. The first time you run DankSearch, it creates a default config file at `~/.config/danksearch/config.toml`.

## Configuration File Location[​](#configuration-file-location "Direct link to Configuration File Location")

Default paths:

- Linux/macOS/BSD: `~/.config/danksearch/config.toml`

Override with the `-c` flag:

```
dsearch -c /path/to/config.toml
```

## Basic Settings[​](#basic-settings "Direct link to Basic Settings")

### `index_path`[​](#index_path "Direct link to index_path")

Where DankSearch stores the index database.

**Default:**

- Linux/macOS/BSD: `~/.cache/danksearch/index`

### `listen_addr`[​](#listen_addr "Direct link to listen_addr")

HTTP server address and port.

**Default:** `:43654`

### `max_file_bytes`[​](#max_file_bytes "Direct link to max_file_bytes")

Maximum file size to index (in bytes). Larger files are skipped.

**Default:** `2097152` (2MB)

```
max_file_bytes=2097152# 2MB
```

### `worker_count`[​](#worker_count "Direct link to worker_count")

Number of parallel indexing workers. More workers = faster indexing but higher CPU usage during index operations.

**Default:** Half your CPU cores (minimum 1)

### `index_all_files`[​](#index_all_files "Direct link to index_all_files")

Index all file types, not just text files. When enabled, binary files are indexed by filename only.

**Default:** `true`

### `auto_reindex`[​](#auto_reindex "Direct link to auto_reindex")

Automatically re-index on startup if the interval has passed.

**Default:** `false`

### `reindex_interval_hours`[​](#reindex_interval_hours "Direct link to reindex_interval_hours")

How often to re-index (in hours). Set to `0` to disable periodic re-indexing.

**Default:** `24`

```
reindex_interval_hours=24
```

### `text_extensions`[​](#text_extensions "Direct link to text_extensions")

File extensions to extract text content from. Other files are indexed by filename only.

**Default:**

```
text_extensions=[
".txt",".md",".go",".py",".js",".ts",
".jsx",".tsx",".json",".yaml",".yml",
".toml",".html",".css",".rs",".c",
".cpp",".h",".java",".rb",".php",".sh",
]
```

## Index Paths[​](#index-paths "Direct link to Index Paths")

Index multiple directories with individual settings using `[[index_paths]]` blocks. Each path can have its own depth limit and exclusion rules.

### Basic Example[​](#basic-example "Direct link to Basic Example")

```
[[index_paths]]
path="/home/brandon"
max_depth=6
exclude_hidden=true
exclude_dirs=["node_modules","venv","target"]
```

### Configuration Options[​](#configuration-options "Direct link to Configuration Options")

#### `path`[​](#path "Direct link to path")

Directory to index.

#### `max_depth`[​](#max_depth "Direct link to max_depth")

Maximum directory depth to traverse. Set to `0` for unlimited depth.

**Example:**

```
max_depth=6# Go 6 levels deep
max_depth=0# No limit
```

#### `exclude_hidden`[​](#exclude_hidden "Direct link to exclude_hidden")

Skip hidden files and directories (starting with `.`).

**Default:** `true`

#### `watch`[​](#watch "Direct link to watch")

Enable or disable inotify file watchers for this path. When disabled, the path is indexed but changes won't be detected automatically.

**Default:** `true`

```
watch=false# Disable watchers (useful for network mounts)
```

#### `exclude_dirs`[​](#exclude_dirs "Direct link to exclude_dirs")

List of directory names to skip during indexing.

**Default excludes:**

```
exclude_dirs=[
# JavaScript/Node.js
"node_modules","bower_components",".npm",".yarn",

# Python
"site-packages","__pycache__",".venv","venv",".tox",
".pytest_cache",".eggs",

# Build outputs
"dist","build","out","bin","obj",

# Rust
"target",

# Go
"vendor",

# Java/JVM
".gradle",".m2",

# Ruby
"bundle",

# Cache directories
".cache",".parcel-cache",".next",".nuxt",

# OS specific
"Library",".Trash-1000",

# Databases
".postgresql",".mysql",".mongodb",".redis",

# Package manager caches
"go",".cargo",".pyenv",".rbenv",".nvm",".rustup",

# IDE/Editor
".idea",".vscode",
]
```

## Multiple Index Paths[​](#multiple-index-paths "Direct link to Multiple Index Paths")

Configure different indexing strategies for different directories:

```
# Index home with moderate depth
[[index_paths]]
path="/home/brandon"
max_depth=6
exclude_hidden=true
exclude_dirs=["node_modules","venv","target","dist"]

# Index repos with more depth, exclude VCS
[[index_paths]]
path="/home/brandon/repos"
max_depth=8
exclude_hidden=true
exclude_dirs=["node_modules","venv","target",".git"]

# Index documents fully, including hidden files
[[index_paths]]
path="/home/brandon/Documents"
max_depth=0# No limit
exclude_hidden=false
exclude_dirs=[]

# Index network mount without watchers
[[index_paths]]
path="/mnt/nfs/documents"
max_depth=5
watch=false# Disable inotify (not supported on NFS)
```

## Example Configuration[​](#example-configuration "Direct link to Example Configuration")

Here's a complete example config:

```
# DankSearch Configuration
index_path="/home/brandon/.cache/danksearch/index"
listen_addr=":43654"
max_file_bytes=2097152# 2MB
worker_count=4
index_all_files=true
auto_reindex=false
reindex_interval_hours=24

text_extensions=[
".txt",".md",".go",".py",".js",".ts",
".jsx",".tsx",".json",".yaml",".yml",
".toml",".html",".css",".rs",".c",
".cpp",".h",".java",".rb",".php",".sh",
]

[[index_paths]]
path="/home/brandon"
max_depth=6
exclude_hidden=true
exclude_dirs=[
"node_modules","__pycache__","venv","target",
"dist","build",".cache"
]
```

## Tips[​](#tips "Direct link to Tips")

**Speed up indexing:** Increase `worker_count` if you have CPU cores to spare.

**Reduce index size:** Lower `max_file_bytes`, add more directories to `exclude_dirs`, or limit `max_depth`.

**Index everything:** Set `max_depth = 0` and `exclude_dirs = []` for a path you want fully indexed.

**Skip binary files:** Set `index_all_files = false` to index only text files.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

**Indexing is slow:**

- Check `worker_count` - try increasing it
- Add common build/cache directories to `exclude_dirs`
- Reduce `max_depth` for large directory trees

**Search isn't finding files:**

- Run `dsearch index generate` to rebuild the index
- Check if the file's directory is in an `index_paths` block
- Verify the file isn't in an excluded directory
- Check that `exclude_hidden = false` if searching for hidden files

**Port already in use:**

- Change `listen_addr` to a different port
- Check what's using the port: `netstat -tlnp | grep :43654`

## Next Steps[​](#next-steps "Direct link to Next Steps")

- [Usage](https://danklinux.com/docs/danksearch/usage) - Learn CLI commands and API usage