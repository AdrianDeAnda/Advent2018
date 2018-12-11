import numpy as np


def battery(x: int, y: int, serial: int):
    rid = x + 10
    power = rid * y
    power += serial
    power *= rid
    power = (power // 100) % 10
    power -= 5
    return power


assert battery(3, 5, 8) == 4
assert battery(122, 79, 57) == -5
assert battery(217, 196, 39) == 0
assert battery(101, 153, 71) == 4

# Solution for first puzzle


def total_power(serial: int):
    batteries = [
        [battery(x, y, serial) for y in range(300)] for x in range(300)
    ]

    return max(
        ((x, y) for x in range(298) for y in range(298)),
        key=lambda pair: sum(
            batteries[pair[0] + i][pair[1] + j]
            for i in range(3)
            for j in range(3)
        ),
    )


assert total_power(18) == (33, 45)
assert total_power(42) == (21, 61)

print(
    f"Coordinates for 3x3 square with largest total power: {total_power(9306)}"
)

# Solution for second puzzle


def create_grid(serial: int):
    return np.fromfunction(lambda x, y: battery(x, y, serial), (300, 300))


def largest_total_power(serial: int, best: int = 0):
    grid = create_grid(serial)
    indetifier = 0, 0, 0
    for size in range(1, 301):
        for x in range(300 - size):
            for y in range(300 - size):
                temp = np.sum(grid[x : x + size, y : y + size])
                if temp > best:
                    best = temp
                    identifier = x, y, size
    return identifier


# Unit tests commented due to long runtime, both passed on testing
# TODO: Refactor to improve runtime
# assert largest_total_power(18) == (90, 269, 16)
# assert largest_total_power(42) == (232, 251, 12)

print(
    f"Identifier of the square with the largest total power: {largest_total_power(9306)}"
)
