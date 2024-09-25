import psutil
import time
import json
from datetime import datetime

def get_telemetry_data():
    data = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory_percent': psutil.virtual_memory().percent,
        'nic_stats': psutil.net_io_counters(pernic=True),
        'tdp': psutil.sensors_temperatures().get('coretemp', [])[0].current if hasattr(psutil, 'sensors_temperatures') else None
    }
    return data

def log_telemetry_data(filename='telemetry_data.json'):
    with open(filename, 'a') as f:
        while True:
            data = get_telemetry_data()
            f.write(json.dumps(data) + '\n')
            time.sleep(1)

if __name__ == "__main__":
    log_telemetry_data()