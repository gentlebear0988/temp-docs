---
description: >-
  Faceplugin Face SDK — Recognition only. Server Face Recognition API on port 8083 (no /api/liveness).
---

# Face SDK — Recognition

**Recognition only** server products: detect, quality, templates, 1:1 match / similarity. Port **8083**. These images do **not** expose `POST /api/liveness`.

* **Capabilities:** [Face SDK capabilities](capabilities.md) (Recognition section)
* **Server:** [Server SDK](server-sdk.md) — [Linux](face-recognition-linux-sdk.md) (`faceplugin/face-recognition`) · [Windows](face-recognition-windows-sdk.md)
* **Open source:** free Python samples — [Open Source](open-source-windows-and-linux.md)

Mobile Face Recognition apps include **2D liveness on Identify** — they live under [Recognition + Liveness](recognition-and-liveness.md), not here.

For standalone anti-spoofing only see [Liveness](../liveness-detection-sdk/README.md). For match + `/api/liveness` in one server process see [Recognition + Liveness](recognition-and-liveness.md).
