---
description: >-
  Faceplugin Liveness Detection Android SDK. On-premise PAD against photos, screens, masks,
  and deepfakes. AAR, setActivation, init, faceDetection, detect.
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

# Liveness Detection Android SDK

Fully on-premise **Face Liveness SDK for Android** (presentation-attack detection). The demo does not enroll people or run 1:N search. It scores whether the face is real.

Public class: `com.faceplugin.facelivenessdk.FaceLivenessSDK`. Demo id: **`com.faceplugin.faceliveness`**.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceLivenessDetection-Android" %}

### Setup <a href="#setup" id="setup"></a>

1. Copy the SDK (`libfacesdk` folder) to the `root` folder in your project. Place `facelivenessdk.aar` from [Google Drive](https://drive.google.com/drive/folders/1x3jt02f-YHsk4WD_QlnKJSx5uQ5Ds4xH) inside `libfacesdk/`.
2. Add SDK to the project in `settings.gradle`

```
rootProject.name = "YourProjectName"
include ':app'
include ':libfacesdk'
```

3. Add dependency to your `build.gradle`

```
implementation project(path: ':libfacesdk')
```

4. minSdk **24**, `useLegacyPackaging = true`, CAMERA permission. Call **setActivation → init** on a **background** thread.

Status codes: **0** Success, **1** Invalid license, **2** Expired, **3** Not activated, **4** Init failed.

### APIs

#### <mark style="color:orange;">setActivation:</mark> This API is used to activate the SDK <a href="#setactivation" id="setactivation"></a>

```java
public static int setActivation(Context context, String license);
```

| **Input**        | <ul><li><strong>context</strong> (Context): Android <code>Context</code></li><li><strong>license</strong> (String): The license string (<code>FP1.…</code>)</li></ul> |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Return value** | <p>The SDK activation status code.</p><ul><li>0: Success</li><li>1: Invalid license</li><li>2: Expired</li><li>3: Not activated</li><li>4: Init failed</li></ul>       |

#### <mark style="color:orange;">init:</mark> This API is used to initialize the SDK <a href="#init" id="init"></a>

```java
public static int init(Context context) throws IOException;
```

#### <mark style="color:orange;">getMachineCode:</mark> This API is used to retrieve the machine code <a href="#getmachinecode" id="getmachinecode"></a>

```java
public static String getMachineCode(Context context);
```

#### <mark style="color:orange;">getLicenseStatus:</mark> This API is used to read the license tier <a href="#getlicensestatus" id="getlicensestatus"></a>

```java
public static String getLicenseStatus();
public static boolean allowsLiveness();
public static String lastEngineError();
```

Use `allowsLiveness()` before Capture.

#### <mark style="color:orange;">faceDetection:</mark> This API is used to detect faces and determine if the faces are real or fake <a href="#facedetection" id="facedetection"></a>

```java
public static List<FaceBox> faceDetection(Bitmap bitmap, FaceDetectionParam param);
```

| **Input**        | <ul><li><strong>bitmap</strong> (Bitmap): The Bitmap image</li><li><strong>param</strong> (<strong>FaceDetectionParam</strong>): Parameters for face detection</li></ul> |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Return value** | A list of **FaceBox** objects representing the detected faces and their liveness scores.                                                                              |

**FaceDetectionParam**

```java
public class FaceDetectionParam {
    public boolean check_liveness = false; // set it to true to check liveness
    public int check_liveness_level = 0; // 0: accurate model, 1: light model
    public boolean check_eye_closeness = false;
    public boolean check_face_occlusion = false;
    public boolean check_pose = true;
    public boolean check_landmarks = true;
    public boolean check_quality = false;
}
```

**FaceBox**

```java
public class FaceBox {
    public int x1, y1, x2, y2;
    public float liveness, yaw, roll, pitch;
    public float face_quality, face_luminance, score;
    public int trackId;
    public String livenessLabel;
}
```

The liveness score ranges from 0.0 to 1.0. If it's greater than the threshold, it's real face. Demo default threshold is **0.5**.

#### <mark style="color:orange;">detect:</mark> This API is used to detect faces and return engine JSON <a href="#detect" id="detect"></a>

```java
public static String detect(Bitmap bitmap, boolean crop, int flags);
```

`detect` requires a liveness-capable license.

#### <mark style="color:orange;">VideoWorker:</mark> This API is used for the live camera HUD <a href="#videoworker" id="videoworker"></a>

The demo does **not** enroll. VideoWorker match DB is empty. Use it to keep a live track while you still score with `faceDetection`:

`startVideoWorker` → `addVideoWorkerFrame` → `stopVideoWorker`.

#### <mark style="color:orange;">deinit:</mark> This API is used to unload the engine <a href="#deinit" id="deinit"></a>

```java
public static int deinit();
```

### Run the demo

1. Place `facelivenessdk.aar` in `libfacesdk/` (see Setup).
2. Keep `applicationId` **`com.faceplugin.faceliveness`**.
3. Run on a **physical** phone.
4. Home tiles: **Liveness**, Settings, About. The demo does **not** enroll people or run 1:N search.

### Screenshots

| Home | Liveness | Settings | About |
| ---- | -------- | -------- | ----- |
| <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-liveness/mobile/home.png" alt="Faceplugin Face Liveness Android home" width="180"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-liveness/mobile/liveness.png" alt="Faceplugin Face Liveness live camera" width="180"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-liveness/mobile/settings.png" alt="Faceplugin Face Liveness settings" width="180"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-liveness/mobile/about.png" alt="Faceplugin Face Liveness About" width="180"/></p> |

### License

Licenses are **offline** and bound to your `applicationId`. Request a new `FP1.…` for **your** id. Use `allowsLiveness()` before Capture.

{% hint style="warning" %}
`FaceDetectionParam.check_liveness` defaults to **false**. Set it to **true** or you will not get a liveness score.
{% endhint %}

### Try it (after the demo compiles)

```java
FaceDetectionParam param = new FaceDetectionParam();
param.check_liveness = true;
param.check_liveness_level = 0; // 0 accurate, 1 light
List<FaceBox> faces = FaceLivenessSDK.faceDetection(bitmap, param);
if (!faces.isEmpty() && faces.get(0).liveness >= 0.5f) {
    // Real
}
```

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
