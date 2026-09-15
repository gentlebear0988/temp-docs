---
description: Faceplugin open-source Face Recognition SDK for Windows & Linux.
---

# Open Source Windows & Linux

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/Open-Source-Face-Recognition-SDK" %}

### Overview <a href="#setup" id="setup"></a>

The **Open Source Face Recognition SDK** by [Faceplugin](https://faceplugin.com/) is a powerful, privacy-focused solution for integrating face recognition capabilities into your applications. Built with deep learning models, this SDK provides high-accuracy face detection and recognition while ensuring complete data privacy through on-premise processing.\
\
**Please contact us if you need the SDK with higher accuracy.**



### Setup

### Prerequisites



* **Python 3.9 or higher**
* **Anaconda** (recommended for dependency management)
* **Windows or Linux** operating system

#### Setup Instructions



1.  **Install Anaconda** (if not already installed)

    ```
    # Download from: https://www.anaconda.com/products/distribution
    ```
2.  **Create and activate conda environment**

    ```
    conda create -n facesdk python=3.9
    conda activate facesdk
    ```
3.  **Install dependencies**

    ```
    pip install -r requirements.txt
    ```
4.  **Test the installation**

    ```
    python run.py
    ```

***

### Quick Start

#### Basic Usage

```
from face_recognition_sdk import FaceRecognition

# Initialize the SDK
face_sdk = FaceRecognition()

# Process an image
image_path = "path/to/your/image.jpg"
face_info = face_sdk.GetImageInfo(image_path, faceMaxCount=10)

# Compare two faces
similarity = face_sdk.get_similarity(feature1, feature2)
```

#### Example: Face Comparison

```
# Compare two images
image1 = "test/1.jpg"
image2 = "test/2.png"

# Get face information from both images
faces1 = face_sdk.GetImageInfo(image1, faceMaxCount=1)
faces2 = face_sdk.GetImageInfo(image2, faceMaxCount=1)

if faces1 and faces2:
    # Compare the first face from each image
    similarity = face_sdk.get_similarity(faces1[0]['embedding'], faces2[0]['embedding'])
    print(f"Similarity: {similarity}%")
    
    # Check if it's the same person (threshold = 75)
    is_same_person = similarity >= 75
    print(f"Same person: {is_same_person}")
```

***

### APIs

### Core Functions

**`GetImageInfo(image_path, faceMaxCount)`**

Extracts face information from an image.

**Parameters:**

* `image_path` (str): Path to the input image
* `faceMaxCount` (int): Maximum number of faces to detect

**Returns:**

* List of dictionaries containing:
  * `bbox`: Face bounding box coordinates
  * `landmarks`: Facial landmark points
  * `embedding`: Feature embedding vector



**`get_similarity(feature1, feature2)`**

Compares two face feature embeddings.

**Parameters:**

* `feature1` (array): First face embedding
* `feature2` (array): Second face embedding

**Returns:**

* Similarity score (0-100), where higher values indicate greater similarity

#### Configuration

* **Default Threshold**: 75 (for determining if two faces belong to the same person)
* **Supported Formats**: JPG, PNG, BMP, TIFF
* **Face Detection**: Automatic detection of multiple faces per image<br>

### FAQ

**Is this the commercial SDK?** No. Contact Faceplugin for the higher-accuracy native engine.

**On-premise?** Processing stays in user's device

### Related documentation

* [Faceplugin Face Recognition Mobile SDK](mobile-sdk.md)
* [Open Source React](open-source-face-recognition-react-sdk.md) · [Open Source Vue](open-source-face-recognition-vue-sdk.md)
* This browser SDK is **not** the commercial Android/iOS engine.
* [Request a License](../request-a-license-and-support.md) · [Status codes](../resources/status-codes.md)
* [Combining products (eKYC)](../resources/choose-a-product.md) · [SDK comparison](../resources/comparisons/)
