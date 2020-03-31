from pathlib import Path

## own libs
from project_path import folder_gcode
from parse import parse_gcode
from presupuestador import cost

sell_mode = {'servicio': 2, 'producto': 1.5, 'mardel3d': 1.1}

comision = {'cash': 1, 'mercadopago': 1.06, 'mercadolibre_clasic': 1.13, 'mercadolibre_gold':1.23}

def price(cost,sell_mode,comision=1):
    price= (cost * sell_mode)*comision
    return int(price)




for file in folder_gcode.iterdir():
    name= Path(file).name
    d=parse_gcode(file)
    c=cost(d['kind'],d['gr'],d['time'])
    p= price(c,sell_mode['producto'],comision['cash'])
    print(f'{name} sale ${p}')

# print(price(100,2))