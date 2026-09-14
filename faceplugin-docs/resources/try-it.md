---
description: >-
  Try Faceplugin SDKs with copy-paste commands. curl health with no license, then detect, match,
  liveness, and document OCR. Android and Flutter snippets after the demo runs.
---

# Try it

These snippets are meant to be **copied as-is**. You do not write a UI first. Start with `health` and `machinecode` (no license needed), then activate and call one process API.

{% hint style="info" %}
**Server first is the easiest.** Docker Hub + `curl` needs no Android Studio. Mobile snippets assume you already ran the demo once (AAR / frameworks in place, demo license still bound to the demo app id).
{% endhint %}

## 1. Server — no license yet

Start any Linux/Windows App, then:

```bash
curl -s http://127.0.0.1:8083/api/health
curl -s http://127.0.0.1:8083/api/machinecode
```

Change the port: Document Reader **8082**, Face Recognition **8083**, Face Liveness **8084**, Document Liveness **8086**.

`health` works **before** you have a key. Copy `FPMC1.…` from `machinecode` and [request a license](../request-a-license-and-support.md).

## 2. Server — activate once

```bash
# license.txt contains one line: FP1.…
curl -s -X POST http://127.0.0.1:8083/api/activate \
  -H 'Content-Type: text/plain' \
  --data-binary @license.txt
```

Success looks like `"Successfully activated"`. The App also loads the engine on this call.

## 3. Server — one function each product

{% tabs %}
{% tab title="Face Recognition" %}
```bash
IMG=$(base64 -w0 face.jpg)   # macOS: base64 -i face.jpg

curl -s -X POST http://127.0.0.1:8083/api/detect \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"

curl -s -X POST http://127.0.0.1:8083/api/match \
  -H 'Content-Type: application/json' \
  -d "{\"image1\":\"$IMG\",\"image2\":\"$IMG\"}"
```

Install: [Face Recognition Linux SDK](../face-recognition-sdk/face-recognition-linux-sdk.md).
{% endtab %}

{% tab title="Face Liveness" %}
```bash
IMG=$(base64 -w0 face.jpg)

curl -s -X POST http://127.0.0.1:8084/api/liveness \
  -H 'Content-Type: application/json' \
  -d "{\"image\":\"$IMG\"}"
```

Score **≥ 0.5** is Real / pass. JPEG only. [Liveness Detection Linux SDK](../liveness-detection-sdk/liveness-detection-linux-sdk.md).
{% endtab %}

{% tab title="ID Document" %}
```bash
FRONT=$(base64 -w0 passport_front.jpg)

curl -s -X POST http://127.0.0.1:8082/api/documentRecognition \
  -H 'Content-Type: application/json' \
  -d "{\"images\":[{\"image\":\"$FRONT\",\"page_idx\":0}]}"
```

Combined pipeline: `POST /api/documentProcess`. Dedicated Document Liveness product: port **8086**. [ID Document Recognition Linux SDK](../id-document-recognition-sdk/id-document-recognition-linux-sdk.md).
{% endtab %}
{% endtabs %}

Windows: use Git Bash or WSL for `base64`, or Python:

```python
import base64, json, urllib.request
img = base64.b64encode(open("face.jpg", "rb").read()).decode()
req = urllib.request.Request(
    "http://127.0.0.1:8083/api/detect",
    data=json.dumps({"image": img}).encode(),
    headers={"Content-Type": "application/json"},
)
print(urllib.request.urlopen(req).read().decode())
```

## 4. Mobile — after the demo compiles

Keep the **demo application id** so the included `FP1.…` works. Call this on a **background** thread.

{% tabs %}
{% tab title="Android Face Recognition" %}
```kotlin
Thread {
    FaceRecognitionSDK.getMachineCode(context)
    var code = FaceRecognitionSDK.setActivation(context, "FP1.…") // demo key from the repo
    if (code == FaceRecognitionSDK.SDK_SUCCESS) {
        code = FaceRecognitionSDK.init(context)
    }
    val faces = FaceRecognitionSDK.faceDetection(bitmap, FaceDetectionParam())
    val template = FaceRecognitionSDK.templateExtraction(bitmap, faces[0])
    val score = FaceRecognitionSDK.similarity(template, template)
}.start()
```

Install: [Face Recognition Android SDK](../face-recognition-sdk/face-recognition-android-sdk.md).
{% endtab %}

{% tab title="Flutter Face Recognition" %}
```dart
import 'package:face_recognition_sdk/face_recognition_sdk.dart';

Future<void> tryOnce(String imagePath, String license) async {
  await getMachineCode();
  if (await setActivation(license) != sdkSuccess) return;
  if (await init() != sdkSuccess) return;
  final faces = await faceDetection(imagePath);
  final t1 = await templateExtraction(imagePath, faces.first);
  final t2 = await templateExtraction(imagePath, faces.first);
  final score = await similarity(t1, t2);
}
```

Install: [Face Recognition Flutter SDK](../face-recognition-sdk/face-recognition-flutter-sdk.md).
{% endtab %}

{% tab title="Android ID Document" %}
```kotlin
Thread {
    DocumentReaderSDK.getMachineCode(context)
    var code = DocumentReaderSDK.setActivation(context, "FP1.…")
    if (code == DocumentReaderSDK.SDK_SUCCESS) {
        code = DocumentReaderSDK.init(context)
    }
    val json = DocumentReaderSDK.recognize(frontBitmap, null, "none")
}.start()
```

`locateDocument` is overlay-only (no OCR). Install: [ID Document Recognition Android SDK](../id-document-recognition-sdk/id-document-recognition-android-sdk.md).
{% endtab %}
{% endtabs %}

### Related documentation

* [Choose a product](choose-a-product.md) · [Status codes](status-codes.md) · [Troubleshooting](troubleshooting.md)
* [Request a License](../request-a-license-and-support.md)
