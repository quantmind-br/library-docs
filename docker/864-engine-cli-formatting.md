---
title: Format command and log output
url: https://docs.docker.com/engine/cli/formatting/
source: llms
fetched_at: 2026-01-24T14:22:29.291182488-03:00
rendered_js: false
word_count: 253
summary: This document explains how to use Go templates and built-in formatting functions with Docker's --format flag to customize command output across different shell environments.
tags:
    - docker-cli
    - go-templates
    - output-formatting
    - docker-inspect
    - template-functions
category: reference
---

Docker supports [Go templates](https://golang.org/pkg/text/template/) which you can use to manipulate the output format of certain commands and log drivers.

Docker provides a set of basic functions to manipulate template elements. All of these examples use the `docker inspect` command, but many other CLI commands have a `--format` flag, and many of the CLI command references include examples of customizing the output format.

When using the `--format` flag, you need to observe your shell environment. In a POSIX shell, you can run the following with a single quote:

Otherwise, in a Windows shell (for example, PowerShell), you need to use single quotes, but escape the double quotes inside the parameters as follows:

`join` concatenates a list of strings to create a single string. It puts a separator between each element in the list.

`table` specifies which fields you want to see its output.

`json` encodes an element as a json string.

`lower` transforms a string into its lowercase representation.

`split` slices a string into a list of strings separated by a separator.

`title` capitalizes the first character of a string.

`upper` transforms a string into its uppercase representation.

`pad` adds whitespace padding to a string. You can specify the number of spaces to add before and after the string.

`truncate` shortens a string to a specified length. If the string is shorter than the specified length, it remains unchanged.

This example displays the image repository name, truncating it to the first 15 characters if it's longer.

`println` prints each value on a new line.