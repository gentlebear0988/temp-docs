---
description: >-
  Faceplugin open-source Face Recognition Vue SDK. On-premise browser wrapper of the JavaScript face matching SDK. Not the commercial native engine.
---

# Open Source Face Recognition Vue SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-Vue" %}

### Overview <a href="#overview" id="overview"></a>

Free **open-source** Face Recognition Vue sample for the web. It wraps the open-source JavaScript browser SDK. Processing stays in the user's browser.

This is **not** the commercial native Face Recognition SDK. Contact Faceplugin if you need higher accuracy.

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
npm run dev
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

**Is this the commercial native SDK?** No. It wraps the open-source JavaScript browser SDK.

### Related documentation

* [Open Source Javascript SDK](open-source-face-recognition-javascript-sdk.md) · [React](open-source-face-recognition-react-sdk.md)
* [Faceplugin Face Recognition Mobile SDK](mobile-sdk.md)
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/README.md)
