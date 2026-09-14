---
description: >-
  Faceplugin on-premise Face Recognition, Liveness, and ID Document Recognition SDK docs.
  Offline Android, iOS, Flutter, React Native, Windows, and Linux Docker integration guides.
icon: hand-wave
cover: .gitbook/assets/Screenshot 2025-11-21 184657.png
coverY: 0
layout:
  width: default
  cover:
    visible: true
    size: full
    mask: none
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Faceplugin on-premise Face Recognition, Liveness, and ID Document SDKs

### Introduction

**Faceplugin** builds **on-premise, offline** biometric SDKs. Processing stays on the phone, your Windows/Linux host, or your Docker host. There is no per-call Faceplugin cloud.

* **[Face Recognition SDK](face-recognition-sdk/)** — NIST FRVT evaluated face matching, 1:1 and live 1:N on mobile, Face Recognition API on Linux/Windows.
* **[Face Liveness Detection SDK](liveness-detection-sdk/)** — iBeta Level 2 class **passive** PAD / face anti-spoofing against photos, screens, 3D masks, and deepfake-style attacks.
* **[ID Document Recognition SDK](id-document-recognition-sdk/)** — passport OCR, ID card verification, MRZ, barcode, and optional document authenticity.
* **[ID Document Liveness SDK](id-document-liveness-sdk/)** — document anti-spoofing only (no OCR).

This documentation is the **integration** layer: clone a public GitHub demo, add the Drive runtime or pull Docker Hub, activate a license, then call the APIs that repository actually ships.

### How to use these docs

Pick the product you licensed, then **Mobile SDK** (on-device `setActivation` → `init`) or **Server SDK** (HTTP: `GET /api/machinecode` → `POST /api/activate` → process). Ports: Document **8082**, Face Recognition **8083**, Face Liveness **8084**, Document Liveness **8086**.

1. Open the product that matches what you licensed (Face Recognition, Liveness, ID Document, or Document Liveness).
2. Open **Mobile SDK** or **Server SDK**, then the **platform** page (Android, iOS, Flutter, React Native, Linux, Windows, …).
3. Follow **Setup** / **How to run** to place the Drive runtime and start the **demo**.
4. Copy the **machine code** (`FPMC1.…`) if you run a server SDK, then [request a license](request-a-license-and-support.md).
5. Use [Try it](resources/try-it.md) / **APIs** to call the same engine from your app. Store templates and document JSON in **your** database.

Native binaries are **not** on GitHub (too large). Each platform page links the Google Drive folder and the exact copy path.

{% hint style="info" %}
The demo is a full app. You do **not** need the demo screens in production — copy the runtime, call activate → init, then the process APIs.
{% endhint %}

{% hint style="info" %}
After you publish this space, connect the docs domain to **Google Search Console** (GitBook admin: custom domain, sitemap, Open Graph). Markdown in this repo cannot enable Search Console by itself.
{% endhint %}

### Our Products

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Face Recognition SDK</strong></td><td>On-premise face matching, 1:N Identify on mobile, HTTP API on Linux/Windows</td><td><a href="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/identify.png">identify.png</a></td><td></td><td><a href="face-recognition-sdk/">face-recognition-sdk</a></td></tr><tr><td><strong>Face Liveness Detection SDK</strong></td><td>Passive PAD / anti-spoofing against photos, screens, 3D models, and deepfakes</td><td><a href="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-liveness/mobile/liveness.png">liveness.png</a></td><td></td><td><a href="liveness-detection-sdk/">liveness-detection-sdk</a></td></tr><tr><td><strong>ID Document Recognition SDK</strong></td><td>Passport OCR, ID card and driver license recognition from 200+ countries</td><td><a href="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/document-reader/mobile/camera.png">camera.png</a></td><td></td><td><a href="id-document-recognition-sdk/">id-document-recognition-sdk</a></td></tr></tbody></table>

Also: [ID Document Liveness SDK](id-document-liveness-sdk/) (Linux / Docker authenticity only) · [Palm Recognition SDK](palm-recognition-sdk/).

### Try our SDKs

* [Github Repo](https://github.com/Faceplugin-ltd)
* [Google Play App](https://play.google.com/store/apps/details?id=ai.faceplugin.recognition)
* [Our playground](https://playground.faceplugin.com/)
* [HuggingFace Spaces](https://huggingface.co/FacePlugin-Ltd)
* [Docker Hub](https://hub.docker.com/u/faceplugin)
* [Try it (copy-paste)](resources/try-it.md)

### Features <a href="#feature" id="feature"></a>

* Fully On Premise, Offline SDK
* Simple and comprehensive API
* Flexible licensing model

### Platforms <a href="#platform" id="platform"></a>

Android, iOS, Flutter, React Native, Ionic (Capacitor and Cordova), Windows and Linux / Docker platforms.

### Usecases <a href="#application" id="application"></a>

* eKYC
* Fintech
* ID verification
* Digital onboarding
* Online banking, Payments
* Self-checkout at shops
* Government e-services
* Fraud detection and prevention

### Related documentation

* [Choose a product](resources/choose-a-product.md) · [FAQ](resources/faq.md) · [Troubleshooting](resources/troubleshooting.md)
* [Request a License & Support](request-a-license-and-support.md) · [SDK comparison](resources/comparisons/README.md)
* [Status codes](resources/status-codes.md) · [Changelog](resources/changelog.md)
