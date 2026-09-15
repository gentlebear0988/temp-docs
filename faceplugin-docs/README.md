---
description: >-
  Faceplugin on-premise Face Recognition, Liveness, and ID Document Recognition
  SDK docs. Offline Android, iOS, Flutter, React Native, Windows, and Linux
  Docker integration guides.
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
  anchors:
    visible: true
---

# Welcome

### Introduction

**Faceplugin** builds **on-premise, offline** biometric SDKs. Processing stays on the phone, your Windows/Linux host, or your Docker host. There is no per-call Faceplugin cloud.

### What you can build

* **Passport OCR & ID verification** — classify and read **16,900** document templates from **255** countries (MRZ — the machine-readable zone on passports — plus barcode and optional authenticity). Start: [Document capabilities](id-document-recognition-sdk/capabilities.md) · [Passport OCR guide](resources/passport-ocr-and-id-verification.md)
* **Face Recognition API & Identify** — offline 1:1 match, mobile 1:N Identify (one face vs many enrolled templates), NIST FRVT (Face Recognition Vendor Test) evaluated. Start: [Face Recognition capabilities](face-recognition-sdk/capabilities.md)
* **Face anti-spoofing** — passive liveness against photos, screens, 3D masks, deepfake-style attacks. Start: [Face Liveness capabilities](liveness-detection-sdk/capabilities.md)
* **Document authenticity only** — no OCR. [ID Document Liveness](id-document-liveness-sdk/) (Linux **8086**)

Product hubs: [Face Recognition](face-recognition-sdk/) · [Face Liveness Detection](liveness-detection-sdk/) · [ID Document Recognition](id-document-recognition-sdk/) · [ID Document Liveness](id-document-liveness-sdk/)

This documentation is the **integration** layer: clone a public GitHub sample, add the Google Drive runtime package or pull Docker Hub, activate a license, then call the APIs that repository actually exposes.

### How to use these docs

1. Read **Capabilities** for the product you need (what it can do).
2. Open **Mobile SDK** or **Server SDK**, then the **platform** page (Android, iOS, Flutter, React Native, Linux, Windows, …).
3. Follow **Setup** / **How to run** to place the Google Drive runtime package and start the **GitHub sample app** for that product.
4. Copy the **machine code** (`FPMC1.…`) if you run a server SDK, then [request a license](request-a-license-and-support.md).
5. Use [Try it](resources/try-it.md) / **APIs** to call the same **SDK APIs** from your app. Store templates and document JSON in **your** database.

Ports: Document **8082**, Face Recognition **8083**, Face Liveness **8084**, Document Liveness **8086**.

Native binaries are **not** on GitHub (too large). Each platform page links the Google Drive folder and the exact copy path.

{% hint style="info" %}
Each GitHub sample app is a complete application for testing. In production, use the runtime directly: copy the runtime, call `activate` → `init`, then call the processing APIs.
{% endhint %}

### Our Products

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Face Recognition SDK</strong></td><td>On-premise face matching, 1:N Identify on mobile, HTTP API on Linux/Windows</td><td><a href="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/identify.png">https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/identify.png</a></td><td></td><td><a href="face-recognition-sdk/">face-recognition-sdk</a></td></tr><tr><td><strong>Face Liveness Detection SDK</strong></td><td>Passive anti-spoofing against photos, screens, 3D models, and deepfakes</td><td><a href="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-liveness/mobile/liveness.png">https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-liveness/mobile/liveness.png</a></td><td></td><td><a href="liveness-detection-sdk/">liveness-detection-sdk</a></td></tr><tr><td><strong>ID Document Recognition SDK</strong></td><td>Passport OCR, ID verification — 16,900 templates, 255 countries</td><td><a href="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/document-reader/mobile/camera.png">https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/document-reader/mobile/camera.png</a></td><td></td><td><a href="id-document-recognition-sdk/">id-document-recognition-sdk</a></td></tr></tbody></table>

Also: [ID Document Liveness SDK](id-document-liveness-sdk/) (Linux / Docker authenticity only) · [Palm Recognition SDK](palm-recognition-sdk/).

### Try our SDKs

* [GitHub repos](https://github.com/Faceplugin-ltd)
* [Google Play App](https://play.google.com/store/apps/details?id=ai.faceplugin.recognition)
* [Playground](https://playground.faceplugin.com/)
* [Hugging Face Spaces](https://huggingface.co/Faceplugin-Ltd)
* [Docker Hub](https://hub.docker.com/u/faceplugin)
* [Try it (copy-paste)](resources/try-it.md)

### Features <a href="#feature" id="feature"></a>

* Offline after `FP1.…` license activation — no Faceplugin cloud inference
* HTTP APIs on ports **8082** (documents), **8083** (face recognition), **8084** (face liveness), **8086** (document liveness)
* Mobile SDKs for Android, iOS, Flutter, React Native, and Ionic (platform support varies by product)

### Platforms <a href="#platform" id="platform"></a>

Platforms vary by product. **Face Recognition** and **ID Document Recognition** include Android, iOS, Flutter, React Native, Ionic, Windows, and Linux/Docker. **Face Liveness** is Android, iOS, Windows, and Linux/Docker (no public Flutter or React Native SDK).

### Use cases <a href="#application" id="application"></a>

* **eKYC / digital onboarding** — ID OCR + optional authenticity + selfie liveness + face match ([combine products](resources/choose-a-product.md#combining-products-ekyc))
* **Banking and fintech** — passport / ID verification and face anti-spoofing on your infrastructure
* **Access control and attendance** — mobile 1:N Identify with templates you store
* **Fraud prevention** — reject presentation attacks and document spoofs before enrollment

### Related documentation

* [Choose a product](resources/choose-a-product.md) · [Try it](resources/try-it.md) · [Glossary](resources/glossary.md) · [FAQ](resources/faq.md)
* [Request a License & Support](request-a-license-and-support.md) · [SDK comparison](resources/comparisons/)
* [Status codes](resources/status-codes.md) · [Troubleshooting](resources/troubleshooting.md) · [Changelog](resources/changelog.md)
