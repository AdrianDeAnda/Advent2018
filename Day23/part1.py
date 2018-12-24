import numpy as np
import re

with open("input.txt") as f:
    puzzle = f.read().splitlines()

re_str = "<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)"


def nanobots(data, count: int = 0):
    max_r = -float("inf")
    max_point = None

    for line_i, line in enumerate(data):
        x, y, z, r = [int(i) for i in re.search(re_str, line).groups()]
        if r > max_r:
            max_r = r
            max_point = np.array([x, y, z])

    for line_i, line in enumerate(data):
        x, y, z, r = [int(i) for i in re.search(re_str, line).groups()]

        new_point = np.array([x, y, z])
        if np.sum(np.abs(new_point - max_point)) <= max_r:
            count += 1
    return count


print(f"Nanobots are in range of its signals: {nanobots(puzzle)}")
