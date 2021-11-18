
from pathlib import Path

import parse

class FileS():

    def __init__(self,path):

        self.path=Path(path)
        self.data = parse.parse_gcode(self.path)
        self.gr = self.data["gr"]
        self.time = self.data["time"]
        self.kind = self.data["kind"]
        self.instances = self.data["instances"]


        pass


folder = Path(r"C:\Users\marti\Documents\Hola_Deco\3mf")
for file in folder.iterdir():
    if file_check.is_gcode(file):
        q = parse_gcode(file)
        print(FileS(file).__dict__)