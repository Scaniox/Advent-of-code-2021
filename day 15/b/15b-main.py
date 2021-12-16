from pathlib import Path
from numpy import array as arr, zeros, round_
import heapq
from collections import defaultdict

sides = [(0,-1), (1,0), (0,1), (-1,0)]

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


file = Path(__file__).parent.parent / "15-input.txt"
data_list = [list(line) for line in file.read_text().split("\n")[:-1]]
small_data = arr(data_list, dtype = int)

# tile maze
data = zeros(arr(small_data.shape) * 5)

for y in range(5):
    for x in range(5):
        data[y*small_data.shape[0] : (y+1)*small_data.shape[0],\
             x*small_data.shape[1] : (x+1)*small_data.shape[1]] \
        = ((small_data + (x+y)) - 1) % 9 + 1

nodes_to_search = [(0,(0,0))] # priority_score, prev_pos
path = defaultdict(lambda: 99999999) # pos : risk
path[(0,0)] = 0

while len(nodes_to_search):
    current_priority, current_pos = heapq.heappop(nodes_to_search)
    current_risk = path[current_pos]
    #print_checked()
    #print(f"current_node: {current_pos}, current_risk: {current_risk}")
    for side in sides:
        neighbour_pos = tuple(current_pos[i]+side[i] for i in [0,1])
        # only check neighbours actually on the board
        if min([0 <= neighbour_pos[i] < data.shape[i] for i in [0,1]]):
            neighbour_risk = current_risk + data[neighbour_pos]
            M_dist_to_end = sum([data.shape[i]-neighbour_pos[i] for i in [0,1]])
            priority_score = neighbour_risk + M_dist_to_end
            #print(f"neighbour: {neighbour_pos}, risk: {neighbour_risk}")

            if neighbour_risk < path[neighbour_pos]:
                    heapq.heappush(nodes_to_search, (priority_score, neighbour_pos))
                    path[neighbour_pos] = (neighbour_risk)

print(round(path[(len(data)-1,)*2]))
