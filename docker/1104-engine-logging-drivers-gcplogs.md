---
title: Google Cloud Logging driver
url: https://docs.docker.com/engine/logging/drivers/gcplogs/
source: llms
fetched_at: 2026-01-24T14:23:57.413445123-03:00
rendered_js: false
word_count: 449
summary: This document explains how to configure and use the Google Cloud Logging driver (gcplogs) to send Docker container logs to Google Cloud, covering both global and container-specific settings.
tags:
    - docker
    - google-cloud-logging
    - gcplogs
    - logging-driver
    - container-logs
    - gcp-metadata
category: configuration
---

The Google Cloud Logging driver sends container logs to [Google Cloud Logging](https://cloud.google.com/logging/docs/) Logging.

To use the `gcplogs` driver as the default logging driver, set the `log-driver` and `log-opt` keys to appropriate values in the `daemon.json` file, which is located in `/etc/docker/` on Linux hosts or `C:\ProgramData\docker\config\daemon.json` on Windows Server. For more about configuring Docker using `daemon.json`, see [daemon.json](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file).

The following example sets the log driver to `gcplogs` and sets the `gcp-meta-name` option.

Restart Docker for the changes to take effect.

You can set the logging driver for a specific container by using the `--log-driver` option to `docker run`:

If Docker detects that it's running in a Google Cloud Project, it discovers configuration from the [instance metadata service](https://cloud.google.com/compute/docs/metadata). Otherwise, the user must specify which project to log to using the `--gcp-project` log option and Docker attempts to obtain credentials from the [Google Application Default Credential](https://developers.google.com/identity/protocols/application-default-credentials). The `--gcp-project` flag takes precedence over information discovered from the metadata server, so a Docker daemon running in a Google Cloud project can be overridden to log to a different project using `--gcp-project`.

Docker fetches the values for zone, instance name and instance ID from Google Cloud metadata server. Those values can be provided via options if metadata server isn't available. They don't override the values from metadata server.

You can use the `--log-opt NAME=VALUE` flag to specify these additional Google Cloud Logging driver options:

OptionRequiredDescription`gcp-project`optionalWhich Google Cloud project to log to. Defaults to discovering this value from the Google Cloud metadata server.`gcp-log-cmd`optionalWhether to log the command that the container was started with. Defaults to false.`labels`optionalComma-separated list of keys of labels, which should be included in message, if these labels are specified for the container.`labels-regex`optionalSimilar to and compatible with `labels`. A regular expression to match logging-related labels. Used for advanced [log tag options](https://docs.docker.com/engine/logging/log_tags/).`env`optionalComma-separated list of keys of environment variables, which should be included in message, if these variables are specified for the container.`env-regex`optionalSimilar to and compatible with `env`. A regular expression to match logging-related environment variables. Used for advanced [log tag options](https://docs.docker.com/engine/logging/log_tags/).`gcp-meta-zone`optionalZone name for the instance.`gcp-meta-name`optionalInstance name.`gcp-meta-id`optionalInstance ID.

If there is collision between `label` and `env` keys, the value of the `env` takes precedence. Both options add additional fields to the attributes of a logging message.

The following is an example of the logging options required to log to the default logging destination which is discovered by querying the Google Cloud metadata server.

This configuration also directs the driver to include in the payload the label `location`, the environment variable `ENV`, and the command used to start the container.

The following example shows logging options for running outside of Google Cloud. The `GOOGLE_APPLICATION_CREDENTIALS` environment variable must be set for the daemon, for example via systemd: