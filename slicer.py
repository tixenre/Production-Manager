import subprocess
import time
from pathlib import Path
from os import remove
import project_path as pp


def do_slice(file,printset=pp.print_preset_def, fil=pp.filament_preset_def, printer=pp.printer_preset_def):

    file_suffix = Path(file).suffix 

    if file_suffix == ".3mf":
        s = f'{pp.slicer_console}  -g {file}'
    elif file_suffix == ".stl":
        s = f'{pp.slicer_console}  -g {file} --load {printset} --load {fil} --load {printer}'


    file_name = Path(file).name
    print(f'Slicing: {file_name}')
    t1 = time.perf_counter()
    subprocess.call(s)
    t2 = time.perf_counter()
    time_elapse = round(t2-t1,2)
    print(f'Done slicing {file_name} in {time_elapse} seconds')

def slice_3mf(file):

    file_suffix = Path(file).suffix

    if file_suffix == ".3mf":
        do_slice(file)

#Slice
def slice_stl(file):

    file_suffix = Path(file).suffix

    if file_suffix == ".stl":
        printset=pp.print_preset_def
        fil=pp.filament_preset_def
        printer=pp.printer_preset_def
        do_slice(file, printset, fil, printer)



def slice_folder(folder, s_3mf = True, s_stl = False):

    for file in folder.iterdir():
        file_sufix= Path(file).suffix
        if file_sufix == ".gcode":
            remove(file)
        elif s_3mf == True and file_sufix == ".3mf":   
            slice_3mf(file)
        elif s_stl == True and file_sufix == ".stl":
            slice_stl(file)


# file_to_slice = Path(pp.folder_3mf / "Sonic.3mf")
# stl_to_slice = Path(pp.folder_3mf / "Sonic.stl")

slice_folder(pp.folder_3mf)
