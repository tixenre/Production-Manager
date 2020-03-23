import subprocess
import time
import shlex
from shutil import move
from pathlib import Path

# onw libs
from project_path import folder_3mf, folder_gcode, slicer_console, prints, filaments, printers, cwd

### 
prints_presets = [file for file in prints.iterdir()]
filaments_presets = [file for file in filaments.iterdir()]
printers_presets = [file for file in printers.iterdir()]

print_preset_def = Path(prints_presets[1])
filament_preset_def = Path(filaments_presets[3])
printer_preset_def = Path(printers_presets[0])


# # slice .3mf files in /3mf
f1 = Path(r'3mf\Sonic.3mf')
# f2 = Path(r'3mf\Sonic.stl')
# p = Path(r'PrusaSlicer\presets\print\020_Normal.ini')
# pp = Path(r'PrusaSlicer\presets\printer\def.ini')
# i = Path(r'PrusaSlicer\presets\filament\PLA.ini')
# s1 = f'{slicer_console}  ---export-stl {f1}'
# s2 = f'{slicer_console}  -g {f2} --load {p} --load {i} --load {pp}'
# subprocess.call(s1)
# subprocess.call(s2)



def slice_3mf(file):
    suffix = Path(file).suffix
    stem = Path(file).stem
    if suffix == ".3mf":       
        f = file
        s = f'{slicer_console}  ---export-stl {f}'
        subprocess.call(s)
    return stem + '.stl'

def slice_stl(file, p=print_preset_def, fil=filament_preset_def, pp=printer_preset_def):
    suffix = Path(file).suffix
    if suffix == '.stl':
        f = file
        s = f'{slicer_console}  -g {f} --load {p} --load {fil} --load {pp}'
        subprocess.call(s)

def do_slice(file, p=print_preset_def, fil=filament_preset_def, pp=printer_preset_def):
    suffix = Path(file).suffix
    stem = Path(file).stem
    f_3mf = Path(f'3mf/{stem}.3mf')
    f_stl = Path(f'3mf/{stem}.stl')
    if suffix == '.3mf':
        slice_3mf(f_3mf)
        slice_stl(f_stl)
    elif suffix == '.stl':
        slice_stl(f_stl)
    pass

def slice_single(file):
    do_slice(file)
    pass


def slice_batch(folder):
    for file in folder.iterdir():
        do_slice(file)
    pass


# # # # move .gcodes files from /3mf to /gcodes

# def move_gcodes(file):
#     suffix = Path(file).suffix
#     if suffix == '.gcode':
#         move(file, r'C:\Users\tixen\Desktop\Python\Production Manager\PrusaSlicer\gcode')
#     else:
#         pass
#     print('Done moving .gcode files')


# #
    ### TEST ONLY ###
###### Single File Slicing #####
# do_slice(f1)
# # slice_single(file_to_slice)

# ###### Batch File Slicing #####
slice_batch(folder_3mf)
