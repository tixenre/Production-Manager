import tkinter as tk
from tkinter import Label, ttk

root = tk.Tk()

# def selected(event):
#     mylabel = Label(root, text= clicked.get()).pack()
options = {"a": 1,"b": 2}

def comboclick(event):
    show = options.get(combo.get())
    print(show)
    # Label(root, text= show).pack()

combo = ttk.Combobox(root, values  = list(options.keys()))
combo.current(0)
combo.bind("<<ComboboxSelected>>", comboclick)
combo.pack()

root.mainloop()


# function to return key for any value
# def get_key(val):
#     for key, value in options.items():
#          if val == value:
#              return key
 
#     return "key doesn't exist"