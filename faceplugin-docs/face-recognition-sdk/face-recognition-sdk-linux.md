---
description: >-
  Faceplugin Face Recognition SDK Linux Docker — recognition and face liveness in one container.
  faceplugin/face-recognition-liveness-sdk on port 8083. detect, match, liveness.
---

# Face Recognition + Liveness Linux SDK

Fully on-premise **Face Recognition + Face Liveness API for Linux / Docker** in **one** App. Image: `faceplugin/face-recognition-liveness-sdk`. Default port **8083**. Gradio **9003**.

One wrapper (`libFaceRecognitionSDK.so`), one license, two model packs (`far.fpk` + `fal.fpk`). Your license can unlock Recognition only, Liveness only, or both.

This is **not** the recognition-only [Face Recognition Linux SDK](face-recognition-linux-sdk.md) (`faceplugin/face-recognition`). It is **not** the PAD-only [Face Liveness Detection Linux SDK](../liveness-detection-sdk/liveness-detection-linux-sdk.md) (port **8084**). Do not merge Drive folders into one `lib/cpu/`.

All processing stays on your server. **No** biometric data is sent to Faceplugin cloud.

### Code <a href="#code" id="code"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognitionSDK-Linux" %}

### Setup <a href="#setup" id="setup"></a>

{% stepper %}
{% step %}
## Pull Docker Hub (no Drive)

```
sudo docker pull faceplugin/face-recognition-liveness-sdk:latest
sudo docker run -d --name faceplugin-face-recognition-liveness-sdk \
  --shm-size=2gb --privileged \
  -p 8083:8083 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/face-recognition-liveness-sdk:latest
```

On Docker Desktop (macOS/Windows) omit the `/etc/machine-id` volume. Port **8083** is shared with recognition-only — run **one** Face Recognition container at a time.
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

Send `FPMC1.…` to Faceplugin. Docker and host machine codes differ.
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
Control routes (`/api/health`, `/api/machinecode`, `/api/activate`, `/api/licenseStatus`) return a JSON **envelope**. Process POSTs return **engine JSON** as the HTTP body. Native `./run.sh` sets `LD_PRELOAD` for liveness VFS hooks — Docker images already do this.
{% endhint %}

### APIs

Same recognition routes as [Face Recognition Linux SDK](face-recognition-linux-sdk.md), **plus** liveness:

| Endpoint | Purpose |
| -------- | ------- |
| `GET /api/health` | Process is listening (no license) |
| `GET /api/machinecode` | Machine code `FPMC1.…` |
| `GET /api/licenseStatus` | License capabilities |
| `GET /api/backend` | `"cpu"` |
| `POST /api/activate` | Activate and init |
| `POST /api/detect` | Detect faces |
| `POST /api/quality` | Quality checks |
| `POST /api/feature` | Extract template |
| `POST /api/match` | Compare two photos |
| `POST /api/similarity` | Compare two templates |
| `POST /api/liveness` | Passive face PAD |

There is **no** `POST /api/identify` (no server-side 1:N gallery). Store templates in **your** database and call `/api/similarity`.

### Try it

```bash
curl -s http://127.0.0.1:8083/api/health
IMG=$(base64 -w0 face.jpg)

curl -s -X POST http://127.0.0.1:8083/api/detect \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"

curl -s -X POST http://127.0.0.1:8083/api/liveness \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"
```

Score **≥ 0.5** → Real / pass (same threshold family as Face Liveness on **8084**).

Local Gradio: `DEMO_PORT=9003 API_BASE=http://127.0.0.1:8083 python3 demo.py` (Detect, Quality, Match, **Liveness**).

### FAQ

**Is this one container for recognition and PAD?** Yes. Image `faceplugin/face-recognition-liveness-sdk`, port **8083**, including `POST /api/liveness`.

**Prefer two separate products?** Use [Face Recognition Linux](face-recognition-linux-sdk.md) on **8083** and [Face Liveness Linux](../liveness-detection-sdk/liveness-detection-linux-sdk.md) on **8084**.

**Windows combined App?** [Face Recognition + Liveness Windows SDK](face-recognition-sdk-windows.md).

### Related documentation

* [Face Recognition Linux SDK](face-recognition-linux-sdk.md) (recognition only)
* [Face Liveness Detection Linux SDK](../liveness-detection-sdk/liveness-detection-linux-sdk.md)
* [Face Recognition Server SDK](server-sdk.md) · [Choose a product](../resources/choose-a-product.md)
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
