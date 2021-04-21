import subprocess
import time
from pathlib import Path
import os
import pandas as pd

#Project Import
import project_path as pp

#PrusaSlicer
def do_slice(file,printset=pp.printset_file):
    print(file)
    file_ext = Path(file).suffix
    file_stem = Path(file).stem
    file_to_slice=file
    folder_to=f"{pp.folder_gcode_full}/{file_stem}.gcode"
    if file_ext == ".3mf":
        t1 = time.perf_counter()
        print(f'Slicing {file_stem}')
        s = f'{pp.slicer_console}  -g {file_to_slice} --load {printset} --output {folder_to}'
        subprocess.call(s)
        t2 = time.perf_counter()
        print(f'Done Slicing {file_stem} in {t2-t1} seconds')


    return file

