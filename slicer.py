import subprocess
import time
from pathlib import Path
from os import remove
import project_path as pp
import file_checks 

def do_slice(file,printset=pp.print_preset_def, fil=pp.filament_preset_def, printer=pp.printer_preset_def):

    if file_checks.is_3mf(file):
        s = f'{pp.slicer_console}  -g {file}'
    elif file_checks.is_stl(file):
        s = f'{pp.slicer_console}  -g {file} --load {printset} --load {fil} --load {printer}'


    file_name = Path(file).name
    print(f'Slicing: {file_name}')
    t1 = time.perf_counter()
    subprocess.call(s)
    t2 = time.perf_counter()
    time_elapse = round(t2-t1,2)
    print(f'Done slicing {file_name} in {time_elapse} seconds')

def slice_3mf(file):

    if file_checks.is_3mf(file):
        do_slice(file)

#Slice
def slice_stl(file):

    if file_checks.is_stl(file):
        printset=pp.print_preset_def
        fil=pp.filament_preset_def
        printer=pp.printer_preset_def
        do_slice(file, printset, fil, printer)

def slice_folder(folder, s_3mf = True, s_stl = False):
    for file in folder.iterdir():
        if file_checks.is_gcode(file):
            remove(file)
        elif s_3mf == True and file_checks.is_3mf(file):   
            slice_3mf(file)
        elif s_stl == True and file_checks.is_stl(file):
            slice_stl(file)


# file_to_slice = Path(pp.folder_3mf / "Sonic.3mf")
# stl_to_slice = Path(pp.folder_3mf / "Sonic.stl")

slice_folder(pp.folder_3mf)
