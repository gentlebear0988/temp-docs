---
description: >-
  Faceplugin open-source Face Recognition JavaScript SDK. On-premise browser face matching and liveness (npm faceplugin). Not the commercial Android/iOS engine.
---

# Open Source Face Recognition Javascript SDK

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Javascript" %}
Completely Free and Open Source Face recognition Javascript SDK
{% endembed %}

### Overview <a href="#overview" id="overview"></a>

Free **open-source** Face Recognition JavaScript sample for the browser. Face matching (and optional liveness helpers in the sample) run **in the user's tab** — no Faceplugin cloud.

This is **not** the commercial Android/iOS or HTTP Face Recognition engine. Contact Faceplugin if you need higher accuracy.
### Setup

```
npm install faceplugin
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

**Is this the commercial SDK?** No. Browser `npm faceplugin`. Contact Faceplugin for the higher-accuracy native engine.

**On-premise?** Processing stays in the user's tab.

### Related documentation

* [Faceplugin Face Recognition Mobile SDK](mobile-sdk.md)
* [Open Source React](open-source-face-recognition-react-sdk.md) · [Open Source Vue](open-source-face-recognition-vue-sdk.md)
* This browser SDK is **not** the commercial Android/iOS engine.
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/README.md)
