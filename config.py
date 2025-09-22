import os
import platform
import logging
from logging.handlers import RotatingFileHandler

# This is the base directory of the project.
# All other paths are relative to this path.
init_path = os.path.dirname(os.path.abspath(__file__))

# The initial directory for the file dialog.
# You can change this to any absolute path.
# For example: input_dir = "/home/user/documents"
input_dir = init_path

# The path to the image file used in the PDF.
# The default is an image named "image.png" in the project directory.
image_path = os.path.join(init_path, "image.png")

# The directory where the output PDF will be saved.
# The default is the project directory.
output_dir = init_path

# The name of the output PDF file.
output_file = "output.pdf"

# The full path to the output PDF file.
# This is constructed from output_dir and output_file.
output_path = os.path.join(output_dir, output_file)

# The operating system platform.
OS_PLATFORM = platform.system()

def setup_logging():
    log_dir = os.path.join(os.path.expanduser("~"), "pdf-printer-logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, "app.log")

    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s")
    handler.setFormatter(formatter)

    # Add the handler to the root logger
    if not logger.handlers:
        logger.addHandler(handler)
