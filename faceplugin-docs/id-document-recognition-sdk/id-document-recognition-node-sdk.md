---
description: >-
  Faceplugin ID Document Recognition Node.js HTTP API. Same documentProcess routes as Python
  on port 8082. Optional native libDocSDK; stub without it.
---

# ID Document Recognition Node SDK

Node.js **HTTP API** with the same routes as the Python Document Reader server (`POST /api/documentProcess`, license routes, …). Default port **8082**. No Docker.

Native `libDocSDK` is optional. Without it the server can run a Gradio-shaped stub (`DOCSDK_STUB=1`). For production OCR, use the Python Linux/Windows HTTP SDK or provide the native library.

### Code

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Node" %}

### Setup

```bash
npm start
```

Web demos (React / Vue / Angular / JavaScript) can point at this process on **8082**.

Also public: [Go](https://github.com/Faceplugin-ltd/ID-Document-Recognition-Go) and [C/C++](https://github.com/Faceplugin-ltd/ID-Document-Recognition-CPP) HTTP APIs with the same route family.

### Related documentation

* [Linux SDK](id-document-recognition-linux-sdk.md) · [JavaScript client](id-document-recognition-javascript-sdk.md)
* [Document result JSON](document-result-json.md) · [Choose a product](../resources/choose-a-product.md)
