---
title: Run your tests
url: https://docs.docker.com/guides/golang/run-tests/
source: llms
fetched_at: 2026-01-24T14:10:32.400600836-03:00
rendered_js: false
word_count: 188
summary: This guide explains how to incorporate Go unit tests into a multi-stage Docker build process using a specific test stage in the Dockerfile.
tags:
    - docker
    - golang
    - unit-testing
    - multi-stage-build
    - docker-build
    - go-test
category: guide
---

## Run your tests using Go test

## [Prerequisites](#prerequisites)

Complete the [Build your Go image](https://docs.docker.com/guides/golang/build-images/) section of this guide.

## [Overview](#overview)

Testing is an essential part of modern software development. Testing can mean a lot of things to different development teams. There are unit tests, integration tests and end-to-end testing. In this guide you take a look at running your unit tests in Docker when building.

For this section, use the `docker-gs-ping` project that you cloned in [Build your Go image](https://docs.docker.com/guides/golang/build-images/).

## [Run tests when building](#run-tests-when-building)

To run your tests when building, you need to add a test stage to the `Dockerfile.multistage`. The `Dockerfile.multistage` in the sample application's repository already has the following content:

```
# syntax=docker/dockerfile:1# Build the application from sourceFROMgolang:1.19ASbuild-stageWORKDIR/appCOPY go.mod go.sum ./RUN go mod downloadCOPY *.go ./RUN CGO_ENABLED=0 GOOS=linux go build -o /docker-gs-ping# Run the tests in the containerFROMbuild-stageASrun-test-stageRUN go test -v ./...# Deploy the application binary into a lean imageFROMgcr.io/distroless/base-debian11ASbuild-release-stageWORKDIR /COPY --from=build-stage /docker-gs-ping /docker-gs-pingEXPOSE8080USERnonroot:nonrootENTRYPOINT ["/docker-gs-ping"]
```

Run the following command to build an image using the `run-test-stage` stage as the target and view the test results. Include `--progress plain` to view the build output, `--no-cache` to ensure the tests always run, and `--target run-test-stage` to target the test stage.

```
$ docker build -f Dockerfile.multistage -t docker-gs-ping-test --progress plain --no-cache --target run-test-stage .
```

You should see output containing the following.

```
#13 [run-test-stage 1/1] RUN go test -v ./...
#13 4.915 === RUN   TestIntMinBasic
#13 4.915 --- PASS: TestIntMinBasic (0.00s)
#13 4.915 === RUN   TestIntMinTableDriven
#13 4.915 === RUN   TestIntMinTableDriven/0,1
#13 4.915 === RUN   TestIntMinTableDriven/1,0
#13 4.915 === RUN   TestIntMinTableDriven/2,-2
#13 4.915 === RUN   TestIntMinTableDriven/0,-1
#13 4.915 === RUN   TestIntMinTableDriven/-1,0
#13 4.915 --- PASS: TestIntMinTableDriven (0.00s)
#13 4.915     --- PASS: TestIntMinTableDriven/0,1 (0.00s)
#13 4.915     --- PASS: TestIntMinTableDriven/1,0 (0.00s)
#13 4.915     --- PASS: TestIntMinTableDriven/2,-2 (0.00s)
#13 4.915     --- PASS: TestIntMinTableDriven/0,-1 (0.00s)
#13 4.915     --- PASS: TestIntMinTableDriven/-1,0 (0.00s)
#13 4.915 PASS
```

## [Next steps](#next-steps)

In this section, you learned how to run tests when building your image. Next, you’ll learn how to set up a CI/CD pipeline using GitHub Actions.