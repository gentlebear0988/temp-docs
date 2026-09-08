---
description: >-
  Faceplugin Liveness Detection Windows SDK. Fully on-premise PAD HTTP API on port 8084.
  POST /api/liveness. CPU only, no Docker.
---

# Liveness Detection Windows SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceLivenessDetection-Windows" %}

### Setup <a href="#setup" id="setup"></a>

1. Copy the CPU runtime from [Google Drive](https://drive.google.com/drive/folders/11xD987eHT00NUGiJZCNYSvwRadi0Nue5) into `lib\cpu\`.
2. Install and run:

```
pip install -r requirements.txt
run.bat
```

3. Copy `FPMC1.…` from the terminal or `GET /api/machinecode`, request `FP1.…`, then `POST /api/activate`.

No Docker on Windows. API **8084**. Gradio **9004**. CPU only.

Same HTTP API as [Liveness Detection Linux SDK](liveness-detection-linux-sdk.md). `POST /api/check_liveness` is an alias of `/api/liveness`.

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
| **Return value** | Envelope. On success the App also calls <code>init_sdk()</code>.                  |

#### <mark style="color:orange;">check_liveness:</mark> This API is used to determine if the faces are real or fake

```http
POST /api/liveness
Content-Type: application/json

{"image":"<BASE64-JPEG>"}
```

| **Input**        | JPEG image (base64 JSON or form-data). |
| ---------------- | --------------------------------------- |
| **Return value** | Engine JSON. Score **≥ 0.5** → <code>result</code> Real and <code>pass</code> true. |

Python: `sdk.get_machine_code()`, `sdk.activate`, `sdk.init_sdk()`, `sdk.liveness`.

### Try it

Same HTTP API as [Liveness Detection Linux SDK](liveness-detection-linux-sdk.md) on port **8084**. Gradio **9004**. Score **≥ 0.5** → Real.

```
pip install -r requirements.txt
run.bat
```

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
