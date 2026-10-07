---
description: >-
  Faceplugin platform matrix. Which SDKs ship on Android, iOS, Flutter, React Native, Ionic,
  Windows, and Linux Docker.
icon: table
layout:
  width: wide
  description:
    visible: true
---

# Platform matrix

This table is the **shipping product inventory** from public repositories. It is not a roadmap.

Every Linux and Windows server product listed here is **CPU only**.

| Product | Android | iOS | Flutter | React Native | Ionic Capacitor | Ionic Cordova | Windows | Linux / Docker |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ID Document Recognition | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Face Recognition | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Face Liveness | Yes | Yes | — | — | — | — | Yes | Yes |
| ID Document Liveness | — | — | — | — | — | — | — | Yes |

A dash (—) means there is no public SDK for that platform in these docs.

Face Recognition **mobile** already includes 2D liveness on Identify.

## Not customer products in these docs

These names are **not** documented here as Faceplugin customer products:

* All-in-one Face Verification or IDV HTTP app
* GPU desktop packages (`lib/gpu/`)

You combine Document Reader, Face Liveness, and Face Recognition yourself. See [Architecture](../deploy-and-host/architecture.md).

## Ports (server)

| Product | API | Gradio (host only) |
| --- | ---: | ---: |
| Document Reader | 8082 | 9002 |
| Face Recognition | 8083 | 9003 |
| Face Liveness | 8084 | 9004 |
| Document Liveness | 8086 | 9006 |

### Related documentation

* [Choose a product](choose-a-product.md) · [Deploy and host](../deploy-and-host/) · [Hosting requirements](../deploy-and-host/hosting-requirements.md)
