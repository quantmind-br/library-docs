---
title: pydantic_ai.providers - Pydantic AI
url: https://ai.pydantic.dev/api/providers/
source: sitemap
fetched_at: 2026-01-22T22:24:11.08491635-03:00
rendered_js: false
word_count: 11
summary: This document defines the BedrockProvider class for interacting with AWS Bedrock, covering client initialization, authentication methods, and model profile mapping.
tags:
    - aws-bedrock
    - python
    - api-client
    - boto3
    - llm-integration
    - authentication
category: api
---

```
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
```

```
classBedrockProvider(Provider[BaseClient]):
"""Provider for AWS Bedrock."""

    @property
    defname(self) -> str:
        return 'bedrock'

    @property
    defbase_url(self) -> str:
        return self._client.meta.endpoint_url

    @property
    defclient(self) -> BaseClient:
        return self._client

    defmodel_profile(self, model_name: str) -> ModelProfile | None:
        provider_to_profile: dict[str, Callable[[str], ModelProfile | None]] = {
            'anthropic': lambda model_name: BedrockModelProfile(
                bedrock_supports_tool_choice=True,
                bedrock_send_back_thinking_parts=True,
                bedrock_supports_prompt_caching=True,
                bedrock_supports_tool_caching=True,
            ).update(_without_builtin_tools(anthropic_model_profile(model_name))),
            'mistral': lambda model_name: BedrockModelProfile(bedrock_tool_result_format='json').update(
                _without_builtin_tools(mistral_model_profile(model_name))
            ),
            'cohere': lambda model_name: _without_builtin_tools(cohere_model_profile(model_name)),
            'amazon': bedrock_amazon_model_profile,
            'meta': lambda model_name: _without_builtin_tools(meta_model_profile(model_name)),
            'deepseek': lambda model_name: _without_builtin_tools(bedrock_deepseek_model_profile(model_name)),
        }

        # Split the model name into parts
        parts = model_name.split('.', 2)

        # Handle regional prefixes
        if len(parts) > 2 and parts[0] in BEDROCK_GEO_PREFIXES:
            parts = parts[1:]

        # required format is provider.model-name-with-version
        if len(parts) < 2:
            return None

        provider = parts[0]
        model_name_with_version = parts[1]

        # Remove version suffix if it matches the format (e.g. "-v1:0" or "-v14")
        version_match = re.match(r'(.+)-v\d+(?::\d+)?$', model_name_with_version)
        if version_match:
            model_name = version_match.group(1)
        else:
            model_name = model_name_with_version

        if provider in provider_to_profile:
            return provider_to_profile[provider](model_name)

        return None

    @overload
    def__init__(self, *, bedrock_client: BaseClient) -> None: ...

    @overload
    def__init__(
        self,
        *,
        api_key: str,
        base_url: str | None = None,
        region_name: str | None = None,
        profile_name: str | None = None,
        aws_read_timeout: float | None = None,
        aws_connect_timeout: float | None = None,
    ) -> None: ...

    @overload
    def__init__(
        self,
        *,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        aws_session_token: str | None = None,
        base_url: str | None = None,
        region_name: str | None = None,
        profile_name: str | None = None,
        aws_read_timeout: float | None = None,
        aws_connect_timeout: float | None = None,
    ) -> None: ...

    def__init__(
        self,
        *,
        bedrock_client: BaseClient | None = None,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        aws_session_token: str | None = None,
        base_url: str | None = None,
        region_name: str | None = None,
        profile_name: str | None = None,
        api_key: str | None = None,
        aws_read_timeout: float | None = None,
        aws_connect_timeout: float | None = None,
    ) -> None:
"""Initialize the Bedrock provider.

        Args:
            bedrock_client: A boto3 client for Bedrock Runtime. If provided, other arguments are ignored.
            aws_access_key_id: The AWS access key ID. If not set, the `AWS_ACCESS_KEY_ID` environment variable will be used if available.
            aws_secret_access_key: The AWS secret access key. If not set, the `AWS_SECRET_ACCESS_KEY` environment variable will be used if available.
            aws_session_token: The AWS session token. If not set, the `AWS_SESSION_TOKEN` environment variable will be used if available.
            api_key: The API key for Bedrock client. Can be used instead of `aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token`. If not set, the `AWS_BEARER_TOKEN_BEDROCK` environment variable will be used if available.
            base_url: The base URL for the Bedrock client.
            region_name: The AWS region name. If not set, the `AWS_DEFAULT_REGION` environment variable will be used if available.
            profile_name: The AWS profile name.
            aws_read_timeout: The read timeout for Bedrock client.
            aws_connect_timeout: The connect timeout for Bedrock client.
        """
        if bedrock_client is not None:
            self._client = bedrock_client
        else:
            read_timeout = aws_read_timeout or float(os.getenv('AWS_READ_TIMEOUT', 300))
            connect_timeout = aws_connect_timeout or float(os.getenv('AWS_CONNECT_TIMEOUT', 60))
            config: dict[str, Any] = {
                'read_timeout': read_timeout,
                'connect_timeout': connect_timeout,
            }
            api_key = api_key or os.getenv('AWS_BEARER_TOKEN_BEDROCK')
            try:
                if api_key is not None:
                    session = boto3.Session(
                        botocore_session=_BearerTokenSession(api_key),
                        region_name=region_name,
                        profile_name=profile_name,
                    )
                    config['signature_version'] = 'bearer'
                else:
                    session = boto3.Session(
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        aws_session_token=aws_session_token,
                        region_name=region_name,
                        profile_name=profile_name,
                    )
                self._client = session.client(  # type: ignore[reportUnknownMemberType]
                    'bedrock-runtime',
                    config=Config(**config),
                    endpoint_url=base_url,
                )
            except NoRegionError as exc:  # pragma: no cover
                raise UserError('You must provide a `region_name` or a boto3 client for Bedrock Runtime.') fromexc
```