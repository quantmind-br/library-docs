---
title: DGOP | Dank Linux
url: https://danklinux.com/docs/dgop/
source: sitemap
fetched_at: 2026-01-24T13:36:09.751340813-03:00
rendered_js: false
word_count: 155
summary: This document introduces dgop, a stateless system and process monitoring tool that provides a terminal user interface, CLI, and REST API for sampling various system performance metrics.
tags:
    - system-monitoring
    - terminal-ui
    - process-management
    - rest-api
    - performance-metrics
    - linux-tools
category: guide
---

```
██████╗  ██████╗  ██████╗ ██████╗
██╔══██╗██╔════╝ ██╔═══██╗██╔══██╗
██║  ██║██║  ███╗██║   ██║██████╔╝
██║  ██║██║   ██║██║   ██║██╔═══╝
██████╔╝╚██████╔╝╚██████╔╝██║
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝
                                
```

`dgop` (Dank GO Process Status) is a stateless system and process monitoring tool that provides a top-like tui, CLI, and REST API. It allows sampling numerous metrics related to the system.

![DGOP Preview](https://danklinux.com/img/dgoplight.png)![DGOP Preview](https://danklinux.com/img/dgop.png)

dgop tui interface

## Features[​](#features "Direct link to Features")

- top-like TUI
- CPU, GPU, Memory, Process, Network, Disk, and other various metrics
- Cursor-based stateless method to sample data over any arbitrary time period.
- Fully documented with OpenAPI 3.1, REST API
- cli to query any metric, in human-readable or machine-readable formats
- mix and match different metrics under a single `meta` call

## Documentation[​](#documentation "Direct link to Documentation")

- [Installation](https://danklinux.com/docs/dgop/installation) - Detailed setup instructions and requirements
- [Configuration](https://danklinux.com/docs/dgop/configuration) - Configuration options
- [Usage](https://danklinux.com/docs/dgop/usage) - Learn CLI commands and API endpoints

## Contributing[​](#contributing "Direct link to Contributing")

`dgop` is open source and welcomes contributions:

- **Source Code**: [GitHub Repository](https://github.com/AvengeMedia/dgop)
- **Issues**: Report bugs and request features on GitHub
- **Documentation**: Help improve the documentation
- **Testing**: Test on different Linux distributions and hardware

## License[​](#license "Direct link to License")

`dgop` is released under the MIT License. See the [LICENSE](https://github.com/AvengeMedia/dgop/blob/master/LICENSE) file for details.