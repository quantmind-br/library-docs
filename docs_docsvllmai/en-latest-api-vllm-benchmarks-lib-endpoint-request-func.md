---
title: endpoint_request_func - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/lib/endpoint_request_func/
source: sitemap
fetched_at: 2026-05-07T21:15:50.078900047-03:00
rendered_js: false
word_count: 125
summary: This document defines the structures and utility functions used for benchmarking API endpoints in vLLM, specifically for handling OpenAI-compatible completion requests and streaming responses.
tags:
    - vllm
    - benchmarking
    - api-requests
    - asyncio
    - streaming-responses
    - openai-api
category: reference
---

## vllm.benchmarks.lib.endpoint\_request\_func [¶](#vllm.benchmarks.lib.endpoint_request_func "Permanent link")

The request function for API endpoints.

## RequestFuncInput `dataclass` [¶](#vllm.benchmarks.lib.endpoint_request_func.RequestFuncInput "Permanent link")

The input for the request function.

Source code in `vllm/benchmarks/lib/endpoint_request_func.py`

```
@dataclass
classRequestFuncInput:
"""The input for the request function."""

    prompt: str | list[str]
    api_url: str
    prompt_len: int
    output_len: int
    model: str
    model_name: str | None = None
    logprobs: int | None = None
    extra_headers: dict | None = None
    extra_body: dict | None = None
    multi_modal_content: dict | list[dict] | None = None
    ignore_eos: bool = False
    language: str | None = None
    request_id: str | None = None
```

## RequestFuncOutput `dataclass` [¶](#vllm.benchmarks.lib.endpoint_request_func.RequestFuncOutput "Permanent link")

The output of the request function including metrics.

Source code in `vllm/benchmarks/lib/endpoint_request_func.py`

```
@dataclass
classRequestFuncOutput:
"""The output of the request function including metrics."""

    generated_text: str = ""
    success: bool = False
    latency: float = 0.0
    output_tokens: int = 0
    ttft: float = 0.0  # Time to first token
    itl: list[float] = field(default_factory=list)  # list of inter-token latencies
    tpot: float = 0.0  # avg next-token latencies
    prompt_len: int = 0
    error: str = ""
    start_time: float = 0.0
    input_audio_duration: float = 0.0  # in seconds
```

## StreamedResponseHandler [¶](#vllm.benchmarks.lib.endpoint_request_func.StreamedResponseHandler "Permanent link")

Handles streaming HTTP responses by accumulating chunks until complete messages are available.

Source code in `vllm/benchmarks/lib/endpoint_request_func.py`

```
classStreamedResponseHandler:
"""Handles streaming HTTP responses by accumulating chunks until complete
    messages are available."""

    def__init__(self):
        self.buffer = ""
        self._decoder = codecs.getincrementaldecoder("utf-8")()

    defadd_chunk(self, chunk_bytes: bytes) -> list[str]:
"""Add a chunk of bytes to the buffer and return any complete
        messages."""
        chunk_str = self._decoder.decode(chunk_bytes)
        self.buffer += chunk_str

        messages = []

        # Split by double newlines (SSE message separator)
        while "\n\n" in self.buffer:
            message, self.buffer = self.buffer.split("\n\n", 1)
            message = message.strip()
            if message:
                messages.append(message)

        # if self.buffer is not empty, check if it is a complete message
        # by removing data: prefix and check if it is a valid JSON
        if self.buffer.startswith("data: "):
            message_content = self.buffer.removeprefix("data: ").strip()
            if message_content == "[DONE]":
                messages.append(self.buffer.strip())
                self.buffer = ""
            elif message_content:
                try:
                    json.loads(message_content)
                    messages.append(self.buffer.strip())
                    self.buffer = ""
                except json.JSONDecodeError:
                    # Incomplete JSON, wait for more chunks.
                    pass

        return messages
```

### add\_chunk [¶](#vllm.benchmarks.lib.endpoint_request_func.StreamedResponseHandler.add_chunk "Permanent link")

Add a chunk of bytes to the buffer and return any complete messages.

Source code in `vllm/benchmarks/lib/endpoint_request_func.py`

```
defadd_chunk(self, chunk_bytes: bytes) -> list[str]:
"""Add a chunk of bytes to the buffer and return any complete
    messages."""
    chunk_str = self._decoder.decode(chunk_bytes)
    self.buffer += chunk_str

    messages = []

    # Split by double newlines (SSE message separator)
    while "\n\n" in self.buffer:
        message, self.buffer = self.buffer.split("\n\n", 1)
        message = message.strip()
        if message:
            messages.append(message)

    # if self.buffer is not empty, check if it is a complete message
    # by removing data: prefix and check if it is a valid JSON
    if self.buffer.startswith("data: "):
        message_content = self.buffer.removeprefix("data: ").strip()
        if message_content == "[DONE]":
            messages.append(self.buffer.strip())
            self.buffer = ""
        elif message_content:
            try:
                json.loads(message_content)
                messages.append(self.buffer.strip())
                self.buffer = ""
            except json.JSONDecodeError:
                # Incomplete JSON, wait for more chunks.
                pass

    return messages
```

## async\_request\_openai\_completions `async` [¶](#vllm.benchmarks.lib.endpoint_request_func.async_request_openai_completions "Permanent link")

```
async_request_openai_completions(
    request_func_input: RequestFuncInput,
    session: ClientSession,
    pbar: tqdm | None = None,
) -> RequestFuncOutput
```

The async request function for the OpenAI Completions API.

Parameters:

Name Type Description Default `request_func_input` `RequestFuncInput`

The input for the request function.

*required* `pbar` `tqdm | None`

The progress bar to display the progress.

`None`

Returns:

Type Description `RequestFuncOutput`

The output of the request function.

Source code in `vllm/benchmarks/lib/endpoint_request_func.py`

```
async defasync_request_openai_completions(
    request_func_input: RequestFuncInput,
    session: aiohttp.ClientSession,
    pbar: tqdm | None = None,
) -> RequestFuncOutput:
"""The async request function for the OpenAI Completions API.

    Args:
        request_func_input: The input for the request function.
        pbar: The progress bar to display the progress.

    Returns:
        The output of the request function.
    """
    api_url = request_func_input.api_url
    _validate_api_url(api_url, "OpenAI Completions API", "completions")

    payload = {
        "model": request_func_input.model_name
        if request_func_input.model_name
        else request_func_input.model,
        "prompt": request_func_input.prompt,
        "repetition_penalty": 1.0,
        "max_tokens": request_func_input.output_len,
        "logprobs": request_func_input.logprobs,
        "stream": True,
        "stream_options": {
            "include_usage": True,
        },
    }
    _update_payload_common(payload, request_func_input)

    headers = _get_headers()
    _update_headers_common(headers, request_func_input)

    output = RequestFuncOutput()
    output.prompt_len = request_func_input.prompt_len

    generated_text = ""
    st = time.perf_counter()
    output.start_time = st
    most_recent_timestamp = st
    try:
        async with session.post(url=api_url, json=payload, headers=headers) as response:
            if response.status == 200:
                first_chunk_received = False
                handler = StreamedResponseHandler()

                async for chunk_bytes in response.content.iter_any():
                    chunk_bytes = chunk_bytes.strip()
                    if not chunk_bytes:
                        continue

                    messages = handler.add_chunk(chunk_bytes)
                    for message in messages:
                        # NOTE: SSE comments (often used as pings) start with
                        # a colon. These are not JSON data payload and should
                        # be skipped.
                        if message.startswith(":"):
                            continue

                        chunk = message.removeprefix("data: ")

                        if chunk != "[DONE]":
                            data = json.loads(chunk)

                            # NOTE: Some completion API might have a last
                            # usage summary response without a token so we
                            # want to check a token was generated
                            if choices := data.get("choices"):
                                # Note that text could be empty here
                                # e.g. for special tokens
                                text = choices[0].get("text")
                                timestamp = time.perf_counter()
                                # First token
                                if not first_chunk_received:
                                    first_chunk_received = True
                                    ttft = time.perf_counter() - st
                                    output.ttft = ttft

                                # Decoding phase
                                else:
                                    output.itl.append(timestamp - most_recent_timestamp)

                                most_recent_timestamp = timestamp
                                generated_text += text or ""
                            elif usage := data.get("usage"):
                                output.output_tokens = usage.get("completion_tokens")
                                if (pt := usage.get("prompt_tokens")) is not None:
                                    output.prompt_len = pt
                if first_chunk_received:
                    output.success = True
                else:
                    output.success = False
                    output.error = (
                        "Never received a valid chunk to calculate TTFT."
                        "This response will be marked as failed!"
                    )
                output.generated_text = generated_text
                output.latency = most_recent_timestamp - st
            else:
                output.error = response.reason or ""
                output.success = False
    except Exception:
        output.success = False
        exc_info = sys.exc_info()
        output.error = "".join(traceback.format_exception(*exc_info))

    if pbar:
        pbar.update(1)
    return output
```