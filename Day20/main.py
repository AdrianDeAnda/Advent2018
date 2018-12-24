import networkx

paths = open("input.txt").read()[1:-1]
maze = networkx.Graph()

pos = {0}
stack = []
starts, ends = {0}, set()

for c in paths:
    if c == "|":
        ends.update(pos)
        pos = starts
    elif c in "NESW":
        direction = {"N": 1, "E": 1j, "S": -1, "W": -1j}[c]
        maze.add_edges_from([(p, p + direction) for p in pos])
        pos = {p + direction for p in pos}
    elif c == "(":
        stack.append((starts, ends))
        starts, ends = pos, set()
    elif c == ")":
        starts, ends = stack.pop()
        ends.update(pos)

shortest = networkx.algorithms.shortest_path_length(maze, 0)

print(
    f"Largest number of doors required to pass through to reach a room: {max(shortest.values())}"
)
print(
    f"Shortest path from current location that pass through at least 1000 doors: {len([length for length in shortest.values() if length >= 1000])}"
)

