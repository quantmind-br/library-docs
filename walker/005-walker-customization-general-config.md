---
title: General Config | Walker
url: https://benz.gitbook.io/walker/customization/general-config
source: sitemap
fetched_at: 2026-02-01T13:48:31.877968163-03:00
rendered_js: false
word_count: 373
summary: This document explains how to configure and customize the behavior of Walker, including its configuration file location, various settings options, provider configurations, and emergency entry definitions.
tags:
    - configuration
    - customization
    - walker
    - settings
    - providers
    - keybinds
    - emergency-entries
category: configuration
---

You can customize how Walker behaves and interacts by adjusting it's configuration to your liking. Default path for configuration file is `~/.config/walker/config.toml`.

Have a look at the default configuration for a reference: [https://github.com/abenz1267/walker/blob/master/resources/config.tomlarrow-up-right](https://github.com/abenz1267/walker/blob/master/resources/config.toml)

force keyboard focus to stay in walker

invoking walker while it's already open will close it

clicking outside of the main walker box will close it

global\_argument\_delimiter

used to delimit arguments, f.e. `query#arg` means `arg` will be send as an argument to Elephant

can be used to tell Elephant to use exact search instead of fuzzy search

disables mouse-interaction with Walker, **except** for drag&drop from preview pane

hide the quick activation hints globally

hide the actions keybind hints

activate items with a single click

enables debug printing in order to print various info, f.e. available/implemented actions, currently pressed keybind

open walker with the last query in place

You can define how many columns the list for specific providers has without creating a new theme. F.e.

Placeholders for the input or empty list can be configured as such:

```
[placeholders]
"default" = { input = "Search", list = "No Results" }
"desktopapplications" = { input = "Start", list = "No Application" }
```

If the input placeholder is prefixed with `cmd:`, it will run the command and use the output as the placeholder.

`["desktopapplications", "calc", "runner", "menus", "websearch"]`

all providers that should be queried by default

all providers that should be queried when query is empty

all providers that should not display a preview.

global max amount of results

map, key: string, value: string

used to delimit arguments, f.e. `query#arg` means `arg` will be send as an argument to Elephant

Walker allows you to configure "sets" that you can launch, overwriting the configuration from above. Example:

```
[providers.sets.omarchy]
default = [
  "menus:omarchy",
  "menus:omarchylearn",
  "menus:omarchytrigger",
  "menus:omarchycapture",
]
empty = ["menus:omarchy"]
```

Running `walker -s omarchy` launches Walker with these specified providers. `default` sets the providers that will be queried, while `empty` defines which ones will display entries, without searching.

Walker allows you to define static "emergency entries" in case Elephant isn't connected. Example:

```
[[emergencies]]
text = "Firefox"
command = "firefox-developer-edition"
[[emergencies]]
text = "uuctl"
command = "uuctl"
```

Prefixes can be used to explicitly target a provider, f.e.

```
[[providers.prefixes]]
prefix = ">"
provider = "runner"
```

will allow you to explicitly query the `runner` provider.

#### Amount of displayed results

You can adjust the amount of displayed results per provider, f.e.

```
[providers.max_results_provider] # define max results per provider in here
desktopapplications = 10
```

will show at most 10 entries for the `desktopapplications` provider.

#### Provider-Specific Configuration

**Clipboard**

time format of the sub-text

The following global keybinds can be configured:

You can define multiple binds per actions, such as:

```
next = ["Down", "ctrl n", "ctrl j"]
```