
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from script import main
from config import output_path, input_dir

def openFile():
    filepath = filedialog.askopenfilename(
        initialdir=input_dir,
        title="Open file okay?",
        filetypes= (
            ("Excel files",".xls"),
            ("All files", ".*"),
        )
    )
	
    if filepath:
        main(filepath)
		
	# need to write a function to open the current pdf file
        subprocess.call(["xdg-open", output_path])


window = Tk(className="Parsing and Printing App")
window.geometry("500x500")
window['background'] = '#7da87f'
button = Button(text="Open", command=openFile, height=10, width=30, fg="purple")
button.pack()
window.mainloop()
