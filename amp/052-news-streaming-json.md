---
title: Streaming JSON
url: https://ampcode.com/news/streaming-json
source: crawler
fetched_at: 2026-02-06T02:08:28.603551433-03:00
rendered_js: false
word_count: 117
summary: This document introduces the --stream-json and --stream-json-input flags for the Amp CLI, which allow for structured JSON input and output during command execution. It explains how to use these flags to programmatically interact with the CLI and maintain multi-turn conversations.
tags:
    - amp-cli
    - json-streaming
    - cli-flags
    - structured-data
    - automation
    - command-line-interface
category: guide
---

The Amp CLI has two new flags: `--stream-json` and `--stream-json-input`.

They can be used together with the `--execute` flag to turn on structured JSON output and input, respectively.

Here is an example:

```
$ amp --execute "what is 2+2?" --stream-json
```

This would print something like the following on stdout:

```
{"type":"system","subtype":"init","cwd":"/Users/mrnugget/work/amp","session_id":"T-2775dc92-90ed-4f85-8b73-8f9766029e83","tools":["oracle","..."],"mcp_servers":[]}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"what is 2+2?"}]},"parent_tool_use_id":null,"session_id":"T-2775dc92-90ed-4f85-8b73-8f9766029e83"}
{"type":"assistant","message":{"type":"message","role":"assistant","content":[{"type":"text","text":"2 + 2 equals 4."}],"stop_reason":"end_turn","usage":{"input_tokens":12783,"cache_creation_input_tokens":367,"cache_read_input_tokens":12416,"output_tokens":8,"max_tokens":224000,"service_tier":"standard"}},"parent_tool_use_id":null,"session_id":"T-2775dc92-90ed-4f85-8b73-8f9766029e83"}
{"type":"result","subtype":"success","duration_ms":2906,"is_error":false,"num_turns":1,"result":"2 + 2 equals 4.","session_id":"T-2775dc92-90ed-4f85-8b73-8f9766029e83"}
```

Structured input can be provided on stdin with the `--stream-json-input` flag:

```
$ echo '{
  "type": "user",
  "message": {
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": "what is 2+2?"
      }
    ]
  }
}' | amp -x --stream-json --stream-json-input
```

If `--stream-json-input` is set, the Amp CLI will process user messages as soon as they are received on stdin and exit as soon as stdin is closed and the agent has ended its turns.

Combined with `amp threads continue [thread id]`, multi-turn conversations can even happen across multiple invocations of the CLI:

```
$ amp -x "what is 2+2?" --stream-json
...
$ amp threads continue -x "and now add 7 to that" --stream-json
...
{"type":"result","result":"11.", "subtype":"success","duration_ms":2906,"is_error":false,"num_turns":2,"session_id":"T-2775dc92-90ed-4f85-8b73-8f9766029e83"}
```

See the [Manual](https://ampcode.com/manual#cli-streaming-json) for more details and the [Appendix](https://ampcode.com/manual/appendix#stream-json-output) for the full schema.