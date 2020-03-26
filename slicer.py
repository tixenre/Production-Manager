from pathlib import Path
import subprocess
import time
from project_path import folder_3mf

# #Slice File
file_to_slice = Path(folder_3mf / "Sonic.3mf")
stl_to_slice = Path(folder_3mf / "Sonic.stl")
# Folder to Slice
folder_to_slice = folder_3mf

# Presets Path
slicer_console = Path(r'PrusaSlicer\prusa-slicer-console')
print_preset = Path(r'PrusaSlicer\presets\print')
filament_preset = Path(r'PrusaSlicer\presets\filament')
printer_preset = Path(r'PrusaSlicer\presets\printer')
# Presets List
prints_presets = [file for file in print_preset.iterdir()]
filaments_presets = [file for file in filament_preset.iterdir()]
printers_presets = [file for file in printer_preset.iterdir()]
# Default Profiles for Slicing
print_preset_def = Path(prints_presets[1])
filament_preset_def = Path(filaments_presets[3])
printer_preset_def = Path(printers_presets[0])
# print(print_preset_def)
# print(filament_preset_def)
# print(printer_preset_def)


#Slicer
def do_slice(file, printset=print_preset_def, fil=filament_preset_def, printer=printer_preset_def):
    f= Path(file).name
    t1 = time.perf_counter()
    print(f'Slicing {f}')
    s = f'{slicer_console}  -g {file} --load {printset} --load {fil} --load {printer}'
    subprocess.call(s)
    t2 = time.perf_counter()
    print(f'Done Slicing {f} in {t2-t1} seconds')


#######check it!
def stl_to_3mf(file):
    p=(Path(stl_to_slice).parent) ##Parent Folder
    stem = Path(file).stem        ## File Stem
    tw= p / stem / '.3mf'         ## Twin .3mf
    isf= Path.is_file(tw)         ## If True file has a Twin
    print(isf)
    # if isf is False:
    #     s = f'{slicer_console}  --export-3mf {file}'
    #     subprocess.call(s)
    #     Path.unlink(file)
    #     print (f'{file} does not have a twin and it was exported to .3mf')
    # elif isf is True:
    #     Path.unlink(file)
    #     print(f'{file} has a twin and it has been deleted')
    # else:
    #     print('Not STL found')


def slice_file(file):
    do_slice(file)

def slice_folder(folder):
    mmf_in_folder = list(Path(folder_to_slice).glob('*.3mf'))
    stl_in_folder = list(Path(folder_to_slice).glob('*.stl'))
    for stl in  stl_in_folder:
        stl_to_3mf(stl)
    for files in mmf_in_folder:
        do_slice(files)
    

# slice_file(file_to_slice)
# slice_folder(folder_to_slice)
stl_to_3mf(stl_to_slice)