---
description: >-
  Faceplugin vs KBY-AI. Both publish on-premise face recognition and liveness SDKs for mobile
  and Docker. Compare public catalogs against Faceplugin shipping Apps.
---

# Faceplugin vs KBY-AI

[KBY-AI](https://kby-ai.com/face-recognition-sdk/) lists on-premise face recognition and liveness for Windows, Linux/Docker, Android, iOS, Flutter, React Native, and Ionic, plus HTTP APIs and machine-id licenses. GitHub demos use `getMachineCode` / `setActivation` / `initSDK` patterns.

The **surface area overlaps** Faceplugin. Treat accuracy, model packs, and license terms as **vendor-specific**. These docs only guarantee Faceplugin behavior.

| Criterion | Faceplugin | KBY-AI |
| --- | --- | --- |
| On-premise / offline | Yes | Yes (vendor site) |
| Android / iOS | Yes | Yes (vendor site) |
| Flutter / React Native / Ionic | FR + Document yes | Vendor site lists FR plugins |
| Face Liveness Flutter/RN | No public App | Check vendor |
| Windows / Linux | Yes | Yes |
| Docker HTTP API | Yes (`faceplugin/*`, ports 8082–8086) | Yes (vendor Docker demos; ports differ) |
| Face recognition | Yes | Yes |
| Face liveness | Yes (passive JPEG / camera) | Yes (vendor site) |
| Passport OCR / document SDK | Yes | Check vendor (ID products exist on kby-ai.com — verify) |
| Document liveness | Yes | Check vendor |
| NIST FRVT | Evaluated matching (Faceplugin docs) | Vendor also claims NIST ranking — compare the actual FRVT report, not marketing |
| License | `FP1.…` / `FPMC1.…` | Machine ID / lifetime server licenses (vendor docs) |

**Choose Faceplugin** when you need **document OCR + document liveness + face** in one documented suite, Faceplugin Docker Hub names, and the `FPMC1.` machine-code format used in these guides.

**Look at KBY-AI** when their GitHub/Docker samples match your stack; confirm ID/document coverage and FRVT entries independently.

Integrate Faceplugin: [Android Face Recognition](../../face-recognition-sdk/face-recognition-android-sdk.md) · [Liveness Linux](../../liveness-detection-sdk/liveness-detection-linux-sdk.md) · [Document Linux](../../id-document-recognition-sdk/id-document-recognition-linux-sdk.md)

### Related documentation

* [SDK comparison index](README.md) · [Choose a product](../choose-a-product.md)
* [FAQ](../faq.md) · [Try it](../try-it.md)
