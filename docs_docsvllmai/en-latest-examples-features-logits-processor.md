---
title: Custom Logits Processors - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/logits_processor/
source: sitemap
fetched_at: 2026-05-07T21:12:52.788335225-03:00
rendered_js: false
word_count: 1210
summary: This document demonstrates how to implement and integrate custom logits processors in vLLM to modify model output distributions during inference. It covers batch-level processing, request-level wrapping, and passing custom parameters via SamplingParams.
tags:
    - vllm
    - logits-processor
    - inference
    - custom-sampling
    - token-masking
    - python
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/features/logits_processor.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/logits\_processor](https://github.com/vllm-project/vllm/tree/main/examples/features/logits_processor).

This directory contains examples demonstrating how to use custom logits processors with vLLM's offline inference API. Logits processors allow you to modify the model's output distribution before sampling, enabling controlled generation behaviors like token masking, constrained decoding, and custom sampling strategies.

## Scripts[¶](#scripts "Permanent link")

### `custom.py` — Engine-level logits processor[¶](#custompy-engine-level-logits-processor "Permanent link")

Demonstrates how to instantiate vLLM with a custom logits processor class that operates at the batch level. The example uses a `DummyLogitsProcessor` that masks out all tokens except a specified `target_token` when passed via `SamplingParams.extra_args`.

```
pythonexamples/features/logits_processor/custom.py
```

### `custom_req.py` — Request-level logits processor wrapper[¶](#custom_reqpy-request-level-logits-processor-wrapper "Permanent link")

Shows how to wrap a request-level logits processor (which operates on individual requests) to be compatible with vLLM's batch-level logits processing interface.

```
pythonexamples/features/logits_processor/custom_req.py
```

### `custom_req_init.py` — Request-level processor with engine config[¶](#custom_req_initpy-request-level-processor-with-engine-config "Permanent link")

A special case of wrapping a request-level logits processor where the processor needs access to engine configuration or model metadata during initialization (e.g., vocabulary size, tokenizer info).

```
pythonexamples/features/logits_processor/custom_req_init.py
```

## Key Concepts[¶](#key-concepts "Permanent link")

- **Batch-level vs. request-level**: vLLM processes logits at the batch level for efficiency. If you have a per-request processor, you need to wrap it using the patterns shown in `custom_req.py` and `custom_req_init.py`.
- **`SamplingParams.extra_args`** : Use this to pass custom keyword arguments to your logits processor on a per-request basis (e.g., `target_token`).
- **`DummyLogitsProcessor`** : A reference implementation available in `vllm/test_utils.py` that can be used as a starting point for custom processors.

## Further Reading[¶](#further-reading "Permanent link")

- [vLLM Sampling Parameters](https://docs.vllm.ai/en/latest/api/inference_params.html#sampling-parameters)
- [vLLM LLM API](https://docs.vllm.ai/en/latest/api/offline_inference/llm.html)

## Example materials[¶](#example-materials "Permanent link")

custom.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

"""This example demonstrates instantiating vLLM with a custom logits processor
class object.

For a basic example of implementing a custom logits processor, see
the `DummyLogitsProcessor` implementation in `vllm/test_utils.py`.

For testing purposes, a dummy logits processor is employed which, if
`target_token` is passed as a keyword argument to `SamplingParams.extra_args`,
will mask out all tokens except `target_token`.

A batch is constructed with `temperature=0.0` and 50% of requests specifying
`target_token`, and for these requests - and *only* these requests - we
expect the `target_token` to be decoded in each step, yielding an output
similar to that shown below:

Generated Outputs:
------------------------------------------------------------
Prompt:    'Hello, my name is'
Output:    " ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '"
------------------------------------------------------------
Prompt:    'The president of the United States is'
Output:    " not a racist. He is a racist.\nHe's a racist because he"
------------------------------------------------------------
Prompt:    'The capital of France is'
Output:    ' also also also also also also also also also also also also also
             also also also'
------------------------------------------------------------
Prompt:    'The future of AI is'
Output:    ' in the hands of the people.\n\nThe future of AI is in the'
------------------------------------------------------------
"""

fromtypingimport Any

importtorch

fromvllmimport LLM, SamplingParams
fromvllm.configimport VllmConfig
fromvllm.v1.sample.logits_processorimport (
    BatchUpdate,
    LogitsProcessor,
)
fromvllm.v1.sample.logits_processor.builtinimport process_dict_updates


# Hypothetical custom logits processor
classDummyLogitsProcessor(LogitsProcessor):
"""Fake logit processor to support unit testing and examples"""

    @classmethod
    defvalidate_params(cls, params: SamplingParams):
        target_token: Any | None = params.extra_args and params.extra_args.get(
            "target_token"
        )
        if target_token is not None and not isinstance(target_token, int):
            raise ValueError(
                f"target_token value {target_token}{type(target_token)} is not int"
            )

    def__init__(
        self, vllm_config: VllmConfig, device: torch.device, is_pin_memory: bool
    ):
        self.req_info: dict[int, int] = {}

    defis_argmax_invariant(self) -> bool:
        return False

    defupdate_state(self, batch_update: BatchUpdate | None):
        defextract_extra_arg(params: SamplingParams) -> int | None:
            self.validate_params(params)
            return params.extra_args and params.extra_args.get("target_token")

        process_dict_updates(
            self.req_info,
            batch_update,
            # This function returns the LP's per-request state based on the
            # request details, or None if this LP does not apply to the
            # request.
            lambda params, _, __: extract_extra_arg(params),
        )

    defapply(self, logits: torch.Tensor) -> torch.Tensor:
        if not self.req_info:
            return logits

        # Save target values before modification
        cols = torch.tensor(
            list(self.req_info.values()), dtype=torch.long, device=logits.device
        )
        rows = torch.tensor(
            list(self.req_info.keys()), dtype=torch.long, device=logits.device
        )
        values_to_keep = logits[rows, cols].clone()

        # Mask all but target tokens
        logits[rows] = float("-inf")
        logits[rows, cols] = values_to_keep

        return logits


# Sample prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
# Create a mixture of requests which do and don't utilize the dummy logitproc
sampling_params_list = [
    SamplingParams(temperature=0.0, extra_args={"target_token": 128}),
    SamplingParams(temperature=0.0),
    SamplingParams(temperature=0.0, extra_args={"target_token": 67}),
    SamplingParams(temperature=0.0),
]


defmain():
    # Create an LLM.
    llm = LLM(
        model="facebook/opt-125m",
        logits_processors=[DummyLogitsProcessor],
    )
    # Generate texts from the prompts.
    # The output is a list of RequestOutput objects
    # that contain the prompt, generated text, and other information.
    outputs = llm.generate(prompts, sampling_params_list)
    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt:    {prompt!r}")
        print(f"Output:    {generated_text!r}")
        print("-" * 60)


if __name__ == "__main__":
    main()
```

custom\_req.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

"""This example demonstrates wrapping a request-level logits processor to be
compatible with vLLM's batch-level logits processing

For demo purposes, a dummy logits processor is employed which, if
`target_token` is passed as a keyword argument to `SamplingParams.extra_args`,
will mask out all tokens except `target_token`. This logits processor can be
applied to a vector of logits associated with a single decode step for a single
request. The logits processor cannot be applied to a request which does not
pass in a `target_token` custom argument.

The request-level dummy logits processor is wrapped to create a batch-level
logits processor, which can apply the logits processor to output logits from
all requests in the persistent batch in a given decode step. For requests which
do not provide a `target_token` argument, the corresponding row of `logits`
will not be modified.

A batch is constructed with `temperature=0.0` and 50% of requests specifying
`target_token`, and for these requests - and *only* these requests - we
expect the `target_token` to be decoded in each step, yielding an output
similar to that shown below:

Generated Outputs:
------------------------------------------------------------
Prompt:    'Hello, my name is'
Output:    " ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '"
------------------------------------------------------------
Prompt:    'The president of the United States is'
Output:    " not a racist. He is a racist.\nHe's a racist because he"
------------------------------------------------------------
Prompt:    'The capital of France is'
Output:    ' also also also also also also also also also also also also also
             also also also'
------------------------------------------------------------
Prompt:    'The future of AI is'
Output:    ' in the hands of the people.\n\nThe future of AI is in the'
------------------------------------------------------------
"""

fromtypingimport Any

importtorch

fromvllmimport LLM, SamplingParams
fromvllm.loggerimport init_logger
fromvllm.v1.sample.logits_processorimport (
    AdapterLogitsProcessor,
    RequestLogitsProcessor,
)

logger = init_logger(__name__)


classDummyPerReqLogitsProcessor:
"""The request-level logits processor masks out all logits except the
    token id identified by `target_token`"""

    def__init__(self, target_token: int) -> None:
"""Specify `target_token`"""
        self.target_token = target_token

    def__call__(
        self,
        output_ids: list[int],
        logits: torch.Tensor,
    ) -> torch.Tensor:
        val_to_keep = logits[self.target_token].item()
        logits[:] = float("-inf")
        logits[self.target_token] = val_to_keep
        return logits


classWrappedPerReqLogitsProcessor(AdapterLogitsProcessor):
"""Example of wrapping a fake request-level logit processor to create a
    batch-level logits processor"""

    @classmethod
    defvalidate_params(cls, params: SamplingParams):
        target_token: Any | None = params.extra_args and params.extra_args.get(
            "target_token"
        )
        if target_token is not None and not isinstance(target_token, int):
            raise ValueError(f"target_token value {target_token} is not int")

    defis_argmax_invariant(self) -> bool:
        return False

    defnew_req_logits_processor(
        self,
        params: SamplingParams,
    ) -> RequestLogitsProcessor | None:
"""This method returns a new request-level logits processor, customized
        to the `target_token` value associated with a particular request.

        Returns None if the logits processor should not be applied to the
        particular request. To use the logits processor the request must have
        a "target_token" custom argument with an integer value.

        Args:
          params: per-request sampling params

        Returns:
          `Callable` request logits processor, or None
        """
        target_token: Any | None = params.extra_args and params.extra_args.get(
            "target_token"
        )
        if target_token is None:
            return None
        return DummyPerReqLogitsProcessor(target_token)


# Sample prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
# Create a mixture of requests which do and don't utilize the dummy logitproc
sampling_params_list = [
    SamplingParams(temperature=0.0, extra_args={"target_token": 128}),
    SamplingParams(temperature=0.0),
    SamplingParams(temperature=0.0, extra_args={"target_token": 67}),
    SamplingParams(temperature=0.0),
]


defmain():
    # Create an LLM.
    llm = LLM(
        model="facebook/opt-125m",
        logits_processors=[WrappedPerReqLogitsProcessor],
    )
    # Generate texts from the prompts.
    # The output is a list of RequestOutput objects
    # that contain the prompt, generated text, and other information.
    outputs = llm.generate(prompts, sampling_params_list)
    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt:    {prompt!r}")
        print(f"Output:    {generated_text!r}")
        print("-" * 60)


if __name__ == "__main__":
    main()
```

custom\_req\_init.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

"""This example demonstrates a special case of wrapping a request-level logits
processor, namely the case where it is necessary to utilize engine config or
environment info passed to the constructor. The subclass must override the
wrapper base class `__init__()` method to access the engine config, the device
identifier, or the flag which indicates whether pinned memory is available.

For demo purposes, a request-level dummy logits processor is employed which
causes the same token (`target_token`) to be decoded in each step. The
request-level dummy logits processor is wrapped to create a batch-level logits
processor, which can apply the logits processor to output logits from all
requests in the persistent batch in a given decode step.

The wrapped dummy logits processor below models a scenario where we must
disable the logits processor on non-"cuda" platforms. The wrapper base class
`__init__()` is overridden in order to check this condition and set a flag.

A batch is constructed with `temperature=0.0` and 50% of requests specifying
`target_token`, and for these requests - and *only* these requests - we
expect that on a "cuda" device the output will look something like:

Generated Outputs:
------------------------------------------------------------
Prompt:    'Hello, my name is'
Output:    " ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '"
------------------------------------------------------------
Prompt:    'The president of the United States is'
Output:    " not a racist. He is a racist.\nHe's a racist because he"
------------------------------------------------------------
Prompt:    'The capital of France is'
Output:    ' also also also also also also also also also also also also also
             also also also'
------------------------------------------------------------
Prompt:    'The future of AI is'
Output:    ' in the hands of the people.\n\nThe future of AI is in the'
------------------------------------------------------------

which indicates that the logits processor is running. However, on a non-"cuda"
device, the first and third requests would not repeat the same token.
"""

importtorch

fromvllmimport LLM, SamplingParams
fromvllm.configimport VllmConfig
fromvllm.loggerimport init_logger
fromvllm.v1.sample.logits_processorimport (
    AdapterLogitsProcessor,
    RequestLogitsProcessor,
)

logger = init_logger(__name__)


classDummyPerReqLogitsProcessor:
"""The request-level logits processor masks out all logits except the
    token id identified by `target_token`"""

    def__init__(self, target_token: int) -> None:
"""Specify `target_token`"""
        self.target_token = target_token

    def__call__(
        self,
        output_ids: list[int],
        logits: torch.Tensor,
    ) -> torch.Tensor:
        val_to_keep = logits[self.target_token].item()
        logits[:] = float("-inf")
        logits[self.target_token] = val_to_keep
        return logits


classWrappedPerReqLogitsProcessor(AdapterLogitsProcessor):
"""Example of overriding the wrapper class `__init__()` in order to utilize
    info about the device type"""

    @classmethod
    defvalidate_params(cls, params: SamplingParams):
        target_token = params.extra_args and params.extra_args.get("target_token")
        if target_token is not None and not isinstance(target_token, int):
            raise ValueError(
                f"`target_token` has to be an integer, got {target_token}."
            )

    def__init__(
        self, vllm_config: VllmConfig, device: torch.device, is_pin_memory: bool
    ):
        super().__init__(vllm_config, device, is_pin_memory)
        self.is_cuda = device.type == "cuda"

    defis_argmax_invariant(self) -> bool:
        return False

    defnew_req_logits_processor(
        self,
        params: SamplingParams,
    ) -> RequestLogitsProcessor | None:
"""This method returns a new request-level logits processor, customized
        to the `target_token` value associated with a particular request.

        Returns None if the logits processor should not be applied to the
        particular request. To use the logits processor the request must have
        a "target_token" custom argument with an integer value, and the device
        must be "cuda"-type

        Args:
          params: per-request sampling params

        Returns:
          `Callable` request logits processor, or None
        """
        if (
            not self.is_cuda
            or (
                target_token := params.extra_args
                and params.extra_args.get("target_token")
            )
            is None
        ):
            return None
        return DummyPerReqLogitsProcessor(target_token)


# Sample prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
# Create a mixture of requests which do and don't utilize the dummy logitproc
sampling_params_list = [
    SamplingParams(temperature=0.0, extra_args={"target_token": 128}),
    SamplingParams(temperature=0.0),
    SamplingParams(temperature=0.0, extra_args={"target_token": 67}),
    SamplingParams(temperature=0.0),
]


defmain():
    # Create an LLM.
    llm = LLM(
        model="facebook/opt-125m",
        logits_processors=[WrappedPerReqLogitsProcessor],
    )
    # Generate texts from the prompts.
    # The output is a list of RequestOutput objects
    # that contain the prompt, generated text, and other information.
    outputs = llm.generate(prompts, sampling_params_list)
    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt:    {prompt!r}")
        print(f"Output:    {generated_text!r}")
        print("-" * 60)


if __name__ == "__main__":
    main()
```