---
description: >-
  Faceplugin ID Document Recognition Linux Docker SDK. Fully on-premise OCR and
  authenticity HTTP API on port 8082. documentRecognition, documentProcess.
---

# ID Document Recognition Linux SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Docker" %}

### Setup <a href="#setup" id="setup"></a>

1. Pull and run the Docker Hub image:

```
sudo docker pull faceplugin/document-reader:latest
sudo docker run -d --name faceplugin-document-reader \
  --shm-size=2gb --privileged \
  -p 8082:8082 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/document-reader:latest
```

`--shm-size=2gb` is required. On Docker Desktop omit the `/etc/machine-id` volume.

2. Health (no license): `curl -s http://127.0.0.1:8082/api/health`
3. Get machine code: `GET /api/machinecode`
4. Contact us for `FP1.…`, then `POST /api/activate`

Native: put `libDocSDK.so`, `libDocumentEngine.so`, `dcr.fpk` from [Drive](https://drive.google.com/drive/folders/16DFGKtyGbyL-0gfVOmNVaQ9vgXCYDr2M) **directly** in `lib/cpu/`, then `./run.sh`.

Default port **8082**. Gradio demo on **9002** (host only).

### APIs

#### <mark style="color:orange;">get_machine_code:</mark> This API is used to retrieve the code specific to the server

```http
GET /api/machinecode
```

Also: `GET /api/health`, `GET /api/licenseStatus`, `GET /api/backend`.

#### <mark style="color:orange;">activate_machine:</mark> This API is used to activate the SDK

```http
POST /api/activate
```

| **Input**        | Plain <code>FP1.…</code>, JSON <code>{"license":"FP1.…"}</code>, or a license file |
| ---------------- | ------------------------------------------------------------------------------------ |
| **Return value** | Envelope. On success the App also calls <code>init_sdk()</code>.                  |

#### <mark style="color:orange;">documentRecognition:</mark> This API is used to run OCR / MRZ / barcode / image quality only

```http
POST /api/documentRecognition
```

```json
{
  "images": [
    { "image": "<BASE64>", "page_idx": 0 },
    { "image": "<BASE64>", "page_idx": 1 }
  ]
}
```

| **Input**        | One or more page images (base64). Authenticity is always off. |
| ---------------- | ------------------------------------------------------------- |
| **Return value** | Engine JSON (not the envelope).                                 |

#### <mark style="color:orange;">documentLiveness:</mark> This API is used to run authenticity / security only

```http
POST /api/documentLiveness
```

| **Input**        | One or more page images (base64). OCR / MRZ / barcode / image quality are always off. |
| ---------------- | -------------------------------------------------------------------------------------- |
| **Return value** | Engine JSON with <code>security</code> checks when the license includes Liveness.     |

#### <mark style="color:orange;">documentProcess:</mark> This API is used to run the combined OCR / MRZ / barcode / image quality / authenticity pipeline

```http
POST /api/documentProcess
```

```json
{
  "images": [
    { "image": "<BASE64>", "page_idx": 0 }
  ],
  "response": {
    "OCR": "normal",
    "MRZ": "normal",
    "Barcode": "normal",
    "ImageQuality": "normal",
    "Authenticity": "normal"
  }
}
```

- `"Authenticity": "none"` skips liveness checks. `"normal"` runs them when the license includes Liveness.
- `"ImageQuality": "none"` skips capture-quality checks.

| **Input**        | One or more page images (base64) and optional <code>response</code> flags. |
| ---------------- | ----------------------------------------------------------------------------- |
| **Return value** | Engine JSON (not the envelope).                                                |

#### <mark style="color:orange;">generalProcess:</mark> This API is used for a single-image general process

```http
POST /api/generalProcess
```

```json
{ "image": "<BASE64>", "options": {} }
```

Python:

```python
import sdk

sdk.activate("license.txt")
sdk.init_sdk()
print(sdk.document_recognition([{"image": base64_front}]))
print(sdk.document_process(images, options={"response": {"OCR": "normal", "Authenticity": "normal"}}))
```
