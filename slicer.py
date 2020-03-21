import os
import subprocess
import shutil
from contextlib import contextmanager
import time

os.chdir(r'\Users\tixen\Desktop\Python\Production Manager')
print(os.getcwd())

path_3mf = '3mf'
path_gcode = 'gcode'

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

def files_in(folder):
    with change_dir(folder):
        files = os.listdir()
    return files


# slice .3mf files in /3mf
def do_slice(file):
    _, file_ext = os.path.splitext(file)
    with change_dir(path_3mf):
        if file_ext == ".3mf":
            t1= time.perf_counter()
            print(f'Slicing {file}')
            subprocess.Popen([r'C:\Users\tixen\Desktop\Python\Production Manager\PrusaSlicer\prusa-slicer-console', '-g',file],).communicate(timeout=None)
            t2= time.perf_counter()
            print(f'Done Slicing {file} in {t2-t1} seconds')
        else:
            pass
    
    


# move .gcodes files from /3mf to /gcodes
def move_gcodes():
    for file in files_in(path_3mf):
        _, file_ext = os.path.splitext(file)
        with change_dir(path_3mf):
            if file_ext == ".gcode":
                shutil.copy(file,os.path.join(os.path.dirname(os.getcwd()), path_gcode))
                os.remove(file)
            else:
                pass
    print('Done moving')

# for file in files_in(path_3mf):
#     do_slice(file)
#     move_gcodes()