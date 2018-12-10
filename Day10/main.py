import re
import numpy as np

input = np.array(
    [
        [int(i) for i in re.findall("-?\d+", line)]
        for line in open("input.txt").readlines()
    ]
)

# Solution for both puzzles


def get_message_and_time(d, size: int = 20000):
    x, y, t = [], [], []
    for i in range(size):
        x.append((d[:, 0] + i * d[:, 2]).max() - (d[:, 0] + i * d[:, 2]).min())
        y.append((d[:, 1] + i * d[:, 3]).max() - (d[:, 1] + i * d[:, 3]).min())
        t.append(x[i] * y[i])
    t = t.index(min(t))
    return x[t] + 1, y[t] + 1, t


def create_message(data):
    mssg_x, mssg_y, time = get_message_and_time(data)
    data[:, :2] += time * data[:, 2:]
    data[:, 0] -= data[:, 0].min()
    data[:, 1] -= data[:, 1].min()
    grid = np.zeros((mssg_y, mssg_x), dtype=int)

    for j in range(data.shape[0]):
        grid[data[j, 1], data[j, 0]] = 1

    for j in range(mssg_y):
        print("".join("#" if p else " " for p in grid[j]))

    return time


print("The message is:\n")
print(f"\nIt took {create_message(input)} seconds to appear in the sky.")
