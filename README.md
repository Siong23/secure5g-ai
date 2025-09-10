

# 🔐 secure5g-ai

An open-source project for generating realistic, labeled 5G network traffic datasets using a live 5G testbed infrastructure. The goal is to support the research and development of AI/ML-based security mechanisms in next-generation mobile networks.

---

## 📌 Overview

As 5G technology rapidly evolves, its complex architecture and increased attack surface demand smarter, AI-driven security solutions. However, the effectiveness of such solutions heavily depends on the availability of realistic, high-quality datasets.

**secure5g-ai** addresses this gap by:
- Leveraging live 5G testbed to simulate and capture real 5G traffic under benign and malicious conditions.
- Generating, labeling, and curating a publicly reusable 5G security dataset.
- Laying the foundation for future ML/DL-based intrusion detection research.

---

## 🎯 Key Objectives

- 📶 **Testbed-Driven Dataset Collection**: Use a live 5G setup to capture real traffic scenarios (control/user planes).
- 🐍 **Attack Simulation**: Generate labeled traffic by replaying or scripting common 5G-related threats.
- 🗃️ **Dataset Curation**: Format and annotate the data for ML research (CSV, PCAP, NetFlow, etc.).
- 📊 **Preliminary Analysis**: Provide baseline statistics and visualizations for researchers.

---

## 🖼️ System Architecture
```
          +-------------------------------------+
          | 5G Testbed                      |
          | - gNB + Core                        |
          | - 5G UEs (phones, emulators, SDRs)  |
          +-------------------------------------+
                            ↓
             +------------------------------+
             | Traffic Capture & Labeling   |
             | - Wireshark                  |
             | - TCPDump, sFlow exporters   |
             +------------------------------+
                            ↓
         +----------------------------------------+
         | Dataset Preprocessing Pipeline         |
         | - Parsing, Filtering, Normalizing      |
         | - Attack Injection & Labeling Scripts  |
         +-------------------+--------------------+
                             ↓
             +-------------------------------+
             | secure5g-dataset/             |
             | - Labeled flows               |
             | - Metadata (labels, scenario) |
             | - Format: CSV, NetFlow, JSON  |
             +-------------------------------+
```

## Example Workflow
1. Simulate Network Traffic
   - Use UEs to perform common tasks (browsing, video streaming, VoLTE).
2. Inject Attacks
   - Trigger malicious behavior (DoS, malformed packets, spoofing).
3. Capture Packts
   - Use tcpdump or tshark to capture traffic on fronthaul and core interfaces.
4. Label & Export
   - Tag malicious vs. normal flows and export to CSV/NetFlow formats.
5. Preprocess Dataset
   - Run scripts to extract features, clean, and prepare for ML pipelines.

## Security Use Cases
- Anomaly detection model training
- Network behavior modeling for fronthaul/core
- Early-stage testing of ML/NIDS systems
- Traffic classification and signature generation
