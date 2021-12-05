from pathlib import Path
from numpy import array as arr, zeros, sum as np_sum
import re

def draw_line(line_data, screen):#increments entries on screen in the line
    x1, y1, x2, y2 = line_data

    if y1 == y2: # horizontal line
        if x2 < x1: # ensure x2 > x1
            x1, x2 = x2, x1
        y = y1
        for x in range(x1,x2+1):
            screen[y,x] += 1

    elif x1 == x2: # vertical line
        if y2 < y1: # ensure y2 > y1
            y1, y2 = y2, y1
        x = x1
        for y in range(y1, y2+1):
            screen[y,x] += 1
    else: # diagonal line
        if x2 < x1: # ensure x2 > x1 (line slopes right)
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        if y2 > y1: # line slopes right and down
            for i in range(0, x2-x1+1):
                screen[y1+i,x1+i] += 1
        else: # line slopes right and up
            for i in range(0, x2-x1+1):
                screen[y1-i,x1+i] += 1


input_path = Path(__file__).parent.parent / "5-input.txt"
input_lines = input_path.read_text().split("\n")[:-1]

data_match_str = "([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)"
line_data_str = [re.match(data_match_str, line).groups() for line in input_lines]
line_data_ints = [[int(d) for d in line] for line in line_data_str]

vent_screen = zeros([1000,1000])
for line in line_data_ints:
    draw_line(line, vent_screen)

overlap_count = np_sum(vent_screen >= 2)

print(overlap_count)
