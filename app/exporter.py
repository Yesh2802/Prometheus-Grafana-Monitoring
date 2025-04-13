from prometheus_client import start_http_server, Gauge
import random
import time

# Define a custom metric
CPU_TEMP = Gauge('custom_cpu_temp_celsius', 'Simulated CPU temperature')

def simulate_metrics():
    while True:
        CPU_TEMP.set(random.uniform(50.0, 90.0))
        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    simulate_metrics()
