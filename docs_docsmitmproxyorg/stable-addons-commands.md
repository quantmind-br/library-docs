---
title: Custom Commands
url: https://docs.mitmproxy.org/stable/addons/commands/
source: crawler
fetched_at: 2026-01-28T15:59:11.934623923-03:00
rendered_js: false
word_count: 592
summary: This document explains how to create and use custom commands in mitmproxy addons, including defining commands with decorators, specifying argument types, and working with flow selectors.
tags:
    - mitmproxy
    - addons
    - commands
    - flow-handling
    - api-reference
    - keybindings
    - type-checking
category: reference
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/addons/commands.md)

Commands allow users to actively interact with addons - querying their state, commanding them to perform actions, and having them transform data. Like [options](https://docs.mitmproxy.org/stable/addons/options/), commands are typed, and both invocations and data returned from commands are checked at runtime. Commands are a very powerful construct - for instance, all user interaction in mitmproxy console are built by binding commands to keys.

## Simple example

Let’s begin with a simple example.

```
"""Add a custom command to mitmproxy's command prompt."""
import logging
from mitmproxy import command
class MyAddon:
    def __init__(self):
        self.num = 0
    @command.command("myaddon.inc")
    def inc(self) -> None:
        self.num += 1
        logging.info(f"num = {self.num}")
addons = [MyAddon()]
```

examples/addons/commands-simple.py

To see this example in action, start mitmproxy console with the addon loaded:

```
> mitmproxy -s ./examples/addons/commands-simple.py
```

Now, make sure the event log is showing, and then execute the command at the prompt (started by typing “:”):

```
:myaddon.inc
```

Notice that tab completion works - our addon command has complete parity with builtin commands. There are a few things to note about this example:

- Commands are declared through the `command.command` decorator. Each command has a unique name - by convention, we use period-separated names, with the name of the addon as a prefix.
- Annotating commands with types is mandatory, including the return type (in this case `None`). This allows mitmproxy to support addon commands throughout its toolset - runtime invocations are type checked, addon commands are included in the built-in help, the command editor in mitmproxy console can perform sophisticated completion and error checking, and so forth.

## Working with flows

Since command arguments are typed, we can provide special conveniences for working with certain important data types. The most useful of these are the `Flows` classes that represent mitmproxy traffic.

Consider the following addon:

```
"""Handle flows as command arguments."""
import logging
from collections.abc import Sequence
from mitmproxy import command
from mitmproxy import flow
from mitmproxy import http
from mitmproxy.log import ALERT
class MyAddon:
    @command.command("myaddon.addheader")
    def addheader(self, flows: Sequence[flow.Flow]) -> None:
        for f in flows:
            if isinstance(f, http.HTTPFlow):
                f.request.headers["myheader"] = "value"
        logging.log(ALERT, "done")
addons = [MyAddon()]
```

examples/addons/commands-flows.py

The `myaddon.addheader` command is quite simple: it takes a sequence of flows, and adds a header to every request. The really interesting aspect of this example is how users specify flows. Because mitmproxy can inspect the type signature, it can expand a text flow selector into a sequence of flows for us transparently. This means that the user has the full flexibility of [flow filters](https://docs.mitmproxy.org/stable/concepts/filters/) available. Let’s try it out.

Start by loading the addon into mitmproxy and sending some traffic through so we have flows to work with:

```
> mitmproxy -s ./examples/addons/commands-flows.py
```

We can now invoke our toy command in various ways. Let’s begin by running it just on the currently focused flow:

```
:myaddon.addheader @focus
```

We can also invoke it on all flows:

```
:myaddon.addheader @all
```

Or only flows from **google.com**:

```
:myaddon.addheader ~d google.com
```

What’s more, we can trivially bind these commands to keyboard shortcuts within mitmproxy if we plan to use them frequently. Flow selectors combined with commands are amazingly powerful, and lets us build and expose re-usable functions for operating on flows.

## Paths

Commands can take an arbitrary number of arguments. Let’s build on the previous example to illustrate this, and also demonstrate another special type: paths.

```
"""Handle file paths as command arguments."""
import logging
from collections.abc import Sequence
from mitmproxy import command
from mitmproxy import flow
from mitmproxy import http
from mitmproxy import types
from mitmproxy.log import ALERT
class MyAddon:
    @command.command("myaddon.histogram")
    def histogram(
        self,
        flows: Sequence[flow.Flow],
        path: types.Path,
    ) -> None:
        totals: dict[str, int] = {}
        for f in flows:
            if isinstance(f, http.HTTPFlow):
                totals[f.request.host] = totals.setdefault(f.request.host, 0) + 1
        with open(path, "w+") as fp:
            for cnt, dom in sorted((v, k) for (k, v) in totals.items()):
                fp.write(f"{cnt}: {dom}\n")
        logging.log(ALERT, "done")
addons = [MyAddon()]
```

examples/addons/commands-paths.py

Our command calculates a histogram of the domains in the specified set of flows, and writes it to a path which is specified as the second argument to the command. Try invoking it like this:

```
:myaddon.histogram @all /tmp/xxx
```

Notice that mitmproxy provides tab completion both for the flow specification and the path.

## Supported Types

The following types are supported for options. If you need to use a type not listed here, please send us a pull request.

- Primitive types: `str`, `int`, `bool`
- Sequences: `typing.Sequence[str]`
- Flows and flow sequences: `flow.Flow` and `typing.Sequence[flow.Flow]`
- Multiple choice strings: `types.Choice`
- Meta-types: `types.Command` and `types.Arg`. These are for constructing commands that invoke other commands. This is most commonly useful in keybinding - see the built-in mitmproxy console keybindings for a rich suite of examples.
- Data types: `types.CutSpec` and `types.Data`. The cuts mechanism is in alpha at the moment, and provides a convenient way to snip up flow data.
- Path: `types.Path`