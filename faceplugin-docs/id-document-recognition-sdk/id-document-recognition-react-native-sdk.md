---
description: >-
  Faceplugin ID Document Recognition React Native SDK. On-premise OCR, MRZ, and
  authenticity. document-reader-sdk plugin, not Expo Go.
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

# ID Document Recognition React Native SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-React-Native" %}

### How to Run

#### 1. Set Up React-Native Development Environment

You can refer to React Native [official document](https://reactnative.dev/docs/environment-setup) to setup enviroment.

#### 2. How to run Android App

```
yarn
cd example
yarn android
```

#### 3. How to run the iOS App

```
yarn
cd example
yarn
cd ios
pod install
```

Package: `document-reader-sdk`. **Not Expo Go.** Physical arm64 device.

Android AAR: [Drive](https://drive.google.com/drive/folders/1nDSfvj0WtC1lZgzwFd7471ECVtk-nuYH) → `android/libs/` (example: `example/android/libdocsdk/`). iOS: [Drive](https://drive.google.com/drive/folders/1do6Ws_BlXGkR_K9jI_ULd1zHjqLGSP4q) → `ios/Frameworks/`. Install from GitHub, not npm.

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

#### <mark style="color:orange;">locateDocument:</mark> This API is used to find document corners on a preview frame

```ts
locateDocument(image: ImageInput): Promise<string>
```

#### <mark style="color:orange;">recognize:</mark> This API is used to run FullProcess

```ts
recognize(front, back?, authenticity?): Promise<string>
```

#### <mark style="color:orange;">documentRecognition:</mark> This API is used to run OCR / MRZ / barcode / image quality only

```ts
documentRecognition(front, back?): Promise<string>
```

#### <mark style="color:orange;">documentLiveness:</mark> This API is used to run authenticity / security only

```ts
documentLiveness(front, back?): Promise<string>
```

Also: `getLicenseStatus`, `startNewSession`, `deinit`.
