# Real-Time Threat Detection Pipeline

Real-time network log monitoring with ML-based threat detection (98.92% accuracy).

## Architecture

Log Generator -> Queue -> ML Classifier -> Live Dashboard

## Features

- Real-time processing: Logs processed as they arrive (2 logs/second)
- Queue-based buffering: Handles burst traffic without data loss
- ML-powered detection: 98.92% accuracy Random Forest classifier
- Live dashboard: Updates every 2 seconds with metrics

## How It Works

1. Log Generator simulates network traffic (normal + suspicious)
2. Queue buffers logs for processing
3. ML Classifier (Random Forest + TF-IDF) detects threats
4. Live Dashboard displays real-time results

## Run Locally

### Prerequisites

pip install scikit-learn pandas numpy joblib

### Run the Pipeline

python real_time_threat_pipeline.py

Press Ctrl+C to stop.

## Sample Output

Total Logs: 15 | Suspicious: 5 | Normal: 10
Accuracy: 100.0%

Recent Detections:
  NORMAL | TCP 192.168.1.23:55123 -> 8.8.8.8:53 | conf: 95.2%
  SUSPICIOUS | TCP 192.168.1.45:44321 -> 185.142.53.35:3389 | conf: 98.5%

## Performance Metrics

- Accuracy: 98.92%
- Processing rate: 2 logs/second
- Classification time: ~0.1 sec/log

## Technologies

- Python 3.11
- Scikit-learn (Random Forest, TF-IDF)
- Pandas and NumPy
- Threading and Queue

## License

MIT

## Author

Aikaksh Singh Routela