# AutoDefender
An intelligent network intrusion response system built with Snort IDS, Python, and GNS3.

# 🛡️ AutoDefender: Intelligent Intrusion Response System

## 📌 Project Overview
AutoDefender is an automated network security solution designed to detect and autonomously respond to malicious network traffic. Built as a graduation project, it integrates network simulation, intrusion detection, and custom automation scripts to minimize incident response time.

## 🏗️ Architecture & Topology
*<img width="1652" height="1034" alt="Topology" src="https://github.com/user-attachments/assets/cf63db4b-cd55-4fd3-90a3-980868f92b5d" />*
> The enterprise network was designed and simulated using **GNS3** within a **VMware** virtualized environment, featuring distinct zones for internal servers, end-users, and the firewall/IDS perimeter.

## 🛠️ Technologies Used
* **Networking:** GNS3, Cisco IOS (Simulated), TCP/IP protocols.
* **Security:** Snort IDS, Firewall (iptables/UFW), Traffic Analysis.
* **OS & Virtualization:** Ubuntu Linux, Kali Linux, VMware.
* **Automation:** Python (Custom active-response scripts).

## ⚙️ How It Works
1. **Traffic Monitoring:** Snort IDS is configured on an Ubuntu server to analyze incoming network packets in real-time.
2. **Threat Detection:** Custom Snort rules trigger alerts upon identifying malicious signatures (e.g., DoS attempts, port scans).
3. **Automated Response:** A Python script continuously parses Snort logs. Once a critical threat is detected, it automatically executes commands to update firewall rules, blocking the attacker's IP address dynamically.

🎥 System in Action (Demo)

https://drive.google.com/file/d/15a5QilhPRNQcf25GqksWPqUMT7Se11fM/view?usp=sharing

## 📁 Repository Structure
* `/scripts` - Python automation and active-response scripts.
* `/configs` - Custom Snort rules (.rules) and Router/Switch configurations (.cfg).
* `/topology` - GNS3 network design files and project screenshots.

## 🚀 Key Takeaways
This project bridges the gap between network administration and cybersecurity, demonstrating hands-on skills in deploying virtual environments, analyzing network packets, and writing security automation code.
