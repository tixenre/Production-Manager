import os
import re

## own libs
from project_path import folder_gcode

def parse_gcode(file):
        file_name, file_ext = os.path.splitext(file)
        if file_ext == ".gcode":
            with open(file, 'r') as f_gcode:
                data = f_gcode.read()
                value_gr = re.search(r'total filament used \[g\] = (\d+.\d+)',data)
                value_cm3 = re.search(r'filament used \[cm3\] = (\d+.\d+)',data)
                value_kind = re.search(r'filament_type = (\w+)', data)
                value_time = re.search(r'estimated printing time \(silent mode\) = (\d+)\w? (\d+)\w? (\d+)\w?', data)

            if value_gr and value_kind and value_time :
                gr = float(value_gr.group(1))
                cm3= float(value_cm3.group(1))
                kind = (value_kind.group(1))
                time = int((float(value_time.group(1))*60)+(float(value_time.group(2)))/60)
                f= dict(name = (file_name),kind = (kind),gr=(gr),time=(time),cm3=(cm3))
                print(f'Parsing {file_name}')
                print(f)
                return f
            else:
                print('Something went wrong with get_data')

parse_gcode(r'C:\Users\tixen\Desktop\Python\Production Manager\gcode')
# for file in folder_gcode.iterdir():
#     q=parse_gcode(file)
#     f=q['gr']
#     print(f)