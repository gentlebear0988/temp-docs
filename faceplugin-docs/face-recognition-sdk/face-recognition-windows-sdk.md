---
description: >-
  Faceplugin Face Recognition Windows SDK. Fully on-premise HTTP API on port 8083. detect,
  quality, feature, match, similarity. No Docker.
---

# Face Recognition Windows SDK

Fully on-premise **commercial Face Recognition HTTP API for Windows**. Default port **8083**. Gradio **9003**. No Docker on Windows.

This is not the [Open Source Face Recognition Windows SDK](open-source-face-recognition-windows-sdk.md). For recognition **and** liveness in one App, use [Face Recognition SDK Windows (Recognition + Liveness)](face-recognition-sdk-windows.md).

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-Windows" %}

### Setup <a href="#setup" id="setup"></a>

1. Copy the runtime from [Google Drive](https://drive.google.com/drive/folders/12i5d2-TahuJumre2EVYqWO8cIi_unTBz) into `lib\cpu\`.
2. Install and run:

```
pip install -r requirements.txt
run.bat
```

3. Copy `FPMC1.…` from the terminal or `GET /api/machinecode`, request `FP1.…`, then `POST /api/activate`.

### APIs

Same routes as [Face Recognition Linux SDK](face-recognition-linux-sdk.md):

| Endpoint | Purpose |
| -------- | ------- |
| `GET /api/health` | Process is listening (no license) |
| `GET /api/machinecode` | Machine code `FPMC1.…` |
| `GET /api/licenseStatus` | License tier |
| `GET /api/backend` | `"cpu"` |
| `POST /api/activate` | Activate and `init_sdk()` |
| `POST /api/detect` | Detect faces |
| `POST /api/quality` | Quality checks |
| `POST /api/feature` | Extract template |
| `POST /api/match` | Compare two photos |
| `POST /api/similarity` | Compare two templates |

There is **no** `POST /api/identify`.

Python: `sdk.detect`, `sdk.quality`, `sdk.feature`, `sdk.match`, `sdk.similarity`.

### Try it

```bash
curl -s http://127.0.0.1:8083/api/health
IMG=$(base64 -w0 face.jpg)

curl -s -X POST http://127.0.0.1:8083/api/detect \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"
```

**Postman:** import `postman/FaceRecognition-API.postman_collection.json` from the repo. **Gradio (host only):** `DEMO_PORT=9003 API_BASE=http://127.0.0.1:8083 python demo.py`.

Control routes return a JSON **envelope**. Process POSTs return **engine JSON**. There is **no** `POST /api/identify` (no server-side 1:N gallery). Store templates in **your** database and call `/api/similarity`.

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
