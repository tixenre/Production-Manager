import subprocess
import time
from os import remove
import project_path as pp
import file_check 

def do_slice(file,**kwargs):

    if kwargs.get("print_set"):
        print_set = kwargs.get("print_set")
    else:
        print_set = pp.print_preset_def
    if kwargs.get("filament_set"):
        filament_set = kwargs.get("filament_set")
    else:
        filament_set = pp.filament_preset_def
    if kwargs.get("printer_set"):
        printer_set = kwargs.get("printer_set")
    else:
        printer_set = pp.print_preset_def

    if (kwargs and file_check.is_3mf(file)) or file_check.is_stl(file):
        settings = f'{pp.slicer_console}  -g {file} --load {print_set} --load {filament_set} --load {printer_set}'

    elif not kwargs and file_check.is_3mf(file):
        settings = f'{pp.slicer_console}  -g {file}'


    file_name = file_check.get_file_name(file)
    print("")
    print(f'Slicing: {file_name}')
    t1 = time.perf_counter()
    subprocess.call(settings)
    t2 = time.perf_counter()
    time_elapse = round(t2-t1,2)
    print(f'Done slicing {file_name} in {time_elapse} seconds')

# def slice_folder(folder):
#     for file in folder.iterdir():
#         if file_check.is_gcode(file):
#             remove(file)
#         elif file_check.is_3mf(file):   
#             do_slice(file)


# file_to_slice = Path(pp.folder_3mf / "Sonic.3mf")
# stl_to_slice = Path(pp.folder_3mf / "Sonic.stl")

# slice_folder(pp.folder_3mf)
# slice_folder(Path(r"C:\Users\marti\Documents\Hola_Deco\3mf"))

# do_slice(Path(r"C:\Users\marti\Documents\GitHub\Production-Manager\3mf\Stand_Celular_Cargador.3mf"))
# do_slice(Path(r"C:\Users\marti\Documents\GitHub\Production-Manager\3mf\Robert_Plant.3mf"))

