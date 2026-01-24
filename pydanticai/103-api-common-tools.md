---
title: pydantic_ai.common_tools - Pydantic AI
url: https://ai.pydantic.dev/api/common_tools/
source: sitemap
fetched_at: 2026-01-22T22:23:55.579831131-03:00
rendered_js: false
word_count: 1388
summary: This document provides an API reference for the DuckDuckGo and Exa search tools integrated into Pydantic AI for web search and data retrieval.
tags:
    - pydantic-ai
    - duckduckgo-search
    - exa-search
    - api-reference
    - web-scraping
    - python-library
category: api
---

### DuckDuckGoResult

Bases: `TypedDict`

A DuckDuckGo search result.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/duckduckgo.py`

```
24
25
26
27
28
29
30
31
32
```

```
classDuckDuckGoResult(TypedDict):
"""A DuckDuckGo search result."""

    title: str
"""The title of the search result."""
    href: str
"""The URL of the search result."""
    body: str
"""The body of the search result."""
```

#### title `instance-attribute`

The title of the search result.

#### href `instance-attribute`

The URL of the search result.

#### body `instance-attribute`

The body of the search result.

### DuckDuckGoSearchTool `dataclass`

The DuckDuckGo search tool.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/duckduckgo.py`

```
38
39
40
41
42
43
44
45
46
47
48
49
50
51
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
```

```
@dataclass
classDuckDuckGoSearchTool:
"""The DuckDuckGo search tool."""

    client: DDGS
"""The DuckDuckGo search client."""

    _: KW_ONLY

    max_results: int | None
"""The maximum number of results. If None, returns results only from the first response."""

    async def__call__(self, query: str) -> list[DuckDuckGoResult]:
"""Searches DuckDuckGo for the given query and returns the results.

        Args:
            query: The query to search for.

        Returns:
            The search results.
        """
        search = functools.partial(self.client.text, max_results=self.max_results)
        results = await anyio.to_thread.run_sync(search, query)
        return duckduckgo_ta.validate_python(results)
```

#### client `instance-attribute`

The DuckDuckGo search client.

#### max\_results `instance-attribute`

The maximum number of results. If None, returns results only from the first response.

#### \_\_call\__ `async`

Searches DuckDuckGo for the given query and returns the results.

Parameters:

Name Type Description Default `query` `str`

The query to search for.

*required*

Returns:

Type Description `list[DuckDuckGoResult]`

The search results.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/duckduckgo.py`

```
50
51
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
```

```
async def__call__(self, query: str) -> list[DuckDuckGoResult]:
"""Searches DuckDuckGo for the given query and returns the results.

    Args:
        query: The query to search for.

    Returns:
        The search results.
    """
    search = functools.partial(self.client.text, max_results=self.max_results)
    results = await anyio.to_thread.run_sync(search, query)
    return duckduckgo_ta.validate_python(results)
```

### duckduckgo\_search\_tool

```
duckduckgo_search_tool(
    duckduckgo_client: DDGS | None = None,
    max_results: int | None = None,
)
```

Creates a DuckDuckGo search tool.

Parameters:

Name Type Description Default `duckduckgo_client` `DDGS | None`

The DuckDuckGo search client.

`None` `max_results` `int | None`

The maximum number of results. If None, returns results only from the first response.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/duckduckgo.py`

```
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
```

```
defduckduckgo_search_tool(duckduckgo_client: DDGS | None = None, max_results: int | None = None):
"""Creates a DuckDuckGo search tool.

    Args:
        duckduckgo_client: The DuckDuckGo search client.
        max_results: The maximum number of results. If None, returns results only from the first response.
    """
    return Tool[Any](
        DuckDuckGoSearchTool(client=duckduckgo_client or DDGS(), max_results=max_results).__call__,
        name='duckduckgo_search',
        description='Searches DuckDuckGo for the given query and returns the results.',
    )
```

Exa tools for Pydantic AI agents.

Provides web search, content retrieval, and AI-powered answer capabilities using the Exa API, a neural search engine that finds high-quality, relevant results across billions of web pages.

### ExaSearchResult

Bases: `TypedDict`

An Exa search result with content.

See [Exa Search API documentation](https://docs.exa.ai/reference/search) for more information.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
```

```
classExaSearchResult(TypedDict):
"""An Exa search result with content.

    See [Exa Search API documentation](https://docs.exa.ai/reference/search)
    for more information.
    """

    title: str
"""The title of the search result."""
    url: str
"""The URL of the search result."""
    published_date: str | None
"""The published date of the content, if available."""
    author: str | None
"""The author of the content, if available."""
    text: str
"""The text content of the search result."""
```

#### title `instance-attribute`

The title of the search result.

#### url `instance-attribute`

The URL of the search result.

#### published\_date `instance-attribute`

```
published_date: str | None
```

The published date of the content, if available.

The author of the content, if available.

#### text `instance-attribute`

The text content of the search result.

### ExaAnswerResult

Bases: `TypedDict`

An Exa answer result with citations.

See [Exa Answer API documentation](https://docs.exa.ai/reference/answer) for more information.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

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
```

```
classExaAnswerResult(TypedDict):
"""An Exa answer result with citations.

    See [Exa Answer API documentation](https://docs.exa.ai/reference/answer)
    for more information.
    """

    answer: str
"""The AI-generated answer to the query."""
    citations: list[dict[str, Any]]
"""Citations supporting the answer."""
```

#### answer `instance-attribute`

The AI-generated answer to the query.

#### citations `instance-attribute`

Citations supporting the answer.

### ExaContentResult

Bases: `TypedDict`

Content retrieved from a URL.

See [Exa Contents API documentation](https://docs.exa.ai/reference/get-contents) for more information.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
```

```
classExaContentResult(TypedDict):
"""Content retrieved from a URL.

    See [Exa Contents API documentation](https://docs.exa.ai/reference/get-contents)
    for more information.
    """

    url: str
"""The URL of the content."""
    title: str
"""The title of the page."""
    text: str
"""The text content of the page."""
    author: str | None
"""The author of the content, if available."""
    published_date: str | None
"""The published date of the content, if available."""
```

#### url `instance-attribute`

The URL of the content.

#### title `instance-attribute`

The title of the page.

#### text `instance-attribute`

The text content of the page.

#### author `instance-attribute`

The author of the content, if available.

#### published\_date `instance-attribute`

```
published_date: str | None
```

The published date of the content, if available.

### ExaSearchTool `dataclass`

The Exa search tool.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
115
116
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
```

```
@dataclass
classExaSearchTool:
"""The Exa search tool."""

    client: AsyncExa
"""The Exa async client."""

    num_results: int
"""The number of results to return."""

    max_characters: int | None
"""Maximum characters of text content per result, or None for no limit."""

    async def__call__(
        self,
        query: str,
        search_type: Literal['auto', 'keyword', 'neural', 'fast', 'deep'] = 'auto',
    ) -> list[ExaSearchResult]:
"""Searches Exa for the given query and returns the results with content.

        Args:
            query: The search query to execute with Exa.
            search_type: The type of search to perform. 'auto' automatically chooses
                the best search type, 'keyword' for exact matches, 'neural' for
                semantic search, 'fast' for speed-optimized search, 'deep' for
                comprehensive multi-query search.

        Returns:
            The search results with text content.
        """
        text_config: bool | dict[str, int] = {'maxCharacters': self.max_characters} if self.max_characters else True
        response = await self.client.search(  # pyright: ignore[reportUnknownMemberType]
            query,
            num_results=self.num_results,
            type=search_type,
            contents={'text': text_config},
        )

        return [
            ExaSearchResult(
                title=result.title or '',
                url=result.url,
                published_date=result.published_date,
                author=result.author,
                text=result.text or '',
            )
            for result in response.results
        ]
```

#### client `instance-attribute`

The Exa async client.

#### num\_results `instance-attribute`

The number of results to return.

#### max\_characters `instance-attribute`

```
max_characters: int | None
```

Maximum characters of text content per result, or None for no limit.

#### \_\_call\__ `async`

```
__call__(
    query: str,
    search_type: Literal[
        "auto", "keyword", "neural", "fast", "deep"
    ] = "auto",
) -> list[ExaSearchResult]
```

Searches Exa for the given query and returns the results with content.

Parameters:

Name Type Description Default `query` `str`

The search query to execute with Exa.

*required* `search_type` `Literal['auto', 'keyword', 'neural', 'fast', 'deep']`

The type of search to perform. 'auto' automatically chooses the best search type, 'keyword' for exact matches, 'neural' for semantic search, 'fast' for speed-optimized search, 'deep' for comprehensive multi-query search.

`'auto'`

Returns:

Type Description `list[ExaSearchResult]`

The search results with text content.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
115
116
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
```

```
async def__call__(
    self,
    query: str,
    search_type: Literal['auto', 'keyword', 'neural', 'fast', 'deep'] = 'auto',
) -> list[ExaSearchResult]:
"""Searches Exa for the given query and returns the results with content.

    Args:
        query: The search query to execute with Exa.
        search_type: The type of search to perform. 'auto' automatically chooses
            the best search type, 'keyword' for exact matches, 'neural' for
            semantic search, 'fast' for speed-optimized search, 'deep' for
            comprehensive multi-query search.

    Returns:
        The search results with text content.
    """
    text_config: bool | dict[str, int] = {'maxCharacters': self.max_characters} if self.max_characters else True
    response = await self.client.search(  # pyright: ignore[reportUnknownMemberType]
        query,
        num_results=self.num_results,
        type=search_type,
        contents={'text': text_config},
    )

    return [
        ExaSearchResult(
            title=result.title or '',
            url=result.url,
            published_date=result.published_date,
            author=result.author,
            text=result.text or '',
        )
        for result in response.results
    ]
```

### ExaFindSimilarTool `dataclass`

The Exa find similar tool.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
```

```
@dataclass
classExaFindSimilarTool:
"""The Exa find similar tool."""

    client: AsyncExa
"""The Exa async client."""

    num_results: int
"""The number of results to return."""

    async def__call__(
        self,
        url: str,
        exclude_source_domain: bool = True,
    ) -> list[ExaSearchResult]:
"""Finds pages similar to the given URL and returns them with content.

        Args:
            url: The URL to find similar pages for.
            exclude_source_domain: Whether to exclude results from the same domain
                as the input URL. Defaults to True.

        Returns:
            Similar pages with text content.
        """
        response = await self.client.find_similar(  # pyright: ignore[reportUnknownMemberType]
            url,
            num_results=self.num_results,
            exclude_source_domain=exclude_source_domain,
            contents={'text': True},
        )

        return [
            ExaSearchResult(
                title=result.title or '',
                url=result.url,
                published_date=result.published_date,
                author=result.author,
                text=result.text or '',
            )
            for result in response.results
        ]
```

#### client `instance-attribute`

The Exa async client.

#### num\_results `instance-attribute`

The number of results to return.

#### \_\_call\__ `async`

```
__call__(
    url: str, exclude_source_domain: bool = True
) -> list[ExaSearchResult]
```

Finds pages similar to the given URL and returns them with content.

Parameters:

Name Type Description Default `url` `str`

The URL to find similar pages for.

*required* `exclude_source_domain` `bool`

Whether to exclude results from the same domain as the input URL. Defaults to True.

`True`

Returns:

Type Description `list[ExaSearchResult]`

Similar pages with text content.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
```

```
async def__call__(
    self,
    url: str,
    exclude_source_domain: bool = True,
) -> list[ExaSearchResult]:
"""Finds pages similar to the given URL and returns them with content.

    Args:
        url: The URL to find similar pages for.
        exclude_source_domain: Whether to exclude results from the same domain
            as the input URL. Defaults to True.

    Returns:
        Similar pages with text content.
    """
    response = await self.client.find_similar(  # pyright: ignore[reportUnknownMemberType]
        url,
        num_results=self.num_results,
        exclude_source_domain=exclude_source_domain,
        contents={'text': True},
    )

    return [
        ExaSearchResult(
            title=result.title or '',
            url=result.url,
            published_date=result.published_date,
            author=result.author,
            text=result.text or '',
        )
        for result in response.results
    ]
```

### ExaGetContentsTool `dataclass`

The Exa get contents tool.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
```

```
@dataclass
classExaGetContentsTool:
"""The Exa get contents tool."""

    client: AsyncExa
"""The Exa async client."""

    async def__call__(
        self,
        urls: list[str],
    ) -> list[ExaContentResult]:
"""Gets the content of the specified URLs.

        Args:
            urls: A list of URLs to get content for.

        Returns:
            The content of each URL.
        """
        response = await self.client.get_contents(urls, text=True)  # pyright: ignore[reportUnknownMemberType,reportUnknownVariableType]

        return [
            ExaContentResult(
                url=result.url,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
                title=result.title or '',  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
                text=result.text or '',  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
                author=result.author,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
                published_date=result.published_date,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
            )
            for result in response.results  # pyright: ignore[reportUnknownVariableType,reportUnknownMemberType]
        ]
```

#### client `instance-attribute`

The Exa async client.

#### \_\_call\__ `async`

Gets the content of the specified URLs.

Parameters:

Name Type Description Default `urls` `list[str]`

A list of URLs to get content for.

*required*

Returns:

Type Description `list[ExaContentResult]`

The content of each URL.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
```

```
async def__call__(
    self,
    urls: list[str],
) -> list[ExaContentResult]:
"""Gets the content of the specified URLs.

    Args:
        urls: A list of URLs to get content for.

    Returns:
        The content of each URL.
    """
    response = await self.client.get_contents(urls, text=True)  # pyright: ignore[reportUnknownMemberType,reportUnknownVariableType]

    return [
        ExaContentResult(
            url=result.url,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
            title=result.title or '',  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
            text=result.text or '',  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
            author=result.author,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
            published_date=result.published_date,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
        )
        for result in response.results  # pyright: ignore[reportUnknownVariableType,reportUnknownMemberType]
    ]
```

### ExaAnswerTool `dataclass`

The Exa answer tool.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
211
212
213
214
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
```

```
@dataclass
classExaAnswerTool:
"""The Exa answer tool."""

    client: AsyncExa
"""The Exa async client."""

    async def__call__(
        self,
        query: str,
    ) -> ExaAnswerResult:
"""Generates an AI-powered answer to the query with citations.

        Args:
            query: The question to answer.

        Returns:
            An answer with supporting citations from web sources.
        """
        response = await self.client.answer(query, text=True)

        return ExaAnswerResult(
            answer=response.answer,  # pyright: ignore[reportUnknownMemberType,reportArgumentType,reportAttributeAccessIssue]
            citations=[
                {
                    'url': citation.url,  # pyright: ignore[reportUnknownMemberType]
                    'title': citation.title or '',  # pyright: ignore[reportUnknownMemberType]
                    'text': citation.text or '',  # pyright: ignore[reportUnknownMemberType]
                }
                for citation in response.citations  # pyright: ignore[reportUnknownVariableType,reportUnknownMemberType,reportAttributeAccessIssue]
            ],
        )
```

#### client `instance-attribute`

The Exa async client.

#### \_\_call\__ `async`

```
__call__(query: str) -> ExaAnswerResult
```

Generates an AI-powered answer to the query with citations.

Parameters:

Name Type Description Default `query` `str`

The question to answer.

*required*

Returns:

Type Description `ExaAnswerResult`

An answer with supporting citations from web sources.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
```

```
async def__call__(
    self,
    query: str,
) -> ExaAnswerResult:
"""Generates an AI-powered answer to the query with citations.

    Args:
        query: The question to answer.

    Returns:
        An answer with supporting citations from web sources.
    """
    response = await self.client.answer(query, text=True)

    return ExaAnswerResult(
        answer=response.answer,  # pyright: ignore[reportUnknownMemberType,reportArgumentType,reportAttributeAccessIssue]
        citations=[
            {
                'url': citation.url,  # pyright: ignore[reportUnknownMemberType]
                'title': citation.title or '',  # pyright: ignore[reportUnknownMemberType]
                'text': citation.text or '',  # pyright: ignore[reportUnknownMemberType]
            }
            for citation in response.citations  # pyright: ignore[reportUnknownVariableType,reportUnknownMemberType,reportAttributeAccessIssue]
        ],
    )
```

### exa\_search\_tool

```
exa_search_tool(
    api_key: str,
    *,
    num_results: int = 5,
    max_characters: int | None = None
) -> Tool[Any]
```

```
exa_search_tool(
    *,
    client: AsyncExa,
    num_results: int = 5,
    max_characters: int | None = None
) -> Tool[Any]
```

```
exa_search_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None,
    num_results: int = 5,
    max_characters: int | None = None
) -> Tool[Any]
```

Creates an Exa search tool.

Parameters:

Name Type Description Default `api_key` `str | None`

The Exa API key. Required if `client` is not provided.

You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).

`None` `client` `AsyncExa | None`

An existing AsyncExa client. If provided, `api_key` is ignored. This is useful for sharing a client across multiple tools.

`None` `num_results` `int`

The number of results to return. Defaults to 5.

`5` `max_characters` `int | None`

Maximum characters of text content per result. Use this to limit token usage. Defaults to None (no limit).

`None`

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
```

```
defexa_search_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None,
    num_results: int = 5,
    max_characters: int | None = None,
) -> Tool[Any]:
"""Creates an Exa search tool.

    Args:
        api_key: The Exa API key. Required if `client` is not provided.

            You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
        client: An existing AsyncExa client. If provided, `api_key` is ignored.
            This is useful for sharing a client across multiple tools.
        num_results: The number of results to return. Defaults to 5.
        max_characters: Maximum characters of text content per result. Use this to limit
            token usage. Defaults to None (no limit).
    """
    if client is None:
        if api_key is None:
            raise ValueError('Either api_key or client must be provided')
        client = AsyncExa(api_key=api_key)
    return Tool[Any](
        ExaSearchTool(
            client=client,
            num_results=num_results,
            max_characters=max_characters,
        ).__call__,
        name='exa_search',
        description='Searches Exa for the given query and returns the results with content. Exa is a neural search engine that finds high-quality, relevant results.',
    )
```

### exa\_find\_similar\_tool

```
exa_find_similar_tool(
    api_key: str, *, num_results: int = 5
) -> Tool[Any]
```

```
exa_find_similar_tool(
    *, client: AsyncExa, num_results: int = 5
) -> Tool[Any]
```

```
exa_find_similar_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None,
    num_results: int = 5
) -> Tool[Any]
```

Creates an Exa find similar tool.

Parameters:

Name Type Description Default `api_key` `str | None`

The Exa API key. Required if `client` is not provided.

You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).

`None` `client` `AsyncExa | None`

An existing AsyncExa client. If provided, `api_key` is ignored. This is useful for sharing a client across multiple tools.

`None` `num_results` `int`

The number of similar results to return. Defaults to 5.

`5`

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
```

```
defexa_find_similar_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None,
    num_results: int = 5,
) -> Tool[Any]:
"""Creates an Exa find similar tool.

    Args:
        api_key: The Exa API key. Required if `client` is not provided.

            You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
        client: An existing AsyncExa client. If provided, `api_key` is ignored.
            This is useful for sharing a client across multiple tools.
        num_results: The number of similar results to return. Defaults to 5.
    """
    if client is None:
        if api_key is None:
            raise ValueError('Either api_key or client must be provided')
        client = AsyncExa(api_key=api_key)
    return Tool[Any](
        ExaFindSimilarTool(client=client, num_results=num_results).__call__,
        name='exa_find_similar',
        description='Finds web pages similar to a given URL. Useful for discovering related content, competitors, or alternative sources.',
    )
```

### exa\_get\_contents\_tool

```
exa_get_contents_tool(*, client: AsyncExa) -> Tool[Any]
```

```
exa_get_contents_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None
) -> Tool[Any]
```

Creates an Exa get contents tool.

Parameters:

Name Type Description Default `api_key` `str | None`

The Exa API key. Required if `client` is not provided.

You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).

`None` `client` `AsyncExa | None`

An existing AsyncExa client. If provided, `api_key` is ignored. This is useful for sharing a client across multiple tools.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
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
```

```
defexa_get_contents_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None,
) -> Tool[Any]:
"""Creates an Exa get contents tool.

    Args:
        api_key: The Exa API key. Required if `client` is not provided.

            You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
        client: An existing AsyncExa client. If provided, `api_key` is ignored.
            This is useful for sharing a client across multiple tools.
    """
    if client is None:
        if api_key is None:
            raise ValueError('Either api_key or client must be provided')
        client = AsyncExa(api_key=api_key)
    return Tool[Any](
        ExaGetContentsTool(client=client).__call__,
        name='exa_get_contents',
        description='Gets the full text content of specified URLs. Useful for reading articles, documentation, or any web page when you have the exact URL.',
    )
```

### exa\_answer\_tool

```
exa_answer_tool(*, client: AsyncExa) -> Tool[Any]
```

```
exa_answer_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None
) -> Tool[Any]
```

Creates an Exa answer tool.

Parameters:

Name Type Description Default `api_key` `str | None`

The Exa API key. Required if `client` is not provided.

You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).

`None` `client` `AsyncExa | None`

An existing AsyncExa client. If provided, `api_key` is ignored. This is useful for sharing a client across multiple tools.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
```

```
defexa_answer_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None,
) -> Tool[Any]:
"""Creates an Exa answer tool.

    Args:
        api_key: The Exa API key. Required if `client` is not provided.

            You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
        client: An existing AsyncExa client. If provided, `api_key` is ignored.
            This is useful for sharing a client across multiple tools.
    """
    if client is None:
        if api_key is None:
            raise ValueError('Either api_key or client must be provided')
        client = AsyncExa(api_key=api_key)
    return Tool[Any](
        ExaAnswerTool(client=client).__call__,
        name='exa_answer',
        description='Generates an AI-powered answer to a question with citations from web sources. Returns a comprehensive answer backed by real sources.',
    )
```

### ExaToolset

Bases: `FunctionToolset`

A toolset that provides Exa search tools with a shared client.

This is more efficient than creating individual tools when using multiple Exa tools, as it shares a single API client across all tools.

Example:

```
frompydantic_aiimport Agent
frompydantic_ai.common_tools.exaimport ExaToolset

toolset = ExaToolset(api_key='your-api-key')
agent = Agent('openai:gpt-4o', toolsets=[toolset])
```

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
```

````
classExaToolset(FunctionToolset):
"""A toolset that provides Exa search tools with a shared client.

    This is more efficient than creating individual tools when using multiple
    Exa tools, as it shares a single API client across all tools.

    Example:
    ```python
    from pydantic_ai import Agent
    from pydantic_ai.common_tools.exa import ExaToolset

    toolset = ExaToolset(api_key='your-api-key')
    agent = Agent('openai:gpt-4o', toolsets=[toolset])
    ```
    """

    def__init__(
        self,
        api_key: str,
        *,
        num_results: int = 5,
        max_characters: int | None = None,
        include_search: bool = True,
        include_find_similar: bool = True,
        include_get_contents: bool = True,
        include_answer: bool = True,
        id: str | None = None,
    ):
"""Creates an Exa toolset with a shared client.

        Args:
            api_key: The Exa API key.

                You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
            num_results: The number of results to return for search and find_similar. Defaults to 5.
            max_characters: Maximum characters of text content per result. Use this to limit
                token usage. Defaults to None (no limit).
            include_search: Whether to include the search tool. Defaults to True.
            include_find_similar: Whether to include the find_similar tool. Defaults to True.
            include_get_contents: Whether to include the get_contents tool. Defaults to True.
            include_answer: Whether to include the answer tool. Defaults to True.
            id: Optional ID for the toolset, used for durable execution environments.
        """
        client = AsyncExa(api_key=api_key)
        tools: list[Tool[Any]] = []

        if include_search:
            tools.append(exa_search_tool(client=client, num_results=num_results, max_characters=max_characters))

        if include_find_similar:
            tools.append(exa_find_similar_tool(client=client, num_results=num_results))

        if include_get_contents:
            tools.append(exa_get_contents_tool(client=client))

        if include_answer:
            tools.append(exa_answer_tool(client=client))

        super().__init__(tools, id=id)
````

#### \_\_init\__

```
__init__(
    api_key: str,
    *,
    num_results: int = 5,
    max_characters: int | None = None,
    include_search: bool = True,
    include_find_similar: bool = True,
    include_get_contents: bool = True,
    include_answer: bool = True,
    id: str | None = None
)
```

Creates an Exa toolset with a shared client.

Parameters:

Name Type Description Default `api_key` `str`

The Exa API key.

You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).

*required* `num_results` `int`

The number of results to return for search and find\_similar. Defaults to 5.

`5` `max_characters` `int | None`

Maximum characters of text content per result. Use this to limit token usage. Defaults to None (no limit).

`None` `include_search` `bool`

Whether to include the search tool. Defaults to True.

`True` `include_find_similar` `bool`

Whether to include the find\_similar tool. Defaults to True.

`True` `include_get_contents` `bool`

Whether to include the get\_contents tool. Defaults to True.

`True` `include_answer` `bool`

Whether to include the answer tool. Defaults to True.

`True` `id` `str | None`

Optional ID for the toolset, used for durable execution environments.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`

```
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
```

```
def__init__(
    self,
    api_key: str,
    *,
    num_results: int = 5,
    max_characters: int | None = None,
    include_search: bool = True,
    include_find_similar: bool = True,
    include_get_contents: bool = True,
    include_answer: bool = True,
    id: str | None = None,
):
"""Creates an Exa toolset with a shared client.

    Args:
        api_key: The Exa API key.

            You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
        num_results: The number of results to return for search and find_similar. Defaults to 5.
        max_characters: Maximum characters of text content per result. Use this to limit
            token usage. Defaults to None (no limit).
        include_search: Whether to include the search tool. Defaults to True.
        include_find_similar: Whether to include the find_similar tool. Defaults to True.
        include_get_contents: Whether to include the get_contents tool. Defaults to True.
        include_answer: Whether to include the answer tool. Defaults to True.
        id: Optional ID for the toolset, used for durable execution environments.
    """
    client = AsyncExa(api_key=api_key)
    tools: list[Tool[Any]] = []

    if include_search:
        tools.append(exa_search_tool(client=client, num_results=num_results, max_characters=max_characters))

    if include_find_similar:
        tools.append(exa_find_similar_tool(client=client, num_results=num_results))

    if include_get_contents:
        tools.append(exa_get_contents_tool(client=client))

    if include_answer:
        tools.append(exa_answer_tool(client=client))

    super().__init__(tools, id=id)
```

### TavilySearchResult

Bases: `TypedDict`

A Tavily search result.

See [Tavily Search Endpoint documentation](https://docs.tavily.com/api-reference/endpoint/search) for more information.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/tavily.py`

```
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
```

```
classTavilySearchResult(TypedDict):
"""A Tavily search result.

    See [Tavily Search Endpoint documentation](https://docs.tavily.com/api-reference/endpoint/search)
    for more information.
    """

    title: str
"""The title of the search result."""
    url: str
"""The URL of the search result.."""
    content: str
"""A short description of the search result."""
    score: float
"""The relevance score of the search result."""
```

#### title `instance-attribute`

The title of the search result.

#### url `instance-attribute`

The URL of the search result..

#### content `instance-attribute`

A short description of the search result.

#### score `instance-attribute`

The relevance score of the search result.

### TavilySearchTool `dataclass`

The Tavily search tool.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/tavily.py`

```
40
41
42
43
44
45
46
47
48
49
50
51
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
```

```
@dataclass
classTavilySearchTool:
"""The Tavily search tool."""

    client: AsyncTavilyClient
"""The Tavily search client."""

    async def__call__(
        self,
        query: str,
        search_deep: Literal['basic', 'advanced'] = 'basic',
        topic: Literal['general', 'news'] = 'general',
        time_range: Literal['day', 'week', 'month', 'year', 'd', 'w', 'm', 'y'] | None = None,
    ) -> list[TavilySearchResult]:
"""Searches Tavily for the given query and returns the results.

        Args:
            query: The search query to execute with Tavily.
            search_deep: The depth of the search.
            topic: The category of the search.
            time_range: The time range back from the current date to filter results.

        Returns:
            A list of search results from Tavily.
        """
        results = await self.client.search(query, search_depth=search_deep, topic=topic, time_range=time_range)  # type: ignore[reportUnknownMemberType]
        return tavily_search_ta.validate_python(results['results'])
```

#### client `instance-attribute`

```
client: AsyncTavilyClient
```

The Tavily search client.

#### \_\_call\__ `async`

```
__call__(
    query: str,
    search_deep: Literal["basic", "advanced"] = "basic",
    topic: Literal["general", "news"] = "general",
    time_range: (
        Literal[
            "day",
            "week",
            "month",
            "year",
            "d",
            "w",
            "m",
            "y",
        ]
        | None
    ) = None,
) -> list[TavilySearchResult]
```

Searches Tavily for the given query and returns the results.

Parameters:

Name Type Description Default `query` `str`

The search query to execute with Tavily.

*required* `search_deep` `Literal['basic', 'advanced']`

The depth of the search.

`'basic'` `topic` `Literal['general', 'news']`

The category of the search.

`'general'` `time_range` `Literal['day', 'week', 'month', 'year', 'd', 'w', 'm', 'y'] | None`

The time range back from the current date to filter results.

`None`

Returns:

Type Description `list[TavilySearchResult]`

A list of search results from Tavily.

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/tavily.py`

```
47
48
49
50
51
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
```

```
async def__call__(
    self,
    query: str,
    search_deep: Literal['basic', 'advanced'] = 'basic',
    topic: Literal['general', 'news'] = 'general',
    time_range: Literal['day', 'week', 'month', 'year', 'd', 'w', 'm', 'y'] | None = None,
) -> list[TavilySearchResult]:
"""Searches Tavily for the given query and returns the results.

    Args:
        query: The search query to execute with Tavily.
        search_deep: The depth of the search.
        topic: The category of the search.
        time_range: The time range back from the current date to filter results.

    Returns:
        A list of search results from Tavily.
    """
    results = await self.client.search(query, search_depth=search_deep, topic=topic, time_range=time_range)  # type: ignore[reportUnknownMemberType]
    return tavily_search_ta.validate_python(results['results'])
```

### tavily\_search\_tool

```
tavily_search_tool(api_key: str)
```

Creates a Tavily search tool.

Parameters:

Name Type Description Default `api_key` `str`

The Tavily API key.

You can get one by signing up at [https://app.tavily.com/home](https://app.tavily.com/home).

*required*

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/tavily.py`

```
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
```

```
deftavily_search_tool(api_key: str):
"""Creates a Tavily search tool.

    Args:
        api_key: The Tavily API key.

            You can get one by signing up at [https://app.tavily.com/home](https://app.tavily.com/home).
    """
    return Tool[Any](
        TavilySearchTool(client=AsyncTavilyClient(api_key)).__call__,
        name='tavily_search',
        description='Searches Tavily for the given query and returns the results.',
    )
```