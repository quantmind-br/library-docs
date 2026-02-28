---
title: FAQs | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/launch/faqs
source: crawler
fetched_at: 2026-02-27T23:41:57.381488-03:00
rendered_js: true
word_count: 637
summary: This document provides answers to frequently asked questions regarding the Spotify hardware certification process, including timelines, device shipping requirements, and issue priority levels.
tags:
    - certification-process
    - hardware-integration
    - spotify-connect
    - quality-assurance
    - device-certification
    - sp-avs
category: reference
---

### How soon can you begin certifying my integration?

We can never promise to start testing immediately. If you know in advance that you have a strict deadline, follow these tips to make sure you have an approval in time:

- Use Certomato as early as possible. Remember that all tests need to be passed.
- To increase your chances of success, do a thorough run of Certomato and verify that each step passes correctly.
- To ensure a smooth process, stay active on the Certification Portal.
- Prepare to start working on issues as soon as they have been submitted.
- In-depth QA on your side before submitting increases the probability to pass sooner rather than later.
- Ensure that your companion app or other UI with Spotify follows the Companion App [design guidelines](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/companion-app).
- Make sure firmware and devices reaches Spotify in time for certification. If this fails, we cannot ensure that certification will be able to start on set date and priority level may change. This may lead to certification not being done in time.

### We have less than 2 months before our deadline. What can we do?

Contact Spotify Certification as soon as possible using the Certification Portal. Together we’ll set up a time plan to make sure testing will be able to start at a good time.

### What do I do if I want the devices shipped back to us?

We at Spotify would prefer to keep the devices if possible, as it simplifies future testing if future testing is required. If you do want the packages shipped back, contact us, and we will place the packages at our reception, but it is up to you to prepare and pay for pickup with your delivery handler. Please inform us of this before devices are sent, so we can keep the packaging it came in.

### What are the different issue priorities in the Certification Portal?

All reported issues will get a priority level which indicates its importance. The table below explains the priority levels given for issues found during certification tests.

**Table: Priority level indicating the importance of the issue**

BlockerMajorMinorBlocks our testing, thus prevents us from continuing with the certificationNon compliance with our product requirements and/or an issue having a major impact on the user experience, must be fixed in order to pass certificationAffects the user experience negatively but not to a major degree

### How do I communicate with Spotify?

The Spotify Helpdesk is where all the issues and bugs are captured in an associated project that the partner has been given access.

For general questions about certification, the process and issues with the eSDK, visit [Certomato](https://certomato.spotify.com) to direct your questions to the team.

### Can I use my own descriptions about Spotify in the user manual or on the product box?

No, use only the Spotify approved copy.

### Do I need to send you new devices for SP-AVS certification?

No, as long as we can update the devices you sent for Spotify Connect Certification, you do not have to send us new units.

### How long does it take to get certified for SP-AVS?

It depends on Spotify’s and Amazon’s backlog, but in general it shouldn’t take more than 3 weeks.

### Do I have to pass the Spotify Connect certification before I can start MRM?

Yes, you need to pass the certification for Spotify Connect before submitting for AVS and MRM to Amazon.

### Can I run AVS certification and MRM at the same time?

Yes, you can run ‘single room’ and MRM simultaneously but you need to be clear about that in your certification ticket. Also, make sure you have tested both on your end before submitting for certification.

### What if I have general questions about certification?

Visit the Certification Portal to direct your quetsions to the team. You can find the link to the Certification Portal in the onboarding email.