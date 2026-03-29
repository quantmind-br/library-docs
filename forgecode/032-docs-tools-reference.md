---
title: ForgeCode
url: https://forgecode.dev/docs/tools-reference/
source: sitemap
fetched_at: 2026-03-29T14:52:25.789657183-03:00
rendered_js: false
word_count: 267
summary: This document provides a comprehensive reference for built-in tools that enable AI agents to interact with the system, including file operations, data processing, and communication capabilities.
tags:
    - ai-agents
    - file-operations
    - data-processing
    - tool-reference
    - api-tools
category: reference
---

ForgeCode provides a comprehensive set of built-in tools that enable AI agents to interact with your system, manage files, process data, and communicate with users. This reference documents all available tools and their parameters.

> **Note:** These tools are used internally by ForgeCode's AI agents and are not meant to be directly called by developers. This reference is provided for understanding what capabilities agents have access to within your system.

### read[​](#read "Direct link to read")

Reads file contents at a specified path.

#### Parameters[​](#parameters "Direct link to Parameters")

ParameterTypeRequiredDescription`path`stringYesAbsolute path to the file

### write[​](#write "Direct link to write")

Creates or overwrites a file with specified content.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

ParameterTypeRequiredDescription`path`stringYesAbsolute path to the file`content`stringYesContent to write to the file`overwrite`booleanNoWhether to overwrite if file exists (default: false)

### patch[​](#patch "Direct link to patch")

Modifies files with targeted text operations on matched patterns.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

ParameterTypeRequiredDescription`path`stringYesAbsolute path to the file`patches`arrayYesList of patch operations to apply

#### Patch Operations[​](#patch-operations "Direct link to Patch Operations")

OperationDescription`prepend`Add content before the matched text`append`Add content after the matched text`replace`Replace the matched text with new content`swap`Exchange the matched text with another text

### remove[​](#remove "Direct link to remove")

Removes a file at a specified path.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

ParameterTypeRequiredDescription`path`stringYesAbsolute path to the file

### search[​](#search "Direct link to search")

Searches for text patterns across files using regex.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

ParameterTypeRequiredDescription`path`stringYesDirectory to search in (recursively)`regex`stringYesRegular expression pattern to search for`file_pattern`stringNoGlob pattern to filter files (e.g., "\*.js")

### undo[​](#undo "Direct link to undo")

Reverts the most recent file operation on a specific file.

#### Parameters[​](#parameters-5 "Direct link to Parameters")

ParameterTypeRequiredDescription`path`stringYesAbsolute path of the file to revert

### fetch[​](#fetch "Direct link to fetch")

Retrieves content from URLs as markdown or raw text.

#### Parameters[​](#parameters-6 "Direct link to Parameters")

ParameterTypeRequiredDescription`url`stringYesURL to fetch content from`raw`booleanNoWhether to return raw content instead of markdown (default: false)`max_length`numberNoMaximum characters to return (default: 40000)`start_index`numberNoStarting character index for pagination (default: 0)

### shell[​](#shell "Direct link to shell")

Executes shell commands with safety measures.

#### Parameters[​](#parameters-7 "Direct link to Parameters")

ParameterTypeRequiredDescription`command`stringYesShell command to execute`cwd`stringYesWorking directory for command execution