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

Demo application id: **`com.faceplugin.facerecognitionsdk`**. `ionic serve` is not enough — open the native project.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-Ionic-Capacitor" %}

### How to run

```bash
npm install && npm run build
cd example && npm install
```

Place `facerecognitionsdk.aar` from [Drive](https://drive.google.com/drive/folders/1kpzYVv9Gbm_pEpDe9-x7FGB4NWZzvez0) in `example/android/libfacesdk/`. Place iOS frameworks from [Drive](https://drive.google.com/drive/folders/1PKmV-o7gq7s7dDtiNgXPfCi2ZlWaRy5H) in `ios/Frameworks/`.

```bash
npx cap sync
npx cap open android
```

### APIs

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

#### <mark style="color:orange;">templateExtraction:</mark> This API is used to extract face template

```ts
templateExtraction(image: ImageInput, faceBox: FaceBox): Promise<string>
```

#### <mark style="color:orange;">similarity:</mark> This API is used to calculate similarity between two templates

```ts
similarity(feature1: string, feature2: string): Promise<number>
```

Also: `getLicenseStatus`, `detect`, `extractFeature`, `quality`, `cropFace`, `lastLicenseError`, VideoWorker (`startVideoWorker`, `syncVideoWorkerDatabase`, `ingestLiveCameraFrame`), camera helpers (`startLivePreview`, `takeLiveSnapshot`, `exportLastLiveFrame`), `deinit`.
