from pathlib import Path
from numpy import array as arr, zeros
from collections import Counter
import re


def print_arr(array):
    txt = ""
    for y in range(array.shape[0]):
        txt += "\n"
        for x in range(array.shape[1]):
            if array[y,x]:
                txt += "\u001b[37m 1"
            else:
                txt += "\u001b[30m 0"
    txt += "\u001b[0m"
    print(txt)

file_text = (Path(__file__).parent.parent / "13-input.txt").read_text()
point_coords = [[int(x), int(y)] for (x,y) in re.findall("([0-9]+),([0-9]+)", file_text)]
instructions = [(a, int(o)) for a, o in re.findall("fold along ([xy])=([0-9]+)", file_text)]


for axis_s, fold in instructions[:1]:
    axis = axis_s == "y"
    for point_i, point in enumerate(point_coords):
        if point[axis] > fold:
            point[axis] = fold - (point[axis] - fold)

visible_points = []
for point in point_coords:
    if point not in visible_points:
        visible_points.append(point)

print(len(visible_points))
