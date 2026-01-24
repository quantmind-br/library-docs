---
title: Connecting services with Docker Compose
url: https://docs.docker.com/guides/go-prometheus-monitoring/compose/
source: llms
fetched_at: 2026-01-24T14:04:56.52016851-03:00
rendered_js: false
word_count: 817
---

Now that you have containerized the Golang application, you will use Docker Compose to connect your services together. You will connect the Golang application, Prometheus, and Grafana services together to monitor the Golang application with Prometheus and Grafana.

Create a new file named `compose.yml` in the root directory of your Golang application. The Docker Compose file contains instructions to run multiple services and connect them together.

Here is a Docker Compose file for a project that uses Golang, Prometheus, and Grafana. You will also find this file in the `go-prometheus-monitoring` directory.

The Docker Compose file consists of three services:

- **Golang application service**: This service builds the Golang application using the Dockerfile and runs it in a container. It exposes the application's port `8000` and connects to the `go-network` network. It also defines a health check to monitor the application's health. You have also used `healthcheck` to monitor the health of the application. The health check runs every 30 seconds and retries 5 times if the health check fails. The health check uses the `curl` command to check the `/health` endpoint of the application. Apart from the health check, you have also added a `develop` section to watch the changes in the application's source code and rebuild the application using the Docker Compose Watch feature.
- **Prometheus service**: This service runs the Prometheus server in a container. It uses the official Prometheus image `prom/prometheus:v2.55.0`. It exposes the Prometheus server on port `9090` and connects to the `go-network` network. You have also mounted the `prometheus.yml` file from the `Docker` directory which is present in the root directory of your project. The `prometheus.yml` file contains the Prometheus configuration to scrape the metrics from the Golang application. This is how you connect the Prometheus server to the Golang application.
  
  In the `prometheus.yml` file, you have defined a job named `myapp` to scrape the metrics from the Golang application. The `targets` field specifies the target to scrape the metrics from. In this case, the target is the Golang application running on port `8000`. The `api` is the service name of the Golang application in the Docker Compose file. The Prometheus server will scrape the metrics from the Golang application every 10 seconds.
- **Grafana service**: This service runs the Grafana server in a container. It uses the official Grafana image `grafana/grafana:11.3.0`. It exposes the Grafana server on port `3000` and connects to the `go-network` network. You have also mounted the `grafana.yml` file from the `Docker` directory which is present in the root directory of your project. The `grafana.yml` file contains the Grafana configuration to add the Prometheus data source. This is how you connect the Grafana server to the Prometheus server. In the environment variables, you have set the Grafana admin user and password, which will be used to log in to the Grafana dashboard.
  
  In the `grafana.yml` file, you have defined a Prometheus data source named `Prometheus (Main)`. The `type` field specifies the type of the data source, which is `prometheus`. The `url` field specifies the URL of the Prometheus server to fetch the metrics from. In this case, the URL is `http://prometheus:9090`. `prometheus` is the service name of the Prometheus server in the Docker Compose file. The `isDefault` field specifies whether the data source is the default data source in Grafana.

Apart from the services, the Docker Compose file also defines a volume named `grafana-data` to persist the Grafana data and a network named `go-network` to connect the services together. You have created a custom network `go-network` to connect the services together. The `driver: bridge` field specifies the network driver to use for the network.

Now that you have the Docker Compose file, you can build the services and run them together using Docker Compose.

To build and run the services, run the following command in the terminal:

The `docker compose up` command builds the services defined in the Docker Compose file and runs them together. You will see the similar output in the terminal:

The services will start running, and you can access the Golang application at `http://localhost:8000`, Prometheus at `http://localhost:9090/health`, and Grafana at `http://localhost:3000`. You can also check the running containers using the `docker ps` command.

In this section, you learned how to connect services together using Docker Compose. You created a Docker Compose file to run multiple services together and connect them using networks. You also learned how to build and run the services using Docker Compose.

Related information:

- [Docker Compose overview](https://docs.docker.com/compose/)
- [Compose file reference](https://docs.docker.com/reference/compose-file/)

Next, you will learn how to develop the Golang application with Docker Compose and monitor it with Prometheus and Grafana.

In the next section, you will learn how to develop the Golang application with Docker. You will also learn how to use Docker Compose Watch to rebuild the image whenever you make changes to the code. Lastly, you will test the application and visualize the metrics in Grafana using Prometheus as the data source.