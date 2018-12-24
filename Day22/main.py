"""
NOT MY CODE.
Used to achieve the stars for the day, need to be redone with own code.
"""

import networkx


def neighbours(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def allowed_tools(erosion_level):
    erosion_level = erosion_level % 3
    if erosion_level == 0:
        return {1, 2}
    if erosion_level == 1:
        return {0, 1}
    if erosion_level == 2:
        return {0, 2}


def solve(depth, target):
    tx, ty = target
    grid = []

    for y in range(ty + 100):
        row = []
        for x in range(tx + 100):
            row.append(0)
        grid.append(row)

    for y in range(ty + 100):
        for x in range(tx + 100):
            if x == 0 and y == 0:
                gi = 0
            elif x == 0:
                gi = y * 48271
            elif y == 0:
                gi = x * 16807
            elif tx == x and ty == y:
                gi = 0
            else:
                gi = grid[y - 1][x] * grid[y][x - 1]
            el = (gi + depth) % 20183
            grid[y][x] = el

    G = networkx.DiGraph()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            allowed = allowed_tools(grid[y][x])
            for t1 in allowed:
                for t2 in allowed:
                    if t1 == t2:
                        continue
                    G.add_edge((x, y, t1), (x, y, t2), weight=7)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for nx, ny in neighbours(x, y):
                if nx < 0 or nx >= len(grid[0]):
                    continue
                if ny < 0 or ny >= len(grid):
                    continue
                from_erosion = grid[y][x]
                to_erosion = grid[ny][nx]
                tools = allowed_tools(from_erosion).intersection(
                    allowed_tools(to_erosion)
                )
                if (nx, ny) == (tx, ty):
                    tools = [0, 1, 2]

                for tool in tools:
                    G.add_edge((x, y, tool), (nx, ny, tool), weight=1)

    for t in [0, 1]:
        G.add_edge((tx, ty, t), (tx, ty, 2), weight=7)

    total = 0
    for y in range(ty + 1):
        for x in range(tx + 1):
            total += grid[y][x] % 3
    print(f"Total risk level for the smallest rectangle: {total}")

    shortest_path_length = networkx.dijkstra_path_length(
        G, (0, 0, 2), (tx, ty, 2)
    )
    print(f"Fewest number of minutes taken to reach the target: {shortest_path_length}")


solve(11739, (11, 718))
