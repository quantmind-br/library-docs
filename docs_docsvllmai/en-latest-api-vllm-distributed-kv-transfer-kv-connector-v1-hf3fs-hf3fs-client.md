---
title: hf3fs_client - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_client/
source: sitemap
fetched_at: 2026-05-07T21:18:16.27529301-03:00
rendered_js: false
word_count: 0
summary: This document defines a Python client class for managing high-performance file system (HF3FS) I/O operations, including batch read and write capabilities integrated with PyTorch and CUDA streams.
tags:
    - python
    - hf3fs
    - pytorch
    - cuda
    - io-operations
    - shared-memory
    - file-system
category: api
---

```
classHf3fsClient:
    def__init__(self, path: str, size: int, bytes_per_page: int, entries: int):
"""Initialize the HF3FS client with hf3fs_fuse.

        Args:
            path: Path to the file used for storage
            size: Total size of the storage file in bytes
            bytes_per_page: Size of each page in bytes
            entries: Maximum number of concurrent operations
        """
        if not HF3FS_AVAILABLE:
            raise ImportError(
                "hf3fs_fuse.io is not available. Please install the hf3fs_fuse package."
            )

        self.path = path
        self.size = size
        self.bytes_per_page = bytes_per_page
        self.entries = entries

        self._closed = False

        self.file = None
        self.shm_r = None
        self.shm_w = None
        self.ior_r = None
        self.ior_w = None
        self.iov_r = None
        self.iov_w = None
        try:
            # Create the file if it doesn't exist and set its size
            self.file = os.open(self.path, os.O_RDWR | os.O_CREAT)
            os.ftruncate(self.file, size)
            register_fd(self.file)

            self.hf3fs_mount_point = extract_mount_point(path)
            self.bs = self.bytes_per_page
            self.shm_r = multiprocessing.shared_memory.SharedMemory(
                size=self.bs * self.entries, create=True
            )
            self.shm_w = multiprocessing.shared_memory.SharedMemory(
                size=self.bs * self.entries, create=True
            )

            self.shm_r_tensor = torch.frombuffer(self.shm_r.buf, dtype=torch.uint8)
            self.shm_w_tensor = torch.frombuffer(self.shm_w.buf, dtype=torch.uint8)

            numel = self.bs * self.entries
            self.r_pinned = torch.empty(
                numel,
                dtype=torch.uint8,
                device="cpu",
                pin_memory=True,
            )
            self.w_pinned = torch.empty(
                numel,
                dtype=torch.uint8,
                device="cpu",
                pin_memory=True,
            )

            self.numa = -1
            self.ior_r = make_ioring(
                self.hf3fs_mount_point,
                self.entries,
                for_read=True,
                timeout=1,
                numa=self.numa,
            )
            self.ior_w = make_ioring(
                self.hf3fs_mount_point,
                self.entries,
                for_read=False,
                timeout=1,
                numa=self.numa,
            )
            self.iov_r = make_iovec(self.shm_r, self.hf3fs_mount_point)
            self.iov_w = make_iovec(self.shm_w, self.hf3fs_mount_point)
            self.shm_r.unlink()
            self.shm_w.unlink()

            self.rlock = threading.RLock()
            self.wlock = threading.RLock()

            self.stream = torch.cuda.Stream()
            self.stream_ptr_int = self.stream.cuda_stream

        except Exception:
            self._release_resources()
            raise

        logger.debug(
            "Initialized HF3FS client with file: %s, size: %s bytes", path, size
        )

    def_release_resources(self) -> None:
"""Release all acquired resources safely"""
        # iov must be released before ioring and shm
        for attr in ("iov_r", "iov_w", "ior_r", "ior_w"):
            obj = getattr(self, attr, None)
            if obj is not None:
                del obj
                setattr(self, attr, None)

        for attr in ("shm_r", "shm_w"):
            shm = getattr(self, attr, None)
            if shm is not None:
                try:
                    shm.close()
                except Exception as e:
                    logger.warning("Failed to close %s: %s", attr, e)
                setattr(self, attr, None)

        if self.file is not None:
            try:
                deregister_fd(self.file)
            except Exception as e:
                logger.warning("deregister_fd failed: %s", e)
            try:
                os.close(self.file)
            except OSError as e:
                logger.warning("os.close failed: %s", e)
            self.file = None

    @rsynchronized()
    defbatch_read(self, offsets: list[int], tensors: list[torch.Tensor]) -> list[int]:
"""Read data from the file at specified offsets into tensors.

        Args:
            offsets: List of byte offsets to read from
            tensors: List of tensors to read data into

        Returns:
            List of operation results (0 for success, non-zero for error)
        """
        self.check(offsets, tensors)
        assert self.ior_r is not None
        assert self.iov_r is not None

        # prepare
        current = 0
        for offset, tensor in zip(offsets, tensors):
            size = tensor.numel() * tensor.itemsize
            self.ior_r.prepare(
                self.iov_r[current : current + size], True, self.file, offset
            )
            current += size

        # submit
        ionum = len(offsets)
        resv = self.ior_r.submit().wait(min_results=ionum)

        # results
        with torch.cuda.stream(self.stream):
            hf3fs_utils.read_shm(
                self.shm_r_tensor, self.r_pinned, tensors, self.stream_ptr_int
            )
        results = [res.result for res in resv]

        return results

    @wsynchronized()
    defbatch_write(
        self, offsets: list[int], tensors: list[torch.Tensor], event: torch.cuda.Event
    ) -> list[int]:
"""Write data from tensors to the file at specified offsets.

        Args:
            offsets: List of byte offsets to write to
            tensors: List of tensors containing data to write

        Returns:
            List of operation results (0 for success, non-zero for error)
        """

        self.check(offsets, tensors)
        assert self.ior_w is not None
        assert self.iov_w is not None

        # prepare
        with torch.cuda.stream(self.stream):
            self.stream.wait_event(event)
            hf3fs_utils.write_shm(
                tensors, self.shm_w_tensor, self.w_pinned, self.stream_ptr_int
            )

        current = 0
        for offset, tensor in zip(offsets, tensors):
            size = tensor.numel() * tensor.itemsize
            self.ior_w.prepare(
                self.iov_w[current : current + size], False, self.file, offset
            )
            current += size

        # submit
        ionum = len(offsets)
        resv = self.ior_w.submit().wait(min_results=ionum)

        # results
        results = [res.result for res in resv]

        return results

    defcheck(self, offsets: list[int], tensors: list[torch.Tensor]) -> None:
        sizes = [t.numel() * t.itemsize for t in tensors]
        if any(
            [
                len(offsets) > self.entries,
                len(offsets) != len(sizes),
                any(
                    offset < 0 or offset + size > self.size
                    for offset, size in zip(offsets, sizes)
                ),
                any(size > self.bytes_per_page for size in sizes),
            ]
        ):
            self.close()
            raise ValueError("Hf3fsClient.check Failed")

    defget_size(self) -> int:
"""Get the total size of the storage file.

        Returns:
            Size of the file in bytes
        """
        return self.size

    defclose(self) -> None:
"""Close the client and clean up resources."""
        if self._closed:
            return
        self._closed = True
        self._release_resources()

    defflush(self) -> None:
"""Flush any pending writes to disk."""
        if not self._closed and self.file is not None:
            os.fsync(self.file)
```