---
description: >-
  Faceplugin Face Recognition SDK for Linux Docker. Combined on-premise recognition and
  liveness HTTP API. Image face-recognition-liveness-sdk, port 8083.
---

# Face Recognition SDK Linux (Recognition + Liveness)

Fully on-premise **combined Face Recognition + Liveness** Linux App. One license (application id **1000**), two model packs (`far.fpk` + `fal.fpk`). Docker image: `faceplugin/face-recognition-liveness-sdk`. Port **8083**. Gradio **9003**. CPU only.

This is **not** the older single-product repos [FaceRecognition-Docker](https://github.com/Faceplugin-ltd/FaceRecognition-Docker) or [FaceLivenessDetection-Docker](https://github.com/Faceplugin-ltd/FaceLivenessDetection-Docker).

All processing stays on your server. **No** biometric data is sent to Faceplugin cloud.

{% hint style="info" %}
`./run.sh` / Docker set `LD_PRELOAD` of the wrapper. That is required for liveness VFS hooks. Native libraries are **linux/amd64**. Apple Silicon Docker uses amd64 emulation.
{% endhint %}

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognitionSDK-Linux" %}

### Setup <a href="#setup" id="setup"></a>

{% stepper %}
{% step %}
## Pull Docker Hub (no Drive)

```
sudo docker pull faceplugin/face-recognition-liveness-sdk:latest
sudo docker run -d --name faceplugin-face-recognition-liveness \
  --shm-size=2gb --privileged \
  -p 8083:8083 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/face-recognition-liveness-sdk:latest
```

On Docker Desktop (macOS/Windows) omit the `/etc/machine-id` volume.

The API starts even if activation fails. Copy `FPMC1.…` from `docker logs`.
{% endstep %}

{% step %}
## Confirm health (no license yet)

```
curl -s http://127.0.0.1:8083/api/health
```
{% endstep %}

{% step %}
## Activate

```
curl -s http://127.0.0.1:8083/api/machinecode
curl -s -X POST http://127.0.0.1:8083/api/activate \
  -H 'Content-Type: text/plain' \
  --data-binary @license.txt
```

Docker and local host codes are **different**.
{% endstep %}
{% endstepper %}

**Native (optional):** put files from [Drive](https://drive.google.com/drive/folders/1Lzz3eb_JMDZ0xyGtnGzxsUmMbgaYzin6) **directly** in `lib/cpu/` (`libFaceRecognitionSDK.so`, `libfar-eng.so`, `far.fpk`, `libfal-eng.so`, `fal.fpk`, …). Wrong layout: `lib/cpu/SomeFolder/…`. Then `pip3 install -r requirements.txt` and `./run.sh`. Local `./run.sh` wants glibc **2.38+** (e.g. Ubuntu 24.04).

**Several containers, one license (Linux host):** mount `/etc/machine-id` into each container and use different host ports. On Docker Desktop each container may need its own license.

| Item | Minimum | Recommended |
| ---- | ------- | ----------- |
| CPU | 2 cores | 4 cores |
| RAM | 4 GB | 8 GB |
| Disk | 4 GB | 8 GB |

### License

After `GET /api/licenseStatus`:

| Capability | Meaning |
| ---------- | ------- |
| **Recognition + Liveness** | Detect / Quality / Match **and** `/api/liveness` |
| **Recognition only** | Detect / Quality / Match; Liveness stays unavailable |
| **Liveness only** | Liveness; Detect / Quality / Match stay unavailable |
| **Not licensed** | Machine code only until you activate |

[Request a License & Support](../request-a-license-and-support.md).

### Try it

```bash
curl -s http://127.0.0.1:8083/api/health
IMG=$(base64 -w0 face.jpg)   # macOS: base64 -i face.jpg

curl -s -X POST http://127.0.0.1:8083/api/detect \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"

curl -s -X POST http://127.0.0.1:8083/api/liveness \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"
```

**Postman:** import `postman/FaceRecognition-API.postman_collection.json`. Base URL `http://127.0.0.1:8083`. Paths have **no** `/v1`.

**Gradio (host only):** the Docker image is API-only.

```
pip3 install -r requirements-demo.txt
DEMO_PORT=9003 API_BASE=http://127.0.0.1:8083 python3 demo.py
```

Open [http://127.0.0.1:9003](http://127.0.0.1:9003). Tabs: Detect, Quality, Match, Liveness.

<p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/desktop/demo-ui-detect.png" alt="Faceplugin Face Recognition SDK Linux Detect tab" width="720"/></p>

<p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-liveness/desktop/demo-ui.png" alt="Faceplugin Face Recognition SDK Linux Liveness tab" width="720"/></p>

### Integrate into your own app

| Path | When to use |
| ---- | ----------- |
| **HTTP** (`app.py`) | Any language. Keep this API running and `POST` base64 JPEGs. |
| **`sdk.py`** | Python on the **same** Linux host as `lib/cpu/` (or inside the container). Set `LD_LIBRARY_PATH` and `LD_PRELOAD` the same way `./run.sh` does. |

You do **not** need Gradio in production.

### APIs

All Face Recognition routes from [Linux SDK](face-recognition-linux-sdk.md) **plus**:

#### <mark style="color:orange;">check_liveness:</mark> This API is used to determine if the faces are real or fake

{% tabs %}
{% tab title="JSON" %}
```http
POST /api/liveness
Content-Type: application/json

{"image":"<BASE64-JPEG>"}
```
{% endtab %}
{% tab title="form-data" %}
File field `image` (alias `file`). Same URL. Alias path: `POST /api/check_liveness`.
{% endtab %}
{% endtabs %}

| **Input**        | JPEG image (base64 JSON or form-data). |
| ---------------- | --------------------------------------- |
| **Return value** | Engine JSON. Score **≥ 0.5** → <code>result</code> Real and <code>pass</code> true. |

Python:

```python
import sdk

print(sdk.get_machine_code())
sdk.activate("license.txt")
sdk.init_sdk()
print(sdk.get_license_status())
print(sdk.detect(base64_image))
print(sdk.liveness(base64_image))
```

Call order: `get_machine_code` → `activate` → `init_sdk` → detect / quality / feature / match / similarity / liveness.

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
