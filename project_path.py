from pathlib import Path
import shlex

cwd = Path.cwd()
folder_3mf = Path('3mf')
folder_gcode = Path('gcode')

slicer_console = Path(r'PrusaSlicer\prusa-slicer-console')

## Slicer preset Path##
prints = Path(r'PrusaSlicer\presets\print')
filaments = Path(r'PrusaSlicer\presets\filament')
printers = Path(r'PrusaSlicer\presets\printer')


prints_presets = [file for file in prints.iterdir()]
filaments_presets = [file for file in filaments.iterdir()]
printers_presets = [file for file in printers.iterdir()]

print_preset_def = Path(prints_presets[1])
filament_preset_def = filaments_presets[3]
printer_preset_def = printers_presets[0]


# print(print_preset_def)
# print(filament_preset_def)
# print(printer_preset_def)
