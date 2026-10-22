# Itest CLI

**A lightweight, zero-bloat internet toolkit for your terminal.**

Itest CLI is a Python-powered command-line toolkit for checking internet connectivity, measuring download performance, and troubleshooting connection reliability. Designed for simplicity and minimal overhead, Itest brings essential internet diagnostics into one convenient terminal interface.

Whether you're checking your connection, investigating unstable networking, or measuring download speeds, Itest gives you the tools to understand your internet connection without opening a browser.

## Features

- **Connectivity Checks** — Verify that your system can reach a configured server before running network tests.
- **Download Speed Testing** — Measure download throughput and monitor transfer progress directly in your terminal.
- **Connection Resilience** — Pause and retry connection attempts when a target host becomes unavailable, where supported.
- **Terminal-Based Feedback** — View progress indicators, transfer summaries, and speed measurements without a graphical interface.
- **Configurable Settings** — Change supported configuration variables, such as the server used for connectivity checks.
- **Simple Global Access** — Install the command-line utility so it can be launched from any directory.
- **Lightweight by Design** — Built with Python and shell automation, with a focus on keeping the workflow straightforward.

## Installation

Itest includes an installation script that automates setup and command-line integration.

### Prerequisites

- Python 3
- Bash-compatible shell
- Git
- A Linux environment
- Network access for internet diagnostics

### Install from source

**1. Clone the repository**

```bash
git clone https://github.com/desalegnfitsum116-art/Itest-Internet-speed-test.git
cd Itest
```

Alternatively, navigate to your existing project directory:

```bash
cd ~/Desktop/Projects/Itest
```

**2. Make the installer executable**

```bash
chmod +x install.sh
```

**3. Install Itest**

```bash
./install.sh install
```

Follow any prompts displayed by the installer. Depending on how the installer configures system-wide command access, administrative privileges may be required.

**4. Verify the installation**

Open a new terminal and run:

```bash
Itest help
```

If the help information appears, the command is available and ready to use.

## Commands

Itest uses a command-based interface designed to keep common networking tasks accessible and easy to remember.

### 1. Diagnostics

Commands for checking connectivity and measuring internet performance.

| Command | Description |
|---|---|
| `Itest test` | Run the available connectivity and download performance tests. |
| `Itest help` | Display help information and supported commands. |

**Example:**

```bash
Itest test
```

Use this command to check your connection and measure download performance through the configured test workflow.

### 2. Configuration

Commands for adjusting supported settings without modifying the source code.

**Syntax:**

```bash
Itest set <variable> <value>
```

| Argument | Description |
|---|---|
| `<variable>` | The name of a supported configuration variable. |
| `<value>` | The value to assign to that variable. |

**Example — Change the server host:**

```bash
Itest set server_host cloudflare.com
```

**Current configuration**

| Variable | Default value | Purpose |
|---|---|---|
| `server_host` | `google.com` | Host used for the configured server connectivity check. |

Configuration changes and their persistence depend on the installed version of Itest.

### 3. Help and Reference

Display available commands and usage instructions:

```bash
Itest help
```

Use the help command whenever you need to check the supported syntax or discover available options.

### 4. Installation Management

These commands are executed through the installation script rather than the installed `Itest` command.

| Command | Description |
|---|---|
| `./install.sh install` | Install Itest and configure command-line access. |
| `./install.sh uninstall` | Remove the installation and associated command-line integration managed by the installer. |

**Uninstall Itest:**

```bash
./install.sh uninstall
```

Review any prompts before confirming removal, particularly if the installer manages system-wide files.

## Project Structure

A typical Itest installation repository may look like this:

```text
Itest/
├── install.sh       # Installation and removal automation
├── README.md        # Project documentation
└── ...              # Python source and supporting files
```

The exact layout depends on the files included in your repository.

## Vision

Itest aims to become a unified internet toolkit that brings everyday networking utilities together under a single command.

Potential future capabilities include:

- **Network Diagnostics** — More detailed connection checks and failure reporting.
- **Latency Analysis** — Measure response times and monitor connection consistency.
- **Packet Loss Monitoring** — Identify unreliable connections and dropped packets.
- **DNS Utilities** — Inspect DNS resolution and troubleshoot lookup failures.
- **Download Diagnostics** — Compare transfer performance across configurable test endpoints.
- **Connection Monitoring** — Track connection availability over time.
- **IP Information** — Display useful information about public IP addresses and network routing.

These are potential future additions, not necessarily features available in the current release.

## Design Philosophy

Itest follows three principles:

- **Simple** — Commands should be easy to understand and remember.
- **Lightweight** — Keep dependencies and unnecessary complexity to a minimum.
- **Practical** — Focus on useful networking information that can be accessed directly from the terminal.

## Contributing

Contributions, bug reports, feature suggestions, and improvements are welcome.

When proposing a feature, prioritize reliability, clear output, minimal dependencies, and consistency with the existing command structure.

## License

See the repository's license file for licensing terms. If the project does not yet have one, add a `LICENSE` file before specifying redistribution terms.

---

**Itest CLI — Essential internet diagnostics, one command away.**