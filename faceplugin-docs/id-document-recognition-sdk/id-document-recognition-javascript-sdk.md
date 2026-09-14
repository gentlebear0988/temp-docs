---
description: >-
  Faceplugin ID Document Recognition JavaScript SDK. Browser and Node HTTP client for
  documentProcess against the Document Reader API on port 8082. Not libDocSDK.
---

# ID Document Recognition JavaScript SDK

Browser + Node **HTTP client** for the Document Reader API. It does **not** load `libDocSDK`. Point it at Linux/Windows Python (**8082**), or Node / Go / C++ servers that expose the same routes.

### Code

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-JavaScript" %}

### Setup

1. Start a Document Reader API on **8082** ([Linux](id-document-recognition-linux-sdk.md) / [Windows](id-document-recognition-windows-sdk.md) / Node).
2. Clone and run the demo (`http://127.0.0.1:5176/demo/` — see repo README).

```js
const client = new DocumentReaderClient("http://127.0.0.1:8082");
const result = await client.documentProcess([
  { image: frontB64, page_idx: 0 },
]);
```

### APIs (client)

| Method | Maps to |
| --- | --- |
| `health()` | `GET /api/health` |
| `licenseStatus()` | `GET /api/licenseStatus` |
| `machineCode()` | `GET /api/machinecode` |
| `documentProcess(images, options)` | `POST /api/documentProcess` |
| `generalProcess(image, options)` | `POST /api/generalProcess` |

Parse fields with [Document result JSON](document-result-json.md).

### Related documentation

* [Linux SDK](id-document-recognition-linux-sdk.md) · [React](id-document-recognition-react-sdk.md) · [Vue](id-document-recognition-vue-sdk.md) · [Angular](id-document-recognition-angular-sdk.md)
* [Choose a product](../resources/choose-a-product.md) · [Request a License](../request-a-license-and-support.md)
