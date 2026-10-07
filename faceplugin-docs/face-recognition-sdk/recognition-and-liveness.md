---
description: >-
  Faceplugin Face SDK — Recognition + Liveness. Mobile Identify with 2D liveness, and server
  combined API on port 8083 with /api/liveness.
---

# Face SDK — Recognition + Liveness

Products that ship **face recognition and liveness together**.

### Mobile

On-device enroll / **1:N Identify** with **passive 2D liveness** (same native engine as FaceRecognitionSDK Android / iOS). See [Mobile SDK](mobile-sdk.md).

### Server

One process on port **8083**: recognition routes **plus** `POST /api/liveness`. Image: `faceplugin/face-recognition-liveness-sdk`.

* **Linux / Docker:** [Linux](face-recognition-sdk-linux.md)
* **Windows:** [Windows](face-recognition-sdk-windows.md)
* **.NET:** [`.NET`](face-recognition-dot-net-sdk.md)

**Capabilities:** [Face SDK capabilities](capabilities.md).

Prefer two separate server products? Run [Recognition](recognition.md) on **8083** and [Liveness](../liveness-detection-sdk/README.md) on **8084**. For production eKYC, prefer this combined Face package — see [Deploy and host](../deploy-and-host/architecture.md).
