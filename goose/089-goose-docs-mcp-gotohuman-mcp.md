---
title: gotoHuman Extension | goose
url: https://block.github.io/goose/docs/mcp/gotohuman-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:19.369548077-03:00
rendered_js: true
word_count: 218
summary: This tutorial explains how to integrate the gotoHuman MCP Server with goose to implement human-in-the-loop approval steps within AI-driven workflows.
tags:
    - gotohuman
    - goose-ai
    - mcp-server
    - human-in-the-loop
    - workflow-automation
    - approval-workflow
category: tutorial
---

This tutorial covers how to add the [gotoHuman MCP Server](https://github.com/gotohuman/gotohuman-mcp-server) as a goose extension to bring **human-in-the-loop approvals** into your AI workflows. With gotoHuman, goose can pause and request a review before continuing, perfect for blog drafts, code reviews,compliance checks, etc.

In this example, goose sends a LinkedIn post draft to gotoHuman for approval using the `n8n news to post` template that was created.

```
Send this blog draft about goose to gotoHuman for review using my `n8n news to post` form. 

Include today’s date as the timestamp, these links: 
[goose Docs: https://block.github.io/goose/, gotoHuman: https://gotohuman.com/], 
summarize it as ‘Introducing goose’s integration with gotoHuman for human approvals,’ 
and here’s the draft:

goose is an open-source AI agent that runs locally on your machine, right in your terminal or IDE. 
It connects to MCP servers like gotoHuman to extend its abilities. While goose can automate tasks, 
sometimes you need a human in the loop. With gotoHuman MCP, you can add approval steps into any workflow;
from reviewing a LinkedIn post draft to signing off on a code change. 
Once approved, goose can continue where it left off. 
This makes agent workflows safer, more collaborative, and better suited for real-world teams.
```

Now if you open the **Review Link** from goose’s output, you’ll see the request waiting in your gotoHuman dashboard: