
import os
import subprocess
import logging
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from script import main
from config import output_path, input_dir, OS_PLATFORM, setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def openFile():
    logger.info("Opening file dialog.")
    filepath = filedialog.askopenfilename(
        initialdir=input_dir,
        title="Open file okay?",
        filetypes=(
            ("Excel files", ".xls"),
            ("All files", ".*"),
        )
    )

    if filepath:
        try:
            logger.info(f"File selected: {filepath}")
            main(filepath)
            logger.info(f"Successfully created PDF for {filepath}.")

            # need to write a function to open the current pdf file
            if OS_PLATFORM == 'Darwin':
                logger.info(f"Opening PDF file at {output_path} on macOS.")
                subprocess.call(['open', output_path])
            elif OS_PLATFORM == 'Windows':
                logger.info(f"Opening PDF file at {output_path} on Windows.")
                os.startfile(output_path)
            else:
                logger.info(f"Opening PDF file at {output_path} on Linux.")
                subprocess.call(['xdg-open', output_path])
        except Exception as e:
            logger.error(f"An error occurred: {e}", exc_info=True)
    else:
        logger.warning("No file selected.")


window = Tk(className="Parsing and Printing App")
window.geometry("500x500")
window['background'] = '#7da87f'
button = Button(text="Open", command=openFile, height=10, width=30, fg="purple")
button.pack()

logger.info("Starting GUI application.")
window.mainloop()
logger.info("Closing GUI application.")
