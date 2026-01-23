---
title: pydantic_ai.retries - Pydantic AI
url: https://ai.pydantic.dev/api/retries/
source: sitemap
fetched_at: 2026-01-22T22:24:14.309296288-03:00
rendered_js: false
word_count: 1098
summary: This document defines utilities for implementing retry logic in HTTP requests using the tenacity library, including configuration schemas and custom transport wrappers for Pydantic AI.
tags:
    - pydantic-ai
    - tenacity
    - retry-logic
    - http-transport
    - error-handling
    - python-library
category: api
---

Retries utilities based on tenacity, especially for HTTP requests.

This module provides HTTP transport wrappers and wait strategies that integrate with the tenacity library to add retry capabilities to HTTP requests. The transports can be used with HTTP clients that support custom transports (such as httpx), while the wait strategies can be used with any tenacity retry decorator.

The module includes: - TenacityTransport: Synchronous HTTP transport with retry capabilities - AsyncTenacityTransport: Asynchronous HTTP transport with retry capabilities - wait\_retry\_after: Wait strategy that respects HTTP Retry-After headers

### RetryConfig

Bases: `TypedDict`

The configuration for tenacity-based retrying.

These are precisely the arguments to the tenacity `retry` decorator, and they are generally used internally by passing them to that decorator via `@retry(**config)` or similar.

All fields are optional, and if not provided, the default values from the `tenacity.retry` decorator will be used.

Source code in `pydantic_ai_slim/pydantic_ai/retries.py`

```
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
```

```
classRetryConfig(TypedDict, total=False):
"""The configuration for tenacity-based retrying.

    These are precisely the arguments to the tenacity `retry` decorator, and they are generally
    used internally by passing them to that decorator via `@retry(**config)` or similar.

    All fields are optional, and if not provided, the default values from the `tenacity.retry` decorator will be used.
    """

    sleep: Callable[[int | float], None | Awaitable[None]]
"""A sleep strategy to use for sleeping between retries.

    Tenacity's default for this argument is `tenacity.nap.sleep`."""

    stop: StopBaseT
"""
    A stop strategy to determine when to stop retrying.

    Tenacity's default for this argument is `tenacity.stop.stop_never`."""

    wait: WaitBaseT
"""
    A wait strategy to determine how long to wait between retries.

    Tenacity's default for this argument is `tenacity.wait.wait_none`."""

    retry: SyncRetryBaseT | RetryBaseT
"""A retry strategy to determine which exceptions should trigger a retry.

    Tenacity's default for this argument is `tenacity.retry.retry_if_exception_type()`."""

    before: Callable[[RetryCallState], None | Awaitable[None]]
"""
    A callable that is called before each retry attempt.

    Tenacity's default for this argument is `tenacity.before.before_nothing`."""

    after: Callable[[RetryCallState], None | Awaitable[None]]
"""
    A callable that is called after each retry attempt.

    Tenacity's default for this argument is `tenacity.after.after_nothing`."""

    before_sleep: Callable[[RetryCallState], None | Awaitable[None]] | None
"""
    An optional callable that is called before sleeping between retries.

    Tenacity's default for this argument is `None`."""

    reraise: bool
"""Whether to reraise the last exception if the retry attempts are exhausted, or raise a RetryError instead.

    Tenacity's default for this argument is `False`."""

    retry_error_cls: type[RetryError]
"""The exception class to raise when the retry attempts are exhausted and `reraise` is False.

    Tenacity's default for this argument is `tenacity.RetryError`."""

    retry_error_callback: Callable[[RetryCallState], Any | Awaitable[Any]] | None
"""An optional callable that is called when the retry attempts are exhausted and `reraise` is False.

    Tenacity's default for this argument is `None`."""
```

#### sleep `instance-attribute`

A sleep strategy to use for sleeping between retries.

Tenacity's default for this argument is `tenacity.nap.sleep`.

#### stop `instance-attribute`

A stop strategy to determine when to stop retrying.

Tenacity's default for this argument is `tenacity.stop.stop_never`.

#### wait `instance-attribute`

A wait strategy to determine how long to wait between retries.

Tenacity's default for this argument is `tenacity.wait.wait_none`.

#### retry `instance-attribute`

```
retry: RetryBaseT | RetryBaseT
```

A retry strategy to determine which exceptions should trigger a retry.

Tenacity's default for this argument is `tenacity.retry.retry_if_exception_type()`.

#### before `instance-attribute`

A callable that is called before each retry attempt.

Tenacity's default for this argument is `tenacity.before.before_nothing`.

#### after `instance-attribute`

A callable that is called after each retry attempt.

Tenacity's default for this argument is `tenacity.after.after_nothing`.

#### before\_sleep `instance-attribute`

An optional callable that is called before sleeping between retries.

Tenacity's default for this argument is `None`.

#### reraise `instance-attribute`

Whether to reraise the last exception if the retry attempts are exhausted, or raise a RetryError instead.

Tenacity's default for this argument is `False`.

#### retry\_error\_cls `instance-attribute`

```
retry_error_cls: type[RetryError]
```

The exception class to raise when the retry attempts are exhausted and `reraise` is False.

Tenacity's default for this argument is `tenacity.RetryError`.

#### retry\_error\_callback `instance-attribute`

An optional callable that is called when the retry attempts are exhausted and `reraise` is False.

Tenacity's default for this argument is `None`.

### TenacityTransport

Bases: `BaseTransport`

Synchronous HTTP transport with tenacity-based retry functionality.

This transport wraps another BaseTransport and adds retry capabilities using the tenacity library. It can be configured to retry requests based on various conditions such as specific exception types, response status codes, or custom validation logic.

The transport works by intercepting HTTP requests and responses, allowing the tenacity controller to determine when and how to retry failed requests. The validate\_response function can be used to convert HTTP responses into exceptions that trigger retries.

Parameters:

Name Type Description Default `wrapped` `BaseTransport | None`

The underlying transport to wrap and add retry functionality to.

`None` `config` `RetryConfig`

The arguments to use for the tenacity `retry` decorator, including retry conditions, wait strategy, stop conditions, etc. See the tenacity docs for more info.

*required* `validate_response` `Callable[[Response], Any] | None`

Optional callable that takes a Response and can raise an exception to be handled by the controller if the response should trigger a retry. Common use case is to raise exceptions for certain HTTP status codes. If None, no response validation is performed.

`None`

Example

```
fromhttpximport Client, HTTPStatusError, HTTPTransport
fromtenacityimport retry_if_exception_type, stop_after_attempt

frompydantic_ai.retriesimport RetryConfig, TenacityTransport, wait_retry_after

transport = TenacityTransport(
    RetryConfig(
        retry=retry_if_exception_type(HTTPStatusError),
        wait=wait_retry_after(max_wait=300),
        stop=stop_after_attempt(5),
        reraise=True
    ),
    HTTPTransport(),
    validate_response=lambda r: r.raise_for_status()
)
client = Client(transport=transport)
```

Source code in `pydantic_ai_slim/pydantic_ai/retries.py`

```
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
```

````
classTenacityTransport(BaseTransport):
"""Synchronous HTTP transport with tenacity-based retry functionality.

    This transport wraps another BaseTransport and adds retry capabilities using the tenacity library.
    It can be configured to retry requests based on various conditions such as specific exception types,
    response status codes, or custom validation logic.

    The transport works by intercepting HTTP requests and responses, allowing the tenacity controller
    to determine when and how to retry failed requests. The validate_response function can be used
    to convert HTTP responses into exceptions that trigger retries.

    Args:
        wrapped: The underlying transport to wrap and add retry functionality to.
        config: The arguments to use for the tenacity `retry` decorator, including retry conditions,
            wait strategy, stop conditions, etc. See the tenacity docs for more info.
        validate_response: Optional callable that takes a Response and can raise an exception
            to be handled by the controller if the response should trigger a retry.
            Common use case is to raise exceptions for certain HTTP status codes.
            If None, no response validation is performed.

    Example:
        ```python
        from httpx import Client, HTTPStatusError, HTTPTransport
        from tenacity import retry_if_exception_type, stop_after_attempt

        from pydantic_ai.retries import RetryConfig, TenacityTransport, wait_retry_after

        transport = TenacityTransport(
            RetryConfig(
                retry=retry_if_exception_type(HTTPStatusError),
                wait=wait_retry_after(max_wait=300),
                stop=stop_after_attempt(5),
                reraise=True
            ),
            HTTPTransport(),
            validate_response=lambda r: r.raise_for_status()
        )
        client = Client(transport=transport)
        ```
    """

    def__init__(
        self,
        config: RetryConfig,
        wrapped: BaseTransport | None = None,
        validate_response: Callable[[Response], Any] | None = None,
    ):
        self.config = config
        self.wrapped = wrapped or HTTPTransport()
        self.validate_response = validate_response

    defhandle_request(self, request: Request) -> Response:
"""Handle an HTTP request with retry logic.

        Args:
            request: The HTTP request to handle.

        Returns:
            The HTTP response.

        Raises:
            RuntimeError: If the retry controller did not make any attempts.
            Exception: Any exception raised by the wrapped transport or validation function.
        """

        @retry(**self.config)
        defhandle_request(req: Request) -> Response:
            response = self.wrapped.handle_request(req)

            # this is normally set by httpx _after_ calling this function, but we want the request in the validator:
            response.request = req

            if self.validate_response:
                try:
                    self.validate_response(response)
                except Exception:
                    response.close()
                    raise
            return response

        return handle_request(request)

    def__enter__(self) -> TenacityTransport:
        self.wrapped.__enter__()
        return self

    def__exit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None,
    ) -> None:
        self.wrapped.__exit__(exc_type, exc_value, traceback)

    defclose(self) -> None:
        self.wrapped.close()  # pragma: no cover
````

#### handle\_request

```
handle_request(request: Request) -> Response
```

Handle an HTTP request with retry logic.

Parameters:

Name Type Description Default `request` `Request`

The HTTP request to handle.

*required*

Returns:

Type Description `Response`

The HTTP response.

Raises:

Type Description `RuntimeError`

If the retry controller did not make any attempts.

`Exception`

Any exception raised by the wrapped transport or validation function.

Source code in `pydantic_ai_slim/pydantic_ai/retries.py`

```
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
```

```
defhandle_request(self, request: Request) -> Response:
"""Handle an HTTP request with retry logic.

    Args:
        request: The HTTP request to handle.

    Returns:
        The HTTP response.

    Raises:
        RuntimeError: If the retry controller did not make any attempts.
        Exception: Any exception raised by the wrapped transport or validation function.
    """

    @retry(**self.config)
    defhandle_request(req: Request) -> Response:
        response = self.wrapped.handle_request(req)

        # this is normally set by httpx _after_ calling this function, but we want the request in the validator:
        response.request = req

        if self.validate_response:
            try:
                self.validate_response(response)
            except Exception:
                response.close()
                raise
        return response

    return handle_request(request)
```

### AsyncTenacityTransport

Bases: `AsyncBaseTransport`

Asynchronous HTTP transport with tenacity-based retry functionality.

This transport wraps another AsyncBaseTransport and adds retry capabilities using the tenacity library. It can be configured to retry requests based on various conditions such as specific exception types, response status codes, or custom validation logic.

The transport works by intercepting HTTP requests and responses, allowing the tenacity controller to determine when and how to retry failed requests. The validate\_response function can be used to convert HTTP responses into exceptions that trigger retries.

Parameters:

Name Type Description Default `wrapped` `AsyncBaseTransport | None`

The underlying async transport to wrap and add retry functionality to.

`None` `config` `RetryConfig`

The arguments to use for the tenacity `retry` decorator, including retry conditions, wait strategy, stop conditions, etc. See the tenacity docs for more info.

*required* `validate_response` `Callable[[Response], Any] | None`

Optional callable that takes a Response and can raise an exception to be handled by the controller if the response should trigger a retry. Common use case is to raise exceptions for certain HTTP status codes. If None, no response validation is performed.

`None`

Example

```
fromhttpximport AsyncClient, HTTPStatusError
fromtenacityimport retry_if_exception_type, stop_after_attempt

frompydantic_ai.retriesimport AsyncTenacityTransport, RetryConfig, wait_retry_after

transport = AsyncTenacityTransport(
    RetryConfig(
        retry=retry_if_exception_type(HTTPStatusError),
        wait=wait_retry_after(max_wait=300),
        stop=stop_after_attempt(5),
        reraise=True
    ),
    validate_response=lambda r: r.raise_for_status()
)
client = AsyncClient(transport=transport)
```

Source code in `pydantic_ai_slim/pydantic_ai/retries.py`

```
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
```

````
classAsyncTenacityTransport(AsyncBaseTransport):
"""Asynchronous HTTP transport with tenacity-based retry functionality.

    This transport wraps another AsyncBaseTransport and adds retry capabilities using the tenacity library.
    It can be configured to retry requests based on various conditions such as specific exception types,
    response status codes, or custom validation logic.

    The transport works by intercepting HTTP requests and responses, allowing the tenacity controller
    to determine when and how to retry failed requests. The validate_response function can be used
    to convert HTTP responses into exceptions that trigger retries.

    Args:
        wrapped: The underlying async transport to wrap and add retry functionality to.
        config: The arguments to use for the tenacity `retry` decorator, including retry conditions,
            wait strategy, stop conditions, etc. See the tenacity docs for more info.
        validate_response: Optional callable that takes a Response and can raise an exception
            to be handled by the controller if the response should trigger a retry.
            Common use case is to raise exceptions for certain HTTP status codes.
            If None, no response validation is performed.

    Example:
        ```python
        from httpx import AsyncClient, HTTPStatusError
        from tenacity import retry_if_exception_type, stop_after_attempt

        from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig, wait_retry_after

        transport = AsyncTenacityTransport(
            RetryConfig(
                retry=retry_if_exception_type(HTTPStatusError),
                wait=wait_retry_after(max_wait=300),
                stop=stop_after_attempt(5),
                reraise=True
            ),
            validate_response=lambda r: r.raise_for_status()
        )
        client = AsyncClient(transport=transport)
        ```
    """

    def__init__(
        self,
        config: RetryConfig,
        wrapped: AsyncBaseTransport | None = None,
        validate_response: Callable[[Response], Any] | None = None,
    ):
        self.config = config
        self.wrapped = wrapped or AsyncHTTPTransport()
        self.validate_response = validate_response

    async defhandle_async_request(self, request: Request) -> Response:
"""Handle an async HTTP request with retry logic.

        Args:
            request: The HTTP request to handle.

        Returns:
            The HTTP response.

        Raises:
            RuntimeError: If the retry controller did not make any attempts.
            Exception: Any exception raised by the wrapped transport or validation function.
        """

        @retry(**self.config)
        async defhandle_async_request(req: Request) -> Response:
            response = await self.wrapped.handle_async_request(req)

            # this is normally set by httpx _after_ calling this function, but we want the request in the validator:
            response.request = req

            if self.validate_response:
                try:
                    self.validate_response(response)
                except Exception:
                    await response.aclose()
                    raise
            return response

        return await handle_async_request(request)

    async def__aenter__(self) -> AsyncTenacityTransport:
        await self.wrapped.__aenter__()
        return self

    async def__aexit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None,
    ) -> None:
        await self.wrapped.__aexit__(exc_type, exc_value, traceback)

    async defaclose(self) -> None:
        await self.wrapped.aclose()
````

#### handle\_async\_request `async`

```
handle_async_request(request: Request) -> Response
```

Handle an async HTTP request with retry logic.

Parameters:

Name Type Description Default `request` `Request`

The HTTP request to handle.

*required*

Returns:

Type Description `Response`

The HTTP response.

Raises:

Type Description `RuntimeError`

If the retry controller did not make any attempts.

`Exception`

Any exception raised by the wrapped transport or validation function.

Source code in `pydantic_ai_slim/pydantic_ai/retries.py`

```
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
```

```
async defhandle_async_request(self, request: Request) -> Response:
"""Handle an async HTTP request with retry logic.

    Args:
        request: The HTTP request to handle.

    Returns:
        The HTTP response.

    Raises:
        RuntimeError: If the retry controller did not make any attempts.
        Exception: Any exception raised by the wrapped transport or validation function.
    """

    @retry(**self.config)
    async defhandle_async_request(req: Request) -> Response:
        response = await self.wrapped.handle_async_request(req)

        # this is normally set by httpx _after_ calling this function, but we want the request in the validator:
        response.request = req

        if self.validate_response:
            try:
                self.validate_response(response)
            except Exception:
                await response.aclose()
                raise
        return response

    return await handle_async_request(request)
```

### wait\_retry\_after

Create a tenacity-compatible wait strategy that respects HTTP Retry-After headers.

This wait strategy checks if the exception contains an HTTPStatusError with a Retry-After header, and if so, waits for the time specified in the header. If no header is present or parsing fails, it falls back to the provided strategy.

The Retry-After header can be in two formats: - An integer representing seconds to wait - An HTTP date string representing when to retry

Parameters:

Name Type Description Default `fallback_strategy` `Callable[[RetryCallState], float] | None`

Wait strategy to use when no Retry-After header is present or parsing fails. Defaults to exponential backoff with max 60s.

`None` `max_wait` `float`

Maximum time to wait in seconds, regardless of header value. Defaults to 300 (5 minutes).

`300`

Returns:

Type Description `Callable[[RetryCallState], float]`

A wait function that can be used with tenacity retry decorators.

Example

```
fromhttpximport AsyncClient, HTTPStatusError
fromtenacityimport retry_if_exception_type, stop_after_attempt

frompydantic_ai.retriesimport AsyncTenacityTransport, RetryConfig, wait_retry_after

transport = AsyncTenacityTransport(
    RetryConfig(
        retry=retry_if_exception_type(HTTPStatusError),
        wait=wait_retry_after(max_wait=120),
        stop=stop_after_attempt(5),
        reraise=True
    ),
    validate_response=lambda r: r.raise_for_status()
)
client = AsyncClient(transport=transport)
```

Source code in `pydantic_ai_slim/pydantic_ai/retries.py`

```
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
```

````
defwait_retry_after(
    fallback_strategy: Callable[[RetryCallState], float] | None = None, max_wait: float = 300
) -> Callable[[RetryCallState], float]:
"""Create a tenacity-compatible wait strategy that respects HTTP Retry-After headers.

    This wait strategy checks if the exception contains an HTTPStatusError with a
    Retry-After header, and if so, waits for the time specified in the header.
    If no header is present or parsing fails, it falls back to the provided strategy.

    The Retry-After header can be in two formats:
    - An integer representing seconds to wait
    - An HTTP date string representing when to retry

    Args:
        fallback_strategy: Wait strategy to use when no Retry-After header is present
                          or parsing fails. Defaults to exponential backoff with max 60s.
        max_wait: Maximum time to wait in seconds, regardless of header value.
                 Defaults to 300 (5 minutes).

    Returns:
        A wait function that can be used with tenacity retry decorators.

    Example:
        ```python
        from httpx import AsyncClient, HTTPStatusError
        from tenacity import retry_if_exception_type, stop_after_attempt

        from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig, wait_retry_after

        transport = AsyncTenacityTransport(
            RetryConfig(
                retry=retry_if_exception_type(HTTPStatusError),
                wait=wait_retry_after(max_wait=120),
                stop=stop_after_attempt(5),
                reraise=True
            ),
            validate_response=lambda r: r.raise_for_status()
        )
        client = AsyncClient(transport=transport)
        ```
    """
    if fallback_strategy is None:
        fallback_strategy = wait_exponential(multiplier=1, max=60)

    defwait_func(state: RetryCallState) -> float:
        exc = state.outcome.exception() if state.outcome else None
        if isinstance(exc, HTTPStatusError):
            retry_after = exc.response.headers.get('retry-after')
            if retry_after:
                try:
                    # Try parsing as seconds first
                    wait_seconds = int(retry_after)
                    return min(float(wait_seconds), max_wait)
                except ValueError:
                    # Try parsing as HTTP date
                    try:
                        retry_time = cast(datetime, parsedate_to_datetime(retry_after))
                        assert isinstance(retry_time, datetime)
                        now = datetime.now(timezone.utc)
                        wait_seconds = (retry_time - now).total_seconds()

                        if wait_seconds > 0:
                            return min(wait_seconds, max_wait)
                    except (ValueError, TypeError, AssertionError):
                        # If date parsing fails, fall back to fallback strategy
                        pass

        # Use fallback strategy
        return fallback_strategy(state)

    return wait_func
````