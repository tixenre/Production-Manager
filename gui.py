from tkinter import *
from slice_and_move import *
from presupuestador import *

root=Tk()
root.title("3PM - 3D Poduction Manager v0.0 alpha1")
root.config(bg='gray')


frame=Frame()
frame.config(bg='white')
frame.config(width='300', height='650')
frame.pack(side='left',fill='y', padx='7',pady='7')


button_slice=Button(frame, text="Slice", command=do_slice)
button_slice.pack()

button_cost=Button(frame, text="Costo",command=cost)
button_cost.pack()

button_price=Button(frame, text="Precio Final")
button_price.pack()


root.mainloop()