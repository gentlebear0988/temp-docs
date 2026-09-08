---
description: ID Document Recognition Ionic Cordova SDK
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

# ID Document Recognition Ionic Cordova SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Ionic-Cordova" %}

### How to run

### ✅ Setup Environment

Install Node.js, Ionic CLI, and Cordova as on the Face Recognition Cordova page.

```bash
ionic cordova plugin add ./DocumentReaderPlugin
ionic cordova build android
ionic cordova run android
```

Drive: [Android](https://drive.google.com/drive/folders/1nDSfvj0WtC1lZgzwFd7471ECVtk-nuYH) · [iOS](https://drive.google.com/drive/folders/1do6Ws_BlXGkR_K9jI_ULd1zHjqLGSP4q). Prefer [Capacitor](id-document-recognition-ionic-capacitor-sdk.md) for new projects.

### APIs

Same activate → init → locate / recognize / documentRecognition / documentLiveness sequence as the other mobile Document Reader Apps. Status codes **0**–**4**.

#### <mark style="color:orange;">setActivation:</mark> This API is used to activate the SDK

```ts
setActivation(license: string): Promise<number>
```

#### <mark style="color:orange;">init:</mark> This API is used to initialize the SDK

```ts
init(): Promise<number>
```

#### <mark style="color:orange;">recognize:</mark> This API is used to run FullProcess

```ts
recognize(front, back?, authenticity?): Promise<string>
```

Also: `getMachineCode`, `locateDocument`, `documentRecognition`, `documentLiveness`, `getLicenseStatus`, `deinit`.

Place `documentreadersdk.aar` in the Cordova plugin Android libs and `docsdk.framework` in the iOS Frameworks folder. `ionic serve` cannot load the engine. Parse JSON with [Document result JSON](document-result-json.md).

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
