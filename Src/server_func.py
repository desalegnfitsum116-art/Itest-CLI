import platform
import subprocess
import time
import json_func as data

def ping_server() -> bool:
    host = data.load_data().get("server_host")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0

def wait_for_server(interval: int = 3):
    host = data.load_data().get("server_host")
    print(f"Waiting for {host} to respond...")
    while True:
        if ping_server():
            print(f"Connection established! {host} is online.")
            break
        else:
            print(f"No response yet. Retrying in {interval} seconds...")
            time.sleep(interval)

def Set (var, val):
    var = var.lower()
    val = f"https://{val}" if var == "server_host" and not val.startswith("http") else val
    if var in data.load_data():
        data.save_data({**data.load_data(), var: val})
        return f"{var} set to {val}."
    else:
        return f"Variable {var} not found."

def Get(var):
    var = var.lower()
    if var in data.load_data():
        return data.load_data().get(var)
    else:
        return f"Variable {var} not found."