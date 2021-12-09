from pathlib import Path
import re

def resolve_number(pattern_digits, number_digits):
    numbers_to_wires = {} # number: wire set
    wires_to_numbers = {} # wire set : number
    digit_sets = [frozenset(s) for s in pattern_digits[:-1].split(" ")]
    fives = [] # five elements: 2, 3, 5
    sixes = [] # six elements: 0, 6, 9

    for digit_set in digit_sets:
        match len(digit_set):
            case 2:
                numbers_to_wires[1] = digit_set
                wires_to_numbers[digit_set] = 1
            case 3:
                numbers_to_wires[7] = digit_set
                wires_to_numbers[digit_set] = 7
            case 4:
                numbers_to_wires[4] = digit_set
                wires_to_numbers[digit_set] = 4
            case 7:
                numbers_to_wires[8] = digit_set
                wires_to_numbers[digit_set] = 8
            case 5:
                fives.append(digit_set)
            case 6:
                sixes.append(digit_set)
            case x:
                print(f"odd length; {x}")

    #sixes
    for digit_set in sixes:
        if digit_set & numbers_to_wires[4] == numbers_to_wires[4]:# six that contains 7 is 9
            numbers_to_wires[9] = digit_set
            wires_to_numbers[digit_set] = 9
        elif not(digit_set & numbers_to_wires[1] == numbers_to_wires[1]): # six that doesn't contain 1 is 6
            numbers_to_wires[6] = digit_set
            wires_to_numbers[digit_set] = 6
        else:
            numbers_to_wires[0] = sixes[0] # 0 is remaining six
            wires_to_numbers[digit_set] = 0


    #fives
    for digit_set in fives:
        if digit_set & numbers_to_wires[1] == numbers_to_wires[1]: # five that contains 1 is 3
            numbers_to_wires[3] = digit_set
            wires_to_numbers[digit_set] = 3
        elif  len(digit_set & numbers_to_wires[6]) == 5:# 5 shares 5 elements with 6
            numbers_to_wires[5] = digit_set
            wires_to_numbers[digit_set] = 5
        else:
            numbers_to_wires[2] = digit_set # 2 is the remaining 5
            wires_to_numbers[digit_set] = 2

    # resolve number
    number_digit_sets = [frozenset(s) for s in number_digits.split(" ")[1:]]
    number = 0
    for i, digit_set in enumerate(number_digit_sets):
        number += wires_to_numbers[digit_set] * (10**(3-i))

    return number



file = Path(__file__).parent.parent / "8-input.txt"
lines = file.read_text().split("\n")[:-1]

blocks = [l.split("|") for l in lines]

total = 0
for patterns, number in blocks:
    total += resolve_number(patterns, number)


print(total)
