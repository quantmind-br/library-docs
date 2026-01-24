---
title: Provenance attestations
url: https://docs.docker.com/build/metadata/attestations/slsa-provenance/
source: llms
fetched_at: 2026-01-24T14:17:07.945402207-03:00
rendered_js: false
word_count: 0
summary: This document provides a technical example of a SLSA provenance record for a Docker image build, detailing the build environment, materials, and execution steps performed by BuildKit.
tags:
    - slsa-provenance
    - in-toto
    - docker-build
    - buildkit
    - supply-chain-security
    - artifact-metadata
category: reference
---

```
{
  "_type": "https://in-toto.io/Statement/v0.1",
  "predicateType": "https://slsa.dev/provenance/v0.2",
  "subject": [
    {
      "name": "pkg:docker/<registry>/<image>@<tag/digest>?platform=<platform>",
      "digest": {
        "sha256": "e8275b2b76280af67e26f068e5d585eb905f8dfd2f1918b3229db98133cb4862"
      }
    }
  ],
  "predicate": {
    "builder": { "id": "" },
    "buildType": "https://mobyproject.org/buildkit@v1",
    "materials": [
      {
        "uri": "pkg:docker/docker/dockerfile@1",
        "digest": {
          "sha256": "9ba7531bd80fb0a858632727cf7a112fbfd19b17e94c4e84ced81e24ef1a0dbc"
        }
      },
      {
        "uri": "pkg:docker/golang@1.19.4-alpine?platform=linux%2Farm64",
        "digest": {
          "sha256": "a9b24b67dc83b3383d22a14941c2b2b2ca6a103d805cac6820fd1355943beaf1"
        }
      }
    ],
    "buildConfig": {
      "llbDefinition": [
        {
          "id": "step4",
          "op": {
            "Op": {
              "exec": {
                "meta": {
                  "args": ["/bin/sh", "-c", "go mod download -x"],
                  "env": [
                    "PATH=/go/bin:/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                    "GOLANG_VERSION=1.19.4",
                    "GOPATH=/go",
                    "CGO_ENABLED=0"
                  ],
                  "cwd": "/src"
                },
                "mounts": [
                  { "input": 0, "dest": "/", "output": 0 },
                  {
                    "input": -1,
                    "dest": "/go/pkg/mod",
                    "output": -1,
                    "mountType": 3,
                    "cacheOpt": { "ID": "//go/pkg/mod" }
                  },
                  {
                    "input": 1,
                    "selector": "/go.mod",
                    "dest": "/src/go.mod",
                    "output": -1,
                    "readonly": true
                  },
                  {
                    "input": 1,
                    "selector": "/go.sum",
                    "dest": "/src/go.sum",
                    "output": -1,
                    "readonly": true
                  }
                ]
              }
            },
            "platform": { "Architecture": "arm64", "OS": "linux" },
            "constraints": {}
          },
          "inputs": ["step3:0", "step1:0"]
        }
      ]
    },
    "metadata": {
      "buildInvocationID": "edf52vxjyf9b6o5qd7vgx0gru",
      "buildStartedOn": "2022-12-15T15:38:13.391980297Z",
      "buildFinishedOn": "2022-12-15T15:38:14.274565297Z",
      "reproducible": false,
      "completeness": {
        "parameters": true,
        "environment": true,
        "materials": false
      },
      "https://mobyproject.org/buildkit@v1#metadata": {
        "vcs": {
          "revision": "a9ba846486420e07d30db1107411ac3697ecab68-dirty",
          "source": "git@github.com:<org>/<repo>.git"
        },
        "source": {
          "locations": {
            "step4": {
              "locations": [
                {
                  "ranges": [
                    { "start": { "line": 5 }, "end": { "line": 5 } },
                    { "start": { "line": 6 }, "end": { "line": 6 } },
                    { "start": { "line": 7 }, "end": { "line": 7 } },
                    { "start": { "line": 8 }, "end": { "line": 8 } }
                  ]
                }
              ]
            }
          },
          "infos": [
            {
              "filename": "Dockerfile",
              "data": "RlJPTSBhbHBpbmU6bGF0ZXN0Cg==",
              "llbDefinition": [
                {
                  "id": "step0",
                  "op": {
                    "Op": {
                      "source": {
                        "identifier": "local://dockerfile",
                        "attrs": {
                          "local.differ": "none",
                          "local.followpaths": "[\"Dockerfile\",\"Dockerfile.dockerignore\",\"dockerfile\"]",
                          "local.session": "s4j58ngehdal1b5hn7msiqaqe",
                          "local.sharedkeyhint": "dockerfile"
                        }
                      }
                    },
                    "constraints": {}
                  }
                },
                { "id": "step1", "op": { "Op": null }, "inputs": ["step0:0"] }
              ]
            }
          ]
        },
        "layers": {
          "step2:0": [
            [
              {
                "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
                "digest": "sha256:261da4162673b93e5c0e7700a3718d40bcc086dbf24b1ec9b54bca0b82300626",
                "size": 3259190
              },
              {
                "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
                "digest": "sha256:bc729abf26b5aade3c4426d388b5ea6907fe357dec915ac323bb2fa592d6288f",
                "size": 286218
              },
              {
                "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
                "digest": "sha256:7f1d6579712341e8062db43195deb2d84f63b0f2d1ed7c3d2074891085ea1b56",
                "size": 116878653
              },
              {
                "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
                "digest": "sha256:652874aefa1343799c619d092ab9280b25f96d97939d5d796437e7288f5599c9",
                "size": 156
              }
            ]
          ]
        }
      }
    }
  }
}
```