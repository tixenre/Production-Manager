import subprocess, time, shlex
from shutil import move
from pathlib import Path

# onw libs
from project_path import folder_3mf, folder_gcode, slicer_path, filaments, prints, printers

prints_presets = [file for file in prints.iterdir()]
filaments_presets = [file for file in filaments.iterdir()]
printers_presets = [file for file in printers.iterdir()]

print_preset_def= prints_presets[3].name
filament_preset_def= filaments_presets[3].name
printer_preset_def= printers_presets[0].name


### slice .3mf files in /3mf
def do_slice(file,prints_preset=print_preset_def,filaments_preset='filament_preset_def',printers_preset='printer_preset_def'):
    suffix = Path(file).suffix
    name= Path(file).name
    if suffix == ".3mf":
        t1= time.perf_counter()
        print(f'Slicing {name}')
        subprocess.Popen([slicer_path, '-g', file]).communicate(timeout=None)
        t2= time.perf_counter()
        print(f'Done Slicing {name} in {t2-t1} seconds')
    else:
        pass

def slice_single(file):
    do_slice(file)
    pass

def slice_batch(folder):
    for file in folder.iterdir():
        do_slice(file)
    pass      

# # # move .gcodes files from /3mf to /gcodes
def move_gcodes(file):
    suffix = Path(file).suffix
    if suffix == '.gcode':
        move(file, r'C:\Users\tixen\Desktop\Python\Production Manager\PrusaSlicer\gcode')
    else:
        pass
    print('Done moving .gcode files')



#
        ### TEST ONLY ###
###### Single File Slicing #####
# file_to_slice = folder_3mf / 'Sonic.3mf'

# slice_single(file_to_slice)

###### Batch File Slicing #####
slice_batch(folder_3mf)
