from pathlib import Path

brackets = {"(" : ")",
            "[" : "]",
            "{" : "}",
            "<" : ">"}

bracket_scores = {"(" : 1,
                 "[" : 2,
                 "{" : 3,
                 "<" : 4}

file = Path(__file__).parent.parent / "10-input.txt"
lines = [l.strip() for l in file.read_text().split("\n")[:-1]]

autocomplete_scores = []
for line in lines:
    stack = []
    corrupted_line = False
    for c in line:
        if c in brackets.keys():
            stack.append(c)
        elif c in brackets.values():
            if len(stack) == 0 or brackets[stack.pop(-1)] != c:
                #sytax error discovered
                corrupted_line = True
                break
        else:
            print("non bracket data")

    if corrupted_line:
        continue
    # stack contains remaining characters
    line_score = 0
    for bracket in stack[::-1]: # remove each bracket from stack
            line_score *= 5
            line_score += bracket_scores[bracket]

    autocomplete_scores.append(line_score)

middle = sorted(autocomplete_scores)[len(autocomplete_scores)//2]

print(middle)
