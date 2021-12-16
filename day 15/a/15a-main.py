from pathlib import Path
from numpy import array as arr, ones, roll, sum as np_sum
import heapq
from collections import defaultdict

sides = [(0,-1), (1,0), (0,1), (-1,0)]

file = Path(__file__).parent.parent / "15-input.txt"
data_list = [list(line) for line in file.read_text().split("\n")[:-1]]
data = arr(data_list, dtype = int)

def print_checked():
    text = ""
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            if path[(y,x)][0] < 99999999:
                text += f"\u001b[34m{data[y,x]}\u001b[0m"
            else:
                text += f"\u001b[37m{data[y,x]}\u001b[0m"
        text += "\n"

    print(text)

nodes_to_search = [(0,(0,0))] # priority_score, prev_pos
path = defaultdict(lambda: (99999999, (-1,-1)) ) # pos : (risk, previous_node)
path[(0,0)] = (0, (-1,-1))

while len(nodes_to_search):
    current_priority, current_pos = heapq.heappop(nodes_to_search)
    current_risk = path[current_pos][0]
    #print_checked()
    #print(f"current_node: {current_pos}, current_risk: {current_risk}")
    for side in sides:
        neighbour_pos = tuple(current_pos[i]+side[i] for i in [0,1])
        # only check neighbours actually on the board
        if min([0 <= neighbour_pos[i] < data.shape[i] for i in [0,1]]):
            neighbour_risk = current_risk + data[neighbour_pos]
            #print(f"neighbour: {neighbour_pos}, risk: {neighbour_risk}")

            M_dist_to_end = sum([data.shape[i]-neighbour_pos[i] for i in [0,1]])
            priority_score = neighbour_risk + M_dist_to_end

            if neighbour_risk < path[neighbour_pos][0]:
                    heapq.heappush(nodes_to_search, (priority_score, neighbour_pos))
                    path[neighbour_pos] = (neighbour_risk, current_pos)

print(path[(len(data)-1,)*2][0])
