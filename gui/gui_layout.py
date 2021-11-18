import tkinter as tk
from tkinter import Frame, ttk
from tkinter import filedialog
from pathlib import Path

import sys
sys.path.append(r'C:\Users\marti\Documents\GitHub\Production-Manager')

import slicer
import parse
import file_check

import gui_style as gs


class Gui:

    def __init__(self, window):

        self.window = window
        self.window.title('Production Manager v0.1')
        self.window.geometry(gs.windows_size)

        #Creates the tabs notebook
        my_notebook = ttk.Notebook(self.window)
        my_notebook.pack(fill = "both",pady= (gs.pady,gs.pady),padx= (gs.padx,gs.padx))


        ##########################  TAB 1: SLICE AND PARCE
        #Create frames tab
        frame_tab1 = Frame(my_notebook,width= 800, height= 600, background= gs.background_color)
        frame_tab1.pack(fill = "both",expand= 1)
        my_notebook.add(frame_tab1,text= "Slice and Parce")

        # Frame Actions
        frame_actions = tk.LabelFrame(frame_tab1,background= gs.background_color)
        frame_actions.pack(fill= tk.X)

        button_select_file = ttk.Button(frame_actions, text = "Select File",command = self.browse_file_button) 

        button_print_profile = ttk.Button(frame_actions, text = "Print Profile")
        button_filament_profile = ttk.Button(frame_actions, text = "Filament")
        button_printer_profile = ttk.Button(frame_actions, text = "Printer")

        button_slice = ttk.Button(frame_actions, text = "Slice .3mf", command = self.slice_button)
        button_parce = ttk.Button(frame_actions, text = "Parce .gcode", command = self.parse_button)

        button_select_file.pack(side=tk.LEFT, ipadx = 1, ipady = 1, pady= (7,7),padx = (7,0))

        button_print_profile.pack(side=tk.LEFT, ipadx = 1, ipady = 1, pady= (7,7),padx = (40,0))
        button_filament_profile.pack(side=tk.LEFT, ipadx = 1, ipady = 1, pady= (7,7))
        button_printer_profile.pack(side=tk.LEFT, ipadx = 1, ipady = 1, pady= (7,7))

        button_parce.pack(side=tk.RIGHT, ipadx = 10, ipady = 1, pady= (7,7), padx = (0,5))
        button_slice.pack(side=tk.RIGHT, ipadx = 10, ipady = 1, pady= (7,7))




        # Frame Table
        frame_table= tk.LabelFrame(frame_tab1, text="File Info", background= gs.background_color)
        frame_table.pack(fill=tk.X)

        # Table

        column_names = ('name', 'time', 'gr','size','kind', 'cost', 'price')

        self.tree = ttk.Treeview(frame_table, columns = column_names)
        self.tree.pack(fill=tk.X, padx = 5)
        self.tree.column('#0', width=30, stretch=tk.YES)
        self.tree.heading('#0', text='ID', anchor=tk.W)

        self.tree.column(column_names[0], width=75, minwidth=35)
        self.tree.heading(column_names[0], text=column_names[0].capitalize(), anchor=tk.W)
        
        self.tree.column(column_names[1], width=75, minwidth=35)
        self.tree.heading(column_names[1], text=column_names[0].capitalize(), anchor=tk.W)
        
        self.tree.column(column_names[2], width=75, minwidth=35)
        self.tree.heading(column_names[2], text=column_names[2].capitalize(), anchor=tk.W)
        
        self.tree.column(column_names[3], width=75, minwidth=35)
        self.tree.heading(column_names[3], text=column_names[3].capitalize(), anchor=tk.W)
        
        self.tree.column(column_names[4], width=75, minwidth=35)
        self.tree.heading(column_names[4], text=column_names[4].capitalize(), anchor=tk.W)
        
        self.tree.column(column_names[5], width=75, minwidth=35)
        self.tree.heading(column_names[5], text=column_names[5].capitalize(), anchor=tk.W)
        
        self.tree.column(column_names[6], width=75, minwidth=35)
        self.tree.heading(column_names[6], text=column_names[6].capitalize(), anchor=tk.W)



        ##########################  TAB 2: NAME
        frame_tab2 = Frame(my_notebook,width= 800, height= 600, background= gs.background_color)
        frame_tab2.pack(fill = "both",expand= 1)
        my_notebook.add(frame_tab2,text= "NAME")

    

    def browse_file_button(self):
        filename =filedialog.askopenfilenames(filetypes=(("3mf files","*.3mf"),("gcodefiles","*.gcode"),("All files","*.*")))
        print(filename)
        return filename

    def browse_directory_button(self):
        filename = filedialog.askdirectory()
        print(filename)
        return filename



    def slice_button(self):
        files = self.browse_file_button()
        for i in files:
            if i and file_check.is_3mf(i):
                slicer.do_slice(i)

    def parse_button(self):
        # cleaning table tree
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        #quering data
        folder = Path(self.browse_directory_button())
        for i in folder.iterdir():
            if file_check.is_gcode(i):
                d = parse.parse_gcode(i)
                # filling data
                self.tree.insert('', 0, text="TEST", values=(d['name'],d["time"],d["gr"]))



if __name__ == "__main__":

    window = tk.Tk()
    aplicacion = Gui(window)

    window.mainloop()


