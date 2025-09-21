#!/usr/bin/env python3
import sys
import subprocess
import os

# --- Configuration ---
# The main script of your application
SCRIPT_TO_BUNDLE = "gui.py"

# The desired name for the final executable
APP_NAME = "PDF-Printer"
# -------------------

def build():
    """
    Detects the OS and runs PyInstaller with the correct configuration.
    """
    # 1. Detect Operating System and set the output name
    if sys.platform == "win32":
        print("Detected Windows OS.")
        # On Windows, executables typically end with .exe
        output_name = f"{APP_NAME}.exe"
        command_options = ["--windowed"] # Hides the console window for GUI apps
    elif sys.platform.startswith("linux"):
        print("Detected Linux OS.")
        # On Linux, executables usually have no extension
        output_name = APP_NAME
        command_options = []
    elif sys.platform == "darwin":
        print("Detected macOS.")
        # macOS apps can be run from a bare executable
        output_name = APP_NAME
        command_options = ["--windowed"]
    else:
        print(f"Unsupported OS: {sys.platform}. This script only supports Windows, Linux, and macOS.")
        sys.exit(1)

    # 2. Check if the script to bundle exists
    if not os.path.exists(SCRIPT_TO_BUNDLE):
        print(f"Error: The entry script '{SCRIPT_TO_BUNDLE}' was not found.")
        print("Please make sure you are in the correct directory and the file exists.")
        sys.exit(1)

    # 3. Construct the PyInstaller command
    # Using --onefile to create a single executable
    # Using --clean to remove temporary files before the build
    command = [
        "pyinstaller",
        "--onefile",
        "--clean",
        "--name", output_name,
        *command_options,
        SCRIPT_TO_BUNDLE
    ]

    print("\nRunning PyInstaller...")
    print(f"Command: {' '.join(command)}")
    print("This may take a few minutes.\n")

    # 4. Run the command
    try:
        subprocess.run(command, check=True)
        print(f"\nSuccessfully created executable: dist/{output_name}")
        print("You can find it in the 'dist' folder.")
    except FileNotFoundError:
        print("Error: 'pyinstaller' command not found.")
        print("Please make sure PyInstaller is installed in your Python environment:")
        print("pip install pyinstaller")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("\n--- PyInstaller failed. See the output above for details. ---")
        sys.exit(1)

if __name__ == "__main__":
    build()
