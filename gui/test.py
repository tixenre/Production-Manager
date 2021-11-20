import tkinter as tk
from tkinter import Frame, ttk
from tkinter import filedialog
from pathlib import Path


import sys
sys.path.append(Path.cwd().absolute().as_posix())
import slicer
import parse
import file_check
import project_path as pp

import gui_style as gs


root = tk.Tk()

# def selected(event):
#     mylabel = Label(root, text= clicked.get()).pack()
options = pp.print_presets




def make_combo_box(master,values):
    combo = ttk.Combobox(master, values  = list(values.keys()))
    combo.current(0)
    def comboclick(event):
        show = options.get(combo.get())
        tk.Label(master, text= show).pack()
        print(show)
    combo.bind("<<ComboboxSelected>>", comboclick)
    combo.pack()


selected = make_combo_box(root,options)



root.mainloop()







# function to return key for any value
# def get_key(val):
#     for key, value in options.items():
#          if val == value:
#              return key
 
#     return "key doesn't exist"