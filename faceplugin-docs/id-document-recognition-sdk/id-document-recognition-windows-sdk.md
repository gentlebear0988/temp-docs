---
description: >-
  Faceplugin ID Document Recognition Windows SDK. Fully on-premise OCR and authenticity
  HTTP API on port 8082. documentRecognition, documentProcess.
---

# ID Document Recognition Windows SDK

Fully on-premise **ID Document Recognition HTTP API for Windows**. Default port **8082**. Gradio **9002**. No Docker on Windows — use [Linux SDK](id-document-recognition-linux-sdk.md) for Docker.

Reads ID cards, passports, and driver licenses. Same routes as [ID Document Recognition Linux SDK](id-document-recognition-linux-sdk.md). Parse results with [Document result JSON](document-result-json.md).

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Windows" %}

### Setup <a href="#setup" id="setup"></a>

{% stepper %}
{% step %}
## Copy the runtime

Copy the CPU libraries from [Google Drive](https://drive.google.com/drive/folders/1YfHUwnXO0E2NSvS_81nTNO2z3mKVO85g) into `lib\cpu\`.
{% endstep %}

{% step %}
## Install and run

```
pip install -r requirements.txt
run.bat
```

Demo UI: `run_demo.bat` after the API is up.
{% endstep %}

{% step %}
## Copy the machine code and activate

```
curl -s http://127.0.0.1:8082/api/machinecode
curl -s -X POST http://127.0.0.1:8082/api/activate \
  -H 'Content-Type: text/plain' \
  --data-binary @license.txt
```
{% endstep %}
{% endstepper %}

### APIs

Same as [ID Document Recognition Linux SDK](id-document-recognition-linux-sdk.md):

| Endpoint | Purpose |
| -------- | ------- |
| `GET /api/health` | Process is listening (no license) |
| `GET /api/machinecode` | Machine code `FPMC1.…` |
| `GET /api/licenseStatus` | License status |
| `POST /api/activate` | Activate and `init_sdk()` |
| `POST /api/documentRecognition` | OCR / MRZ / barcode / image quality only |
| `POST /api/documentLiveness` | Authenticity only |
| `POST /api/documentProcess` | Combined pipeline |
| `POST /api/generalProcess` | Single-image general process |

Python: `sdk.document_recognition`, `sdk.document_liveness`, `sdk.document_process`, `sdk.general_process`, plus `start_new_session`, `start_new_page`, `unload` (not HTTP routes).

`documentRecognition` is OCR / MRZ / barcode / image quality only. `documentLiveness` is authenticity only. Combined flags stay on `documentProcess`: `"normal"` or `"strict"` (Windows README); `"none"` turns Liveness off. Image quality is `"none"` | `"normal"` like OCR.

### Try it

```bash
curl -s http://127.0.0.1:8082/api/health
IMG=$(base64 -w0 id-front.jpg)

curl -s -X POST http://127.0.0.1:8082/api/documentProcess \
  -H 'Content-Type: application/json' \
  -d "{\"images\":[{\"image\":\"$IMG\",\"page_idx\":0}],\"response\":{\"OCR\":\"normal\",\"Authenticity\":\"normal\"}}"
```

**Postman:** import `postman/DocumentReader-API.postman_collection.json` from the repo. Base URL `http://127.0.0.1:8082`. Gradio **9002**. Authenticity names: [Document security check fields](document-security-check-fields.md).

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
