---
title: CVEs
url: https://docs.docker.com/dhi/core-concepts/cves/
source: llms
fetched_at: 2026-01-24T14:19:31.894707736-03:00
rendered_js: false
word_count: 616
summary: This document explains the significance of Common Vulnerabilities and Exposures (CVEs) in container security and provides instructions for scanning Docker Hardened Images using various security tools.
tags:
    - docker-security
    - cve
    - vulnerability-scanning
    - docker-hardened-images
    - docker-scout
    - trivy
    - grype
    - vex
category: guide
---

## Common Vulnerabilities and Exposures (CVEs)

CVEs are publicly disclosed cybersecurity flaws in software or hardware. Each CVE is assigned a unique identifier (e.g., CVE-2024-12345) and includes a standardized description, allowing organizations to track and address vulnerabilities consistently.

In the context of Docker, CVEs often pertain to issues within base images, or application dependencies. These vulnerabilities can range from minor bugs to critical security risks, such as remote code execution or privilege escalation.

Regularly scanning and updating Docker images to mitigate CVEs is crucial for maintaining a secure and compliant environment. Ignoring CVEs can lead to severe security breaches, including:

- Unauthorized access: Exploits can grant attackers unauthorized access to systems.
- Data breaches: Sensitive information can be exposed or stolen.
- Service disruptions: Vulnerabilities can be leveraged to disrupt services or cause downtime.
- Compliance violations: Failure to address known vulnerabilities can lead to non-compliance with industry regulations and standards.

Docker Hardened Images (DHIs) are crafted to minimize the risk of CVEs from the outset. By adopting a security-first approach, DHIs offer several advantages in CVE mitigation:

- Reduced attack surface: DHIs are built using a distroless approach, stripping away unnecessary components and packages. This reduction in image size, up to 95% smaller than traditional images, limits the number of potential vulnerabilities, making it harder for attackers to exploit unneeded software.
- Faster CVE remediation: Maintained by Docker with an enterprise-grade SLA, DHIs are continuously updated to address known vulnerabilities. Critical and high-severity CVEs are patched quickly, ensuring that your containers remain secure without manual intervention.
- Proactive vulnerability management: By utilizing DHIs, organizations can proactively manage vulnerabilities. The images come with CVE and Vulnerability Exposure (VEX) feeds, enabling teams to stay informed about potential threats and take necessary actions promptly.

Regularly scanning Docker images for CVEs is essential for maintaining a secure containerized environment. While Docker Scout is integrated into Docker Desktop and the Docker CLI, tools like Grype and Trivy offer alternative scanning capabilities. The following are instructions for using each tool to scan Docker images for CVEs.

### [Docker Scout](#docker-scout)

Docker Scout is integrated into Docker Desktop and the Docker CLI. It provides vulnerability insights, CVE summaries, and direct links to remediation guidance.

#### [Scan a DHI using Docker Scout](#scan-a-dhi-using-docker-scout)

To scan a Docker Hardened Image using Docker Scout, run the following command:

Example output:

For more detailed filtering and JSON output, see [Docker Scout CLI reference](https://docs.docker.com/reference/cli/docker/scout/).

### [Grype](#grype)

[Grype](https://github.com/anchore/grype) is an open-source scanner that checks container images against vulnerability databases like the NVD and distro advisories.

#### [Scan a DHI using Grype](#scan-a-dhi-using-grype)

After installing Grype, you can scan a Docker Hardened Image by pulling the image and running the scan command. Grype requires you to export the VEX attestation to a file first:

Example output:

### [Trivy](#trivy)

[Trivy](https://github.com/aquasecurity/trivy) is an open-source vulnerability scanner for containers and other artifacts. It detects vulnerabilities in OS packages and application dependencies.

#### [Scan a DHI using Trivy](#scan-a-dhi-using-trivy)

After installing Trivy, you can scan a Docker Hardened Image by pulling the image and running the scan command:

Example output:

Docker Hardened Images include signed [VEX (Vulnerability Exploitability eXchange)](https://docs.docker.com/dhi/core-concepts/vex/) attestations that identify vulnerabilities not relevant to the image’s runtime behavior.

When using Docker Scout or Trivy, these VEX statements are automatically applied using the previous examples, and no manual configuration needed.

To manually retrieve the VEX attestation for tools that support it:

> The `docker scout vex get` command requires [Docker Scout CLI](https://github.com/docker/scout-cli/) version 1.18.3 or later.
> 
> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use `registry://dhi.io/python:3.13` instead of `dhi.io/python:3.13`.

For example:

This creates a `vex.json` file containing the VEX statements for the specified image. You can then use this file with tools that support VEX to filter out known non-exploitable CVEs.