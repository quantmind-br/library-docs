---
title: Inspect a service on the swarm
url: https://docs.docker.com/engine/swarm/swarm-tutorial/inspect-service/
source: llms
fetched_at: 2026-01-24T14:26:15.730172072-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates the output of the docker service inspect command, detailing the configuration, task templates, and runtime state of a Docker Swarm service.
tags:
    - docker
    - swarm-mode
    - docker-service
    - service-inspection
    - cli-reference
category: reference
---

```
[manager1]$ docker service inspect helloworld
[
{
    "ID": "9uk4639qpg7npwf3fn2aasksr",
    "Version": {
        "Index": 418
    },
    "CreatedAt": "2016-06-16T21:57:11.622222327Z",
    "UpdatedAt": "2016-06-16T21:57:11.622222327Z",
    "Spec": {
        "Name": "helloworld",
        "TaskTemplate": {
            "ContainerSpec": {
                "Image": "alpine",
                "Args": [
                    "ping",
                    "docker.com"
                ]
            },
            "Resources": {
                "Limits": {},
                "Reservations": {}
            },
            "RestartPolicy": {
                "Condition": "any",
                "MaxAttempts": 0
            },
            "Placement": {}
        },
        "Mode": {
            "Replicated": {
                "Replicas": 1
            }
        },
        "UpdateConfig": {
            "Parallelism": 1
        },
        "EndpointSpec": {
            "Mode": "vip"
        }
    },
    "Endpoint": {
        "Spec": {}
    }
}
]
```