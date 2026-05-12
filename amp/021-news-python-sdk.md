---
title: Amp Python SDK
url: https://ampcode.com/news/python-sdk
source: crawler
fetched_at: 2026-02-06T02:08:19.471736941-03:00
rendered_js: false
word_count: 114
summary: This document introduces the Amp Python SDK, explaining how to install and use it to programmatically execute Amp tasks and migrations from within a Python environment.
tags:
    - python-sdk
    - amp-cli
    - automation
    - code-migration
    - asynchronous-execution
category: guide
---

For all of you who swear by tabs and clean syntax, the Amp Python SDK is now live.

You can run Amp programmatically from your Python code, just like you already do in TypeScript.

Here, for example, is how you instruct Amp to migrate React components with [custom toolbox tools](https://ampcode.com/news/toolboxes) to validate changes:

```
import asyncio
import os
from amp_sdk import execute, AmpOptions

prompt = """
	  Goal: Migrate all React components from React 17 to React 18.

    1. Find all React component files (.tsx, .jsx)
    2. For each component:
       - Update deprecated lifecycle methods
       - Replace ReactDOM.render with createRoot
    3. Track any components that fail migration with the reason
    4. Run the typecheck_test_tool after each change
    5. Output a summary: migrated count, failed list with reasons
"""

async def main():

    # Use the toolbox directory to share tools with Amp
    toolbox_dir = os.path.join(os.getcwd(), "toolbox")

    async for message in execute(
        prompt,
        AmpOptions(
            cwd=os.getcwd(),
            toolbox=toolbox_dir,
            visibility="workspace",
            dangerously_allow_all=True,
        ),
    ):

        if message.type == "result":
            if message.is_error:
                print(f"Error: {message.error}")
            else:
                print(f"Summary: {message.result}")

if __name__ == "__main__":
    asyncio.run(main())
```

To get started, install the pip package and the Amp CLI:

```
# Install the Amp SDK with pip
$ pip install amp-sdk

# Install the Amp CLI globally
$ npm install -g @sourcegraph/amp
```

Now you can build anything with Amp in any Python runtime environment. To get more ideas and familiar with the SDK, take a look at the examples in the [manual](https://ampcode.com/manual/sdk#advanced-usage).

*Note:* The Amp SDK requires paid credits and cannot use free-tier credits, because ads are not visible in programmatic contexts.