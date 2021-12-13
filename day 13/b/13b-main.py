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
                txt += "\u001b[37m■"
            else:
                txt += "\u001b[30m■"
    txt += "\u001b[0m"
    print(txt)


file_text = (Path(__file__).parent.parent / "13-input.txt").read_text()
point_coords = [[int(x), int(y)] for (x,y) in re.findall("([0-9]+),([0-9]+)", file_text)]
instructions = [(a, int(o)) for a, o in re.findall("fold along ([xy])=([0-9]+)", file_text)]

for axis_s, fold in instructions:
    axis = axis_s == "y"
    for point_i, point in enumerate(point_coords):
        if point[axis] > fold:
            point[axis] = fold - (point[axis] - fold)

visible_points = []
for point in point_coords:
    if point not in visible_points:
        visible_points.append(point)


# plot point on a matrix
width = max(visible_points, key=lambda p:int(p[0]))[0]
height = max(visible_points, key=lambda p:int(p[1]))[1]
paper_arr = zeros((int(height)+1, int(width)+1))

for x, y in visible_points:
    paper_arr[int(y), int(x)] = 1

print_arr(paper_arr)
