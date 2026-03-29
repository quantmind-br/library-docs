---
title: LM - DSPy
url: https://dspy.ai/api/models/LM/
source: sitemap
fetched_at: 2026-01-23T08:01:42.137682665-03:00
rendered_js: false
word_count: 5
summary: This document defines the initialization method for language model instances within the DSPy framework, detailing parameters for model configuration, caching, and execution. It includes specialized logic for handling parameters like temperature and token limits for specific reasoning model families.
tags:
    - dspy
    - language-models
    - api-reference
    - llm-configuration
    - python-sdk
    - model-initialization
category: api
---

```
def__init__(
    self,
    model: str,
    model_type: Literal["chat", "text", "responses"] = "chat",
    temperature: float | None = None,
    max_tokens: int | None = None,
    cache: bool = True,
    callbacks: list[BaseCallback] | None = None,
    num_retries: int = 3,
    provider: Provider | None = None,
    finetuning_model: str | None = None,
    launch_kwargs: dict[str, Any] | None = None,
    train_kwargs: dict[str, Any] | None = None,
    use_developer_role: bool = False,
    **kwargs,
):
"""
    Create a new language model instance for use with DSPy modules and programs.

    Args:
        model: The model to use. This should be a string of the form ``"llm_provider/llm_name"``
               supported by LiteLLM. For example, ``"openai/gpt-4o"``.
        model_type: The type of the model, either ``"chat"`` or ``"text"``.
        temperature: The sampling temperature to use when generating responses.
        max_tokens: The maximum number of tokens to generate per response.
        cache: Whether to cache the model responses for reuse to improve performance
               and reduce costs.
        callbacks: A list of callback functions to run before and after each request.
        num_retries: The number of times to retry a request if it fails transiently due to
                     network error, rate limiting, etc. Requests are retried with exponential
                     backoff.
        provider: The provider to use. If not specified, the provider will be inferred from the model.
        finetuning_model: The model to finetune. In some providers, the models available for finetuning is different
            from the models available for inference.
        rollout_id: Optional integer used to differentiate cache entries for otherwise
            identical requests. Different values bypass DSPy's caches while still caching
            future calls with the same inputs and rollout ID. Note that `rollout_id`
            only affects generation when `temperature` is non-zero. This argument is
            stripped before sending requests to the provider.
    """
    # Remember to update LM.copy() if you modify the constructor!
    self.model = model
    self.model_type = model_type
    self.cache = cache
    self.provider = provider or self.infer_provider()
    self.callbacks = callbacks or []
    self.history = []
    self.num_retries = num_retries
    self.finetuning_model = finetuning_model
    self.launch_kwargs = launch_kwargs or {}
    self.train_kwargs = train_kwargs or {}
    self.use_developer_role = use_developer_role
    self._warned_zero_temp_rollout = False

    # Handle model-specific configuration for different model families
    model_family = model.split("/")[-1].lower() if "/" in model else model.lower()

    # Recognize OpenAI reasoning models (o1, o3, o4, gpt-5 family)
    # Exclude non-reasoning variants like gpt-5-chat this is in azure ai foundry
    # Allow date suffixes like -2023-01-01 after model name or mini/nano/pro
    # For gpt-5, use negative lookahead to exclude -chat and allow other suffixes
    model_pattern = re.match(
        r"^(?:o[1345](?:-(?:mini|nano|pro))?(?:-\d{4}-\d{2}-\d{2})?|gpt-5(?!-chat)(?:-.*)?)$",
        model_family,
    )

    if model_pattern:
        if (temperature and temperature != 1.0) or (max_tokens and max_tokens < 16000):
            raise ValueError(
                "OpenAI's reasoning models require passing temperature=1.0 or None and max_tokens >= 16000 or None to "
                "`dspy.LM(...)`, e.g., dspy.LM('openai/gpt-5', temperature=1.0, max_tokens=16000)"
            )
        self.kwargs = dict(temperature=temperature, max_completion_tokens=max_tokens, **kwargs)
        if self.kwargs.get("rollout_id") is None:
            self.kwargs.pop("rollout_id", None)
    else:
        self.kwargs = dict(temperature=temperature, max_tokens=max_tokens, **kwargs)
        if self.kwargs.get("rollout_id") is None:
            self.kwargs.pop("rollout_id", None)

    self._warn_zero_temp_rollout(self.kwargs.get("temperature"), self.kwargs.get("rollout_id"))
```