---
description: >-
  Faceplugin ID Document Recognition Linux Docker SDK. Fully on-premise OCR and
  authenticity HTTP API on port 8082. documentRecognition, documentProcess.
---

# ID Document Recognition Linux SDK

Fully on-premise **ID Document Recognition HTTP API for Linux / Docker**. Image: `faceplugin/document-reader`. Default port **8082**. Gradio **9002**.

Reads ID cards, passports, and driver licenses. OCR, MRZ, barcode / QR, image quality, crops, and optional authenticity (document liveness).

All processing stays on your server. **No** biometric data is sent to Faceplugin cloud.

{% hint style="warning" %}
`--shm-size=2gb` is required. A smaller shm size can crash the engine.
{% endhint %}

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Docker" %}

### Setup <a href="#setup" id="setup"></a>

{% stepper %}
{% step %}
## Pull Docker Hub (no Drive)

```
sudo docker pull faceplugin/document-reader:latest
sudo docker run -d --name faceplugin-document-reader \
  --shm-size=2gb --privileged \
  -p 8082:8082 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/document-reader:latest
```

On Docker Desktop omit the `/etc/machine-id` volume.
{% endstep %}

{% step %}
## Confirm health (no license yet)

```
curl -s http://127.0.0.1:8082/api/health
```
{% endstep %}

{% step %}
## Activate

```
curl -s http://127.0.0.1:8082/api/machinecode
curl -s -X POST http://127.0.0.1:8082/api/activate \
  -H 'Content-Type: text/plain' \
  --data-binary @license.txt
```
{% endstep %}
{% endstepper %}

**Native (optional):** put `libDocSDK.so`, `libDocumentEngine.so`, `dcr.fpk` from [Drive](https://drive.google.com/drive/folders/16DFGKtyGbyL-0gfVOmNVaQ9vgXCYDr2M) **directly** in `lib/cpu/`, then `./run.sh`.

**Try online:** [Hugging Face Space](https://huggingface.co/spaces/FacePlugin-Ltd/ID-Document-Recognition-SDK) (Gradio UI → your Linux API).

### License

After `GET /api/licenseStatus`:

- **Recognition + Liveness** — OCR **and** authenticity
- **Recognition** — OCR / MRZ / barcode; `security` stays empty / not checked
- **Liveness** — authenticity only

[Request a License & Support](../request-a-license-and-support.md).

### Try it

```bash
curl -s http://127.0.0.1:8082/api/health
IMG=$(base64 -w0 id-front.jpg)

curl -s -X POST http://127.0.0.1:8082/api/documentProcess \
  -H 'Content-Type: application/json' \
  -d "{\"images\":[{\"image\":\"$IMG\",\"page_idx\":0}],\"response\":{\"OCR\":\"normal\",\"Authenticity\":\"normal\"}}"
```

**Postman:** import `postman/DocumentReader-API.postman_collection.json` from the repo. Base URL `http://127.0.0.1:8082`.

**Gradio (host only):**

```
pip3 install -r requirements-demo.txt
DEMO_PORT=9002 API_BASE=http://127.0.0.1:8082 python3 demo.py
```

Open [http://127.0.0.1:9002](http://127.0.0.1:9002). Tabs: Result, Liveness, Images, Raw JSON.

Parse the engine JSON with [Document result JSON](document-result-json.md).

### Integrate into your own app

| Path | When to use |
| ---- | ----------- |
| **HTTP** | Any language. Keep this API running and `POST` page images. |
| **`sdk.py`** | Python on the same Linux host as `lib/cpu/`. |

You do **not** need Gradio in production.

### APIs

Control routes return a JSON **envelope**. Process POSTs return **engine JSON** as the HTTP body.

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

Need authenticity **without** OCR as a separate product? See [ID Document Liveness Linux SDK](../id-document-liveness-sdk/id-document-liveness-linux-sdk.md).

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

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
