---
description: >-
  Faceplugin Liveness Detection SDK. Fully on-premise iBeta Level 2 class PAD against
  photos, screens, 3D masks, and deepfakes on Android, iOS, Windows, and Linux.
---

# Liveness Detection SDK

### Overview

Introducing our industry-leading **Liveness Detection SDK**, a **cross-platform, on-premise solution** designed for high-accuracy spoof detection. Utilizing advanced **3D passive liveness detection**, this SDK offers seamless and secure biometric verification without requiring any user interaction, making it ideal for smooth user experiences.

Our SDK is **iBeta Level 2 compliant**, adhering to the highest standards of liveness detection, capable of detecting:

* **Printed photos**
* **Screen replays**
* **3D models**
* **Deepfakes**

**Mobile** apps run a live camera (VideoWorker plus `faceDetection`). **Linux and Windows** score one RGB JPEG over HTTP (`POST /api/liveness`). Score **0.5 or higher** is treated as Real / pass.

This SDK is **standalone**. If you already use Face Recognition Identify on mobile, that flow already includes **passive 2D liveness**. Choose this product when you need PAD **without** enrollment or 1:N search.

### Platforms

Pick **Mobile SDK** or **Server SDK**, then the platform page.

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td><strong>Mobile SDK</strong></td><td>Android and iOS. Live camera PAD.</td><td><a href="mobile-sdk.md">mobile-sdk.md</a></td></tr><tr><td></td><td><strong>Server SDK</strong></td><td>Windows and Linux / Docker. JPEG over HTTP on port 8084.</td><td><a href="server-sdk.md">server-sdk.md</a></td></tr></tbody></table>

### Usecases

* [x] Financial Services (Banking & Fintech)
* [x] Identity Verification & KYC (Know Your Customer)
* [x] Healthcare & Telemedicine
* [x] Access Control & Security
* [x] Online Education & Exam Proctoring
* [x] E-Commerce & Retail
* [x] Gaming & Entertainment
* [x] Fraud Prevention
