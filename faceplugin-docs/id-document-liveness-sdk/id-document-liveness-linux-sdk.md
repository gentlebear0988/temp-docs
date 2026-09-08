---
description: >-
  Faceplugin ID Document Liveness Linux SDK. On-premise document anti-spoofing HTTP API.
  Docker image faceplugin/document-liveness, POST /api/documentLiveness on port 8086.
---

# ID Document Liveness Linux SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Liveness-Detection-Docker" %}

### Setup <a href="#setup" id="setup"></a>

1. Pull and run the Docker Hub image:

```
sudo docker pull faceplugin/document-liveness:latest
sudo docker run -d --name faceplugin-document-liveness \
  --shm-size=2gb --privileged \
  -p 8086:8086 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/document-liveness:latest
```

`--shm-size=2gb` is required.

2. Health (no license): `curl -s http://127.0.0.1:8086/api/health`
3. Get machine code: `GET /api/machinecode`
4. Contact us for `FP1.…`, then `POST /api/activate`

Native: put `libDocSDK.so`, `libDocumentEngine.so`, `dcr.fpk` from [Drive](https://drive.google.com/drive/folders/1_V05Nvcdc3WfOPuyquFyGIW-4CDj8aAm) **directly** in `lib/cpu/`, then `./run.sh`. On Docker Desktop omit the `/etc/machine-id` volume.

Default port **8086**. Gradio demo on **9006** (host only).

Need OCR as well? Use [ID Document Recognition Linux SDK](../id-document-recognition-sdk/id-document-recognition-linux-sdk.md) with a Liveness-capable license.

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

#### <mark style="color:orange;">documentLiveness:</mark> This API is used to run authenticity / document anti-spoofing

```http
POST /api/documentLiveness
Content-Type: application/json

{"images":[{"image":"<BASE64>","page_idx":0},{"image":"<BASE64>","page_idx":1}]}
```

| **Input**        | One or more page images (base64). OCR / MRZ / barcode / image quality are always off. |
| ---------------- | -------------------------------------------------------------------------------------- |
| **Return value** | Engine JSON with <code>security</code> checks. There is no <code>documentRecognition</code> / <code>documentProcess</code> on this App. |

Python:

```python
import sdk

sdk.activate("license.txt")
sdk.init_sdk()
print(sdk.document_liveness([{"image": base64_front}, {"image": base64_back, "page_idx": 1}]))
```

### Try it

```bash
curl -s http://127.0.0.1:8086/api/health
IMG=$(base64 -w0 id-front.jpg)

curl -s -X POST http://127.0.0.1:8086/api/documentLiveness \
  -H 'Content-Type: application/json' \
  -d "{\"images\":[{\"image\":\"$IMG\",\"page_idx\":0}]}"
```

**Postman:** import `postman/DocumentLiveness-API.postman_collection.json` from the repo. Base URL `http://127.0.0.1:8086`.

**Gradio (host only):** port **9006**. There is **no** `documentRecognition` / `documentProcess` on this App — authenticity only. Security keys: [Document security check fields](../id-document-recognition-sdk/document-security-check-fields.md).

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
