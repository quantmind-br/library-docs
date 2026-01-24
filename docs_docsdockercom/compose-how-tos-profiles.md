---
title: Use service profiles
url: https://docs.docker.com/compose/how-tos/profiles/
source: llms
fetched_at: 2026-01-24T14:17:49.301799034-03:00
rendered_js: false
word_count: 530
summary: This document explains how to use Docker Compose profiles to selectively enable or disable services for different environments or use cases. It covers profile assignment in configuration files and methods for activating profiles via the command line or environment variables.
tags:
    - docker-compose
    - profiles
    - service-management
    - environment-configuration
    - cli-options
    - orchestration
category: guide
---

## Using profiles with Compose

Profiles help you adjust your Compose application for different environments or use cases by selectively activating services. Services can be assigned to one or more profiles; unassigned services start/stop by default, while assigned ones only start/stop when their profile is active. This setup means specific services, like those for debugging or development, to be included in a single `compose.yml` file and activated only as needed.

Services are associated with profiles through the [`profiles` attribute](https://docs.docker.com/reference/compose-file/services/#profiles) which takes an array of profile names:

Here the services `frontend` and `phpmyadmin` are assigned to the profiles `frontend` and `debug` respectively and as such are only started when their respective profiles are enabled.

Services without a `profiles` attribute are always enabled. In this case running `docker compose up` would only start `backend` and `db`.

Valid profiles names follow the regex format of `[a-zA-Z0-9][a-zA-Z0-9_.-]+`.

> The core services of your application shouldn't be assigned `profiles` so they are always enabled and automatically started.

To start a specific profile supply the `--profile` [command-line option](https://docs.docker.com/reference/cli/docker/compose/) or use the [`COMPOSE_PROFILES` environment variable](https://docs.docker.com/compose/how-tos/environment-variables/envvars/#compose_profiles):

Both commands start the services with the `debug` profile enabled. In the previous `compose.yaml` file, this starts the services `db`, `backend` and `phpmyadmin`.

### [Start multiple profiles](#start-multiple-profiles)

You can also enable multiple profiles, e.g. with `docker compose --profile frontend --profile debug up` the profiles `frontend` and `debug` will be enabled.

Multiple profiles can be specified by passing multiple `--profile` flags or a comma-separated list for the `COMPOSE_PROFILES` environment variable:

If you want to enable all profiles at the same time, you can run `docker compose --profile "*"`.

When you explicitly target a service on the command line that has one or more profiles assigned, you do not need to enable the profile manually as Compose runs that service regardless of whether its profile is activated. This is useful for running one-off services or debugging tools.

Only the targeted service (and any of its declared dependencies via `depends_on`) is started. Other services that share the same profile will not be started unless:

- They are also explicitly targeted, or
- The profile is explicitly enabled using `--profile` or `COMPOSE_PROFILES`.

When a service with assigned `profiles` is explicitly targeted on the command line its profiles are started automatically so you don't need to start them manually. This can be used for one-off services and debugging tools. As an example consider the following configuration:

In this example, `db-migrations` runs even though it is assigned to the tools profile, because it was explicitly targeted. The `db` service is also started automatically because it is listed in `depends_on`.

If the targeted service has dependencies that are also gated behind a profile, you must ensure those dependencies are either:

- In the same profile
- Started separately
- Not assigned to any profile so are always enabled

As with starting specific profiles, you can use the `--profile` [command-line option](https://docs.docker.com/reference/cli/docker/compose/#use--p-to-specify-a-project-name) or use the [`COMPOSE_PROFILES` environment variable](https://docs.docker.com/compose/how-tos/environment-variables/envvars/#compose_profiles):

Both commands stop and remove services with the `debug` profile and services without a profile. In the following `compose.yaml` file, this stops the services `db`, `backend` and `phpmyadmin`.

if you only want to stop the `phpmyadmin` service, you can run

or

> Running `docker compose down` only stops `backend` and `db`.

[`profiles`](https://docs.docker.com/reference/compose-file/services/#profiles)