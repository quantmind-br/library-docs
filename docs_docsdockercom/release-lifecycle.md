---
title: Release lifecycle
url: https://docs.docker.com/release-lifecycle/
source: llms
fetched_at: 2026-01-24T14:28:25.756866273-03:00
rendered_js: false
word_count: 942
summary: This document defines the various stages of Docker's product release lifecycle and outlines the support, availability, and retirement policies for each phase.
tags:
    - docker-lifecycle
    - release-stages
    - product-retirement
    - software-support
    - deprecation-policy
    - feature-availability
category: reference
---

## Docker's product release lifecycle

This page details Docker's product release lifecycle and how Docker defines each stage. It also provides information on the product retirement process. Features and products may progress through some or all of these phases.

> Our [Subscription Service Agreement](https://www.docker.com/legal/docker-subscription-service-agreement) governs your use of Docker and covers details of eligibility, content, use, payments and billing, and warranties. This document is not a contract and all use of Docker’s services are subject to Docker’s [Subscription Service Agreement](https://www.docker.com/legal/docker-subscription-service-agreement).

Lifecycle stageCustomer availabilitySupport availabilityLimitationsRetirement[Experimental](#experimental)Limited availabilityCommunity supportSoftware may have limitations, bugs and/or stability concernsCan be discontinued without notice[Beta](#beta)All or those involved in a Beta Feedback ProgramCommunity supportSoftware may have limitations, bugs and/or stability concernsCan be discontinued without notice[Early Access (EA)](#early-access-ea)All or those involved in an Early Access Feedback ProgramFullSoftware may have limitations, bugs and/or stability concerns. These limitations will be documented.Follows the [retirement process](#retirement-process)[General Availability (GA)](#general-availability-ga)AllFullFew or no limitations for supported use casesFollows the [retirement process](#retirement-process)

### [Experimental](#experimental)

Experimental offerings are features that Docker is currently experimenting with. Customers who access experimental features have the opportunity to test, validate, and provide feedback on future functionality. This helps us focus our efforts on what provides the most value to our customers.

**Customer availability:** Availability of experimental features is limited. A portion of users may have access to none, one or many experimental features.

**Support:** Support for experimental features is best effort via Community support channels and forums.

**Limitations:** Experimental features may have potentially significant limitations such as functional limitations, performance limitations, and API limitations. Features and programmatic interfaces may change at any time without notice.

**Retirement:** During the experimental period, Docker will determine whether to continue an offering through its lifecycle. We reserve the right to change the scope of or discontinue an Experimental product or feature at any point in time without notice, as outlined in our [Subscription Service Agreement](https://www.docker.com/legal/docker-subscription-service-agreement).

### [Beta](#beta)

Beta offerings are initial releases of potential future products or features. Customers who participate in our beta programs have the opportunity to test, validate, and provide feedback on future functionality. This helps us focus our efforts on what provides the most value to our customers.

**Customer availability:** Participation in beta releases is by invitation or via use of clearly identified beta features in product. Beta invitations may be public or private.

**Support:** Support for beta features is best effort via Community support channels and forums.

**Limitations:** Beta releases may have potentially significant limitations such as functional limitations, performance limitations, and API limitations. Features and programmatic interfaces may change at any time without notice.

**Retirement:** During the beta period, Docker will determine whether to continue an offering through its lifecycle. We reserve the right to change the scope of or discontinue a Beta product or feature at any point in time without notice, as outlined in our [Subscription Service Agreement](https://www.docker.com/legal/docker-subscription-service-agreement).

### [Early Access (EA)](#early-access-ea)

Early Access offerings are products or features that may have potential feature limitations and are enabled for specific user groups as part of an incremental roll-out strategy. They are ready to be released to the world, pending some fine tuning.

**Customer availability:** Early Access functionality can be rolled out to all customers or specific segments of users in addition to or in place of existing functionality.

**Support:** Early Access offerings are provided with the same level of support as General Availability features and products.

**Limitations:** Early Access releases may have potentially significant limitations such as functional limitations, performance limitations, and API limitations, though these limitations will be documented. Breaking changes to features and programmatic interfaces will follow the [retirement process](#retirement-process) outlined below.

**Retirement:** In the event we retire an Early Access product before General Availability, we will strive to follow the [retirement process](#retirement-process) outlined below.

### [General Availability (GA)](#general-availability-ga)

General Availability offerings are fully functional products or features that are openly accessible to all Docker customers.

**Customer availability:** All Docker users have access to GA offerings according to their subscription levels.

**Limitations:** General Availability features and products will have few or no limitations for supported use cases.

**Support:** All GA offerings are fully supported, as described in our [support page](https://www.docker.com/support/).

**Retirement:** General Availability offerings follow the [retirement process](#retirement-process) outlined below.

The decision to retire or deprecate features follows a rigorous process including understanding the demand, use, impact of feature retirement and, most importantly, customer feedback. Our goal is to invest resources in areas that will add the most value for the most customers

Docker is committed to being clear, transparent, and proactive when interacting with our customers, especially about changes to our platform. To that end, we will make best efforts to follow these guidelines when retiring functionality:

- **Advance notice:** For retirement of major features or products, we will attempt to notify customers at least 6 months in advance.
- **Viable alternatives:** Docker will strive to provide viable alternatives to our customers when retiring functionality. These may be alternative offerings from Docker or recommended alternatives from 3rd party providers. Where possible and appropriate, Docker will automatically migrate customers to alternatives for retired functionality.
- **Continued support:** Docker commits to providing continued support for functionality until its retirement date.

We may need to accelerate the timeline for retirement of functionality in extenuating circumstances, such as essential changes necessary to protect the integrity of our platform or the security of our customers and others. In these cases, it is important that those changes occur as quickly as possible.

Similarly, integrated third party software or services may need to be retired due to the third-party decision to change or retire their solution. In these situations, the pace of retirement will be out of our control.

However, even under these circumstances, we will provide as much advance notice as possible.