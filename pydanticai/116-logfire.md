---
title: Debugging & Monitoring with Pydantic Logfire - Pydantic AI
url: https://ai.pydantic.dev/logfire/
source: sitemap
fetched_at: 2026-01-22T22:23:33.514051045-03:00
rendered_js: false
word_count: 1691
summary: This document explains how to integrate and use Pydantic Logfire with Pydantic AI to provide observability, tracing, and performance monitoring for LLM applications.
tags:
    - pydantic-ai
    - logfire
    - observability
    - opentelemetry
    - tracing
    - python
    - monitoring
category: guide
---

Applications that use LLMs have some challenges that are well known and understood: LLMs are **slow**, **unreliable** and **expensive**.

These applications also have some challenges that most developers have encountered much less often: LLMs are **fickle** and **non-deterministic**. Subtle changes in a prompt can completely change a model's performance, and there's no `EXPLAIN` query you can run to understand why.

Warning

From a software engineers point of view, you can think of LLMs as the worst database you've ever heard of, but worse.

If LLMs weren't so bloody useful, we'd never touch them.

To build successful applications with LLMs, we need new tools to understand both model performance, and the behavior of applications that rely on them.

LLM Observability tools that just let you understand how your model is performing are useless: making API calls to an LLM is easy, it's building that into an application that's hard.

## Pydantic Logfire

[Pydantic Logfire](https://pydantic.dev/logfire) is an observability platform developed by the team who created and maintain Pydantic Validation and Pydantic AI. Logfire aims to let you understand your entire application: Gen AI, classic predictive AI, HTTP traffic, database queries and everything else a modern application needs, all using OpenTelemetry.

Pydantic Logfire is a commercial product

Logfire is a commercially supported, hosted platform with an extremely generous and perpetual [free tier](https://pydantic.dev/pricing/). You can sign up and start using Logfire in a couple of minutes. Logfire can also be self-hosted on the enterprise tier.

Pydantic AI has built-in (but optional) support for Logfire. That means if the `logfire` package is installed and configured and agent instrumentation is enabled then detailed information about agent runs is sent to Logfire. Otherwise there's virtually no overhead and nothing is sent.

Here's an example showing details of running the [Weather Agent](https://ai.pydantic.dev/examples/weather-agent/) in Logfire:

[![Weather Agent Logfire](https://ai.pydantic.dev/img/logfire-weather-agent.png)](https://ai.pydantic.dev/img/logfire-weather-agent.png)

A trace is generated for the agent run, and spans are emitted for each model request and tool call.

## Using Logfire

To use Logfire, you'll need a Logfire [account](https://logfire.pydantic.dev). The Logfire Python SDK is included with `pydantic-ai`:

Or if you're using the slim package, you can install it with the `logfire` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[logfire]"
```

```
uvadd"pydantic-ai-slim[logfire]"
```

Then authenticate your local environment with Logfire:

And configure a project to send data to:

pipuv

```
uvrunlogfireprojectsnew
```

(Or use an existing project with `logfire projects use`)

This will write to a `.logfire` directory in the current working directory, which the Logfire SDK will use for configuration at run time.

With that, you can start using Logfire to instrument Pydantic AI code:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) instrument\_pydantic\_ai.py

```
importlogfire

frompydantic_aiimport Agent

logfire.configure()  # (1)!
logfire.instrument_pydantic_ai()  # (2)!

agent = Agent('gateway/openai:gpt-5', instructions='Be concise, reply with one sentence.')
result = agent.run_sync('Where does "hello world" come from?')  # (3)!
print(result.output)
"""
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
"""
```

1. [`logfire.configure()`](https://logfire.pydantic.dev/docs/reference/api/logfire/#logfire.configure) configures the SDK, by default it will find the write token from the `.logfire` directory, but you can also pass a token directly.
2. [`logfire.instrument_pydantic_ai()`](https://logfire.pydantic.dev/docs/reference/api/logfire/#logfire.Logfire.instrument_pydantic_ai) enables instrumentation of Pydantic AI.
3. Since we've enabled instrumentation, a trace will be generated for each run, with spans emitted for models calls and tool function execution

instrument\_pydantic\_ai.py

```
importlogfire

frompydantic_aiimport Agent

logfire.configure()  # (1)!
logfire.instrument_pydantic_ai()  # (2)!

agent = Agent('openai:gpt-5', instructions='Be concise, reply with one sentence.')
result = agent.run_sync('Where does "hello world" come from?')  # (3)!
print(result.output)
"""
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
"""
```

1. [`logfire.configure()`](https://logfire.pydantic.dev/docs/reference/api/logfire/#logfire.configure) configures the SDK, by default it will find the write token from the `.logfire` directory, but you can also pass a token directly.
2. [`logfire.instrument_pydantic_ai()`](https://logfire.pydantic.dev/docs/reference/api/logfire/#logfire.Logfire.instrument_pydantic_ai) enables instrumentation of Pydantic AI.
3. Since we've enabled instrumentation, a trace will be generated for each run, with spans emitted for models calls and tool function execution

*(This example is complete, it can be run "as is")*

Which will display in Logfire thus:

[![Logfire Simple Agent Run](https://ai.pydantic.dev/img/logfire-simple-agent.png)](https://ai.pydantic.dev/img/logfire-simple-agent.png)

The [Logfire documentation](https://logfire.pydantic.dev/docs/) has more details on how to use Logfire, including how to instrument other libraries like [HTTPX](https://logfire.pydantic.dev/docs/integrations/http-clients/httpx/) and [FastAPI](https://logfire.pydantic.dev/docs/integrations/web-frameworks/fastapi/).

Since Logfire is built on [OpenTelemetry](https://opentelemetry.io/), you can use the Logfire Python SDK to send data to any OpenTelemetry collector, see [below](#using-opentelemetry).

### Debugging

To demonstrate how Logfire can let you visualise the flow of a Pydantic AI run, here's the view you get from Logfire while running the [chat app examples](https://ai.pydantic.dev/examples/chat-app/):

### Monitoring Performance

We can also query data with SQL in Logfire to monitor the performance of an application. Here's a real world example of using Logfire to monitor Pydantic AI runs inside Logfire itself:

[![Logfire monitoring Pydantic AI](https://ai.pydantic.dev/img/logfire-monitoring-pydanticai.png)](https://ai.pydantic.dev/img/logfire-monitoring-pydanticai.png)

### Monitoring HTTP Requests

As per Hamel Husain's influential 2024 blog post ["Fuck You, Show Me The Prompt."](https://hamel.dev/blog/posts/prompt/) (bear with the capitalization, the point is valid), it's often useful to be able to view the raw HTTP requests and responses made to model providers.

To observe raw HTTP requests made to model providers, you can use Logfire's [HTTPX instrumentation](https://logfire.pydantic.dev/docs/integrations/http-clients/httpx/) since all provider SDKs (except for [Bedrock](https://ai.pydantic.dev/models/bedrock/)) use the [HTTPX](https://www.python-httpx.org/) library internally:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) with\_logfire\_instrument\_httpx.py

```
importlogfire

frompydantic_aiimport Agent

logfire.configure()
logfire.instrument_pydantic_ai()
logfire.instrument_httpx(capture_all=True)  # (1)!

agent = Agent('gateway/openai:gpt-5')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
```

1. See the [`logfire.instrument_httpx` docs](https://logfire.pydantic.dev/docs/reference/api/logfire/#logfire.Logfire.instrument_httpx) more details, `capture_all=True` means both headers and body are captured for both the request and response.

with\_logfire\_instrument\_httpx.py

```
importlogfire

frompydantic_aiimport Agent

logfire.configure()
logfire.instrument_pydantic_ai()
logfire.instrument_httpx(capture_all=True)  # (1)!

agent = Agent('openai:gpt-5')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
```

1. See the [`logfire.instrument_httpx` docs](https://logfire.pydantic.dev/docs/reference/api/logfire/#logfire.Logfire.instrument_httpx) more details, `capture_all=True` means both headers and body are captured for both the request and response.

[![Logfire with HTTPX instrumentation](https://ai.pydantic.dev/img/logfire-with-httpx.png)](https://ai.pydantic.dev/img/logfire-with-httpx.png)

## Using OpenTelemetry

Pydantic AI's instrumentation uses [OpenTelemetry](https://opentelemetry.io/) (OTel), which Logfire is based on.

This means you can debug and monitor Pydantic AI with any OpenTelemetry backend.

Pydantic AI follows the [OpenTelemetry Semantic Conventions for Generative AI systems](https://opentelemetry.io/docs/specs/semconv/gen-ai/), so while we think you'll have the best experience using the Logfire platform ![😉](https://cdn.jsdelivr.net/gh/jdecked/twemoji@16.0.1/assets/svg/1f609.svg ":wink:"), you should be able to use any OTel service with GenAI support.

### Logfire with an alternative OTel backend

You can use the Logfire SDK completely freely and send the data to any OpenTelemetry backend.

Here's an example of configuring the Logfire library to send data to the excellent [otel-tui](https://github.com/ymtdzzz/otel-tui) — an open source terminal based OTel backend and viewer (no association with Pydantic Validation).

Run `otel-tui` with docker (see [the otel-tui readme](https://github.com/ymtdzzz/otel-tui) for more instructions):

Terminal

```
docker run --rm -it -p 4318:4318 --name otel-tui ymtdzzz/otel-tui:latest
```

then run,

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) otel\_tui.py

```
importos

importlogfire

frompydantic_aiimport Agent

os.environ['OTEL_EXPORTER_OTLP_ENDPOINT'] = 'http://localhost:4318'  # (1)!
logfire.configure(send_to_logfire=False)  # (2)!
logfire.instrument_pydantic_ai()
logfire.instrument_httpx(capture_all=True)

agent = Agent('gateway/openai:gpt-5')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> Paris
```

1. Set the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable to the URL of your OpenTelemetry backend. If you're using a backend that requires authentication, you may need to set [other environment variables](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/). Of course, these can also be set outside the process, e.g. with `export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318`.
2. We [configure](https://logfire.pydantic.dev/docs/reference/api/logfire/#logfire.configure) Logfire to disable sending data to the Logfire OTel backend itself. If you removed `send_to_logfire=False`, data would be sent to both Logfire and your OpenTelemetry backend.

otel\_tui.py

```
importos

importlogfire

frompydantic_aiimport Agent

os.environ['OTEL_EXPORTER_OTLP_ENDPOINT'] = 'http://localhost:4318'  # (1)!
logfire.configure(send_to_logfire=False)  # (2)!
logfire.instrument_pydantic_ai()
logfire.instrument_httpx(capture_all=True)

agent = Agent('openai:gpt-5')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> Paris
```

1. Set the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable to the URL of your OpenTelemetry backend. If you're using a backend that requires authentication, you may need to set [other environment variables](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/). Of course, these can also be set outside the process, e.g. with `export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318`.
2. We [configure](https://logfire.pydantic.dev/docs/reference/api/logfire/#logfire.configure) Logfire to disable sending data to the Logfire OTel backend itself. If you removed `send_to_logfire=False`, data would be sent to both Logfire and your OpenTelemetry backend.

Running the above code will send tracing data to `otel-tui`, which will display like this:

[![otel tui simple](https://ai.pydantic.dev/img/otel-tui-simple.png)](https://ai.pydantic.dev/img/otel-tui-simple.png)

Running the [weather agent](https://ai.pydantic.dev/examples/weather-agent/) example connected to `otel-tui` shows how it can be used to visualise a more complex trace:

[![otel tui weather agent](https://ai.pydantic.dev/img/otel-tui-weather.png)](https://ai.pydantic.dev/img/otel-tui-weather.png)

For more information on using the Logfire SDK to send data to alternative backends, see [the Logfire documentation](https://logfire.pydantic.dev/docs/how-to-guides/alternative-backends/).

### OTel without Logfire

You can also emit OpenTelemetry data from Pydantic AI without using Logfire at all.

To do this, you'll need to install and configure the OpenTelemetry packages you need. To run the following examples, use

Terminal

```
uv run \
  --with 'pydantic-ai-slim[openai]' \
  --with opentelemetry-sdk \
  --with opentelemetry-exporter-otlp \
  raw_otel.py
```

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) raw\_otel.py

```
importos

fromopentelemetry.exporter.otlp.proto.http.trace_exporterimport OTLPSpanExporter
fromopentelemetry.sdk.traceimport TracerProvider
fromopentelemetry.sdk.trace.exportimport BatchSpanProcessor
fromopentelemetry.traceimport set_tracer_provider

frompydantic_aiimport Agent

os.environ['OTEL_EXPORTER_OTLP_ENDPOINT'] = 'http://localhost:4318'
exporter = OTLPSpanExporter()
span_processor = BatchSpanProcessor(exporter)
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(span_processor)

set_tracer_provider(tracer_provider)

Agent.instrument_all()
agent = Agent('gateway/openai:gpt-5')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> Paris
```

raw\_otel.py

```
importos

fromopentelemetry.exporter.otlp.proto.http.trace_exporterimport OTLPSpanExporter
fromopentelemetry.sdk.traceimport TracerProvider
fromopentelemetry.sdk.trace.exportimport BatchSpanProcessor
fromopentelemetry.traceimport set_tracer_provider

frompydantic_aiimport Agent

os.environ['OTEL_EXPORTER_OTLP_ENDPOINT'] = 'http://localhost:4318'
exporter = OTLPSpanExporter()
span_processor = BatchSpanProcessor(exporter)
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(span_processor)

set_tracer_provider(tracer_provider)

Agent.instrument_all()
agent = Agent('openai:gpt-5')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> Paris
```

### Alternative Observability backends

Because Pydantic AI uses OpenTelemetry for observability, you can easily configure it to send data to any OpenTelemetry-compatible backend, not just our observability platform [Pydantic Logfire](#pydantic-logfire).

The following providers have dedicated documentation on Pydantic AI:

- [Langfuse](https://langfuse.com/docs/integrations/pydantic-ai)
- [W&B Weave](https://weave-docs.wandb.ai/guides/integrations/pydantic_ai/)
- [Arize](https://arize.com/docs/ax/observe/tracing-integrations-auto/pydantic-ai)
- [Openlayer](https://www.openlayer.com/docs/integrations/pydantic-ai)
- [OpenLIT](https://docs.openlit.io/latest/integrations/pydantic)
- [LangWatch](https://docs.langwatch.ai/integration/python/integrations/pydantic-ai)
- [Patronus AI](https://docs.patronus.ai/docs/percival/pydantic)
- [Opik](https://www.comet.com/docs/opik/tracing/integrations/pydantic-ai)
- [mlflow](https://mlflow.org/docs/latest/genai/tracing/integrations/listing/pydantic_ai)
- [Agenta](https://docs.agenta.ai/observability/integrations/pydanticai)
- [Confident AI](https://documentation.confident-ai.com/docs/llm-tracing/integrations/pydanticai)
- [LangWatch](https://docs.langwatch.ai/integration/python/integrations/pydantic-ai)
- [Braintrust](https://www.braintrust.dev/docs/integrations/sdk-integrations/pydantic-ai)
- [SigNoz](https://signoz.io/docs/pydantic-ai-observability/)

## Advanced usage

### Configuring data format

Pydantic AI follows the [OpenTelemetry Semantic Conventions for Generative AI systems](https://opentelemetry.io/docs/specs/semconv/gen-ai/). Specifically, it follows version 1.37.0 of the conventions by default, with a few exceptions. Certain span and attribute names are not spec compliant by default for compatibility reasons, but can be made compliant by passing [`InstrumentationSettings(version=3)`](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings            dataclass   ") (the default is currently `version=2`). This will change the following:

- The span name `agent run` becomes `invoke_agent {gen_ai.agent.name}` (with the agent name filled in)
- The span name `running tool` becomes `execute_tool {gen_ai.tool.name}` (with the tool name filled in)
- The attribute name `tool_arguments` becomes `gen_ai.tool.call.arguments`
- The attribute name `tool_response` becomes `gen_ai.tool.call.result`

To use [OpenTelemetry semantic conventions version 1.36.0](https://github.com/open-telemetry/semantic-conventions/blob/v1.36.0/docs/gen-ai/README.md) or older, pass [`InstrumentationSettings(version=1)`](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings            dataclass   "). Moreover, those semantic conventions specify that messages should be captured as individual events (logs) that are children of the request span, whereas by default, Pydantic AI instead collects these events into a JSON array which is set as a single large attribute called `events` on the request span. To change this, use `event_mode='logs'`:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) instrumentation\_settings\_event\_mode.py

```
importlogfire

frompydantic_aiimport Agent

logfire.configure()
logfire.instrument_pydantic_ai(version=1, event_mode='logs')
agent = Agent('gateway/openai:gpt-5')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
```

instrumentation\_settings\_event\_mode.py

```
importlogfire

frompydantic_aiimport Agent

logfire.configure()
logfire.instrument_pydantic_ai(version=1, event_mode='logs')
agent = Agent('openai:gpt-5')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
```

This won't look as good in the Logfire UI, and will also be removed from Pydantic AI in a future release, but may be useful for backwards compatibility.

Note that the OpenTelemetry Semantic Conventions are still experimental and are likely to change.

### Setting OpenTelemetry SDK providers

By default, the global `TracerProvider` and `LoggerProvider` are used. These are set automatically by `logfire.configure()`. They can also be set by the `set_tracer_provider` and `set_logger_provider` functions in the OpenTelemetry Python SDK. You can set custom providers with [`InstrumentationSettings`](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings            dataclass   ").

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) instrumentation\_settings\_providers.py

```
fromopentelemetry.sdk._logsimport LoggerProvider
fromopentelemetry.sdk.traceimport TracerProvider

frompydantic_aiimport Agent, InstrumentationSettings

instrumentation_settings = InstrumentationSettings(
    tracer_provider=TracerProvider(),
    logger_provider=LoggerProvider(),
)

agent = Agent('gateway/openai:gpt-5', instrument=instrumentation_settings)
# or to instrument all agents:
Agent.instrument_all(instrumentation_settings)
```

instrumentation\_settings\_providers.py

```
fromopentelemetry.sdk._logsimport LoggerProvider
fromopentelemetry.sdk.traceimport TracerProvider

frompydantic_aiimport Agent, InstrumentationSettings

instrumentation_settings = InstrumentationSettings(
    tracer_provider=TracerProvider(),
    logger_provider=LoggerProvider(),
)

agent = Agent('openai:gpt-5', instrument=instrumentation_settings)
# or to instrument all agents:
Agent.instrument_all(instrumentation_settings)
```

### Instrumenting a specific `Model`

instrumented\_model\_example.py

```
frompydantic_aiimport Agent
frompydantic_ai.models.instrumentedimport InstrumentationSettings, InstrumentedModel

settings = InstrumentationSettings()
model = InstrumentedModel('openai:gpt-5', settings)
agent = Agent(model)
```

### Excluding binary content

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) excluding\_binary\_content.py

```
frompydantic_aiimport Agent, InstrumentationSettings

instrumentation_settings = InstrumentationSettings(include_binary_content=False)

agent = Agent('gateway/openai:gpt-5', instrument=instrumentation_settings)
# or to instrument all agents:
Agent.instrument_all(instrumentation_settings)
```

excluding\_binary\_content.py

```
frompydantic_aiimport Agent, InstrumentationSettings

instrumentation_settings = InstrumentationSettings(include_binary_content=False)

agent = Agent('openai:gpt-5', instrument=instrumentation_settings)
# or to instrument all agents:
Agent.instrument_all(instrumentation_settings)
```

### Excluding prompts and completions

For privacy and security reasons, you may want to monitor your agent's behavior and performance without exposing sensitive user data or proprietary prompts in your observability platform. Pydantic AI allows you to exclude the actual content from telemetry while preserving the structural information needed for debugging and monitoring.

When `include_content=False` is set, Pydantic AI will exclude sensitive content from telemetry, including user prompts and model completions, tool call arguments and responses, and any other message content.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) excluding\_sensitive\_content.py

```
frompydantic_aiimport Agent
frompydantic_ai.models.instrumentedimport InstrumentationSettings

instrumentation_settings = InstrumentationSettings(include_content=False)

agent = Agent('gateway/openai:gpt-5', instrument=instrumentation_settings)
# or to instrument all agents:
Agent.instrument_all(instrumentation_settings)
```

excluding\_sensitive\_content.py

```
frompydantic_aiimport Agent
frompydantic_ai.models.instrumentedimport InstrumentationSettings

instrumentation_settings = InstrumentationSettings(include_content=False)

agent = Agent('openai:gpt-5', instrument=instrumentation_settings)
# or to instrument all agents:
Agent.instrument_all(instrumentation_settings)
```

This setting is particularly useful in production environments where compliance requirements or data sensitivity concerns make it necessary to limit what content is sent to your observability platform.

### Adding Custom Metadata

Use the agent's `metadata` parameter to attach additional data to the agent's span. When instrumentation is enabled, the computed metadata is recorded on the agent span under the `metadata` attribute. See the [usage and metadata example in the agents guide](https://ai.pydantic.dev/agents/#run-metadata) for details and usage.