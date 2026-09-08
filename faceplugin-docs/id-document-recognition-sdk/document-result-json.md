---
description: >-
  ID Document Recognition result JSON. documentName, OCR, MRZ, barcode, verification, image
  quality, images, and security fields returned by recognize and documentProcess on every platform.
---

# Document result JSON

`recognize` (mobile) and `POST /api/documentProcess` (Linux / Windows) return the **same idea**: one JSON object. Dedicated `documentRecognition` / `documentLiveness` (and the matching HTTP paths) use the same JSON shape with recognition-only or authenticity-only fields populated. Flutter, React Native, and Ionic **normalize Android output** so it matches this **iOS-shaped** contract.

Parse this object in your app. Do not copy the demo Result screen.

### Top-level fields

| Field | Meaning |
| ----- | ------- |
| `errorCode` | Optional engine error |
| `documentName` | Document type name |
| `countryName` | Issuing country |
| `score` | Document / locate confidence |
| `msg` | Optional message |
| `verification` | Field and document checks |
| `imageQuality` | Capture quality checks (omitted when `response.ImageQuality` is `"none"`) |
| `ocr` | Visual-zone fields |
| `mrz` | Machine-readable zone |
| `barcode` | Barcode / QR fields |
| `images` | Crops (portrait, document, signature, …). Recognition only; omitted on `documentLiveness`. |
| `security` | Authenticity / document liveness (license-gated) |

### `verification`

| Key | Meaning |
| --- | ------- |
| `overall` | Whole-document verdict |
| `docType` | Type check |
| `expiry` | Expiry check |
| `text` | OCR consistency |
| `mrz` | MRZ check |
| `security` | Authenticity rolled up |
| `imageQA` | Image quality rolled up |
| `portrait` | Portrait check |
| `reasons` | Optional list of fail reasons |

Values: **0** Pass, **1** Fail, **2** Not checked.

### `imageQuality.checks`

Typical keys (order used in the Android demo): `focus`, `glares`, `resolution`, `colorness`, `perspective`, `bounds`, `portrait`, `handwritten`, `brightness`, `occlusion`.

Each check uses `CheckResult`: **0** Fail, **1** Pass, **2** Not checked. That is **not** the same 0/1/2 mapping as `verification`.

### `images[]`

Each item: `name`, `image` (often base64), optional `source`. Present on `documentRecognition` / `recognize` / `documentProcess`. **Omitted** on `documentLiveness`.

### `security`

Authenticity / document liveness (license-gated). Full key list: [Document security check fields](document-security-check-fields.md).

| Key | Meaning |
| --- | ------- |
| `overall` | Rolled-up authenticity (`success` / `fail` / `notChecked`) |
| `label` | Human-readable status |
| `pages[]` | Per-page groups (`pageIndex`, `overall`, `label`, plus check keys such as `uvLuminescence`, `hologramIntegrity`) |

Each group is `{ title, result, checks? }` or `{ title, score }` for pattern percent. Nested checks are omitted when they were not run.

Needs a **Liveness-capable** license. Mobile: pass authenticity `"normal"` into `recognize`. Server: `"Authenticity": "normal"` (Windows also documents `"strict"`). `"none"` skips Security.

### Locate JSON (camera overlay only)

`locateDocument` is **not** folded into the recognize result. Expect `score`, `position.corners`, and sometimes `_locateImageWidth` / `_locateImageHeight`. **No OCR** and **no image quality** on this path (`ImageQuality` is `"none"`).

### License status JSON

`getLicenseStatus` / `GET /api/licenseStatus`: `licensed`, `level`, `levelName`, `recognition`, `authenticity`, `label` (for example `"Recognition + Liveness"`). Home and About use `label`.

Flutter, React Native, and Ionic ship typed helpers (`recognizeResult`, `rows`, `summary`, `images`, `securityRows`) so you do not write a 600-line parser.

[Request a License & Support](../request-a-license-and-support.md) · [Contact US](../contact-us.md)
