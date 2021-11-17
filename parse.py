import os
import re
from pathlib import Path

## own libs
from project_path import folder_gcode
import file_check

def parse_gcode(file):
    file_name = file_check.get_file_name(file)
    if file_check.is_gcode(file):

        with open(file, "r") as f_gcode:
            d = f_gcode.read()

            days = 0
            hours = 0
            minutes = 6

            #Checks if gcode time starts with days
            if re.search(r"estimated printing time \(silent mode\) = (\d+)d", d):
                re_time = re.search(r"estimated printing time \(silent mode\) = (\d+)d (\d+)h (\d+)m", d)
                days = int(re_time.group(1))
                hours = int(re_time.group(2))
                minutes += int(re_time.group(3))
            
            #Checks if gcode time starts with hours
            elif re.search(r"estimated printing time \(silent mode\) = (\d+)h", d):
                re_time = re.search(r"estimated printing time \(silent mode\) = (\d+)h (\d+)m", d)
                hours = int(re_time.group(1))
                minutes += int(re_time.group(2))
 
            #Checks if gcode time starts with minutes
            elif re.search(r"estimated printing time \(silent mode\) = (\d+)m", d):
                re_time = re.search(r"estimated printing time \(silent mode\) = (\d+)m", d)
                minutes += int(re_time.group(1))
            
            re_time = days*24*60 + hours*60 + round(minutes,-1)
            re_gr = re.search(r"total filament used \[g\] = (\d+.\d+)",d)
            re_kind = re.search(r"filament_type = (\w+)", d)
            re_cm3 = re.search(r"filament used \[cm3\] = (\d+.\d+)",d)
            re_instances = set(re.findall(r"copy (.+)", d))
            re_nozzle_diameter = re.search(r"nozzle_diameter = (.+)",d)
            re_printer_model = re.search(r"printer_model = (.+)",d)
            re_size_z = re.findall(r"G1 Z(\d+\.\d+)",d)

        if re_gr and re_kind and re_time :
            print("")
            print(f"Parsing: {file_name}")

            data = {
                "time" : re_time,
                "gr" : float(re_gr.group(1)),
                "kind" : re_kind.group(1),
                "cm3" : float(re_cm3.group(1)),
                "instances" : int(max(re_instances))+1,
                "nozzle_diameter" : float(re_nozzle_diameter.group(1)),
                "printer_model" : re_printer_model.group(1),
                "size_z": re_size_z.pop(-5)
                }
            return data

        else:
            print(f"Something went wrong with parsing {file_name}")
        
    else:
        print(f"Gcode {file_name} not found")
        return None


def most_frequent(List):
    return max(set(List), key = List.count)

# folder = Path(r"C:\Users\marti\Documents\Hola_Deco\3mf")
# for file in folder.iterdir():
#     if file_check.is_gcode(file):
#         q = parse_gcode(file)
#         print(q["cm3"])

file = Path(r"C:\Users\marti\Documents\GitHub\Production-Manager\gcode\Mickey Navidad Bola - (4h14m) (55.4072gr) (0.3mm) (PLA) (17-11).gcode")

print(parse_gcode(file))