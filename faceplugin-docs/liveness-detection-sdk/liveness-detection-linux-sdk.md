---
description: >-
  Faceplugin Face Liveness API for Linux Docker. On-premise anti-spoofing PAD. POST
  /api/liveness on port 8084. Score 0.5 or higher is Real.
---

# Face Liveness Detection Linux SDK

Fully on-premise **Face Liveness HTTP API for Linux / Docker**. Image: `faceplugin/face-liveness`. Default port **8084**.

Score **one RGB JPEG**. Score **≥ 0.5** → Real / `pass` true. Score **&lt; 0.5** → Spoof / `pass` false.

Need recognition as well? Run [Face Recognition Linux SDK](../face-recognition-sdk/face-recognition-linux-sdk.md) on port **8083** as a **second** container.

All processing stays on your server. **No** biometric data is sent to Faceplugin cloud.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceLivenessDetection-Docker" %}

### Setup <a href="#setup" id="setup"></a>

Sizing: [Hosting requirements](../deploy-and-host/hosting-requirements.md).

{% stepper %}
{% step %}
## Pull from Docker Hub (no Google Drive download)

```
sudo docker pull faceplugin/face-liveness:latest
sudo docker run -d --name faceplugin-face-liveness \
  --shm-size=1gb --privileged \
  -p 8084:8084 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/face-liveness:latest
```

On Docker Desktop (macOS/Windows) omit the `/etc/machine-id` volume.
{% endstep %}

{% step %}
## Confirm health (no license yet)

```
curl -s http://127.0.0.1:8084/api/health
```
{% endstep %}

{% step %}
## Copy the machine code

```
curl -s http://127.0.0.1:8084/api/machinecode
```

Send machine code to Faceplugin. Docker and local host codes are **different**.
{% endstep %}

{% step %}
## Activate

Put your key in `license.txt`, then:

```
curl -s -X POST http://127.0.0.1:8084/api/activate \
  -H 'Content-Type: text/plain' \
  --data-binary @license.txt
```
{% endstep %}

{% step %}
## Check liveness

```
IMG=$(base64 -w0 face.jpg)   # macOS: base64 -i face.jpg

curl -s -X POST http://127.0.0.1:8084/api/liveness \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"
```
{% endstep %}
{% endstepper %}

### Run multiple containers with one license <a href="#run-multiple-containers" id="run-multiple-containers"></a>

You only need this section if you want to run multiple Face Liveness containers on the same Linux host.

On Linux, mount `/etc/machine-id` into each container so they use the same machine code. Each container must have a different container name and host port.

For example:

```bash
sudo docker run -d --name faceplugin-face-liveness-2 \
  --shm-size=1gb --privileged \
  -p 8085:8084 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/face-liveness:latest
```

Activate each container with the same license key (`POST /api/activate` on each host port).

On Docker Desktop (macOS/Windows), omit the `/etc/machine-id` volume. Each container may require its own license.

### Other ways to run

#### Option B — Docker Compose (local build)

```
git clone https://github.com/Faceplugin-ltd/FaceLivenessDetection-Docker.git
cd FaceLivenessDetection-Docker
```

Put the [Google Drive runtime](https://drive.google.com/drive/folders/1rFnw7VASLmA4q8NWenQgszFS8njRGEgt) files **directly** in `lib/cpu/`, then:

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

Default port **8084**. Gradio demo (`demo.py`) on **9004** (host only). The Docker Hub image is API-only.

`POST /api/check_liveness` is an alias of `/api/liveness`.

{% hint style="info" %}
Control routes (`/api/health`, `/api/machinecode`, `/api/activate`, `/api/licenseStatus`) return a JSON **envelope**. `POST /api/liveness` returns **engine JSON** as the HTTP body.
{% endhint %}

### License

Licenses are **offline**. [Request a License & Support](../request-a-license-and-support.md).

### APIs

| Endpoint | Purpose |
| -------- | ------- |
| `GET /api/health` | Process is listening (no license) |
| `GET /api/machinecode` | Machine code |
| `GET /api/licenseStatus` | License status |
| `GET /api/backend` | `"cpu"` |
| `POST /api/activate` | Activate and `init_sdk()` |
| `POST /api/liveness` | Passive face anti-spoofing |
| `POST /api/check_liveness` | Alias of `/api/liveness` |

Full reference: [Face Liveness HTTP API](../http-api/face-liveness.md). Shared control routes: [Shared endpoints](../http-api/shared.md).

Some routes wrap the result in a small JSON object (an **envelope**). `POST /api/liveness` returns **engine JSON** as the body. Score **≥ 0.5** → Real / `pass` true.

Python:

```python
import sdk

machine_code = sdk.get_machine_code()
sdk.activate("license.txt")
sdk.init_sdk()
print(sdk.liveness(base64_jpeg))
```

### Try it

```bash
curl -s http://127.0.0.1:8084/api/health
IMG=$(base64 -w0 face.jpg)

curl -s -X POST http://127.0.0.1:8084/api/liveness \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"
```

**Postman:** import `postman/FaceLiveness-API.postman_collection.json` from the repo. Base URL `http://127.0.0.1:8084`.

**Gradio (host only):**

```
pip3 install -r requirements-demo.txt
DEMO_PORT=9004 API_BASE=http://127.0.0.1:8084 python3 demo.py
```

Open [http://127.0.0.1:9004](http://127.0.0.1:9004). You do **not** need Gradio in production.

[Request a License & Support](../request-a-license-and-support.md) · [Contact us](../contact-us.md)

### FAQ

**Face Liveness API?** `POST /api/liveness` on port **8084**. Score **≥ 0.5** → Real.

**Machine code?** `GET /api/machinecode` returns machine code. Docker and host codes differ.

### Related documentation

* [Faceplugin Face Liveness Detection Server SDK](server-sdk.md) · [Windows](liveness-detection-windows-sdk.md) · [Glossary](../resources/glossary.md)
* [Face Recognition Linux SDK](../face-recognition-sdk/face-recognition-linux-sdk.md)
* [ID Document Recognition Linux SDK](../id-document-recognition-sdk/id-document-recognition-linux-sdk.md)
* [ID Document Liveness Linux SDK](../id-document-liveness-sdk/id-document-liveness-linux-sdk.md)
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/README.md)
