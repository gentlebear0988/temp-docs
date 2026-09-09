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

All processing stays on the device. **No** biometric data is sent to Faceplugin cloud.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-Flutter" %}

### How to Run

{% stepper %}
{% step %}
## Install tools

Flutter **3.44+**, Dart **3.3+**, JDK **17+** for Android. Run `flutter doctor` and fix reported issues. Accept Android licenses: `flutter doctor --android-licenses`. `JAVA_HOME` must point to the JDK **home** (the folder that contains `bin`), not to `bin` itself.
{% endstep %}

{% step %}
## Clone and bootstrap

```bash
git clone https://github.com/Faceplugin-ltd/FaceRecognition-Flutter.git
cd FaceRecognition-Flutter
dart run tool/bootstrap.dart
```
{% endstep %}

{% step %}
## Place native runtimes

| Platform | File | Example app path | Your own app path |
| -------- | ---- | ---------------- | ----------------- |
| Android | `facerecognitionsdk.aar` | `example/android/libfacesdk/` | Copy `example/android/libfacesdk/` into **your app** `android/libfacesdk/` and `include(":libfacesdk")` |
| iOS | three frameworks | `ios/Frameworks/` | Plugin checkout `ios/Frameworks/` |

- Android Drive: [facerecognitionsdk.aar](https://drive.google.com/drive/folders/1kpzYVv9Gbm_pEpDe9-x7FGB4NWZzvez0)
- iOS Drive: [frameworks](https://drive.google.com/drive/folders/1PKmV-o7gq7s7dDtiNgXPfCi2ZlWaRy5H) (`facerecognitionsdk`, `FaceRecognitionEngine`, `onnxruntime`)

{% hint style="warning" %}
Do **not** `implementation(files(…aar))` inside the plugin — AGP will fail `bundleDebugAar`. Copy the `libfacesdk` **module** from the example into your app.
{% endhint %}

On a Mac after placing iOS frameworks: `dart run tool/bootstrap.dart` (builds matching `.xcframework`s) then `cd example/ios && pod install`. CocoaPods links the `.xcframework`s into the plugin pod — plain `.framework` alone often leaves undefined `FaceRecognitionSDK` symbols under `use_frameworks!`.
{% endstep %}

{% step %}
## Run the example

```bash
cd example
flutter run
```

Physical phone. Wait for the home status bar → **Ready**.
{% endstep %}
{% endstepper %}

Keep demo ids so the included license works:

| Platform | Id |
| -------- | -- |
| Android package name | `com.faceplugin.facerecognitionsdk` |
| iOS bundle identifier | `com.faceplugin.facerecognition.app` |

| Requirement | Value |
| ----------- | ----- |
| Flutter | 3.44+ (see `pubspec.yaml`) |
| Android | minSdk 24, physical device recommended |
| iOS | iOS 13+, physical device recommended |

Demo tiles: Enroll, Identify, Capture, Attribute, Settings, About.

### Screenshots

| Home | Identify | Capture |
| ---- | -------- | ------- |
| <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/home.png" alt="Faceplugin Face Recognition Flutter home" width="200"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/identify.png" alt="Faceplugin Face Recognition live identify" width="200"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/capture.png" alt="Faceplugin Face Recognition oval capture" width="200"/></p> |

### License

Licenses are **offline**. Demo keys live in `example/lib/core/constants/license.dart`. Request a new `FP1.…` for your own app.

Default thresholds in the example Settings: identify **0.67**, liveness **0.5**, pose **40°**, eye-close **0.5**. You pass these as Dart parameters — change them for your product.

[Request a License & Support](../request-a-license-and-support.md).

### Integrate into your own app

You need the Flutter plugin + native runtimes. You do **not** need the example UI or person database.

```yaml
dependencies:
  face_recognition_sdk:
    git:
      url: https://github.com/Faceplugin-ltd/FaceRecognition-Flutter.git
```

Then copy runtimes (table above), set your Android package name / iOS bundle identifier, add camera + photo-library permissions, and request a license for your own app.

```dart
import 'package:face_recognition_sdk/face_recognition_sdk.dart';

Future<void> activate() async {
  final code = await getMachineCode(); // FPMC1.… — send when requesting a key
  final act = await setActivation('FP1.…');
  if (act != sdkSuccess) {
    throw StateError(await lastLicenseError());
  }
  final initCode = await init();
  if (initCode != sdkSuccess) {
    throw StateError('init failed: $initCode');
  }
}

Future<void> enrollStill(String imagePath) async {
  final faces = await faceDetection(imagePath);
  if (faces.length != 1) return;
  final template = await templateExtraction(imagePath, faces.first);
  final cropB64 = await cropFace(imagePath, faces.first);
  // Store template + crop in YOUR database
}
```

Optional oval UI: `FaceCapture` from `package:face_recognition_sdk/capture`.

### APIs

```dart
import 'package:face_recognition_sdk/face_recognition_sdk.dart';
```

Call order: `getMachineCode` → `setActivation` → `init` → detect / VideoWorker → `deinit`.

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

Boxes include geometry (`x1,y1,x2,y2`), pose, liveness / quality / eyes / occlusion, age / gender / emotion / mask / glasses, optional `attributes`, and `landmarks` + `landmarkCount`.

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

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
