---
description: >-
  Faceplugin Face Recognition SDK for Windows. Combined on-premise recognition and liveness
  HTTP API on port 8083. detect, match, and POST /api/liveness.
---

# Face Recognition SDK Windows (Recognition + Liveness)

Fully on-premise **combined Face Recognition + Liveness** Windows App. Same HTTP surface as [Face Recognition SDK Linux (Recognition + Liveness)](face-recognition-sdk-linux.md). Port **8083**. Gradio **9003**. **No Docker** on Windows.

One license (application id **1000**), two model packs (`far.fpk` + `fal.fpk`).

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognitionSDK-Windows" %}

### Setup <a href="#setup" id="setup"></a>

{% stepper %}
{% step %}
## Copy the runtime

Put every file from [Google Drive](https://drive.google.com/drive/folders/1twWrWO-F4lEnyMxBt-UtLTsQToqsQ-Xd) **directly** into `lib\cpu\` (not a nested folder).
{% endstep %}

{% step %}
## Run the API

```
pip install -r requirements.txt
run.bat
```
{% endstep %}

{% step %}
## Activate

```
curl -s http://127.0.0.1:8083/api/machinecode
curl -s -X POST http://127.0.0.1:8083/api/activate ^
  -H "Content-Type: text/plain" ^
  --data-binary @license.txt
```
{% endstep %}
{% endstepper %}

License **level** unlocks Recognition only, Liveness only, or both. Check `GET /api/licenseStatus`.

### Try it

Same curl / Postman / Gradio flow as Linux, on `http://127.0.0.1:8083`. Import `postman/FaceRecognition-API.postman_collection.json`. Gradio on **9003** (host only). Score **≥ 0.5** → Real.

### APIs

Recognition routes: `POST /api/detect`, `/api/quality`, `/api/feature`, `/api/match`, `/api/similarity`.

#### <mark style="color:orange;">check_liveness:</mark> This API is used to determine if the faces are real or fake

```http
POST /api/liveness
```

Alias: `POST /api/check_liveness`. Python: `sdk.liveness`.

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
