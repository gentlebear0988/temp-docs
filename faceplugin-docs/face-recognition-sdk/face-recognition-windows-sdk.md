---
description: >-
  Faceplugin Face Recognition Windows SDK. Fully on-premise HTTP API on port 8083. detect,
  quality, feature, match, similarity. No Docker.
---

# Face Recognition Windows SDK

Fully on-premise **commercial Face Recognition HTTP API for Windows**. Default port **8083**. Gradio **9003**. No Docker on Windows.

This is not the [Open Source Face Recognition Windows SDK](open-source-face-recognition-windows-sdk.md). For recognition **and** liveness in one App, use [Face Recognition SDK Windows (Recognition + Liveness)](face-recognition-sdk-windows.md).

All processing stays on your server. **No** biometric data is sent to Faceplugin cloud.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-Windows" %}

### Setup <a href="#setup" id="setup"></a>

{% stepper %}
{% step %}
## Copy the runtime

Copy the CPU libraries from [Google Drive](https://drive.google.com/drive/folders/12i5d2-TahuJumre2EVYqWO8cIi_unTBz) into `lib\cpu\`.
{% endstep %}

{% step %}
## Install and run

```
pip install -r requirements.txt
run.bat
```
{% endstep %}

{% step %}
## Copy the machine code

```
curl -s http://127.0.0.1:8083/api/machinecode
```

Send `FPMC1.…` to Faceplugin. Copy it from the terminal if curl is not available.
{% endstep %}

{% step %}
## Activate

```
curl -s -X POST http://127.0.0.1:8083/api/activate \
  -H 'Content-Type: text/plain' \
  --data-binary @license.txt
```
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Control routes (`/api/health`, `/api/machinecode`, `/api/activate`, `/api/licenseStatus`) return a JSON **envelope**. Process POSTs (`/api/detect`, `/api/quality`, …) return **engine JSON** as the HTTP body.
{% endhint %}

### APIs

Same routes as [Face Recognition Linux SDK](face-recognition-linux-sdk.md):

| Endpoint | Purpose |
| -------- | ------- |
| `GET /api/health` | Process is listening (no license) |
| `GET /api/machinecode` | Machine code `FPMC1.…` |
| `GET /api/licenseStatus` | License status |
| `GET /api/backend` | `"cpu"` |
| `POST /api/activate` | Activate and `init_sdk()` |
| `POST /api/detect` | Detect faces |
| `POST /api/quality` | Quality checks |
| `POST /api/feature` | Extract template |
| `POST /api/match` | Compare two photos |
| `POST /api/similarity` | Compare two templates |

There is **no** `POST /api/identify` (no server-side 1:N gallery). Store templates in **your** database and call `/api/similarity`.

Python: `sdk.detect`, `sdk.quality`, `sdk.feature`, `sdk.match`, `sdk.similarity`.

Call order: `get_machine_code` → `activate` → `init_sdk` → detect / quality / feature / match / similarity.

### Try it

```bash
curl -s http://127.0.0.1:8083/api/health
IMG=$(base64 -w0 face.jpg)

curl -s -X POST http://127.0.0.1:8083/api/detect \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"

curl -s -X POST http://127.0.0.1:8083/api/match \
  -H 'Content-Type: application/json' \
  -d "{\"image1\":\"$IMG\",\"image2\":\"$IMG\"}"
```

**Postman:** import `postman/FaceRecognition-API.postman_collection.json` from the repo. Base URL `http://127.0.0.1:8083`. Paths have **no** `/v1`.

**Gradio (host only):** `DEMO_PORT=9003 API_BASE=http://127.0.0.1:8083 python demo.py`. Open [http://127.0.0.1:9003](http://127.0.0.1:9003). You do **not** need Gradio in production.

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)


### FAQ

**Face Recognition API on Windows?** Yes. Port **8083**, same routes as Linux. No Docker.

**Offline?** Yes after `POST /api/activate` with an `FP1.…` bound to this host's `FPMC1.…`.

### Related documentation

* [Faceplugin Face Recognition Server SDK](server-sdk.md) · [Linux](face-recognition-linux-sdk.md)
* [Liveness Detection Windows SDK](../liveness-detection-sdk/liveness-detection-windows-sdk.md)
* [ID Document Recognition Windows SDK](../id-document-recognition-sdk/id-document-recognition-windows-sdk.md)
* [Combined Recognition + Liveness (Windows)](face-recognition-sdk-windows.md)
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/README.md)
