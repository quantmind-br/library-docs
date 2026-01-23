---
title: Fetch Extension | goose
url: https://block.github.io/goose/docs/mcp/fetch-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:10.448847003-03:00
rendered_js: true
word_count: 198
summary: This document provides instructions on installing and configuring the Fetch MCP Server extension for goose to enable web content retrieval and processing capabilities.
tags:
    - goose
    - mcp-server
    - web-fetching
    - extension-setup
    - api-integration
    - uvx
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

Known Limitation

The Fetch extension [does not work](https://github.com/block/goose/issues/1184) with Google models (e.g. gemini-2.0-flash) because this extension uses `format: uri` in its JSON schema which Google doesn't support.

This tutorial covers how to add the [Fetch MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) as a goose extension to retrieve and process content from the web.

TLDR

- goose Desktop
- goose CLI

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [uv](https://docs.astral.sh/uv/#installation) installed on your system to run this command, as it uses `uvx`.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=uvx&arg=mcp-server-fetch&id=fetch&name=Fetch&description=Web%20content%20fetching%20and%20processing%20capabilities)
2. Click `Yes` to confirm the installation
3. Click the button in the top-left to open the sidebar
4. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

Let's use the Fetch extension to get random programming jokes from the [Official Joke API](https://official-joke-api.appspot.com/random_joke).

info

While this API does not require an API key, many APIs do. If you need to provide an API key, you can set it as an environment variable and tell goose its name. Example: *"get tomorrow's weather for New Orleans from the weatherapi. Don't use the key directly but instead use a script that gets the value from the env var WEATHER\_API\_KEY"*

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
make a web page that tells jokes for programmers. The page should ask the user the setup of the joke, allow them to guess the punchline and then tell them if they are right or wrong. Include a button that allows them to request another joke. you can fetch the jokes from the official joke api
```

### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll help you create a web page that uses the Official Joke API to display programming jokes. I'll break this down into steps:

First, let's verify the API endpoint and see what kind of data we get
Then create an HTML file with the necessary structure
Add JavaScript to handle the interactions

Let me check the API first:


FETCH
url: https://official-joke-api.appspot.com/jokes/programming/random

Output
Content type application/json; charset=utf-8 cannot be simplified to markdown, but here is the raw content:
Contents of https://official-joke-api.appspot.com/jokes/programming/random:
[{"type":"programming","setup":"A SQL query walks into a bar, walks up to two tables and asks...","punchline":"'Can I join you?'","id":23}]

Perfect! Now I'll create an HTML file with the necessary structure and JavaScript code:

TEXT_EDITOR
command: write
file_text:
<!DOCTYPE html> <html lang="en"> <head> <meta charset="U...
path:
programmer_jokes.html

Output
programmer_jokes.html


[... contents of programmer_jokes.html ...]

I've created a complete web page that:

Fetches random programming jokes from the Official Joke API
Shows the setup of the joke
Provides an input field for users to guess the punchline
Shows whether they got it right or wrong
Displays the actual punchline after they guess
Includes a button to get another joke

The page also includes:
Clean, modern styling
Error handling for API failures
Responsive design that works on both desktop and mobile
Visual feedback for correct/incorrect answers
Disabled input after guessing to prevent multiple attempts
You can open the file programmer_jokes.html in your web browser to try it out. Would you like me to help you test it or make any adjustments to the design or functionality?
```

### Results[​](#results "Direct link to Results")

![website goose built](https://block.github.io/goose/assets/images/programmer-jokes-fetch-mcp-ccb6ac3de6a6a9ecec6f529638d2049a.png)

Source Code