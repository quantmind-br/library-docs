---
title: Overview
url: https://docs.mitmproxy.org/stable/addons/overview/
source: crawler
fetched_at: 2026-01-28T16:18:23.2261535-03:00
rendered_js: false
word_count: 345
summary: This document introduces mitmproxy's addon mechanism, explaining how addons interact with events, options, and commands, and provides examples for structuring addons and using an abbreviated scripting syntax.
tags:
    - mitmproxy
    - addons
    - scripting
    - event-handlers
    - proxy-development
    - python
category: tutorial
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/addons/overview.md)

## Addons

Mitmproxy’s addon mechanism is an exceptionally powerful part of mitmproxy. In fact, much of mitmproxy’s own functionality is defined in [a suite of built-in addons](https://github.com/mitmproxy/mitmproxy/tree/main/mitmproxy/addons), implementing everything from functionality like [anticaching](https://docs.mitmproxy.org/stable/overview/features/#anticache) and [sticky cookies](https://docs.mitmproxy.org/stable/overview/features/#sticky-cookies) to our onboarding webapp.

Addons interact with mitmproxy by responding to [events](https://docs.mitmproxy.org/stable/api/events.html), which allow them to hook into and change mitmproxy’s behaviour. They are configured through [options](https://docs.mitmproxy.org/stable/addons/options/), which can be set in mitmproxy’s config file, changed interactively by users, or passed on the command-line. Finally, they can expose [commands](https://docs.mitmproxy.org/stable/addons/commands/), which allows users to invoke their actions either directly or by binding them to keys in the interactive tools.

## Anatomy of an addon

```
"""
Basic skeleton of a mitmproxy addon.
Run as follows: mitmproxy -s anatomy.py
"""
import logging
class Counter:
    def __init__(self):
        self.num = 0
    def request(self, flow):
        self.num = self.num + 1
        logging.info("We've seen %d flows" % self.num)
addons = [Counter()]
```

examples/addons/anatomy.py

Above is a simple addon that keeps track of the number of flows (or more specifically HTTP requests) we’ve seen. Every time it sees a new flow, it increments and logs its tally. The output can be found in the event log in the interactive tools, or on the console in mitmdump.

Take it for a spin and make sure that it does what it’s supposed to, by loading it into your mitmproxy tool of choice. We’ll use mitmdump in these examples, but the flag is identical for all tools:

Here are a few things to note about the code above:

- Mitmproxy picks up the contents of the `addons` global list and loads what it finds into the addons mechanism.
- Addons are just objects - in this case our addon is an instance of `Counter`.
- The `request` method is an example of an *event*. Addons simply implement a method for each event they want to handle. Each event and its signature are documented in the [API documentation](https://docs.mitmproxy.org/stable/api/events.html).

## Abbreviated Scripting Syntax

Sometimes, we would like to write a quick script without going through the trouble of creating a class. The addons mechanism has a shorthand that allows a module as a whole to be treated as an addon object. This lets us place event handler functions in the module scope. For instance, here is a complete script that adds a header to every request:

```
"""An addon using the abbreviated scripting syntax."""
def request(flow):
    flow.request.headers["myheader"] = "value"
```

examples/addons/anatomy2.py