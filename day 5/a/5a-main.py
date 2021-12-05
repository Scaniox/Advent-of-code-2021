from pathlib import Path
from numpy import array as arr, zeros, sum as np_sum
import re

def draw_line(line_data, screen):#increments entries on screen in the line
    x1, y1, x2, y2 = line_data
    # ensure x2 y2 are the larger values
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1

    if y1 == y2: # horizontal line
        print("horiz")
        y = y1
        for x in range(x1,x2+1):
            screen[y,x] += 1

    elif x1 == x2: # vertical line
        print("vert")
        x = x1
        for y in range(y1, y2+1):
            screen[y,x] += 1
    else:
        pass

input_path = Path(__file__).parent.parent / "5-input.txt"
input_lines = input_path.read_text().split("\n")[:-1]

data_match_str = "([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)"
line_data_str = [re.match(data_match_str, line).groups() for line in input_lines]
line_data_ints = [[int(d) for d in line] for line in line_data_str]

vent_screen = zeros([1000,1000])
for line in line_data_ints:
    draw_line(line, vent_screen)

overlap_count = np_sum(vent_screen >= 2)

print(vent_screen)
print(overlap_count)
