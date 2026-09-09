---
description: >-
  Faceplugin Face Recognition Linux Docker SDK. Fully on-premise HTTP API on port 8083.
  detect, quality, feature, match, similarity.
---

# Face Recognition Linux SDK

Fully on-premise **Face Recognition HTTP API for Linux / Docker**. Image: `faceplugin/face-recognition`. Default port **8083**.

This product is **recognition only**. For recognition **and** liveness in one App, use [Face Recognition SDK Linux (Recognition + Liveness)](face-recognition-sdk-linux.md).

All processing stays on your server. **No** biometric data is sent to Faceplugin cloud.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-Docker" %}

### Setup <a href="#setup" id="setup"></a>

{% stepper %}
{% step %}
## Pull Docker Hub (no Drive)

```
sudo docker pull faceplugin/face-recognition:latest
sudo docker run -d --name faceplugin-face-recognition \
  --shm-size=2gb --privileged \
  -p 8083:8083 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/face-recognition:latest
```

On Docker Desktop (macOS/Windows) omit the `/etc/machine-id` volume.
{% endstep %}

{% step %}
## Confirm health (no license yet)

```
curl -s http://127.0.0.1:8083/api/health
```
{% endstep %}

{% step %}
## Copy the machine code

```
curl -s http://127.0.0.1:8083/api/machinecode
```

Send `FPMC1.…` to Faceplugin. Docker and local host codes are **different**.
{% endstep %}

{% step %}
## Activate

Put your key in `license.txt`, then:

```
curl -s -X POST http://127.0.0.1:8083/api/activate \
  -H 'Content-Type: text/plain' \
  --data-binary @license.txt
```
{% endstep %}
{% endstepper %}

**Native (optional):** put `libFaceRecognitionSDK.so`, `libfar-eng.so`, `far.fpk` from [Drive](https://drive.google.com/drive/folders/1NVq0psW8PLfEX58FWNE-RKFWfCZdOMmz) **directly** in `lib/cpu/`, then `pip3 install -r requirements.txt` and `./run.sh`. Local `./run.sh` wants glibc **2.38+** (e.g. Ubuntu 24.04).

{% hint style="info" %}
Control routes (`/api/health`, `/api/machinecode`, `/api/activate`, `/api/licenseStatus`) return a JSON **envelope**. Process POSTs (`/api/detect`, `/api/quality`, …) return **engine JSON** as the HTTP body.
{% endhint %}

### License

Licenses are **offline**. [Request a License & Support](../request-a-license-and-support.md).

### Try it

```bash
curl -s http://127.0.0.1:8083/api/health
IMG=$(base64 -w0 face.jpg)   # macOS: base64 -i face.jpg

curl -s -X POST http://127.0.0.1:8083/api/detect \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"

curl -s -X POST http://127.0.0.1:8083/api/match \
  -H 'Content-Type: application/json' \
  -d "{\"image1\":\"$IMG\",\"image2\":\"$IMG\"}"
```

**Postman:** import `postman/FaceRecognition-API.postman_collection.json` from the repo. Base URL `http://127.0.0.1:8083`. Paths have **no** `/v1`.

**Gradio (host only):** the Docker image is API-only. On the host:

```
pip3 install -r requirements-demo.txt
DEMO_PORT=9003 API_BASE=http://127.0.0.1:8083 python3 demo.py
```

Open [http://127.0.0.1:9003](http://127.0.0.1:9003). Tabs: Detect, Quality, Match.

### Integrate into your own app

| Path | When to use |
| ---- | ----------- |
| **HTTP** (`app.py`) | Any language. Keep this API running and `POST` base64 JPEGs. |
| **`sdk.py`** | Python on the **same** Linux host as `lib/cpu/` (or inside the container). |

You do **not** need Gradio in production.

### APIs

#### <mark style="color:orange;">get_machine_code:</mark> This API is used to retrieve the code specific to the server

```http
GET /api/machinecode
```

| **Input**        | None |
| ---------------- | ---- |
| **Return value** | Envelope. <code>data.machinecode</code> is <code>FPMC1.…</code> |

Also: `GET /api/health` (`data.status` is `"ok"`), `GET /api/licenseStatus`, `GET /api/backend` (`"cpu"`).

#### <mark style="color:orange;">activate_machine:</mark> This API is used to activate the SDK

```http
POST /api/activate
Content-Type: text/plain

FP1.…
```

JSON `{"license":"FP1.…"}` and a license file body are also accepted. Empty body returns envelope `code: -1`.

| **Input**        | License key or file |
| ---------------- | -------------------- |
| **Return value** | Envelope. On success the App also calls <code>init_sdk()</code>. |

#### <mark style="color:orange;">detect:</mark> This API is used to detect faces

{% tabs %}
{% tab title="JSON" %}
```http
POST /api/detect
Content-Type: application/json

{"image":"<BASE64>","cropImage":false}
```
{% endtab %}
{% tab title="form-data" %}
File field `image` (alias `file`). Text field `cropImage` (`true` / `false`). Same URL.
{% endtab %}
{% endtabs %}

| **Input**        | Base64 image. Optional <code>cropImage</code> (alias <code>crop_image</code>). |
| ---------------- | ------------------------------------------------------------------------------ |
| **Return value** | Engine JSON (not the envelope). A gated call without a recognition license returns <code>code</code> 8 with <code>licenseError</code>. |

#### <mark style="color:orange;">quality:</mark> This API is used to run face image quality checks

```http
POST /api/quality
```

Same body as detect. ICAO-style checks. Python: `sdk.quality`.

#### <mark style="color:orange;">feature:</mark> This API is used to extract a face template

```http
POST /api/feature
```

```json
{ "image": "<BASE64>" }
```

Store the template in **your** database. Compare later with `/api/similarity`.

#### <mark style="color:orange;">match:</mark> This API is used to compare two photos (1:1)

```http
POST /api/match
```

```json
{ "image1": "<BASE64>", "image2": "<BASE64>", "cropImage": false }
```

The server detects and extracts internally.

#### <mark style="color:orange;">similarity:</mark> This API is used to compare two templates

```http
POST /api/similarity
```

```json
{ "feature1": "<BASE64>", "feature2": "<BASE64>" }
```

Aliases: `template1` / `template2`. Both features must decode to the **same length**. Form-data uses **text** fields (not files).

There is **no** `POST /api/identify` (no server-side 1:N gallery).

Python:

```python
import sdk

print(sdk.get_machine_code())
sdk.activate("license.txt")
sdk.init_sdk()
print(sdk.get_license_status())
print(sdk.detect(base64_image))
print(sdk.match(image1, image2))
```

Call order: `get_machine_code` → `activate` → `init_sdk` → detect / quality / feature / match / similarity.

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
