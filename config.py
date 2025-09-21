import os

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