from pathlib import Path
from collections import defaultdict

def paths_to_end(vert, visit_counts, doubled_vert, path):
    if vert == "end":
        return 1

    total_paths = 0
    visit_counts = visit_counts.copy()
    visit_counts[vert] += 1
    path = path + (vert,)

    for neighbour in vertices[vert]:
        if neighbour.isupper() \
         or visit_counts[neighbour] < 1 \
         or neighbour == doubled_vert and visit_counts[neighbour] < 2:
            total_paths += paths_to_end(neighbour, visit_counts, doubled_vert, path)

    return total_paths



data_file = Path(__file__).parent.parent / "12-input.txt"
vertices = defaultdict(list)
for line in data_file.read_text().split("\n")[:-1]:
    v1, v2 = line.split("-")
    vertices[v1].append(v2)
    vertices[v2].append(v1)

visit_counts = defaultdict(int)

no_doubled_paths = paths_to_end("start", visit_counts, "Null", tuple())
total_paths = no_doubled_paths
for doubled_vert in vertices:
    if doubled_vert.islower() and doubled_vert not in ["start", "end"]:
        total_paths += paths_to_end("start", visit_counts, doubled_vert, tuple()) - no_doubled_paths

print(total_paths)
