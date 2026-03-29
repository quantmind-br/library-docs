---
title: Vertex AI Live API WebSocket Passthrough | liteLLM
url: https://docs.litellm.ai/docs/pass_through/vertex_ai_live_websocket
source: sitemap
fetched_at: 2026-01-21T19:46:59.103391022-03:00
rendered_js: false
word_count: 439
summary: This document explains how to configure and use LiteLLM's WebSocket passthrough for the Vertex AI Live API, enabling real-time bidirectional communication and cost tracking for Gemini models.
tags:
    - vertex-ai
    - websocket
    - litellm
    - gemini-live
    - real-time-api
    - cost-tracking
category: guide
---

LiteLLM now supports WebSocket passthrough for the Vertex AI Live API, enabling real-time bidirectional communication with Gemini models.

## Overview[​](#overview "Direct link to Overview")

The Vertex AI Live API WebSocket passthrough allows you to:

- Connect to Vertex AI Live API through LiteLLM proxy
- Use existing Vertex AI authentication methods
- Pass through all WebSocket messages bidirectionally
- Support text, audio, video, and multimodal interactions
- Track costs automatically for all usage types

## Configuration[​](#configuration "Direct link to Configuration")

### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

Set the following environment variables for Vertex AI authentication:

```
# Required
DEFAULT_VERTEXAI_PROJECT=your-project-id
DEFAULT_VERTEXAI_LOCATION=us-central1

# Optional - use one of these for authentication
DEFAULT_GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
# OR run: gcloud auth application-default login
```

### Configuration File[​](#configuration-file "Direct link to Configuration File")

Alternatively, configure in your `config.yaml`:

```
litellm_settings:
default_vertex_config:
vertex_project:"your-project-id"
vertex_location:"us-central1"
vertex_credentials:"os.environ/GOOGLE_APPLICATION_CREDENTIALS"
```

## Usage[​](#usage "Direct link to Usage")

### WebSocket Endpoints[​](#websocket-endpoints "Direct link to WebSocket Endpoints")

- `ws://your-proxy-host/v1/vertex-ai/live`
- `ws://your-proxy-host/vertex-ai/live`

### Query Parameters[​](#query-parameters "Direct link to Query Parameters")

- `project_id` (optional): Google Cloud project ID (can be set in config)
- `location` (optional): Vertex AI location (can be set in config, default: us-central1)

### Example Connection[​](#example-connection "Direct link to Example Connection")

```
// If project_id and location are set in config, you can connect without query params
const ws =newWebSocket('ws://localhost:4000/v1/vertex-ai/live');

// Or specify them explicitly
const ws =newWebSocket('ws://localhost:4000/v1/vertex-ai/live?project_id=your-project-id&location=us-central1');
```

## Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

The WebSocket passthrough automatically tracks costs for all usage types based on the [Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing#model-optimizer-pricing):

### Supported Cost Tracking[​](#supported-cost-tracking "Direct link to Supported Cost Tracking")

- **Text**: Character-based or token-based pricing depending on model
- **Audio**: Per-second pricing for audio input/output
- **Video**: Per-second pricing for video input
- **Images**: Per-image pricing for image input

### Cost Calculation[​](#cost-calculation "Direct link to Cost Calculation")

Costs are calculated using the same methods as other Vertex AI models in LiteLLM:

- Uses `cost_per_character` for Gemini models
- Uses `cost_per_token` for partner models (Claude, Llama, etc.)
- Includes audio, video, and image costs when applicable

### Cost Logging[​](#cost-logging "Direct link to Cost Logging")

Costs are automatically logged to:

- LiteLLM proxy logs
- Database (if configured)
- Spend tracking system
- Admin dashboard

Example log output:

```
Vertex AI Live WebSocket session cost: $0.001234 (input: $0.000800, output: $0.000434) tokens: 150, characters: 1200, duration: 45.2s
```

## API Reference[​](#api-reference "Direct link to API Reference")

### Setup Message[​](#setup-message "Direct link to Setup Message")

Send this message first to initialize the session:

```
{
"setup":{
"model":"projects/your-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash-live-preview-04-09",
"generation_config":{
"response_modalities":["TEXT"]
}
}
}
```

### Text Input[​](#text-input "Direct link to Text Input")

```
{
"client_content":{
"turns":[
{
"role":"user",
"parts":[{"text":"Hello! How are you?"}]
}
],
"turn_complete":true
}
}
```

### Audio Input[​](#audio-input "Direct link to Audio Input")

```
{
"realtime_input":{
"media_chunks":[
{
"data":"base64-encoded-audio-data",
"mime_type":"audio/pcm"
}
]
}
}
```

## Supported Features[​](#supported-features "Direct link to Supported Features")

### Response Modalities[​](#response-modalities "Direct link to Response Modalities")

- **TEXT**: Text responses
- **AUDIO**: Audio responses with voice synthesis

### Tools[​](#tools "Direct link to Tools")

- **Function Calling**: Define and use custom functions
- **Code Execution**: Execute Python code
- **Google Search**: Search the web
- **Voice Activity Detection**: Detect when user is speaking

### Advanced Features[​](#advanced-features "Direct link to Advanced Features")

- **Audio Transcription**: Transcribe input and output audio
- **Proactive Audio**: Model responds only when relevant
- **Affective Dialog**: Understand emotional expressions

## Examples[​](#examples "Direct link to Examples")

### Python Client[​](#python-client "Direct link to Python Client")

```
import asyncio
import json
import websockets

asyncdefchat_with_gemini():
    uri ="ws://localhost:4000/v1/vertex-ai/live?project_id=your-project-id"

asyncwith websockets.connect(uri)as websocket:
# Setup
        setup ={
"setup":{
"model":"projects/your-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash-live-preview-04-09",
"generation_config":{"response_modalities":["TEXT"]}
}
}
await websocket.send(json.dumps(setup))

# Wait for setup response
        response =await websocket.recv()
print(f"Setup: {response}")

# Send message
        message ={
"client_content":{
"turns":[{"role":"user","parts":[{"text":"Hello!"}]}],
"turn_complete":True
}
}
await websocket.send(json.dumps(message))

# Receive response
asyncfor response in websocket:
print(f"Response: {response}")
# Check if turn is complete
            data = json.loads(response)
if data.get("serverContent",{}).get("turnComplete"):
break

asyncio.run(chat_with_gemini())
```

### JavaScript Client[​](#javascript-client "Direct link to JavaScript Client")

```
const ws =newWebSocket('ws://localhost:4000/v1/vertex-ai/live?project_id=your-project-id');

ws.onopen=function(){
// Send setup
const setup ={
setup:{
model:"projects/your-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash-live-preview-04-09",
generation_config:{response_modalities:["TEXT"]}
}
};
    ws.send(JSON.stringify(setup));
};

ws.onmessage=function(event){
const data =JSON.parse(event.data);
console.log('Received:', data);

// Check if setup is complete
if(data.setupComplete){
// Send a message
const message ={
client_content:{
turns:[{role:"user",parts:[{text:"Hello!"}]}],
turn_complete:true
}
};
        ws.send(JSON.stringify(message));
}
};
```

## Error Handling[​](#error-handling "Direct link to Error Handling")

The WebSocket connection may close with these codes:

- `4001`: Vertex AI credentials not configured
- `4002`: Project ID not provided
- `1011`: Internal server error

## Authentication[​](#authentication "Direct link to Authentication")

The WebSocket passthrough uses the same authentication as other LiteLLM endpoints:

1. **API Key**: Pass `Authorization: Bearer your-api-key` header
2. **Vertex AI Credentials**: Set environment variables or config file

## Limitations[​](#limitations "Direct link to Limitations")

- Requires valid Google Cloud project with Vertex AI API enabled
- WebSocket connections are not persistent across server restarts
- Rate limits apply based on your Google Cloud quotas

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Common Issues[​](#common-issues "Direct link to Common Issues")

1. **Authentication Error**: Ensure Vertex AI credentials are properly configured
2. **Project Not Found**: Verify the project ID exists and has Vertex AI enabled
3. **Connection Refused**: Check that the LiteLLM proxy server is running

### Debug Mode[​](#debug-mode "Direct link to Debug Mode")

Enable debug logging to see detailed connection information:

- [Vertex AI Live API Reference](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live)
- [LiteLLM Proxy Configuration](https://docs.litellm.ai/docs/proxy/)
- [Vertex AI Passthrough Endpoints](https://docs.litellm.ai/docs/pass_through/vertex_ai)