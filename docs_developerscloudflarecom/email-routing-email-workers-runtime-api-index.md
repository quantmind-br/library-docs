---
title: Runtime API · Cloudflare Email Routing docs
url: https://developers.cloudflare.com/email-routing/email-workers/runtime-api/index.md
source: llms
fetched_at: 2026-01-24T15:13:46.772635756-03:00
rendered_js: false
word_count: 348
summary: This document defines the EmailEvent and associated interfaces used to programmatically process, forward, or reject incoming emails within a Worker. It details the syntax for ES modules and Service Workers, as well as the properties and methods available on ForwardableEmailMessage.
tags:
    - cloudflare-workers
    - email-routing
    - emailevent
    - serverless-functions
    - email-processing
    - javascript-api
category: reference
---

## Background

An `EmailEvent` is the event type to programmatically process your emails with a Worker. You can reject, forward, or drop emails according to the logic you construct in your Worker.

***

## Syntax: ES modules

`EmailEvent` can be handled in Workers functions written using the [ES modules format](https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/) by adding an `email` function to your module's exported handlers:

```js
export default {
  async email(message, env, ctx) {
    await message.forward("<YOUR_EMAIL>");
  },
};
```

### Parameters

* `message` ForwardableEmailMessage

  * A [`ForwardableEmailMessage` object](#forwardableemailmessage-definition).

* `env` object

  * An object containing the bindings associated with your Worker using ES modules format, such as KV namespaces and Durable Objects.

* `ctx` object

  * An object containing the context associated with your Worker using ES modules format. Currently, this object just contains the `waitUntil` function.

***

## Syntax: Service Worker

Service Workers are deprecated

Service Workers are deprecated but still supported. We recommend using [Module Workers](https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/) instead. New features may not be supported for Service Workers.

`EmailEvent` can be handled in Workers functions written using the Service Worker syntax by attaching to the `email` event with `addEventListener`:

```js
addEventListener("email", async (event) => {
  await event.message.forward("<YOUR_EMAIL>");
});
```

### Properties

* `event.message` ForwardableEmailMessage

  * An [`ForwardableEmailMessage` object](#forwardableemailmessage-definition).

***

## `ForwardableEmailMessage` definition

```ts
 interface ForwardableEmailMessage<Body = unknown> {
  readonly from: string;
  readonly to: string;
  readonly headers: Headers;
  readonly raw: ReadableStream;
  readonly rawSize: number;


  public constructor(from: string, to: string, raw: ReadableStream | string);


  setReject(reason: string): void;
  forward(rcptTo: string, headers?: Headers): Promise<void>;
  reply(message: EmailMessage): Promise<void>;
}
```

An email message that is sent to a consumer Worker and can be rejected/forwarded.

* `from` string

  * `Envelope From` attribute of the email message.

* `to` string

  * `Envelope To` attribute of the email message.

* `headers` Headers

  * A [`Headers` object](https://developer.mozilla.org/en-US/docs/Web/API/Headers).

* `raw` ReadableStream

  * [Stream](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream) of the email message content.

* `rawSize` number

  * Size of the email message content.

* `setReject(reasonstring)` : void

  * Reject this email message by returning a permanent SMTP error back to the connecting client, including the given reason.

* `forward(rcptTostring, headersHeadersoptional)` : Promise

  * Forward this email message to a verified destination address of the account. If you want, you can add extra headers to the email message. Only `X-*` headers are allowed.
  * When the promise resolves, the message is confirmed to be forwarded to a verified destination address.

* `reply(EmailMessage)` : Promise

  * Reply to the sender of this email message with a new EmailMessage object.
  * When the promise resolves, the message is confirmed to be replied.

## `EmailMessage` definition

```ts
interface EmailMessage {
    readonly from: string;
    readonly to: string;
}
```

An email message that can be sent from a Worker.

* `from` string

  * `Envelope From` attribute of the email message.

* `to` string

  * `Envelope To` attribute of the email message.