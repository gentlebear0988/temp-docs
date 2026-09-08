---
description: >-
  Faceplugin ID Document Recognition Android SDK. On-premise OCR, MRZ, barcode, and
  authenticity. documentreadersdk.aar in libdocsdk, not libfacesdk.
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

# ID Document Recognition Android SDK

Fully on-premise **ID Document Recognition SDK for Android**. Reads passports, national IDs, and driver licenses. Place `documentreadersdk.aar` in **`libdocsdk/`**, not `libfacesdk/`.

Public class: `com.faceplugin.documentreadersdk.DocumentReaderSDK`. Demo id: **`com.faceplugin.documentreader`**.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Android" %}

### Setup <a href="#setup" id="setup"></a>

1. Copy the SDK (`libdocsdk` folder) to the `root` folder in your project. Place `documentreadersdk.aar` from [Google Drive](https://drive.google.com/drive/folders/1nDSfvj0WtC1lZgzwFd7471ECVtk-nuYH) inside `libdocsdk/`.
2. Add SDK to the project in `settings.gradle`

```
rootProject.name = "YourProjectName"
include ':app'
include ':libdocsdk'
```

3. Add dependency to your `build.gradle`

```
implementation project(path: ':libdocsdk')
```

4. minSdk **24**, JDK **17**. Call **setActivation → init** off the UI thread.

Status codes: **0** Success, **1** Invalid license, **2** Expired, **3** Not activated, **4** Init failed.

### APIs

#### <mark style="color:orange;">setActivation:</mark> This API is used to activate the SDK <a href="#setactivation" id="setactivation"></a>

```java
public static int setActivation(Context context, String license);
```

#### <mark style="color:orange;">init:</mark> This API is used to initialize the SDK <a href="#init" id="init"></a>

```java
public static int init(Context context) throws IOException;
```

#### <mark style="color:orange;">getMachineCode:</mark> This API is used to retrieve the machine code <a href="#getmachinecode" id="getmachinecode"></a>

```java
public static String getMachineCode(Context context);
```

#### <mark style="color:orange;">getLicenseStatus:</mark> This API is used to read recognition and authenticity flags <a href="#getlicensestatus" id="getlicensestatus"></a>

```java
public static String getLicenseStatus();
public static String lastLicenseError();
```

JSON fields: `licensed`, `level`, `levelName`, `recognition`, `authenticity`, `label`.

#### <mark style="color:orange;">locateDocument:</mark> This API is used to find document corners on a preview frame <a href="#locatedocument" id="locatedocument"></a>

```java
public static String locateDocument(Bitmap bitmap);
```

| **Input**        | Preview bitmap. |
| ---------------- | ---------------- |
| **Return value** | JSON: corners + score. **No OCR.** Use for the overlay only. |

Also: `locateVideoFrame(byte[] nv21, int width, int height, int rotation)` for camera NV21 frames.

#### <mark style="color:orange;">recognize:</mark> This API is used to run FullProcess (OCR / MRZ / barcode / authenticity) <a href="#recognize" id="recognize"></a>

```java
public static String recognize(Bitmap bitmap);
public static String recognize(Bitmap front, Bitmap back, boolean authenticity);
public static String recognize(Bitmap front, Bitmap back, String authenticityMode);
```

| **Input**        | One image, or front + optional back. Authenticity <code>"normal"</code> / <code>"none"</code> or boolean. |
| ---------------- | ------------------------------------------------------------------------------------------------------------- |
| **Return value** | JSON: OCR / MRZ / barcode, verification, image quality, crops, security (if licensed).                   |

Verification: **0** Pass, **1** Fail, **2** Not checked.

#### <mark style="color:orange;">documentRecognition:</mark> This API is used to run OCR / MRZ / barcode / image quality only <a href="#documentrecognition" id="documentrecognition"></a>

```java
public static String documentRecognition(Bitmap front);
public static String documentRecognition(Bitmap front, Bitmap back);
```

Authenticity is always off.

#### <mark style="color:orange;">documentLiveness:</mark> This API is used to run authenticity / security only <a href="#documentliveness" id="documentliveness"></a>

```java
public static String documentLiveness(Bitmap front);
public static String documentLiveness(Bitmap front, Bitmap back);
```

OCR / MRZ / barcode / image quality are always off.

#### <mark style="color:orange;">startNewSession:</mark> This API is used to open a FullProcess session before recognize <a href="#startnewsession" id="startnewsession"></a>

```java
DocumentReaderSDK.startNewSession("{\"scenario\":\"FullProcess\",\"series\":false}");
```

#### <mark style="color:orange;">deinit:</mark> This API is used to unload the engine <a href="#deinit" id="deinit"></a>

```java
public static String deinit();
```

`deinit()` returns a **String** (not `int`).

### Run the demo

1. Place `documentreadersdk.aar` in `libdocsdk/` (not `libfacesdk`).
2. Keep `applicationId` **`com.faceplugin.documentreader`**.
3. Run on a **physical** phone.
4. Home: Camera, Gallery, About. Result tabs: OCR / MRZ / barcode, Liveness (security), Images, Raw JSON.

### Screenshots

| Home | Camera | Gallery |
| ---- | ------ | ------- |
| <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/document-reader/mobile/home.png" alt="Faceplugin Document Reader Android home" width="180"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/document-reader/mobile/camera.png" alt="Faceplugin Document Reader camera overlay" width="180"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/document-reader/mobile/gallery.png" alt="Faceplugin Document Reader gallery" width="180"/></p> |

| Result | Security | Images |
| ------ | -------- | ------ |
| <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/document-reader/mobile/result.png" alt="Faceplugin Document Reader result" width="180"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/document-reader/mobile/security.png" alt="Faceplugin Document Reader security" width="180"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/document-reader/mobile/images.png" alt="Faceplugin Document Reader crops" width="180"/></p> |

### License

Licenses are **offline** and bound to your `applicationId`. After `getLicenseStatus()`:

- **Recognition + Liveness** — OCR / MRZ / barcode **and** authenticity
- **Recognition** — OCR / MRZ / barcode; Security stays empty / not checked
- **Liveness** — authenticity only; OCR stays empty / not checked

Parse the JSON with [Document result JSON](document-result-json.md).

### Try it (after the demo compiles)

```java
DocumentReaderSDK.setActivation(context, DEMO_LICENSE);
DocumentReaderSDK.init(context);
String json = DocumentReaderSDK.recognize(front, back, "normal");
```

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
