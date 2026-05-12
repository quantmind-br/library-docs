---
title: connector - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/media/connector/
source: sitemap
fetched_at: 2026-05-07T21:34:13.076704793-03:00
rendered_js: false
word_count: 51
summary: This document defines a MediaConnector class responsible for managing media input retrieval, validation, and local caching using HTTP connections and file system pathways.
tags:
    - media-processing
    - caching-logic
    - http-connector
    - file-validation
    - multi-modal
    - data-loading
category: reference
---

```
@MEDIA_CONNECTOR_REGISTRY.register("http")
classMediaConnector:
"""Configuration values can be user-provided either by --media-io-kwargs or
    by the runtime API field "media_io_kwargs". Ensure proper validation and
    error handling.
    """

    def__init__(
        self,
        media_io_kwargs: dict[str, dict[str, Any]] | None = None,
        connection: HTTPConnection = global_http_connection,
        *,
        allowed_local_media_path: str = "",
        allowed_media_domains: list[str] | None = None,
    ) -> None:
"""
        Args:
            media_io_kwargs: Additional args passed to process media
                             inputs, keyed by modalities. For example,
                             to set num_frames for video, set
                             `--media-io-kwargs '{"video":{"num_frames":40}}'`
            connection: HTTP connection client to download media contents.
            allowed_local_media_path: A local directory to load media files from.
            allowed_media_domains: If set, only media URLs that belong to this
                                   domain can be used for multi-modal inputs.
        """
        super().__init__()

        self.media_io_kwargs: dict[str, dict[str, Any]] = (
            media_io_kwargs if media_io_kwargs else {}
        )
        self.connection = connection

        if allowed_local_media_path:
            allowed_local_media_path_ = Path(allowed_local_media_path)

            if not allowed_local_media_path_.exists():
                raise ValueError(
                    "Invalid `--allowed-local-media-path`: The path "
                    f"{allowed_local_media_path_} does not exist."
                )
            if not allowed_local_media_path_.is_dir():
                raise ValueError(
                    "Invalid `--allowed-local-media-path`: The path "
                    f"{allowed_local_media_path_} must be a directory."
                )
        else:
            allowed_local_media_path_ = None

        self.allowed_local_media_path = allowed_local_media_path_
        if allowed_media_domains is None:
            allowed_media_domains = []
        self.allowed_media_domains = allowed_media_domains

        # Media download cache (opt-in via VLLM_MEDIA_CACHE)
        self._media_cache_dir: str | None = None
        self._media_cache_max_bytes: int = 0
        self._media_cache_ttl_secs: float = 0
        media_cache = envs.VLLM_MEDIA_CACHE
        if media_cache:
            try:
                os.makedirs(media_cache, exist_ok=True)
                # Verify the directory is writable before enabling caching
                with tempfile.NamedTemporaryFile(dir=media_cache, delete=True):
                    pass
                self._media_cache_dir = media_cache
                self._media_cache_max_bytes = (
                    envs.VLLM_MEDIA_CACHE_MAX_SIZE_MB * 1024 * 1024
                )
                self._media_cache_ttl_secs = envs.VLLM_MEDIA_CACHE_TTL_HOURS * 3600
                logger.info(
                    "Media cache enabled at %s (max %d MB, TTL %s hours)",
                    media_cache,
                    envs.VLLM_MEDIA_CACHE_MAX_SIZE_MB,
                    envs.VLLM_MEDIA_CACHE_TTL_HOURS,
                )
            except OSError:
                logger.warning(
                    "VLLM_MEDIA_CACHE path %s is not writable, media caching disabled",
                    media_cache,
                )

    def_get_cached_bytes(self, url: str) -> bytes | None:
"""Return cached bytes for a URL, or None if not cached/expired."""
        if not self._media_cache_dir:
            return None
        cache_path = self._media_cache_path(url)
        # Check TTL
        try:
            age = time.time() - cache_path.stat().st_mtime
        except OSError:
            return None
        if age > self._media_cache_ttl_secs:
            cache_path.unlink(missing_ok=True)
            return None
        # Touch mtime for LRU ordering
        try:
            cache_path.touch()
            return cache_path.read_bytes()
        except OSError:
            return None

    def_put_cached_bytes(self, url: str, data: bytes) -> None:
"""Store downloaded bytes and evict if over budget."""
        if not self._media_cache_dir:
            return
        cache_path = self._media_cache_path(url)
        # Atomic write via temp file + rename
        tmp_path = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="wb", dir=self._media_cache_dir, delete=False
            ) as tmp_file:
                tmp_file.write(data)
                tmp_path = tmp_file.name
            os.rename(tmp_path, str(cache_path))
        except OSError:
            # Another process beat us or disk issue
            if tmp_path is not None:
                with contextlib.suppress(OSError):
                    os.remove(tmp_path)
            return
        self._maybe_evict(exclude=cache_path)

    def_maybe_evict(self, exclude: Path | None = None) -> None:
"""Evict expired entries first, then LRU until under size limit."""
        cache_dir = Path(self._media_cache_dir)  # type: ignore[arg-type]
        entries = []
        expired = []
        total_size = 0
        now = time.time()
        for f in cache_dir.iterdir():
            if f.name.startswith("."):
                continue
            try:
                stat = f.stat()
            except OSError:
                continue
            age = now - stat.st_mtime
            if age > self._media_cache_ttl_secs:
                expired.append(f)
                continue
            total_size += stat.st_size
            # Never evict the file we just wrote
            if exclude is not None and f.name == exclude.name:
                continue
            entries.append((stat.st_mtime, stat.st_size, f))

        # Evict items according to LRU policy
        entries.sort(key=lambda e: e[0], reverse=True)
        while total_size > self._media_cache_max_bytes and entries:
            mtime, size, f = entries.pop()
            expired.append(f)
            total_size -= size

        for f in expired:
            f.unlink(missing_ok=True)

    def_media_cache_path(self, url: str) -> Path:
        url_hash = hashlib.sha256(url.encode()).hexdigest()[:20]
        ext = Path(url.split("?", 1)[0]).suffix or ""
        return Path(self._media_cache_dir) / f"{url_hash}{ext}"  # type: ignore[arg-type]

    def_load_data_url(
        self,
        url_spec: Url,
        media_io: MediaIO[_M],
    ) -> _M:  # type: ignore[type-var]
        url_spec_path = url_spec.path or ""
        data_spec, data = url_spec_path.split(",", 1)
        media_type, data_type = data_spec.split(";", 1)
        # media_type starts with a leading "/" (e.g., "/video/jpeg")
        media_type = media_type.lstrip("/")

        if data_type != "base64":
            msg = "Only base64 data URLs are supported for now."
            raise NotImplementedError(msg)

        return media_io.load_base64(media_type, data)

    def_load_file_url(
        self,
        url_spec: Url,
        media_io: MediaIO[_M],
    ) -> _M:  # type: ignore[type-var]
        allowed_local_media_path = self.allowed_local_media_path
        if allowed_local_media_path is None:
            raise RuntimeError(
                "Cannot load local files without `--allowed-local-media-path`."
            )

        url_spec_path = url_spec.path or ""
        url_spec_netloc = url_spec.netloc or ""
        filepath = Path(url2pathname(url_spec_netloc + url_spec_path))
        if allowed_local_media_path not in filepath.resolve().parents:
            raise ValueError(
                f"The file path {filepath} must be a subpath "
                f"of `--allowed-local-media-path {allowed_local_media_path}`."
            )

        return media_io.load_file(filepath)

    def_assert_url_in_allowed_media_domains(self, url_spec: Url) -> None:
        if (
            self.allowed_media_domains
            and url_spec.hostname not in self.allowed_media_domains
        ):
            raise ValueError(
                f"The URL must be from one of the allowed domains: "
                f"{self.allowed_media_domains}. Input URL domain: "
                f"{url_spec.hostname}"
            )

    defload_from_url(
        self,
        url: str,
        media_io: MediaIO[_M],
        *,
        fetch_timeout: int | None = None,
    ) -> _M:  # type: ignore[type-var]
        url_spec = parse_url(url)

        if url_spec.scheme and url_spec.scheme.startswith("http"):
            self._assert_url_in_allowed_media_domains(url_spec)

            cached = self._get_cached_bytes(url)
            if cached is not None:
                return media_io.load_bytes(cached)

            connection = self.connection
            data = connection.get_bytes(
                url_spec.url,
                timeout=fetch_timeout,
                allow_redirects=envs.VLLM_MEDIA_URL_ALLOW_REDIRECTS,
            )

            self._put_cached_bytes(url, data)
            return media_io.load_bytes(data)

        if url_spec.scheme == "data":
            return self._load_data_url(url_spec, media_io)

        if url_spec.scheme == "file":
            return self._load_file_url(url_spec, media_io)

        msg = "The URL must be either a HTTP, data or file URL."
        raise ValueError(msg)

    async defload_from_url_async(
        self,
        url: str,
        media_io: MediaIO[_M],
        *,
        fetch_timeout: int | None = None,
    ) -> _M:
        url_spec = parse_url(url)
        loop = asyncio.get_running_loop()

        if url_spec.scheme and url_spec.scheme.startswith("http"):
            self._assert_url_in_allowed_media_domains(url_spec)

            cached = await loop.run_in_executor(
                global_thread_pool, self._get_cached_bytes, url
            )
            if cached is not None:
                future = loop.run_in_executor(
                    global_thread_pool, media_io.load_bytes, cached
                )
                return await future

            connection = self.connection
            data = await connection.async_get_bytes(
                url_spec.url,
                timeout=fetch_timeout,
                allow_redirects=envs.VLLM_MEDIA_URL_ALLOW_REDIRECTS,
            )

            await loop.run_in_executor(
                global_thread_pool, self._put_cached_bytes, url, data
            )
            future = loop.run_in_executor(global_thread_pool, media_io.load_bytes, data)
            return await future

        if url_spec.scheme == "data":
            future = loop.run_in_executor(
                global_thread_pool, self._load_data_url, url_spec, media_io
            )
            return await future

        if url_spec.scheme == "file":
            future = loop.run_in_executor(
                global_thread_pool, self._load_file_url, url_spec, media_io
            )
            return await future
        msg = "The URL must be either a HTTP, data or file URL."
        raise ValueError(msg)

    deffetch_audio(
        self,
        audio_url: str,
    ) -> tuple[np.ndarray, int | float]:
"""
        Load audio from a URL.
        """
        audio_io = AudioMediaIO(**self.media_io_kwargs.get("audio", {}))

        return self.load_from_url(
            audio_url,
            audio_io,
            fetch_timeout=envs.VLLM_AUDIO_FETCH_TIMEOUT,
        )

    async deffetch_audio_async(
        self,
        audio_url: str,
    ) -> tuple[np.ndarray, int | float]:
"""
        Asynchronously fetch audio from a URL.
        """
        audio_io = AudioMediaIO(**self.media_io_kwargs.get("audio", {}))

        return await self.load_from_url_async(
            audio_url,
            audio_io,
            fetch_timeout=envs.VLLM_AUDIO_FETCH_TIMEOUT,
        )

    deffetch_image(
        self,
        image_url: str,
        *,
        image_mode: str = "RGB",
    ) -> Image.Image:
"""
        Load a PIL image from an HTTP or base64 data URL.

        By default, the image is converted into RGB format.
        """
        image_io = ImageMediaIO(
            image_mode=image_mode, **self.media_io_kwargs.get("image", {})
        )

        try:
            return self.load_from_url(
                image_url,
                image_io,
                fetch_timeout=envs.VLLM_IMAGE_FETCH_TIMEOUT,
            )
        except UnidentifiedImageError as e:
            # convert to ValueError to be properly caught upstream
            raise ValueError(str(e)) frome

    async deffetch_image_async(
        self,
        image_url: str,
        *,
        image_mode: str = "RGB",
    ) -> Image.Image:
"""
        Asynchronously load a PIL image from an HTTP or base64 data URL.

        By default, the image is converted into RGB format.
        """
        image_io = ImageMediaIO(
            image_mode=image_mode, **self.media_io_kwargs.get("image", {})
        )

        try:
            return await self.load_from_url_async(
                image_url,
                image_io,
                fetch_timeout=envs.VLLM_IMAGE_FETCH_TIMEOUT,
            )
        except UnidentifiedImageError as e:
            # convert to ValueError to be properly caught upstream
            raise ValueError(str(e)) frome

    deffetch_video(
        self,
        video_url: str,
        *,
        image_mode: str = "RGB",
    ) -> tuple[npt.NDArray, dict[str, Any]]:
"""
        Load video from an HTTP or base64 data URL.
        """
        image_io = ImageMediaIO(
            image_mode=image_mode, **self.media_io_kwargs.get("image", {})
        )
        video_io = VideoMediaIO(image_io, **self.media_io_kwargs.get("video", {}))

        return self.load_from_url(
            video_url,
            video_io,
            fetch_timeout=envs.VLLM_VIDEO_FETCH_TIMEOUT,
        )

    async deffetch_video_async(
        self,
        video_url: str,
        *,
        image_mode: str = "RGB",
    ) -> tuple[npt.NDArray, dict[str, Any]]:
"""
        Asynchronously load video from an HTTP or base64 data URL.

        By default, the image is converted into RGB format.
        """
        image_io = ImageMediaIO(
            image_mode=image_mode, **self.media_io_kwargs.get("image", {})
        )
        video_io = VideoMediaIO(image_io, **self.media_io_kwargs.get("video", {}))

        return await self.load_from_url_async(
            video_url,
            video_io,
            fetch_timeout=envs.VLLM_VIDEO_FETCH_TIMEOUT,
        )

    deffetch_image_embedding(
        self,
        data: str,
    ) -> torch.Tensor:
"""
        Load image embedding from a URL.
        """
        image_embedding_io = ImageEmbeddingMediaIO()

        return image_embedding_io.load_base64("", data)

    deffetch_audio_embedding(
        self,
        data: str,
    ) -> torch.Tensor:
"""
        Load audio embedding from a URL.
        """
        audio_embedding_io = AudioEmbeddingMediaIO()

        return audio_embedding_io.load_base64("", data)
```