---
description: >-
  Faceplugin Face Recognition server SDKs. On-premise HTTP APIs for Windows, Linux, Docker,
  and .NET. Detect, quality, feature, match, similarity.
---

# Server SDK

Face Recognition as an HTTP API (or .NET bindings) on **your** machine. Still-image detect, quality, template extract, 1:1 match, and template similarity. There is **no** server-side 1:N gallery (`POST /api/identify` does not exist).

Typical call order: `GET /api/machinecode` → send `FPMC1.…` → `POST /api/activate` → `POST /api/detect` / `match` / `similarity`. Default port **8083**.

The **Recognition + Liveness** pages are a combined engine (separate product from recognition-only Linux/Windows). Open-source Windows/Linux SDKs are free Python samples with lower accuracy than the commercial API.

For on-device apps, use [Mobile SDK](mobile-sdk.md).

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td><strong>Windows SDK</strong></td><td>Commercial HTTP API on port 8083. CPU only. No Docker.</td><td></td><td><a href="face-recognition-windows-sdk.md">face-recognition-windows-sdk.md</a></td></tr><tr><td></td><td><strong>Linux SDK</strong></td><td>Docker Hub image faceplugin/face-recognition. Same HTTP API as Windows.</td><td><a href="../.gitbook/assets/linux_PNG1 (1).png">linux_PNG1 (1).png</a></td><td><a href="face-recognition-linux-sdk.md">face-recognition-linux-sdk.md</a></td></tr><tr><td></td><td><strong>Windows (Recognition + Liveness)</strong></td><td>Combined recognition and PAD in one Windows App.</td><td></td><td><a href="face-recognition-sdk-windows.md">face-recognition-sdk-windows.md</a></td></tr><tr><td></td><td><strong>Linux (Recognition + Liveness)</strong></td><td>Combined recognition and PAD in one Linux / Docker App.</td><td><a href="../.gitbook/assets/linux_PNG1 (1).png">linux_PNG1 (1).png</a></td><td><a href="face-recognition-sdk-linux.md">face-recognition-sdk-linux.md</a></td></tr><tr><td></td><td><strong>Dot Net SDK</strong></td><td>.NET MAUI and C# bindings. Follow the public GitHub README.</td><td><a href="../.gitbook/assets/dotnet.png">dotnet.png</a></td><td><a href="face-recognition-dot-net-sdk.md">face-recognition-dot-net-sdk.md</a></td></tr><tr><td></td><td><strong>Open Source Windows</strong></td><td>Free Python SDK. Lower accuracy than the commercial engine.</td><td></td><td><a href="open-source-face-recognition-windows-sdk.md">open-source-face-recognition-windows-sdk.md</a></td></tr><tr><td></td><td><strong>Open Source Linux</strong></td><td>Free Python SDK for Linux.</td><td><a href="../.gitbook/assets/linux_PNG1 (1).png">linux_PNG1 (1).png</a></td><td><a href="open-source-face-recognition-linux-sdk.md">open-source-face-recognition-linux-sdk.md</a></td></tr></tbody></table>
