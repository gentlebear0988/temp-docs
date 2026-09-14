---
description: >-
  Faceplugin Face Recognition SDK. Fully on-premise, NIST FRVT evaluated face matching
  for Android, iOS, Flutter, React Native, Windows, Linux, and Docker.
---

# Face Recognition SDK

### Overview

Discover our cutting-edge **Face Recognition SDK**, a **cross-platform, on-premise solution** built to deliver high-performance biometric authentication and identification. Utilizing our **NIST FRVT top-ranked face recognition algorithm**, this SDK ensures industry-leading accuracy and speed for a wide range of applications.

On **mobile**, the demo apps enroll people, run live **1:N Identify** with a camera (VideoWorker), and apply **passive 2D liveness**. On **Linux and Windows**, you call a still-image HTTP API: detect faces, score quality, extract a template, match two photos, or compare two templates. There is **no** server-side 1:N gallery.

If you only need spoof detection and do not enroll anyone, use the standalone [Liveness Detection SDK](../liveness-detection-sdk/).

### Features

* [x] Face Detection
* [x] Face Landmark Detection
* [x] Face Template Extraction
* [x] Face Template Matching
* [x] Live 1:N Identify (mobile)
* [x] Liveness Detection (passive 2D on mobile Identify)
* [x] Pose Estimation
* [x] Fully On-Premise

### Platforms

Pick **Mobile SDK** or **Server SDK**, then the platform page. Each page includes GitHub source, install steps, and the APIs that App actually ships.

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td><strong>Mobile SDK</strong></td><td>Android, iOS, Flutter, React Native, Ionic, and browser open-source clients.</td><td><a href="mobile-sdk.md">mobile-sdk.md</a></td></tr><tr><td></td><td><strong>Server SDK</strong></td><td>Windows, Linux / Docker, combined Recognition + Liveness, .NET, and open-source Python.</td><td><a href="server-sdk.md">server-sdk.md</a></td></tr></tbody></table>

Typical call order on **mobile**: `setActivation` → `init` → detect / extract template → store templates in **your** database → `similarity` or VideoWorker (live 1:N). Identify default **0.67**. Liveness default **0.5**.

Typical call order on **Linux / Windows**: `GET /api/machinecode` → `POST /api/activate` → `POST /api/detect` / `match` / `liveness`. There is **no** server-side 1:N gallery (`POST /api/identify` does not exist).

### Usecases

* [x] Access Control & Security
* [x] Attendance & Time Tracking
* [x] Law Enforcement & Public Safety
* [x] User Authentication for Applications
* [x] Retail & Customer Experience
* [x] Healthcare
* [x] Travel & Transportation
* [x] Smart Devices & IoT
* [x] Entertainment & Events
* [x] Education
* [x] Fraud Prevention
