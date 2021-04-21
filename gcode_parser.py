import re
import os
import datetime
from pathlib import Path
import re
import base64

import pandas as pd
import numpy as np

#Gcode Folder
import project_path as pp
import prints_database


today= datetime.date.today()
fieldnames = prints_database.database_fieldnames


def parser(file,delete_gcode=True):
    folder=pp.folder_gcode
    file_ext = Path(file).suffix
    file_stem = Path(file).stem
    file_to_parse=folder/file
    if file_ext == ".gcode":


        #Parce Thumbnail 
        with open(file,"r") as gcode_file:
            data = gcode_file.read()
            match = re.search(r"(; thumbnail begin 220x124 22424)(.*)(; thumbnail end)",data, re.DOTALL)
            thumbnail = match.group(2).replace("; ", "")
            if len(thumbnail) > 0:
                with open(f"{file_stem}.png","wb") as png_file:
                    png_file.write(base64.b64decode(thumbnail.encode()))

        #Parce Print Job details
        with open(file, 'r') as f_gcode:
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
            minutes = int(value_time)
            gr = float(value_gr.group(1))
            kind = (value_kind.group(1))
            cm3= float(value_cm3.group(1))

            print(f'Parsing {file_stem}')

           
            #Create Dataframe and export it to .csv
            df = pd.DataFrame(columns=fieldnames)
            df.loc[1,"Name"] = file_stem
            df.loc[1,"Minutes"] = minutes
            df.loc[1,"Hs"] = str(datetime.timedelta(minutes=minutes))
            df.loc[1,"Gr"] = gr
            df.loc[1,"3mf Path"] = file_to_parse
            df.loc[1,"cm3"] = cm3
            df.loc[1,"Kind"] = kind
            df.loc[1,"Last Modify"] = today
            df.set_index("ID",inplace=True)
            df.to_csv(f"csv/{file_stem}.csv")

            print(f'{file_stem} was parced and exported to .csv')

            
            if delete_gcode == True:
                os.remove(file)


        else:
            print(f'Something went wrong with {file}')
        pass
        
# def extract_thumbnail(gcode):
#     file_stem = Path(gcode).stem
#     with open(gcode,"r") as gcode_file:
#         data = gcode_file.read()
#         match = re.search(r"(; thumbnail begin 220x124 22424)(.*)(; thumbnail end)",data, re.DOTALL)
#         thumbnail = match.group(2).replace("; ", "")
#     if len(thumbnail) > 0:
#         with open(f"{file_stem}.png","wb") as png_file:
#             png_file.write(base64.b64decode(thumbnail.encode()))