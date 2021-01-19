from pathlib import Path
import os

path_=Path(".")

folder_gcode= path_ /"gcode"
folder_gcode_full=folder_gcode.resolve()
folder_3mf= path_/"3mf"
folder_mardel3d_db= path_/"mardel3d_db"
folder_3mf_full=folder_3mf.resolve()
slicer_console= path_/"PrusaSlicer-2.3.0/prusa-slicer-console.exe"
printset_file="bd\printset\ss.ini"


