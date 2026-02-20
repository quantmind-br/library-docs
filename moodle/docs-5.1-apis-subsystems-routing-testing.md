---
title: Unit Testing | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/subsystems/routing/testing
source: sitemap
fetched_at: 2026-02-17T15:37:16.902233-03:00
rendered_js: false
word_count: 501
summary: This document explains how to unit test routes in Moodle by extending the route_testcase class and using helper methods to mock route loaders and handle server requests. It covers setting up a simplified router environment and processing individual or grouped API requests for validation.
tags:
    - moodle-development
    - unit-testing
    - routing-api
    - phpunit
    - mock-objects
    - server-requests
    - test-case-class
category: guide
---

One of the benefits of using routes is how easy they are to unit test. It is also possible to test [parameters](https://moodledev.io/docs/5.1/apis/subsystems/routing/parameters) for validation, which is especially useful for [mapped parameters](https://moodledev.io/docs/5.1/apis/subsystems/routing/parameters#mapped-parameters).

## The `\route_testcase` testcase class[​](#the-route_testcase-testcase-class "Direct link to the-route_testcase-testcase-class")

When testing routes your test should extend the `\route_testcase` base testcase, which is loaded as part of the PHPUnit Bootstrap.

This testcase provides a number of helper methods to create environments to test your routes.

When unit testing code it is usually desirable to test only your code without all of the additional unrelated code typically included in the setup of routes. To make this easier the testcase includes methods to create a simplified router, to add one or more routes from a class, to create requests, and to route requests through the router to the relevant route.

## Creating a simplified app[​](#creating-a-simplified-app "Direct link to Creating a simplified app")

You can quickly and easily create a copy of the Moodle Router using the `route_testcase::get_router()` method.

This is a fully-configured copy of the Moodle Router, and allows to handle requests directly.

```
finalclassmy_testextends\route_testcase{
publicfunctiontest_example():void{
$router=$this->get_router();
}
}
```

note

This router contains *all* possible routes in Moodle. When writing unit tests it is typically advisable to only include the routes that you wish to test.

## Specifying routes to include[​](#specifying-routes-to-include "Direct link to Specifying routes to include")

When calling `get_router()` the Router will use [Dependency Injection](https://moodledev.io/docs/5.1/apis/core/di) to inject all dependencies of the router. Amongst these dependencies is an implementation of the `\core\router\route_loader_interface`. The default implementation of this is the `\core\route\route_loader`.

Moodle also provides a `mocking_route_loader` which can be used in unit tests to either create completely new mocked routes, or to load existing routes from disk.

When using the mocking route loader only those routes that you explicitly add will be included.

Ordering

Because the router uses DI to inject routes during its initialisation, all routes must be mocked before calling `get_router()` or related methods.

### Adding existing routes[​](#adding-existing-routes "Direct link to Adding existing routes")

You can easily add existing routes to mocking route loader either individually, or by including all routes in a class.

To add an individual route, you can use the `\route_testcase::add_route_to_route_loader()` method, for example:

Adding a single route to the route loader

```
finalclassmy_testextends\route_testcase{
publicfunctiontest_example():void{
$this->add_route_to_route_loader(
my_route::class,
'my_route_method',
);

$router=$this->get_router();
}
}
```

You can also add all routes in a class to the route loader using the `\route_testcase::add_class_routes_to_route_loader()` method, for example:

Adding all routes in a class to the route loader

```
finalclassmy_testextends\route_testcase{
publicfunctiontest_example():void{
$this->add_class_routes_to_route_loader(
my_route::class,
);

$router=$this->get_router();
}
}

```

### Using the app to handle a request[​](#using-the-app-to-handle-a-request "Direct link to Using the app to handle a request")

The `\route_testcase` also includes several methods to simplify generating a Request object, and having routing it within the Router.

You can create a request and manually pass it to Router using the `\route_testcase::create_request()` method, for example:

Creating an example request and processing it

```
publicfunctiontest_example():void{
$this->add_class_routes_to_route_loader(
my_route::class,
);

$router=$this->get_router();

// Create the ServerRequest.
$request=$this->create_request('GET','/path/to/route',route_loader_interface::ROUTE_GROUP_API);

// Pass the request into the App and process it through all Middleware.
$response=$router->get_app()->handle($request);
}
```

Request Groups

When creating a request the default is to use the Route Group for the REST API, but any valid `ROUTE_GROUP` is supported.

The `\route_testcase::process_request()` and `\route_testcsae::process_api_request()` methods act as a shortcut for creating the request, fetching the router, and the app, and handling the request to return a response. The above example can therefore be simplified to:

Creating and processing an example request

```
publicfunctiontest_example():void{
$this->add_class_routes_to_route_loader(
my_route::class,
);

$response=$this->process_api_request('GET','/path/to/route');
}
```

All of these methods also accept:

- any headers to provide with your request
- any query parameters