---
description: >-
  Faceplugin ID Document Recognition React web demo. Call the on-premise Document Reader
  HTTP API from a React app for OCR and authenticity.
---

# ID Document Recognition React SDK

React web demo for Faceplugin ID Document Recognition. Same HTTP API as Linux / Docker (`POST /api/documentRecognition`, `/api/documentLiveness`, `/api/documentProcess` on port **8082**).

### Code <a href="#setup" id="setup"></a>

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-React" %}

### Setup <a href="#setup" id="setup"></a>

Start the Document Reader API (Linux Docker on **8082**), then run the React demo from the repository README. This is a web client — it does not load `libDocSDK`.

Point the demo at `http://127.0.0.1:8082`. Parse results with [Document result JSON](document-result-json.md). Sibling clients: [JavaScript](id-document-recognition-javascript-sdk.md), [Vue](id-document-recognition-vue-sdk.md), [Angular](id-document-recognition-angular-sdk.md).

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
