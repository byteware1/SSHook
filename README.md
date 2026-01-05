<div align="center">

# 🖥️ SSHook

**Discord-controlled Screenshot Tool (Python · Research Project)**

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Discord](https://img.shields.io/badge/discord.py-2.x-purple)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/status-Educational-orange)

</div>

---

## 📌 Overview

**SSHook** is a Python-based research project demonstrating how a Discord bot can remotely interact with a host machine and return screenshots on command.

The script:
- Connects to a Discord bot
- Automatically creates a dedicated text channel
- Responds to a bot command by capturing a screenshot
- Sends the screenshot directly to Discord

> ⚠️ **This project is for educational and research purposes only.  
Use only on systems you own or have explicit permission to access.**

---

## ✨ Features

- 🤖 Discord bot command control
- 📸 Screenshot capture via `pyautogui`
- 📡 Automatic Discord channel creation
- 🧠 Host-based identification (local IP-based channel name)
- ⚡ Simple, lightweight Python implementation

---

## 🧱 Tech Stack

- **Language:** Python 3
- **Discord API:** discord.py
- **Screenshot:** pyautogui + Pillow
- **Networking:** socket

---

## 📂 How It Works (High-Level)

1. Bot connects to Discord using a token  
2. On startup, it:
   - Detects the local IP
   - Creates (or reuses) a dedicated text channel
3. When the `!shot` command is issued:
   - A screenshot is taken
   - The image is sent to the Discord channel

---

## ⚙️ Setup Guide

### 1️⃣ Install Python

Make sure Python is installed:

👉 https://www.python.org/downloads/

Verify:
```bash
python --version
