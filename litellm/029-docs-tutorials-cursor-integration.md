---
title: Cursor Integration | liteLLM
url: https://docs.litellm.ai/docs/tutorials/cursor_integration
source: sitemap
fetched_at: 2026-01-21T19:55:15.284819781-03:00
rendered_js: false
word_count: 260
summary: This document provides instructions for routing Cursor IDE requests through a LiteLLM proxy to enable unified logging, budget controls, and access to custom AI models.
tags:
    - cursor-ide
    - litellm
    - proxy-configuration
    - mcp-server
    - api-integration
    - virtual-keys
category: guide
---

Route Cursor IDE requests through LiteLLM for unified logging, budget controls, and access to any model.

info

**Supported modes:** Ask, Plan. Agent mode doesn't support custom API keys yet.

## Quick Reference[​](#quick-reference "Direct link to Quick Reference")

SettingValueBase URL`<LITELLM_PROXY_BASE_URL>/cursor`API KeyYour LiteLLM Virtual KeyModelPublic Model Name from LiteLLM

* * *

## Setup[​](#setup "Direct link to Setup")

### 1. Configure Base URL[​](#1-configure-base-url "Direct link to 1. Configure Base URL")

Open **Cursor → Settings → Cursor Settings → Models**.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/f725f154-588d-448d-a1d7-3c8bffaf3cf3/ascreenshot.jpeg?tl_px=0%2C0&br_px=1376%2C769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=263%2C73)

Enable **Override OpenAI Base URL** and enter your proxy URL with `/cursor`:

```
https://your-litellm-proxy.com/cursor
```

![](https://colony-recorder.s3.amazonaws.com/files/2025-12-13/6580de2b-3a59-45b2-b7b6-3ab105d87e74/ascreenshot.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2JDELI43356LVVTC%2F20251213%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Date=20251213T224156Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&X-Amz-Signature=5a1af4ff63d38d51e06d398ed50f10161d690e3e57e9d67c1d23ce5b7ffdefd5)

### 2. Create Virtual Key[​](#2-create-virtual-key "Direct link to 2. Create Virtual Key")

In LiteLLM Dashboard, go to **Virtual Keys → + Create New Key**.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/1d8156bc-1b12-433f-936d-77f876142e3f/ascreenshot.jpeg?tl_px=0%2C0&br_px=1376%2C769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=240%2C182)

Name your key and select which models it can access.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/c45843db-b623-442b-b42b-3145ef3ba986/ascreenshot.jpeg?tl_px=0%2C151&br_px=1376%2C920&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=453%2C277)

Click **Create Key** then copy it immediately—you won't see it again.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/4022504d-fdba-4e17-b16e-bf8e935cbcad/ascreenshot.jpeg?tl_px=0%2C101&br_px=1376%2C870&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=512%2C277)

Paste it into the **OpenAI API Key** field in Cursor.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/6b50fc92-9219-4868-aac2-a29d0c063e57/ascreenshot.jpeg?tl_px=251%2C235&br_px=1627%2C1004&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=524%2C276)

### 3. Add Custom Model[​](#3-add-custom-model "Direct link to 3. Add Custom Model")

Click **+ Add Custom Model** in Cursor Settings.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/4e46538e-a876-44c4-a133-bdae664510f3/ascreenshot.jpeg?tl_px=192%2C8&br_px=1569%2C777&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=524%2C276)

Get the **Public Model Name** from LiteLLM Dashboard → Models + Endpoints.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/2ee87f64-104a-4b37-8041-c92130a44896/ascreenshot.jpeg?tl_px=0%2C11&br_px=1376%2C780&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=331%2C277)

Paste the name in Cursor and enable the toggle.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/5ab35f93-d417-423f-a359-9811ce18e2c3/ascreenshot.jpeg?tl_px=352%2C26&br_px=1728%2C795&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=786%2C277)

### 4. Test[​](#4-test "Direct link to 4. Test")

Open **Ask** mode with `Cmd+L` / `Ctrl+L` and select your model.

![](https://colony-recorder.s3.amazonaws.com/files/2025-12-13/d87ee25b-3c6d-4231-ba00-4d841d0612bc/ascreenshot.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2JDELI43356LVVTC%2F20251213%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Date=20251213T223855Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&X-Amz-Signature=75316b8cd2d451f476232bd0ca459c4b6877e788637bf228bbd7d8b319fd1427)

Send a message. All requests now route through LiteLLM.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/05a5853a-58ed-44bf-a5c2-c14f9003eace/ascreenshot.jpeg?tl_px=0%2C151&br_px=1728%2C1117&force_format=jpeg&q=100&width=1120.0)

* * *

## Connecting MCP Servers[​](#connecting-mcp-servers "Direct link to Connecting MCP Servers")

You can also connect MCP servers to Cursor via LiteLLM Proxy.

For official instructions on configuring MCP integration with Cursor, please refer to the Cursor documentation here: [https://cursor.com/en-US/docs/context/mcp](https://cursor.com/en-US/docs/context/mcp).

1. In Cursor Settings, go to the "Tools & MCP" tab and click "New MCP Server".
2. In your `mcp.json`, add the following configuration:

```
{
  "mcpServers": {
    "litellm": {
      "url": "http://localhost:4000/everything/mcp",
      "type": "http",
      "headers": {
        "Authorization": "Bearer sk-LITELLM_VIRTUAL_KEY"
      }
    }
  }
}
```

3. LiteLLM's MCP will now appear under "Installed MCP Servers" in Cursor.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

IssueSolutionModel not respondingCheck base URL ends with `/cursor` and key has model accessAuth errorsRegenerate key; ensure it starts with `sk-`Agent mode not workingExpected—only Ask and Plan modes support custom keys