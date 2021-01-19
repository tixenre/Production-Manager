import os
import csv
import time
import project_path as pp
import slice
import parser3
from pathlib import PurePath

#folder=PurePath("Users\tixen\Desktop\bd_mardel3d")
folder= pp.folder_3mf

def base_datos_mardel3d():

    t1 = time.perf_counter()
    for f in os.listdir(folder):
        slice.do_slice(f)
        pass

    with open("parsed.csv",'w+',newline='') as csv_temp:
        fieldnames = ["Name","Minutes","Hs","Gr","Cm3","Kind","Date"]
        csv_writer = csv.DictWriter(csv_temp, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()

    for f in os.listdir(pp.folder_gcode):
        parser3.parse_gcode(f,folder=pp.folder_gcode)
        pass
    
    t2 = time.perf_counter()
    print(f'Done Slicing and Parsong All Files from Folder{folder} in {t2-t1} seconds')

base_datos_mardel3d()



