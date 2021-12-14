from pathlib import Path
import re
from collections import Counter, defaultdict
import time

file_text = (Path(__file__).parent.parent / "14-test.txt").read_text()
template = re.match("([A-Z]+)\n", file_text).groups()[0]
rules = re.findall("([A-Z])([A-Z]) -> ([A-Z])", file_text)
rules = {(r[0], r[1]): r[2] for r in rules}

# convert template into pairs, storing them in pairs table
pairs_counts = defaultdict(int)
item2 = template[0]
for next_item in template:
    item1 = item2
    item2 = next_item
    pairs_counts[item1+item2] += 1


for step in range(40):
    t1 = time.time()

    pairs_counts_buff = pairs_counts.copy()
    for pair, pair_count in pairs_counts.items():
        new_char = rules[pair]
        pairs_counts_buff[pair] -= pair_count
        pairs_counts_buff[pair[0]+new_char] += pair_count
        pairs_counts_buff[new_char+pair[1]] += pair_count

    pairs_counts = pairs_counts_buff


    print(f"step {step} took: {time.time() - t1}")

start_c = template[0]
end_c = template[len(template)]
for c in [start_c, end_c]:
    pair_counts[c] -= 1

for pair in pairs_counts
    pairs_counts[pair] /= 2

for c in [start_c, end_c]:
    pair_counts[c] += 1
