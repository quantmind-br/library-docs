---
title: /realtime | liteLLM
url: https://docs.litellm.ai/docs/realtime
source: sitemap
fetched_at: 2026-01-21T19:54:09.903514476-03:00
rendered_js: false
word_count: 79
summary: This document explains how to implement load balancing for realtime audio requests across Azure and OpenAI using LiteLLM and WebSockets.
tags:
    - azure-openai
    - litellm
    - load-balancing
    - websocket
    - realtime-api
    - gpt-4o
category: configuration
---

Use this to loadbalance across Azure + OpenAI.

```
// test.js
constWebSocket=require("ws");

const url ="ws://0.0.0.0:4000/v1/realtime?model=openai-gpt-4o-realtime-audio";
// const url = "wss://my-endpoint-sweden-berri992.openai.azure.com/openai/realtime?api-version=2024-10-01-preview&deployment=gpt-4o-realtime-preview";
const ws =newWebSocket(url,{
headers:{
"api-key":`f28ab7b695af4154bc53498e5bdccb07`,
"OpenAI-Beta":"realtime=v1",
},
});

ws.on("open",functionopen(){
console.log("Connected to server.");
    ws.send(JSON.stringify({
type:"response.create",
response:{
modalities:["text"],
instructions:"Please assist the user.",
}
}));
});

ws.on("message",functionincoming(message){
console.log(JSON.parse(message.toString()));
});

ws.on("error",functionhandleError(error){
console.error("Error: ", error);
});
```

To prevent requests from being dropped, by default LiteLLM just logs these event types:

You can override this by setting the `logged_real_time_event_types` parameter in the config. For example: