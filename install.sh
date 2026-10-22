#!/bin/bash

# Configuration variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SCRIPT_PATH="$DIR/Src/main.py"
VENV_PATH="$DIR/.venv"
VENV_PYTHON="$VENV_PATH/bin/python3"
SYMLINK_NAME="/usr/local/bin/Itest"

install_app() {
    echo "Starting installation..."
    
    # 1. Ensure the Python file exists
    if [ ! -f "$SCRIPT_PATH" ]; then
        echo "Error: main.py not found in $DIR"
        exit 1
    fi

    # 2. Make sure file is executable
    chmod +x "$SCRIPT_PATH"

    # 3. Create virtual environment if missing
    if [ ! -d "$VENV_PATH" ]; then
        echo "Creating virtual environment..."
        python3 -m venv "$VENV_PATH"
    fi

    # 4. Install dependencies inside the venv
    echo "Installing required Python packages..."
    "$VENV_PATH/bin/pip" install --upgrade pip
    "$VENV_PATH/bin/pip" install typer rich

    # 5. Inject the absolute venv shebang into main.py
    echo "Configuring shebang line..."
    # Remove existing shebang lines if any exist
    sed -i '1{/^#!/d}' "$SCRIPT_PATH"
    # Insert the new correct absolute venv path shebang at the top
    sed -i "1i #!$VENV_PYTHON" "$SCRIPT_PATH"

    # 6. Create the system symlink
    echo "Creating system shortcut (requires sudo keys)..."
    if [ -L "$SYMLINK_NAME" ] || [ -f "$SYMLINK_NAME" ]; then
        sudo rm "$SYMLINK_NAME"
    fi
    sudo ln -s "$SCRIPT_PATH" "$SYMLINK_NAME"

    echo "Success! You can now run the app globally by typing: wifispeed"
}

uninstall_app() {
    echo "Starting uninstallation..."

    # 1. Remove the global symlink shortcut
    if [ -L "$SYMLINK_NAME" ] || [ -f "$SYMLINK_NAME" ]; then
        echo "Removing system shortcut (requires sudo keys)..."
        sudo rm "$SYMLINK_NAME"
    else
        echo "Shortcut $SYMLINK_NAME not found or already removed."
    fi

    # 2. Clean up virtual environment dependencies
    if [ -d "$VENV_PATH" ]; then
        echo "Removing virtual environment directory..."
        rm -rf "$VENV_PATH"
    fi

    echo "Uninstallation complete."
}

# Process the command line argument parameters
case "$1" in
    install)
        install_app
        ;;
    uninstall)
        uninstall_app
        ;;
    *)
        echo "Usage: $0 {install|uninstall}"
        exit 1
        ;;
esac

