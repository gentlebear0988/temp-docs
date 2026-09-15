---
description: >-
  Faceplugin open-source Palm Recognition SDK. On-premise RGB-camera palm matching with Python
  Anaconda. ROI extraction and compare_two_images. Not a Faceplugin commercial face SDK.
---

# Palm Recognition SDK

### Overview

**Faceplugin Palm Recognition SDK** is a **free, on-premise** Python sample for palm matching from a standard **RGB camera**. It is **not** the commercial [Face Recognition SDK](../face-recognition-sdk/) and it is **not** a document or liveness product.

All processing stays on your machine.

### Features

* [x] Palm Detection
* [x] ROI (region of interest) extraction
* [x] Template Extraction
* [x] Template Matching
* [x] On-premise (your machine only)

### Platforms

The public sample is the [open-source Palm Recognition repository](open-source-palm-recognition-sdk.md) (Anaconda / Python on Windows in the README).

### FAQ

**Does this replace Face Recognition?** No. Use [Face Recognition](../face-recognition-sdk/) for faces.

**Is there a Docker HTTP API?** Not in this sample. Commercial face/document server SDKs are Docker Hub images under each product’s Server SDK.

### Use cases

* **Access control demo** — extract palm ROI and match templates in Python on your machine
* **Attendance prototype** — compare two palm images with `compare_two_images`
* **R&D** — evaluate palm matching before choosing a commercial face product

### Related documentation

* [Open-source Palm Recognition setup](open-source-palm-recognition-sdk.md)
* [Face Recognition SDK](../face-recognition-sdk/) · [Request a License](../request-a-license-and-support.md)
