---
description: >-
  Faceplugin Face Recognition SDK for Linux Docker. Combined on-premise recognition and
  liveness HTTP API. Image face-recognition-liveness-sdk, port 8083.
---

# Face Recognition SDK Linux (Recognition + Liveness)

Fully on-premise **combined Face Recognition + Liveness** Linux App. One license (application id **1000**), two model packs (`far.fpk` + `fal.fpk`). Docker image: `faceplugin/face-recognition-liveness-sdk`. Port **8083**. Gradio **9003**.

This is **not** the older single-product repos [FaceRecognition-Docker](https://github.com/Faceplugin-ltd/FaceRecognition-Docker) or [FaceLivenessDetection-Docker](https://github.com/Faceplugin-ltd/FaceLivenessDetection-Docker).

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognitionSDK-Linux" %}

### Setup <a href="#setup" id="setup"></a>

```
sudo docker pull faceplugin/face-recognition-liveness-sdk:latest
sudo docker run -d --name faceplugin-face-recognition-liveness \
  --shm-size=2gb --privileged \
  -p 8083:8083 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/face-recognition-liveness-sdk:latest
```

Native: [Drive](https://drive.google.com/drive/folders/1Lzz3eb_JMDZ0xyGtnGzxsUmMbgaYzin6) → `lib/cpu/`. `./run.sh` / Docker set `LD_PRELOAD` for liveness VFS hooks.

License **level** unlocks Recognition only, Liveness only, or both. Check `GET /api/licenseStatus`.

### APIs

All Face Recognition routes from [Linux SDK](face-recognition-linux-sdk.md) **plus**:

#### <mark style="color:orange;">check_liveness:</mark> This API is used to determine if the faces are real or fake

```http
POST /api/liveness
Content-Type: application/json

{"image":"<BASE64-JPEG>"}
```

Alias: `POST /api/check_liveness`. Score **≥ 0.5** → `result` Real and `pass` true.

Python: `sdk.detect`, `sdk.quality`, `sdk.match`, `sdk.feature`, `sdk.similarity`, `sdk.liveness`.
