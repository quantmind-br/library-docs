---
title: User Interface
url: https://docs.mitmproxy.org/stable/mitmproxytutorial-userinterface/
source: crawler
fetched_at: 2026-01-28T16:18:11.342468984-03:00
rendered_js: false
word_count: 399
summary: This document introduces the mitmproxy command-line user interface, explaining how to view and navigate network flows, inspect flow details, and interact with the tool using keyboard shortcuts and the command prompt.
tags:
    - mitmproxy-ui
    - user-interface
    - cli-navigation
    - keyboard-shortcuts
    - flow-management
    - command-prompt
    - proxy-tool
category: tutorial
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/cli-tutorials/cli-01-user-interface.md)

First of all, we need to become familiar with mitmproxy’s user interface. Open the terminal window in which you started mitmproxy. You are in the default view of mitmproxy, which shows a list of flows. You should see your browser’s HTTP requests to load this tutorial. mitmproxy adds rows to the view as new requests come in.

Video Content

[Welcome to the mitmproxy tutorial. In this lesson we cover the user interface.  
\
00:00](#)

[This is the default view of mitmproxy.  
\
00:14](#)

[mitmproxy adds rows to the view as new requests come in.  
\
00:18](#)

[Let’s generate some requests using `curl` in a separate terminal.  
\
00:23](#)

[Use curl’s `--proxy` option to configure mitmproxy as a proxy.  
\
00:31](#)

[We use the text-based weather service `wttr.in`.  
\
00:46](#)

[You see the requests to `wttr.in` in the list of flows.  
\
01:12](#)

[mitmproxy is controlled using keyboard shortcuts.  
\
01:17](#)

[Use your arrow keys `↑` and `↓` to change the focused flow (`>>`).  
\
01:21](#)

[The focused flow (`>>`) is used as a target for various commands.  
\
01:30](#)

[One such command shows the flow details, it is bound to `ENTER`.  
\
01:36](#)

[Press `ENTER` to view the details of the focused flow.  
\
01:42](#)

[The flow details view has 3 panes: request, response, and detail.  
\
01:47](#)

[Use your arrow keys `←` and `→` to switch between panes.  
\
01:52](#)

[Press `q` to exit the current view.  
\
02:10](#)

[Press `?` to get a list of all available keyboard shortcuts.  
\
02:14](#)

[Tip: Remember the `?` shortcut. It works in every view.  
\
02:28](#)

[Press `q` to exit the current view.  
\
02:33](#)

[Each shortcut is internally bound to a command.  
\
02:36](#)

[You can also execute commands directly (without using shortcuts).  
\
02:40](#)

[Press `:` to open the command prompt at the bottom.  
\
02:46](#)

[Enter `console.view.flow @focus`.  
\
02:51](#)

[The command `console.view.flow` opens the details view for a flow.  
\
03:01](#)

[The argument `@focus` defines the target flow.  
\
03:06](#)

[Press `ENTER` to execute the command.  
\
03:11](#)

[Commands unleash the full power of mitmproxy, i.e., to configure interceptions.  
\
03:14](#)

[You now know basics of mitmproxy’s UI and how to control it.  
\
03:21](#)

[In the next lesson you will learn to intercept flows.  
\
03:28](#)

In the next lesson, you will learn to intercept requests before sending them to the server.