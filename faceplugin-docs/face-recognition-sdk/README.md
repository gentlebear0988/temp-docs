---
description: >-
  Faceplugin Face Recognition SDK. Fully on-premise, NIST FRVT evaluated face matching
  for Android, iOS, Flutter, React Native, Windows, Linux, and Docker.
---

# Face Recognition SDK

### Overview

Discover our cutting-edge **Face Recognition SDK**, a **cross-platform, on-premise solution** built to deliver high-performance biometric authentication and identification. Utilizing our **NIST FRVT top-ranked face recognition algorithm**, this SDK ensures industry-leading accuracy and speed for a wide range of applications.

### Features

* [x] Face Detection
* [x] Face Landmark Detection
* [x] Face Template Extraction
* [x] Face Template Matching
* [x] Live 1:N Identify
* [x] Liveness Detection
* [x] Pose Estimation
* [x] Fully On-Premise

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td><strong>Android SDK</strong></td><td></td><td><a href="../.gitbook/assets/android.png">android.png</a></td><td><a href="face-recognition-android-sdk.md">face-recognition-android-sdk.md</a></td></tr><tr><td></td><td><strong>iOS SDK</strong></td><td></td><td><a href="../.gitbook/assets/apple-logo-3-300x300.png">apple-logo-3-300x300.png</a></td><td><a href="face-recognition-ios-sdk.md">face-recognition-ios-sdk.md</a></td></tr><tr><td></td><td><strong>React Native</strong></td><td></td><td></td><td><a href="face-recognition-android-sdk-1.md">face-recognition-android-sdk-1.md</a></td></tr><tr><td></td><td><strong>Flutter</strong></td><td></td><td></td><td><a href="face-recognition-android-sdk-2.md">face-recognition-android-sdk-2.md</a></td></tr><tr><td></td><td><strong>Ionic Capacitor</strong></td><td></td><td></td><td><a href="face-recognition-ionic-capacitor-sdk.md">face-recognition-ionic-capacitor-sdk.md</a></td></tr><tr><td></td><td>Windows SDK</td><td></td><td></td><td><a href="face-recognition-windows-sdk.md">face-recognition-windows-sdk.md</a></td></tr><tr><td></td><td>Linux SDK</td><td></td><td><a href="../.gitbook/assets/linux_PNG1 (1).png">linux_PNG1 (1).png</a></td><td><a href="face-recognition-linux-sdk.md">face-recognition-linux-sdk.md</a></td></tr><tr><td></td><td>Linux (Recognition + Liveness)</td><td></td><td></td><td><a href="face-recognition-sdk-linux.md">face-recognition-sdk-linux.md</a></td></tr></tbody></table>

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

###
