from pathlib import Path as P


data_file = P(__file__).parent.parent / "3-input.txt"
lines = data_file.read_text().split("\n")[:-1]

file_data = []
for line in lines:
    file_data.append([int(c) for c in line])

answers = [0,0]
for select_most_common in[False,True]:
    data = file_data.copy()
    for digit_index in range(0,11):
        # identify if 1 or 0 is the most common
        total = 0
        for number in data:
            total += number[digit_index]

        # choose if numbers must have a 1 or 0 in this digit to stay
        if total == len(data)/2: # same number of 1s and 0s for this digit
            if select_most_common:
                select_bit = 1
            else:
                select_bit = 0
        else: # different number of 1s and 0s
            if select_most_common:
                select_bit = round(total/len(data))
            else:
                select_bit = 1-round(total/len(data))

        # keep only wanted numbers (removing unwanted ones from data causes problems)
        save = []
        for number in data:
            if number[digit_index] == select_bit:
                save.append(number)
        data = save.copy()

        if len(data) == 1:
            break
    answers[select_most_common] = int("".join([str(c) for c in data[0]]), base = 2)

print(answers[0]*answers[1])
