---
title: 'Interface: HttpService'
url: https://docs.docker.com/reference/api/extensions-sdk/HttpService/
source: llms
fetched_at: 2026-01-24T14:31:28.957554223-03:00
rendered_js: false
word_count: 174
summary: This document defines the HTTP request methods available in the Docker Extension VM service for communicating with backend services.
tags:
    - docker-extensions
    - vm-service
    - http-requests
    - api-client
    - sdk-reference
category: api
---

Table of contents

* * *

**`Since`**

0.2.0

## [Methods](#methods)

### [get](#get)

▸ **get**(`url`): `Promise`&lt;`unknown`&gt;

Performs an HTTP GET request to a backend service.

```
ddClient.extension.vm.service
 .get("/some/service")
 .then((value: any) => console.log(value)
```

#### [Parameters](#parameters)

NameTypeDescription`url``string`The URL of the backend service.

#### [Returns](#returns)

`Promise`&lt;`unknown`&gt;

* * *

### [post](#post)

▸ **post**(`url`, `data`): `Promise`&lt;`unknown`&gt;

Performs an HTTP POST request to a backend service.

```
ddClient.extension.vm.service
 .post("/some/service", { ... })
 .then((value: any) => console.log(value));
```

#### [Parameters](#parameters-1)

NameTypeDescription`url``string`The URL of the backend service.`data``any`The body of the request.

#### [Returns](#returns-1)

`Promise`&lt;`unknown`&gt;

* * *

### [put](#put)

▸ **put**(`url`, `data`): `Promise`&lt;`unknown`&gt;

Performs an HTTP PUT request to a backend service.

```
ddClient.extension.vm.service
 .put("/some/service", { ... })
 .then((value: any) => console.log(value));
```

#### [Parameters](#parameters-2)

NameTypeDescription`url``string`The URL of the backend service.`data``any`The body of the request.

#### [Returns](#returns-2)

`Promise`&lt;`unknown`&gt;

* * *

### [patch](#patch)

▸ **patch**(`url`, `data`): `Promise`&lt;`unknown`&gt;

Performs an HTTP PATCH request to a backend service.

```
ddClient.extension.vm.service
 .patch("/some/service", { ... })
 .then((value: any) => console.log(value));
```

#### [Parameters](#parameters-3)

NameTypeDescription`url``string`The URL of the backend service.`data``any`The body of the request.

#### [Returns](#returns-3)

`Promise`&lt;`unknown`&gt;

* * *

### [delete](#delete)

▸ **delete**(`url`): `Promise`&lt;`unknown`&gt;

Performs an HTTP DELETE request to a backend service.

```
ddClient.extension.vm.service
 .delete("/some/service")
 .then((value: any) => console.log(value));
```

#### [Parameters](#parameters-4)

NameTypeDescription`url``string`The URL of the backend service.

#### [Returns](#returns-4)

`Promise`&lt;`unknown`&gt;

* * *

### [head](#head)

▸ **head**(`url`): `Promise`&lt;`unknown`&gt;

Performs an HTTP HEAD request to a backend service.

```
ddClient.extension.vm.service
 .head("/some/service")
 .then((value: any) => console.log(value));
```

#### [Parameters](#parameters-5)

NameTypeDescription`url``string`The URL of the backend service.

#### [Returns](#returns-5)

`Promise`&lt;`unknown`&gt;

* * *

### [request](#request)

▸ **request**(`config`): `Promise`&lt;`unknown`&gt;

Performs an HTTP request to a backend service.

```
ddClient.extension.vm.service
 .request({ url: "/url", method: "GET", headers: { 'header-key': 'header-value' }, data: { ... }})
 .then((value: any) => console.log(value));
```

#### [Parameters](#parameters-6)

NameTypeDescription`config`[`RequestConfig`](https://docs.docker.com/reference/api/extensions-sdk/RequestConfig/)The URL of the backend service.

#### [Returns](#returns-6)

`Promise`&lt;`unknown`&gt;