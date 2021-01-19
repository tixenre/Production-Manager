import tkinter as tk
from tkinter import filedialog

root=tk.Tk()    

ent1=tk.Entry(root)
ent1.grid(row=2,column=2)

def browsefunc():
    filename =filedialog.askopenfilename(filetypes=(("3mf files","*.3mf"),("All files","*.*")))
    ent1.insert(tk.END, filename) # add this

b1=tk.Button(root,text="3mf File",command=browsefunc)
b1.grid(row=2,column=4)

root.mainloop()