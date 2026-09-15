---
description: >-
  Faceplugin ID Document Recognition Angular demo. Web UI calling documentProcess on port 8082.
  HTTP client — not an on-device native SDK.
---

# ID Document Recognition Angular SDK

Angular **web demo** for ID Document Recognition. Calls `POST /api/documentProcess` on a Document Reader API (default **8082**). This is **not** an on-device OCR SDK.

### Code

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-Angular" %}

### Setup

1. Start Document Reader on **8082**.
2. Follow the repo README to install and serve the UI.
3. Point the API base URL at your server if it is not `http://127.0.0.1:8082`.

### Related documentation

* [JavaScript client](id-document-recognition-javascript-sdk.md) · [React](id-document-recognition-react-sdk.md) · [Vue](id-document-recognition-vue-sdk.md) · [Glossary](../resources/glossary.md)
* [Document result JSON](document-result-json.md) · [Choose a product](../resources/choose-a-product.md)
