---
title: Image attestation storage
url: https://docs.docker.com/build/metadata/attestations/attestation-storage/
source: llms
fetched_at: 2026-01-24T14:17:05.312238119-03:00
rendered_js: false
word_count: 560
summary: This document defines the technical specification for storing Buildkit attestations, such as SBOMs and SLSA provenance, within OCI image indexes for registry compatibility.
tags:
    - buildkit
    - attestations
    - oci-artifacts
    - sbom
    - in-toto
    - container-security
    - image-manifest
category: reference
---

Buildkit supports creating and attaching attestations to build artifacts. These attestations can provide valuable information from the build process, including, but not limited to: [SBOMs](https://en.wikipedia.org/wiki/Software_supply_chain), [SLSA Provenance](https://slsa.dev/provenance), build logs, etc.

This document describes the current custom format used to store attestations, which is designed to be compatible with current registry implementations today. In the future, we may support exporting attestations in additional formats.

Attestations are stored as manifest objects in the image index, similar in style to OCI artifacts.

### [Attestation Manifest](#attestation-manifest)

Attestation manifests are attached to the root image index object, under a separate [OCI image manifest](https://github.com/opencontainers/image-spec/blob/main/manifest.md). Each attestation manifest can contain multiple [attestation blobs](#attestation-blob), with all the of the attestations in a manifest applying to a single platform manifest. All properties of standard OCI and Docker manifests continue to apply.

The image `config` descriptor will point to a valid [image config](https://github.com/opencontainers/image-spec/blob/main/config.md), however, it will not contain attestation-specific details, and should be ignored as it is only included for compatibility purposes.

Each image layer in `layers` will contain a descriptor for a single [attestation blob](#attestation-blob). The `mediaType` of each layer will be set in accordance to its contents, one of:

- `application/vnd.in-toto+json` (currently, the only supported option)
  
  Indicates an in-toto attestation blob

Any unknown `mediaType`s should be ignored.

To assist attestation traversal, the following annotations may be set on each layer descriptor:

- `in-toto.io/predicate-type`
  
  This annotation will be set if the enclosed attestation is an in-toto attestation (currently, the only supported option). The annotation will be set to contain the same value as the `predicateType` property present inside the attestation.
  
  When present, this annotation may be used to find the specific attestation(s) they are looking for to avoid pulling the contents of the others.

### [Attestation Blob](#attestation-blob)

The contents of each layer will be a blob dependent on its `mediaType`.

- `application/vnd.in-toto+json`
  
  The blob contents will contain a full [in-toto attestation statement](https://github.com/in-toto/attestation/blob/main/spec/README.md#statement):
  
  The subject of the attestation should be set to be the same digest as the target manifest described in the [Attestation Manifest Descriptor](#attestation-manifest-descriptor), or some object within.

### [Attestation Manifest Descriptor](#attestation-manifest-descriptor)

Attestation manifests are attached to the root [image index](https://github.com/opencontainers/image-spec/blob/main/image-index.md), in the `manifests` key, after all the original runnable manifests. All properties of standard OCI and Docker manifest descriptors continue to apply.

To prevent container runtimes from accidentally pulling or running the image described in the manifest, the `platform` property of the attestation manifest will be set to `unknown/unknown`, as follows:

To assist index traversal, the following annotations will be set on the manifest descriptor descriptor:

- `vnd.docker.reference.type`
  
  This annotation describes the type of the artifact, and will be set to `attestation-manifest`. If any other value is specified, the entire manifest should be ignored.
- `vnd.docker.reference.digest`
  
  This annotation will contain the digest of the object in the image index that the attestation manifest refers to.
  
  When present, this annotation can be used to find the matching attestation manifest for a selected image manifest.

*Example showing an SBOM attestation attached to a `linux/amd64` image*

#### [Image index (`sha256:94acc2ca70c40f3f6291681f37ce9c767e3d251ce01c7e4e9b98ccf148c26260`):](#image-index-sha25694acc2ca70c40f3f6291681f37ce9c767e3d251ce01c7e4e9b98ccf148c26260)

This image index defines two descriptors: an AMD64 image `sha256:23678f31..` and an attestation manifest `sha256:02cb9aa7..` for that image.

#### [Attestation manifest (`sha256:02cb9aa7600e73fcf41ee9f0f19cc03122b2d8be43d41ce4b21335118f5dd943`):](#attestation-manifest-sha25602cb9aa7600e73fcf41ee9f0f19cc03122b2d8be43d41ce4b21335118f5dd943)

This attestation manifest contains one attestation that is an in-toto attestation that contains a "https://spdx.dev/Document" predicate, signifying that it is defining a SBOM for the image.

#### [Image config (`sha256:a781560066f20ec9c28f2115a95a886e5e71c7c7aa9d8fd680678498b82f3ea3`):](#image-config-sha256a781560066f20ec9c28f2115a95a886e5e71c7c7aa9d8fd680678498b82f3ea3)

#### [Layer content (`sha256:1ea07d5e55eb47ad0e6bbfa2ec180fb580974411e623814e519064c88f022f5c`):](#layer-content-sha2561ea07d5e55eb47ad0e6bbfa2ec180fb580974411e623814e519064c88f022f5c)

Attestation body containing the SBOM data listing the packages used during the build in SPDX format.