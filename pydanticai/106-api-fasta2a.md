---
title: fasta2a - Pydantic AI
url: https://ai.pydantic.dev/api/fasta2a/
source: sitemap
fetched_at: 2026-01-22T22:24:04.275005426-03:00
rendered_js: false
word_count: 2952
summary: Defines the core FastA2A application class and the Broker abstract base class for building AI agent-to-agent interfaces using Starlette.
tags:
    - fasta2a
    - python
    - starlette
    - agent-to-agent
    - task-management
    - api-reference
category: api
---

### FastA2A

Bases: `Starlette`

The main class for the FastA2A library.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/applications.py`

```
 29
 30
 31
 32
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
```

```
classFastA2A(Starlette):
"""The main class for the FastA2A library."""

    def__init__(
        self,
        *,
        storage: Storage,
        broker: Broker,
        # Agent card
        name: str | None = None,
        url: str = 'http://localhost:8000',
        version: str = '1.0.0',
        description: str | None = None,
        provider: AgentProvider | None = None,
        skills: list[Skill] | None = None,
        # Starlette
        debug: bool = False,
        routes: Sequence[Route] | None = None,
        middleware: Sequence[Middleware] | None = None,
        exception_handlers: dict[Any, ExceptionHandler] | None = None,
        lifespan: Lifespan[FastA2A] | None = None,
    ):
        if lifespan is None:
            lifespan = _default_lifespan

        super().__init__(
            debug=debug,
            routes=routes,
            middleware=middleware,
            exception_handlers=exception_handlers,
            lifespan=lifespan,
        )

        self.name = name or 'My Agent'
        self.url = url
        self.version = version
        self.description = description
        self.provider = provider
        self.skills = skills or []
        # NOTE: For now, I don't think there's any reason to support any other input/output modes.
        self.default_input_modes = ['application/json']
        self.default_output_modes = ['application/json']

        self.task_manager = TaskManager(broker=broker, storage=storage)

        # Setup
        self._agent_card_json_schema: bytes | None = None
        self.router.add_route(
            '/.well-known/agent-card.json', self._agent_card_endpoint, methods=['HEAD', 'GET', 'OPTIONS']
        )
        self.router.add_route('/', self._agent_run_endpoint, methods=['POST'])
        self.router.add_route('/docs', self._docs_endpoint, methods=['GET'])

    async def__call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope['type'] == 'http' and not self.task_manager.is_running:
            raise RuntimeError('TaskManager was not properly initialized.')
        await super().__call__(scope, receive, send)

    async def_agent_card_endpoint(self, request: Request) -> Response:
        if self._agent_card_json_schema is None:
            agent_card = AgentCard(
                name=self.name,
                description=self.description or 'An AI agent exposed as an A2A agent.',
                url=self.url,
                version=self.version,
                protocol_version='0.3.0',
                skills=self.skills,
                default_input_modes=self.default_input_modes,
                default_output_modes=self.default_output_modes,
                capabilities=AgentCapabilities(
                    streaming=False, push_notifications=False, state_transition_history=False
                ),
            )
            if self.provider is not None:
                agent_card['provider'] = self.provider
            self._agent_card_json_schema = agent_card_ta.dump_json(agent_card, by_alias=True)
        return Response(content=self._agent_card_json_schema, media_type='application/json')

    async def_docs_endpoint(self, request: Request) -> Response:
"""Serve the documentation interface."""
        docs_path = Path(__file__).parent / 'static' / 'docs.html'
        return FileResponse(docs_path, media_type='text/html')

    async def_agent_run_endpoint(self, request: Request) -> Response:
"""This is the main endpoint for the A2A server.

        Although the specification allows freedom of choice and implementation, I'm pretty sure about some decisions.

        1. The server will always either send a "submitted" or a "failed" on `message/send`.
            Never a "completed" on the first message.
        2. There are three possible ends for the task:
            2.1. The task was "completed" successfully.
            2.2. The task was "canceled".
            2.3. The task "failed".
        3. The server will send a "working" on the first chunk on `tasks/pushNotification/get`.
        """
        data = await request.body()
        a2a_request = a2a_request_ta.validate_json(data)

        if a2a_request['method'] == 'message/send':
            jsonrpc_response = await self.task_manager.send_message(a2a_request)
        elif a2a_request['method'] == 'tasks/get':
            jsonrpc_response = await self.task_manager.get_task(a2a_request)
        elif a2a_request['method'] == 'tasks/cancel':
            jsonrpc_response = await self.task_manager.cancel_task(a2a_request)
        else:
            raise NotImplementedError(f'Method {a2a_request["method"]} not implemented.')
        return Response(
            content=a2a_response_ta.dump_json(jsonrpc_response, by_alias=True), media_type='application/json'
        )
```

### Broker `dataclass`

Bases: `ABC`

The broker class is in charge of scheduling the tasks.

The HTTP server uses the broker to schedule tasks.

The simple implementation is the `InMemoryBroker`, which is the broker that runs the tasks in the same process as the HTTP server. That said, this class can be extended to support remote workers.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/broker.py`

```
19
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
50
51
52
```

```
@dataclass
classBroker(ABC):
"""The broker class is in charge of scheduling the tasks.

    The HTTP server uses the broker to schedule tasks.

    The simple implementation is the `InMemoryBroker`, which is the broker that
    runs the tasks in the same process as the HTTP server. That said, this class can be
    extended to support remote workers.
    """

    @abstractmethod
    async defrun_task(self, params: TaskSendParams) -> None:
"""Send a task to be executed by the worker."""
        raise NotImplementedError('send_run_task is not implemented yet.')

    @abstractmethod
    async defcancel_task(self, params: TaskIdParams) -> None:
"""Cancel a task."""
        raise NotImplementedError('send_cancel_task is not implemented yet.')

    @abstractmethod
    async def__aenter__(self) -> Self: ...

    @abstractmethod
    async def__aexit__(self, exc_type: Any, exc_value: Any, traceback: Any): ...

    @abstractmethod
    defreceive_task_operations(self) -> AsyncIterator[TaskOperation]:
"""Receive task operations from the broker.

        On a multi-worker setup, the broker will need to round-robin the task operations
        between the workers.
        """
```

#### run\_task `abstractmethod` `async`

```
run_task(params: TaskSendParams) -> None
```

Send a task to be executed by the worker.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/broker.py`

```
@abstractmethod
async defrun_task(self, params: TaskSendParams) -> None:
"""Send a task to be executed by the worker."""
    raise NotImplementedError('send_run_task is not implemented yet.')
```

#### cancel\_task `abstractmethod` `async`

```
cancel_task(params: TaskIdParams) -> None
```

Cancel a task.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/broker.py`

```
@abstractmethod
async defcancel_task(self, params: TaskIdParams) -> None:
"""Cancel a task."""
    raise NotImplementedError('send_cancel_task is not implemented yet.')
```

#### receive\_task\_operations `abstractmethod`

Receive task operations from the broker.

On a multi-worker setup, the broker will need to round-robin the task operations between the workers.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/broker.py`

```
@abstractmethod
defreceive_task_operations(self) -> AsyncIterator[TaskOperation]:
"""Receive task operations from the broker.

    On a multi-worker setup, the broker will need to round-robin the task operations
    between the workers.
    """
```

### Skill

Bases: `TypedDict`

Skills are a unit of capability that an agent can perform.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
227
228
229
```

```
@pydantic.with_config({'alias_generator': to_camel})
classSkill(TypedDict):
"""Skills are a unit of capability that an agent can perform."""

    id: str
"""A unique identifier for the skill."""

    name: str
"""Human readable name of the skill."""

    description: str
"""A human-readable description of the skill.

    It will be used by the client or a human as a hint to understand the skill.
    """

    tags: list[str]
"""Set of tag-words describing classes of capabilities for this specific skill.

    Examples: "cooking", "customer support", "billing".
    """

    examples: NotRequired[list[str]]
"""The set of example scenarios that the skill can perform.

    Will be used by the client as a hint to understand how the skill can be used. (e.g. "I need a recipe for bread")
    """

    input_modes: list[str]
"""Supported mime types for input data."""

    output_modes: list[str]
"""Supported mime types for output data."""
```

#### id `instance-attribute`

A unique identifier for the skill.

#### name `instance-attribute`

Human readable name of the skill.

#### description `instance-attribute`

A human-readable description of the skill.

It will be used by the client or a human as a hint to understand the skill.

#### tags `instance-attribute`

Set of tag-words describing classes of capabilities for this specific skill.

Examples: "cooking", "customer support", "billing".

#### examples `instance-attribute`

The set of example scenarios that the skill can perform.

Will be used by the client as a hint to understand how the skill can be used. (e.g. "I need a recipe for bread")

#### input\_modes `instance-attribute`

Supported mime types for input data.

#### output\_modes `instance-attribute`

Supported mime types for output data.

### Storage

Bases: `ABC`, `Generic[ContextT]`

A storage to retrieve and save tasks, as well as retrieve and save context.

The storage serves two purposes: 1. Task storage: Stores tasks in A2A protocol format with their status, artifacts, and message history 2. Context storage: Stores conversation context in a format optimized for the specific agent implementation

Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`

```
17
18
19
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
50
51
52
53
54
55
```

```
classStorage(ABC, Generic[ContextT]):
"""A storage to retrieve and save tasks, as well as retrieve and save context.

    The storage serves two purposes:
    1. Task storage: Stores tasks in A2A protocol format with their status, artifacts, and message history
    2. Context storage: Stores conversation context in a format optimized for the specific agent implementation
    """

    @abstractmethod
    async defload_task(self, task_id: str, history_length: int | None = None) -> Task | None:
"""Load a task from storage.

        If the task is not found, return None.
        """

    @abstractmethod
    async defsubmit_task(self, context_id: str, message: Message) -> Task:
"""Submit a task to storage."""

    @abstractmethod
    async defupdate_task(
        self,
        task_id: str,
        state: TaskState,
        new_artifacts: list[Artifact] | None = None,
        new_messages: list[Message] | None = None,
    ) -> Task:
"""Update the state of a task. Appends artifacts and messages, if specified."""

    @abstractmethod
    async defload_context(self, context_id: str) -> ContextT | None:
"""Retrieve the stored context given the `context_id`."""

    @abstractmethod
    async defupdate_context(self, context_id: str, context: ContextT) -> None:
"""Updates the context for a `context_id`.

        Implementing agent can decide what to store in context.
        """
```

#### load\_task `abstractmethod` `async`

```
load_task(
    task_id: str, history_length: int | None = None
) -> Task | None
```

Load a task from storage.

If the task is not found, return None.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`

```
@abstractmethod
async defload_task(self, task_id: str, history_length: int | None = None) -> Task | None:
"""Load a task from storage.

    If the task is not found, return None.
    """
```

#### submit\_task `abstractmethod` `async`

```
submit_task(context_id: str, message: Message) -> Task
```

Submit a task to storage.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`

```
@abstractmethod
async defsubmit_task(self, context_id: str, message: Message) -> Task:
"""Submit a task to storage."""
```

#### update\_task `abstractmethod` `async`

```
update_task(
    task_id: str,
    state: TaskState,
    new_artifacts: list[Artifact] | None = None,
    new_messages: list[Message] | None = None,
) -> Task
```

Update the state of a task. Appends artifacts and messages, if specified.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`

```
36
37
38
39
40
41
42
43
44
```

```
@abstractmethod
async defupdate_task(
    self,
    task_id: str,
    state: TaskState,
    new_artifacts: list[Artifact] | None = None,
    new_messages: list[Message] | None = None,
) -> Task:
"""Update the state of a task. Appends artifacts and messages, if specified."""
```

#### load\_context `abstractmethod` `async`

```
load_context(context_id: str) -> ContextT | None
```

Retrieve the stored context given the `context_id`.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`

```
@abstractmethod
async defload_context(self, context_id: str) -> ContextT | None:
"""Retrieve the stored context given the `context_id`."""
```

#### update\_context `abstractmethod` `async`

```
update_context(context_id: str, context: ContextT) -> None
```

Updates the context for a `context_id`.

Implementing agent can decide what to store in context.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`

```
@abstractmethod
async defupdate_context(self, context_id: str, context: ContextT) -> None:
"""Updates the context for a `context_id`.

    Implementing agent can decide what to store in context.
    """
```

### Worker `dataclass`

Bases: `ABC`, `Generic[ContextT]`

A worker is responsible for executing tasks.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/worker.py`

```
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
67
68
69
```

```
@dataclass
classWorker(ABC, Generic[ContextT]):
"""A worker is responsible for executing tasks."""

    broker: Broker
    storage: Storage[ContextT]

    @asynccontextmanager
    async defrun(self) -> AsyncIterator[None]:
"""Run the worker.

        It connects to the broker, and it makes itself available to receive commands.
        """
        async with anyio.create_task_group() as tg:
            tg.start_soon(self._loop)
            yield
            tg.cancel_scope.cancel()

    async def_loop(self) -> None:
        async for task_operation in self.broker.receive_task_operations():
            await self._handle_task_operation(task_operation)

    async def_handle_task_operation(self, task_operation: TaskOperation) -> None:
        try:
            with use_span(task_operation['_current_span']):
                with tracer.start_as_current_span(
                    f'{task_operation["operation"]} task', attributes={'logfire.tags': ['fasta2a']}
                ):
                    if task_operation['operation'] == 'run':
                        await self.run_task(task_operation['params'])
                    elif task_operation['operation'] == 'cancel':
                        await self.cancel_task(task_operation['params'])
                    else:
                        assert_never(task_operation)
        except Exception:
            await self.storage.update_task(task_operation['params']['id'], state='failed')

    @abstractmethod
    async defrun_task(self, params: TaskSendParams) -> None: ...

    @abstractmethod
    async defcancel_task(self, params: TaskIdParams) -> None: ...

    @abstractmethod
    defbuild_message_history(self, history: list[Message]) -> list[Any]: ...

    @abstractmethod
    defbuild_artifacts(self, result: Any) -> list[Artifact]: ...
```

#### run `async`

Run the worker.

It connects to the broker, and it makes itself available to receive commands.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/worker.py`

```
29
30
31
32
33
34
35
36
37
38
```

```
@asynccontextmanager
async defrun(self) -> AsyncIterator[None]:
"""Run the worker.

    It connects to the broker, and it makes itself available to receive commands.
    """
    async with anyio.create_task_group() as tg:
        tg.start_soon(self._loop)
        yield
        tg.cancel_scope.cancel()
```

This module contains the schema for the agent card.

### AgentCard

Bases: `TypedDict`

The card that describes an agent.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
13
14
15
16
17
18
19
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
67
```

```
@pydantic.with_config({'alias_generator': to_camel})
classAgentCard(TypedDict):
"""The card that describes an agent."""

    name: str
"""Human readable name of the agent e.g. "Recipe Agent"."""

    description: str
"""A human-readable description of the agent.

    Used to assist users and other agents in understanding what the agent can do.
    (e.g. "Agent that helps users with recipes and cooking.")
    """

    url: str
"""A URL to the address the agent is hosted at."""

    version: str
"""The version of the agent - format is up to the provider. (e.g. "1.0.0")"""

    protocol_version: str
"""The version of the A2A protocol this agent supports."""

    provider: NotRequired[AgentProvider]
"""The service provider of the agent."""

    documentation_url: NotRequired[str]
"""A URL to documentation for the agent."""

    icon_url: NotRequired[str]
"""A URL to an icon for the agent."""

    preferred_transport: NotRequired[str]
"""The transport of the preferred endpoint. If empty, defaults to JSONRPC."""

    additional_interfaces: NotRequired[list[AgentInterface]]
"""Announcement of additional supported transports."""

    capabilities: AgentCapabilities
"""The capabilities of the agent."""

    security: NotRequired[list[dict[str, list[str]]]]
"""Security requirements for contacting the agent."""

    security_schemes: NotRequired[dict[str, SecurityScheme]]
"""Security scheme definitions."""

    default_input_modes: list[str]
"""Supported mime types for input data."""

    default_output_modes: list[str]
"""Supported mime types for output data."""

    skills: list[Skill]
"""The set of skills, or distinct capabilities, that the agent can perform."""
```

#### name `instance-attribute`

Human readable name of the agent e.g. "Recipe Agent".

#### description `instance-attribute`

A human-readable description of the agent.

Used to assist users and other agents in understanding what the agent can do. (e.g. "Agent that helps users with recipes and cooking.")

#### url `instance-attribute`

A URL to the address the agent is hosted at.

#### version `instance-attribute`

The version of the agent - format is up to the provider. (e.g. "1.0.0")

#### protocol\_version `instance-attribute`

The version of the A2A protocol this agent supports.

#### provider `instance-attribute`

The service provider of the agent.

#### documentation\_url `instance-attribute`

A URL to documentation for the agent.

#### icon\_url `instance-attribute`

A URL to an icon for the agent.

#### preferred\_transport `instance-attribute`

The transport of the preferred endpoint. If empty, defaults to JSONRPC.

#### additional\_interfaces `instance-attribute`

Announcement of additional supported transports.

#### capabilities `instance-attribute`

```
capabilities: AgentCapabilities
```

The capabilities of the agent.

#### security `instance-attribute`

Security requirements for contacting the agent.

#### security\_schemes `instance-attribute`

Security scheme definitions.

#### default\_input\_modes `instance-attribute`

Supported mime types for input data.

#### default\_output\_modes `instance-attribute`

Supported mime types for output data.

#### skills `instance-attribute`

The set of skills, or distinct capabilities, that the agent can perform.

### AgentProvider

Bases: `TypedDict`

The service provider of the agent.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
classAgentProvider(TypedDict):
"""The service provider of the agent."""

    organization: str
"""The name of the agent provider's organization."""

    url: str
"""A URL for the agent provider's website or relevant documentation."""
```

#### organization `instance-attribute`

The name of the agent provider's organization.

#### url `instance-attribute`

A URL for the agent provider's website or relevant documentation.

### AgentCapabilities

Bases: `TypedDict`

The capabilities of the agent.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classAgentCapabilities(TypedDict):
"""The capabilities of the agent."""

    streaming: NotRequired[bool]
"""Whether the agent supports streaming."""

    push_notifications: NotRequired[bool]
"""Whether the agent can notify updates to client."""

    state_transition_history: NotRequired[bool]
"""Whether the agent exposes status change history for tasks."""
```

#### streaming `instance-attribute`

Whether the agent supports streaming.

#### push\_notifications `instance-attribute`

Whether the agent can notify updates to client.

#### state\_transition\_history `instance-attribute`

Whether the agent exposes status change history for tasks.

### HttpSecurityScheme

Bases: `TypedDict`

HTTP security scheme.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classHttpSecurityScheme(TypedDict):
"""HTTP security scheme."""

    type: Literal['http']
"""The type of the security scheme. Must be 'http'."""

    scheme: str
"""The name of the HTTP Authorization scheme."""

    bearer_format: NotRequired[str]
"""A hint to the client to identify how the bearer token is formatted."""

    description: NotRequired[str]
"""Description of this security scheme."""
```

#### type `instance-attribute`

The type of the security scheme. Must be 'http'.

#### scheme `instance-attribute`

The name of the HTTP Authorization scheme.

#### bearer\_format `instance-attribute`

A hint to the client to identify how the bearer token is formatted.

#### description `instance-attribute`

Description of this security scheme.

### ApiKeySecurityScheme

Bases: `TypedDict`

API Key security scheme.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classApiKeySecurityScheme(TypedDict):
"""API Key security scheme."""

    type: Literal['apiKey']
"""The type of the security scheme. Must be 'apiKey'."""

    name: str
"""The name of the header, query or cookie parameter to be used."""

    in_: Literal['query', 'header', 'cookie']
"""The location of the API key."""

    description: NotRequired[str]
"""Description of this security scheme."""
```

#### type `instance-attribute`

The type of the security scheme. Must be 'apiKey'.

#### name `instance-attribute`

The name of the header, query or cookie parameter to be used.

#### in_ `instance-attribute`

```
in_: Literal['query', 'header', 'cookie']
```

The location of the API key.

#### description `instance-attribute`

Description of this security scheme.

### OAuth2SecurityScheme

Bases: `TypedDict`

OAuth2 security scheme.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classOAuth2SecurityScheme(TypedDict):
"""OAuth2 security scheme."""

    type: Literal['oauth2']
"""The type of the security scheme. Must be 'oauth2'."""

    flows: dict[str, Any]
"""An object containing configuration information for the flow types supported."""

    description: NotRequired[str]
"""Description of this security scheme."""
```

#### type `instance-attribute`

The type of the security scheme. Must be 'oauth2'.

#### flows `instance-attribute`

An object containing configuration information for the flow types supported.

#### description `instance-attribute`

Description of this security scheme.

### OpenIdConnectSecurityScheme

Bases: `TypedDict`

OpenID Connect security scheme.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classOpenIdConnectSecurityScheme(TypedDict):
"""OpenID Connect security scheme."""

    type: Literal['openIdConnect']
"""The type of the security scheme. Must be 'openIdConnect'."""

    open_id_connect_url: str
"""OpenId Connect URL to discover OAuth2 configuration values."""

    description: NotRequired[str]
"""Description of this security scheme."""
```

#### type `instance-attribute`

The type of the security scheme. Must be 'openIdConnect'.

#### open\_id\_connect\_url `instance-attribute`

OpenId Connect URL to discover OAuth2 configuration values.

#### description `instance-attribute`

Description of this security scheme.

### SecurityScheme `module-attribute`

A security scheme for authentication.

### AgentInterface

Bases: `TypedDict`

An interface that the agent supports.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classAgentInterface(TypedDict):
"""An interface that the agent supports."""

    transport: str
"""The transport protocol (e.g., 'jsonrpc', 'websocket')."""

    url: str
"""The URL endpoint for this transport."""

    description: NotRequired[str]
"""Description of this interface."""
```

#### transport `instance-attribute`

The transport protocol (e.g., 'jsonrpc', 'websocket').

#### url `instance-attribute`

The URL endpoint for this transport.

#### description `instance-attribute`

Description of this interface.

### AgentExtension

Bases: `TypedDict`

A declaration of an extension supported by an Agent.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classAgentExtension(TypedDict):
"""A declaration of an extension supported by an Agent."""

    uri: str
"""The URI of the extension."""

    description: NotRequired[str]
"""A description of how this agent uses this extension."""

    required: NotRequired[bool]
"""Whether the client must follow specific requirements of the extension."""

    params: NotRequired[dict[str, Any]]
"""Optional configuration for the extension."""
```

#### uri `instance-attribute`

The URI of the extension.

#### description `instance-attribute`

A description of how this agent uses this extension.

#### required `instance-attribute`

Whether the client must follow specific requirements of the extension.

#### params `instance-attribute`

Optional configuration for the extension.

### Skill

Bases: `TypedDict`

Skills are a unit of capability that an agent can perform.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
227
228
229
```

```
@pydantic.with_config({'alias_generator': to_camel})
classSkill(TypedDict):
"""Skills are a unit of capability that an agent can perform."""

    id: str
"""A unique identifier for the skill."""

    name: str
"""Human readable name of the skill."""

    description: str
"""A human-readable description of the skill.

    It will be used by the client or a human as a hint to understand the skill.
    """

    tags: list[str]
"""Set of tag-words describing classes of capabilities for this specific skill.

    Examples: "cooking", "customer support", "billing".
    """

    examples: NotRequired[list[str]]
"""The set of example scenarios that the skill can perform.

    Will be used by the client as a hint to understand how the skill can be used. (e.g. "I need a recipe for bread")
    """

    input_modes: list[str]
"""Supported mime types for input data."""

    output_modes: list[str]
"""Supported mime types for output data."""
```

#### id `instance-attribute`

A unique identifier for the skill.

#### name `instance-attribute`

Human readable name of the skill.

#### description `instance-attribute`

A human-readable description of the skill.

It will be used by the client or a human as a hint to understand the skill.

#### tags `instance-attribute`

Set of tag-words describing classes of capabilities for this specific skill.

Examples: "cooking", "customer support", "billing".

#### examples `instance-attribute`

The set of example scenarios that the skill can perform.

Will be used by the client as a hint to understand how the skill can be used. (e.g. "I need a recipe for bread")

#### input\_modes `instance-attribute`

Supported mime types for input data.

#### output\_modes `instance-attribute`

Supported mime types for output data.

### Artifact

Bases: `TypedDict`

Agents generate Artifacts as an end result of a Task.

Artifacts are immutable, can be named, and can have multiple parts. A streaming response can append parts to existing Artifacts.

A single Task can generate many Artifacts. For example, "create a webpage" could create separate HTML and image Artifacts.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classArtifact(TypedDict):
"""Agents generate Artifacts as an end result of a Task.

    Artifacts are immutable, can be named, and can have multiple parts. A streaming response can append parts to
    existing Artifacts.

    A single Task can generate many Artifacts. For example, "create a webpage" could create separate HTML and image
    Artifacts.
    """

    artifact_id: str
"""Unique identifier for the artifact."""

    name: NotRequired[str]
"""The name of the artifact."""

    description: NotRequired[str]
"""A description of the artifact."""

    parts: list[Part]
"""The parts that make up the artifact."""

    metadata: NotRequired[dict[str, Any]]
"""Metadata about the artifact."""

    extensions: NotRequired[list[str]]
"""Array of extensions."""

    append: NotRequired[bool]
"""Whether to append this artifact to an existing one."""

    last_chunk: NotRequired[bool]
"""Whether this is the last chunk of the artifact."""
```

#### artifact\_id `instance-attribute`

Unique identifier for the artifact.

#### name `instance-attribute`

The name of the artifact.

#### description `instance-attribute`

A description of the artifact.

#### parts `instance-attribute`

The parts that make up the artifact.

#### metadata `instance-attribute`

Metadata about the artifact.

#### extensions `instance-attribute`

Array of extensions.

#### append `instance-attribute`

Whether to append this artifact to an existing one.

#### last\_chunk `instance-attribute`

Whether this is the last chunk of the artifact.

### PushNotificationConfig

Bases: `TypedDict`

Configuration for push notifications.

A2A supports a secure notification mechanism whereby an agent can notify a client of an update outside a connected session via a PushNotificationService. Within and across enterprises, it is critical that the agent verifies the identity of the notification service, authenticates itself with the service, and presents an identifier that ties the notification to the executing Task.

The target server of the PushNotificationService should be considered a separate service, and is not guaranteed (or even expected) to be the client directly. This PushNotificationService is responsible for authenticating and authorizing the agent and for proxying the verified notification to the appropriate endpoint (which could be anything from a pub/sub queue, to an email inbox or other service, etc.).

For contrived scenarios with isolated client-agent pairs (e.g. local service mesh in a contained VPC, etc.) or isolated environments without enterprise security concerns, the client may choose to simply open a port and act as its own PushNotificationService. Any enterprise implementation will likely have a centralized service that authenticates the remote agents with trusted notification credentials and can handle online/offline scenarios. (This should be thought of similarly to a mobile Push Notification Service).

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classPushNotificationConfig(TypedDict):
"""Configuration for push notifications.

    A2A supports a secure notification mechanism whereby an agent can notify a client of an update
    outside a connected session via a PushNotificationService. Within and across enterprises,
    it is critical that the agent verifies the identity of the notification service, authenticates
    itself with the service, and presents an identifier that ties the notification to the executing
    Task.

    The target server of the PushNotificationService should be considered a separate service, and
    is not guaranteed (or even expected) to be the client directly. This PushNotificationService is
    responsible for authenticating and authorizing the agent and for proxying the verified notification
    to the appropriate endpoint (which could be anything from a pub/sub queue, to an email inbox or
    other service, etc.).

    For contrived scenarios with isolated client-agent pairs (e.g. local service mesh in a contained
    VPC, etc.) or isolated environments without enterprise security concerns, the client may choose to
    simply open a port and act as its own PushNotificationService. Any enterprise implementation will
    likely have a centralized service that authenticates the remote agents with trusted notification
    credentials and can handle online/offline scenarios. (This should be thought of similarly to a
    mobile Push Notification Service).
    """

    id: NotRequired[str]
"""Server-assigned identifier."""

    url: str
"""The URL to send push notifications to."""

    token: NotRequired[str]
"""Token unique to this task/session."""

    authentication: NotRequired[SecurityScheme]
"""Authentication details for push notifications."""
```

#### id `instance-attribute`

Server-assigned identifier.

#### url `instance-attribute`

The URL to send push notifications to.

#### token `instance-attribute`

Token unique to this task/session.

#### authentication `instance-attribute`

Authentication details for push notifications.

### TaskPushNotificationConfig

Bases: `TypedDict`

Configuration for task push notifications.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
305
306
307
308
309
310
311
312
313
```

```
@pydantic.with_config({'alias_generator': to_camel})
classTaskPushNotificationConfig(TypedDict):
"""Configuration for task push notifications."""

    id: str
"""The task id."""

    push_notification_config: PushNotificationConfig
"""The push notification configuration."""
```

#### id `instance-attribute`

The task id.

#### push\_notification\_config `instance-attribute`

```
push_notification_config: PushNotificationConfig
```

The push notification configuration.

### Message

Bases: `TypedDict`

A Message contains any content that is not an Artifact.

This can include things like agent thoughts, user context, instructions, errors, status, or metadata.

All content from a client comes in the form of a Message. Agents send Messages to communicate status or to provide instructions (whereas generated results are sent as Artifacts).

A Message can have multiple parts to denote different pieces of content. For example, a user request could include a textual description from a user and then multiple files used as context from the client.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classMessage(TypedDict):
"""A Message contains any content that is not an Artifact.

    This can include things like agent thoughts, user context, instructions, errors, status, or metadata.

    All content from a client comes in the form of a Message. Agents send Messages to communicate status or to provide
    instructions (whereas generated results are sent as Artifacts).

    A Message can have multiple parts to denote different pieces of content. For example, a user request could include
    a textual description from a user and then multiple files used as context from the client.
    """

    role: Literal['user', 'agent']
"""The role of the message."""

    parts: list[Part]
"""The parts of the message."""

    kind: Literal['message']
"""Event type."""

    metadata: NotRequired[dict[str, Any]]
"""Metadata about the message."""

    # Additional fields
    message_id: str
"""Identifier created by the message creator."""

    context_id: NotRequired[str]
"""The context the message is associated with."""

    task_id: NotRequired[str]
"""Identifier of task the message is related to."""

    reference_task_ids: NotRequired[list[str]]
"""Array of task IDs this message references."""

    extensions: NotRequired[list[str]]
"""Array of extensions."""
```

#### role `instance-attribute`

The role of the message.

#### parts `instance-attribute`

The parts of the message.

#### kind `instance-attribute`

Event type.

#### metadata `instance-attribute`

Metadata about the message.

#### message\_id `instance-attribute`

Identifier created by the message creator.

#### context\_id `instance-attribute`

The context the message is associated with.

#### task\_id `instance-attribute`

Identifier of task the message is related to.

#### reference\_task\_ids `instance-attribute`

Array of task IDs this message references.

#### extensions `instance-attribute`

Array of extensions.

### TextPart

Bases: `_BasePart`

A part that contains text.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
364
365
366
367
368
369
370
371
372
```

```
@pydantic.with_config({'alias_generator': to_camel})
classTextPart(_BasePart):
"""A part that contains text."""

    kind: Literal['text']
"""The kind of the part."""

    text: str
"""The text of the part."""
```

#### kind `instance-attribute`

The kind of the part.

#### text `instance-attribute`

The text of the part.

### FileWithBytes

Bases: `TypedDict`

File with base64 encoded data.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
375
376
377
378
379
380
381
382
383
```

```
@pydantic.with_config({'alias_generator': to_camel})
classFileWithBytes(TypedDict):
"""File with base64 encoded data."""

    bytes: str
"""The base64 encoded content of the file."""

    mime_type: NotRequired[str]
"""Optional mime type for the file."""
```

#### bytes `instance-attribute`

The base64 encoded content of the file.

#### mime\_type `instance-attribute`

Optional mime type for the file.

### FileWithUri

Bases: `TypedDict`

File with URI reference.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
386
387
388
389
390
391
392
393
394
```

```
@pydantic.with_config({'alias_generator': to_camel})
classFileWithUri(TypedDict):
"""File with URI reference."""

    uri: str
"""The URI of the file."""

    mime_type: NotRequired[str]
"""The mime type of the file."""
```

#### uri `instance-attribute`

The URI of the file.

#### mime\_type `instance-attribute`

The mime type of the file.

### FilePart

Bases: `_BasePart`

A part that contains a file.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
397
398
399
400
401
402
403
404
405
```

```
@pydantic.with_config({'alias_generator': to_camel})
classFilePart(_BasePart):
"""A part that contains a file."""

    kind: Literal['file']
"""The kind of the part."""

    file: FileWithBytes | FileWithUri
"""The file content - either bytes or URI."""
```

#### kind `instance-attribute`

The kind of the part.

#### file `instance-attribute`

The file content - either bytes or URI.

### DataPart

Bases: `_BasePart`

A part that contains structured data.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
408
409
410
411
412
413
414
415
416
```

```
@pydantic.with_config({'alias_generator': to_camel})
classDataPart(_BasePart):
"""A part that contains structured data."""

    kind: Literal['data']
"""The kind of the part."""

    data: dict[str, Any]
"""The data of the part."""
```

#### kind `instance-attribute`

The kind of the part.

#### data `instance-attribute`

The data of the part.

### Part `module-attribute`

A fully formed piece of content exchanged between a client and a remote agent as part of a Message or an Artifact.

Each Part has its own content type and metadata.

### TaskState `module-attribute`

```
TaskState: TypeAlias = Literal[
    "submitted",
    "working",
    "input-required",
    "completed",
    "canceled",
    "failed",
    "rejected",
    "auth-required",
    "unknown",
]
```

The possible states of a task.

### TaskStatus

Bases: `TypedDict`

Status and accompanying message for a task.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
```

```
@pydantic.with_config({'alias_generator': to_camel})
classTaskStatus(TypedDict):
"""Status and accompanying message for a task."""

    state: TaskState
"""The current state of the task."""

    message: NotRequired[Message]
"""Additional status updates for client."""

    timestamp: NotRequired[str]
"""ISO datetime value of when the status was updated."""
```

#### state `instance-attribute`

The current state of the task.

#### message `instance-attribute`

Additional status updates for client.

#### timestamp `instance-attribute`

ISO datetime value of when the status was updated.

### Task

Bases: `TypedDict`

A Task is a stateful entity that allows Clients and Remote Agents to achieve a specific outcome.

Clients and Remote Agents exchange Messages within a Task. Remote Agents generate results as Artifacts. A Task is always created by a Client and the status is always determined by the Remote Agent.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
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
465
466
467
468
469
470
471
472
```

```
@pydantic.with_config({'alias_generator': to_camel})
classTask(TypedDict):
"""A Task is a stateful entity that allows Clients and Remote Agents to achieve a specific outcome.

    Clients and Remote Agents exchange Messages within a Task. Remote Agents generate results as Artifacts.
    A Task is always created by a Client and the status is always determined by the Remote Agent.
    """

    id: str
"""Unique identifier for the task."""

    context_id: str
"""The context the task is associated with."""

    kind: Literal['task']
"""Event type."""

    status: TaskStatus
"""Current status of the task."""

    history: NotRequired[list[Message]]
"""Optional history of messages."""

    artifacts: NotRequired[list[Artifact]]
"""Collection of artifacts created by the agent."""

    metadata: NotRequired[dict[str, Any]]
"""Extension metadata."""
```

#### id `instance-attribute`

Unique identifier for the task.

#### context\_id `instance-attribute`

The context the task is associated with.

#### kind `instance-attribute`

Event type.

#### status `instance-attribute`

Current status of the task.

#### history `instance-attribute`

Optional history of messages.

#### artifacts `instance-attribute`

Collection of artifacts created by the agent.

#### metadata `instance-attribute`

Extension metadata.

### TaskStatusUpdateEvent

Bases: `TypedDict`

Sent by server during message/stream requests.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
```

```
@pydantic.with_config({'alias_generator': to_camel})
classTaskStatusUpdateEvent(TypedDict):
"""Sent by server during message/stream requests."""

    task_id: str
"""The id of the task."""

    context_id: str
"""The context the task is associated with."""

    kind: Literal['status-update']
"""Event type."""

    status: TaskStatus
"""The status of the task."""

    final: bool
"""Indicates the end of the event stream."""

    metadata: NotRequired[dict[str, Any]]
"""Extension metadata."""
```

#### task\_id `instance-attribute`

The id of the task.

#### context\_id `instance-attribute`

The context the task is associated with.

#### kind `instance-attribute`

Event type.

#### status `instance-attribute`

The status of the task.

#### final `instance-attribute`

Indicates the end of the event stream.

#### metadata `instance-attribute`

Extension metadata.

### TaskArtifactUpdateEvent

Bases: `TypedDict`

Sent by server during message/stream requests.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
```

```
@pydantic.with_config({'alias_generator': to_camel})
classTaskArtifactUpdateEvent(TypedDict):
"""Sent by server during message/stream requests."""

    task_id: str
"""The id of the task."""

    context_id: str
"""The context the task is associated with."""

    kind: Literal['artifact-update']
"""Event type identification."""

    artifact: Artifact
"""The artifact that was updated."""

    append: NotRequired[bool]
"""Whether to append to existing artifact (true) or replace (false)."""

    last_chunk: NotRequired[bool]
"""Indicates this is the final chunk of the artifact."""

    metadata: NotRequired[dict[str, Any]]
"""Extension metadata."""
```

#### task\_id `instance-attribute`

The id of the task.

#### context\_id `instance-attribute`

The context the task is associated with.

#### kind `instance-attribute`

Event type identification.

#### artifact `instance-attribute`

The artifact that was updated.

#### append `instance-attribute`

Whether to append to existing artifact (true) or replace (false).

#### last\_chunk `instance-attribute`

Indicates this is the final chunk of the artifact.

#### metadata `instance-attribute`

Extension metadata.

### TaskIdParams

Bases: `TypedDict`

Parameters for a task id.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
524
525
526
527
528
529
530
531
532
```

```
@pydantic.with_config({'alias_generator': to_camel})
classTaskIdParams(TypedDict):
"""Parameters for a task id."""

    id: str
"""The unique identifier for the task."""

    metadata: NotRequired[dict[str, Any]]
"""Optional metadata associated with the request."""
```

#### id `instance-attribute`

The unique identifier for the task.

#### metadata `instance-attribute`

Optional metadata associated with the request.

### TaskQueryParams

Bases: `TaskIdParams`

Query parameters for a task.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
@pydantic.with_config({'alias_generator': to_camel})
classTaskQueryParams(TaskIdParams):
"""Query parameters for a task."""

    history_length: NotRequired[int]
"""Number of recent messages to be retrieved."""
```

#### history\_length `instance-attribute`

Number of recent messages to be retrieved.

### MessageSendConfiguration

Bases: `TypedDict`

Configuration for the send message request.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
```

```
@pydantic.with_config({'alias_generator': to_camel})
classMessageSendConfiguration(TypedDict):
"""Configuration for the send message request."""

    accepted_output_modes: list[str]
"""Accepted output modalities by the client."""

    blocking: NotRequired[bool]
"""If the server should treat the client as a blocking request."""

    history_length: NotRequired[int]
"""Number of recent messages to be retrieved."""

    push_notification_config: NotRequired[PushNotificationConfig]
"""Where the server should send notifications when disconnected."""
```

#### accepted\_output\_modes `instance-attribute`

Accepted output modalities by the client.

#### blocking `instance-attribute`

If the server should treat the client as a blocking request.

#### history\_length `instance-attribute`

Number of recent messages to be retrieved.

#### push\_notification\_config `instance-attribute`

Where the server should send notifications when disconnected.

### MessageSendParams

Bases: `TypedDict`

Parameters for message/send method.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
560
561
562
563
564
565
566
567
568
569
570
571
```

```
@pydantic.with_config({'alias_generator': to_camel})
classMessageSendParams(TypedDict):
"""Parameters for message/send method."""

    configuration: NotRequired[MessageSendConfiguration]
"""Send message configuration."""

    message: Message
"""The message being sent to the server."""

    metadata: NotRequired[dict[str, Any]]
"""Extension metadata."""
```

#### configuration `instance-attribute`

Send message configuration.

#### message `instance-attribute`

The message being sent to the server.

#### metadata `instance-attribute`

Extension metadata.

### TaskSendParams

Bases: `TypedDict`

Internal parameters for task execution within the framework.

Note: This is not part of the A2A protocol - it's used internally for broker/worker communication.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
```

```
@pydantic.with_config({'alias_generator': to_camel})
classTaskSendParams(TypedDict):
"""Internal parameters for task execution within the framework.

    Note: This is not part of the A2A protocol - it's used internally
    for broker/worker communication.
    """

    id: str
"""The id of the task."""

    context_id: str
"""The context id for the task."""

    message: Message
"""The message to process."""

    history_length: NotRequired[int]
"""Number of recent messages to be retrieved."""

    metadata: NotRequired[dict[str, Any]]
"""Extension metadata."""
```

#### id `instance-attribute`

The id of the task.

#### context\_id `instance-attribute`

The context id for the task.

#### message `instance-attribute`

The message to process.

#### history\_length `instance-attribute`

Number of recent messages to be retrieved.

#### metadata `instance-attribute`

Extension metadata.

### ListTaskPushNotificationConfigParams

Bases: `TypedDict`

Parameters for getting list of pushNotificationConfigurations associated with a Task.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
598
599
600
601
602
603
604
605
606
```

```
@pydantic.with_config({'alias_generator': to_camel})
classListTaskPushNotificationConfigParams(TypedDict):
"""Parameters for getting list of pushNotificationConfigurations associated with a Task."""

    id: str
"""Task id."""

    metadata: NotRequired[dict[str, Any]]
"""Extension metadata."""
```

#### id `instance-attribute`

Task id.

#### metadata `instance-attribute`

Extension metadata.

### DeleteTaskPushNotificationConfigParams

Bases: `TypedDict`

Parameters for removing pushNotificationConfiguration associated with a Task.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
609
610
611
612
613
614
615
616
617
618
619
620
```

```
@pydantic.with_config({'alias_generator': to_camel})
classDeleteTaskPushNotificationConfigParams(TypedDict):
"""Parameters for removing pushNotificationConfiguration associated with a Task."""

    id: str
"""Task id."""

    push_notification_config_id: str
"""The push notification config id to delete."""

    metadata: NotRequired[dict[str, Any]]
"""Extension metadata."""
```

#### id `instance-attribute`

Task id.

#### push\_notification\_config\_id `instance-attribute`

```
push_notification_config_id: str
```

The push notification config id to delete.

#### metadata `instance-attribute`

Extension metadata.

### JSONRPCMessage

Bases: `TypedDict`

A JSON RPC message.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
623
624
625
626
627
628
629
630
```

```
classJSONRPCMessage(TypedDict):
"""A JSON RPC message."""

    jsonrpc: Literal['2.0']
"""The JSON RPC version."""

    id: int | str | None
"""The request id."""
```

#### jsonrpc `instance-attribute`

The JSON RPC version.

#### id `instance-attribute`

The request id.

### JSONRPCRequest

Bases: `JSONRPCMessage`, `Generic[Method, Params]`

A JSON RPC request.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
637
638
639
640
641
642
643
644
```

```
classJSONRPCRequest(JSONRPCMessage, Generic[Method, Params]):
"""A JSON RPC request."""

    method: Method
"""The method to call."""

    params: Params
"""The parameters to pass to the method."""
```

#### method `instance-attribute`

The method to call.

#### params `instance-attribute`

The parameters to pass to the method.

### JSONRPCError

Bases: `TypedDict`, `Generic[CodeT, MessageT]`

A JSON RPC error.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
655
656
657
658
659
660
661
662
663
664
665
```

```
classJSONRPCError(TypedDict, Generic[CodeT, MessageT]):
"""A JSON RPC error."""

    code: CodeT
"""A number that indicates the error type that occurred."""

    message: MessageT
"""A string providing a short description of the error."""

    data: NotRequired[Any]
"""A primitive or structured value containing additional information about the error."""
```

#### code `instance-attribute`

A number that indicates the error type that occurred.

#### message `instance-attribute`

A string providing a short description of the error.

#### data `instance-attribute`

A primitive or structured value containing additional information about the error.

### JSONRPCResponse

Bases: `JSONRPCMessage`, `Generic[ResultT, ErrorT]`

A JSON RPC response.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`

```
classJSONRPCResponse(JSONRPCMessage, Generic[ResultT, ErrorT]):
"""A JSON RPC response."""

    result: NotRequired[ResultT]
    error: NotRequired[ErrorT]
```

### JSONParseError `module-attribute`

A JSON RPC error for a parse error.

### InvalidRequestError `module-attribute`

```
InvalidRequestError = JSONRPCError[
    Literal[-32600],
    Literal["Request payload validation error"],
]
```

A JSON RPC error for an invalid request.

### MethodNotFoundError `module-attribute`

A JSON RPC error for a method not found.

### InvalidParamsError `module-attribute`

A JSON RPC error for invalid parameters.

### InternalError `module-attribute`

A JSON RPC error for an internal error.

### TaskNotFoundError `module-attribute`

A JSON RPC error for a task not found.

### TaskNotCancelableError `module-attribute`

```
TaskNotCancelableError = JSONRPCError[
    Literal[-32002], Literal["Task not cancelable"]
]
```

A JSON RPC error for a task not cancelable.

### PushNotificationNotSupportedError `module-attribute`

```
PushNotificationNotSupportedError = JSONRPCError[
    Literal[-32003],
    Literal["Push notification not supported"],
]
```

A JSON RPC error for a push notification not supported.

### UnsupportedOperationError `module-attribute`

```
UnsupportedOperationError = JSONRPCError[
    Literal[-32004],
    Literal["This operation is not supported"],
]
```

A JSON RPC error for an unsupported operation.

### ContentTypeNotSupportedError `module-attribute`

```
ContentTypeNotSupportedError = JSONRPCError[
    Literal[-32005], Literal["Incompatible content types"]
]
```

A JSON RPC error for incompatible content types.

### InvalidAgentResponseError `module-attribute`

```
InvalidAgentResponseError = JSONRPCError[
    Literal[-32006], Literal["Invalid agent response"]
]
```

A JSON RPC error for invalid agent response.

### SendMessageRequest `module-attribute`

A JSON RPC request to send a message.

### SendMessageResponse `module-attribute`

A JSON RPC response to send a message.

### StreamMessageRequest `module-attribute`

```
StreamMessageRequest = JSONRPCRequest[
    Literal["message/stream"], MessageSendParams
]
```

A JSON RPC request to stream a message.

### StreamMessageResponse `module-attribute`

A JSON RPC response to a StreamMessageRequest.

### GetTaskRequest `module-attribute`

A JSON RPC request to get a task.

### GetTaskResponse `module-attribute`

```
GetTaskResponse = JSONRPCResponse[Task, TaskNotFoundError]
```

A JSON RPC response to get a task.

### CancelTaskRequest `module-attribute`

```
CancelTaskRequest = JSONRPCRequest[
    Literal["tasks/cancel"], TaskIdParams
]
```

A JSON RPC request to cancel a task.

### CancelTaskResponse `module-attribute`

A JSON RPC response to cancel a task.

### SetTaskPushNotificationRequest `module-attribute`

```
SetTaskPushNotificationRequest = JSONRPCRequest[
    Literal["tasks/pushNotification/set"],
    TaskPushNotificationConfig,
]
```

A JSON RPC request to set a task push notification.

### SetTaskPushNotificationResponse `module-attribute`

```
SetTaskPushNotificationResponse = JSONRPCResponse[
    TaskPushNotificationConfig,
    PushNotificationNotSupportedError,
]
```

A JSON RPC response to set a task push notification.

### GetTaskPushNotificationRequest `module-attribute`

```
GetTaskPushNotificationRequest = JSONRPCRequest[
    Literal["tasks/pushNotification/get"], TaskIdParams
]
```

A JSON RPC request to get a task push notification.

### GetTaskPushNotificationResponse `module-attribute`

```
GetTaskPushNotificationResponse = JSONRPCResponse[
    TaskPushNotificationConfig,
    PushNotificationNotSupportedError,
]
```

A JSON RPC response to get a task push notification.

### ResubscribeTaskRequest `module-attribute`

```
ResubscribeTaskRequest = JSONRPCRequest[
    Literal["tasks/resubscribe"], TaskIdParams
]
```

A JSON RPC request to resubscribe to a task.

### ListTaskPushNotificationConfigRequest `module-attribute`

```
ListTaskPushNotificationConfigRequest = JSONRPCRequest[
    Literal["tasks/pushNotificationConfig/list"],
    ListTaskPushNotificationConfigParams,
]
```

A JSON RPC request to list task push notification configs.

### DeleteTaskPushNotificationConfigRequest `module-attribute`

```
DeleteTaskPushNotificationConfigRequest = JSONRPCRequest[
    Literal["tasks/pushNotificationConfig/delete"],
    DeleteTaskPushNotificationConfigParams,
]
```

A JSON RPC request to delete a task push notification config.

### A2ARequest `module-attribute`

```
A2ARequest = Annotated[
    Union[
        SendMessageRequest,
        StreamMessageRequest,
        GetTaskRequest,
        CancelTaskRequest,
        SetTaskPushNotificationRequest,
        GetTaskPushNotificationRequest,
        ResubscribeTaskRequest,
        ListTaskPushNotificationConfigRequest,
        DeleteTaskPushNotificationConfigRequest,
    ],
    Discriminator("method"),
]
```

A JSON RPC request to the A2A server.

### A2AResponse `module-attribute`

A JSON RPC response from the A2A server.

### A2AClient

A client for the A2A protocol.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/client.py`

```
31
32
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
classA2AClient:
"""A client for the A2A protocol."""

    def__init__(self, base_url: str = 'http://localhost:8000', http_client: httpx.AsyncClient | None = None) -> None:
        if http_client is None:
            self.http_client = httpx.AsyncClient(base_url=base_url)
        else:
            self.http_client = http_client
            self.http_client.base_url = base_url

    async defsend_message(
        self,
        message: Message,
        *,
        metadata: dict[str, Any] | None = None,
        configuration: MessageSendConfiguration | None = None,
    ) -> SendMessageResponse:
"""Send a message using the A2A protocol.

        Returns a JSON-RPC response containing either a result (Task) or an error.
        """
        params = MessageSendParams(message=message)
        if metadata is not None:
            params['metadata'] = metadata
        if configuration is not None:
            params['configuration'] = configuration

        request_id = str(uuid.uuid4())
        payload = SendMessageRequest(jsonrpc='2.0', id=request_id, method='message/send', params=params)
        content = send_message_request_ta.dump_json(payload, by_alias=True)
        response = await self.http_client.post('/', content=content, headers={'Content-Type': 'application/json'})
        self._raise_for_status(response)

        return send_message_response_ta.validate_json(response.content)

    async defget_task(self, task_id: str) -> GetTaskResponse:
        payload = GetTaskRequest(jsonrpc='2.0', id=None, method='tasks/get', params={'id': task_id})
        content = a2a_request_ta.dump_json(payload, by_alias=True)
        response = await self.http_client.post('/', content=content, headers={'Content-Type': 'application/json'})
        self._raise_for_status(response)
        return get_task_response_ta.validate_json(response.content)

    def_raise_for_status(self, response: httpx.Response) -> None:
        if response.status_code >= 400:
            raise UnexpectedResponseError(response.status_code, response.text)
```

#### send\_message `async`

```
send_message(
    message: Message,
    *,
    metadata: dict[str, Any] | None = None,
    configuration: MessageSendConfiguration | None = None
) -> SendMessageResponse
```

Send a message using the A2A protocol.

Returns a JSON-RPC response containing either a result (Task) or an error.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/client.py`

```
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
```

```
async defsend_message(
    self,
    message: Message,
    *,
    metadata: dict[str, Any] | None = None,
    configuration: MessageSendConfiguration | None = None,
) -> SendMessageResponse:
"""Send a message using the A2A protocol.

    Returns a JSON-RPC response containing either a result (Task) or an error.
    """
    params = MessageSendParams(message=message)
    if metadata is not None:
        params['metadata'] = metadata
    if configuration is not None:
        params['configuration'] = configuration

    request_id = str(uuid.uuid4())
    payload = SendMessageRequest(jsonrpc='2.0', id=request_id, method='message/send', params=params)
    content = send_message_request_ta.dump_json(payload, by_alias=True)
    response = await self.http_client.post('/', content=content, headers={'Content-Type': 'application/json'})
    self._raise_for_status(response)

    return send_message_response_ta.validate_json(response.content)
```

### UnexpectedResponseError

Bases: `Exception`

An error raised when an unexpected response is received from the server.

Source code in `.venv/lib/python3.12/site-packages/fasta2a/client.py`

```
classUnexpectedResponseError(Exception):
"""An error raised when an unexpected response is received from the server."""

    def__init__(self, status_code: int, content: str) -> None:
        self.status_code = status_code
        self.content = content
```