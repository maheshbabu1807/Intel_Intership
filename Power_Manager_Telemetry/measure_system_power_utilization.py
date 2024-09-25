import subprocess
import threading
import psutil
import time
import json

def get_telemetry_data():
    data = {
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

def start_telemetry_logging(filename='telemetry_data.json'):
    def log():
        log_telemetry_data(filename)
    thread = threading.Thread(target=log)
    thread.daemon = True
    thread.start()

def run_load_simulation(load_percent):
    # Convert load_percent to string to be passed as an argument
    subprocess.run(['docker', 'run', '--rm', 'load_simulator', str(load_percent)])

def measure_system_power_utilization(load_percent):
    start_telemetry_logging()
    run_load_simulation(load_percent)

if __name__ == "__main__":
    load_percent = 100  # Example load percent
    measure_system_power_utilization(load_percent)