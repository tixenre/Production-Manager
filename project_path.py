from pathlib import Path
import shlex

cwd = Path.cwd()
folder_3mf = Path('3mf')
folder_gcode = Path('gcode')

slicer_console = Path(r'PrusaSlicer\prusa-slicer-console')

## Slicer preset Path##
filaments = Path(r'PrusaSlicer\presets\filament')
prints = Path(r'PrusaSlicer\presets\print')
printers = Path(r'PrusaSlicer\presets\printer')

# sh = shlex.quote(filaments)
# print(sh)
