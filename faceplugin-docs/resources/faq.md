---
description: >-
  Faceplugin SDK FAQ. Passive vs active liveness, offline on-premise licensing, Flutter support,
  Docker vs host machine codes, demo app ids, and match thresholds.
---

# FAQ

## What is a face recognition SDK?

A library that detects faces, extracts a template (embedding), and compares templates. Faceplugin’s commercial SDK runs **on-premise**. You store templates in **your** database. See [Face Recognition SDK](../face-recognition-sdk/).

## What is passive liveness detection?

The engine scores a camera frame or JPEG **without** a smile / turn-head challenge. Faceplugin’s [Face Liveness Detection SDK](../liveness-detection-sdk/) is **passive PAD** (iBeta Level 2 **class** wording in these docs — not a claim of a named iBeta certificate unless you have one on file).

## What is the difference between active and passive liveness?

**Passive:** no user challenge (Face Liveness Apps, and 2D liveness on Face Recognition Identify). **Active:** challenge demos exist on GitHub as `Active-Liveness-Detection-Android` and `Active-Liveness-Detection-iOS`. They are **not** the Face Liveness App. Face Liveness Linux/Windows is still `POST /api/liveness` on one JPEG.

## Can face recognition work completely offline?

Yes. After you activate with an `FP1.…` key bound to the app id (mobile) or machine code (server), matching does not need the internet.

## Can Faceplugin run on-premise?

Yes. That is the product model: phone, Windows/Linux host, or Docker on **your** infrastructure.

## Does the Faceplugin SDK require an internet connection?

Not for inference after activation. You need a network only to clone GitHub, pull Docker Hub, download Drive runtimes, and to contact Faceplugin for a license.

## Does Faceplugin support Flutter?

Yes for Face Recognition and ID Document Recognition (`face_recognition_sdk`, `document_reader_sdk`). There is **no** public Face Liveness Flutter App — use Face Recognition’s 2D liveness on Identify and/or native Android/iOS Liveness.

## Does Faceplugin support iOS?

Yes for Face Recognition, Face Liveness, and ID Document Recognition. Physical iPhone; demo bundle ids are listed on each iOS page.

## Docker vs host machine code

`GET /api/machinecode` returns `FPMC1.…`. Docker and a native host on the same machine produce **different** codes. License the environment you run in production. See [Request a License](../request-a-license-and-support.md).

## Demo `FP1.…` and my own app id

Sample keys are bound to the **demo** application id / bundle id on the platform page. Request a new key for your production id.

## Match and liveness thresholds

Mobile Identify default match **0.67**. Face Liveness server: score **≥ 0.5** → Real / pass. Tune only if Faceplugin gives you a different operating point for your license.

## How large is the Android SDK?

The GitHub repo is small. Native models (AAR + `.fpk` / engine) come from Google Drive and are large — that is why they are not on GitHub. Check the Drive folder size for the product you licensed.

## Is there a Node.js or C++ App?

Not as a public customer App in this documentation. Server integration is HTTP (`curl` from any language) or Python `sdk.py` on the same host as `lib/cpu/`.

### Related documentation

* [Try it](try-it.md) · [Troubleshooting](troubleshooting.md) · [Status codes](status-codes.md)
* [Choose a product](choose-a-product.md) · [SDK comparison](comparisons/README.md)
