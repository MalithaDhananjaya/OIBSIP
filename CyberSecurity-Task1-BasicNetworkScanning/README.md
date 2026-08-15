# Task 1: Basic Network Scanning using Nmap

## 📌 Overview
This project demonstrates basic network reconnaissance using **Nmap** on a target host (`scanme.nmap.org`). The assessment identifies open ports, running services, operating system details, and network routing to map out the target's attack surface.

---

## 🎯 Target Information
| Field         | Value                  |
|---------------|------------------------|
| Target Host   | `scanme.nmap.org`      |
| IP Address    | `45.33.32.156`         |
| Status        | Host is up (0.13s latency) |

---

## 🛠️ Command Executed
\```bash
sudo nmap -A scanme.nmap.org
\```

**Flag breakdown (`-A`):** Enables OS detection, version detection, script scanning, and traceroute.

---

## 🔍 Key Findings & Open Ports

| Port / Protocol | State | Service    | Version / Details                    |
|------------------|-------|------------|----------------------------------------|
| 22/tcp           | Open  | SSH        | OpenSSH 6.6.1p1 Ubuntu                |
| 25/tcp           | Open  | SMTP       | Unknown (EHLO domain error returned)  |
| 80/tcp           | Open  | HTTP       | Apache httpd 2.4.7 (Ubuntu)           |
| 9929/tcp         | Open  | Nping-echo | Nping echo service                    |
| 31337/tcp        | Open  | tcpwrapped | -                                      |

---

## 💻 OS & Infrastructure Details
- **Operating System:** Linux (Kernel 4.19 - 5.15 guess, 92% confidence)
- **Network Distance:** 5 hops

---

## 🕵️ Red Team Analysis & Conclusion
- **Reconnaissance Success:** Successfully discovered active web and SSH services running on older software versions (Apache 2.4.7, OpenSSH 6.6.1p1).
- **Potential Vector:** Older software versions identified during this scan present potential targets for further vulnerability assessment in subsequent testing stages.

---

## ⚠️ Disclaimer
This scan was performed against `scanme.nmap.org`, a host explicitly provided by the Nmap project for legal scanning practice. Only scan hosts you own or have explicit written permission to test.

