import re
import os
import csv
import datetime
from pathlib import Path

#Gcode Folder
import project_path as pp

def parse_gcode(file,folder=pp.folder_gcode):
        file_ext = Path(file).suffix
        file_stem = Path(file).stem
        file_to_parse=folder/file
        if file_ext == ".gcode":
            with open(file_to_parse, 'r') as f_gcode:
                data = f_gcode.read()
                value_gr = re.search(r'total filament used \[g\] = (\d+.\d+)',data)
                value_cm3 = re.search(r'filament used \[cm3\] = (\d+.\d+)',data)
                value_kind = re.search(r'filament_type = (\w+)', data)
                value_time = re.search(r'estimated printing time \(silent mode\) = (\d+)\w? (\d+)\w? (\d+)\w?', data)

            if value_gr and value_kind and value_time :
                minutes = (int(value_time.group(1))*60)+int(value_time.group(2))+5
                gr = float(value_gr.group(1))
                kind = (value_kind.group(1))
                cm3= float(value_cm3.group(1))
                print(f'Parsing {file_stem}')

                with open("parsed.csv",'a',newline='') as csv_temp:
                    fieldnames = ["Name","Minutes","Hs","Gr","Cm3","Kind","Date"]
                    csv_writer = csv.DictWriter(csv_temp, fieldnames=fieldnames, delimiter=',')
                    today= datetime.date.today()
                    csv_writer.writerow({"Name":file_stem,
                            "Minutes":minutes,
                            "Hs":str(datetime.timedelta(minutes=minutes)),
                            "Gr":gr,
                            "Cm3":cm3,
                            "Kind":kind,
                            "Date":today})    
            else:
                print('Something went wrong with get_data')
        os.remove(file_to_parse)
    
