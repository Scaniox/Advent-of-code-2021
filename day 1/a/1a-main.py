from pathlib import Path as P
data_file = P(__file__).parent.parent / "1-input.txt"
print(data_file)
data = [int(line) for line in data_file.read_text().split("\n")[:-1]]

prev = 9*(10**99)
incs = 0
for datum in data:
    if datum > prev:
        incs += 1
    prev = datum

print(incs)
