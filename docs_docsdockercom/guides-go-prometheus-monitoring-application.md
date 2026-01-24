---
title: Understand the application
url: https://docs.docker.com/guides/go-prometheus-monitoring/application/
source: llms
fetched_at: 2026-01-24T14:04:56.874551957-03:00
rendered_js: false
word_count: 710
---

## Building the application

- You have a [Git client](https://git-scm.com/downloads). The examples in this section use a command-line based Git client, but you can use any client.

You will be creating a Golang server with some endpoints to simulate a real-world application. Then you will expose metrics from the server using Prometheus.

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:

Once you cloned you will see the following content structure inside `go-prometheus-monitoring` directory,

- **main.go** - The entry point of the application.
- **go.mod and go.sum** - Go module files.
- **Dockerfile** - Dockerfile used to build the app.
- **Docker/** - Contains the Docker Compose configuration files for Grafana and Prometheus.
- **compose.yaml** - Compose file to launch everything (Golang app, Prometheus, and Grafana).
- **dashboard.json** - Grafana dashboard configuration file.
- **Dockerfile** - Dockerfile used to build the Golang app.
- **compose.yaml** - Docker Compose file to launch everything (Golang app, Prometheus, and Grafana).
- Other files are for licensing and documentation purposes.

The following is the complete logic of the application you will find in `main.go`.

In this part of the code, you have imported the required packages `gin`, `prometheus`, and `promhttp`. Then you have defined a couple of variables, `HttpRequestTotal` and `HttpRequestErrorTotal` are Prometheus counter metrics, and `customRegistry` is a custom registry that will be used to register these metrics. The name of the metric is a string that you can use to identify the metric. The help string is a string that will be shown when you query the `/metrics` endpoint to understand the metric. The reason you are using the custom registry is so avoid the default Go metrics that are registered by default by the Prometheus client. Then using the `init` function you are registering the metrics with the custom registry.

In the `main` function, you have created a new instance of the `gin` framework and created three routes. You can see the health endpoint that is on path `/health` that will return a JSON with `{"message": "Up and running!"}` and the `/v1/users` endpoint that will return a JSON with `{"message": "Hello from /v1/users"}`. The third route is for the `/metrics` endpoint that will return the metrics in the Prometheus format. Then you have `RequestMetricsMiddleware` middleware, it will be called for every request made to the API. It will record the incoming requests metrics like status codes and paths. Finally, you are running the gin application on port 8000.

Now comes the middleware function `RequestMetricsMiddleware`. This function is called for every request made to the API. It increments the `HttpRequestTotal` counter (different counter for different paths and status codes) if the status code is less than or equal to 400. If the status code is greater than 400, it increments the `HttpRequestErrorTotal` counter (different counter for different paths and status codes). The `PrometheusHandler` function is the custom handler that will be called for the `/metrics` endpoint. It will return the metrics in the Prometheus format.

That's it, this was the complete gist of the application. Now it's time to run and test if the app is registering metrics correctly.

Make sure you are still inside `go-prometheus-monitoring` directory in the terminal, and run the following command. Install the dependencies by running `go mod tidy` and then build and run the application by running `go run main.go`. Then visit `http://localhost:8000/health` or `http://localhost:8000/v1/users`. You should see the output `{"message": "Up and running!"}` or `{"message": "Hello from /v1/users"}`. If you are able to see this then your app is successfully up and running.

Now, check your application's metrics by accessing the `/metrics` endpoint. Open `http://localhost:8000/metrics` in your browser. You should see similar output to the following.

In the terminal, press `ctrl` + `c` to stop the application.

> If you don't want to run the application locally, and want to run it in a Docker container, skip to next page where you create a Dockerfile and containerize the application.

In this section, you learned how to create a Golang app to register metrics with Prometheus. By implementing middleware functions, you were able to increment the counters based on the request path and status codes.

In the next section, you'll learn how to containerize your application.