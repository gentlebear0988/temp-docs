---
description: >-
  Faceplugin ID Document Recognition React demo. Vite UI calling documentProcess on port 8082.
  HTTP client — not an on-device native SDK.
---

# ID Document Recognition React SDK

React (Vite) **web demo** for ID Document Recognition. Talks to any Document Reader HTTP API via `POST /api/documentProcess`. Default `http://127.0.0.1:8082`. This is **not** an on-device OCR SDK.

### Code

{% embed url="https://github.com/Faceplugin-ltd/ID-Document-Recognition-React" %}

### Setup

1. Start Document Reader on **8082**.
2. `npm install` then `npm start` (or `VITE_DOCUMENT_RECOGNITION_URL=http://127.0.0.1:8082 npm start`).
3. Open **http://127.0.0.1:5173/** — tabs Result / Security / Images / Raw JSON.

For native mobile, use [Flutter](id-document-recognition-flutter-sdk.md) or [React Native](id-document-recognition-react-native-sdk.md).

### Related documentation

* [JavaScript client](id-document-recognition-javascript-sdk.md) · [Document result JSON](document-result-json.md)
* [Linux SDK](id-document-recognition-linux-sdk.md) · [Choose a product](../resources/choose-a-product.md)
