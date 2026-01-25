# **Security Incident Artifact Analyzer**

A lightweight DFIR tool for analyzing common incident artifacts such as registry keys, browser history, Sysmon logs, and network traces to support rapid triage and investigation.

---

## Overview

Security Incident Artifact Analyzer is a modular and extensible tool designed to help analysts quickly extract, parse, and interpret digital evidence during incident response.  
It focuses on **speed**, **clarity**, and **practical use cases** commonly encountered in real-world investigations.

---

## Features

- **Registry Analysis**  
  Extracts Run keys, MRU lists, USB artifacts, and persistence indicators.

- **Browser History Parsing**  
  Supports Chrome/Edge/Firefox history, downloads, and session data.

- **Sysmon Log Processing**  
  Identifies suspicious process creation, network events, and file modifications.

- **Network Artifact Inspection**  
  Parses active connections, suspicious IPs, and basic enrichment.

- **Report Generation**  
  Outputs results in JSON or Markdown for easy sharing and documentation.

---

## Project Structure

```
security-incident-artifact-analyzer/
 ├─ parsers/
 │   ├─ registry_parser.py
 │   ├─ browser_history.py
 │   ├─ sysmon_parser.py
 │   └─ network_parser.py
 ├─ core/
 │   ├─ analyzer.py
 │   └─ report.py
 ├─ README.md
 ├─ LICENSE
 └─ requirements.txt
```

---

## Getting Started

### **1. Clone the repository**
```bash
git clone https://github.com/secwexen/security-incident-artifact-analyzer.git
cd security-incident-artifact-analyzer
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## **New CLI Commands for Security Incident Artifact Analyzer**

The analyzer now requires **artifact type flags** instead of a generic `--analyze`. Use one of the following options:

| Flag         | Description                        | Example Input File              |
| ------------ | ---------------------------------- | ------------------------------- |
| `--registry` | Analyze Windows Registry artifacts | `examples/registry.reg`         |
| `--browser`  | Analyze browser history            | `examples/browser_history.json` |
| `--sysmon`   | Analyze Sysmon event logs          | `examples/sysmon.evtx`          |
| `--network`  | Analyze network logs or PCAPs      | `examples/network.pcap`         |

---

## **Usage Examples**

```bash
# Analyze Sysmon logs
python -m core.analyzer --sysmon examples/sysmon.evtx

# Analyze browser history
python -m core.analyzer --browser examples/browser_history.json

# Analyze Windows Registry
python -m core.analyzer --registry examples/registry.reg

# Analyze network logs / PCAP
python -m core.analyzer --network examples/network.pcap
```

---

## Notes

* Only **one artifact type** can be processed per run.
* Make sure the **input file exists** and the path is correct.
* The results will be saved in the **reports/** folder or printed in the console.

---

## Use Cases

- Rapid triage during security incidents  
- SOC/DFIR investigations  
- Malware analysis support  
- Threat hunting  
- Training and lab environments  

---

## License

Apache-2.0 License
