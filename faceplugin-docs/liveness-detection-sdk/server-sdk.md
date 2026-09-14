---
description: >-
  Faceplugin Face Liveness API for Windows and Linux Docker. On-premise PAD HTTP POST
  /api/liveness on port 8084. Score 0.5 or higher is Real.
---

# Faceplugin Liveness Detection Server SDK

Score **one RGB JPEG** over HTTP. `POST /api/liveness` (alias `/api/check_liveness`). Score **0.5 or higher** → Real / pass.

Typical call order: `GET /api/machinecode` → send `FPMC1.…` → `POST /api/activate` → `POST /api/liveness`. Default port **8084**.

For a live camera on Android or iOS, use [Mobile SDK](mobile-sdk.md).

Need recognition **and** liveness in one server App? See [Face Recognition SDK Linux (Recognition + Liveness)](../face-recognition-sdk/face-recognition-sdk-linux.md) or [Windows](../face-recognition-sdk/face-recognition-sdk-windows.md).

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td><strong>Windows SDK</strong></td><td>HTTP API on port 8084. Send a JPEG, get a liveness score. No Docker.</td><td></td><td><a href="liveness-detection-windows-sdk.md">liveness-detection-windows-sdk.md</a></td></tr><tr><td></td><td><strong>Linux SDK</strong></td><td>Docker image faceplugin/face-liveness. Same HTTP API as Windows.</td><td><a href="../.gitbook/assets/linux-docker.png">linux-docker.png</a></td><td><a href="liveness-detection-linux-sdk.md">liveness-detection-linux-sdk.md</a></td></tr></tbody></table>

```mermaid
flowchart LR
  JPEG --> PAD
  PAD --> Score
  Score --> RealOrSpoof
```

### FAQ

**What is the Face Liveness API?** `POST /api/liveness` on port **8084**. Score **≥ 0.5** is Real / pass.

**Is this document anti-spoofing?** No. Use [ID Document Liveness](../id-document-liveness-sdk/).


### Related documentation

* [Faceplugin Liveness Detection Mobile SDK](mobile-sdk.md) · [Liveness Detection SDK](README.md)
* [Face Recognition Server SDK](../face-recognition-sdk/server-sdk.md)
* [ID Document Liveness Server SDK](../id-document-liveness-sdk/server-sdk.md)
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/README.md)
