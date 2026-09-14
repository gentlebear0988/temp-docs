---
description: >-
  Faceplugin Liveness Detection server SDKs. On-premise PAD HTTP API for Windows, Linux,
  and Docker. POST /api/liveness on port 8084.
---

# Server SDK

Score **one RGB JPEG** over HTTP. `POST /api/liveness` (alias `/api/check_liveness`). Score **0.5 or higher** → Real / pass.

Typical call order: `GET /api/machinecode` → send `FPMC1.…` → `POST /api/activate` → `POST /api/liveness`. Default port **8084**.

For a live camera on Android or iOS, use [Mobile SDK](mobile-sdk.md).

Need recognition **and** liveness in one server App? See [Face Recognition SDK Linux (Recognition + Liveness)](../face-recognition-sdk/face-recognition-sdk-linux.md) or [Windows](../face-recognition-sdk/face-recognition-sdk-windows.md).

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td><strong>Windows SDK</strong></td><td>HTTP API on port 8084. Send a JPEG, get a liveness score. No Docker.</td><td></td><td><a href="liveness-detection-windows-sdk.md">liveness-detection-windows-sdk.md</a></td></tr><tr><td></td><td><strong>Linux SDK</strong></td><td>Docker image faceplugin/face-liveness. Same HTTP API as Windows.</td><td><a href="../.gitbook/assets/linux_PNG1 (1).png">linux_PNG1 (1).png</a></td><td><a href="liveness-detection-linux-sdk.md">liveness-detection-linux-sdk.md</a></td></tr></tbody></table>
