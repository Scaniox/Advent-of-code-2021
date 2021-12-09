from pathlib import Path
import re

file = Path(__file__).parent.parent / "8-input.txt"
lines = file.read_text().split("\n")[:-1]

blocks = [l.split("|") for l in lines]

known_digits = 0
for patterns, number in blocks:
    number_digits = [s.strip() for s in number.split(" ")]
    for digit in number_digits:
        known_digits += len(digit) in [2,3,4,7]


print(known_digits)
