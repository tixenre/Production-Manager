import shlex


p =  f'-g --load \presets\filament\0.2Normal.ini Sonic.3mf'

print(shlex.split(p))
