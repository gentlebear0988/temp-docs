---
description: >-
  Faceplugin open-source Face Recognition Windows SDK. Free on-premise Python sample. Lower accuracy than the commercial HTTP API on port 8083.
---

# Open Source Face Recognition Windows SDK

### Code <a href="#code" id="code"></a>

{% embed url="https://github.com/Faceplugin-ltd/Open-Source-Face-Recognition-SDK" %}
Free open-source Face Recognition Windows SDK
{% endembed %}

### Overview <a href="#overview" id="overview"></a>

Free **open-source** Face Recognition sample for Windows (Python). Detect faces, extract embeddings, and compare them **on your machine** — no Faceplugin cloud.

Accuracy is **lower** than the commercial [Face Recognition Windows SDK](face-recognition-windows-sdk.md). Contact Faceplugin if you need the higher-accuracy native engine.

The Windows library path in `face_util/faceutil.py` should be:

```
dll_path = os.path.abspath(os.path.dirname(__file__)) + '/C/FaceUtil.dll'
```

### Setup <a href="#setup" id="setup"></a>

Please download anaconda on your computer and install it. We used Windows machine without GPU for testing

1.  **Create anaconda environment**

    `conda create -n facesdk python=3.9`
2.  **Activate env**

    `conda activate facesdk`
3.  **Install dependencies**

    `pip install -r requirements.txt`
4.  **Compare face images in the** `test` **directory**

    `python run.py`

### APIs and Parameters

* **GetImageInfo(image, faceMaxCount):** returns face bounding boxes, landmarks and feature embedding
* **get\_similarity(feat1, feat2):** returns similarity between two feature embeddings. 0 to 100
* **Threshold:** value to determine if two embeddings belong to same person, default = 75


### FAQ

**Same accuracy as the commercial API?** No. Use [Face Recognition Windows SDK](face-recognition-windows-sdk.md) on port **8083** for the commercial engine.

### Related documentation

* [Faceplugin Face Recognition Server SDK](server-sdk.md) · [Open Source Linux](open-source-face-recognition-linux-sdk.md) · [Glossary](../resources/glossary.md)
* Lower accuracy than the commercial [Windows HTTP API](face-recognition-windows-sdk.md).
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/README.md)
