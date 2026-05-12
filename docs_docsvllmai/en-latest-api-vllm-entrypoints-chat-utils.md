---
title: chat_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/chat_utils/
source: sitemap
fetched_at: 2026-05-07T21:19:21.065707193-03:00
rendered_js: false
word_count: 15
summary: This class provides an asynchronous interface for parsing and tracking multi-modal content, such as images, audio, video, and embeddings, for use in machine learning model processing.
tags:
    - asyncio
    - multi-modal
    - data-parsing
    - media-processing
    - embeddings
    - python-class
category: reference
---

```
classAsyncMultiModalContentParser(BaseMultiModalContentParser):
    def__init__(
        self,
        tracker: AsyncMultiModalItemTracker,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ) -> None:
        super().__init__()

        self._tracker = tracker
        self._connector: MediaConnector = MEDIA_CONNECTOR_REGISTRY.load(
            envs.VLLM_MEDIA_CONNECTOR,
            media_io_kwargs=tracker.media_io_kwargs,
            allowed_local_media_path=tracker.allowed_local_media_path,
            allowed_media_domains=tracker.allowed_media_domains,
        )
        self._mm_processor_kwargs: dict[str, Any] | None = mm_processor_kwargs

    @property
    defmodel_config(self) -> ModelConfig:
        return self._tracker.model_config

    @override
    defparse_prompt_embeds(self, data: str) -> None:
"""Schedule async prompt embeds decode and store the coroutine in the tracker.

        Like the sync variant, emits a single sentinel `PROMPT_EMBEDS_PLACEHOLDER_TOKEN`
        per content part. Unlike the sync variant, the tensor decode is deferred to a
        thread-pool executor via `safe_load_prompt_embeds_async`.
        """
        if not self.model_config.enable_prompt_embeds:
            raise ValueError(_ENABLE_PROMPT_EMBEDS_ERROR)

        coro = self._load_prompt_embeds_async(data.encode())
        self._tracker.add("prompt_embeds", coro)
        self._add_placeholder("prompt_embeds", PROMPT_EMBEDS_PLACEHOLDER_TOKEN)

    async def_load_prompt_embeds_async(
        self, data_bytes: bytes
    ) -> tuple[torch.Tensor, None]:
        # Second tuple slot fills the tracker's generic `(item, uuid | None)`
        # contract. prompt_embeds has no UUID concept, so it's always `None`.
        tensor = await safe_load_prompt_embeds_async(self.model_config, data_bytes)
        return tensor, None

    async def_image_with_uuid_async(self, image_url: str | None, uuid: str | None):
        image = (
            await self._connector.fetch_image_async(image_url) if image_url else None
        )
        return image, uuid

    defparse_image(self, image_url: str | None, uuid: str | None = None) -> None:
        coro = self._image_with_uuid_async(image_url, uuid)

        placeholder = self._tracker.add("image", coro)
        self._add_placeholder("image", placeholder)

    defparse_image_embeds(
        self,
        image_embeds: str | dict[str, str] | None,
        uuid: str | None = None,
    ) -> None:
        mm_config = self.model_config.get_multimodal_config()
        if not mm_config.enable_mm_embeds:
            raise ValueError(
                "You must set `--enable-mm-embeds` to input `image_embeds`"
            )

        future = asyncio.Future[
            tuple[torch.Tensor | dict[str, torch.Tensor] | None, str | None]
        ]()

        if isinstance(image_embeds, dict):
            embeds = {
                k: self._connector.fetch_image_embedding(v)
                for k, v in image_embeds.items()
            }
            future.set_result((embeds, uuid))

        if isinstance(image_embeds, str):
            embedding = self._connector.fetch_image_embedding(image_embeds)
            future.set_result((embedding, uuid))

        if image_embeds is None:
            future.set_result((None, uuid))

        placeholder = self._tracker.add("image_embeds", future)
        self._add_placeholder("image", placeholder)

    defparse_audio_embeds(
        self,
        audio_embeds: str | dict[str, str] | None,
        uuid: str | None = None,
    ) -> None:
        mm_config = self.model_config.get_multimodal_config()
        if not mm_config.enable_mm_embeds:
            raise ValueError(
                "You must set `--enable-mm-embeds` to input `audio_embeds`"
            )

        future = asyncio.Future[
            tuple[torch.Tensor | dict[str, torch.Tensor] | None, str | None]
        ]()

        if isinstance(audio_embeds, dict):
            embeds = {
                k: self._connector.fetch_audio_embedding(v)
                for k, v in audio_embeds.items()
            }
            future.set_result((embeds, uuid))

        if isinstance(audio_embeds, str):
            embedding = self._connector.fetch_audio_embedding(audio_embeds)
            future.set_result((embedding, uuid))

        if audio_embeds is None:
            future.set_result((None, uuid))

        placeholder = self._tracker.add("audio_embeds", future)
        self._add_placeholder("audio", placeholder)

    defparse_image_pil(
        self,
        image_pil: Image.Image | None,
        uuid: str | None = None,
    ) -> None:
        future = asyncio.Future[tuple[Image.Image | None, str | None]]()
        if image_pil:
            future.set_result((image_pil, uuid))
        else:
            future.set_result((None, uuid))

        placeholder = self._tracker.add("image", future)
        self._add_placeholder("image", placeholder)

    async def_audio_with_uuid_async(self, audio_url: str | None, uuid: str | None):
        audio = (
            await self._connector.fetch_audio_async(audio_url) if audio_url else None
        )
        return audio, uuid

    defparse_audio(self, audio_url: str | None, uuid: str | None = None) -> None:
        coro = self._audio_with_uuid_async(audio_url, uuid)

        placeholder = self._tracker.add("audio", coro)
        self._add_placeholder("audio", placeholder)

    defparse_input_audio(
        self, input_audio: InputAudio | None, uuid: str | None = None
    ) -> None:
        if input_audio:
            audio_data = input_audio.get("data", "")
            audio_format = input_audio.get("format", "")
            if audio_data:
                audio_url = f"data:audio/{audio_format};base64,{audio_data}"
            else:
                # If a UUID is provided, audio data may be empty.
                audio_url = None
        else:
            audio_url = None

        return self.parse_audio(audio_url, uuid)

    async def_video_with_uuid_async(self, video_url: str | None, uuid: str | None):
        video = (
            await self._connector.fetch_video_async(video_url) if video_url else None
        )
        return video, uuid

    defparse_video(self, video_url: str | None, uuid: str | None = None) -> None:
        coro = self._video_with_uuid_async(video_url, uuid)

        placeholder = self._tracker.add("video", coro)
        self._add_placeholder("video", placeholder)

        # Extract audio from video if use_audio_in_video is True
        if (
            video_url
            and self._mm_processor_kwargs
            and self._mm_processor_kwargs.get("use_audio_in_video", False)
        ):
            audio_coro = self._audio_with_uuid_async(video_url, uuid)
            audio_placeholder = self._tracker.add("audio", audio_coro)
            self._add_placeholder("audio", audio_placeholder)
```