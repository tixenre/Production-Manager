import shlex
from pathlib import Path
from project_path import folder_3mf, folder_gcode, filaments

mylist = [file for file in filaments.iterdir()]

# p =  f'-g --load \presets\filament\0.2Normal.ini Sonic.3mf'

# print(mylist)
