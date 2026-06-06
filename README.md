# 🔍 Real-Time Threat Detection Pipeline

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.9.0-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-2.0+-green.svg)](https://pandas.pydata.org/)
[![ML](https://img.shields.io/badge/ML-Random%20Forest-red.svg)](https://en.wikipedia.org/wiki/Random_forest)

## 📋 Overview

A **real-time network log monitoring system** that detects cyber threats using Machine Learning. The pipeline processes 2 logs/second with **98.92% accuracy**.

## 🔗 Links

- **GitHub**: [real-time-threat-pipeline](https://github.com/Aikaksh-Singh-Routela/real-time-threat-pipeline)

### Key Features

| Feature | Description |
|---------|-------------|
| **⚡ Real-time Processing** | Logs processed as they arrive (2 logs/second) |
| **📦 Queue-based Buffering** | Handles burst traffic without data loss |
| **🎯 ML-powered Detection** | 98.92% accuracy Random Forest classifier |
| **📊 Live Dashboard** | Updates every 2 seconds with metrics |
| **🔄 End-to-End Pipeline** | From log generation to threat detection |

## 🏗️ Architecture
Log Generator → Queue Buffer → ML Classifier → Live Dashboard
↓ ↓ ↓ ↓
Simulates Handles Random Real-time
Network Burst Forest + Metrics
Traffic Traffic TF-IDF Display

text

## 📊 How It Works

| Step | Component | Description |
|------|-----------|-------------|
| 1 | **Log Generator** | Simulates network traffic (normal + suspicious patterns) |
| 2 | **Queue Buffer** | Temporarily stores logs to handle traffic bursts |
| 3 | **ML Classifier** | Random Forest + TF-IDF analyzes each log |
| 4 | **Live Dashboard** | Displays real-time results and metrics every 2 seconds |

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **ML Model** | Random Forest Classifier |
| **Feature Extraction** | TF-IDF Vectorization |
| **Data Processing** | Pandas, NumPy |
| **Model Persistence** | Joblib |
| **Language** | Python 3.11+ |

## 📦 Installation

### Prerequisites

```bash
# Clone repository
git clone https://github.com/Aikaksh-Singh-Routela/real-time-threat-pipeline.git
cd real-time-threat-pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install scikit-learn pandas numpy joblib
Run the Pipeline
bash
python real_time_threat_pipeline.py
📊 Sample Output
text
[LOG GENERATOR] Generating network logs...
[QUEUE] Processing log #1: Normal traffic
[CLASSIFIER] Prediction: Normal (Confidence: 95.2%)
[DASHBOARD] Threat Detected: No | Suspicious Count: 0 | Total: 100

[LOG GENERATOR] Generating suspicious pattern...
[QUEUE] Processing log #42: Multiple failed attempts
[CLASSIFIER] Prediction: THREAT DETECTED (Confidence: 98.9%)
[DASHBOARD] Threat Detected: YES | Suspicious Count: 3 | Total: 200
📈 Performance Metrics
Metric	Value
Accuracy	98.92%
Processing Speed	2 logs/second
Update Frequency	Every 2 seconds
Models Used	Random Forest + TF-IDF
📁 Project Structure
text
real-time-threat-pipeline/
├── real_time_threat_pipeline.py   # Main pipeline script
├── model/                          # Saved ML model
├── logs/                           # Generated log files
└── README.md                       # Documentation
🔧 Configuration
You can modify these parameters in the script:

Parameter	Default	Description
LOG_RATE	2 logs/sec	Log generation speed
QUEUE_SIZE	100	Maximum queue capacity
UPDATE_INTERVAL	2 seconds	Dashboard refresh rate
TEST_SPLIT	0.2	Train/test split ratio
🚀 Future Improvements
Add more threat patterns (SQL injection, XSS, etc.)

Implement real-time alerting (email/SMS)

Add support for live network traffic capture

Create web-based dashboard (Streamlit/FastAPI)

Add model retraining pipeline

🤝 Contributing
Contributions welcome! Feel free to submit issues and pull requests.

📄 License
MIT License

Author: Aikaksh Singh Routela

Built with 🔒, 🐍, and 🤖 by Aikaksh Singh Routela
