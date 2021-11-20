from pathlib import Path


cwd = Path.cwd()
folder_3mf = Path('3mf')
folder_gcode = Path('gcode')

#Slicer Path
slicer_console = cwd.joinpath(r"Production-Manager\PrusaSlicer\prusa-slicer-console")

prints = cwd.joinpath(r"PrusaSlicer\presets\print")
filaments = cwd.joinpath(r"PrusaSlicer\presets\filament")
printers = cwd.joinpath(r"PrusaSlicer\presets\printer")

print_preset_def = cwd.joinpath(r"PrusaSlicer\presets\print\030_Rapido_Fuerte.ini")
filament_preset_def = cwd.joinpath(r"PrusaSlicer\presets\filament\PLA.ini")
printer_preset_def = cwd.joinpath(r"PrusaSlicer\presets\printer\def.ini")



def get_print_settings(folder,default):
    di = {}
    di.update({"default" : default.as_posix()})
    for i in folder.iterdir():
        name = Path(i).stem
        path_ = i.as_posix()
        di.update({name:path_})
    return di

print_presets = get_print_settings(prints,print_preset_def)
filament_presets = get_print_settings(filaments,filament_preset_def)
printer_presets = get_print_settings(printers,printer_preset_def)

