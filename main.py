#!/home/fitsum/Desktop/Projects/WifiSpeedTest/.venv/bin/python3

import time
import urllib.request
import typer
from rich.progress import Progress, TextColumn, BarColumn, DownloadColumn, TransferSpeedColumn
import server_func

app = typer.Typer()


def measure_download_speed() -> float:
    url = "https://cloudflare.com"
    
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
def main():
    server_func.wait_for_server("google.com", interval=2)
    print()
    
    actual_speed = measure_download_speed()
    
    if actual_speed > 0:
        typer.secho(f"\nInternet speed: {actual_speed} Mbps.", fg=typer.colors.GREEN, bold=True)
    else:
        typer.secho("\nCould not calculate speed.", fg=typer.colors.RED)

@app.command()
def help():
    print("This is a live network CLI tool that validates status and dynamically evaluates download speeds.")

if __name__ == "__main__":
    app()

