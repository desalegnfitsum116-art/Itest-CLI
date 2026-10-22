#!/home/fitsum/Desktop/Projects/WifiSpeedTest/.venv/bin/python3

import time
import urllib.request
import typer
from rich.progress import Progress, TextColumn, BarColumn, DownloadColumn, TransferSpeedColumn
import server_func as server_func
import json_func as data

app = typer.Typer()


def measure_download_speed() -> float:
    url = data.load_data().get("server_host")
    
    progress = Progress(
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        DownloadColumn(),
        TransferSpeedColumn(),
    )
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            total_size = int(response.headers.get('content-length', 10000000))
            
            start_time = time.time()
            downloaded = 0
            chunks = []
            
            with progress:
                task = progress.add_task("Testing Internet Connection...", total=total_size)
                
                while True:
                    chunk = response.read(1024 * 64)
                    if not chunk:
                        break
                    chunks.append(chunk)
                    downloaded += len(chunk)
                    progress.update(task, completed=downloaded)
                    
            end_time = time.time()
            
        duration = end_time - start_time
        if duration == 0:
            return 0.0
            
        total_megabits = (downloaded * 8) / 1_000_000
        speed_mbps = total_megabits / duration
        return round(speed_mbps, 2)
        
    except Exception as e:
        typer.secho(f"\nSpeed test failed: {e}", fg=typer.colors.RED)
        return 0.0

@app.command()
def test():
    server_func.wait_for_server(interval=2)
    print()
    
    actual_speed = measure_download_speed()
    
    if actual_speed > 0:
        typer.secho(f"\nInternet speed: {actual_speed} Mbps.", fg=typer.colors.GREEN, bold=True)
    else:
        typer.secho("\nCould not calculate speed.", fg=typer.colors.RED)

@app.command()
def set(var, val):
    result = server_func.Set(var, val)
    typer.secho(result, fg=typer.colors.CYAN)

@app.command()
def ping():
    result = server_func.wait_for_server(interval=2)
    typer.secho(result, fg=typer.colors.CYAN)

@app.command()
def list():
    for var, val in data.load_data().items():
        typer.secho(f"{var}: {val}", fg=typer.colors.YELLOW)

@app.command()
def help():
    print("""
Itest CLI — Lightweight Internet Toolkit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Check connectivity, measure download speeds, and
troubleshoot internet connection reliability.

USAGE
    Itest <command> [options]

COMMANDS
    test                         Test connectivity and download speed
    set <variable> <value>       Update a configuration variable
    help                         Display this help message

EXAMPLES
    Itest test
    Itest set server_host cloudflare.com
    Itest help

CONFIGURATION
    server_host                  Target host (default: google.com)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lightweight. Simple. Built for the terminal.
""")

if __name__ == "__main__":
    app()

