---
description: >-
  Deploy and host Faceplugin server SDKs. Architecture, hosting requirements, and production
  checklist for Linux, Docker, and Windows.
icon: server
layout:
  description:
    visible: true
---

# Deploy and host

Use this section when you put Faceplugin on **your** servers. Faceplugin does not host inference for you after you activate a license.

| Page | Read it when you need to |
| --- | --- |
| [Architecture](architecture.md) | Combine products, choose HTTP vs `sdk.py`, know what you own |
| [Hosting requirements](hosting-requirements.md) | Size CPU, RAM, disk, ports, and Docker flags |
| [Production deployment](production-deployment.md) | Harden a first-run install for production |

For eKYC servers, prefer [Face Recognition + Liveness](../face-recognition-sdk/recognition-and-liveness.md) and [Document Recognition + Liveness](../id-document-recognition-sdk/recognition-and-liveness.md) instead of separate recognition-only and liveness-only containers. Start with a platform page for install steps, then use this section for topology and ops.

### Related documentation

* [HTTP API](../http-api/) · [Choose a product](../resources/choose-a-product.md) · [Request a License](../request-a-license-and-support.md)
