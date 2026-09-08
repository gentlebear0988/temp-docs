---
description: >-
  Faceplugin Liveness Detection iOS SDK. On-premise PAD against photos, screens, masks, and
  deepfakes. Xcode frameworks, setActivation, initSDK, detectImage.
---

# Liveness Detection iOS SDK

Fully on-premise **Face Liveness SDK for iOS**. Native class: `FaceLivenessSDK`. Demo bundle id in Xcode: **`com.faceplugin.faceliveness.app`**.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceLivenessDetection-iOS" %}

### Setup <a href="#setup" id="setup"></a>

1. Unzip the frameworks from [Google Drive](https://drive.google.com/drive/folders/1HzREOmFg9kBLbuso1e57j8Hk5Jk41kyr): `facelivenessdk.framework`, `FaceLivenessEngine.framework`, `onnxruntime.framework`.
2. Add the SDK frameworks to the project in Xcode (**Embed & Sign**).
3. Add `FaceLivenessSDK-Bridging-Header.h` to Build Settings.

Status codes: **0** Success, **1** Invalid license, **2** Expired, **3** Not activated, **4** Init failed.

### APIs

#### <mark style="color:orange;">setActivation:</mark> This API is used to activate the SDK <a href="#setactivation" id="setactivation"></a>

```objectivec
+(int)setActivation:(NSString*)license;
```

| **Input**        | <ul><li><strong>license</strong> (NSString*): The license string (<code>FP1.…</code>)</li></ul> |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| **Return value** | <p>The SDK activation status code.</p><ul><li>0: Success</li><li>1: Invalid license</li><li>2: Expired</li><li>3: Not activated</li><li>4: Init failed</li></ul> |

#### <mark style="color:orange;">initSDK:</mark> This API is used to initialize the SDK <a href="#initsdk" id="initsdk"></a>

```objectivec
+(int)initSDK;
```

#### <mark style="color:orange;">getMachineCode:</mark> This API is used to retrieve the machine code <a href="#getmachinecode" id="getmachinecode"></a>

```objectivec
+(NSString*)getMachineCode;
```

#### <mark style="color:orange;">getLicenseStatus:</mark> This API is used to read the license tier <a href="#getlicensestatus" id="getlicensestatus"></a>

```objectivec
+(NSString*)getLicenseStatus;
+(BOOL)allowsLiveness;
+(NSString*)lastLicenseError;
```

#### <mark style="color:orange;">detectImage:</mark> This API is used to detect faces and determine if the faces are real or fake <a href="#detectimage" id="detectimage"></a>

```objectivec
+(NSString*)detectImage:(UIImage*)image crop:(BOOL)crop flags:(int)flags;
```

| **Input**        | <ul><li><strong>image</strong> (UIImage*): The input image</li></ul> |
| ---------------- | -------------------------------------------------------------------- |
| **Return value** | JSON string with detected faces and liveness scores.                   |

The liveness score ranges from 0.0 to 1.0. If it's greater than the threshold, it's real face. Demo default threshold is **0.5**.

#### <mark style="color:orange;">VideoWorker:</mark> This API is used for the live camera HUD <a href="#videoworker" id="videoworker"></a>

```objectivec
+(int)startVideoWorkerWithMatchThreshold:(float)threshold;
+(int)addVideoWorkerFrame:(UIImage*)image;
+(int)addVideoWorkerSampleBuffer:(CMSampleBufferRef)sampleBuffer;
+(void)stopVideoWorker;
```

The liveness demo does **not** enroll a match database.

#### <mark style="color:orange;">deinitSDK:</mark> This API is used to unload the engine <a href="#deinitsdk" id="deinitsdk"></a>

```objectivec
+(int)deinitSDK;
```
