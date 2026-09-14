---
description: >-
  Faceplugin vs FaceTec. 2D on-premise face/liveness/document SDKs versus FaceTec 3D FaceMap
  liveness, server SDK, and usage-based 3D liveness billing.
---

# Faceplugin vs FaceTec

[FaceTec](https://www.facetec.com/) focuses on **3D liveness** (3D FaceMap / FaceScan), 3D face matching, and ID scan/OCR as part of that flow. Device SDKs target **iOS, Android, and webcams**. Customers run FaceTec **Server SDK** on their servers; FaceTec’s site describes **monthly 3D liveness usage** (minimum commitment) with ID scans included for customers. Certified PAD is a core FaceTec marketing claim.

Faceplugin ships **2D** on-premise engines: still-image or camera-frame matching and **passive** PAD, plus standalone passport OCR and document liveness. Linux/Windows are **HTTP APIs** you host (ports 8083 / 8084 / 8082). License is an offline `FP1.…` key, not a per-liveness monthly meter in these docs.

| Criterion | Faceplugin | FaceTec |
| --- | --- | --- |
| On-premise processing | Yes (device or your HTTP host) | Yes (customer-hosted Server SDK; also cloud options) |
| Offline after activation | Yes | Check vendor (3D session typically talks to **your** FaceTec server) |
| Android / iOS | Yes | Yes |
| Flutter / React Native / Ionic | Yes (FR + Document; Liveness is Android/iOS) | Check vendor |
| Windows / Linux HTTP API | Yes | Server SDK / REST on **your** FaceTec server |
| Passive 2D PAD | Yes | 3D liveness is the product |
| Active / challenge liveness | Not the Face Liveness App | 3D video-selfie capture |
| Passport OCR / ID scan | Yes (Document Recognition SDK) | Yes (Photo ID OCR / barcode / NFC per FaceTec site) |
| Document liveness product | Yes (Linux) | ID tampering checks in Identity Check flow |
| Flutter Face Liveness App | No public App | Check vendor |
| Pricing model in public docs | License key / machine code | Monthly 3D liveness usage + minimums (per FaceTec.com) |
| NIST / iBeta | FRVT evaluated matching; iBeta Level 2 **class** PAD wording | FaceTec publishes PAD certification claims — verify on FaceTec.com |

**Choose Faceplugin** when you want **unlimited on-prem inference after license**, 2D JPEG/`faceDetection` APIs, Docker Hub images, and a **separate** document OCR engine you orchestrate ([eKYC](../choose-a-product.md#combining-products-ekyc)).

**Look at FaceTec** when you specifically need **3D FaceMap liveness** and their certified PAD / 3D matching stack.

Integrate Faceplugin: [Android Face Recognition](../../face-recognition-sdk/face-recognition-android-sdk.md) · [Liveness Linux](../../liveness-detection-sdk/liveness-detection-linux-sdk.md) · [Document Linux](../../id-document-recognition-sdk/id-document-recognition-linux-sdk.md)

### Related documentation

* [SDK comparison index](README.md) · [Choose a product](../choose-a-product.md)
* [FAQ](../faq.md) · [Try it](../try-it.md)
