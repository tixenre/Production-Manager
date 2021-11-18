import tkinter as tk
from tkinter import ttk

import sqlite3


class Gui:

    # db_name = 'database.sqlite'

    def __init__(self, window):

        self.window = window
        self.window.title('Production Manager v0.3 beta1')
        self.window.geometry('1200x650')

    # Frame Files
        frame_info = tk.LabelFrame(self.window, text="File Info")
        frame_info.pack()

    # Frame Table
        frame_files = tk.LabelFrame(self.window, text="Files")
        frame_files.pack(fill=tk.X)



        # Name Input
        self.name_var= tk.StringVar()
        tk.Label(frame_info, text='Name: ').grid(row=1, column=0)
        self.name = tk.Entry(frame_info, textvariable=self.name_var)
        self.name.focus()
        self.name.grid(row=1, column=1)

        # Size Input
        self.size_var= tk.IntVar()
        tk.Label(frame_info, text='Size (mm): ').grid(row=2, column=0)
        self.size = tk.Entry(frame_info, textvariable=self.size_var)
        self.size.grid(row=2, column=1)

        # Filament Input
        self.filament_var = tk.StringVar()
        filaments_lis = {'PLA', 'PETg', 'ABS', 'Flex'}
        tk.Label(frame_info, text='Filament: ').grid(row=3, column=0)
        self.filament = tk.OptionMenu(
            frame_info, self.filament_var, *filaments_lis)
        self.filament.grid(row=3, column=1)
        
        # Gr Input
        self.gr_var= tk.IntVar()
        tk.Label(frame_info, text='Gr: ').grid(row=4, column=0)
        self.gr = tk.Entry(frame_info,textvariable=self.gr_var)
        self.gr.grid(row=4, column=1)

        # Time input
        self.time_var= tk.IntVar()
        tk.Label(frame_info, text='Time (min): ').grid(row=5, column=0)
        self.time = tk.Entry(frame_info,textvariable=self.time_var)
        self.time.grid(row=5, column=1)

    #     # Cost
        tk.Label(frame_info, text='Cost: ').grid(row=6, column=0)
        self.cost = tk.Label(frame_info, text='')
        self.cost.grid(row=6, column=1)

        # Price
        tk.Label(frame_info, text='Price',).grid(row=7, column=0)
        self.price = tk.Label(frame_info, text='')
        self.price.grid(row=7, column=1)

        # Presupuesto Button
        ttk.Button(frame_info, text='Presupuestar', command="self.presupuestar").grid(
            row=8, columnspan=2, sticky=tk.W)
        ttk.Button(frame_info, text='Add', command="self.add_file").grid(
            row=8, columnspan=2, sticky=tk.E)

        # Output Messages
        self.message = tk.Label(frame_info, text='')
        self.message.grid(row=9, columnspan=2, sticky=tk.W + tk.E)

    #     # -------------------------Table

        # Table
        self.tree = ttk.Treeview(frame_files, columns=(
            'name', 'size', 'kind', 'gr', 'time', 'cost', 'price'))
        self.tree.pack(side=tk.TOP,fill=tk.X)
        self.tree.column('#0', width=30, stretch=tk.NO)
        self.tree.heading('#0', text='ID', anchor=tk.W)
        self.tree.column('name', width=75, minwidth=25)
        self.tree.heading('name', text='Name', anchor=tk.W)
        self.tree.column('size', width=75, minwidth=25)
        self.tree.heading('size', text='Size (mm)', anchor=tk.W)
        self.tree.column('kind', width=75, minwidth=25)
        self.tree.heading('kind', text='Kind', anchor=tk.W)
        self.tree.column('gr', width=75, minwidth=25)
        self.tree.heading('gr', text='gr', anchor=tk.W)
        self.tree.column('time', width=75, minwidth=25)
        self.tree.heading('time', text='Minutes', anchor=tk.W)
        self.tree.column('cost', width=75, minwidth=25)
        self.tree.heading('cost', text='Cost', anchor=tk.W)
        self.tree.column('price', width=75, minwidth=25)
        self.tree.heading('price', text='Price', anchor=tk.W)

        # Table Button
        # ttk.Button(frame_files, text='Read', command=self.read_file).pack(
        #     fill=tk.X, side=tk.LEFT)
        # ttk.Button(frame_files, text='Update', command=self.add_update).pack(
        #     fill=tk.X, side=tk.LEFT)
        # ttk.Button(frame_files, text='Presupuestar',
        #            command=self.presupuestar).pack(fill=tk.X, side=tk.LEFT)
        # ttk.Button(frame_files, text='Delete', command=self.delete_file).pack(
            # fill=tk.X, side=tk.LEFT)

    #     self.get_files()
    # # Coneccion Base de Datos

    # def run_query(self, query, parameters=()):
    #     with sqlite3.connect(self.db_name) as conn:
    #         cursor = conn.cursor()
    #         result = cursor.execute(query, parameters)
    #         conn.commit()
    #     return result

    # def get_files(self):
    #     # cleaning table
    #     records = self.tree.get_children()
    #     for element in records:
    #         self.tree.delete(element)
    #     # quering data
    #     query = 'SELECT * FROM files_db ORDER BY name ASC'
    #     db_rows = self.run_query(query)
    #     # filling data
    #     for row in db_rows:
    #         self.tree.insert('', 0, text=row[0], values=(
    #             row[1], row[2], row[3], row[4], row[5],row[6],row[7]))

    # def presupuestar(self):
    #     if len(self.gr.get()) != 0 and len(self.time.get()) != 0:
    #         gr = float(self.gr.get())
    #         time = float(self.time.get())
    #         cost = gr + time
    #         self.cost['text'] = cost
    #         self.price['text'] = cost*2
    #         return print(cost)
    #     else:
    #         print('Gr and Time must be fill')

    # def add_file(self):
    #     if len(self.name.get()) != 0:
    #         self.presupuestar()
    #         query = 'INSERT INTO files_db VALUES(NULL,?,?,?,?,?,?,?)'
    #         parameters = (self.name.get(), self.size.get(), self.filament_var.get(
    #         ), self.gr.get(), self.time.get(), self.cost['text'], self.price['text'])
    #         self.run_query(query, parameters)
    #         self.message['text'] = f'{self.name.get()} saved'
    #     else:
    #         self.message['text'] = 'Name, gr and time are required'
    #     self.get_files()

    # def delete_file(self):
    #     self.message['text'] = ''
    #     try:
    #         self.tree.item(self.tree.selection())['values'][0]
    #     except IndexError:
    #         self.message['text'] = "Select a File"
    #         return
    #     self.message['text'] = ''
    #     name = self.tree.item(self.tree.selection())['values'][0]
    #     query = 'DELETE FROM files_db WHERE name = ?'
    #     self.run_query(query, (name,))
    #     self.message['text'] = f'File {name} has been deleted'
    #     self.get_files()

    # def read_file(self):
    #     try:
    #         self.tree.item(self.tree.selection())['values'][0]
    #     except IndexError:
    #         self.message['text'] = "Select a File"
    #         return
    #     query = 'SELECT * FROM files_db  WHERE name = ?'
    #     name = self.tree.item(self.tree.selection())['values'][0]
    #     with sqlite3.connect(self.db_name) as conn:
    #         cursor = conn.cursor()
    #         cursor.execute(query,(name,))
    #         files=cursor.fetchall()
    #         for file in files:
    #             self.name_var.set(file[1])
    #             self.size_var.set(file[2])
    #             self.filament_var.set(file[3])
    #             self.gr_var.set(file[4])
    #             self.time_var.set(file[5])
    #     self.message['text'] = f'{self.name.get()} Read'

    # def add_update(self):
    #     if len(self.name.get()) != 0:
    #         self.presupuestar()
    #         query = 'UPDATE files_db SET name = ?, size = ?, filament_kind = ?, gr = ?, minutes = ?, cost = ?, price = ?'
    #         parameters = (self.name.get(), self.size.get(), self.filament_var.get(
    #         ), self.gr.get(), self.time.get(), self.cost['text'], self.price['text'])
    #         self.run_query(query, parameters)
    #         self.message['text'] = f'{self.name.get()} saved'
    #     else:
    #         self.message['text'] = 'Name, gr and time are required'
    #     self.get_files()    
        

if __name__ == "__main__":

    window = tk.Tk()
    aplicacion = Gui(window)

    window.mainloop()
