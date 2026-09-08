---
description: >-
  Faceplugin Face Recognition React Native SDK. On-premise 1:1 and 1:N matching with 2D
  liveness. face-recognition-sdk plugin, Yarn 3, not Expo Go.
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

# Face Recognition React Native SDK

Fully on-premise **Face Recognition SDK for React Native** (Android and iOS). Package: `face-recognition-sdk`. Expo Go is **not** supported.

Demo tiles: Enroll, Identify, Capture, Attribute, Settings, About. Demo application id: **`com.faceplugin.facerecognitionsdk`**.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-React-Native" %}

### How to Run

#### 1. Set Up React Native Development Environment

You can refer to React Native [official document](https://reactnative.dev/docs/environment-setup) to setup enviroment. Use **Yarn 3** as in `package.json` (do not `npm install` at the repo root).

#### 2. Get the runtimes

- Android AAR: [Google Drive](https://drive.google.com/drive/folders/1kpzYVv9Gbm_pEpDe9-x7FGB4NWZzvez0) → `example/android/libfacesdk/facerecognitionsdk.aar`
- iOS frameworks: [Google Drive](https://drive.google.com/drive/folders/1PKmV-o7gq7s7dDtiNgXPfCi2ZlWaRy5H) → `ios/Frameworks/` (`facerecognitionsdk`, `FaceRecognitionEngine`, `onnxruntime`)

#### 3. How to run Android App

```
yarn
cd example
yarn android
```

#### 4. How to run the iOS App

```
yarn
cd example
yarn
cd ios
pod install
```

Open `example/ios/FaceRecognitionSdkExample.xcworkspace` in Xcode and run on a **physical** iPhone.

### APIs

```ts
import { setActivation, init, faceDetection, templateExtraction, similarity } from 'face-recognition-sdk';
```

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

#### <mark style="color:orange;">getLicenseStatus:</mark> This API is used to read the license tier

```ts
getLicenseStatus(): Promise<string>
```

#### <mark style="color:orange;">faceDetection:</mark> This API is used to detect faces

```ts
faceDetection(image: ImageInput, param?: FaceDetectionParam): Promise<FaceBox[]>
```

#### <mark style="color:orange;">templateExtraction:</mark> This API is used to extract face template

```ts
templateExtraction(image: ImageInput, faceBox: FaceBox): Promise<string>
```

| **Input**        | Image URI / path / base64, and a detected <code>FaceBox</code>. |
| ---------------- | ---------------------------------------------------------------- |
| **Return value** | Template as base64. Store it in **your** database.                |

#### <mark style="color:orange;">similarity:</mark> This API is used to calculate similarity between two templates

```ts
similarity(feature1: string, feature2: string): Promise<number>
```

#### <mark style="color:orange;">detect:</mark> This API is used to detect faces and return engine JSON

```ts
detect(image: ImageInput, crop?: boolean, flags?: number): Promise<string>
```

Also: `extractFeature`, `quality`, `cropFace`, `setLandmarkMode` / `getLandmarkMode` (`14` / `68` / `468`), `lastLicenseError`, `deinit`, `estimatorStatus`.

#### <mark style="color:orange;">VideoWorker:</mark> This API is used for live 1:N identify

```ts
startVideoWorker(config?: VideoWorkerConfig): Promise<number>
syncVideoWorkerDatabase(featuresB64: string[], matchThreshold?: number): Promise<number>
ingestLiveCameraFrame(...): Promise<LiveFrameResult>
subscribeVideoWorker(listener): () => void
stopVideoWorker(): Promise<void>
```

Prefer `ingestLiveCameraFrame` so rotation is handled for you.
