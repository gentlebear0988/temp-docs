---
description: >-
  Faceplugin ID Document Recognition Flutter SDK. On-premise OCR, MRZ, and authenticity.
  document_reader_sdk plugin for Android and iOS.
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

# ID Document Recognition Flutter SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Flutter" %}

### How to Run

#### 1. Set Up Flutter Development Environment

You can refer to Flutter [official document](https://docs.flutter.dev/get-started/install) to setup enviroment.

#### 2. How to Run the App

Requires Flutter **3.44+** and JDK **17**. Copy runtimes, or run `dart run tool/bootstrap.dart`.

- Android AAR: [Drive](https://drive.google.com/drive/folders/1nDSfvj0WtC1lZgzwFd7471ECVtk-nuYH) → `example/android/libdocsdk/` (your own app: plugin `android/libs/`)
- iOS framework: [Drive](https://drive.google.com/drive/folders/1do6Ws_BlXGkR_K9jI_ULd1zHjqLGSP4q) → `ios/Frameworks/`

```
cd example
flutter pub get
flutter run
```

Physical phone. Package: `document_reader_sdk`. Authenticity accepts `true` / `false` or `'normal'` / `'none'`.

### APIs

Status codes: **0** Success, **1** Invalid license, **2** Expired, **3** Not activated, **4** Init failed.

#### <mark style="color:orange;">setActivation:</mark> This API is used to activate the SDK

```dart
Future<int> setActivation(String license)
```

#### <mark style="color:orange;">init:</mark> This API is used to initialize the SDK

```dart
Future<int> init()
```

#### <mark style="color:orange;">getMachineCode:</mark> This API is used to retrieve the machine code

```dart
Future<String> getMachineCode()
```

#### <mark style="color:orange;">locateDocument:</mark> This API is used to find document corners on a preview frame

```dart
Future<String> locateDocument(ImageInput image)
```

#### <mark style="color:orange;">recognize:</mark> This API is used to run FullProcess

```dart
Future<String> recognize(ImageInput front, [ImageInput? back, Object authenticity = true])
```

#### <mark style="color:orange;">documentRecognition:</mark> This API is used to run OCR / MRZ / barcode / image quality only

```dart
Future<String> documentRecognition(ImageInput front, [ImageInput? back])
```

#### <mark style="color:orange;">documentLiveness:</mark> This API is used to run authenticity / security only

```dart
Future<String> documentLiveness(ImageInput front, [ImageInput? back])
```

Also: `getLicenseStatus`, `startNewSession`, `deinit`.
