from pathlib import Path
from numpy import array as arr, zeros, ones, roll, sum as np_sum

sides = [(-1,-1),(0,-1),(1,-1),
        (-1,0),(1,0),
        (-1,1),(0,1),(1,1)]

file = Path(__file__).parent.parent / "11-input.txt"
data_list = [list(line) for line in file.read_text().split("\n")[:-1]]
data = arr(data_list, dtype = int)
energies = zeros(data.shape+arr((2,2)))
energies[1:-1,1:-1] = data

edge_mask = zeros(energies.shape)
edge_mask[1:-1,1:   -1] = ones(data.shape)

total_flashes = 0
for step in range(1,101):

    energies += 1
    not_flashed = ones(energies.shape)

    while True:
        to_flash = not_flashed *( energies > 9)
        for offset in sides:
            energies += roll(to_flash, offset, axis=(0,1))
        not_flashed *= 1-to_flash
        energies *= edge_mask

        if not(to_flash.any()): # no changes
            break

    total_flashes += np_sum(energies > 9)
    energies = energies * (energies <= 9)


print(total_flashes)
