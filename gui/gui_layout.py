
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


class Gui:

    def __init__(self, window):

        self.window = window
        self.window.title('Production Manager v0.1')
        # self.window.geometry(gs.windows_size)

        #Creates the tabs notebook
        my_notebook = ttk.Notebook(self.window)
        my_notebook.pack(fill = "both",pady= (gs.pady,gs.pady),padx= (gs.padx,gs.padx))


        ##########################  TAB 1: SLICE AND PARCE
        #Create frames tab
        frame_tab1 = Frame(my_notebook,width= 800, height= 600, background= gs.background_color)
        frame_tab1.pack(fill = "both",expand= True)
        my_notebook.add(frame_tab1,text= "Slice and Parce")

        # Frame Actions
        frame_actions = tk.LabelFrame(frame_tab1,background= gs.background_color)
        frame_actions.pack(fill= tk.X)

        button_select_file = ttk.Button(frame_actions, text = "Select File",command = self.browse_files) 

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



        # Filament Input
        filaments_list = self.get_print_settings()
        def comboclick(event):
            show = filaments_list.get(combo.get())
            print(show)
            # Label(root, text= show).pack()

        combo = ttk.Combobox(frame_actions, values  = list(filaments_list.keys()))
        combo.current(0)
        combo.bind("<<ComboboxSelected>>", comboclick)
        combo.pack()

        # Frame Table
        frame_table= tk.LabelFrame(frame_tab1, text="File Info", background= gs.background_color)
        frame_table.pack(fill = tk.BOTH, expand= True)

        # Table

        column_names = ('name',
                        'time',
                        'gr',
                        'kind',
                        "instances",
                        'size',
                        "printer",
                        'cost',
                        'price')

        # scrollbars
        self.tree = ttk.Treeview(frame_table, columns = column_names, style="tree_style.Treeview")
        self.tree.pack(fill=tk.BOTH, padx = (5,0), expand= True, side= tk.LEFT)
        style = ttk.Style()
        style.configure("tree_style.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("tree_style.Treeview.Heading", font=('Calibri', 11,'bold')) # Modify the font of the headings
        # style.layout("tree_style.Treeview", [('tree_style.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        self.tree.tag_configure('odd', background='#E8E8E8')
        self.tree.tag_configure('even', background='#DFDFDF')


        # add a scrollbar
        scrollbar = ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(fill=tk.Y, padx = (0,5), side = tk.RIGHT)


        self.tree.column('#0', width=30, stretch=tk.YES)
        self.tree.heading('#0', text='ID', anchor=tk.W)
        for i in column_names:
            self.tree.column(i, width=75, minwidth=35)
            self.tree.heading(i, text= i.capitalize(), anchor=tk.W)



        #Frame Save 
        frame_save= tk.LabelFrame(frame_tab1, text="Save")
        frame_save.configure(background= gs.background_color)
        frame_save.pack(fill = tk.X, side = tk.BOTTOM)

        button_save = ttk.Button(frame_save, text = "Save to database") 
        button_save.pack(side=tk.LEFT, ipadx = 1, ipady = 1, pady= (7,7),padx = (7,0))

        button_clear = ttk.Button(frame_save, text = "Clear Table", command= self.clear_table) 
        button_clear.pack(side=tk.LEFT, ipadx = 1, ipady = 1, pady= (7,7),padx = (7,0))



        ##########################  TAB 2: NAME
        frame_tab2 = Frame(my_notebook,width= 800, height= 600, background= gs.background_color)
        frame_tab2.pack(fill = "both",expand= 1)
        my_notebook.add(frame_tab2,text= "NAME")

    

    def browse_files(self, suffix = ".3mf"):
        filename =filedialog.askopenfilenames(filetypes=((f"{suffix} files",f"*{suffix}"),("All files","*.*")))
        print(filename)
        return filename

    def browse_directory(self):
        filename = filedialog.askdirectory()
        # print(filename)
        return filename



    def slice_button(self):
        files = self.browse_files(suffix= ".3mf")
        for i in files:
            if i and file_check.is_3mf(i):
                slicer.do_slice(i)

    def parse_button(self):
        self.clear_table()

        #quering data
        folder = self.browse_files(suffix=".gcode")
        for i in folder:
            if file_check.is_gcode(i):
                d = parse.parse_gcode(i)
                # filling data
                self.tree.insert('', 0, text="TEST", values=(d['name'],d["time_hs"],d["gr"],d["kind"],d["instances"]))
        return d            

    def clear_table(self):
        # cleaning table tree
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

    def get_print_settings(self):
        
        di = {}
        di.update({"default" : pp.print_preset_def.as_posix()})
        for i in pp.prints.iterdir():
            name = Path(i).stem
            path_ = i.as_posix()
            di.update({name:path_})
        print(di)
        return di

if __name__ == "__main__":

    window = tk.Tk()
    aplicacion = Gui(window)

    window.mainloop()


