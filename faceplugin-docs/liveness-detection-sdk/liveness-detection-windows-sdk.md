---
description: >-
  Faceplugin Face Liveness Detection Windows SDK. Fully on-premise PAD HTTP API on port 8084.
  POST /api/liveness. No Docker.
---

# Face Liveness Detection Windows SDK

Fully on-premise **Face Liveness HTTP API for Windows**. Default port **8084**. Gradio **9004**. No Docker on Windows.

Score **one RGB JPEG**. Score **≥ 0.5** → Real / `pass` true. Same HTTP API as [Face Liveness Detection Linux SDK](liveness-detection-linux-sdk.md). `POST /api/check_liveness` is an alias of `/api/liveness`.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceLivenessDetection-Windows" %}

### Setup <a href="#setup" id="setup"></a>

{% stepper %}
{% step %}
## Copy the runtime

Copy the CPU libraries from [Google Drive](https://drive.google.com/drive/folders/11xD987eHT00NUGiJZCNYSvwRadi0Nue5) into `lib\cpu\`.
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
curl -s http://127.0.0.1:8084/api/machinecode
```

Send `FPMC1.…` to Faceplugin.
{% endstep %}

{% step %}
## Activate, then check liveness

```
curl -s -X POST http://127.0.0.1:8084/api/activate \
  -H 'Content-Type: text/plain' \
  --data-binary @license.txt

IMG=$(base64 -w0 face.jpg)
curl -s -X POST http://127.0.0.1:8084/api/liveness \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"
```
{% endstep %}
{% endstepper %}

### APIs

#### <mark style="color:orange;">get_machine_code:</mark> This API is used to retrieve the code specific to the server

```http
GET /api/machinecode
```

| **Input**        | None |
| ---------------- | ---- |
| **Return value** | Envelope. <code>data.machinecode</code> is <code>FPMC1.…</code> |

Also: `GET /api/health`, `GET /api/licenseStatus`, `GET /api/backend`.

#### <mark style="color:orange;">activate_machine:</mark> This API is used to activate the SDK

```http
POST /api/activate
```

| **Input**        | Plain <code>FP1.…</code>, JSON <code>{"license":"FP1.…"}</code>, or a license file |
| ---------------- | ------------------------------------------------------------------------------------ |
| **Return value** | Envelope. On success the HTTP service also calls <code>init_sdk()</code>.                  |

#### <mark style="color:orange;">check_liveness:</mark> This API is used to determine if the faces are real or fake

```http
POST /api/liveness
Content-Type: application/json

{"image":"<BASE64-JPEG>"}
```

File field `image` (alias `file`) is accepted as `multipart/form-data`. Same URL.

| **Input**        | JPEG image (base64 JSON or form-data). |
| ---------------- | --------------------------------------- |
| **Return value** | Engine JSON. Score **≥ 0.5** → <code>result</code> Real and <code>pass</code> true. |

Python: `sdk.get_machine_code()`, `sdk.activate`, `sdk.init_sdk()`, `sdk.liveness`.

### Try it

```bash
curl -s http://127.0.0.1:8084/api/health
IMG=$(base64 -w0 face.jpg)

curl -s -X POST http://127.0.0.1:8084/api/liveness \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"
```

**Postman:** import `postman/FaceLiveness-API.postman_collection.json` from the repo. Base URL `http://127.0.0.1:8084`.

**Gradio (host only):** `DEMO_PORT=9004 API_BASE=http://127.0.0.1:8084 python demo.py`.

[Request a License & Support](../request-a-license-and-support.md) · [Contact us](../contact-us.md)

### FAQ

**API?** Same as Linux: `POST /api/liveness` on port **8084**. No Docker on Windows.

**Active liveness?** No. This product is passive JPEG anti-spoofing only.

### Related documentation

* [Faceplugin Face Liveness Detection Server SDK](server-sdk.md) · [Linux](liveness-detection-linux-sdk.md)
* [Face Recognition Windows SDK](../face-recognition-sdk/face-recognition-windows-sdk.md)
* [ID Document Recognition Windows SDK](../id-document-recognition-sdk/id-document-recognition-windows-sdk.md)
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/README.md)
