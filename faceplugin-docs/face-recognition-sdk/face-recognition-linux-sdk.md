---
description: >-
  Faceplugin Face Recognition Linux Docker SDK. Fully on-premise HTTP API on port 8083.
  detect, quality, feature, match, similarity. CPU only.
---

# Face Recognition Linux SDK

Fully on-premise **Face Recognition HTTP API for Linux / Docker**. Image: `faceplugin/face-recognition`. Default port **8083**. CPU only. Gradio demo (`demo.py`) on **9003** (host only).

This product is **recognition only**. For recognition **and** liveness in one App, use [Face Recognition SDK Linux (Recognition + Liveness)](face-recognition-sdk-linux.md).

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-Docker" %}

### Setup <a href="#setup" id="setup"></a>

1. Pull and run the Docker Hub image (no Drive required):

```
sudo docker pull faceplugin/face-recognition:latest
sudo docker run -d --name faceplugin-face-recognition \
  --shm-size=2gb --privileged \
  -p 8083:8083 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/face-recognition:latest
```

On Docker Desktop (macOS/Windows) omit the `/etc/machine-id` volume.

2. Confirm it is running: `curl -s http://127.0.0.1:8083/api/health` (no license needed).
3. Get machine code: `GET /api/machinecode` (`FPMC1.…`).
4. Contact us to get the license according to the machine code.
5. Activate: `POST /api/activate`.

Native (optional): put `libFaceRecognitionSDK.so`, `libfar-eng.so`, `far.fpk` from [Drive](https://drive.google.com/drive/folders/1NVq0psW8PLfEX58FWNE-RKFWfCZdOMmz) **directly** in `lib/cpu/`, then `./run.sh`. Local `./run.sh` wants glibc **2.38+** (e.g. Ubuntu 24.04).

JSON or `multipart/form-data` are accepted on process routes. Shared control routes return a JSON envelope. Process POSTs return **engine JSON**.

### APIs

#### <mark style="color:orange;">get_machine_code:</mark> This API is used to retrieve the code specific to the server

```http
GET /api/machinecode
```

| **Input**        | None |
| ---------------- | ---- |
| **Return value** | Envelope. <code>data.machinecode</code> is <code>FPMC1.…</code> |

Also: `GET /api/health`, `GET /api/licenseStatus`, `GET /api/backend` (`"cpu"`).

#### <mark style="color:orange;">activate_machine:</mark> This API is used to activate the SDK

```http
POST /api/activate
Content-Type: text/plain

FP1.…
```

JSON `{"license":"FP1.…"}` and a license file body are also accepted.

| **Input**        | License key or file |
| ---------------- | -------------------- |
| **Return value** | Envelope. On success the App also calls <code>init_sdk()</code>. |

#### <mark style="color:orange;">detect:</mark> This API is used to detect faces

```http
POST /api/detect
Content-Type: application/json

{"image":"<BASE64>","cropImage":false}
```

| **Input**        | Base64 image. Optional <code>cropImage</code> (alias <code>crop_image</code>). |
| ---------------- | ------------------------------------------------------------------------------ |
| **Return value** | Engine JSON (not the envelope).                                                  |

#### <mark style="color:orange;">quality:</mark> This API is used to run face image quality checks

```http
POST /api/quality
```

#### <mark style="color:orange;">feature:</mark> This API is used to extract a face template

```http
POST /api/feature
```

```json
{ "image": "<BASE64>" }
```

#### <mark style="color:orange;">match:</mark> This API is used to compare two photos (1:1)

```http
POST /api/match
```

```json
{ "image1": "<BASE64>", "image2": "<BASE64>", "cropImage": false }
```

#### <mark style="color:orange;">similarity:</mark> This API is used to compare two templates

```http
POST /api/similarity
```

```json
{ "feature1": "<BASE64>", "feature2": "<BASE64>" }
```

There is **no** `POST /api/identify` (no server-side 1:N gallery).

Python:

```python
import sdk

sdk.activate("license.txt")
sdk.init_sdk()
print(sdk.detect(base64_image))
print(sdk.match(image1, image2))
```
