---
title: Gemini Realtime API - Google AI Studio | liteLLM
url: https://docs.litellm.ai/docs/providers/google_ai_studio/realtime
source: sitemap
fetched_at: 2026-01-21T19:49:17.220946305-03:00
rendered_js: false
word_count: 38
summary: This document provides a code example demonstrating how to connect to the LiteLLM Realtime API using WebSockets in a Node.js environment.
tags:
    - litellm
    - websockets
    - node-js
    - realtime-api
    - openai-compatible
category: tutorial
---

```
// test.js
constWebSocket=require("ws");

const url ="ws://0.0.0.0:4000/v1/realtime?model=openai-gemini-2.0-flash";

const ws =newWebSocket(url,{
headers:{
"api-key":`${LITELLM_API_KEY}`,
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