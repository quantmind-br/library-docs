---
title: Websocket - Evolution API Documentation
url: https://doc.evolution-api.com/v2/en/integrations/websocket
source: sitemap
fetched_at: 2026-04-12T18:46:06.58981713-03:00
rendered_js: false
word_count: 461
summary: 'This document explains how to connect to and utilize the Evolution API''s real-time event stream via WebSockets, detailing two operating modes: global mode for monitoring all instances or traditional mode for connecting to a single, isolated instance.'
tags:
    - websocket-api
    - real-time-events
    - global-mode
    - traditional-mode
    - connection-guide
category: guide
---

The Evolution API uses `socket.io` to emit real-time events, leveraging WebSocket technology. This makes integration development more efficient and straightforward for developers. WebSocket provides a full-duplex communication channel over a single, long-lasting connection, enabling real-time data flow between the client and the server.

## WebSocket Operating Modes

### Global Mode

In **global mode**, the `WEBSOCKET_GLOBAL_EVENTS` environment variable must be set to `true`. In this mode, the WebSocket is initialized when the service starts and sends events from all instances, regardless of channels. This means that any client connected to the WebSocket will receive global events, covering all Evolution API instances configured in the system.

- **Activation**: Configure in the `.env` file:
  
  ```
  WEBSOCKET_GLOBAL_EVENTS=true
  ```
- **Functionality**: Ideal for scenarios where you want to monitor or process events from all instances simultaneously without needing to establish a separate connection for each instance.
- **Connection**: In global mode, the WebSocket connection **does not** require the use of `/instance_name` in the URL. The connection URL will simply be:

### Traditional Mode

In **traditional mode**, the WebSocket can only be connected after executing the `set` command on the instance. This allows the WebSocket to be specific to each instance, and real-time communication is restricted to that instance.

- **Activation**: Ensure that `WEBSOCKET_GLOBAL_EVENTS` is set to `false` or not configured, and follow the traditional instance setup flow.
- **Functionality**: Ideal for scenarios where you want more isolated real-time communication, focused on a single instance, allowing greater control and segmentation of events.
- **Connection**: In traditional mode, the WebSocket connection requires the use of `/instance_name` in the URL:
  
  ```
  wss://api.yoursite.com/instance_name
  ```

## Connecting to the WebSocket

### Global Mode

In global mode, the connection URL is simpler and does not require the instance name:

### Traditional Mode

In traditional mode, use the following URL format:

```
wss://api.yoursite.com/instance_name
```

Replace `api.yoursite.com` with your API’s actual domain and `instance_name` with your specific instance name.

### WebSocket Connection Example

Here is a basic example of how to establish a WebSocket connection using JavaScript:

```
const socket = io('wss://api.yoursite.com/instance_name', {
  transports: ['websocket']
});

socket.on('connect', () => {
  console.log('Connected to the Evolution API WebSocket');
});

// Listening to events
socket.on('event_name', (data) => {
  console.log('Event received:', data);
});

// Handling disconnection
socket.on('disconnect', () => {
  console.log('Disconnected from the Evolution API WebSocket');
});
```

In this example, replace `event_name` with the specific event you want to listen to.

## Handling Events

Once connected, you can listen to various events emitted by the server. Each event can carry data relevant to the event’s context. For instance, if you are listening for message updates, you may receive data containing the updated message content and metadata.

## Closing the Connection

To close the WebSocket connection, use the `disconnect` method:

Remember to handle the connection responsibly by disconnecting when your application or component is unmounted to avoid memory leaks and ensure efficient resource usage.

## Final Considerations

The Evolution API provides a powerful way to interact in real-time through WebSockets, offering a seamless experience for both developers and end users. Whether in global mode, monitoring all instances simultaneously, or in traditional mode, focused on a single instance, the system’s flexibility allows for adaptation to the specific needs of your project.