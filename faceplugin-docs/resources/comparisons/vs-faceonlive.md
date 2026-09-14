---
description: >-
  Faceplugin vs FaceOnLive. Both sell on-premise face, liveness, and ID SDKs. Compare public
  catalogs, APIs, and what Faceplugin shipping Apps actually implement.
---

# Faceplugin vs FaceOnLive

[FaceOnLive](https://faceonlive.com/) markets on-premises face recognition, liveness, ID recognition, ID liveness, and an ID Verification SDK Suite. Public docs show `setActivation` / `faceDetection` / `templateExtraction` style mobile APIs and Linux ID liveness libraries.

The catalogs **overlap**. Do not assume identical engines, accuracy, or licenses. Compare **this Faceplugin documentation** (real routes: `POST /api/liveness`, `documentProcess`, `FPMC1.…`) against FaceOnLive’s current docs.

| Criterion | Faceplugin | FaceOnLive |
| --- | --- | --- |
| On-premise / offline | Yes | Yes (vendor site) |
| Android / iOS | Yes | Yes (vendor site) |
| Flutter / React Native | FR + Document yes; Liveness no Flutter/RN App | Vendor site lists Flutter and RN |
| Windows / Linux HTTP | Yes (8082 / 8083 / 8084 / 8086) | Check vendor (Linux SDKs documented) |
| Docker Hub images | `faceplugin/face-recognition`, `face-liveness`, `document-reader`, `document-liveness` | Check vendor |
| Face recognition | Yes | Yes (vendor site) |
| Passive face PAD | Yes | Yes (vendor site; PAD L2 claims — verify) |
| Passport OCR / MRZ | Yes | Yes (vendor site) |
| Document liveness | Yes (Linux) | Yes (vendor GitHub/docs) |
| Combined eKYC App | You orchestrate products ([choose a product](../choose-a-product.md)) | Vendor markets a suite |
| NIST FRVT | Evaluated matching (Faceplugin docs) | Check vendor |
| Playground / HF / Docker Hub | Documented in these docs | Check vendor |

**Choose Faceplugin** when you want the **exact APIs and ports in these docs**, official `faceplugin/*` Docker Hub images, and a license flow around **`FPMC1.…` / `FP1.…`**.

**Look at FaceOnLive** when their suite packaging or platform list matches your project; confirm engines and licenses on [faceonlive.com/docs](https://faceonlive.com/docs/).

Integrate Faceplugin: [Android Face Recognition](../../face-recognition-sdk/face-recognition-android-sdk.md) · [Liveness Linux](../../liveness-detection-sdk/liveness-detection-linux-sdk.md) · [Document Linux](../../id-document-recognition-sdk/id-document-recognition-linux-sdk.md)

### Related documentation

* [SDK comparison index](README.md) · [Choose a product](../choose-a-product.md)
* [FAQ](../faq.md) · [Try it](../try-it.md)
