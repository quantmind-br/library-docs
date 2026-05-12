---
title: pi-ai
tags:
  - llm
  - typescript
  - agentic-workflows
  - api-wrapper
  - typebox
  - tool-calling
category: api
optimized: true
optimized_at: 2026-05-03T12:31:00Z
related:
  - "[[001-packages-agent-readme|pi-agent-core]]"
  - "[[009-packages-coding-agent-readme|coding-agent]]"
  - "[[052-packages-coding-agent-docs-models|models config]]"
  - "[[053-packages-coding-agent-docs-providers|providers setup]]"
word_count: 835
optimized: true
optimized_at: 2026-05-03T12:00:00Z
---
# @mariozechner/pi-ai

Unified LLM API with automatic model discovery, tool calling, token/cost tracking, and cross-provider context serialization.

> Only includes models that support tool calling (function calling) for agentic workflows.

## Supported Providers

| Provider | API |
|----------|-----|
| OpenAI | `openai-responses`, `openai-completions` |
| Azure OpenAI | `azure-openai-responses` |
| DeepSeek, xAI, Groq, Cerebras, Fireworks | `openai-completions` |
| Anthropic | `anthropic-messages` |
| Google, Vertex AI | `google-generative-ai`, `google-vertex` |
| Mistral | `mistral-conversations` |
| Cloudflare AI Gateway/Workers AI | `openai-completions` |
| OpenRouter, Vercel AI Gateway | `openai-completions` |
| Amazon Bedrock | `bedrock-converse-stream` |
| OpenCode Zen/Go, Kimi, Xiaomi MiMo | Various |
| Any OpenAI-compatible | Ollama, vLLM, LM Studio |

```bash
npm install @mariozechner/pi-ai
```

TypeBox exports (`Type`, `Static`, `TSchema`) are re-exported from this package.

## Quick Start

```typescript
import { Type, getModel, stream, complete, Context, Tool, StringEnum } from '@mariozechner/pi-ai';

// Get model with auto-complete
const model = getModel('openai', 'gpt-4o-mini');

// Define tools with TypeBox schemas
const tools: Tool[] = [{
  name: 'get_time',
  description: 'Get the current time',
  parameters: Type.Object({
    timezone: Type.Optional(Type.String({ description: 'Optional timezone' }))
  })
}];

// Build context (serializable between models)
const context: Context = {
  systemPrompt: 'You are a helpful assistant.',
  messages: [{ role: 'user', content: 'What time is it?' }],
  tools
};

// Streaming with full events
const s = stream(model, context);
for await (const event of s) {
  switch (event.type) {
    case 'text_delta':
      process.stdout.write(event.delta);
      break;
    case 'toolcall_end':
      console.log(`\nTool: ${event.toolCall.name}`);
      break;
    case 'done':
      console.log(`\nFinished: ${event.reason}`);
      break;
  }
}

// Get final message
const finalMessage = await s.result();
context.messages.push(finalMessage);

// Handle tool calls
const toolCalls = finalMessage.content.filter(b => b.type === 'toolCall');
for (const call of toolCalls) {
  const result = call.name === 'get_time'
    ? new Date().toLocaleString('en-US', { timeZone: call.arguments.timezone || 'UTC' })
    : 'Unknown tool';

  context.messages.push({
    role: 'toolResult',
    toolCallId: call.id,
    toolName: call.name,
    content: [{ type: 'text', text: result }],
    isError: false,
    timestamp: Date.now()
  });
}

// Continue if tools were called
if (toolCalls.length > 0) {
  const continuation = await complete(model, context);
  context.messages.push(continuation);
}

// Cost tracking
console.log(`Tokens: ${finalMessage.usage.input} in, ${finalMessage.usage.output} out`);
console.log(`Cost: $${finalMessage.usage.cost.total.toFixed(4)}`);
```

### Simple Interface

```typescript
import { streamSimple, completeSimple } from '@mariozechner/pi-ai';

const response = await completeSimple(model, context, { reasoning: 'medium' });
for (const block of response.content) {
  if (block.type === 'thinking') {
    console.log('Thinking:', block.thinking);
  } else if (block.type === 'text') {
    console.log('Response:', block.text);
  }
}
```

## Tools

Tools use TypeBox schemas for type-safe definitions with automatic validation.

### Defining Tools

```typescript
import { Type, Tool, StringEnum } from '@mariozechner/pi-ai';

const weatherTool: Tool = {
  name: 'get_weather',
  description: 'Get current weather',
  parameters: Type.Object({
    location: Type.String(),
    units: StringEnum(['celsius', 'fahrenheit'], { default: 'celsius' })
  })
};
```

> Use `StringEnum` instead of `Type.Enum` for Google API compatibility.

### Tool Results

Tool results support text and images:

```typescript
context.messages.push({
  role: 'toolResult',
  toolCallId: block.id,
  toolName: block.name,
  content: [
    { type: 'text', text: JSON.stringify(result) },
    { type: 'image', data: base64Image, mimeType: 'image/png' }
  ],
  isError: false,
  timestamp: Date.now()
});
```

### Streaming Tool Calls

Tool arguments stream progressively during `toolcall_delta`:

```typescript
if (event.type === 'toolcall_delta') {
  const toolCall = event.partial.content[event.contentIndex];
  // BE DEFENSIVE: arguments may be incomplete
  if (toolCall.type === 'toolCall' && toolCall.arguments?.path) {
    console.log(`Writing to: ${toolCall.arguments.path}`);
  }
}

if (event.type === 'toolcall_end') {
  // Full validated toolCall here
  const { id, name, arguments: args } = event.toolCall;
}
```

### Validating Tool Arguments

With `agentLoop`, validation is automatic. For custom loops:

```typescript
import { stream, validateToolCall } from '@mariozechner/pi-ai';

for await (const event of stream(model, { messages, tools })) {
  if (event.type === 'toolcall_end') {
    try {
      const validatedArgs = validateToolCall(tools, event.toolCall);
      const result = await executeMyTool(event.toolCall.name, validatedArgs);
    } catch (error) {
      // Return error to model for retry
      context.messages.push({
        role: 'toolResult',
        toolCallId: event.toolCall.id,
        toolName: event.toolCall.name,
        content: [{ type: 'text', text: error.message }],
        isError: true,
        timestamp: Date.now()
      });
    }
  }
}
```

### Event Reference

| Event | Description | Key Properties |
|-------|-------------|----------------|
| `start` | Stream begins | `partial.model` |
| `text_start/end` | Text block | `contentIndex` |
| `text_delta` | Text chunk | `delta`, `contentIndex` |
| `thinking_start/end` | Thinking block | `contentIndex` |
| `thinking_delta` | Thinking chunk | `delta` |
| `toolcall_start/end` | Tool call | `contentIndex`, `toolCall` |
| `toolcall_delta` | Streaming args | `delta`, `partial.arguments` |
| `done` | Complete | `reason`, `message` |
| `error` | Error/abort | `reason`, `error` |

## Image Input

Check `model.input.includes('image')`. Non-vision models silently ignore images.

```typescript
if (model.input.includes('image')) {
  const image = readFileSync('image.png').toString('base64');
  const response = await complete(model, {
    messages: [{
      role: 'user',
      content: [
        { type: 'text', text: 'What is in this image?' },
        { type: 'image', data: base64Image, mimeType: 'image/png' }
      ]
    }]
  });
}
```

## Thinking/Reasoning

Check `model.reasoning` to verify support.

### Unified Interface

```typescript
import { streamSimple, completeSimple } from '@mariozechner/pi-ai';

// Many providers: anthropic, openai, google, xai, groq, cerebras, openrouter
const response = await completeSimple(model, context, { reasoning: 'medium' });
// Levels: 'minimal' | 'low' | 'medium' | 'high' | 'xhigh'
```

### Provider-Specific

```typescript
// OpenAI
await complete(openaiModel, context, {
  reasoningEffort: 'medium',
  reasoningSummary: 'detailed'
});

// Anthropic
await complete(anthropicModel, context, {
  thinkingEnabled: true,
  thinkingBudgetTokens: 8192
});

// Google
await complete(googleModel, context, {
  thinking: { enabled: true, budgetTokens: 8192 }
});
```

### Streaming

```typescript
for await (const event of streamSimple(model, context, { reasoning: 'high' })) {
  switch (event.type) {
    case 'thinking_delta':
      process.stdout.write(event.delta);
      break;
  }
}
```

## Stop Reasons

Every `AssistantMessage` has `stopReason`:

- `"stop"` - Normal completion
- `"length"` - Hit token limit
- `"toolUse"` - Calling tools
- `"error"` - Generation error
- `"aborted"` - Cancelled via signal

May also include `responseId` from upstream.

## Error Handling

```typescript
for await (const event of stream) {
  if (event.type === 'error') {
    console.error(`Error (${event.reason}):`, event.error.errorMessage);
  }
}
```

### Aborting Requests

```typescript
const controller = new AbortController();
setTimeout(() => controller.abort(), 2000);

const s = stream(model, { messages }, { signal: controller.signal });
const response = await s.result();

if (response.stopReason === 'aborted') {
  console.log('Partial content:', response.content);
}
```

### Continuing After Abort

```typescript
context.messages.push(partial);
context.messages.push({ role: 'user', content: 'Please continue' });
const continuation = await complete(model, context);
```

### Debugging Payloads

```typescript
await complete(model, context, {
  onPayload: (payload) => {
    console.log(JSON.stringify(payload, null, 2));
  }
});
```

## APIs, Models, Providers

### Built-in APIs

| API | Functions | Providers |
|-----|-----------|-----------|
| `anthropic-messages` | `streamAnthropic`, `AnthropicOptions` | Anthropic |
| `google-generative-ai` | `streamGoogle`, `GoogleOptions` | Google |
| `google-vertex` | `streamGoogleVertex`, `GoogleVertexOptions` | Vertex AI |
| `mistral-conversations` | `streamMistral`, `MistralOptions` | Mistral |
| `openai-completions` | `streamOpenAICompletions`, `OpenAICompletionsOptions` | Many |
| `openai-responses` | `streamOpenAIResponses`, `OpenAIResponsesOptions` | OpenAI |
| `openai-codex-responses` | `streamOpenAICodexResponses` | Codex |
| `azure-openai-responses` | `streamAzureOpenAIResponses` | Azure |
| `bedrock-converse-stream` | `streamBedrock`, `BedrockOptions` | Bedrock |

### Querying

```typescript
const providers = getProviders();
const models = getModels('anthropic');
const model = getModel('openai', 'gpt-4o-mini');
```

### Custom Models

```typescript
import { Model } from '@mariozechner/pi-ai';

// Ollama
const ollamaModel: Model<'openai-completions'> = {
  id: 'llama-3.1-8b',
  name: 'Llama 3.1 8B',
  api: 'openai-completions',
  provider: 'ollama',
  baseUrl: 'http://localhost:11434/v1',
  reasoning: false,
  input: ['text'],
  cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
  contextWindow: 128000,
  maxTokens: 32000
};

// LiteLLM with compat settings
const litellmModel: Model<'openai-completions'> = {
  id: 'gpt-4o',
  api: 'openai-completions',
  provider: 'litellm',
  baseUrl: 'http://localhost:4000/v1',
  compat: { supportsStore: false }
};
```

### OpenAI Compat Settings

```typescript
interface OpenAICompletionsCompat {
  supportsStore?: boolean;              // default: true
  supportsDeveloperRole?: boolean;       // default: true
  supportsReasoningEffort?: boolean;     // default: true
  supportsUsageInStreaming?: boolean;    // default: true
  supportsStrictMode?: boolean;          // default: true
  sendSessionAffinityHeaders?: boolean;  // default: false
  maxTokensField?: 'max_completion_tokens' | 'max_tokens';
  requiresToolResultName?: boolean;      // default: false
  requiresAssistantAfterToolResult?: boolean;
  requiresThinkingAsText?: boolean;
  requiresReasoningContentOnAssistantMessages?: boolean;
  thinkingFormat?: 'openai' | 'deepseek' | 'zai' | 'qwen' | 'qwen-chat-template';
  cacheControlFormat?: 'anthropic';
  openRouterRouting?: OpenRouterRouting;
  vercelGatewayRouting?: VercelGatewayRouting;
}
```

### Thinking Level Map

For Ollama/vLLM/SGLang servers:

```typescript
const model: Model<'openai-completions'> = {
  id: 'gpt-oss:20b',
  api: 'openai-completions',
  provider: 'ollama',
  reasoning: true,
  thinkingLevelMap: {
    minimal: null,  // unsupported
    low: null,
    medium: null,
    high: 'high',
    xhigh: null,
  },
  compat: {
    supportsDeveloperRole: false,
    supportsReasoningEffort: false,
  }
};
```

## Cross-Provider Handoffs

Seamless context transfer between providers:

```typescript
// Start with Claude
const claude = getModel('anthropic', 'claude-sonnet-4-20250514');
context.messages.push({ role: 'user', content: 'What is 25 * 18?' });
const claudeResponse = await complete(claude, context, { thinkingEnabled: true });
context.messages.push(claudeResponse);

// Switch to GPT-5
const gpt5 = getModel('openai', 'gpt-5-mini');
context.messages.push({ role: 'user', content: 'Is that correct?' });
const gptResponse = await complete(gpt5, context);

// Switch to Gemini
const gemini = getModel('google', 'gemini-2.5-flash');
const geminiResponse = await complete(gemini, context);
```

Automatic transformations:
- User/tool result messages: pass through
- Same-provider assistant messages: preserve
- Different-provider assistant messages: thinking blocks become `<thinking>` tagged text
- Tool calls and text: preserve unchanged

## Context Serialization

`Context` is plain JSON-serializable:

```typescript
const serialized = JSON.stringify(context);
localStorage.setItem('conversation', serialized);

const restored: Context = JSON.parse(localStorage.getItem('conversation')!);
```

## Browser Usage

API key must be passed explicitly (no env vars):

```typescript
const response = await complete(model, {
  messages: [{ role: 'user', content: 'Hello!' }]
}, { apiKey: 'your-api-key' });
```

> **Security Warning**: Exposing API keys in frontend is dangerous. Use backend proxy for production.

### Browser Limitations

- Amazon Bedrock not supported
- OAuth flows not supported
- Use `@mariozechner/pi-ai/oauth` in Node.js

## Environment Variables

| Provider | Variable(s) |
|----------|-------------|
| OpenAI | `OPENAI_API_KEY` |
| Azure OpenAI | `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_BASE_URL` (or `AZURE_OPENAI_RESOURCE_NAME`) |
| Anthropic | `ANTHROPIC_API_KEY` or `ANTHROPIC_OAUTH_TOKEN` |
| DeepSeek | `DEEPSEEK_API_KEY` |
| Google | `GEMINI_API_KEY` |
| Vertex AI | `GOOGLE_CLOUD_API_KEY` or `GOOGLE_CLOUD_PROJECT` + `GOOGLE_CLOUD_LOCATION` + ADC |
| Mistral | `MISTRAL_API_KEY` |
| Groq | `GROQ_API_KEY` |
| Cerebras | `CEREBRAS_API_KEY` |
| Cloudflare | `CLOUDFLARE_API_KEY` + `CLOUDFLARE_ACCOUNT_ID` + `CLOUDFLARE_GATEWAY_ID` |
| xAI | `XAI_API_KEY` |
| Fireworks | `FIREWORKS_API_KEY` |
| OpenRouter | `OPENROUTER_API_KEY` |
| Vercel AI Gateway | `AI_GATEWAY_API_KEY` |
| zAI | `ZAI_API_KEY` |
| MiniMax | `MINIMAX_API_KEY` |
| OpenCode | `OPENCODE_API_KEY` |
| Kimi | `KIMI_API_KEY` |
| Xiaomi MiMo | `XIAOMI_API_KEY` (API) or `XIAOMI_TOKEN_PLAN_CN_API_KEY` (CN/AMS/SGP) |
| GitHub Copilot | `COPILOT_GITHUB_TOKEN` or `GH_TOKEN` |

### Checking Keys

```typescript
import { getEnvApiKey } from '@mariozechner/pi-ai';
const key = getEnvApiKey('openai');  // checks OPENAI_API_KEY
```

## OAuth Providers

### CLI Login

```bash
npx @mariozechner/pi-ai login              # interactive
npx @mariozechner/pi-ai login anthropic    # specific provider
npx @mariozechner/pi-ai list               # list providers
```

Credentials saved to `auth.json`.

### Programmatic OAuth

```typescript
import {
  loginAnthropic, loginOpenAICodex, loginGitHubCopilot,
  refreshOAuthToken, getOAuthApiKey,
  type OAuthProvider, type OAuthCredentials
} from '@mariozechner/pi-ai/oauth';

// Login
const credentials = await loginGitHubCopilot({
  onAuth: (url, instructions) => {
    console.log(`Open: ${url}`);
  },
  onPrompt: async (prompt) => {
    return await getUserInput(prompt.message);
  },
});

// Store and use
writeFileSync('auth.json', JSON.stringify({ 'github-copilot': { type: 'oauth', ...credentials } }));

// Get API key (auto-refreshes if expired)
const result = await getOAuthApiKey('github-copilot', auth);
if (result) {
  writeFileSync('auth.json', JSON.stringify({ 'github-copilot': { type: 'oauth', ...result.newCredentials } }));
  const response = await complete(model, { messages }, { apiKey: result.apiKey });
}
```

### Vertex AI

```bash
# Local (user credentials)
gcloud auth application-default login
export GOOGLE_CLOUD_PROJECT="my-project"
export GOOGLE_CLOUD_LOCATION="us-central1"

# CI/Production (service account)
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
```

### Provider Notes

**OpenAI Codex**: Requires ChatGPT Plus/Pro. Set `transport` in options: `"sse"`, `"websocket"`, or `"auto"`. WebSocket connections reuse sessions, expire after 5 min inactivity.

**Azure OpenAI**: Responses API only. Supports `*.openai.azure.com` and `*.cognitiveservices.azure.com`. Root endpoints auto-normalize. Use `AZURE_OPENAI_API_VERSION` (default `v1`). Deployment names treated as model IDs by default.

**GitHub Copilot**: If "model not supported" error, enable manually in VS Code Copilot Chat model selector.

## Faux Provider (Tests)

```typescript
import {
  complete, fauxAssistantMessage, fauxText, fauxThinking,
  fauxToolCall, registerFauxProvider, stream
} from '@mariozechner/pi-ai';

const registration = registerFauxProvider({ tokensPerSecond: 50 });
const model = registration.getModel();

registration.setResponses([
  fauxAssistantMessage([
    fauxThinking('Need to inspect package metadata first.'),
    fauxToolCall('echo', { text: 'package.json' })
  ], { stopReason: 'toolUse' })
]);

const first = await complete(model, context, { sessionId: 'session-1' });
registration.unregister();
```

## Adding a New Provider

See [[021-agents.md|AGENTS.md]] for full checklist. Summary:

1. **types.ts**: Add `KnownApi`, options interface, `KnownProvider`
2. **providers/**: Create stream function, return standardized events
3. **register-builtins.ts**: Lazy-load, add subpath export
4. **generate-models.ts**: Fetch/parse provider models
5. **test/**: Add to stream.test.ts and provider matrix
6. **coding-agent/**: Update model-resolver.ts, args.ts, README.md, docs/providers.md
7. **README.md**: Document new provider
8. **CHANGELOG.md**: Add entry

## License

MIT
