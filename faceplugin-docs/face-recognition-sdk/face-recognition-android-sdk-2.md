---
description: >-
  Faceplugin Face Recognition Flutter SDK. On-premise 1:1 and 1:N matching with 2D liveness.
  face_recognition_sdk plugin for Android and iOS.
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

# Face Recognition Flutter SDK

Fully on-premise **Face Recognition SDK for Flutter**. Package: `face_recognition_sdk`. Same native engines as the Android and iOS Face Recognition SDKs.

Demo ids: Android `com.faceplugin.facerecognitionsdk`, iOS `com.faceplugin.facerecognition.app`.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-Flutter" %}

### How to Run

#### 1. Set Up Flutter Development Environment

You can refer to Flutter [official document](https://docs.flutter.dev/get-started/install) to setup enviroment.

#### 2. Get the runtimes

```
dart run tool/bootstrap.dart
```

- Android AAR: [Google Drive](https://drive.google.com/drive/folders/1kpzYVv9Gbm_pEpDe9-x7FGB4NWZzvez0) → `example/android/libfacesdk/facerecognitionsdk.aar` (your own app: plugin `android/libs/`)
- iOS frameworks: [Google Drive](https://drive.google.com/drive/folders/1PKmV-o7gq7s7dDtiNgXPfCi2ZlWaRy5H) → `ios/Frameworks/`

#### 3. How to Run the App

```
cd example
flutter pub get
flutter run
```

Physical phone. If you are going to run the iOS app, run `cd example/ios && pod install` and see Flutter [iOS deployment](https://docs.flutter.dev/deployment/ios).

### APIs

```dart
import 'package:face_recognition_sdk/face_recognition_sdk.dart';
```

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

#### <mark style="color:orange;">faceDetection:</mark> This API is used to detect faces

```dart
Future<List<FaceBox>> faceDetection(String imageUri, [FaceDetectionParam param])
```

#### <mark style="color:orange;">templateExtraction:</mark> This API is used to extract face template

```dart
Future<String> templateExtraction(String imageUri, FaceBox faceBox)
```

#### <mark style="color:orange;">similarity:</mark> This API is used to calculate similarity between two templates

```dart
Future<double> similarity(String feature1B64, String feature2B64)
```

#### <mark style="color:orange;">detect:</mark> This API is used to detect faces and return engine JSON

```dart
Future<String> detect(ImageInput image, {bool crop = false, int flags = DETECT_ALL})
```

Also: `extractFeature`, `quality`, `cropFace`, `setLandmarkMode` / `getLandmarkMode`, `getLicenseStatus`, `lastLicenseError`, `deinit`.

#### <mark style="color:orange;">VideoWorker:</mark> This API is used for live 1:N identify

```dart
Future<int> startVideoWorker(VideoWorkerConfig config)
Future<int> syncVideoWorkerDatabase(List<String> features, {double matchThreshold = 0.67})
Future<LiveFrameResult> ingestLiveCameraFrame(LiveCameraPhoto photo, LiveFrameOptions options)
Stream<String> get videoWorkerEvents
Future<void> stopVideoWorker()
```
