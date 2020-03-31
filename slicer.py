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
print_preset_def = Path(r'PrusaSlicer\presets\print\020_Normal.ini')
filament_preset_def = Path(r'PrusaSlicer\presets\filament\PLA.ini')
printer_preset_def = Path(r'PrusaSlicer\presets\printer\def.ini')

# Slicer
def do_slice(file, printset=print_preset_def, fil=filament_preset_def, printer=printer_preset_def):
    if Path(file).suffix == '.3mf':
        f = Path(file).name
        t1 = time.perf_counter()
        print(f'Slicing {f}')
        s = f'{slicer_console}  -g {file} --load {printset} --load {fil} --load {printer}'
        subprocess.call(s)
        t2 = time.perf_counter()
        print(f'Done Slicing {f} in {t2-t1} seconds')


# def slice_file(file):
#     do_slice(file)


# def slice_folder(folder):
#     mmf_in_folder = list(Path(folder_to_slice).glob('*.3mf'))
#     stl_in_folder = list(Path(folder_to_slice).glob('*.stl'))
#     for stl in stl_in_folder:
#         stl_to_3mf(stl)
#     for files in mmf_in_folder:
#         do_slice(files)

if __name__ == "__main__":
    print(print_preset_def)
    print(filament_preset_def)
    print(printer_preset_def)
    do_slice(file_to_slice)
    # slice_folder(folder_to_slice)
    # stl_to_3mf(stl_to_slice)
