from pathlib import Path
import re
from numpy import array as arr, zeros, sum as np_sum

def string_to_arr(arr_string):
    board_arr = zeros([5,5])
    for line_index, line in enumerate(arr_string.split("\n")[:5]): # only first 5 lines to remove last line from final block
        line = line.strip()
        line_list = re.split("[ ]+", line)
        board_arr[line_index] = arr(line_list)

    marking_arr = zeros([5,5]) != 0
    return arr([board_arr, marking_arr])

blocks = (Path(__file__).parent.parent / "4-input.txt").read_text().split("\n\n")
random_no = list(map(int, blocks[0].split(",")))

usable_boards = list(map(string_to_arr,blocks[1:]))
usable_boards_buffer = []

for drawn_no in random_no:
    for board_index, board in enumerate(usable_boards):
        # mark number
        board[1] += board[0] == drawn_no # mark numbers matching

        # check to see if the board has won
        # columns
        win = bool(max(board[1].cumprod(axis=0)[-1]))
        # rows
        win |= bool(max(board[1].cumprod(axis=1)[:,-1]))

        if win:
            if len(usable_boards) == 1:
                unmarked_only = (board[1] == 0) * board[0]
                score = drawn_no * np_sum(unmarked_only)
                print(int(score))
                quit()
        else:
            usable_boards_buffer.append(board)

    usable_boards = usable_boards_buffer
    usable_boards_buffer = []
