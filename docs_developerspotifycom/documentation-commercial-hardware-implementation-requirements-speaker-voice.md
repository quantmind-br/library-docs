---
title: Speaker with Voice | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/speaker-voice
source: crawler
fetched_at: 2026-02-27T23:41:20.687975-03:00
rendered_js: true
word_count: 248
summary: This document outlines the certification requirements and integration processes for supporting Spotify via Amazon Alexa and Google Assistant on hardware products.
tags:
    - spotify-connect
    - alexa
    - sp-avs
    - google-assistant
    - certification
    - voice-integration
    - google-cast
category: guide
---

## Amazon Alexa

To support Spotify through Alexa (SP-AVS) on your WiFi product, you need to pass Spotify Connect certification first, by following the process outlined here.

These steps should be followed once you’ve passed Spotify Connect Certification on the device that will support SP-AVS:

**1**. Work with Amazon to get SP-AVS enabled for development on your platform. You’ll need to send them proof that you have passed Spotify Connect Certification otherwise they can’t enable you for this. You can find more information regarding the Amazon Alexa process on their developer site.

**2**. When you have implemented SP-AVS, you need to go through Voice Certification.

- Run and submit the AVS tests in Certomato. Make sure that your integration passes all applicable tests in the AVS self-certification checklist.
- Submit for Voice certification by filing a Spotify Helpdesk ticket.
  
  - In the ticket, you should attach the self-certification checklist that shows you have passed all applicable tests.
  - You should also attach setup and troubleshooting documentation, as well as the firmware and instructions on how to update the device.
- Amazon will slot you in for certification and keep you updated on the status of your certification.

Once you pass,

**3**. Spotify will review Amazon’s test results.

When Spotify has approved your integration, and you’ve submitted all the required paperwork, you are good to launch!

## Google Assistant

In order to support Spotify on Google Assistant you need to implement Google Cast. Please forward your NDA confirmation email to your Google contact in order to implement Google Cast.