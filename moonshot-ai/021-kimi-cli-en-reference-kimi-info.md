---
title: ""
url: https://moonshotai.github.io/kimi-cli/en/reference/kimi-info.md
source: github_pages
fetched_at: 2026-01-28T07:56:09.947442039-03:00
rendered_js: false
word_count: 119
summary: This document provides a reference for the 'kimi info' subcommand, which displays version, protocol, and runtime information for the Kimi Code CLI.
tags:
    - kimi-cli
    - cli-reference
    - version-info
    - system-metadata
    - command-line
category: reference
---

--- url: /kimi-cli/en/reference/kimi-info.md --- # \`kimi info\` Subcommand \`kimi info\` displays version and protocol information for Kimi Code CLI. \`\`\`sh kimi info \[--json] \`\`\` ## Options | Option | Description | |--------|-------------| | \`--json\` | Output in JSON format | ## Output | Field | Description | |-------|-------------| | \`kimi\_cli\_version\` | Kimi Code CLI version number | | \`agent\_spec\_versions\` | List of supported agent spec versions | | \`wire\_protocol\_version\` | Wire protocol version | | \`python\_version\` | Python runtime version | ## Examples \*\*Text output\** \`\`\`sh $ kimi info kimi-cli version: 0.71 agent spec versions: 1 wire protocol: 1 python version: 3.14.0 \`\`\` \*\*JSON output\** \`\`\`sh $ kimi info --json {"kimi\_cli\_version": "0.71", "agent\_spec\_versions": \["1"], "wire\_protocol\_version": "1", "python\_version": "3.13.1"} \`\`\`