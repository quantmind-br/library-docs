---
title: docker buildx imagetools inspect
url: https://docs.docker.com/reference/cli/docker/buildx/imagetools/inspect/
source: llms
fetched_at: 2026-01-24T14:33:24.467433569-03:00
rendered_js: false
word_count: 0
summary: An OCI Image Index manifest that defines a list of image manifests for different hardware architectures and operating systems.
tags:
    - oci-image-index
    - container-manifest
    - multi-platform
    - oci-spec
    - json-schema
category: reference
---

```
{
  "schemaVersion": 2,
  "mediaType": "application/vnd.oci.image.index.v1+json",
  "digest": "sha256:d895e8fdcf5e2bb39acb5966f97fc4cd87a2d13d27c939c320025eb4aca5440c",
  "size": 4654,
  "manifests": [
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:ac9dd4fbec9e36b562f910618975a2936533f8e411a3fea2858aacc0ac972e1c",
      "size": 1054,
      "platform": {
        "architecture": "amd64",
        "os": "linux"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:0f4dc6797db467372cbf52c7236816203654a839f64a6542c9135d1973c9d744",
      "size": 1054,
      "platform": {
        "architecture": "arm",
        "os": "linux",
        "variant": "v7"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:d62bb533d95afe17c4a9caf1e7c57a3b0a7a67409ccfa7af947aeb0f670ffb87",
      "size": 1054,
      "platform": {
        "architecture": "arm64",
        "os": "linux"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:b4944057e0c68203cdcc3dceff3b2df3c7d9e3dd801724fa977b01081da7771e",
      "size": 1054,
      "platform": {
        "architecture": "s390x",
        "os": "linux"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:825702a51eb4234904fc9253d8b0bf0a584787ffd8fc3fd6fa374188233ce399",
      "size": 1054,
      "platform": {
        "architecture": "ppc64le",
        "os": "linux"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:dfb27c6acc9b9f3a7c9d47366d137089565062f43c8063c9f5e408d34c87ee4a",
      "size": 1054,
      "platform": {
        "architecture": "riscv64",
        "os": "linux"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:f2fe69bccc878e658caf21dfc99eaf726fb20d28f17398c1d66a90e62cc019f9",
      "size": 1113,
      "annotations": {
        "vnd.docker.reference.digest": "sha256:ac9dd4fbec9e36b562f910618975a2936533f8e411a3fea2858aacc0ac972e1c",
        "vnd.docker.reference.type": "attestation-manifest"
      },
      "platform": {
        "architecture": "unknown",
        "os": "unknown"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:9e112f8d4e383186f36369fba7b454e246d2e9ca5def797f1b84ede265e9f3ca",
      "size": 1113,
      "annotations": {
        "vnd.docker.reference.digest": "sha256:0f4dc6797db467372cbf52c7236816203654a839f64a6542c9135d1973c9d744",
        "vnd.docker.reference.type": "attestation-manifest"
      },
      "platform": {
        "architecture": "unknown",
        "os": "unknown"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:09d593587f8665269ec6753eaed7fbdb09968f71587dd53e06519502cbc16775",
      "size": 1113,
      "annotations": {
        "vnd.docker.reference.digest": "sha256:d62bb533d95afe17c4a9caf1e7c57a3b0a7a67409ccfa7af947aeb0f670ffb87",
        "vnd.docker.reference.type": "attestation-manifest"
      },
      "platform": {
        "architecture": "unknown",
        "os": "unknown"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:985a3f4544dfb042db6a8703f5f76438667dd7958aba14cb04bebe3b4cbd9307",
      "size": 1113,
      "annotations": {
        "vnd.docker.reference.digest": "sha256:b4944057e0c68203cdcc3dceff3b2df3c7d9e3dd801724fa977b01081da7771e",
        "vnd.docker.reference.type": "attestation-manifest"
      },
      "platform": {
        "architecture": "unknown",
        "os": "unknown"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:cfccb6afeede7dc29bf8abef4815d56f2723fa482ea63c9cd519cd991c379294",
      "size": 1113,
      "annotations": {
        "vnd.docker.reference.digest": "sha256:825702a51eb4234904fc9253d8b0bf0a584787ffd8fc3fd6fa374188233ce399",
        "vnd.docker.reference.type": "attestation-manifest"
      },
      "platform": {
        "architecture": "unknown",
        "os": "unknown"
      }
    },
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:2e93733432c6a14cb57db33928b3a17d7ca298b3babe24d9f56dca2754dbde3b",
      "size": 1113,
      "annotations": {
        "vnd.docker.reference.digest": "sha256:dfb27c6acc9b9f3a7c9d47366d137089565062f43c8063c9f5e408d34c87ee4a",
        "vnd.docker.reference.type": "attestation-manifest"
      },
      "platform": {
        "architecture": "unknown",
        "os": "unknown"
      }
    }
  ]
}
```