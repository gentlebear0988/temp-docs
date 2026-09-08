---
description: >-
  Faceplugin document security check fields. Authenticity JSON keys customers receive:
  uvLuminescence, hologramIntegrity, photoOriginAnalysis, nested checks title and result.
---

# Document security check fields

When authenticity is **on** and the license includes Liveness, `recognize` / `documentProcess` add a `security` object. This page is the **customer JSON** contract — keys and titles your UI can show.

Needs `"Authenticity": "normal"` (or mobile `recognize(..., "normal")`). `"none"` omits `security`. Not every document produces every key.

### Shape

```json
{
  "security": {
    "overall": "success",
    "label": "Pass",
    "pages": [
      {
        "pageIndex": 0,
        "overall": "success",
        "label": "Pass",
        "uvLuminescence": {
          "title": "Ultraviolet luminescence analysis",
          "result": "success",
          "checks": {
            "unexpectedUvGlow": {
              "title": "Unexpected UV glow",
              "result": "fail"
            }
          }
        }
      }
    ]
  }
}
```

| Field | Meaning |
| ----- | ------- |
| `overall` / `label` | Rolled-up page or document status |
| `pages[]` | Front is `pageIndex` **0**, back **1** |
| group `title` | Ready-made heading for your list |
| group `result` | `success`, `fail`, or `notChecked` |
| group `score` | Percent, mainly `securityPattern` |
| `checks` | Nested sub-checks. **Omitted** when that sub-check was not run (`notChecked`) |

`verification.security` uses **0** Pass, **1** Fail, **2** Not checked. That is a **different** mapping from `security.*.result` strings.

### Group keys (page-level)

These names are stable in the JSON. The title is also on the object — prefer `title` for UI.

| Key | Title |
| --- | ----- |
| `uvLuminescence` | Ultraviolet luminescence analysis |
| `uvFiber` | Ultraviolet fiber analysis |
| `uvText` | Ultraviolet text verification |
| `irMrz` | Infrared MRZ analysis |
| `irVisibility` | Infrared visibility analysis |
| `securityPattern` | Security pattern analysis (often a **score** %) |
| `laminateProtection` | Laminate protection analysis |
| `opticallyVariable` | Optically variable feature verification |
| `hologramIntegrity` | Hologram integrity verification |
| `kineticFeature` | Kinetic optical verification |
| `letterpressPattern` | Letterpress pattern verification |
| `physicalDocument` | Physical document verification |
| `photoOriginAnalysis` | Photo origin analysis |
| `portraitRegion` | Portrait area verification |
| `portraitMatch` | Portrait consistency verification |
| `barcodeFormat` | Barcode format verification |
| `covertPersonalInfo` | Covert personal information verification |
| `protectedPersonalInfo` | Protected personal information verification |
| `biometricImpression` | Biometric impression verification |
| `textCrosscheck` | Text consistency analysis |
| `mrzCrosscheck` | MRZ consistency analysis |

A page also has metadata keys you should skip when listing checks: `pageIndex`, `overall`, `label`, `pages`, `presentation`.

### Nested `checks` keys

Each value is `{ "title", "result" }`. Presence depends on the document and capture (visible light vs UV/IR hardware).

| Key | Title |
| --- | ----- |
| `unexpectedUvGlow` | Unexpected UV glow |
| `uvVisible` | UV-visible element |
| `hologramPresent` | Hologram presence |
| `hologramStill` | Still hologram |
| `hologramAngles` | Multi-angle hologram |
| `hologramMotion` | Moving hologram |
| `opticalInk` | Optical ink verification |
| `laserInk` | Laser-etched ink |
| `patternIntact` | Unbroken pattern |
| `patternAligned` | Pattern alignment |
| `patternColor` | Pattern color match |
| `patternWeight` | Pattern line thickness |
| `irHiddenPattern` | Pattern hidden in infrared |
| `blankArea` | Unused area |
| `fillArea` | Printed background |
| `photoArea` | Document photo |
| `photoIntegrity` | Photo authenticity |
| `photoSize` | Photo size |
| `photoColor` | Photo color |
| `photoShape` | Photo shape |
| `photoCorners` | Photo corners |
| `mrzArea` | Machine-readable zone |
| `barcodeArea` | Barcode area |
| `barcodeSize` | Barcode size |
| `barcodePattern` | Barcode pattern verification |
| `ghostImage` | Ghost portrait |
| `ghostClarity` | Ghost image clarity |
| `portraitVsGhost` | Photo vs ghost image |
| `portraitVsChip` | Photo vs chip portrait |
| `portraitVsPrint` | Photo vs printed portrait |
| `portraitVsLive` | Photo vs live face |
| `portraitVsBarcode` | Photo vs barcode image |
| `chipVsLive` | Chip portrait vs live face |
| `chipVsBarcode` | Chip vs barcode portrait |
| `chipVsGhost` | Chip vs ghost image |
| `barcodeVsLive` | Barcode vs live face |
| `barcodeVsGhost` | Barcode vs ghost image |
| `ghostVsLive` | Ghost vs live face |
| `extraVsPrint` | Extra photo vs printed portrait |
| `extraVsChip` | Extra photo vs chip portrait |
| `extraVsLive` | Extra photo vs live face |
| `extraVsBarcode` | Extra photo vs barcode |
| `extraVsGhost` | Extra photo vs ghost |
| `displayAttack` | Display attack detection |
| `digitalSource` | Digital source detection |
| `digitalSeal` | Digital signature |
| `contactChip` | Contact chip |
| `microprint` | Microprint |
| `hiddenObject` | Hidden element |
| `hiddenFeature` | Hidden feature verification |
| `lowContrast` | Low-contrast element |
| `printedText` | Printed text |
| `depthAnalysis` | 3D depth analysis |
| `faceDetection` | Face verification |
| `faceLandmarks` | Face landmarks |
| `noFace` | Restricted area is empty |
| `headPose` | Head position |
| `documentGeometry` | Document geometry analysis |
| `monochromeCopy` | Monochrome reproduction detection |
| `variablePrint` | Variable print verification |
| `ageMatch` | Age consistency |
| `sexMatch` | Sex consistency |

{% hint style="info" %}
A missing key means that check was not run for this image — not that it passed. Do not treat absence as `success`.
{% endhint %}

Top-level recognize contract: [Document result JSON](document-result-json.md).
