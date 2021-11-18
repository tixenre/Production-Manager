import tkinter as tk
from tkinter import filedialog
from pathlib import Path

import sys

sys.path.append(r'C:\Users\marti\Documents\GitHub\Production-Manager')

import slicer
import parse
import file_check


row_count = iter(list(range(1,51)))
row_current = next(row_count)



