import re
import glob
import os

files = glob.glob("*.png")
for file in files:
     m = re.match('button_.*_48px', file)
     dst = file[m.start():m.end()]
     os.rename(file, dst + ".png")