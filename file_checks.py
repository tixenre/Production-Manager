from pathlib import Path

def get_suffix(file):
    return Path(file).suffix

def is_3mf(file):
    """Returns True if a file is .3mf"""
    if get_suffix(file) == ".3mf":
        return True
    else:
        return False

def is_stl(file):
    """Returns True if a file is .stl"""
    if get_suffix(file) == ".stl":
        return True
    else:
        return False

def is_gcode(file):
    """Returns True if a file is .gcode"""
    if get_suffix(file) == ".gcode":
        return True
    else:
        return False

def is_jpg(file):
    """Returns True if a file is .jpg"""
    if get_suffix(file) == ".jpg":
        return True
    else:
        return False