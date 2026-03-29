---
title: docker swarm ca
url: https://docs.docker.com/reference/cli/docker/swarm/ca/
source: llms
fetched_at: 2026-01-24T14:41:18.815896316-03:00
rendered_js: false
word_count: 440
summary: This document describes the docker swarm ca command, which is used to view or rotate the root certificate authority for a Docker Swarm cluster.
tags:
    - docker-swarm
    - certificate-authority
    - security
    - ca-rotation
    - cluster-management
    - tls-certificates
category: reference
---

DescriptionDisplay and rotate the root CAUsage`docker swarm ca [OPTIONS]`

Swarm This command works with the Swarm orchestrator.

View or rotate the current swarm CA certificate.

> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

OptionDefaultDescription`--ca-cert`Path to the PEM-formatted root CA certificate to use for the new cluster  
`--ca-key`Path to the PEM-formatted root CA key to use for the new cluster`--cert-expiry``2160h0m0s`Validity period for node certificates (ns|us|ms|s|m|h)[`-d, --detach`](#detach)Exit immediately instead of waiting for the root rotation to converge  
`--external-ca`Specifications of one or more certificate signing endpoints`-q, --quiet`Suppress progress output[`--rotate`](#rotate)Rotate the swarm CA - if no certificate or key are provided, new ones will be generated

Run the `docker swarm ca` command without any options to view the current root CA certificate in PEM format.

Pass the `--rotate` flag (and optionally a `--ca-cert`, along with a `--ca-key` or `--external-ca` parameter flag), in order to rotate the current swarm root CA.

Once the rotation os finished (all the progress bars have completed) the now-current CA certificate will be printed:

### [Root CA rotation (--rotate)](#rotate)

> Mirantis Kubernetes Engine (MKE), formerly known as Docker UCP, provides an external certificate manager service for the swarm. If you run swarm on MKE, you shouldn't rotate the CA certificates manually. Instead, contact Mirantis support if you need to rotate a certificate.

Root CA Rotation is recommended if one or more of the swarm managers have been compromised, so that those managers can no longer connect to or be trusted by any other node in the cluster.

Alternately, root CA rotation can be used to give control of the swarm CA to an external CA, or to take control back from an external CA.

The `--rotate` flag does not require any parameters to do a rotation, but you can optionally specify a certificate and key, or a certificate and external CA URL, and those will be used instead of an automatically-generated certificate/key pair.

Because the root CA key should be kept secret, if provided it will not be visible when viewing swarm any information via the CLI or API.

The root CA rotation will not be completed until all registered nodes have rotated their TLS certificates. If the rotation is not completing within a reasonable amount of time, try running `docker node ls --format '{{.ID}} {{.Hostname}} {{.Status}} {{.TLSStatus}}'` to see if any nodes are down or otherwise unable to rotate TLS certificates.

### [Run root CA rotation in detached mode (--detach)](#detach)

Initiate the root CA rotation, but do not wait for the completion of or display the progress of the rotation.