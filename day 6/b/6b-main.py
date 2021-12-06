from pathlib import Path
from collections import Counter, defaultdict

file = Path(__file__).parent.parent / "6-input.txt"
fish_list_str = file.read_text().strip().split(",")
fish_list = [int(f) for f in fish_list_str]
fish_dict = defaultdict(int, Counter(fish_list))
fish_table = []
for i in range(9):
    fish_table.append(fish_dict[i])

fish_table_buffer = [0]*9
for day in range(256):
    fish_table_buffer = [0]*9
    fish_table_buffer[8] = fish_table_buffer[6] = fish_table[0]

    for i in range(0, 8):
        fish_table_buffer[i] += fish_table[i+1]

    fish_table = fish_table_buffer
total = sum(fish_table)

print(total)
