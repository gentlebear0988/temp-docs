---
description: >-
  Faceplugin ID Document Recognition JavaScript SDK. Browser and Node HTTP client for
  OCR, MRZ, and authenticity against the on-premise Document Reader API on port 8082.
---

# ID Document Recognition JavaScript SDK

JavaScript **HTTP client** for Faceplugin ID Document Recognition (browser and Node.js). This package does **not** load `libDocSDK`. Run it against the Linux, Windows, Node, Go, or C++ API on port **8082**.

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-JavaScript" %}

### Setup <a href="#setup" id="setup"></a>

```
npm test
python -m http.server 5176
```

Open `http://127.0.0.1:5176/demo/` with the API at `http://127.0.0.1:8082`.

Web demos: [React](https://github.com/Faceplugin-ltd/ID-Document-Recognition-React) · [Vue](https://github.com/Faceplugin-ltd/ID-Document-Recognition-Vue) · [Angular](https://github.com/Faceplugin-ltd/ID-Document-Recognition-Angular).

### APIs

#### <mark style="color:orange;">documentRecognition:</mark> This API is used to run OCR / MRZ / barcode / image quality only

```js
import { DocumentReaderClient } from "./src/index.js";
const client = new DocumentReaderClient("http://127.0.0.1:8082");
await client.documentRecognition({ images: [{ image: base64Front }] });
```

#### <mark style="color:orange;">documentLiveness:</mark> This API is used to run authenticity / security only

```js
await client.documentLiveness({ images: [{ image: base64Front }] });
```

#### <mark style="color:orange;">documentProcess:</mark> This API is used to run the combined pipeline

```js
await client.documentProcess({
  images: [{ image: base64Front }],
  response: { OCR: "normal", Authenticity: "normal" },
});
```
