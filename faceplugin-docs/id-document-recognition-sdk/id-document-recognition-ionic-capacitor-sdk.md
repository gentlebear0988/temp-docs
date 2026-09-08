---
description: ID Document Recognition Ionic Capacitor SDK
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

# ID Document Recognition Ionic Capacitor SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Ionic-Capacitor" %}

### How to run

```bash
npm install && npm run build
cd example && npm install
npx cap sync
npx cap open android
```

Package: `document-reader-capacitor`. `ionic serve` is not enough — open the native project. Cordova is a [different repo](id-document-recognition-ionic-cordova-sdk.md).

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

Also: `getLicenseStatus`, `startNewSession`, `startLivePreview` / `takeLiveSnapshot`, `deinit`.
