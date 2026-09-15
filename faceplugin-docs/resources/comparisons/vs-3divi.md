---
description: >-
  Faceplugin vs 3DiVi Face SDK. On-premise face recognition, platforms, liveness, and ID
  document products. Public 3DiVi docs versus Faceplugin products in these docs.
---

# Faceplugin vs 3DiVi

[3DiVi Face SDK](https://3divi.ai/products/software/face-sdk) is a C++ face recognition library with wrappers (C#, Java, Python, Swift, Flutter) for Windows, Linux, Android, and iOS. It documents on-prem / on-device / own-cloud deployment and a **2d_liveness** estimator. 3DiVi also sells OMNI Platform (client-server video) and Image API (REST).

Faceplugin is an **on-premise SDK suite**: Face Recognition, standalone Face Liveness (passive PAD HTTP + mobile), ID Document Recognition (passport OCR / MRZ), and ID Document Liveness. Server Apps are Docker Hub images with `FPMC1.…` machine-code licenses.

| Criterion | Faceplugin | 3DiVi |
| --- | --- | --- |
| On-premise / offline after license | Yes | Yes (offline and online license modes documented) |
| Android / iOS face SDK | Yes | Yes |
| Flutter face | Yes (Face Recognition + Document) | Yes (Face SDK docs list Flutter) |
| React Native / Ionic | Yes | Check vendor |
| Windows / Linux face | Yes (HTTP API + native) | Yes (C++/Python/C#) |
| Linux Docker Hub HTTP API | Yes (`faceplugin/face-recognition`, `face-liveness`, `document-reader`) | Check vendor (local license server mentioned for Docker) |
| Standalone face PAD product | Yes (passive `POST /api/liveness`) | Liveness as Face SDK estimator; BAF / other products exist |
| Passport OCR / ID card SDK | Yes | Check vendor (not the core Face SDK page) |
| Document liveness | Yes (Linux 8086) | Check vendor |
| NIST FRVT (as claimed in Faceplugin docs) | Evaluated matching | Check vendor |
| iBeta PAD | Level 2 **class** wording in Faceplugin docs | Check vendor |
| License model | Offline `FP1.…` / `FPMC1.…` | Hardware, app id, USB token, online validation options |

**Choose Faceplugin** when you want a **documented HTTP Docker API** plus **ID OCR and document liveness** in the same vendor docs, with mobile 1:N Identify demos.

**Look at 3DiVi** when you need their C++ Face SDK / OMNI video platform specifically. Confirm Flutter/RN and document OCR on [3DiVi docs](https://docs.3divi.ai/face_sdk/).

Integrate Faceplugin: [Android Face Recognition](../../face-recognition-sdk/face-recognition-android-sdk.md) · [Liveness Linux](../../liveness-detection-sdk/liveness-detection-linux-sdk.md) · [Document Linux](../../id-document-recognition-sdk/id-document-recognition-linux-sdk.md)

### Related documentation

* [SDK comparison index](README.md) · [Choose a product](../choose-a-product.md)
* [FAQ](../faq.md) · [Try it](../try-it.md)
