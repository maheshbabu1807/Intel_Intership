import psutil
import time
import sys

def generate_load(duration=60, load_percent=50):
    end_time = time.time() + duration
    while time.time() < end_time:
        if psutil.cpu_percent(interval=1) < load_percent:
            for _ in range(10000): pass

if __name__ == "__main__":
    load_percent = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    generate_load(duration=60, load_percent=load_percent)