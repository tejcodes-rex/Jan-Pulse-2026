# Jan-Pulse: The Demographic Nervous System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
[![GitHub](https://img.shields.io/badge/GitHub-View%20Source-181717?logo=github)](https://github.com/tejcodes-rex/Jan-Pulse-2026)

## Overview
Jan-Pulse is an AI-driven policy targeting system designed to identify 'Digital Dark Zones' and 'Ghost Children' using Aadhaar authentication telemetry.

## Key Findings
We have triangulated three critical policy signals:
1. **Ghost Children:** Identifying school dropouts via biometric update lags.
2. **Workforce Velocity:** Tracking labor migration corridors using demographic update frequency.
3. **Digital Dark Zones:** Pinpointing areas with high adult population but zero digital footprint (financial exclusion).

## Project Structure
```
├── src/                # Core Analytics Engine
│   ├── main.py         # Entry Point
│   └── analytics_engine.py
├── data/               # Certified Master Datasets
├── assets/             # High-Resolution Visualizations
└── docs/               # Methodology and Policy Matrices
```

## Installation
```bash
pip install -r requirements.txt
```

## Usage
To run the analytics engine:
```bash
python src/main.py
```

## Methodology
Our approach utilizes a "Map-Reduce" architecture to process state-distributed CSV streams, preserving Pin-Code level granularity without memory sampling errors. See `docs/` for the complete methodologies.

---
*Built for the UIDAI Data Hackathon 2026.*
