import parse
import presupuestador
import slicer
import project_path as pp

from pathlib import Path

# #Slice File
file_to_slice = Path(pp.folder_3mf / "Sonic.3mf")
stl_to_slice = Path(pp.folder_3mf / "Sonic.stl")
# Folder to Slice
folder_to_slice = pp.folder_3mf

# for mf in folder_to_slice.iterdir():
#     slicer.do_slice(mf)
for gcode in folder_to_slice.iterdir():
    f=parse.parse_gcode(gcode)
    print(f)

