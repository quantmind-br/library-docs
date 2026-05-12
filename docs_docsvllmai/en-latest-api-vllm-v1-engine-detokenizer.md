---
title: detokenizer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/engine/detokenizer/
source: sitemap
fetched_at: 2026-05-07T21:40:35.506057298-03:00
rendered_js: false
word_count: 111
summary: The BaseIncrementalDetokenizer provides an abstract base class for incrementally converting token IDs into text while handling stop-string evaluation and output buffering.
tags:
    - detokenization
    - vllm
    - inference-engine
    - token-processing
    - stop-sequences
category: reference
---

## BaseIncrementalDetokenizer [¶](#vllm.v1.engine.detokenizer.BaseIncrementalDetokenizer "Permanent link")

Bases: `IncrementalDetokenizer`, `ABC`

Source code in `vllm/v1/engine/detokenizer.py`

```
classBaseIncrementalDetokenizer(IncrementalDetokenizer, ABC):
    def__init__(self, request: EngineCoreRequest):
        super().__init__()

        # Stop strings
        params = request.sampling_params
        assert params is not None
        if params.stop is None:
            self.stop = []
        elif isinstance(params.stop, str):
            self.stop = [params.stop]
        else:
            self.stop = params.stop
        self.min_tokens = params.min_tokens
        self.include_stop_str_in_output = params.include_stop_str_in_output

        # Number of chars to hold back when stop strings are to be excluded
        # from streamed output.
        if self.stop and not self.include_stop_str_in_output:
            self.stop_buffer_length = max(len(s) for s in self.stop) - 1
        else:
            self.stop_buffer_length = 0
        self._last_output_text_offset: int = 0

        # Generation data
        self.output_text = ""

    defupdate(self, new_token_ids: list[int], stop_terminated: bool) -> str | None:
"""
        Update RequestState for the request_id by:
            1) Detokenize the new token ids incrementally.
            2) Evaluate stop criteria.

        Return matched stop string or None.
        """
        if not new_token_ids:
            # Skip detokenization if no new token ids.
            return None

        if stop_terminated and not self.include_stop_str_in_output:
            # If stop-terminated, exclude last token from detokenization
            # based on include_stop_str_in_output parameter.
            skipped_stop_token_id = new_token_ids[-1]
            new_token_ids = new_token_ids[:-1]
        else:
            skipped_stop_token_id = None

        # 1) Detokenize the new token ids incrementally.
        stop_check_offset = len(self.output_text)
        for new_token_id in new_token_ids:
            self.token_ids.append(new_token_id)
            self.output_text += self.decode_next(new_token_id)
            # Support min_tokens, see https://github.com/vllm-project/vllm/pull/22014
            if self.min_tokens and self.num_output_tokens() <= self.min_tokens:
                stop_check_offset = len(self.output_text)

        if skipped_stop_token_id is not None:
            # Cleanup after skipping detokenization.
            self.token_ids.append(skipped_stop_token_id)

        # 2) Evaluate stop strings.
        stop_string = None
        if self.stop and self.num_output_tokens() > self.min_tokens:
            stop = check_stop_strings(
                output_text=self.output_text,
                new_char_count=len(self.output_text) - stop_check_offset,
                stop=self.stop,
                include_in_output=self.include_stop_str_in_output,
            )
            if stop is not None:
                stop_string, truncate_to = stop
                if truncate_to != -1:
                    self.output_text = self.output_text[:truncate_to]

        return stop_string

    @abstractmethod
    defdecode_next(self, next_token_id: int) -> str:
        raise NotImplementedError

    defget_next_output_text(self, finished: bool, delta: bool) -> str:
"""If delta is True, only new text since the last call to
        this method is returned"""

        # We return the full output text if the sequence is finished.
        buffer_length = 0 if finished else self.stop_buffer_length
        if not delta:
            if not buffer_length:
                return self.output_text
            return self.output_text[:-buffer_length]

        length = len(self.output_text) - buffer_length
        last_offset = self._last_output_text_offset
        if last_offset < length:
            self._last_output_text_offset = length
            return self.output_text[last_offset:length]
        return ""
```

### get\_next\_output\_text [¶](#vllm.v1.engine.detokenizer.BaseIncrementalDetokenizer.get_next_output_text "Permanent link")

```
get_next_output_text(finished: bool, delta: bool) -> str
```

If delta is True, only new text since the last call to this method is returned

Source code in `vllm/v1/engine/detokenizer.py`

```
defget_next_output_text(self, finished: bool, delta: bool) -> str:
"""If delta is True, only new text since the last call to
    this method is returned"""

    # We return the full output text if the sequence is finished.
    buffer_length = 0 if finished else self.stop_buffer_length
    if not delta:
        if not buffer_length:
            return self.output_text
        return self.output_text[:-buffer_length]

    length = len(self.output_text) - buffer_length
    last_offset = self._last_output_text_offset
    if last_offset < length:
        self._last_output_text_offset = length
        return self.output_text[last_offset:length]
    return ""
```

### update [¶](#vllm.v1.engine.detokenizer.BaseIncrementalDetokenizer.update "Permanent link")

```
update(
    new_token_ids: list[int], stop_terminated: bool
) -> str | None
```

Update RequestState for the request\_id by

1\) Detokenize the new token ids incrementally. 2) Evaluate stop criteria.

Return matched stop string or None.

Source code in `vllm/v1/engine/detokenizer.py`

```
defupdate(self, new_token_ids: list[int], stop_terminated: bool) -> str | None:
"""
    Update RequestState for the request_id by:
        1) Detokenize the new token ids incrementally.
        2) Evaluate stop criteria.

    Return matched stop string or None.
    """
    if not new_token_ids:
        # Skip detokenization if no new token ids.
        return None

    if stop_terminated and not self.include_stop_str_in_output:
        # If stop-terminated, exclude last token from detokenization
        # based on include_stop_str_in_output parameter.
        skipped_stop_token_id = new_token_ids[-1]
        new_token_ids = new_token_ids[:-1]
    else:
        skipped_stop_token_id = None

    # 1) Detokenize the new token ids incrementally.
    stop_check_offset = len(self.output_text)
    for new_token_id in new_token_ids:
        self.token_ids.append(new_token_id)
        self.output_text += self.decode_next(new_token_id)
        # Support min_tokens, see https://github.com/vllm-project/vllm/pull/22014
        if self.min_tokens and self.num_output_tokens() <= self.min_tokens:
            stop_check_offset = len(self.output_text)

    if skipped_stop_token_id is not None:
        # Cleanup after skipping detokenization.
        self.token_ids.append(skipped_stop_token_id)

    # 2) Evaluate stop strings.
    stop_string = None
    if self.stop and self.num_output_tokens() > self.min_tokens:
        stop = check_stop_strings(
            output_text=self.output_text,
            new_char_count=len(self.output_text) - stop_check_offset,
            stop=self.stop,
            include_in_output=self.include_stop_str_in_output,
        )
        if stop is not None:
            stop_string, truncate_to = stop
            if truncate_to != -1:
                self.output_text = self.output_text[:truncate_to]

    return stop_string
```

## check\_stop\_strings [¶](#vllm.v1.engine.detokenizer.check_stop_strings "Permanent link")

Check if any stop strings are matched and truncate sequence output text accordingly.

Returns tuple (stop\_string, offset) if matched or else None.

Where stop\_string is the matched stop string and offset is the length to which output\_text should be truncated, or -1 for no truncation.

Source code in `vllm/v1/engine/detokenizer.py`

```
defcheck_stop_strings(
    output_text: str,
    new_char_count: int,
    stop: list[str],
    include_in_output: bool,
) -> tuple[str, int] | None:
"""Check if any stop strings are matched and truncate sequence
    output text accordingly.

    Returns tuple (stop_string, offset) if matched or else None.

    Where stop_string is the matched stop string and offset is the
    length to which output_text should be truncated, or -1 for no
    truncation.
    """
    if not new_char_count or not stop:
        return None

    for stop_str in stop:
        stop_string_len = len(stop_str)
        # Avoid searching already-searched text.
        stop_index = output_text.find(stop_str, 1 - new_char_count - stop_string_len)
        if stop_index == -1:
            continue

        if include_in_output:
            # Truncate to end of stop string.
            stop_index += stop_string_len
            if stop_index >= len(output_text):
                # No truncation required.
                return stop_str, -1

        # Truncate the output text to either the beginning
        # or end of the stop string.
        return stop_str, stop_index
    return None
```