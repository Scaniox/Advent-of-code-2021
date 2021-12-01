from pathlib import Path as P

# process input data into list
data_file = P(__file__).parent.parent / "1-input.txt"
data = [int(line) for line in open(data_file)]

window_sum = sum(data[:3])
previous_sum = sum(data[:3])
incs = 0

for i,datum in enumerate(data[3:]):
    # update window sum
    window_sum += datum
    window_sum -= data[i]

    # increase incs if window sum has increased
    if window_sum > previous_sum:
        incs += 1
    previous_sum = window_sum

print(incs)
