---
title: 'Interface: ExecStreamOptions'
url: https://docs.docker.com/reference/api/extensions-sdk/ExecStreamOptions/
source: llms
fetched_at: 2026-01-24T14:31:18.115038306-03:00
rendered_js: false
word_count: 194
summary: This document defines the interface for handling command execution events, including output processing, error reporting, and process termination callbacks.
tags:
    - process-execution
    - event-handling
    - stdout-stderr
    - callback-functions
    - api-reference
category: reference
---

Table of contents

* * *

**`Since`**

0.2.2

## [Properties](#properties)

### [onOutput](#onoutput)

• `Optional` **onOutput**: (`data`: { `stdout`: `string` ; `stderr?`: `undefined` } | { `stdout?`: `undefined` ; `stderr`: `string` }) =&gt; `void`

#### [Type declaration](#type-declaration)

▸ (`data`): `void`

Invoked when receiving output from command execution. By default, the output is split into chunks at arbitrary boundaries. If you prefer the output to be split into complete lines, set `splitOutputLines` to true. The callback is then invoked once for each line.

**`Since`**

0.2.0

##### [Parameters](#parameters)

NameTypeDescription`data``{ stdout: string; stderr?: undefined } | { stdout?: undefined; stderr: string }`Output content. Can include either stdout string, or stderr string, one at a time.

##### [Returns](#returns)

`void`

* * *

### [onError](#onerror)

• `Optional` **onError**: (`error`: `any`) =&gt; `void`

#### [Type declaration](#type-declaration-1)

▸ (`error`): `void`

Invoked to report error if the executed command errors.

##### [Parameters](#parameters-1)

NameTypeDescription`error``any`The error happening in the executed command

##### [Returns](#returns-1)

`void`

* * *

### [onClose](#onclose)

• `Optional` **onClose**: (`exitCode`: `number`) =&gt; `void`

#### [Type declaration](#type-declaration-2)

▸ (`exitCode`): `void`

Invoked when process exits.

##### [Parameters](#parameters-2)

NameTypeDescription`exitCode``number`The process exit code

##### [Returns](#returns-2)

`void`

* * *

### [splitOutputLines](#splitoutputlines)

• `Optional` `Readonly` **splitOutputLines**: `boolean`

Specifies the behaviour invoking `onOutput(data)`. Raw output by default, splitting output at any position. If set to true, `onOutput` will be invoked once for each line.