---
title: docker node inspect
url: https://docs.docker.com/reference/cli/docker/node/inspect/
source: llms
fetched_at: 2026-01-24T14:39:10.350950597-03:00
rendered_js: false
word_count: 0
summary: Provides a structural representation of a Docker Swarm node, detailing its configuration, hardware resources, engine plugins, and cluster management status.
tags:
    - docker-swarm
    - node-metadata
    - container-orchestration
    - api-response
    - cluster-management
category: reference
---

```
[
  {
    "ID": "e216jshn25ckzbvmwlnh5jr3g",
    "Version": {
      "Index": 10
    },
    "CreatedAt": "2017-05-16T22:52:44.9910662Z",
    "UpdatedAt": "2017-05-16T22:52:45.230878043Z",
    "Spec": {
      "Role": "manager",
      "Availability": "active"
    },
    "Description": {
      "Hostname": "swarm-manager",
      "Platform": {
        "Architecture": "x86_64",
        "OS": "linux"
      },
      "Resources": {
        "NanoCPUs": 1000000000,
        "MemoryBytes": 1039843328
      },
      "Engine": {
        "EngineVersion": "17.06.0-ce",
        "Plugins": [
          {
            "Type": "Volume",
            "Name": "local"
          },
          {
            "Type": "Network",
            "Name": "overlay"
          },
          {
            "Type": "Network",
            "Name": "null"
          },
          {
            "Type": "Network",
            "Name": "host"
          },
          {
            "Type": "Network",
            "Name": "bridge"
          },
          {
            "Type": "Network",
            "Name": "overlay"
          }
        ]
      },
      "TLSInfo": {
        "TrustRoot": "-----BEGIN CERTIFICATE-----\nMIIBazCCARCgAwIBAgIUOzgqU4tA2q5Yv1HnkzhSIwGyIBswCgYIKoZIzj0EAwIw\nEzERMA8GA1UEAxMIc3dhcm0tY2EwHhcNMTcwNTAyMDAyNDAwWhcNMzcwNDI3MDAy\nNDAwWjATMREwDwYDVQQDEwhzd2FybS1jYTBZMBMGByqGSM49AgEGCCqGSM49AwEH\nA0IABMbiAmET+HZyve35ujrnL2kOLBEQhFDZ5MhxAuYs96n796sFlfxTxC1lM/2g\nAh8DI34pm3JmHgZxeBPKUURJHKWjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMB\nAf8EBTADAQH/MB0GA1UdDgQWBBS3sjTJOcXdkls6WSY2rTx1KIJueTAKBggqhkjO\nPQQDAgNJADBGAiEAoeVWkaXgSUAucQmZ3Yhmx22N/cq1EPBgYHOBZmHt0NkCIQC3\nzONcJ/+WA21OXtb+vcijpUOXtNjyHfcox0N8wsLDqQ==\n-----END CERTIFICATE-----\n",
        "CertIssuerSubject": "MBMxETAPBgNVBAMTCHN3YXJtLWNh",
        "CertIssuerPublicKey": "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAExuICYRP4dnK97fm6OucvaQ4sERCEUNnkyHEC5iz3qfv3qwWV/FPELWUz/aACHwMjfimbcmYeBnF4E8pRREkcpQ=="
      }
    },
    "Status": {
      "State": "ready",
      "Addr": "168.0.32.137"
    },
    "ManagerStatus": {
      "Leader": true,
      "Reachability": "reachable",
      "Addr": "168.0.32.137:2377"
    }
  }
]
```