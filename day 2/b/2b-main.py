from pathlib import Path as P
from numpy import array as arr

# process input data into list
data_file = P(__file__).parent.parent / "2-input.txt"
instructions = data_file.read_text().split("\n")[:-1]

pos = arr([0,0])
aim = 0

for instruction in instructions:
    direction, dist = instruction.split(" ")
    dist = int(dist)

    if direction == "down":
        aim += dist
    elif direction == "up":
        aim -= dist

    if direction == "forward":
        pos += dist*arr([1,aim])


print(pos[0]*pos[1])
