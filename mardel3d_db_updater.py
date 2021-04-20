import os
import csv
import time
import project_path as pp
import slice
import gcode_parser
from pathlib import PurePath

#folder=PurePath("Users\tixen\Desktop\bd_mardel3d")
#folder= pp.folder_3mf
folder=pp.folder_mardel3d_db


t1 = time.perf_counter()
for f in os.listdir(folder):
    slice.do_slice(f,folder=folder)
    pass

t2 = time.perf_counter()
print(f'Done Slicing and Parsong All Files from Folder{folder} in {t2-t1} seconds')

gcode_parser.parse_gcode()

print(f'gcodes_parsed.csv has been created')
    
    



