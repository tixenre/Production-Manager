from tkinter import *
from tkinter import Button, filedialog
from pathlib import Path
import os
import pandas as pd
import numpy as np


import slice
import gcode_parser
import project_path as pp


root=Tk()
root.title("3PM - 3D Poduction Manager v0.0")
root.config(bg='gray')





#Slice .3mf in a folder
def path_3mf():
    files= filedialog.askopenfilenames(title="Select .3mf",
                                        filetypes=[(".3mf Files","*.3mf")],
                                        multiple=True,
                                        initialdir= pp.folder_3mf)
    for f in files:
        p= Path(f)
        slice.do_slice(p)

#Parce gcodes in a folder
def path_gcode():
    filename= filedialog.askopenfilenames(title="Select .gcode",
                                        filetypes=[(".gcode Files","*.gcode")],
                                        multiple=True,
                                        initialdir= pp.folder_gcode)
    for f in filename:
        p= Path(f)
        gcode_parser.parser(p,delete_gcode=True)

#Join csv to a data base.
def join_df():
    files= filedialog.askopenfilenames(title="Select .csv",
                                        filetypes=[(".csv Files","*.csv")],
                                        initialdir= pp.folder_csv)

    combined_csv = pd.concat([pd.read_csv(f) for f in files])
    # for f in files:
    #     os.remove(f)
    combined_csv.replace(r'^\s*$', np.nan, regex=True)
    combined_csv.to_csv("db/db2.csv", index=False)
    
# Slice, parce and join data base.
def get_info():
    path_3mf()
    for f in os.listdir(pp.folder_gcode):
        gcode_parser.parser(f,delete_gcode=True)


def ss():
    path_3mf()
    files= filedialog.askopenfilenames(title="Select .3mf",
                                        filetypes=[(".3mf Files","*.3mf")],
                                        multiple=True,
                                        initialdir= pp.folder_3mf)
    for f in files:
        p= Path(f)
        slice.do_slice(p)
        gcode_parser.parser(f,delete_gcode=True)

#Botones
button_3mf_select= Button(root,text="Slice .3mf",command=path_3mf).pack()
button_get_info= Button(root,text="Parce .gcode",command=path_gcode).pack()
button_get_info= Button(root,text="Join .csv",command=join_df).pack()
button_get_info= Button(root,text="Get Info",command=get_info).pack()



root.mainloop()