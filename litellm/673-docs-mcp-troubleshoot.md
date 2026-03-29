---
title: MCP Troubleshooting Guide | liteLLM
url: https://docs.litellm.ai/docs/mcp_troubleshoot
source: sitemap
fetched_at: 2026-01-21T19:45:43.919879832-03:00
rendered_js: false
word_count: 616
summary: This document provides a comprehensive troubleshooting guide for diagnosing connectivity and configuration issues when using LiteLLM as an MCP proxy. It explains how to isolate failures between client, proxy, and server hops using tools like the MCP Inspector and curl smoke tests.
tags:
    - litellm
    - mcp-proxy
    - troubleshooting
    - debugging
    - connectivity-test
    - oauth-discovery
    - json-rpc
category: guide
---

When LiteLLM acts as an MCP proxy, traffic normally flows `Client → LiteLLM Proxy → MCP Server`, while OAuth-enabled setups add an authorization server for metadata discovery.

For provisioning steps, transport options, and configuration fields, refer to [mcp.md](https://docs.litellm.ai/docs/mcp).

## Locate the Error Source[​](#locate-the-error-source "Direct link to Locate the Error Source")

Pin down where the failure occurs before adjusting settings so you do not mix symptoms from separate hops.

### LiteLLM UI / Playground Errors (LiteLLM → MCP)[​](#litellm-ui--playground-errors-litellm--mcp "Direct link to LiteLLM UI / Playground Errors (LiteLLM → MCP)")

Failures shown on the MCP creation form or within the MCP Tool Testing Playground mean the LiteLLM proxy cannot reach the MCP server. Typical causes are misconfiguration (transport, headers, credentials), MCP/server outages, network/firewall blocks, or inaccessible OAuth metadata.

**Actions**

- Capture LiteLLM proxy logs alongside MCP-server logs (see [Error Log Example](https://docs.litellm.ai/docs/mcp_troubleshoot#error-log-example-failed-mcp-call)) to inspect the request/response pair and stack traces.
- From the LiteLLM server, run Method 2 ([`curl` smoke test](https://docs.litellm.ai/docs/mcp_troubleshoot#curl-smoke-test)) against the MCP endpoint to confirm basic connectivity.

### Client Traffic Issues (Client → LiteLLM)[​](#client-traffic-issues-client--litellm "Direct link to Client Traffic Issues (Client → LiteLLM)")

If only real client requests fail, determine whether LiteLLM ever reaches the MCP hop.

#### MCP Protocol Sessions[​](#mcp-protocol-sessions "Direct link to MCP Protocol Sessions")

Clients such as IDEs or agent runtimes speak the MCP protocol directly with LiteLLM.

**Actions**

- Inspect LiteLLM access logs (see [Access Log Example](https://docs.litellm.ai/docs/mcp_troubleshoot#access-log-example-successful-mcp-call)) to verify the client request reached the proxy and which MCP server it targeted.
- Review LiteLLM error logs (see [Error Log Example](https://docs.litellm.ai/docs/mcp_troubleshoot#error-log-example-failed-mcp-call)) for TLS, authentication, or routing errors that block the request before the MCP call starts.
- Use the [MCP Inspector](https://docs.litellm.ai/docs/mcp_troubleshoot#mcp-inspector) to confirm the MCP server is reachable outside of the failing client.

#### Responses/Completions with Embedded MCP Calls[​](#responsescompletions-with-embedded-mcp-calls "Direct link to Responses/Completions with Embedded MCP Calls")

During `/responses` or `/chat/completions`, LiteLLM may trigger MCP tool calls mid-request. An error could occur before the MCP call begins or after the MCP responds.

**Actions**

- Check LiteLLM request logs (see [Access Log Example](https://docs.litellm.ai/docs/mcp_troubleshoot#access-log-example-successful-mcp-call)) to see whether an MCP attempt was recorded; if not, the problem lies in `Client → LiteLLM`.
- Validate MCP connectivity with the [MCP Inspector](https://docs.litellm.ai/docs/mcp_troubleshoot#mcp-inspector) to ensure the server responds.
- Reproduce the same MCP call via the LiteLLM Playground to confirm LiteLLM can complete the MCP hop independently.

### OAuth Metadata Discovery[​](#oauth-metadata-discovery "Direct link to OAuth Metadata Discovery")

LiteLLM performs metadata discovery per the MCP spec ([section 2.3](https://modelcontextprotocol.info/specification/draft/basic/authorization/#23-server-metadata-discovery)). When OAuth is enabled, confirm the authorization server exposes the metadata URL and that LiteLLM can fetch it.

**Actions**

- Use `curl <metadata_url>` (or similar) from the LiteLLM host to ensure the discovery document is reachable and contains the expected authorization/token endpoints.
- Record the exact metadata URL, requested scopes, and any static client credentials so support can replay the discovery step if needed.

## Verify Connectivity[​](#verify-connectivity "Direct link to Verify Connectivity")

Run lightweight validations before impacting production traffic.

### MCP Inspector[​](#mcp-inspector "Direct link to MCP Inspector")

Use the MCP Inspector when you need to test both `Client → LiteLLM` and `Client → MCP` communications in one place; it makes isolating the failing hop straightforward.

1. Execute `npx @modelcontextprotocol/inspector` on your workstation.
2. Configure and connect:
   
   - **Transport Type:** choose the transport the client uses (Streamable HTTP for LiteLLM).
   - **URL:** the endpoint under test (LiteLLM MCP URL for `Client → LiteLLM`, or the MCP server URL for `Client → MCP`).
   - **Custom Headers:** e.g., `Authorization: Bearer <LiteLLM API Key>`.
3. Open the **Tools** tab and click **List Tools** to verify the MCP alias responds.

### `curl` Smoke Test[​](#curl-smoke-test "Direct link to curl-smoke-test")

`curl` is ideal on servers where installing the Inspector is impractical. It replicates the MCP tool call LiteLLM would make—swap in the domain of the system under test (LiteLLM or the MCP server).

```
curl -X POST https://your-target-domain.example.com/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

Add `-H "Authorization: Bearer <LiteLLM API Key>"` when the target is a LiteLLM endpoint that requires authentication. Adjust the headers, or payload to target other MCP methods. Matching failures between `curl` and LiteLLM confirm that the MCP server or network/OAuth layer is the culprit.

## Review Logs[​](#review-logs "Direct link to Review Logs")

Well-scoped logs make it clear whether LiteLLM reached the MCP server and what happened next.

### Access Log Example (successful MCP call)[​](#access-log-example-successful-mcp-call "Direct link to Access Log Example (successful MCP call)")

```
INFO:     127.0.0.1:57230 - "POST /everything/mcp HTTP/1.1" 200 OK
```

### Error Log Example (failed MCP call)[​](#error-log-example-failed-mcp-call "Direct link to Error Log Example (failed MCP call)")

```
07:22:00 - LiteLLM:ERROR: client.py:224 - MCP client list_tools failed - Error Type: ExceptionGroup, Error: unhandled errors in a TaskGroup (1 sub-exception), Server: http://localhost:3001/mcp, Transport: MCPTransport.http
  httpcore.ConnectError: All connection attempts failed
ERROR:LiteLLM:MCP client list_tools failed - Error Type: ExceptionGroup, Error: unhandled errors in a TaskGroup (1 sub-exception)...
  httpx.ConnectError: All connection attempts failed
```