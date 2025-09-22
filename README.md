# PDF-Printer

PDF-Printer is a simple utility to convert structured data from an Excel file (`.xls`) into a formatted PDF report.

## Features

-   Reads data from an Excel file.
-   Processes and cleans the data.
-   Generates a PDF report with a custom header, a table of data, and a summary section.
-   Simple graphical user interface to select the input file.
-   Cross-platform (works on macOS, Windows, and Linux).

## Requirements

-   Python 3.9 or newer.

## Local Development

To set up the project for local development, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd pdf-print
    ```

2.  **Create and activate a virtual environment:**
    -   **macOS / Linux:**
        ```bash
        python3 -m venv env
        source env/bin/activate
        ```
    -   **Windows:**
        ```bash
        python -m venv env
        .\env\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application in development mode:**
    ```bash
    python gui.py
    ```
    This will start the application directly using the Python interpreter.

## Building the Application

To build a standalone executable for your operating system, you will need to have PyInstaller installed.

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```

2.  **Build the executable:**
    Run the following command from the root of the project:
    ```bash
    pyinstaller PDF-Printer.spec
    ```
    This command uses the provided spec file to bundle the application and all its dependencies, including the image asset.

    The bundled application will be located in the `dist` directory.

## Running the Application

After building the application, you can run it from the `dist` directory.

-   **macOS:**
    Open the `.app` bundle:
    ```bash
    open dist/PDF-Printer.app
    ```
    Or double-click on `PDF-Printer.app` in Finder.

-   **Windows:**
    Run the `.exe` file:
    ```bash
    dist\PDF-Printer.exe
    ```
    Or double-click on `PDF-Printer.exe` in the File Explorer.

-   **Linux:**
    Run the executable:
    ```bash
    ./dist/PDF-Printer
    ```

## Logging

The application generates logs that can be useful for debugging.
The log file is located in your home directory:
-   **macOS / Linux:** `~/pdf-printer-logs/app.log`
-   **Windows:** `C:\Users\<YourUsername>\pdf-printer-logs\app.log`
