---
description: >-
  Faceplugin open-source Face Recognition React SDK. On-premise browser wrapper
  of the JavaScript face matching SDK. Not the commercial native engine.
---

# Open Source Face Recognition React SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-React" %}

### Overview <a href="#setup" id="setup"></a>

The world's 1st **Completely Free** and **Open Source** **Face Recognition React SDK** for developers to integrate face recognition and liveness detection capabilities into web frontend. Supports real-time, high-accuracy face recognition with deep learning models.\
This is **on-premise face recognition SDK** which means everything is processed in your browser and **NO** data leaves it.\
\
**Please contact us if you need the SDK with higher accuracy.**

### How to Run

### Install dependencies

```
npm i
```

#### Copy the pretrained weight files

```
node post-install.js
```

#### Execute the react app

```
npm start
```

### APIs

*   **Face Detection**

    ```
    loadDetectionModel()
    detectFace(session, canvas_id)
    ```
*   **Face Landmark Extraction**

    ```
    loadLandmarkModel()
    predictLandmark(session, canvas_id, bbox)
    ```
*   **Face Liveness Detection**

    ```
    loadDetectionModel()
    detectFace(session, canvas_id)
    ```
*   **Face Expression Detection**

    ```
    loadExpressionModel()
    predictExpression(session, canvas_id, bbox)
    ```
*   **Face Pose Estimation**

    ```
    loadPoseModel()
    predictPose(session, canvas_id, bbox, question)
    ```
*   **Eye Closeness Detection**

    ```
    loadEyeModel()
    predictEye(session, canvas_id, landmark)
    ```
*   **Gender Detection**

    ```
    loadGenderModel()
    predictGender(session, canvas_id, landmark)
    ```
*   **Age Estimation**

    ```
    loadAgeModel()
    predictAge(session, canvas_id, landmark)
    ```
*   **Face Recognition**

    ```
    loadFeatureModel()
    extractFeature(session, canvas_id, landmarks)
    ```

### FAQ

**Is this the commercial React Native SDK?** No. It wraps the open-source JavaScript browser SDK.

### Related documentation

* [Open Source Javascript SDK](../open-source-face-recognition-javascript-sdk.md) · [Vue](../open-source-face-recognition-vue-sdk.md)
* [Faceplugin Face Recognition Mobile SDK](../mobile-sdk.md)
* [Request a License](../../request-a-license-and-support.md) · [Status codes](../../resources/status-codes.md)
* [Combining products (eKYC)](../../resources/choose-a-product.md) · [SDK comparison](../../resources/comparisons/)
