# WifiSpeedTest CLI

A lightweight, zero-bloat command-line interface tool to test your internet stability and measure download speeds right from your terminal. Built using Python, native networking libraries, and optimized with shell automation scripts.

---

## Features
* **Status Checking**: Validates your internet connection via low-level server pings before testing bandwidth metrics.
* **Connection Resilience**: Automatically pauses and retries connection attempts if the target host drops offline.
* **Visual Progress Bars**: Renders real-time transmission graphs, packet download summaries, and transfer speed evaluations natively inside the terminal screen.
* **Single-Command Setup**: Minimal execution overhead paired with an automated shell utility to link the script natively into your system executable path variables.

---

## Installation

You do not need to manually manage Python virtual environments or configure directory path links. Everything is handled securely via the automated bash deployment workflow script.

1. Clone or navigate to your local working package directory:
   ```bash
   cd ~/Desktop/Projects/WifiSpeedTest
   ```

2. Mark the deployment automation shell routine as runnable:
   ```bash
   chmod +x install.sh
   ```

3. Initialize the deployment process:
   ```bash
   ./install.sh install
   ```
   *(Note: The process will safely prompt for local system credentials to configure global symbolic links under your system paths).*

---

## Usage

Once installed successfully, open a fresh terminal instance in any directory path on your system profile and run the utility directly via the global runtime label:

### Main Command
To execute connection status verifications and calculate throughput bandwidth performance:
```bash
Itest test
```

### Help Information
To view details regarding operational rules or manual parameter handling:
```bash
Itest help
```

---

## Uninstallation

To clean up all local configuration shortcuts, wipe virtual dependencies, and purge executable mappings from your system path directories, execute the uninstallation profile argument:

```bash
./install.sh uninstall
```
