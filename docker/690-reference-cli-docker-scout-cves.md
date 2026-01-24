---
title: docker scout cves
url: https://docs.docker.com/reference/cli/docker/scout/cves/
source: llms
fetched_at: 2026-01-24T14:40:08.368171081-03:00
rendered_js: false
word_count: 770
summary: This document provides a technical reference for the docker scout cves command, which identifies and analyzes software vulnerabilities in container images, directories, and archives.
tags:
    - docker-scout
    - vulnerability-scanning
    - cve-analysis
    - security
    - container-security
    - epss-scores
    - sbom
category: reference
---

DescriptionDisplay CVEs identified in a software artifactUsage`docker scout cves [OPTIONS] [IMAGE|DIRECTORY|ARCHIVE]`

The `docker scout cves` command analyzes a software artifact for vulnerabilities.

If no image is specified, the most recently built image is used.

The following artifact types are supported:

- Images
- OCI layout directories
- Tarball archives, as created by `docker save`
- Local directory or file

By default, the tool expects an image reference, such as:

- `redis`
- `curlimages/curl:7.87.0`
- `mcr.microsoft.com/dotnet/runtime:7.0`

If the artifact you want to analyze is an OCI directory, a tarball archive, a local file or directory, or if you want to control from where the image will be resolved, you must prefix the reference with one of the following:

- `image://` (default) use a local image, or fall back to a registry lookup
- `local://` use an image from the local image store (don't do a registry lookup)
- `registry://` use an image from a registry (don't use a local image)
- `oci-dir://` use an OCI layout directory
- `archive://` use a tarball archive, as created by `docker save`
- `fs://` use a local directory or file
- `sbom://` SPDX file or in-toto attestation file with SPDX predicate or `syft` json SBOM file In case of `sbom://` prefix, if the file is not defined then it will try to read it from the standard input.

OptionDefaultDescription`--details`Print details on default text output`--env`Name of environment[`--epss`](#epss)Display the EPSS scores and organize the package's CVEs according to their EPSS score  
`--epss-percentile`Exclude CVEs with EPSS scores less than the specified percentile (0 to 1)  
`--epss-score`Exclude CVEs with EPSS scores less than the specified value (0 to 1)  
`-e, --exit-code`Return exit code '2' if vulnerabilities are detected`--format``packages`Output format of the generated vulnerability report:  
\- packages: default output, plain text with vulnerabilities grouped by packages  
\- sarif: json Sarif output  
\- spdx: json SPDX output  
\- gitlab: json GitLab output  
\- markdown: markdown output (including some html tags like collapsible sections)  
\- sbom: json SBOM output`--ignore-base`Filter out CVEs introduced from base image`--ignore-suppressed`Filter CVEs found in Scout exceptions based on the specified exception scope  
`--locations`Print package locations including file paths and layer diff\_id`--multi-stage`Show packages from multi-stage Docker builds`--only-base`Only show CVEs introduced by the base image`--only-cisa-kev`Filter to CVEs listed in the CISA KEV catalog`--only-cve-id`Comma separated list of CVE ids (like CVE-2021-45105) to search for  
`--only-fixed`Filter to fixable CVEs`--only-metric`Comma separated list of CVSS metrics (like AV:N or PR:L) to filter CVEs by  
`--only-package`Comma separated regular expressions to filter packages by`--only-package-type`Comma separated list of package types (like apk, deb, rpm, npm, pypi, golang, etc)  
`--only-severity`Comma separated list of severities (critical, high, medium, low, unspecified) to filter CVEs by  
`--only-stage`Comma separated list of multi-stage Docker build stage names`--only-unfixed`Filter to unfixed CVEs`--only-vex-affected`Filter CVEs by VEX statements with status not affected`--only-vuln-packages`When used with --format=only-packages ignore packages with no vulnerabilities  
`--org`Namespace of the Docker organization`-o, --output`Write the report to a file`--platform`Platform of image to analyze`--ref`Reference to use if the provided tarball contains multiple references.  
Can only be used with archive`--vex-author``[<.*@docker.com>]`List of VEX statement authors to accept`--vex-location`File location of directory or file containing VEX statements

### [Display vulnerabilities grouped by package](#display-vulnerabilities-grouped-by-package)

### [Display vulnerabilities from a `docker save` tarball](#display-vulnerabilities-from-a-docker-save-tarball)

### [Display vulnerabilities from an OCI directory](#display-vulnerabilities-from-an-oci-directory)

### [Display vulnerabilities from the current directory](#display-vulnerabilities-from-the-current-directory)

### [Export vulnerabilities to a SARIF JSON file](#export-vulnerabilities-to-a-sarif-json-file)

### [Display markdown output](#display-markdown-output)

The following example shows how to generate the vulnerability report as markdown.

### [List all vulnerable packages of a certain type](#list-all-vulnerable-packages-of-a-certain-type)

The following example shows how to generate a list of packages, only including packages of the specified type, and only showing packages that are vulnerable.

### [Display EPSS score (--epss)](#epss)

The `--epss` flag adds [Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss/) scores to the `docker scout cves` output. EPSS scores are estimates of the likelihood (probability) that a software vulnerability will be exploited in the wild in the next 30 days. The higher the score, the greater the probability that a vulnerability will be exploited.

- `EPSS Score` is a floating point number between 0 and 1 representing the probability of exploitation in the wild in the next 30 days (following score publication).
- `EPSS Percentile` is the percentile of the current score, the proportion of all scored vulnerabilities with the same or a lower EPSS score.

You can use the `--epss-score` and `--epss-percentile` flags to filter the output of `docker scout cves` based on these scores. For example, to only show vulnerabilities with an EPSS score higher than 0.5:

EPSS scores are updated on a daily basis. By default, the latest available score is displayed. You can use the `--epss-date` flag to manually specify a date in the format `yyyy-mm-dd` for fetching EPSS scores.

### [List vulnerabilities from an SPDX file](#list-vulnerabilities-from-an-spdx-file)

The following example shows how to generate a list of vulnerabilities from an SPDX file using `syft`.