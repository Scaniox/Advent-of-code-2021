from pathlib import Path as P
from numpy import array as arr

dir_vectors = {"forward": [1,0],
               "down": [0,1],
               "up": [0,-1]}


# process input data into list
data_file = P(__file__).parent.parent / "2-input.txt"
instructions = data_file.read_text().split("\n")[:-1]

pos = arr([0,0])

for instruction in instructions:
    dir, dist = instruction.split(" ")
    pos += int(dist)*arr(dir_vectors[dir])


print(pos[0]*pos[1])
