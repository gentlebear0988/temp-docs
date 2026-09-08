---
description: >-
  Faceplugin Liveness Detection Linux Docker SDK. Fully on-premise PAD HTTP API on port
  8084. POST /api/liveness. CPU only.
---

# Liveness Detection Linux SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceLivenessDetection-Docker" %}

### Setup <a href="#setup" id="setup"></a>

1. Pull and run the Docker Hub image (no Drive required):

```
sudo docker pull faceplugin/face-liveness:latest
sudo docker run -d --name faceplugin-face-liveness \
  --shm-size=1gb --privileged \
  -p 8084:8084 \
  -v /etc/machine-id:/etc/machine-id:ro \
  faceplugin/face-liveness:latest
```

2. Confirm it is running (no license needed yet):

```
curl -s http://127.0.0.1:8084/api/health
```

3. Get machine code

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption><p>Call <code>GET /api/machinecode</code> to get the machine code (<code>FPMC1.…</code>)</p></figcaption></figure>

4. Contact us to get the license according to the machine code.
5. Activate the server by using the license obtained from us.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption><p>Call <code>POST /api/activate</code> to activate the SDK</p></figcaption></figure>

6. Liveness detection using a JPEG image

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption><p>Call <code>POST /api/liveness</code> to determine if the face is real or spoof</p></figcaption></figure>

Native (optional): put `libFaceLivenessSDK.so`, `libfal-eng.so`, `fal.fpk` from [Drive](https://drive.google.com/drive/folders/1rFnw7VASLmA4q8NWenQgszFS8njRGEgt) **directly** in `lib/cpu/`, then `./run.sh`.

Default port **8084**. CPU only. Gradio demo (`demo.py`) on **9004** (host only).

`POST /api/check_liveness` is an alias of `/api/liveness`.

### APIs

#### <mark style="color:orange;">get_machine_code:</mark> This API is used to retrieve the code specific to the server on which this SDK is running <a href="#setactivation" id="setactivation"></a>

```python
@app.get('/api/machinecode')
def get_machine_code():
    return envelope(data={"machinecode": sdk.get_machine_code()})
```

```http
GET /api/machinecode
```

| **Input**        | None                                                               |
| ---------------- | ------------------------------------------------------------------ |
| **Return value** | Envelope. <code>data.machinecode</code> is <code>FPMC1.…</code> |

Also: `GET /api/health` (no license), `GET /api/licenseStatus`, `GET /api/backend` (`"cpu"`).

#### <mark style="color:orange;">activate_machine:</mark> This API is used to activate the SDK <a href="#initsdk" id="initsdk"></a>

```python
@app.post('/api/activate')
def activate_machine():
    ret = sdk.activate(license)
    sdk.init_sdk()
    return envelope(data={"activated": True})
```

```http
POST /api/activate
Content-Type: text/plain

FP1.…
```

JSON `{"license":"FP1.…"}` and a license file body are also accepted.

| **Input**        | License key or file. |
| ---------------- | -------------------- |
| **Return value** | Envelope. Success: <code>code</code> 0, <code>"Successfully activated"</code>. On success the App also calls <code>init_sdk()</code>. |

#### <mark style="color:orange;">check_liveness:</mark> This API is used to determine if the faces are real or fake <a href="#facedetection" id="facedetection"></a>

```python
@app.post('/api/liveness')
@app.post('/api/check_liveness')
def check_liveness():
    return sdk.liveness(base64_jpeg)
```

```http
POST /api/liveness
Content-Type: application/json

{"image":"<BASE64-JPEG>"}
```

File field `image` (alias `file`) is accepted as `multipart/form-data`. Same URL.

| **Input**        | JPEG image (base64 JSON or form-data). A missing <code>image</code> field returns envelope <code>code: -1</code> and <code>"image required"</code>. |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Return value** | Engine JSON. Score **≥ 0.5** → <code>result</code> Real and <code>pass</code> true. Score **&lt; 0.5** → <code>result</code> Spoof and <code>pass</code> false. |

Example:

```json
{ "score": 0.72, "result": "Real", "pass": true }
```

Python:

```python
import sdk

machine_code = sdk.get_machine_code()
sdk.activate("license.txt")
sdk.init_sdk()
print(sdk.liveness(base64_jpeg))
```
