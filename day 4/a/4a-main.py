from pathlib import Path
import re
from numpy import array as arr, zeros, invert, sum as np_sum

def string_to_arr(arr_string):
    board_arr = zeros([5,5])
    for line_index, line in enumerate(arr_string.split("\n")):
        line = line.strip()
        line_list = re.split("[ ]+", line)
        board_arr[line_index] = map(int, line_list)

    marking_arr = zeros([5,5]) == 0
    return arr([board_arr, marking_arr])

blocks = (Path(__file__).parent.parent / "4-input.txt").read_text().split("\n\n")
random_no = list(map(int, blocks[0].split(",")))

boards = list(map(string_to_arr,blocks[1:]))

print(string_to_arr(blocks[1]))
for drawn_no in random_no:
    for board in boards:
        # mark number
        board[1] |= board[0] == drawn_no

        # check to see if the board has won
        # columns
        win = min(board[1].cumprod(axis=0)[-1])
        # rows
        win |= min(board[1].cumprod(axis=1)[:,-1])

        if win:
            unmarked_only = invert(board[1]) * board[0]
            score = drawn_no * np_sum(unmarked_only)
