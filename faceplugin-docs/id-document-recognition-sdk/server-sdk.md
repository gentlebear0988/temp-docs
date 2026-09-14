---
description: >-
  Faceplugin ID Document Recognition server SDKs. On-premise OCR and authenticity HTTP
  APIs for Windows, Linux, and Docker on port 8082.
---

# Server SDK

ID Document Recognition as an HTTP API on **your** machine. Send page images; receive OCR, MRZ, barcode, image quality, and optional authenticity JSON.

Typical call order: `GET /api/machinecode` → send `FPMC1.…` → `POST /api/activate` → `POST /api/documentRecognition` / `documentLiveness` / `documentProcess`. Default port **8082**.

Parse results with [Document result JSON](document-result-json.md). Authenticity field names: [Document security check fields](document-security-check-fields.md).

Authenticity **without** OCR is a separate product: [ID Document Liveness SDK](../id-document-liveness-sdk/).

For on-device capture, use [Mobile SDK](mobile-sdk.md).

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td><strong>Windows SDK</strong></td><td>HTTP API on port 8082. No Docker on Windows.</td><td></td><td><a href="id-document-recognition-windows-sdk.md">id-document-recognition-windows-sdk.md</a></td></tr><tr><td></td><td><strong>Linux SDK</strong></td><td>Docker image faceplugin/document-reader. Same HTTP API as Windows.</td><td><a href="../.gitbook/assets/linux_PNG1 (1).png">linux_PNG1 (1).png</a></td><td><a href="id-document-recognition-linux-sdk.md">id-document-recognition-linux-sdk.md</a></td></tr></tbody></table>
