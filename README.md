# ⚡ I.R.I.S. (Integrated Response & Inference Server)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Decoupled%20Modular-orange?style=for-the-badge)]()
[![Inference](https://img.shields.io/badge/AI-Hybrid%20\(Local%20%2F%20Cloud\)-success?style=for-the-badge\&logo=ollama\&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Production%20Ready-critical?style=for-the-badge)]()

**An advanced, modular, voice-activated desktop assistant featuring zero-friction local LLM orchestration and strict JSON-schema intent routing.**

</div>

---

## 🎯 About The Project

**I.R.I.S.** is built to bridge the gap between heavy cloud dependencies and local system hardware.

Moving away from monolithic scripts, I.R.I.S. implements a **decoupled engine architecture** that separates:

* 🎙️ Audio processing
* 🧠 Natural language understanding
* 🤖 LLM inference
* 🔀 Intent routing
* ⚙️ System automation
* 🌐 Browser automation
* 🔊 Media control
* 🖥️ Background infrastructure management

Whether running offline models locally via high-performance GPU hardware or connecting to cloud inference APIs, I.R.I.S. handles context switching seamlessly.

---

## 🏗️ System Architecture

The project is structured into independent and maintainable core modules:

```text
I.R.I.S/
├── main.py              # Core event loop, wake-word detection, and audio pipeline
├── engine_server.py     # Background socket orchestrator & silent process daemon
├── engine_llm.py        # LLM communication interface & strict JSON schema parser
├── engine_actions.py    # Task router: browser, media, and system operations
├── processedCommand.py  # Central logic broker between input intent and execution
└── requirements.txt     # Project dependencies
```

This modular structure makes the system easier to understand, debug, extend, and maintain.

---

# 📖 Complete Step-by-Step Setup Guide

Follow this guide to clone, configure, and run **I.R.I.S.** on your local machine from scratch.

## 📋 Prerequisites

Before starting, make sure you have the following installed:

* **Python 3.10 or newer**
* **Git**
* A terminal such as:

  * Windows PowerShell
  * Windows Command Prompt
  * Git Bash
  * macOS Terminal
  * Linux Terminal

You can verify your installations with:

```bash
python --version
git --version
```

---

## 1️⃣ Clone the Repository

Open your terminal and clone the I.R.I.S. repository:

```bash
git clone https://github.com/Night-fury001/IRIS-Hybrid-Agent.git
```

---

## 2️⃣ Navigate Into the Project

Move into the newly cloned project directory:

```bash
cd IRIS-Hybrid-Agent
```

---

## 3️⃣ Create a Virtual Environment

Create an isolated Python environment named `.venv` inside the project directory:

```bash
python -m venv .venv
```

Using a virtual environment keeps I.R.I.S.'s dependencies isolated from your system-wide Python installation.

---

## 4️⃣ Activate the Virtual Environment

### 🪟 Windows — PowerShell

```powershell
.\.venv\Scripts\Activate
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

Then activate the environment again:

```powershell
.\.venv\Scripts\Activate
```

### 🪟 Windows — Command Prompt

```cmd
.\.venv\Scripts\activate.bat
```

### 🍎 macOS / 🐧 Linux

```bash
source .venv/bin/activate
```

Once activated, you should see something similar to:

```text
(.venv)
```

at the beginning of your terminal prompt.

---

## 5️⃣ Install Project Dependencies

Make sure your virtual environment is activated, then install all required Python packages:

```bash
python -m pip install -r requirements.txt
```

This will install the dependencies specified by the project.

---

## 6️⃣ Run I.R.I.S.

Once the dependencies are installed, start the assistant:

```bash
python main.py
```

If everything is configured correctly, I.R.I.S. should start its core event loop and initialize the required components.

---

## 🛑 Deactivate the Virtual Environment

When you're finished working with I.R.I.S., you can deactivate the virtual environment with:

```bash
deactivate
```

You can reactivate it whenever you return to the project:

```bash
.\.venv\Scripts\Activate
```

---

# 🔧 Project Workflow

At a high level, I.R.I.S. follows this pipeline:

```text
           ┌─────────────────┐
           │   User Voice    │
           └────────┬────────┘
                    ↓
           ┌─────────────────┐
           │ Audio Processing│
           └────────┬────────┘
                    ↓
           ┌─────────────────┐
           │  LLM / Inference│
           └────────┬────────┘
                    ↓
           ┌─────────────────┐
           │ Intent Routing  │
           └────────┬────────┘
                    ↓
           ┌─────────────────┐
           │ Action Engine   │
           └────────┬────────┘
                    ↓
       ┌────────────┼────────────┐
       ↓            ↓            ↓
   Browser       System       Media
 Automation      Actions      Control
```

The separation between inference, routing, and execution allows individual components to evolve without requiring the entire assistant to be rewritten.

---

# 📁 Core Components

| File                  | Responsibility                                                  |
| --------------------- | --------------------------------------------------------------- |
| `main.py`             | Main application loop, wake-word detection, and audio pipeline  |
| `engine_server.py`    | Background server, socket orchestration, and process management |
| `engine_llm.py`       | LLM communication and structured JSON intent parsing            |
| `engine_actions.py`   | Executes browser, system, media, and other actions              |
| `processedCommand.py` | Connects interpreted commands with execution logic              |
| `requirements.txt`    | Defines the Python dependencies required by I.R.I.S.            |

---

# 🚀 Getting Started

The complete setup process can be summarized as:

```bash
git clone https://github.com/Night-fury001/IRIS-Hybrid-Agent.git
cd IRIS-Hybrid-Agent
python -m venv .venv
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate
python -m pip install -r requirements.txt
python main.py
```

### macOS / Linux

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

---

# 🧠 Design Philosophy

I.R.I.S. is designed around a few core principles:

### 🔹 Modular

Each major responsibility is separated into its own engine or processing layer.

### 🔹 Hybrid

The system can work with local and cloud-based inference depending on the configured environment.

### 🔹 Extensible

New commands, tools, AI models, and automation capabilities can be added without rebuilding the entire system.

### 🔹 Structured

LLM outputs are handled through structured intent routing rather than relying entirely on unrestricted natural-language responses.

### 🔹 Hardware-Aware

The architecture is designed to take advantage of available local computing resources while still supporting cloud inference when required.

---

# 🛠️ Development

To work on I.R.I.S., clone the repository and create your own development environment:

```bash
git clone https://github.com/Night-fury001/IRIS-Hybrid-Agent.git
cd IRIS-Hybrid-Agent

python -m venv .venv
```

Activate the environment and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Then start the application:

```bash
python main.py
```

---

# 🤝 Contributing

Contributions, improvements, bug fixes, and new ideas are welcome.

If you want to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes locally.
5. Commit your changes.
6. Open a Pull Request.

Example:

```bash
git checkout -b feature/new-capability
git add .
git commit -m "Add new capability"
git push origin feature/new-capability
```

Then create a Pull Request on GitHub.



<div align="center">

**⚡ I.R.I.S. — Integrated Response & Inference Server**

*Modular. Intelligent. Local-first. Extensible.*

</div>
