# SentinelEdge AI
**Offline Deepfake Detector for Field Ops**

![Status](https://img.shields.io/badge/Status-Prototype-green)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Platform](https://img.shields.io/badge/Edge-OnDevice-purple)

## What is SentinelEdge?
**SentinelEdge** is a lightweight AI agent that helps soldiers and field operatives detect deepfakes in real-time.

Unlike standard detection tools that need the cloud, SentinelEdge runs **100% offline**. It lives directly on the device (laptop, body-cam, or phone), scanning audio and video feeds to spot fake content instantly—no internet required.

## Key Features
* **Zero Internet Needed:** Built for disconnected environments (DIL) where the cloud isn't an option.
* **Real-Time Alerts:** Gives an immediate "Red/Green" signal if media is fake.
* **Smart Detection:** Uses a lightweight AI (MobileNetV3) that doesn't kill your battery.
* **Secure:** All analysis happens locally; no data ever leaves the device.

## How It Works (The Logic)
The system follows a simple "OODA Loop" (Observe-Orient-Decide-Act) to function autonomously:

1.  **Observe:** Listens to incoming video or audio streams.
2.  **Orient:** Checks the file quality to choose the best scan method (Fast vs. Deep).
3.  **Decide:** Combines Visual analysis (looking for artifacts) and Audio analysis (spectral checks) to give a confidence score.
4.  **Act:** Triggers a visual or haptic alert if a threat is found.

## Tech Stack
We chose these tools because they are fast, open-source, and run on standard hardware.

| Component | Tech Used | Why we used it |
| :--- | :--- | :--- |
| **Core Logic** | Python AsyncIO | To run multiple checks without lagging |
| **Vision AI** | MobileNetV3 | Detects visual glitches fast |
| **Audio AI** | Librosa | Analyzes voice patterns |
| **Inference** | ONNX Runtime | Runs AI on CPU (No GPU needed) |
| **Security** | SQLite (AES-256) | Encrypted logging for safety |
| **UI** | Streamlit | Simple, tactical dashboard |

## Quick Start
Want to try the prototype simulation? Follow these steps:

**1. Clone the repo**
```bash
git clone [https://github.com/Mankiratbedi/sentineledge.git](https://github.com/Mankiratbedi/sentineledge.git)
cd SentinelEdge