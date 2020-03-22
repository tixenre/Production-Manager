import subprocess, time
from shutil import move
from pathlib import Path

# onw libs
from project_path import folder_3mf, slicer


### slice .3mf files in /3mf
def do_slice(file):
    suffix = Path(file).suffix
    name= Path(file).name
    if suffix == ".3mf":
        t1= time.perf_counter()
        print(f'Slicing {name}')
        subprocess.Popen([slicer, '-g',file],).communicate(timeout=None)
        t2= time.perf_counter()
        print(f'Done Slicing {name} in {t2-t1} seconds')
    else:
        pass
    
   
# # # move .gcodes files from /3mf to /gcodes
def move_gcodes(file):
    suffix = Path(file).suffix
    # dest = folder_gcode.as_posix()
    if suffix == '.gcode':
        # file.replace(folder_gcode)
        move(file, r'C:\Users\tixen\Desktop\Python\Production Manager\PrusaSlicer\gcode')

    else:
        pass
    print('Done moving .gcode files')

# for file in folder_3mf.iterdir():
#         do_slice(file)
#         move_gcodes(file)
# print('Done moving .gcode files')    