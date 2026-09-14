---
description: >-
  Request a Faceplugin offline license. Mobile FP1 keys bind to app id. Server FPMC1 machine
  codes from GET /api/machinecode. Docker and host codes differ. On-premise, no per-call cloud.
---

# Request a License & Support

Faceplugin licenses are **offline**. After activation, face matching, liveness, and document OCR do **not** need the internet.

### Need a license?

* **Mobile SDK:** contact us via WhatsApp, Telegram, or email. Demo `FP1.…` keys are bound to the **sample application id / bundle id** on each platform page. Request a new `FP1.…` if you use your own app.
* **Server SDK (Linux / Windows / Docker):** start the API once, copy `FPMC1.…` from logs or `GET /api/machinecode`, and send that code. Docker and a native host have **different** machine codes. Use the code from the environment you will run in production.

Do not paste demo `FP1.…` keys into your production app.

### FAQ

**Can Faceplugin run completely offline?** Yes, after the key is issued and activated.

**Why is my Docker machine code different from the host?** The fingerprint includes Docker. License the environment you ship.

**Status codes 1–4 on mobile?** See [Status codes](resources/status-codes.md).

### Need support?

We offer **free integration** with all our biometric solutions, ensuring a smooth and hassle-free setup for your systems. Additionally, our dedicated team provides comprehensive **after-sale and maintenance support** to guarantee optimal performance and reliability over time. Whether it's initial deployment or ongoing assistance, we are committed to supporting your needs every step of the way.

### Contact US

* Email : [info@faceplugin.com](mailto:info@faceplugin.com)
* WhatsApp : [+1 (469) 278-4822](https://wa.me/+14692784822)
* Telegram : [@faceplugin](https://t.me/faceplugin)

### Related documentation

* [Try it](resources/try-it.md) · [FAQ](resources/faq.md) · [Troubleshooting](resources/troubleshooting.md)
* [Choose a product](resources/choose-a-product.md) · [Changelog](resources/changelog.md)

{% hint style="info" %}
GitBook admin (not this markdown): custom domain, Open Graph image, sitemap, and **Google Search Console** on the docs hostname.
{% endhint %}
