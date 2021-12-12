from pathlib import Path
from collections import defaultdict

data_file = Path(__file__).parent.parent / "12-test-s.txt"

vertices = defaultdict(list)
for line in data_file.read_text().split("\n")[:-1]:
    v1, v2 = line.split("-")
    vertices[v1].append(v2)
    vertices[v2].append(v1)


unvisitable_verts = []
verts_to_check = ["start"]
paths_from_start = defaultdict(int)
paths_from_start["start"] = 1

while len(verts_to_check) > 0: # keep going until all vertices are checked
    new_verts_to_check = []
    for current_vert in verts_to_check:

        for neighbour in vertices[current_vert]:
            if neighbour not in unvisitable_verts:
                # add this vert's path count to all neighbour verts
                paths_from_start[neighbour] += paths_from_start[current_vert]

                # find next verts to check
                if neighbour != "end":
                    new_verts_to_check.append(neighbour)

        # if this vert is lower case, remove it from visitable verts
        if current_vert.islower():
            unvisitable_verts.append(current_vert)

    verts_to_check = new_verts_to_check


print(paths_from_start)
print(paths_from_start["end"])
