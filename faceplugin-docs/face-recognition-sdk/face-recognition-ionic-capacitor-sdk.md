---
description: >-
  Faceplugin Face Recognition Ionic Capacitor SDK. On-premise face matching and liveness.
  face-recognition-capacitor plugin for new Ionic apps.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Face Recognition Ionic Capacitor SDK

Fully on-premise **Face Recognition SDK for Ionic Capacitor**. Package: `face-recognition-capacitor`. Use this for **new** Ionic apps. Cordova is a [different repo](face-recognition-android-sdk-3.md).

`ionic serve` / the browser **cannot** load the engine. Open Android Studio or Xcode and run on a **physical** phone.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-Ionic-Capacitor" %}

### How to run

{% stepper %}
{% step %}
## Install tools

Node **18+**, JDK **17**, Android Studio and/or Xcode 15+. Physical phone with USB debugging.
{% endstep %}

{% step %}
## Clone, install, build the plugin

```bash
git clone https://github.com/Faceplugin-ltd/FaceRecognition-Ionic-Capacitor.git
cd FaceRecognition-Ionic-Capacitor
npm install
npm run build
cd example && npm install
```
{% endstep %}

{% step %}
## Place native runtimes

| Platform | File | Example app path | Your own app path |
| -------- | ---- | ---------------- | ----------------- |
| Android | `facerecognitionsdk.aar` | `example/android/libfacesdk/` | `node_modules/face-recognition-capacitor/android/libs/` |
| iOS | three frameworks | `ios/Frameworks/` | `node_modules/face-recognition-capacitor/ios/Frameworks/` |

- Android Drive: [facerecognitionsdk.aar](https://drive.google.com/drive/folders/1kpzYVv9Gbm_pEpDe9-x7FGB4NWZzvez0)
- iOS Drive: [frameworks](https://drive.google.com/drive/folders/1PKmV-o7gq7s7dDtiNgXPfCi2ZlWaRy5H) (`facerecognitionsdk`, `FaceRecognitionEngine`, `onnxruntime`)
{% endstep %}

{% step %}
## Sync and run

```bash
cd example
npm run build
npx cap sync
npx cap open android
```

Or `npx cap open ios`. Wait for the home status bar → **Ready**.
{% endstep %}
{% endstepper %}

Keep demo ids so the included license works:

| Platform | Id |
| -------- | -- |
| Android `applicationId` | `com.faceplugin.facerecognitionsdk` |
| iOS bundle id | `com.faceplugin.facerecognitionsdk` |

Demo tiles: Enroll, Identify, Capture, Attribute, Settings, About.

### License

Licenses are **offline** and bound to your `applicationId` / bundle id. The sample key is only for the demo id. Request a new `FP1.…` for **your** id. [Request a License & Support](../request-a-license-and-support.md).

Default thresholds in Settings: identify **0.67**, liveness **0.5**, liveness level `0`, pose **40°**, eye-close **0.5**.

### Integrate into your own app

```bash
npm install git+https://github.com/Faceplugin-ltd/FaceRecognition-Ionic-Capacitor.git
npx cap sync
```

Copy runtimes into `node_modules/face-recognition-capacitor/...` as in the table above. Set **your** `appId` in `capacitor.config.ts`. Add camera + photo-library permissions.

```ts
import {
  getMachineCode,
  setActivation,
  init,
  lastLicenseError,
  faceDetection,
  templateExtraction,
  cropFace,
  SDK_SUCCESS,
} from 'face-recognition-capacitor';

async function activate() {
  const mc = await getMachineCode(); // FPMC1.… — send when requesting a key
  const act = await setActivation('FP1.…'); // bound to YOUR applicationId
  if (act !== SDK_SUCCESS) throw new Error(await lastLicenseError());
  const initCode = await init();
  if (initCode !== SDK_SUCCESS) throw new Error(`init failed: ${initCode}`);
}

async function enrollStill(imageUri: string) {
  const faces = await faceDetection(imageUri);
  if (faces.length !== 1) return;
  const template = await templateExtraction(imageUri, faces[0]);
  const cropB64 = await cropFace(imageUri, faces[0]);
  // Store template + crop in YOUR database
}
```

### APIs

Call order: `getMachineCode` → `setActivation` → `init` → detect / VideoWorker → `deinit`.

Status codes: **0** Success, **1** Invalid license, **2** Expired, **3** Not activated, **4** Init failed.

#### <mark style="color:orange;">setActivation:</mark> This API is used to activate the SDK

```ts
setActivation(license: string): Promise<number>
```

#### <mark style="color:orange;">init:</mark> This API is used to initialize the SDK

```ts
init(): Promise<number>
```

#### <mark style="color:orange;">getMachineCode:</mark> This API is used to retrieve the machine code

```ts
getMachineCode(): Promise<string>
```

#### <mark style="color:orange;">faceDetection:</mark> This API is used to detect faces

```ts
faceDetection(image: ImageInput, param?: FaceDetectionParam): Promise<FaceBox[]>
```

`FaceBox` includes geometry (`x1,y1,x2,y2`), pose, liveness / quality / eyes / occlusion, age / gender / emotion / mask / glasses, `landmarks`, `landmarkCount`.

#### <mark style="color:orange;">templateExtraction:</mark> This API is used to extract face template

```ts
templateExtraction(image: ImageInput, faceBox: FaceBox): Promise<string>
```

#### <mark style="color:orange;">similarity:</mark> This API is used to calculate similarity between two templates

```ts
similarity(feature1: string, feature2: string): Promise<number>
```

Also: `getLicenseStatus`, `detect(image, crop?, flags?)`, `extractFeature`, `quality`, `cropFace`, `lastLicenseError`.

#### <mark style="color:orange;">VideoWorker:</mark> This API is used for live 1:N identify

```ts
startVideoWorker(config?: VideoWorkerConfig): Promise<number>
syncVideoWorkerDatabase(featuresB64: string[], matchThreshold?: number): Promise<number>
startLivePreview() / takeLiveSnapshot() / ingestLiveCameraFrame(...)
subscribeVideoWorker(listener)
stopVideoWorker()
```

Optional session helpers in the example: `IdentifySession`, `CaptureSession`.

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
