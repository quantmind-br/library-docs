---
title: interface - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/plugins/io_processors/interface/
source: sitemap
fetched_at: 2026-05-07T21:34:39.881584904-03:00
rendered_js: false
word_count: 12
summary: Defines the IOProcessor abstract base class for implementing custom pre-processing and post-processing logic for vLLM engine input and output data.
tags:
    - python
    - vllm
    - abstract-base-class
    - io-processing
    - plugin-interface
    - api-interface
category: reference
---

```
classIOProcessor(ABC, Generic[IOProcessorInput, IOProcessorOutput]):
"""Abstract interface for pre/post-processing of engine I/O."""

    def__init__(self, vllm_config: VllmConfig, renderer: BaseRenderer):
        super().__init__()

        self.vllm_config = vllm_config

    defparse_data(self, data: object) -> IOProcessorInput:
        if callable(parse_request := getattr(self, "parse_request", None)):
            warnings.warn(
                "`parse_request` has been renamed to `parse_data`. "
                "Please update your IO Processor Plugin to use the new name. "
                "The old name will be removed in v0.19.",
                DeprecationWarning,
                stacklevel=2,
            )

            return parse_request(data)  # type: ignore

        raise NotImplementedError

    defmerge_sampling_params(
        self,
        params: SamplingParams | None = None,
    ) -> SamplingParams:
        if callable(
            validate_or_generate_params := getattr(
                self, "validate_or_generate_params", None
            )
        ):
            warnings.warn(
                "`validate_or_generate_params` has been split into "
                "`merge_sampling_params` and `merge_pooling_params`."
                "Please update your IO Processor Plugin to use the new methods. "
                "The old name will be removed in v0.19.",
                DeprecationWarning,
                stacklevel=2,
            )

            return validate_or_generate_params(params)  # type: ignore

        return params or SamplingParams()

    defmerge_pooling_params(
        self,
        params: PoolingParams | None = None,
    ) -> PoolingParams:
        if callable(
            validate_or_generate_params := getattr(
                self, "validate_or_generate_params", None
            )
        ):
            warnings.warn(
                "`validate_or_generate_params` has been split into "
                "`merge_sampling_params` and `merge_pooling_params`."
                "Please update your IO Processor Plugin to use the new methods. "
                "The old name will be removed in v0.19.",
                DeprecationWarning,
                stacklevel=2,
            )

            return validate_or_generate_params(params)  # type: ignore

        return params or PoolingParams(task="plugin")

    @abstractmethod
    defpre_process(
        self,
        prompt: IOProcessorInput,
        request_id: str | None = None,
        **kwargs,
    ) -> PromptType | Sequence[PromptType]:
        raise NotImplementedError

    async defpre_process_async(
        self,
        prompt: IOProcessorInput,
        request_id: str | None = None,
        **kwargs,
    ) -> PromptType | Sequence[PromptType]:
        return self.pre_process(prompt, request_id, **kwargs)

    @abstractmethod
    defpost_process(
        self,
        model_output: Sequence[PoolingRequestOutput],
        request_id: str | None = None,
        **kwargs,
    ) -> IOProcessorOutput:
        raise NotImplementedError

    async defpost_process_async(
        self,
        model_output: AsyncGenerator[tuple[int, PoolingRequestOutput]],
        request_id: str | None = None,
        **kwargs,
    ) -> IOProcessorOutput:
        # We cannot guarantee outputs are returned in the same order they were
        # fed to vLLM.
        # Let's sort them by id before post_processing
        sorted_output = sorted(
            [(i, item) async for i, item in model_output], key=lambda output: output[0]
        )
        collected_output = [output[1] for output in sorted_output]
        return self.post_process(collected_output, request_id=request_id, **kwargs)
```