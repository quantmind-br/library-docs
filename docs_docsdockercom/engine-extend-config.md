---
title: Plugin Config Version 1 of Plugin V2
url: https://docs.docker.com/engine/extend/config/
source: llms
fetched_at: 2026-01-24T14:23:15.354390505-03:00
rendered_js: false
word_count: 0
summary: This document defines the configuration schema for a Docker volume plugin, detailing its runtime parameters, environment variables, and interface specifications.
tags:
    - docker-plugin
    - volume-driver
    - container-storage
    - plugin-config
    - json-manifest
category: configuration
---

```
{
  "Args": {
    "Description": "",
    "Name": "",
    "Settable": null,
    "Value": null
  },
  "Description": "A sample volume plugin for Docker",
  "Documentation": "https://docs.docker.com/engine/extend/plugins/",
  "Entrypoint": [
    "/usr/bin/sample-volume-plugin",
    "/data"
  ],
  "Env": [
    {
      "Description": "",
      "Name": "DEBUG",
      "Settable": [
        "value"
      ],
      "Value": "0"
    }
  ],
  "Interface": {
    "Socket": "plugin.sock",
    "Types": [
      "docker.volumedriver/1.0"
    ]
  },
  "Linux": {
    "Capabilities": null,
    "AllowAllDevices": false,
    "Devices": null
  },
  "Mounts": null,
  "Network": {
    "Type": ""
  },
  "PropagatedMount": "/data",
  "User": {},
  "Workdir": ""
}
```