from pathlib import Path

brackets = {"(" : ")",
            "[" : "]",
            "{" : "}",
            "<" : ">"}

bracket_scores = {")" : 3,
                 "]" : 57,
                 "}" : 1197,
                 ">" : 25137}

file = Path(__file__).parent.parent / "10-input.txt"
lines = [l.strip() for l in file.read_text().split("\n")[:-1]]

syntax_score = 0
for line in lines:
    stack = []
    for c in line:
        if c in brackets.keys():
            stack.append(c)
        elif c in brackets.values():
            if len(stack) == 0 or brackets[stack.pop(-1)] != c:
                syntax_score += bracket_scores[c] #sytax error discovered
                break
        else:
            print("non bracket data")

print(syntax_score)
