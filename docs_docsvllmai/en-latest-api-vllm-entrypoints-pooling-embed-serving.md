---
title: serving - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/embed/serving/
source: sitemap
fetched_at: 2026-05-07T21:21:00.967369293-03:00
rendered_js: false
word_count: 0
summary: This document defines a serving class that standardizes embedding API responses by supporting both OpenAI and Cohere output formats.
tags:
    - embedding-api
    - openai-compatibility
    - cohere-compatibility
    - response-formatting
    - python-backend
    - data-serialization
category: api
---

```
classServingEmbedding(PoolingServing):
"""Embedding API supporting both OpenAI and Cohere formats."""

    request_id_prefix = "embd"
    io_processor: EmbedIOProcessor

    def__init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.json_response_cls = get_json_response_cls()

    definit_io_processor(self, *args, **kwargs) -> EmbedIOProcessor:
        return EmbedIOProcessor(*args, **kwargs)

    def_build_response(
        self,
        ctx: PoolingServeContext,
    ) -> Response:
        if isinstance(ctx.request, CohereEmbedRequest):
            return self._build_cohere_response_from_ctx(ctx)
        return self._build_openai_response(ctx)

    def_build_openai_response(
        self,
        ctx: EmbeddingServeContext,
    ) -> JSONResponse | StreamingResponse:
        encoding_format = ctx.request.encoding_format
        embed_dtype = ctx.request.embed_dtype
        endianness = ctx.request.endianness

        if encoding_format == "float" or encoding_format == "base64":
            return self._openai_json_response(
                ctx.final_res_batch,
                ctx.request_id,
                ctx.created_time,
                ctx.model_name,
                encoding_format,
                embed_dtype,
                endianness,
            )

        if encoding_format == "bytes" or encoding_format == "bytes_only":
            return self._openai_bytes_response(
                ctx.final_res_batch,
                ctx.request_id,
                ctx.created_time,
                ctx.model_name,
                encoding_format,
                embed_dtype,
                endianness,
            )

        assert_never(encoding_format)

    def_openai_json_response(
        self,
        final_res_batch: list[PoolingRequestOutput],
        request_id: str,
        created_time: int,
        model_name: str,
        encoding_format: Literal["float", "base64"],
        embed_dtype: EmbedDType,
        endianness: Endianness,
    ) -> JSONResponse:
        encode_fn = cast(
            Callable[[PoolingRequestOutput], list[float] | str],
            (
                encode_pooling_output_float
                if encoding_format == "float"
                else partial(
                    encode_pooling_output_base64,
                    embed_dtype=embed_dtype,
                    endianness=endianness,
                )
            ),
        )

        items: list[EmbeddingResponseData] = []
        num_prompt_tokens = 0

        for idx, final_res in enumerate(final_res_batch):
            item = EmbeddingResponseData(
                index=idx,
                embedding=encode_fn(final_res),
            )
            prompt_token_ids = final_res.prompt_token_ids

            items.append(item)
            num_prompt_tokens += len(prompt_token_ids)

        usage = UsageInfo(
            prompt_tokens=num_prompt_tokens,
            total_tokens=num_prompt_tokens,
        )

        response = EmbeddingResponse(
            id=request_id,
            created=created_time,
            model=model_name,
            data=items,
            usage=usage,
        )
        return self.json_response_cls(content=response.model_dump())

    def_openai_bytes_response(
        self,
        final_res_batch: list[PoolingRequestOutput],
        request_id: str,
        created_time: int,
        model_name: str,
        encoding_format: Literal["bytes", "bytes_only"],
        embed_dtype: EmbedDType,
        endianness: Endianness,
    ) -> StreamingResponse:
        content, items, usage = encode_pooling_bytes(
            pooling_outputs=final_res_batch,
            embed_dtype=embed_dtype,
            endianness=endianness,
        )

        headers = (
            None
            if encoding_format == "bytes_only"
            else {
                "metadata": json.dumps(
                    {
                        "id": request_id,
                        "created": created_time,
                        "model": model_name,
                        "data": items,
                        "usage": usage,
                    }
                )
            }
        )

        response = EmbeddingBytesResponse(content=content, headers=headers)
        return StreamingResponse(
            content=response.content,
            headers=response.headers,
            media_type=response.media_type,
        )

    def_build_cohere_response_from_ctx(
        self,
        ctx: PoolingServeContext,
    ) -> JSONResponse:
        request = ctx.request
        assert isinstance(request, CohereEmbedRequest)

        all_floats = [encode_pooling_output_float(out) for out in ctx.final_res_batch]
        total_tokens = sum(len(out.prompt_token_ids) for out in ctx.final_res_batch)

        image_tokens = total_tokens if request.images is not None else 0
        texts_echo = request.texts

        embedding_types = request.embedding_types or ["float"]
        embeddings_obj = build_typed_embeddings(all_floats, embedding_types)

        input_tokens = total_tokens - image_tokens
        response = CohereEmbedResponse(
            id=ctx.request_id,
            embeddings=embeddings_obj,
            texts=texts_echo,
            meta=CohereMeta(
                billed_units=CohereBilledUnits(
                    input_tokens=input_tokens,
                    image_tokens=image_tokens,
                ),
            ),
        )
        return self.json_response_cls(content=response.model_dump(exclude_none=True))
```