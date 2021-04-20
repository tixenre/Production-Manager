import re
import os
import csv
import datetime
from pathlib import Path

#Gcode Folder
import project_path as pp


today= datetime.date.today()
fieldnames = ["Name","Minutes","Hs","Gr","Cm3","Kind","Date"]



def parser(file):
    folder=pp.folder_gcode
    file_ext = Path(file).suffix
    file_stem = Path(file).stem
    file_to_parse=folder/file
    if file_ext == ".gcode":
        with open(file_to_parse, 'r') as f_gcode:
            data = f_gcode.read()
            value_gr = re.search(r'total filament used \[g\] = (\d+.\d+)',data)
            value_cm3 = re.search(r'filament used \[cm3\] = (\d+.\d+)',data)
            value_kind = re.search(r'filament_type = (\w+)', data)
            value_time_min= re.search(r'estimated printing time \(silent mode\) = (\d+)m (\d+)s', data)
            value_time_hs = re.search(r'estimated printing time \(silent mode\) = (\d+)h (\d+)m (\d+)s', data)
            value_time_days = re.search(r'estimated printing time \(silent mode\) = (\d+)d (\d+)h (\d+)m (\d+)s', data)
            value_time = None
            if value_time_min != None:
                value_time = int(value_time_min.group(1))+5
            elif value_time_hs != None:
                value_time = (int(value_time_hs.group(1))*60)+int(value_time_hs.group(2))+5
            elif value_time_days != None:
                value_time = (int(value_time_days.group(1))*24*60)+(int(value_time_days.group(2))*60)+int(value_time_days.group(3))+5


        if value_gr and value_kind and value_time :
            minutes = value_time
            gr = float(value_gr.group(1))
            kind = (value_kind.group(1))
            cm3= float(value_cm3.group(1))
            print(f'Parsing {file_stem}')

            with open("gcodes_parsed.csv",'a',newline='') as csv_temp:
                csv_writer = csv.DictWriter(csv_temp, fieldnames=fieldnames, delimiter=',')
                csv_writer.writerow({
                                    "Name":file_stem,
                                    "Minutes":minutes,
                                    "Hs":str(datetime.timedelta(minutes=minutes)),
                                    "Gr":gr,
                                    "Cm3":cm3,
                                    "Kind":kind,
                                    "Date":today,
                                    })
            os.remove(file_to_parse)
            
        else:
            print(f'Something went wrong with {file}')

    
    


def parse_gcode(): 
    with open("gcodes_parsed.csv",'w',newline='') as csv_temp:  
        csv_writer = csv.DictWriter(csv_temp, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()

    for f in os.listdir(pp.folder_gcode):
        parser(f)
    pass