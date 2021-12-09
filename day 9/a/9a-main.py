from pathlib import Path
from numpy import array as arr, ones, roll, sum as np_sum

file = Path(__file__).parent.parent / "9-input.txt"
data_list = [list(line) for line in file.read_text().split("\n")[:-1]]
data = arr(data_list, dtype = int)

floor_arr = ones((data.shape + arr((2,2)))) * 9
floor_arr[1:-1,1:-1] = data

minimums_mask = ones(floor_arr.shape)

sides = [(1,0), (-1,0), (1, 1), (-1,1)]
for offset, axis in sides:
    minimums_mask *= floor_arr < roll(floor_arr, offset, axis)

risk_factors = (minimums_mask*(floor_arr+ones(floor_arr.shape)))

print(int(np_sum(risk_factors)))
