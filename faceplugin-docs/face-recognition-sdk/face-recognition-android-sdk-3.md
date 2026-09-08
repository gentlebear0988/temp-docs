---
description: >-
  Faceplugin Face Recognition Ionic Cordova SDK. On-premise face matching and liveness.
  Legacy Cordova plugin. Prefer Capacitor for new Ionic apps.
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

# Face Recognition Ionic-Cordova SDK

Fully on-premise **Face Recognition SDK for Ionic Cordova**. Plugin folder: `FacePlugin/`. Plugin id: `face-recognition-cordova`. Prefer [Ionic Capacitor](face-recognition-ionic-capacitor-sdk.md) for new projects.

Demo application id: **`com.faceplugin.facerecognitionsdk`**.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-Ionic-Cordova" %}

### How to run

### ✅ Setup Environment

Node **18+**, npm, Cordova CLI, JDK **17**, Android SDK. iOS: macOS + Xcode 15+, physical iPhone. Put your Apple Team ID in `build.json`.

#### 1. Install Node.js and npm

```bash
node -v
npm -v
```

#### 2. Get the runtimes

- Android AAR: [Google Drive](https://drive.google.com/drive/folders/1kpzYVv9Gbm_pEpDe9-x7FGB4NWZzvez0) → `FacePlugin/src/android/facerecognitionsdk.aar`
- iOS frameworks: [Google Drive](https://drive.google.com/drive/folders/1PKmV-o7gq7s7dDtiNgXPfCi2ZlWaRy5H) → `FacePlugin/src/ios/Frameworks/`

***

### 📱 Running the App on Android

```bash
npm install
ionic cordova plugin add ./FacePlugin
npm run setup:android
npm run android
```

Add camera permission in `platforms/android/app/src/main/AndroidManifest.xml` if it is not already present:

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

### 🍏 Running the App on iOS

```bash
npm install
ionic cordova plugin add ./FacePlugin
npm run setup:ios
npm run ios
```

Add `NSCameraUsageDescription` in `Info.plist`. Run on a **physical** iOS device.

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

Also: `getLicenseStatus`, `detect`, `extractFeature`, `quality`, VideoWorker (`startVideoWorker`, `ingestLiveCameraFrame`, `exportLastLiveFrame`), `deinit`.
