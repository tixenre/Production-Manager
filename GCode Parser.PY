import re
import os
import subprocess

os.chdir(r'C:\Users\tixen\Desktop\Python\Production Manager\gcodes')

gananciaservicio = 1 + 3.0
gananciaproducto = 5

class Filaments:
    def __init__(self,kind,vendor,spool_cost,density,spool_gr):
        self.kind = "kind"
        self.vendor = "vendor"
        self.spool_cost = float(spool_cost)
        self.density = float(density)
        self.spool_gr = int(spool_gr)
        self.gr_cost = float(spool_cost/spool_gr)
        

pla_grillon3 = Filaments("PLA","Grillon3",1000,1.25,1000)		
petg_grillon3 = Filaments("PETg","Grillon3",1000,1.27,1000)
pla_pal = Filaments("PLA","PrintaLot",960,1.25,1000)
flex_grillon3 = Filaments("Flex","Grillon3",1614,1.25,1000)


def get_filament_gr(file):
    with open(file, 'r') as f_gcode:
        data = f_gcode.read()
        value = re.search(r'total filament used \[g\] = (\d+.\d+)',data)
               
        if value:
            gr = float(value.group(1))
        else:
            print('filament gr not found in {}'.format(file))
            gr = 0.0
        return gr

def get_filament_kind(file):
    with open(file, 'r') as f_gcode:
        data = f_gcode.read()
        value = re.search(r'filament_type = (\w+)', data)

        if value:
            kind = (value.group(1))
        else:
            print('filament kind not found in {}'.format(file))
            kind = None
        return kind

def get_print_time (file):
	with open(file, "r") as f_gcode:
		data= f_gcode.read()
		re_value = re.search(r'estimated printing time \(silent mode\) = (\d+)\w? (\d+)\w? (\d+)\w?', data)

		if re_value:
			value_hs =float(re_value.group(1))*60
			value_min = float(re_value.group(2))
			value = (value_hs+value_min)/60
		else:
			print('Hs not found {}'.format(file))
			value = 0.0
		return value


for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    if file_ext == ".gcode":
        file_filament_kind = get_filament_kind(file)
        file_filament_gr = get_filament_gr(file)
        file_print_time= get_print_time(file)
        
    #elif file_ext == ".3mf":
    #    #slicer= r'C:\Users\tixen\Desktop\Python\Production Manager\PrusaSlicer\prusa-slicer-console.exe'
    #    #export= r'-g
    #    subprocess.Popen([r'C:\Users\tixen\Desktop\Python\Production Manager\PrusaSlicer\prusa-slicer-console.exe', '-g',"myfile.3mf"],)

    def print_cost_():
        cost= (file_filament_gr*pla_grillon3.gr_cost)+(file_print_time*(22.484))
        return cost
    def print_cost_public_():
        cost = print_cost_()*gananciaproducto
        return cost

    print_cost = print_cost_()
    print_price = print_cost_public_()

    print(file_filament_kind)
    print([file_name, file_filament_kind, file_filament_gr, file_print_time])
    print("$",print_price)
