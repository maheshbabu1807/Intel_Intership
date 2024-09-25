import json
def analyze_telemetry_data(filename='telemetry_data.json'):
    with open(filename, 'r') as f:
        data = [json.loads(line) for line in f]

    avg_cpu = sum(item['cpu_percent'] for item in data) / len(data)
    avg_memory = sum(item['memory_percent'] for item in data) / len(data)

    # Check structure of NIC stats
    nic_keys = set(data[0]['nic_stats'].keys())
    avg_nic = {key: sum(item['nic_stats'][key][0] + item['nic_stats'][key][1] for item in data) / len(data) for key in nic_keys}

    avg_tdp = sum(item['tdp'] for item in data if item['tdp'] is not None) / len(data)

    report = {
        'average_cpu_percent': avg_cpu,
        'average_memory_percent': avg_memory,
        'average_nic_usage': avg_nic,
        'average_tdp': avg_tdp
    }

    return report

def generate_report(report_data, output_file='report.txt'):
    with open(output_file, 'w') as f:
        for key, value in report_data.items():
            if isinstance(value, dict):
                f.write(f"{key}:\n")
                for subkey, subvalue in value.items():
                    f.write(f"  {subkey}: {subvalue}\n")
            else:
                f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    report_data = analyze_telemetry_data()
    generate_report(report_data)