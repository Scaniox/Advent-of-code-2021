from pathlib import Path
import re
from collections import Counter, defaultdict
import time

file_text = (Path(__file__).parent.parent / "14-input.txt").read_text()
template = re.match("([A-Z]+)\n", file_text).groups()[0]
rules = re.findall("([A-Z][A-Z]) -> ([A-Z])", file_text)
rules = {r[0]: r[1] for r in rules}

# convert template into pairs, storing them in pairs table
pairs_counts = defaultdict(int)
for i in range(len(template)-1):
    pairs_counts[template[i]+template[i+1]] += 1

for step in range(100000):
    pairs_counts_buff = pairs_counts.copy()
    for pair, pair_count in pairs_counts.items():
        new_char = rules[pair]
        pairs_counts_buff[pair] -= pair_count
        pairs_counts_buff[pair[0]+new_char] += pair_count
        pairs_counts_buff[new_char+pair[1]] += pair_count

    pairs_counts = pairs_counts_buff


# count characters in pairs
character_counts = defaultdict(int)
for pair, count in pairs_counts.items():
    character_counts[pair[0]] += count
    character_counts[pair[1]] += count

minimum = 9* 10**99
maximum = 0

# some character are double counted
for char, count in character_counts.items():
    if char in [template[0], template[-1]]:
        ans = ((count-1)//2) + 1
    else:
        ans = count//2

    minimum = min(minimum, ans)
    maximum = max(maximum, ans)

print(int(maximum-minimum))
