"""
Real-Time Threat Detection Pipeline
==================================
Continuous network log monitoring with ML-based threat detection.
"""

import joblib
import numpy as np
import pandas as pd
import random
import time
import threading
import queue
from datetime import datetime

# ============================================
# LOAD TRAINED MODEL
# ============================================

print("Loading model...")
clf = joblib.load('network_threat_detector.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
print("✅ Model loaded!")

# ============================================
# CREATE QUEUES
# ============================================

log_queue = queue.Queue()      # Holds raw logs
result_queue = queue.Queue()   # Holds classified results
print("✅ Queues created")

# ============================================
# LOG GENERATOR (Simulates network traffic)
# ============================================

malicious_ips = [
    "185.142.53.35", "45.155.205.233", "194.87.237.5",
    "5.188.87.45", "185.130.5.253", "94.102.61.78"
]

normal_external = [
    "8.8.8.8", "8.8.4.4", "1.1.1.1", "142.250.185.46"
]

def generate_log():
    """Generate a single log entry"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    protocol = random.choice(["TCP", "UDP"])
    
    # 30% chance of suspicious activity
    is_suspicious = random.random() < 0.3
    
    if is_suspicious:
        src = f"192.168.1.{random.randint(1, 50)}"
        dst = random.choice(malicious_ips)
        port = random.choice([22, 23, 3389, 445, 1433])
        flag = random.choice(["SYN", "RST"])
    else:
        src = f"192.168.1.{random.randint(1, 50)}"
        dst = random.choice(normal_external)
        port = random.choice([80, 443, 53])
        flag = "ACK"
    
    log = f"{timestamp} {protocol} {src}:{random.randint(1024, 65535)} → {dst}:{port} FLAG: {flag}"
    
    return {
        'timestamp': timestamp,
        'log': log,
        'is_suspicious': is_suspicious
    }

def log_generator():
    """Continuously generate logs and push to queue"""
    count = 0
    while True:
        log_entry = generate_log()
        log_queue.put(log_entry)
        count += 1
        if count % 10 == 0:
            print(f"📊 Generated {count} logs...")
        time.sleep(0.5)

# Start generator in background thread
generator_thread = threading.Thread(target=log_generator, daemon=True)
generator_thread.start()
print("✅ Log generator started (2 logs/second)")

# ============================================
# THREAT DETECTOR
# ============================================

def threat_detector():
    """Consume logs from queue, classify, and push results"""
    while True:
        try:
            # Get log from queue (wait up to 1 second)
            entry = log_queue.get(timeout=1)
            log_text = entry['log']
            actual = entry['is_suspicious']
            
            # Classify
            X_test = vectorizer.transform([log_text])
            prediction = clf.predict(X_test)[0]
            proba = clf.predict_proba(X_test)[0].max()
            
            # Prepare result
            result = {
                'timestamp': entry['timestamp'],
                'log': log_text,
                'actual': actual,
                'prediction': prediction,
                'confidence': float(proba),
                'correct': (actual == (prediction == 1))
            }
            
            # Store result
            result_queue.put(result)
            
            # Display
            status = "🚨 SUSPICIOUS" if prediction == 1 else "✅ NORMAL"
            actual_status = "🚨" if actual else "✅"
            correct_mark = "✓" if result['correct'] else "✗"
            print(f"[{entry['timestamp'][11:19]}] {status} ({proba:.1%}) | Actual: {actual_status} | {correct_mark}")
            
        except queue.Empty:
            pass  # No logs available
        time.sleep(0.1)

# Start detector in background
detector_thread = threading.Thread(target=threat_detector, daemon=True)
detector_thread.start()
print("✅ Threat detector started")

# ============================================
# LIVE DASHBOARD
# ============================================

from IPython.display import clear_output

print("\n🛡️ REAL-TIME THREAT DASHBOARD (Press Ctrl+C to stop)")
print("="*60)

results_list = []

try:
    while True:
        # Get all results from queue
        while not result_queue.empty():
            results_list.append(result_queue.get())
        
        # Keep last 50 results
        results_list = results_list[-50:]
        
        if results_list:
            df = pd.DataFrame(results_list)
            total = len(df)
            suspicious = df['prediction'].sum()
            normal = total - suspicious
            accuracy = df['correct'].mean() * 100
            
            clear_output(wait=True)
            print("🛡️ REAL-TIME THREAT DASHBOARD")
            print("="*60)
            print(f"📊 Total Logs: {total} | 🚨 Suspicious: {suspicious} | ✅ Normal: {normal}")
            print(f"📈 Accuracy: {accuracy:.1f}%\n")
            print("Recent Detections:")
            
            # Show last 10
            for _, row in df.tail(10).sort_values('timestamp', ascending=False).iterrows():
                status = "🚨 SUSPICIOUS" if row['prediction'] == 1 else "✅ NORMAL"
                confidence = row['confidence']
                timestamp = row['timestamp'][11:19]
                print(f"  {status} | {row['log'][:60]}... | conf: {confidence:.1%}")
        else:
            clear_output(wait=True)
            print("🛡️ REAL-TIME THREAT DASHBOARD")
            print("="*60)
            print("Waiting for logs... (generator is running)")
        
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\n\n📊 Dashboard stopped.")
    print(f"Total logs processed: {len(results_list)}")