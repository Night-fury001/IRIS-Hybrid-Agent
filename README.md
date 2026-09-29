# ⚡ I.R.I.S. (Integrated Response & Inference Server)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Decoupled%20Modular-orange?style=for-the-badge)]()
[![Inference](https://img.shields.io/badge/AI-Hybrid%20(Local%20%2F%20Cloud)-success?style=for-the-badge&logo=ollama&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Production%20Ready-critical?style=for-the-badge)]()

*An advanced, modular, voice-activated desktop assistant featuring zero-friction local LLM orchestration and strict JSON-schema intent routing.*

</div>

---

## 🎯 About The Project

**I.R.I.S.** is built to bridge the gap between heavy cloud dependencies and local system hardware. Moving away from monolithic scripts, I.R.I.S. implements a decoupled engine architecture that separates audio processing, infrastructure background management, natural language intent routing, and physical machine automation. 

Whether running offline models locally via high-performance GPU hardware or tapping into cloud inference APIs, I.R.I.S. handles context-switching seamlessly.

---

## 🏗️ System Architecture

The project is structured into independent, highly maintainable core modules:

```text
I.R.I.S/
├── main.py              # Core event loop, wake-word detection, and audio pipeline
├── engine_server.py     # Background socket orchestrator & silent process daemon
├── engine_llm.py        # LLM communication interface & strict JSON schema parser
├── engine_actions.py    # Task router (Browser automation, media playback, system ops)
├── processedCommand.py  # Central logic broker between input intent and execution
└── requirements.txt     # Project dependencies
