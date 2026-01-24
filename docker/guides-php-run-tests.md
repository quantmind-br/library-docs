---
title: Run your tests
url: https://docs.docker.com/guides/php/run-tests/
source: llms
fetched_at: 2026-01-24T14:11:08.481640581-03:00
rendered_js: false
word_count: 256
summary: This document explains how to run PHPUnit tests within Docker containers during both the local development phase and the image build process using multi-stage builds.
tags:
    - php
    - docker
    - phpunit
    - testing
    - docker-compose
    - multi-stage-build
    - containerization
category: guide
---

## Run PHP tests in a container

## [Prerequisites](#prerequisites)

Complete all the previous sections of this guide, starting with [Containerize a PHP application](https://docs.docker.com/guides/php/containerize/).

## [Overview](#overview)

Testing is an essential part of modern software development. Testing can mean a lot of things to different development teams. There are unit tests, integration tests and end-to-end testing. In this guide you take a look at running your unit tests in Docker when developing and when building.

## [Run tests when developing locally](#run-tests-when-developing-locally)

The sample application already has a PHPUnit test inside the `tests` directory. When developing locally, you can use Compose to run your tests.

Run the following command in the `docker-php-sample` directory to run the tests inside a container.

```
$ docker compose run --build --rm server ./vendor/bin/phpunit tests/HelloWorldTest.php
```

You should see output that contains the following.

```
Hello, Docker!PHPUnit 9.6.13 by Sebastian Bergmann and contributors.
.                                                                   1 / 1 (100%)
Time: 00:00.003, Memory: 4.00 MB
OK (1 test, 1 assertion)
```

To learn more about the command, see [docker compose run](https://docs.docker.com/reference/cli/docker/compose/run/).

## [Run tests when building](#run-tests-when-building)

To run your tests when building, you need to update your Dockerfile. Create a new test stage that runs the tests.

The following is the updated Dockerfile.

```
# syntax=docker/dockerfile:1FROMcomposer:ltsasprod-depsWORKDIR/appRUN --mount=type=bind,source=./composer.json,target=composer.json \
    --mount=type=bind,source=./composer.lock,target=composer.lock \
    --mount=type=cache,target=/tmp/cache \
    composer install --no-dev --no-interactionFROMcomposer:ltsasdev-depsWORKDIR/appRUN --mount=type=bind,source=./composer.json,target=composer.json \
    --mount=type=bind,source=./composer.lock,target=composer.lock \
    --mount=type=cache,target=/tmp/cache \
    composer install --no-interactionFROMphp:8.2-apacheasbaseRUN docker-php-ext-install pdo pdo_mysqlCOPY ./src /var/www/htmlFROMbaseasdevelopmentCOPY ./tests /var/www/html/testsRUN mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"COPY --from=dev-deps app/vendor/ /var/www/html/vendorFROMdevelopmentastestWORKDIR/var/www/htmlRUN ./vendor/bin/phpunit tests/HelloWorldTest.phpFROMbaseasfinalRUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"COPY --from=prod-deps app/vendor/ /var/www/html/vendorUSERwww-data
```

Run the following command to build an image using the test stage as the target and view the test results. Include `--progress plain` to view the build output, `--no-cache` to ensure the tests always run, and `--target test` to target the test stage.

```
$ docker build -t php-docker-image-test --progress plain --no-cache --target test .
```

You should see output containing the following.

```
#18 [test 2/2] RUN ./vendor/bin/phpunit tests/HelloWorldTest.php
#18 0.385 Hello, Docker!PHPUnit 9.6.13 by Sebastian Bergmann and contributors.
#18 0.392
#18 0.394 .                                                                   1 / 1 (100%)
#18 0.395
#18 0.395 Time: 00:00.003, Memory: 4.00 MB
#18 0.395
#18 0.395 OK (1 test, 1 assertion)
```

## [Summary](#summary)

In this section, you learned how to run tests when developing locally using Compose and how to run tests when building your image.

Related information:

- [docker compose run](https://docs.docker.com/reference/cli/docker/compose/run/)

## [Next steps](#next-steps)

Next, you’ll learn how to set up a CI/CD pipeline using GitHub Actions.