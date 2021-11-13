from pathlib import Path
# import shlex

cwd = Path.cwd()
folder_3mf = Path('3mf')
folder_gcode = Path('gcode')

slicer_console = Path(r'PrusaSlicer\prusa-slicer-console')

## Slicer preset Path##
prints = Path(r'PrusaSlicer\presets\print')
filaments = Path(r'PrusaSlicer\presets\filament')
printers = Path(r'PrusaSlicer\presets\printer')

print_preset_def = Path(r'PrusaSlicer\presets\print\030_Rapido_Fuerte.ini')
filament_preset_def = Path(r'PrusaSlicer\presets\filament\PLA.ini')
printer_preset_def = Path(r'PrusaSlicer\presets\printer\def.ini')

print_presets = [f for f in prints.iterdir()]
filament_presets = [f for f in filaments.iterdir()]
printer_presets = [f for f in printers.iterdir()]



# print(prints)

