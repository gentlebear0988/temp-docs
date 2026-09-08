---
description: >-
  Faceplugin Face Recognition SDK for Windows. Combined on-premise recognition and liveness
  HTTP API on port 8083. detect, match, and POST /api/liveness.
---

# Face Recognition SDK Windows (Recognition + Liveness)

Fully on-premise **combined Face Recognition + Liveness** Windows App. Same HTTP surface as [Face Recognition SDK Linux (Recognition + Liveness)](face-recognition-sdk-linux.md). Port **8083**. Gradio **9003**. No Docker.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognitionSDK-Windows" %}

### Setup <a href="#setup" id="setup"></a>

1. Copy the CPU runtime from [Google Drive](https://drive.google.com/drive/folders/1twWrWO-F4lEnyMxBt-UtLTsQToqsQ-Xd) into `lib\cpu\`.
2. `pip install -r requirements.txt` then `run.bat`.
3. `GET /api/machinecode` → request `FP1.…` → `POST /api/activate`.

### APIs

Recognition routes: `POST /api/detect`, `/api/quality`, `/api/feature`, `/api/match`, `/api/similarity`.

#### <mark style="color:orange;">check_liveness:</mark> This API is used to determine if the faces are real or fake

```http
POST /api/liveness
```

Alias: `POST /api/check_liveness`. Python: `sdk.liveness`.
