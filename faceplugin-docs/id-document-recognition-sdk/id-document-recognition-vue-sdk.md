---
description: >-
  Faceplugin ID Document Recognition Vue demo. Web UI calling documentProcess on port 8082.
  HTTP client — not an on-device native SDK.
---

# ID Document Recognition Vue SDK

Vue **web demo** for ID Document Recognition. Calls `POST /api/documentProcess` on a Document Reader API (default **8082**). This is **not** an on-device OCR SDK.

### Code

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Vue" %}

### Setup

1. Start Document Reader on **8082**.
2. Follow the repo README (`npm install` / start). Point the Vite env URL at your API if needed.
3. Use Result / Security / Images / Raw JSON tabs like the Gradio demo.

### Related documentation

* [JavaScript client](id-document-recognition-javascript-sdk.md) · [React](id-document-recognition-react-sdk.md) · [Angular](id-document-recognition-angular-sdk.md)
* [Document result JSON](document-result-json.md) · [Choose a product](../resources/choose-a-product.md)
