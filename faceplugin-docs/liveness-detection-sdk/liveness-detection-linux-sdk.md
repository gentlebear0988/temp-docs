---
description: >-
  Faceplugin Face Liveness API for Linux Docker. On-premise anti-spoofing PAD. POST
  /api/liveness on port 8084. Score 0.5 or higher is Real.
---

# Face Liveness Detection Linux SDK

Fully on-premise **Face Liveness HTTP API for Linux / Docker**. Image: `faceplugin/face-liveness`. Default port **8084**.

Score **one RGB JPEG**. Score **≥ 0.5** → Real / `pass` true. Score **&lt; 0.5** → Spoof / `pass` false.

Need recognition as well? Run [Face Recognition Linux SDK](../face-recognition-sdk/face-recognition-linux-sdk.md) on port **8083** as a **second** container.

All processing stays on your server. **No** biometric data is sent to Faceplugin cloud.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceLivenessDetection-Docker" %}

### Setup <a href="#setup" id="setup"></a>

{% stepper %}
{% step %}
## Pull from Docker Hub (no Google Drive download)

```
sudo docker pull faceplugin/face-liveness:latest
sudo docker run -d --name faceplugin-face-liveness \
  --shm-size=1gb --privileged \
  -p 8084:8084 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/face-liveness:latest
```

On Docker Desktop (macOS/Windows) omit the `/etc/machine-id` volume.
{% endstep %}

{% step %}
## Confirm health (no license yet)

```
curl -s http://127.0.0.1:8084/api/health
```
{% endstep %}

{% step %}
## Copy the machine code

```
curl -s http://127.0.0.1:8084/api/machinecode
```

Send `FPMC1.…` to Faceplugin. Docker and local host codes are **different**.
{% endstep %}

{% step %}
## Activate

Put your key in `license.txt`, then:

```
curl -s -X POST http://127.0.0.1:8084/api/activate \
  -H 'Content-Type: text/plain' \
  --data-binary @license.txt
```
{% endstep %}

{% step %}
## Check liveness

```
IMG=$(base64 -w0 face.jpg)   # macOS: base64 -i face.jpg

curl -s -X POST http://127.0.0.1:8084/api/liveness \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"
```
{% endstep %}
{% endstepper %}

**Native (optional):** put `libFaceLivenessSDK.so`, `libfal-eng.so`, `fal.fpk` from [Google Drive](https://drive.google.com/drive/folders/1rFnw7VASLmA4q8NWenQgszFS8njRGEgt) **directly** in `lib/cpu/`, then `./run.sh`.

Default port **8084**. Gradio demo (`demo.py`) on **9004** (host only). The Docker image is API-only.

`POST /api/check_liveness` is an alias of `/api/liveness`.

{% hint style="info" %}
Control routes (`/api/health`, `/api/machinecode`, `/api/activate`, `/api/licenseStatus`) return a JSON **envelope**. `POST /api/liveness` returns **engine JSON** as the HTTP body.
{% endhint %}

### License

Licenses are **offline**. [Request a License & Support](../request-a-license-and-support.md).

### APIs

#### <mark style="color:orange;">get_machine_code:</mark> This API is used to retrieve the code specific to the server on which this SDK is running <a href="#setactivation" id="setactivation"></a>

```http
GET /api/machinecode
```

| **Input**        | None                                                               |
| ---------------- | ------------------------------------------------------------------ |
| **Return value** | Envelope. <code>data.machinecode</code> is <code>FPMC1.…</code> |

Also: `GET /api/health` (no license), `GET /api/licenseStatus`, `GET /api/backend` (`"cpu"`).

#### <mark style="color:orange;">activate_machine:</mark> This API is used to activate the SDK <a href="#initsdk" id="initsdk"></a>

```http
POST /api/activate
Content-Type: text/plain

FP1.…
```

JSON `{"license":"FP1.…"}` and a license file body are also accepted.

| **Input**        | License key or file. |
| ---------------- | -------------------- |
| **Return value** | Envelope. Success: <code>code</code> 0, <code>"Successfully activated"</code>. On success the HTTP service also calls <code>init_sdk()</code>. |

#### <mark style="color:orange;">check_liveness:</mark> This API is used to determine if the faces are real or fake <a href="#facedetection" id="facedetection"></a>

```http
POST /api/liveness
Content-Type: application/json

{"image":"<BASE64-JPEG>"}
```

File field `image` (alias `file`) is accepted as `multipart/form-data`. Same URL. Alias: `POST /api/check_liveness`.

| **Input**        | JPEG image (base64 JSON or form-data). A missing <code>image</code> field returns envelope <code>code: -1</code> and <code>"image required"</code>. |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Return value** | Engine JSON. Score **≥ 0.5** → <code>result</code> Real and <code>pass</code> true. Score **&lt; 0.5** → <code>result</code> Spoof and <code>pass</code> false. |

Example:

```json
{ "score": 0.72, "result": "Real", "pass": true }
```

Python:

```python
import sdk

machine_code = sdk.get_machine_code()
sdk.activate("license.txt")
sdk.init_sdk()
print(sdk.liveness(base64_jpeg))
```

### Try it

```bash
curl -s http://127.0.0.1:8084/api/health
IMG=$(base64 -w0 face.jpg)

curl -s -X POST http://127.0.0.1:8084/api/liveness \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"
```

**Postman:** import `postman/FaceLiveness-API.postman_collection.json` from the repo. Base URL `http://127.0.0.1:8084`.

**Gradio (host only):**

```
pip3 install -r requirements-demo.txt
DEMO_PORT=9004 API_BASE=http://127.0.0.1:8084 python3 demo.py
```

Open [http://127.0.0.1:9004](http://127.0.0.1:9004). You do **not** need Gradio in production.

[Request a License & Support](../request-a-license-and-support.md) · [Contact us](../contact-us.md)

### FAQ

**Face Liveness API?** `POST /api/liveness` on port **8084**. Score **≥ 0.5** → Real.

**Machine code?** `GET /api/machinecode` returns `FPMC1.…`. Docker and host codes differ.

### Related documentation

* [Faceplugin Face Liveness Detection Server SDK](server-sdk.md) · [Windows](liveness-detection-windows-sdk.md)
* [Face Recognition Linux SDK](../face-recognition-sdk/face-recognition-linux-sdk.md)
* [ID Document Recognition Linux SDK](../id-document-recognition-sdk/id-document-recognition-linux-sdk.md)
* [ID Document Liveness Linux SDK](../id-document-liveness-sdk/id-document-liveness-linux-sdk.md)
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/README.md)
