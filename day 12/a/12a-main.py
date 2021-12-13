from pathlib import Path
from collections import defaultdict

def paths_to_end(vert, unvisitable_verts):
    total_paths = 0
    if vert == "end":
        return 1
        
    if vert.islower():
        unvisitable_verts = unvisitable_verts + (vert,)

    for neighbour in vertices[vert]:
        if neighbour not in unvisitable_verts:
            total_paths += paths_to_end(neighbour, unvisitable_verts)

    return total_paths



data_file = Path(__file__).parent.parent / "12-input.txt"
vertices = defaultdict(list)
for line in data_file.read_text().split("\n")[:-1]:
    v1, v2 = line.split("-")
    vertices[v1].append(v2)
    vertices[v2].append(v1)


print(paths_to_end("start", ("start",)))
