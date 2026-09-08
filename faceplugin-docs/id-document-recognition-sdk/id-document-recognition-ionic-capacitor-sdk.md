---
description: >-
  Faceplugin ID Document Recognition Ionic Capacitor SDK. On-premise OCR, MRZ, and
  authenticity. document-reader-capacitor plugin for new Ionic apps.
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

Fully on-premise **ID Document Recognition SDK for Ionic Capacitor**. Package: `document-reader-capacitor`. Prefer this for **new** Ionic apps. Cordova is a [different repo](id-document-recognition-ionic-cordova-sdk.md).

`ionic serve` / the browser **cannot** load the engine. Open Android Studio or Xcode and run on a **physical** phone.

Parse results with [Document result JSON](document-result-json.md).

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Ionic-Capacitor" %}

### How to run

{% stepper %}
{% step %}
## Install and build the plugin

```bash
git clone https://github.com/Faceplugin-ltd/ID-Document-Recognition-Ionic-Capacitor.git
cd ID-Document-Recognition-Ionic-Capacitor
npm install && npm run build
cd example && npm install
```
{% endstep %}

{% step %}
## Place native runtimes

| Platform | File | Example / plugin path |
| -------- | ---- | --------------------- |
| Android | `documentreadersdk.aar` | `example/android/libdocsdk/` (your app: `node_modules/document-reader-capacitor/android/libs/`) |
| iOS | `docsdk.framework` | `ios/Frameworks/` |

- Android Drive: [documentreadersdk.aar](https://drive.google.com/drive/folders/1nDSfvj0WtC1lZgzwFd7471ECVtk-nuYH)
- iOS Drive: [docsdk.framework](https://drive.google.com/drive/folders/1do6Ws_BlXGkR_K9jI_ULd1zHjqLGSP4q)
{% endstep %}

{% step %}
## Sync and run

```bash
cd example
npx cap sync
npx cap open android
```

Or `npx cap open ios`. Add camera + photo-library permissions.
{% endstep %}
{% endstepper %}

### APIs

Status codes: **0** Success, **1** Invalid license, **2** Expired, **3** Not activated, **4** Init failed.

Call order: `getMachineCode` → `setActivation` → `init` → `locateDocument` / `recognize` → `deinit`.

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

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
