from pathlib import Path as P


data_file = P(__file__).parent.parent / "3-input.txt"
data = data_file.read_text().split("\n")[:-1]

total = [0.0]*12

for datum in data:
    for index, digit in enumerate(datum):
        if(digit == "1"):
            total[index] += 1
data_len = len(data)
total = [d/data_len for d in total]
gamma = int("".join([str(round(d)) for d in total]), base = 2)
epsilon = int("".join([str(round(1-d)) for d in total]), base = 2)

print(f"gamma: {gamma}, epsilon: {epsilon}, result: {gamma*epsilon}")
