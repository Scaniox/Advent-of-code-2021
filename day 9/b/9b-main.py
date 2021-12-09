from pathlib import Path
from numpy import array as arr, zeros, ones, roll, sum as np_sum
import time
from collections import Counter

t1 = time.time()

file = Path(__file__).parent.parent / "9-input.txt"
data_list = [list(line) for line in file.read_text().split("\n")[:-1]]
data = arr(data_list, dtype = int)

floor_arr = ones((data.shape + arr((2,2)))) * 9
floor_arr[1:-1,1:-1] = data

sides = [(1,0), (-1,0), (1, 1), (-1,1)]

minimums_mask = ones(floor_arr.shape)
for offset, axis in sides:
    minimums_mask *= floor_arr < roll(floor_arr, offset, axis)

not_nines_mask = floor_arr != 9

# place unique number (seed) at every minimum
seeds_arr = arr(range(1,floor_arr.size+1)).reshape(floor_arr.shape)
basins_arr = seeds_arr * minimums_mask
used_seeds = Counter(basins_arr.flatten())
del used_seeds[0]

# flood fill seeds, & masking with not_nines_mask to isolate basins
for loops in range(10):
    for offset, axis in sides:
        rolled = roll(basins_arr, offset, axis)
        basins_arr += rolled * (rolled != basins_arr)
        basins_arr *= not_nines_mask

# find size of each basin by summing equal to seed / seed
basin_sizes = [np_sum(basins_arr == seed) for seed in used_seeds]
basin_sizes.sort()

t2 = time.time()

print(basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3])
print(f"time taken: {round(t2-t1, 5)}s")
