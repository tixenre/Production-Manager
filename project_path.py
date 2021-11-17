from pathlib import Path

cwd = Path.cwd()
pp= Path(r"C:\Users\marti\Documents\GitHub\Production-Manager")
folder_3mf = Path('3mf')
folder_gcode = Path('gcode')

slicer_console = Path(r'C:\Users\marti\Documents\GitHub\Production-Manager\PrusaSlicer\prusa-slicer-console')

## Slicer preset Path##
prints = Path(r'C:\Users\marti\Documents\GitHub\Production-Manager\PrusaSlicer\presets\print')
filaments = Path(r'C:\Users\marti\Documents\GitHub\Production-Manager\PrusaSlicer\presets\filament')
printers = Path(r'C:\Users\marti\Documents\GitHub\Production-Manager\PrusaSlicer\presets\printer')

print_preset_def = Path(r'C:\Users\marti\Documents\GitHub\Production-Manager\PrusaSlicer\presets\print\030_Rapido_Fuerte.ini')
filament_preset_def = Path(r'C:\Users\marti\Documents\GitHub\Production-Manager\PrusaSlicer\presets\filament\PLA.ini')
printer_preset_def = Path(r'C:\Users\marti\Documents\GitHub\Production-Manager\PrusaSlicer\presets\printer\def.ini')

print_presets = [f for f in prints.iterdir()]
filament_presets = [f for f in filaments.iterdir()]
printer_presets = [f for f in printers.iterdir()]



# print(prints)

