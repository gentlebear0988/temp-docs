---
description: >-
  Faceplugin ID Document Recognition Windows SDK. Fully on-premise OCR and authenticity
  HTTP API on port 8082. documentRecognition, documentProcess.
---

# ID Document Recognition Windows SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Windows" %}

### Setup <a href="#setup" id="setup"></a>

1. Copy the runtime from [Google Drive](https://drive.google.com/drive/folders/1YfHUwnXO0E2NSvS_81nTNO2z3mKVO85g) into `lib\cpu\`.
2. Install and run:

```
pip install -r requirements.txt
run.bat
```

3. Copy `FPMC1.…` from the terminal or `GET /api/machinecode`, request `FP1.…`, then `POST /api/activate`.

No Docker on Windows. API **8082**. Gradio **9002**.

### APIs

Same as [ID Document Recognition Linux SDK](id-document-recognition-linux-sdk.md):

| Endpoint | Purpose |
| -------- | ------- |
| `GET /api/health` | Process is listening (no license) |
| `GET /api/machinecode` | Machine code `FPMC1.…` |
| `GET /api/licenseStatus` | License tier (`recognition` / `authenticity`) |
| `POST /api/activate` | Activate and `init_sdk()` |
| `POST /api/documentRecognition` | OCR / MRZ / barcode / image quality only |
| `POST /api/documentLiveness` | Authenticity only |
| `POST /api/documentProcess` | Combined pipeline |
| `POST /api/generalProcess` | Single-image general process |

Python: `sdk.document_recognition`, `sdk.document_liveness`, `sdk.document_process`, `sdk.general_process`.

### Try it

Same routes as [ID Document Recognition Linux SDK](id-document-recognition-linux-sdk.md) on port **8082**. Import `postman/DocumentReader-API.postman_collection.json`. Gradio **9002**. Parse results with [Document result JSON](document-result-json.md).

Windows also documents authenticity `"strict"` in addition to `"normal"` / `"none"`.

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
