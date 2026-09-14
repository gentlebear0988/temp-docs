---
description: >-
  Faceplugin on-premise Face Recognition SDK. Offline 1:1 and 1:N matching, NIST FRVT evaluated,
  for Android, iOS, Flutter, React Native, Windows, Linux Docker, and .NET.
---

# Face Recognition SDK

### Overview

<figure><img src="../.gitbook/assets/diagram-fr-mobile-identify.png" alt="On-premise Face Recognition Mobile SDK Identify flow: Camera Detect 2D Liveness Embedding Your database Identify 0.67"><figcaption><p>Public mobile Apps (Android, iOS, Flutter, React Native, Ionic): live Identify stores templates in your database. Default match 0.67.</p></figcaption></figure>


**Faceplugin Face Recognition SDK** is a fully **on-premise, offline** face matching engine. Images are processed on the device or on your server — not in Faceplugin’s cloud. The algorithm is evaluated on **NIST FRVT**.

This is **not** the standalone [Liveness Detection SDK](../liveness-detection-sdk/) (PAD only). It is **not** a passport OCR SDK — use [ID Document Recognition](../id-document-recognition-sdk/) to read IDs. On mobile, Identify already includes **passive 2D liveness**. For PAD without enrollment, use Liveness Detection.

On **mobile**, demos enroll people, run live **1:N Identify** (VideoWorker), and store templates in **your** database. On **Linux and Windows**, the Face Recognition **API** is still-image HTTP: detect, quality, feature, match, similarity. There is **no** `POST /api/identify` gallery.

<figure><img src="../.gitbook/assets/diagram-fr-server-api.png" alt="Faceplugin Face Recognition API for Linux Docker and Windows: POST /api/detect match similarity on port 8083, no identify gallery"><figcaption><p>Commercial server Apps FaceRecognition-Windows and FaceRecognition-Docker. Port 8083. No server-side 1:N gallery.</p></figcaption></figure>


```mermaid
flowchart LR
  Camera --> Detect
  Detect --> Liveness2D
  Liveness2D --> Embedding
  Embedding --> Identify
  Identify --> Result
```

### Features

* [x] Face Detection
* [x] Face Landmark Detection
* [x] Face Template Extraction
* [x] Face Template Matching
* [x] Live 1:N Identify (mobile)
* [x] Liveness Detection (passive 2D on mobile Identify)
* [x] Pose Estimation
* [x] Fully On-Premise

### Platforms

Pick **Mobile SDK** or **Server SDK**, then the platform page. Each page includes GitHub source, install steps, and the APIs that App actually ships.

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td><strong>Mobile SDK</strong></td><td>Android, iOS, Flutter, React Native, Ionic, and browser open-source clients.</td><td><a href="mobile-sdk.md">mobile-sdk.md</a></td></tr><tr><td></td><td><strong>Server SDK</strong></td><td>Windows, Linux / Docker, .NET, and open-source Python.</td><td><a href="server-sdk.md">server-sdk.md</a></td></tr></tbody></table>

Typical call order on **mobile**: `setActivation` → `init` → detect / extract template → store templates in **your** database → `similarity` or VideoWorker (live 1:N). Identify default **0.67**. Liveness default **0.5**.

Typical call order on **Linux / Windows**: `GET /api/machinecode` → `POST /api/activate` → `POST /api/detect` / `match` / `similarity`. There is **no** server-side 1:N gallery (`POST /api/identify` does not exist).

### FAQ

**Can face recognition work completely offline?** Yes. After you activate with an `FP1.…` key, matching does not need the internet.

**Does this SDK include liveness?** Mobile Identify includes passive 2D liveness. Standalone iBeta-class PAD is the [Liveness Detection SDK](../liveness-detection-sdk/). On the server, run Face Recognition (port **8083**) and Face Liveness (port **8084**) as **two** Apps.

**Is there a Face Recognition API?** Yes — Linux Docker and Windows HTTP on port **8083**. See [Linux](face-recognition-linux-sdk.md) and [Windows](face-recognition-windows-sdk.md).

### Usecases

* [x] Access Control & Security
* [x] Attendance & Time Tracking
* [x] Law Enforcement & Public Safety
* [x] User Authentication for Applications
* [x] Retail & Customer Experience
* [x] Healthcare
* [x] Travel & Transportation
* [x] Smart Devices & IoT
* [x] Entertainment & Events
* [x] Education
* [x] Fraud Prevention

### Related documentation

* [Liveness Detection SDK](../liveness-detection-sdk/) · [ID Document Recognition SDK](../id-document-recognition-sdk/)
* [Request a License](../request-a-license-and-support.md) · [Try it](../resources/try-it.md) · [FAQ](../resources/faq.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/README.md)
* [Status codes](../resources/status-codes.md)
