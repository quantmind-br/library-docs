---
title: logger - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/logger/
source: sitemap
fetched_at: 2026-05-07T21:22:19.896737953-03:00
rendered_js: false
word_count: 278
summary: This document describes the vLLM logging utilities, which provide methods for deduplicated logging and system-level function call tracing to assist in debugging.
tags:
    - logging
    - vllm
    - debugging
    - trace-functions
    - python-logging
category: reference
---

Logging configuration for vLLM.

## \_VllmLogger [¶](#vllm.logger._VllmLogger "Permanent link")

Bases: `Logger`

Note

This class is just to provide type information. We actually patch the methods directly on the [`logging.Logger`](https://docs.python.org/3/library/logging.html#logging.Logger) instance to avoid conflicting with other libraries such as `intel_extension_for_pytorch.utils._logger`.

Source code in `vllm/logger.py`

```
class_VllmLogger(Logger):
"""
    Note:
        This class is just to provide type information.
        We actually patch the methods directly on the [`logging.Logger`][]
        instance to avoid conflicting with other libraries such as
        `intel_extension_for_pytorch.utils._logger`.
    """

    defdebug_once(self, msg: str, *args: Hashable, scope: LogScope = "local") -> None:
"""
        As [`debug`][logging.Logger.debug], but subsequent calls with
        the same message are silently dropped.
        """
        if not _should_log_with_scope(scope):
            return
        _print_debug_once(self, msg, *args)

    definfo_once(self, msg: str, *args: Hashable, scope: LogScope = "local") -> None:
"""
        As [`info`][logging.Logger.info], but subsequent calls with
        the same message are silently dropped.
        """
        if not _should_log_with_scope(scope):
            return
        _print_info_once(self, msg, *args)

    defwarning_once(
        self, msg: str, *args: Hashable, scope: LogScope = "local"
    ) -> None:
"""
        As [`warning`][logging.Logger.warning], but subsequent calls with
        the same message are silently dropped.
        """
        if not _should_log_with_scope(scope):
            return
        _print_warning_once(self, msg, *args)
```

### debug\_once [¶](#vllm.logger._VllmLogger.debug_once "Permanent link")

```
debug_once(
    msg: str, *args: Hashable, scope: LogScope = "local"
) -> None
```

As [`debug`](https://docs.python.org/3/library/logging.html#logging.Logger.debug), but subsequent calls with the same message are silently dropped.

Source code in `vllm/logger.py`

```
defdebug_once(self, msg: str, *args: Hashable, scope: LogScope = "local") -> None:
"""
    As [`debug`][logging.Logger.debug], but subsequent calls with
    the same message are silently dropped.
    """
    if not _should_log_with_scope(scope):
        return
    _print_debug_once(self, msg, *args)
```

### info\_once [¶](#vllm.logger._VllmLogger.info_once "Permanent link")

```
info_once(
    msg: str, *args: Hashable, scope: LogScope = "local"
) -> None
```

As [`info`](https://docs.python.org/3/library/logging.html#logging.Logger.info), but subsequent calls with the same message are silently dropped.

Source code in `vllm/logger.py`

```
definfo_once(self, msg: str, *args: Hashable, scope: LogScope = "local") -> None:
"""
    As [`info`][logging.Logger.info], but subsequent calls with
    the same message are silently dropped.
    """
    if not _should_log_with_scope(scope):
        return
    _print_info_once(self, msg, *args)
```

### warning\_once [¶](#vllm.logger._VllmLogger.warning_once "Permanent link")

```
warning_once(
    msg: str, *args: Hashable, scope: LogScope = "local"
) -> None
```

As [`warning`](https://docs.python.org/3/library/logging.html#logging.Logger.warning), but subsequent calls with the same message are silently dropped.

Source code in `vllm/logger.py`

```
defwarning_once(
    self, msg: str, *args: Hashable, scope: LogScope = "local"
) -> None:
"""
    As [`warning`][logging.Logger.warning], but subsequent calls with
    the same message are silently dropped.
    """
    if not _should_log_with_scope(scope):
        return
    _print_warning_once(self, msg, *args)
```

## \_should\_log\_with\_scope [¶](#vllm.logger._should_log_with_scope "Permanent link")

```
_should_log_with_scope(scope: LogScope) -> bool
```

Decide whether to log based on scope

Source code in `vllm/logger.py`

```
def_should_log_with_scope(scope: LogScope) -> bool:
"""Decide whether to log based on scope"""
    if scope == "global":
        fromvllm.distributed.parallel_stateimport is_global_first_rank

        return is_global_first_rank()
    if scope == "local":
        fromvllm.distributed.parallel_stateimport is_local_first_rank

        return is_local_first_rank()
    return True
```

## enable\_trace\_function\_call [¶](#vllm.logger.enable_trace_function_call "Permanent link")

```
enable_trace_function_call(
    log_file_path: str, root_dir: str | None = None
)
```

Enable tracing of every function call in code under `root_dir`. This is useful for debugging hangs or crashes. `log_file_path` is the path to the log file. `root_dir` is the root directory of the code to trace. If None, it is the vllm root directory.

Note that this call is thread-level, any threads calling this function will have the trace enabled. Other threads will not be affected.

Source code in `vllm/logger.py`

```
defenable_trace_function_call(log_file_path: str, root_dir: str | None = None):
"""
    Enable tracing of every function call in code under `root_dir`.
    This is useful for debugging hangs or crashes.
    `log_file_path` is the path to the log file.
    `root_dir` is the root directory of the code to trace. If None, it is the
    vllm root directory.

    Note that this call is thread-level, any threads calling this function
    will have the trace enabled. Other threads will not be affected.
    """
    logger.warning(
        "VLLM_TRACE_FUNCTION is enabled. It will record every"
        " function executed by Python. This will slow down the code. It "
        "is suggested to be used for debugging hang or crashes only."
    )
    logger.info("Trace frame log is saved to %s", log_file_path)
    if root_dir is None:
        # by default, this is the vllm root directory
        root_dir = os.path.dirname(os.path.dirname(__file__))
    sys.settrace(partial(_trace_calls, log_file_path, root_dir))
```

## init\_logger [¶](#vllm.logger.init_logger "Permanent link")

```
init_logger(name: str) -> _VllmLogger
```

The main purpose of this function is to ensure that loggers are retrieved in such a way that we can be sure the root vllm logger has already been configured.

Source code in `vllm/logger.py`

```
definit_logger(name: str) -> _VllmLogger:
"""The main purpose of this function is to ensure that loggers are
    retrieved in such a way that we can be sure the root vllm logger has
    already been configured."""

    logger = logging.getLogger(name)

    for method_name, method in _METHODS_TO_PATCH.items():
        setattr(logger, method_name, MethodType(method, logger))

    return cast(_VllmLogger, logger)
```