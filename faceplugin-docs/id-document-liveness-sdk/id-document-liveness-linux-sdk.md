---
description: >-
  Faceplugin ID Document Liveness Linux SDK. On-premise document anti-spoofing HTTP API.
  Docker image faceplugin/document-liveness, POST /api/documentLiveness on port 8086.
icon: linux
---

# ID Document Liveness Linux SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Liveness-Detection-Docker" %}

### Setup <a href="#setup" id="setup"></a>

Sizing: [Hosting requirements](../deploy-and-host/hosting-requirements.md).

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
4. Contact us for license key, then `POST /api/activate`

### Run multiple containers with one license <a href="#run-multiple-containers" id="run-multiple-containers"></a>

You only need this section if you want to run multiple Document Liveness containers on the same Linux host.

On Linux, mount `/etc/machine-id` into each container so they use the same machine code. Each container must have a different container name and host port.

For example:

```bash
sudo docker run -d --name faceplugin-document-liveness-2 \
  --shm-size=2gb --privileged \
  -p 8087:8086 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/document-liveness:latest
```

Activate each container with the same license key (`POST /api/activate` on each host port).

On Docker Desktop (macOS/Windows), omit the `/etc/machine-id` volume. Each container may require its own license.

### Other ways to run

#### Option B — Docker Compose (local build)

```
git clone https://github.com/Faceplugin-ltd/ID-Document-Liveness-Detection-Docker.git
cd ID-Document-Liveness-Detection-Docker
```

Put the [Google Drive runtime](https://drive.google.com/drive/folders/1_V05Nvcdc3WfOPuyquFyGIW-4CDj8aAm) files **directly** in `lib/cpu/`, then:

```
# macOS/Windows Docker Desktop: remove the /etc/machine-id volume from docker-compose.yml first
sudo docker compose up --build -d
sudo docker compose logs -f
```

#### Option C — Native Linux (no Docker)

Same `lib/cpu/` layout:

```
./run.sh
```

On Docker Desktop omit the `/etc/machine-id` volume for Hub and Compose runs.

Default port **8086**. Gradio demo on **9006** (host only).

Need OCR as well? Use [ID Document Recognition Linux SDK](../id-document-recognition-sdk/id-document-recognition-linux-sdk.md).

### APIs

| Endpoint | Purpose |
| -------- | ------- |
| `GET /api/health` | Process is listening (no license) |
| `GET /api/machinecode` | Machine code |
| `GET /api/licenseStatus` | License status |
| `GET /api/backend` | `"cpu"` |
| `POST /api/activate` | Activate and `init_sdk()` |
| `POST /api/documentLiveness` | Authenticity / document anti-spoofing |

Full reference: [Document Liveness HTTP API](../http-api/document-liveness.md). Shared control routes: [Shared endpoints](../http-api/shared.md).

Some routes wrap the result in a small JSON object (an **envelope**). `POST /api/documentLiveness` returns **engine JSON** as the body. There is no `documentRecognition` / `documentProcess` on this product.

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

**Gradio (host only):** port **9006**. There is **no** `documentRecognition` / `documentProcess` on this product — authenticity only. Security keys: [Document security check fields](../id-document-recognition-sdk/document-security-check-fields.md).

[Request a License & Support](../request-a-license-and-support.md) · [Contact us](../contact-us.md)

### FAQ

**Document anti-spoofing API?** `POST /api/documentLiveness` on port **8086**. No OCR.

**Need passport OCR too?** Use [ID Document Recognition Linux](../id-document-recognition-sdk/id-document-recognition-linux-sdk.md) with a Liveness-capable license, or run both containers and call each API from your backend.

### Related documentation

* [Faceplugin ID Document Liveness Server SDK](server-sdk.md) · [Glossary](../resources/glossary.md)
* [ID Document Recognition Linux SDK](../id-document-recognition-sdk/id-document-recognition-linux-sdk.md) (OCR + optional authenticity)
* [Face Liveness Detection Linux SDK](../liveness-detection-sdk/liveness-detection-linux-sdk.md) (face anti-spoofing)
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/README.md)
