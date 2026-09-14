---
description: >-
  Faceplugin Face Recognition SDK Windows — recognition and face liveness in one process.
  HTTP API on port 8083 including POST /api/liveness. No Docker.
---

# Face Recognition + Liveness Windows SDK

Fully on-premise **Face Recognition + Face Liveness HTTP API for Windows** in **one** process. Default port **8083**. Gradio **9003**. No Docker on Windows.

One wrapper (`FaceRecognitionSDK.dll`), one license, two model packs (`far.fpk` + `fal.fpk`). Your license can unlock Recognition only, Liveness only, or both.

This is **not** the recognition-only [Face Recognition Windows SDK](face-recognition-windows-sdk.md). It is **not** the PAD-only [Face Liveness Detection Windows SDK](../liveness-detection-sdk/liveness-detection-windows-sdk.md) (port **8084**). Do not merge Drive folders into one `lib\cpu\`.

For Docker combined, use [Face Recognition + Liveness Linux SDK](face-recognition-sdk-linux.md) (`faceplugin/face-recognition-liveness-sdk`).

All processing stays on your machine. **No** biometric data is sent to Faceplugin cloud.

### Code <a href="#code" id="code"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognitionSDK-Windows" %}

### Setup <a href="#setup" id="setup"></a>

{% stepper %}
{% step %}
## Copy the runtime

Copy the CPU libraries from Drive into `lib\cpu\` (see the repo README for the current folder link).
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
Control routes return a JSON **envelope**. Process POSTs return **engine JSON**. Port **8083** is shared with recognition-only — run **one** Face Recognition App at a time.
{% endhint %}

### APIs

Same recognition routes as [Face Recognition Windows SDK](face-recognition-windows-sdk.md), **plus** liveness:

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

There is **no** `POST /api/identify` (no server-side 1:N gallery).

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

Local Gradio: `run_demo.bat` on **9003** (Detect, Quality, Match, **Liveness**).

### FAQ

**Is this one Windows process for recognition and PAD?** Yes. Public repo [FaceRecognitionSDK-Windows](https://github.com/Faceplugin-ltd/FaceRecognitionSDK-Windows), including `POST /api/liveness`.

**Prefer two separate products?** Use [Face Recognition Windows](face-recognition-windows-sdk.md) on **8083** and [Face Liveness Windows](../liveness-detection-sdk/liveness-detection-windows-sdk.md) on **8084**.

### Related documentation

* [Face Recognition Windows SDK](face-recognition-windows-sdk.md) (recognition only)
* [Face Recognition + Liveness Linux SDK](face-recognition-sdk-linux.md)
* [Face Liveness Detection Windows SDK](../liveness-detection-sdk/liveness-detection-windows-sdk.md)
* [Face Recognition Server SDK](server-sdk.md) · [Choose a product](../resources/choose-a-product.md)
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
