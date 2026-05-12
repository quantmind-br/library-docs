---
title: Speech-to-Text (Transcription/Translation) Support - vLLM
url: https://docs.vllm.ai/en/latest/contributing/model/transcription/
source: sitemap
fetched_at: 2026-05-07T21:11:31.725332794-03:00
rendered_js: false
word_count: 507
summary: This guide provides instructions for implementing the SupportsTranscription interface in vLLM to add support for speech-to-text and translation models.
tags:
    - vllm
    - speech-to-text
    - asr
    - model-integration
    - machine-learning
    - audio-processing
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/contributing/model/transcription.md "Edit this page")

This document walks you through the steps to add support for speech-to-text (ASR) models to vLLM’s transcription and translation APIs by implementing [SupportsTranscription](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription "            SupportsTranscription"). Please refer to the [supported models](https://docs.vllm.ai/en/latest/models/supported_models/#transcription) for further guidance.

## Update the base vLLM model[¶](#update-the-base-vllm-model "Permanent link")

It is assumed you have already implemented your model in vLLM according to the basic model guide. Extend your model with the [SupportsTranscription](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription "            SupportsTranscription") interface and implement the following class attributes and methods.

### `supported_languages` and `supports_transcription_only`[¶](#supported_languages-and-supports_transcription_only "Permanent link")

Declare supported languages and capabilities:

- The `supported_languages` mapping is validated at init time.
- Set `supports_transcription_only=True` if the model should not serve text generation (eg Whisper).

supported\_languages and supports\_transcription\_only

```
fromtypingimport ClassVar, Mapping, Literal
importnumpyasnp
importtorch
fromtorchimport nn

fromvllm.configimport ModelConfig, SpeechToTextConfig
fromvllm.inputsimport PromptType
fromvllm.model_executor.models.interfacesimport SupportsTranscription

classYourASRModel(nn.Module, SupportsTranscription):
    # Map of ISO 639-1 language codes to language names
    supported_languages: ClassVar[Mapping[str, str]] = {
        "en": "English",
        "it": "Italian",
        # ... add more as needed
    }

    # If your model only supports audio-conditioned generation
    # (no text-only generation), enable this flag.
    supports_transcription_only: ClassVar[bool] = True
```

Provide an ASR configuration via [get\_speech\_to\_text\_config](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.get_speech_to_text_config "            get_speech_to_text_config            classmethod   ").

This is for controlling general behavior of the API when serving your model:

get\_speech\_to\_text\_config()

```
classYourASRModel(nn.Module, SupportsTranscription):
    ...

    @classmethod
    defget_speech_to_text_config(
        cls,
        model_config: ModelConfig,
        task_type: Literal["transcribe", "translate"],
    ) -> SpeechToTextConfig:
        return SpeechToTextConfig(
            sample_rate=16_000,
            max_audio_clip_s=30,
            # Set to None to disable server-side chunking if your
            # model/processor handles it already
            min_energy_split_window_size=None,
        )
```

See [Audio preprocessing and chunking](#audio-preprocessing-and-chunking) for what each field controls.

Implement the prompt construction via [get\_generation\_prompt](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.get_generation_prompt "            get_generation_prompt            classmethod   "). The server builds a [SpeechToTextParams](https://docs.vllm.ai/en/latest/api/vllm/config/speech_to_text/#vllm.config.speech_to_text.SpeechToTextParams "            SpeechToTextParams            dataclass   ") object that bundles the resampled waveform, task parameters, and request-specific options. Your model receives this single object and returns a valid [PromptType](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.PromptType "            PromptType            module-attribute   "). There are two common patterns:

#### Multimodal LLM with audio embeddings (e.g., Voxtral, Gemma3n)[¶](#multimodal-llm-with-audio-embeddings-eg-voxtral-gemma3n "Permanent link")

Return a dict containing `multi_modal_data` with the audio, and either a `prompt` string or `prompt_token_ids`:

get\_generation\_prompt()

```
fromvllm.config.speech_to_textimport SpeechToTextParams

classYourASRModel(nn.Module, SupportsTranscription):
    ...

    @classmethod
    defget_generation_prompt(
        cls,
        stt_params: SpeechToTextParams,
    ) -> PromptType:
        audio = stt_params.audio
        stt_config = stt_params.stt_config
        task_type = stt_params.task_type

        task_word = "Transcribe" if task_type == "transcribe" else "Translate"
        prompt = (
            "<start_of_turn>user\n"
            f"{task_word} this audio: <audio_soft_token>"
            "<end_of_turn>\n<start_of_turn>model\n"
        )

        return {
            "multi_modal_data": {"audio": (audio, stt_config.sample_rate)},
            "prompt": prompt,
        }
```

For further clarification on multi modal inputs, please refer to [Multi-Modal Inputs](https://docs.vllm.ai/en/latest/features/multimodal_inputs/).

#### Encoder–decoder audio-only (e.g., Whisper)[¶](#encoderdecoder-audio-only-eg-whisper "Permanent link")

Return a dict with separate `encoder_prompt` and `decoder_prompt` entries:

get\_generation\_prompt()

```
fromvllm.config.speech_to_textimport SpeechToTextParams

classYourASRModel(nn.Module, SupportsTranscription):
    ...

    @classmethod
    defget_generation_prompt(
        cls,
        stt_params: SpeechToTextParams,
    ) -> PromptType:
        audio = stt_params.audio
        stt_config = stt_params.stt_config
        language = stt_params.language
        task_type = stt_params.task_type
        request_prompt = stt_params.request_prompt

        if language is None:
            raise ValueError("Language must be specified")

        prompt = {
            "encoder_prompt": {
                "prompt": "",
                "multi_modal_data": {
                    "audio": (audio, stt_config.sample_rate),
                },
            },
            "decoder_prompt": (
                (f"<|prev|>{request_prompt}" if request_prompt else "")
                + f"<|startoftranscript|><|{language}|>"
                + f"<|{task_type}|><|notimestamps|>"
            ),
        }
        return cast(PromptType, prompt)
```

### `validate_language` (optional)[¶](#validate_language-optional "Permanent link")

Language validation via [validate\_language](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.validate_language "            validate_language            classmethod   ")

If your model requires a language and you want a default, override this method (see Whisper):

validate\_language()

```
@classmethod
defvalidate_language(cls, language: str | None) -> str | None:
    if language is None:
        logger.warning(
            "Defaulting to language='en'. If you wish to transcribe "
            "audio in a different language, pass the `language` field "
            "in the TranscriptionRequest."
        )
        language = "en"
    return super().validate_language(language)
```

### `get_num_audio_tokens` (optional)[¶](#get_num_audio_tokens-optional "Permanent link")

Token accounting for streaming via [get\_num\_audio\_tokens](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.get_num_audio_tokens "            get_num_audio_tokens            classmethod   ")

Provide a fast duration→token estimate to improve streaming usage statistics:

get\_num\_audio\_tokens()

```
classYourASRModel(nn.Module, SupportsTranscription):
    ...

    @classmethod
    defget_num_audio_tokens(
        cls,
        audio_duration_s: float,
        stt_config: SpeechToTextConfig,
        model_config: ModelConfig,
    ) -> int | None:
        # Return None if unknown; otherwise return an estimate.
        return int(audio_duration_s * stt_config.sample_rate // 320)  # example
```

## Audio preprocessing and chunking[¶](#audio-preprocessing-and-chunking "Permanent link")

The API server takes care of basic audio I/O and optional chunking before building prompts:

- Resampling: Input audio is resampled to `SpeechToTextConfig.sample_rate` using [`AudioResampler`](https://docs.vllm.ai/en/latest/api/vllm/multimodal/audio/#vllm.multimodal.audio.AudioResampler "            AudioResampler").
- Chunking: If `SpeechToTextConfig.allow_audio_chunking` is True and the duration exceeds `max_audio_clip_s`, the server splits the audio into overlapping chunks and generates a prompt per chunk. Overlap is controlled by `overlap_chunk_second`.
- Energy-aware splitting: When `min_energy_split_window_size` is set, the server finds low-energy regions to minimize cutting within words.

Relevant server logic:

\_preprocess\_speech\_to\_text()

```
# vllm/entrypoints/openai/speech_to_text.py
async def_preprocess_speech_to_text(...):
    language = self.model_cls.validate_language(request.language)
    ...
    y, sr = load_audio(bytes_, sr=self.asr_config.sample_rate)
    duration = get_audio_duration(y=y, sr=sr)
    do_split_audio = (self.asr_config.allow_audio_chunking
                    and duration > self.asr_config.max_audio_clip_s)
    chunks = [y] if not do_split_audio else self._split_audio(y, int(sr))
    prompts = []
    for chunk in chunks:
        stt_params = request.build_stt_params(
            audio=chunk,
            stt_config=self.asr_config,
            model_config=self.model_config,
            task_type=self.task_type,
        )
        prompt = self.model_cls.get_generation_prompt(stt_params)
        prompts.append(prompt)
    return prompts, duration
```

## Exposing tasks automatically[¶](#exposing-tasks-automatically "Permanent link")

vLLM automatically advertises transcription support if your model implements the interface:

```
if supports_transcription(model):
    if model.supports_transcription_only:
        return ["transcription"]
    supported_tasks.append("transcription")
```

When enabled, the server initializes the transcription and translation handlers:

```
state.openai_serving_transcription = OpenAIServingTranscription(...) if "transcription" in supported_tasks else None
state.openai_serving_translation = OpenAIServingTranslation(...) if "transcription" in supported_tasks else None
```

No extra registration is required beyond having your model class available via the model registry and implementing [`SupportsTranscription`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription "            SupportsTranscription").

## Examples in-tree[¶](#examples-in-tree "Permanent link")

- Whisper encoder–decoder (audio-only): [vllm/model\_executor/models/whisper.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/whisper.py)
- Voxtral decoder-only (audio embeddings + LLM): [vllm/model\_executor/models/voxtral.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/voxtral.py). Make sure to have installed `mistral-common[audio]`.
- Gemma3n decoder-only with fixed instruction prompt: [vllm/model\_executor/models/gemma3n\_mm.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma3n_mm.py)
- Qwen3-Omni multimodal with audio embeddings: [vllm/model\_executor/models/qwen3\_omni\_moe\_thinker.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/qwen3_omni_moe_thinker.py)

## Test with the API[¶](#test-with-the-api "Permanent link")

Once your model implements [`SupportsTranscription`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription "            SupportsTranscription"), you can test the endpoints (API mimics OpenAI):

- Transcription (ASR):
  
  ```
  curl-s-XPOST\
  -H"Authorization: Bearer $VLLM_API_KEY"\
  -H"Content-Type: multipart/form-data"\
  -F"file=@/path/to/audio.wav"\
  -F"model=$MODEL_ID"\
  http://localhost:8000/v1/audio/transcriptions
  ```
- Translation (source → English unless otherwise supported):
  
  ```
  curl-s-XPOST\
  -H"Authorization: Bearer $VLLM_API_KEY"\
  -H"Content-Type: multipart/form-data"\
  -F"file=@/path/to/audio.wav"\
  -F"model=$MODEL_ID"\
  http://localhost:8000/v1/audio/translations
  ```

Or check out more examples in [examples/online\_serving](https://github.com/vllm-project/vllm/tree/main/examples/online_serving).

Note

- If your model handles chunking internally (e.g., via its processor or encoder), set `min_energy_split_window_size=None` in the returned [`SpeechToTextConfig`](https://docs.vllm.ai/en/latest/api/vllm/config/speech_to_text/#vllm.config.speech_to_text.SpeechToTextConfig "            SpeechToTextConfig") to disable server-side chunking.
- Implementing `get_num_audio_tokens` improves accuracy of streaming usage metrics (`prompt_tokens`) without an extra forward pass.
- For multilingual behavior, keep `supported_languages` aligned with actual model capabilities.