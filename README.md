<h1 align="center">
  <img src="assets/logo.png" width="500">
  <br>
  OxPassive
</h1>

<h4 align="center">
  A passive domain intelligence & recon framework for security researchers
</h4>

<p align="center">
  <img src="https://img.shields.io/badge/status-active%20development-blue">
  <img src="https://img.shields.io/badge/python-3.9%2B-blue">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/recon-passive%20only-orange">
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#output">Output</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="#disclaimer">Disclaimer</a>
</p>

---

## 🚀 What is OxPassive?

**OxPassive** is a **passive reconnaissance framework** designed to extract deep domain intelligence **without touching the target**.

No scans.  
No noise.  
No alerts.

Built for **bug bounty hunters, red teamers, and security researchers** who want stealthy recon before active testing.

---

## ✨ Features

- 🔍 Passive subdomain discovery
- 🌐 DNS enumeration (A, AAAA, MX, NS, TXT)
- 🏢 ASN & hosting intelligence
- 🧠 Technology fingerprinting
- 🎯 Scope & CDN detection
- ⚠️ Risk signals (DNSSEC, domain age, misconfigs)
- 📦 Modular & extensible architecture
- ⚡ Single-command execution
- 🛑 Zero interaction with target infrastructure

---

## 📸 Example Output

```bash
python oxpassive.py -d example.com
