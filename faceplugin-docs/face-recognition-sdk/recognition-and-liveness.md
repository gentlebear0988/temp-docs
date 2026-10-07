---
description: >-
  Faceplugin Face SDK — Recognition + Liveness. One server process on port 8083 with match and /api/liveness.
---

# Face SDK — Recognition + Liveness

**Recognition and face liveness in one process** on port **8083**. Same recognition routes as Recognition-only, plus `POST /api/liveness`.

* **Capabilities:** [Face SDK capabilities](capabilities.md) (Recognition + Liveness section)
* **Linux / Docker:** `faceplugin/face-recognition-liveness-sdk` — [Linux](face-recognition-sdk-linux.md)
* **Windows:** combined HTTP API — [Windows](face-recognition-sdk-windows.md)

Prefer two separate services? Run [Recognition](recognition.md) on **8083** and [Liveness](../liveness-detection-sdk/README.md) on **8084**.
