from pathlib import Path
from numpy import array as arr
import re

file_text = (Path(__file__).parent.parent / "13-test.txt").read_text()
point_coords = re.match("([0-9]+,[0-9]+)", file_text)
instructions = re.match("(fold along [xy]=[0-9]+)", file_text)

print(point_coords)
print(instructions)
