---
title: AeroSpace Commands
url: https://nikitabobko.github.io/AeroSpace/commands
source: github_pages
fetched_at: 2026-02-08T11:27:16.741958978-03:00
rendered_js: false
word_count: 1738
summary: This document provides a technical reference for AeroSpace CLI query commands used to inspect the current state of configurations, applications, monitors, and windows.
tags:
    - aerospace
    - cli-commands
    - window-management
    - macos
    - querying
    - system-state
category: reference
---

Query commands are commands that do not change the state but rather allow the examination of the current state.

- Query commands are **NOT** available in config  
  (because there is no way to consume the stdout of these commands in config)
- Query commands are only available in CLI

### [](#config)[30.1. config](#config)

```
config [-h|--help] --get <name> [--json] [--keys]
config [-h|--help] --major-keys
config [-h|--help] --all-keys
config [-h|--help] --config-path
```

Query AeroSpace config options

For now, only `mode.*` config options are supported

Under the hood, the config is represented as recursive data structure of maps, arrays, strings, and integers.

Printing without `--json` or `--keys` flag is supported only for scalar types (strings and integers) and array of scalar types. Printing other complicated objects requires `--json` or `--keys` flag.

**OPTIONS**

-h, --help

Print help

--get &lt;name&gt;

Get the value for a given key. You can inspect available keys with `--major-keys` or `--all-keys`

--major-keys

Print major keys

--all-keys

Print all available keys recursively

--json

Print result in JSON format

--keys

Print keys of the complicated object (map or array)

--config-path

Print absolute path to the loaded config

**EXAMPLES**

- List all binding modes:
  
  ```
  $ aerospace config --get mode --keys
  main
  service
  ```
- List all key bindings for 'main' binding mode:
  
  ```
  $ aerospace config --get mode.main.binding --keys
  alt-1
  alt-2
  ...
  ```
- List all key bindings for 'main' binding mode in JSON format:
  
  ```
  $ aerospace config --get mode.main.binding --json
  {
    "alt-w" : "workspace W",
    "alt-y" : "workspace Y",
    "alt-n" : "workspace N",
    "alt-shift-e" : "move-node-to-workspace E",
    "alt-shift-m" : "move-node-to-workspace M",
    "alt-shift-t" : "move-node-to-workspace T",
  ...
  ```

### [](#debug-windows)[30.2. debug-windows](#debug-windows)

```
debug-windows [-h|--help] [--window-id <window-id>]
```

Interactive command to record Accessibility API debug information to create bug reports

Use this command output to report bug reports about incorrect windows handling (e.g. some windows are floated when they shouldn’t).

The intended usage is the following:

1. Run the command to start the debug session recording
2. Focus problematic window or make the window appear.
3. Run the command one more time to stop the debug session recording and print the results

`debug-windows` command is **not stable API**. Please **don’t rely on** the command existence and output format. The only intended use case is to report bugs about incorrect windows handling.

**OPTIONS**

-h, --help

Print help

--window-id &lt;window-id&gt;

Print debug information of the specified window right away. Usage of this flag disables interactive mode.

### [](#list-apps)[30.3. list-apps](#list-apps)

```
list-apps [-h|--help] [--macos-native-hidden [no]] [--format <output-format>] [--count] [--json]
```

Print the list of running applications that appears in the Dock and may have a user interface

**OPTIONS**

-h, --help

Print help

--macos-native-hidden \[no]

Filter results to only print hidden applications. `[no]` inverts the condition

--format &lt;output-format&gt;

Specify output format. See "Output Format" section for more details. Incompatible with `--count`

--count

Output only the number of apps. Incompatible with: `--format`, `--json`

--json

Output in JSON format. Can be used in combination with `--format` to specify which data to include into the json. Incompatible with `--count`

**OUTPUT FORMAT**

Output format can be configured with optional `[--format <output-format>]` option. `<output-format>` supports [string interpolation](https://en.wikipedia.org/wiki/String_interpolation).

If not specified, the default `<output-format>` is:  
`%{app-pid}%{right-padding} | %{app-bundle-id}%{right-padding} | %{app-name}`

The following variables can be used inside `<output-format>`:

%{app-bundle-id}

String. Application unique identifier. [Bundle ID](https://developer.apple.com/documentation/appstoreconnectapi/bundle_ids)

%{app-name}

String. Application name

%{app-pid}

Number. [UNIX process identifier](https://en.wikipedia.org/wiki/Process_identifier)

%{app-exec-path}

String. Application executable path

%{app-bundle-path}

String. Application bundle path

%{right-padding}

A special variable which expands with a minimum number of spaces required to form a right padding in the appropriate column

%{newline}

Unicode U+000A newline symbol `\n`

%{tab}

Unicode U+0009 tab symbol `\t`

### [](#list-exec-env-vars)[30.4. list-exec-env-vars](#list-exec-env-vars)

```
list-exec-env-vars [-h|--help]
```

List environment variables that exec-* commands and callbacks are run with

Examples of commands and callbacks:

- `aerospace exec-and-forget` command
- `exec-on-workspace-change-callback`

### [](#list-modes)[30.5. list-modes](#list-modes)

```
list-modes [-h|--help] [--current] [--count] [--json]
```

Print a list of modes currently specified in the configuration

See [the guide](https://nikitabobko.github.io/AeroSpace/guide#binding-modes) for documentation about binding modes

**OPTIONS**

-h, --help

Print help

--current

Only print the currently active mode. Incompatible with `--count`

--count

Output only the number of modes. Incompatible with `--current`, `--json`

--json

Output in JSON format. Incompatible with `--count`

### [](#list-monitors)[30.6. list-monitors](#list-monitors)

```
list-monitors [-h|--help] [--focused [no]] [--mouse [no]] [--format <output-format>] [--count] [--json]
```

Print monitors that satisfy conditions

**OPTIONS**

-h, --help

Print help

--focused \[no]

Filter results to only print the focused monitor. `[no]` inverts the condition

--mouse \[no]

Filter results to only print the monitor with the mouse. `[no]` inverts the condition

--format &lt;output-format&gt;

Specify output format. See "Output Format" section for more details. Incompatible with `--count`

--count

Output only the number of monitors. Incompatible with `--format`

--json

Output in JSON format. Can be used in combination with `--format` to specify which data to include into the json. Incompatible with `--count`

**OUTPUT FORMAT**

Output format can be configured with optional `[--format <output-format>]` option. `<output-format>` supports [string interpolation](https://en.wikipedia.org/wiki/String_interpolation).

If not specified, the default `<output-format>` is:  
`%{monitor-id}%{right-padding} | %{monitor-name}`

The following variables can be used inside `<output-format>`:

%{monitor-id}

1-based Number. Sequential number of the belonging monitor

%{monitor-appkit-nsscreen-screens-id}

1-based index of the belonging monitor in `NSScreen.screens` array. Useful for integration with other tools that might be using `NSScreen.screens` ordering (like sketchybar).

%{monitor-name}

String. Name of the belonging monitor

%{monitor-is-main}

Boolean. True if the monitor is main.

%{right-padding}

A special variable which expands with a minimum number of spaces required to form a right padding in the appropriate column

%{newline}

Unicode U+000A newline symbol `\n`

%{tab}

Unicode U+0009 tab symbol `\t`

### [](#list-windows)[30.7. list-windows](#list-windows)

```
list-windows [-h|--help] (--workspace <workspace>...|--monitor <monitor>...)
             [--monitor <monitor>...] [--workspace <workspace>...]
             [--pid <pid>] [--app-bundle-id <app-bundle-id>] [--format <output-format>]
             [--count] [--json]
list-windows [-h|--help] --all [--format <output-format>] [--count] [--json]
list-windows [-h|--help] --focused [--format <output-format>] [--count] [--json]
```

Print windows that satisfy conditions

**OPTIONS**

-h, --help

Print help

--all

Alias for `--monitor all`. Please use this option **with caution**. Use it when you really need to get workspaces/windows from **all monitors**.

For multi-monitor setup `--monitor focused` is almost always a preferred option. If you’re automating something then you don’t want to mess up with workspaces/windows on a different monitor.

With great power comes great responsibility.

--focused

Print the focused window. Please note that it is possible for no window to be in focus. In that case, error is reported.

--workspace &lt;workspace&gt;…​

Filter results to only print windows that belong to either of specified workspaces. `<workspace>…​` is a space-separated list of workspace names.

Possible values:

1. Workspace name
2. `focused` is a special workspace name that represents the focused workspace
3. `visible` is a special workspace name that represents all currently visible workspaces (In multi-monitor setup, there are multiple visible workspaces)

--monitor &lt;monitors&gt;

Filter results to only print workspaces/windows that are attached to specified monitors. `<monitors>` is a space separated list of monitor IDs.

Possible monitors IDs:

1. 1-based index of a monitor as if monitors were ordered horizontally from left to right
2. `all` is a special monitor ID that represents all monitors
3. `mouse` is a special monitor ID that represents monitor with the mouse
4. `focused` is a special monitor ID that represents the focused monitor

--pid &lt;pid&gt;

Filter results to only print windows that belong to the Application with specified `<pid>`

--app-bundle-id &lt;app-bundle-id&gt;

Filter results to only print windows that belong to the Application with specified [Bundle ID](https://developer.apple.com/documentation/appstoreconnectapi/bundle_ids)

Deprecated (but still supported) flag name: `--app-id`

--format &lt;output-format&gt;

Specify output format. See "Output Format" section for more details. Incompatible with `--count`

--count

Output only the number of windows. Incompatible with `--format`

--json

Output in JSON format. Can be used in combination with `--format` to specify which data to include into the json. Incompatible with `--count`

**OUTPUT FORMAT**

Output format can be configured with optional `[--format <output-format>]` option. `<output-format>` supports [string interpolation](https://en.wikipedia.org/wiki/String_interpolation).

If not specified, the default `<output-format>` is:  
`%{window-id}%{right-padding} | %{app-name}%{right-padding} | %{window-title}`

The following variables can be used inside `<output-format>`:

%{window-id}

Number. Window unique ID

%{window-title}

String. Window title

%{window-is-fullscreen}

Boolean. Is window in fullscreen by `aerospace fullscreen` command

%{window-layout}

String. Alias for `%{window-parent-container-layout}`

%{window-parent-container-layout}

String. The layout (`v_tiles`, `h_tiles`, `v_accordion`, `h_accordion`, `floating`) of the window’s parent container.

%{app-bundle-id}

String. Application unique identifier. [Bundle ID](https://developer.apple.com/documentation/appstoreconnectapi/bundle_ids)

%{app-name}

String. Application name

%{app-pid}

Number. [UNIX process identifier](https://en.wikipedia.org/wiki/Process_identifier)

%{app-exec-path}

String. Application executable path

%{app-bundle-path}

String. Application bundle path

%{workspace}

String. Name of the belonging workspace

%{workspace-is-focused}

Boolean. True if the workspace has focus

%{workspace-is-visible}

Boolean. True if the workspace is visible. A workspace can be visible but not focused in a multi-monitor setup

%{workspace-root-container-layout}

String. The layout (`v_tiles`, `h_tiles`, `v_accordion`, `h_accordion`) of the workspace the window belongs to.

%{monitor-id}

1-based Number. Sequential number of the belonging monitor.

%{monitor-appkit-nsscreen-screens-id}

1-based index of the belonging monitor in `NSScreen.screens` array. Useful for integration with other tools that might be using `NSScreen.screens` ordering (like sketchybar).

%{monitor-name}

String. Name of the belonging monitor

%{monitor-is-main}

Boolean. True if the monitor is main.

%{right-padding}

A special variable which expands with a minimum number of spaces required to form a right padding in the appropriate column

%{newline}

Unicode U+000A newline symbol `\n`

%{tab}

Unicode U+0009 tab symbol `\t`

### [](#list-workspaces)[30.8. list-workspaces](#list-workspaces)

```
list-workspaces [-h|--help] --monitor <monitor>... [--visible [no]] [--empty [no]] [--format <output-format>] [--count] [--json]
list-workspaces [-h|--help] --all [--format <output-format>] [--count] [--json]
list-workspaces [-h|--help] --focused [--format <output-format>] [--count] [--json]
```

Print workspaces that satisfy conditions

**OPTIONS**

-h, --help

Print help

--format &lt;output-format&gt;

Specify output format. See "Output Format" section for more details

--all

Alias for `--monitor all`. Please use this option **with caution**. Use it when you really need to get workspaces/windows from **all monitors**.

For multi-monitor setup `--monitor focused` is almost always a preferred option. If you’re automating something then you don’t want to mess up with workspaces/windows on a different monitor.

With great power comes great responsibility.

--focused

Alias for `--monitor focused --visible`. Always prints a single workspace

--monitor &lt;monitors&gt;

Filter results to only print workspaces/windows that are attached to specified monitors. `<monitors>` is a space separated list of monitor IDs.

Possible monitors IDs:

1. 1-based index of a monitor as if monitors were ordered horizontally from left to right
2. `all` is a special monitor ID that represents all monitors
3. `mouse` is a special monitor ID that represents monitor with the mouse
4. `focused` is a special monitor ID that represents the focused monitor

--visible \[no]

Filter results to only print currently visible workspaces. `[no]` inverts the condition. Several workspaces can be visible in multi-monitor setup

--empty \[no]

Filter results to only print empty workspaces. `[no]` inverts the condition.

--format &lt;output-format&gt;

Specify output format. See "Output Format" section for more details. Incompatible with `--count`

--count

Output only the number of workspaces. Incompatible with `--format`

--json

Output in JSON format. Can be used in combination with `--format` to specify which data to include into the json. Incompatible with `--count`

**OUTPUT FORMAT**

Output format can be configured with optional `[--format <output-format>]` option. `<output-format>` supports [string interpolation](https://en.wikipedia.org/wiki/String_interpolation).

If not specified, the default `<output-format>` is:  
`%{workspace}`

The following variables can be used inside `<output-format>`:

%{workspace}

String. Name of the belonging workspace

%{workspace-is-focused}

Boolean. True if the workspace has focus

%{workspace-is-visible}

Boolean. True if the workspace is visible. A workspace can be visible but not focused in a multi-monitor setup

%{workspace-root-container-layout}

String. The layout (`v_tiles`, `h_tiles`, `v_accordion`, `h_accordion`) of the workspace’s root container

%{monitor-id}

1-based Number. Sequential number of the belonging monitor

%{monitor-appkit-nsscreen-screens-id}

1-based Number. Sequential number of the belonging monitor in `NSScreen.screens`. Useful for integration with other tools that might be using `NSScreen.screens` ordering (like sketchybar).

%{monitor-name}

String. Name of the belonging monitor

%{monitor-is-main}

Boolean. True if the monitor is main.

%{right-padding}

A special variable which expands with a minimum number of spaces required to form a right padding in the appropriate column

%{newline}

Unicode U+000A newline symbol `\n`

%{tab}

Unicode U+0009 tab symbol `\t`