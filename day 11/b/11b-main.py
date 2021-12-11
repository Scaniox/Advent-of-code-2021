from pathlib import Path
from numpy import array as arr, zeros, ones, roll, sum as np_sum
import time

sides = [(-1,-1),(0,-1),(1,-1),
        (-1,0),(1,0),
        (-1,1),(0,1),(1,1)]

file = Path(__file__).parent.parent / "11-input.txt"
data_list = [list(line) for line in file.read_text().split("\n")[:-1]]
data = arr(data_list, dtype = int)
energies = zeros(data.shape+arr((2,2)))
energies[1:-1,1:-1] = data

edge_mask = zeros(energies.shape)
edge_mask[1:-1,1:-1] = ones(data.shape)

step = 0
while True:
    step += 1

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

    if (energies[1:-1,1:-1] > 9).all():
        print(f"all flashed on step {step}")
        break
    energies = energies * (energies <= 9)

    #print(f"\nafter step{step}:\n{energies}")
