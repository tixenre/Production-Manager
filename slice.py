import subprocess
import time
from pathlib import Path

#Project Import
import project_path as pp

#PrusaSlicer
def do_slice(file,printset=pp.printset_file,folder=pp.folder_3mf):
    folder_to=pp.folder_gcode_full
    file_ext = Path(file).suffix
    file_stem = Path(file).stem
    file_to_slice=folder/file
    if file_ext == ".3mf":
        t1 = time.perf_counter()
        print(f'Slicing {file_stem}')
        s = f'{pp.slicer_console}  -g {file_to_slice} --load {printset} --output {folder_to}'
        subprocess.call(s)
        t2 = time.perf_counter()
        #print(f'Done Slicing {file_stem} in {t2-t1} seconds')