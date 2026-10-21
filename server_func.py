import platform
import subprocess
import time

def ping_server(host: str) -> bool:
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0

def wait_for_server(host: str, interval: int = 3):
    print(f"Waiting for {host} to respond...")
    while True:
        if ping_server(host):
            print(f"Connection established! {host} is online.")
            break
        else:
            print(f"No response yet. Retrying in {interval} seconds...")
            time.sleep(interval)
