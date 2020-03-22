import re
from pathlib import Path

## own libs
from project_path import folder_gcode
from parse import parse_gcode

class Filaments:
    def __init__(self,kind,vendor,spool_cost,density,spool_gr=1000):
        self.kind = "kind"
        self.vendor = "vendor"
        self.spool_cost = float(spool_cost)
        self.density = float(density)
        self.spool_gr = int(spool_gr)
        self.gr_cost = float(spool_cost/spool_gr)
        

pla_grillon3 = Filaments("PLA","Grillon3",1000,1.25,spool_gr=1000)		
petg_grillon3 = Filaments("PETG","Grillon3",1000,1.27,spool_gr=1000)
pla_pal = Filaments("PLA","PrintaLot",960,1.25,spool_gr=1000)
flex_grillon3 = Filaments("Flex","Grillon3",1614,1.25,spool_gr=1000)
abs_grillon3 = Filaments("ABS","Grillon3",900,1.27,spool_gr=1000)

pla_cost = pla_grillon3.gr_cost
petg_cost = petg_grillon3.gr_cost
abs_cost = abs_grillon3.gr_cost
flex_cost = flex_grillon3.gr_cost


def cm3_to_gr(kind,cm3=0):
    if kind == 'PLA':
        density = 1.25
        gr = cm3 * density
    elif kind == 'PETG':
        density = 1.27
        gr = cm3 * density
    elif kind == 'ABS':
        density = 1.05
        gr = cm3 * density
    elif kind == 'FLEX':
        density = 1.22
        gr = cm3 * density
    else:
        print('Kind not found')
    return gr

def kind_gr_cost(kind):
    if kind == 'PLA':
        return pla_cost
    elif kind == 'PETG':
        return petg_cost
    elif kind == 'ABS':
        return abs_cost
    elif kind == 'FLEX':
        return flex_cost
    else:
        print('Error Kind_gr_cost')

def cost(kind='PLA',cm3=0,time=0,gr=None):
    if gr == None:
        gr=cm3_to_gr(kind,cm3)  
    else:
        pass
    gr_cost=kind_gr_cost(kind)
    cost= (gr*gr_cost)+ time
    return cost


# for file in folder_gcode.iterdir():
#     name= Path(file).name
#     d=parse_gcode(file)
#     c=cost(d['kind'],d['gr'],d['time'])
#     print(f'{name} sale ${c}')