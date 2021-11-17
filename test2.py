
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


file = Path(r"C:\Users\marti\Documents\GitHub\Production-Manager\gcode\Mickey Navidad Bola - (1h28m) (18.3833gr) (0.3mm) (PLA) (0.4) (17-11).gcode")

print(FileS(file).__dict__)