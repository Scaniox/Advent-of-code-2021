from pathlib import Path
from numpy import array as arr, sum as npsum

data_file = Path(__file__).parent.parent / "7-input.txt"
data = arr(data_file.read_text()[:-1].split(","), dtype = int)

print(data)
minimum_middle = 0
minimum_fuel = 1000000000
for middle in range(len(data)):
    # fuel used = (n*(n+1))/2 for n units moved
    distances = abs(data-middle)
    total_fuel = npsum(distances*(distances+1)/2)
    if total_fuel < minimum_fuel:
        minimum_fuel = total_fuel
        minimum_middle = middle


print(int(minimum_fuel))
