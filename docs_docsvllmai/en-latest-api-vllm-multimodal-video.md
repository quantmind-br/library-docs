---
title: video - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/video/
source: sitemap
fetched_at: 2026-05-07T21:34:23.840087565-03:00
rendered_js: false
word_count: 7
summary: This document defines the Molmo2VideoBackend class, which provides methods for calculating video frame sampling rates, determining optimal frame indices, and managing temporal sampling for video processing workflows.
tags:
    - video-processing
    - frame-sampling
    - fps-calculation
    - multimodal
    - video-metadata
    - python
category: api
---

```
@VIDEO_LOADER_REGISTRY.register("molmo2")
classMolmo2VideoBackend(VideoLoader, OpenCVVideoBackendMixin):
    @classmethod
    defget_candidate_target_fps(
        cls,
        video_fps: float,
        sampling_fps: float,
        max_fps: float = 8.0,
    ) -> list[float]:
"""
        Return the subset of `video_fps` factors that remain multiples
        of `sampling_fps`.

        Examples:
            >>> get_candidate_target_fps(video_fps=6, sampling_fps=2)
            [2, 6]
            >>> get_candidate_target_fps(video_fps=5, sampling_fps=1)
            [1, 5]
            >>> get_candidate_target_fps(video_fps=2, sampling_fps=2)
            [2]
            >>> get_candidate_target_fps(video_fps=5, sampling_fps=2)
            Traceback (most recent call last):
                ...
            ValueError: sampling_fps=2 must divide video_fps=5 to produce
                consistent frame steps.
        """
        video_fps = int(video_fps)
        sampling_fps = int(sampling_fps)
        max_fps = int(max_fps)

        if sampling_fps is None:
            raise ValueError("sampling_fps must be provided")
        if video_fps <= 0 or sampling_fps <= 0:
            raise ValueError(
                "video_fps and sampling_fps must be positive "
                f"(got {video_fps}, {sampling_fps})"
            )
        if video_fps % sampling_fps != 0:
            raise ValueError(
                f"sampling_fps={sampling_fps} must divide video_fps={video_fps}."
            )

        candidates = []
        for candidate in range(sampling_fps, video_fps + 1, sampling_fps):
            if candidate > max_fps:
                break
            if video_fps % candidate == 0:
                candidates.append(float(candidate))

        return candidates

    @classmethod
    defget_target_fps(
        cls,
        video_fps: float,
        max_frames: int,
        total_frames: int,
        frame_sample_mode: str,
        candidate_target_fps: list[float],
    ) -> float | None:
"""
        Get the target fps that best spans the videoand has the most frames sampled
        """
        num_frames_sampled = 0
        selected_target_fps = None
        for target_fps in candidate_target_fps:
            step_size = max(int(video_fps / target_fps), 1)
            num_frames_sampled_at_fps = int(total_frames / step_size)
            if num_frames_sampled == 0:
                if (
                    "uniform" in frame_sample_mode
                    and num_frames_sampled_at_fps > max_frames
                ):
                    break
                selected_target_fps = target_fps
                num_frames_sampled = num_frames_sampled_at_fps

            else:
                # the candidate sampling fps increases so frame count can't decrease
                assert num_frames_sampled <= num_frames_sampled_at_fps
                if num_frames_sampled_at_fps > max_frames:
                    # choose the sampling fps that spans the video
                    continue

                elif num_frames_sampled_at_fps > num_frames_sampled:
                    # both are less than max_frames; choose the one with higher
                    # density of frames sampled
                    selected_target_fps = target_fps
                    num_frames_sampled = num_frames_sampled_at_fps
        return selected_target_fps

    @classmethod
    defget_frame_times_and_chosen_fps(
        cls,
        selected_target_fps: float | None,
        total_frames: int,
        max_frames: int,
        video_fps: float,
    ) -> tuple[float | None, npt.NDArray]:
        if selected_target_fps is None:
            frame_indices = np.linspace(
                0, total_frames, max_frames, endpoint=False, dtype=int
            )
        else:
            step_size = max(int(video_fps / selected_target_fps), 1)
            frame_indices = np.arange(0, total_frames, step_size)
        if len(frame_indices) > max_frames:
            frame_indices = frame_indices[:max_frames]
        return selected_target_fps, frame_indices

    @classmethod
    defsample_times(
        cls,
        duration: float,
        max_frames: int,
        frame_sample_mode: str,
        max_fps: int | None,
        candidate_target_fps: list[float] | None = None,
        **kwargs,
    ) -> npt.NDArray:
        if frame_sample_mode == "fps":
            assert candidate_target_fps is not None
            # Try larger and larger FPSs until we hit one that can't span the video
            sampling_fps = candidate_target_fps[0]
            for candidate_fps in candidate_target_fps[1:]:
                if max_frames / candidate_fps < duration:
                    break
                sampling_fps = candidate_fps
            times = np.arange(0, max_frames) / sampling_fps
            times = times[times < duration]
            return times
        elif frame_sample_mode == "uniform_last_frame":
            if max_fps is not None:
                max_duration = (
                    max_frames - 1
                ) / max_fps  # -1 to include the last frame
                if max_duration < duration:
                    times = np.linspace(
                        0, duration, num=max_frames, endpoint=True, dtype=np.float64
                    )
                else:
                    times = np.arange(0.0, stop=duration, step=1 / max_fps)
                    times = np.concatenate([times, [duration]], axis=0)
                    assert len(times) <= max_frames
            else:
                times = np.linspace(
                    0, duration, num=max_frames, endpoint=True, dtype=np.float64
                )
            return times
        else:
            raise NotImplementedError(frame_sample_mode)

    @classmethod
    defcompute_frames_index_to_sample(
        cls,
        source: VideoSourceMetadata,
        target: VideoTargetMetadata,
        **kwargs,
    ):
        max_fps = kwargs.get("max_fps")
        frame_sample_mode = kwargs.get("frame_sample_mode")
        if frame_sample_mode is None:
            return list(range(0, source.total_frames_num))

        if frame_sample_mode not in {"uniform_last_frame", "fps"}:
            raise NotImplementedError(
                f"Unsupported frame_sample_mode: {frame_sample_mode}"
            )

        duration = source.duration
        video_fps = source.original_fps
        total_num_frames = source.total_frames_num
        num_frames = target.num_frames
        sampling_fps = target.fps

        if frame_sample_mode == "uniform_last_frame" and max_fps is not None:
            if total_num_frames <= 2:
                indices = np.arange(total_num_frames).astype(int)
            elif duration > (num_frames - 1) / max_fps:  # -1 to include the last frame
                # uniform fallback
                indices = np.linspace(
                    0,
                    total_num_frames - 1,
                    num=min(num_frames, total_num_frames),
                    endpoint=True,
                ).astype(int)
            else:
                float_indices = np.arange(
                    0.0,
                    stop=total_num_frames - 1,
                    step=float(video_fps / max_fps),
                )
                if np.round(float_indices[-1]) != total_num_frames - 1:
                    float_indices = np.concatenate(
                        [float_indices, [total_num_frames - 1]], axis=0
                    )
                indices = np.round(float_indices).astype(int)
                assert indices[-1] < total_num_frames
                assert len(float_indices) <= num_frames
        elif frame_sample_mode == "uniform_last_frame":
            indices = np.linspace(
                0,
                total_num_frames - 1,
                num=min(num_frames, total_num_frames),
                endpoint=True,
            ).astype(int)
        elif frame_sample_mode == "fps":
            candidate_target_fps = cls.get_candidate_target_fps(video_fps, sampling_fps)
            selected_target_fps = cls.get_target_fps(
                video_fps,
                num_frames,
                total_num_frames,
                frame_sample_mode,
                candidate_target_fps,
            )
            _, indices = cls.get_frame_times_and_chosen_fps(
                selected_target_fps,
                total_num_frames,
                num_frames,
                video_fps,
            )
        return indices.tolist()

    @classmethod
    defload_bytes_opencv(
        cls,
        data: bytes,
        frame_sample_mode: str | None = None,
        num_frames: int = -1,
        max_fps: int = 2,
        sampling_fps: int = 2,
        frame_recovery: bool = False,
        **kwargs,
    ) -> tuple[npt.NDArray, dict[str, Any]]:
        cap = cls.open_video_capture(data)

        source = OpenCVVideoBackendMixin.get_video_metadata(cap)
        target = VideoTargetMetadata(
            num_frames=num_frames,
            fps=sampling_fps,
            max_duration=source.duration,
        )

        frame_idx = cls.compute_frames_index_to_sample(
            source=source,
            target=target,
            frame_sample_mode=frame_sample_mode,
            max_fps=max_fps,
        )

        frames, valid_frame_indices = cls.read_frames(
            cap,
            frame_idx,
            total_frames_num=source.total_frames_num,
            frame_recovery=frame_recovery,
        )

        metadata = cls.create_hf_metadata(
            source=source,
            video_backend="opencv",
            valid_frame_indices=valid_frame_indices,
        )

        return frames, metadata

    @classmethod
    defload_bytes(
        cls,
        data: bytes,
        num_frames: int = -1,
        **kwargs,
    ) -> tuple[npt.NDArray, dict[str, Any]]:
        frame_sample_mode = cast(str | None, kwargs.pop("frame_sample_mode", None))
        max_fps = cast(int, kwargs.pop("max_fps", 2))
        sampling_fps = cast(int, kwargs.pop("sampling_fps", 2))
        out = cls.load_bytes_opencv(
            data,
            frame_sample_mode,
            num_frames,
            max_fps,
            sampling_fps,
            **kwargs,
        )
        return out
```