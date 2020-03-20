import os
import re

def get_data(file):
        file_name, file_ext = os.path.splitext(file)
        if file_ext == ".gcode":
            with open(file, 'r') as f_gcode:
                data = f_gcode.read()
                value_gr = re.search(r'total filament used \[g\] = (\d+.\d+)',data)
                value_mm3 = re.search(r'filament used \[cm3\] = (\d+.\d+)',data)
                value_kind = re.search(r'filament_type = (\w+)', data)
                value_time = re.search(r'estimated printing time \(silent mode\) = (\d+)\w? (\d+)\w? (\d+)\w?', data)

            if value_gr and value_kind and value_time :
                gr = float(value_gr.group(1))
                mm3= float(value_mm3.group(1))
                kind = (value_kind.group(1))
                time = int((float(value_time.group(1))*60)+(float(value_time.group(2)))/60)
                f= dict(name = (file_name),kind = (kind),gr=(gr),time=(time),mm3=(mm3))
                print(f'Getting {file_name}')
                # print(f)
                return f
            else:
                print('Something went wrong with get_data')


os.chdir(r'C:\Users\tixen\Desktop\Python\Production Manager\gcode')
for file in os.listdir():
    print(get_data(file))