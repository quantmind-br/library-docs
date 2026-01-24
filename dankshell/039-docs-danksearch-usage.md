---
title: Usage | Dank Linux
url: https://danklinux.com/docs/danksearch/usage
source: sitemap
fetched_at: 2026-01-24T13:36:08.145574602-03:00
rendered_js: false
word_count: 501
summary: This document explains how to use the dsearch CLI and HTTP API to index and search filesystems with advanced filters like file size, extensions, and EXIF metadata. It details index management commands, search parameters, and output formatting for command-line and programmatic usage.
tags:
    - dsearch
    - filesystem-search
    - cli-reference
    - api-usage
    - index-management
    - search-filters
    - exif-metadata
category: guide
---

```
██████╗ ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██║  ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
██║  ██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██████╔╝███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                      
```

`dsearch` provides both a CLI and HTTP API for searching your filesystem. The API follows OpenAPI 3.1 specification with full documentation available at the `/docs` endpoint.

## API Usage[​](#api-usage "Direct link to API Usage")

The `dsearch` API provides a documentation endpoint with a full OpenAPI 3.1 specification available at `http://localhost:43654/docs`.

It's guaranteed to be up to date, so it's the best way to reference API usage.

## CLI Usage[​](#cli-usage "Direct link to CLI Usage")

DankSearch provides a command-line interface for managing the search index and querying files.

### Starting the Server[​](#starting-the-server "Direct link to Starting the Server")

Run the HTTP API server:

```
# Start server on default port (43654)
dsearch serve

# Access OpenAPI documentation at http://localhost:43654/docs
```

The server runs the search API and file watcher for real-time index updates.

### Basic Search[​](#basic-search "Direct link to Basic Search")

Search for files using the `search` command:

```
# Basic search - searches filename and content
dsearch search "config"

# Limit results
dsearch search "README"--limit5

# Search all results (no limit)
dsearch search "TODO"--limit0
```

### Search Filters[​](#search-filters "Direct link to Search Filters")

#### File Extension[​](#file-extension "Direct link to File Extension")

Filter by file extension:

```
# Find all Python files
dsearch search "main"--ext .py

# Find all markdown files
dsearch search "documentation"--ext .md

# Find JavaScript/TypeScript files
dsearch search "component"--ext .tsx
```

#### File Size[​](#file-size "Direct link to File Size")

Filter by file size (in bytes):

```
# Files larger than 1MB (1048576 bytes)
dsearch search "video" --min-size 1048576

# Files smaller than 100KB (102400 bytes)
dsearch search "config" --max-size 102400

# Files between 10KB and 500KB
dsearch search "log" --min-size 10240 --max-size 512000
```

#### Field-Specific Search[​](#field-specific-search "Direct link to Field-Specific Search")

Search in specific fields:

```
# Search only filenames
dsearch search "config"--field filename

# Search only file content
dsearch search "TODO"--field body

# Search titles (for supported file types)
dsearch search "introduction"--field title

# Search EXIF metadata in images
dsearch search "mountain"--field body
```

#### Virtual Folder Search[​](#virtual-folder-search "Direct link to Virtual Folder Search")

Search within specific directories:

```
# Search all files in a specific folder
dsearch search "*"--folder /home/user/Pictures

# Combine with other filters
dsearch search "vacation"--folder /home/user/Photos --ext .jpg
```

### Fuzzy Matching[​](#fuzzy-matching "Direct link to Fuzzy Matching")

Enable fuzzy matching for typo tolerance:

```
# Find files even with typos
dsearch search "confing"--fuzzy

# Works with other filters
dsearch search "readne"--fuzzy--ext .md
```

### Sorting Results[​](#sorting-results "Direct link to Sorting Results")

Sort results by different criteria:

```
# Sort by relevance score (default)
dsearch search "config"--sort score

# Sort by modification time (newest first)
dsearch search "log"--sort mtime

# Sort by file size
dsearch search "image"--sort size --ext .jpg

# Sort by filename
dsearch search "test"--sort filename

# Sort ascending instead of descending
dsearch search "config"--sort mtime --desc=false
```

### Output Formats[​](#output-formats "Direct link to Output Formats")

#### JSON Output[​](#json-output "Direct link to JSON Output")

Get results in JSON format for scripting:

```
# JSON output
dsearch search "config"--json

# Pipe to jq for parsing
dsearch search "README"--json| jq '.[].path'

# Get file paths only
dsearch search "*.go"--json| jq -r'.[].path'
```

#### Human-Readable Output[​](#human-readable-output "Direct link to Human-Readable Output")

Default output shows key information in a readable format:

```
# Standard output format
dsearch search "main"
```

## Index Management[​](#index-management "Direct link to Index Management")

### Initial Indexing[​](#initial-indexing "Direct link to Initial Indexing")

Generate the initial index:

```
# Start indexing (runs asynchronously)
dsearch index generate
```

This crawls all configured paths and builds the search index. Large directories may take time.

### Index Status[​](#index-status "Direct link to Index Status")

Check index statistics:

```
# View index stats
dsearch index status

# Example output:
# Total Files: 15,432
# Total Bytes: 2.3 GB
# Last Index: 2025-10-28 14:30:00
# Duration: 45s
```

### Incremental Sync[​](#incremental-sync "Direct link to Incremental Sync")

Update the index with new/modified files:

```
# Sync changes
dsearch index sync
```

This is faster than a full reindex - it only processes changes since the last sync.

### File Watcher[​](#file-watcher "Direct link to File Watcher")

The file watcher automatically updates the index when files change:

```
# Start watching (usually runs with serve)
dsearch watch

# Check watcher status
dsearch watch status
```

When running `dsearch serve`, the watcher starts automatically.

## Common Use Cases[​](#common-use-cases "Direct link to Common Use Cases")

### Find Recent Changes[​](#find-recent-changes "Direct link to Find Recent Changes")

```
# Recently modified files, sorted by time
dsearch search ""--sort mtime --limit20
```

### Find Large Files[​](#find-large-files "Direct link to Find Large Files")

```
# Files over 10MB
dsearch search "" --min-size 10485760--sort size
```

### Search Code[​](#search-code "Direct link to Search Code")

```
# Find function definitions in Go files
dsearch search "func main"--ext .go --field body

# Find TODOs in source code
dsearch search "TODO"--fuzzy
```

### Find Documents[​](#find-documents "Direct link to Find Documents")

```
# All markdown documentation
dsearch search ""--ext .md --sort filename

# PDFs with "report" in filename
dsearch search "report"--ext .pdf --field filename
```

### Search Photos by EXIF Metadata[​](#search-photos-by-exif-metadata "Direct link to Search Photos by EXIF Metadata")

DankSearch can filter and search photos using EXIF metadata extracted from images.

#### Camera Make and Model[​](#camera-make-and-model "Direct link to Camera Make and Model")

```
# Find all photos from Canon cameras
dsearch search "*"--ext .jpg --exif-make Canon

# Find photos from a specific camera model
dsearch search "*" --exif-model "Canon EOS 5D"

# Combine with folder search
dsearch search "*"--folder /home/user/Photos --exif-make Nikon
```

#### Sort by Date Taken[​](#sort-by-date-taken "Direct link to Sort by Date Taken")

```
# Sort photos by date taken (newest first)
dsearch search "*"--ext .jpg --sort exif_date --desc

# Sort oldest first
dsearch search "*"--ext .jpg --sort exif_date --desc=false
```

#### Camera Settings[​](#camera-settings "Direct link to Camera Settings")

```
# Find low-light shots (high ISO range)
dsearch search "*" --exif-min-iso 1600 --exif-max-iso 6400

# Find portrait shots (typical focal length range)
dsearch search "*" --exif-min-focal-len 50 --exif-max-focal-len 135

# Find wide aperture shots (shallow depth of field)
dsearch search "*" --exif-min-aperture 1.4 --exif-max-aperture 2.8
```

#### Date Range[​](#date-range "Direct link to Date Range")

```
# Photos taken in a specific date range
dsearch search "*" --exif-date-after "2024-06-01T00:00:00Z" --exif-date-before "2024-08-31T23:59:59Z"

# Summer vacation photos from a specific location
dsearch search "vacation"--folder /home/user/Photos/2024 \
  --exif-date-after "2024-06-01T00:00:00Z"\
  --exif-date-before "2024-08-31T23:59:59Z"
```

#### GPS Location[​](#gps-location "Direct link to GPS Location")

```
# GPS location filtering (bounding box)
# Example: Photos taken in New York City area
dsearch search "*" --exif-lat-min 40.0 --exif-lat-max 41.0\
  --exif-lon-min -74.0 --exif-lon-max -73.0

# Combine location with camera settings
dsearch search "*" --exif-lat-min 40.7 --exif-lat-max 40.8\
  --exif-lon-min -74.0 --exif-lon-max -73.9\
  --exif-make Canon --sort exif_date
```

## Configuration File[​](#configuration-file "Direct link to Configuration File")

Override the default config location:

```
# Use custom config
dsearch -c /path/to/config.toml search "query"

# Works with all commands
dsearch -c ./dev-config.toml serve
```

## Global Flags[​](#global-flags "Direct link to Global Flags")

All commands support:

- `-c, --config` - Path to config file (default: `~/.config/danksearch/config.toml`)
- `-h, --help` - Show help for any command

## Version Information[​](#version-information "Direct link to Version Information")

Check the version:

## Performance Tips[​](#performance-tips "Direct link to Performance Tips")

**Faster searches:**

- Use `--field filename` to skip content matching
- Add `--ext` filters to narrow results
- Keep `--limit` reasonable for large result sets
- Use `--folder` to restrict search scope to specific directories
- Combine EXIF filters to narrow photo searches efficiently

**Efficient indexing:**

- Use `index sync` instead of `generate` for updates
- Configure `exclude_dirs` to skip unnecessary directories
- Adjust `worker_count` in config based on CPU cores

**Photo searches:**

- Use `--folder` to limit searches to photo directories
- Combine `--ext .jpg` with EXIF filters for better performance
- Use `--sort exif_date` for chronological photo browsing

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

**Search returns no results:**

- Run `dsearch index status` to check if indexing is complete
- Try `dsearch index generate` to rebuild the index
- Verify the file is in a configured `index_paths` directory

**Indexing is slow:**

- Check `worker_count` in config - increase if you have CPU cores available
- Add large directories to `exclude_dirs` (e.g., `node_modules`, `.git`)
- Reduce `max_depth` for deep directory trees

**Server won't start:**

- Check if port 43654 is available: `netstat -tlnp | grep :43654`
- Change `listen_addr` in config to use a different port
- Check logs for permission errors