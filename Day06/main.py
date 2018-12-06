from collections import Counter, defaultdict
from re import findall

input = open("input.txt").readlines()


def create_data(input):
    data = [tuple(map(int, findall("\d+", i))) for i in input]
    data_list = list(zip(*data))
    return data, data_list


# Solution for first puzzle


def largest_area(input) -> int:
    data, data_list = create_data(input)
    grid = defaultdict(lambda: -1)

    for i in range(max(data_list[0]) + 2):
        for j in range(max(data_list[1]) + 2):
            m = min(abs(i - k) + abs(j - l) for k, l in data)
            for n, (k, l) in enumerate(data):
                p = abs(i - k) + abs(j - l)
                if p == m:
                    if grid[(i, j)] != -1:
                        grid[(i, j)] = -1
                        break
                    grid[(i, j)] = n

    s = set(grid[(x, max(data_list[1]))] for x in range(max(data_list[0])))
    s = s.union(set(grid[(x, 0)] for x in range(max(data_list[0]))))
    s = s.union(
        set(grid[(max(data_list[0]), y)] for y in range(max(data_list[1])))
    )
    s = s.union(set(grid[(0, y)] for y in range(max(data_list[1]))))

    for i in Counter(grid.values()).most_common():
        if i[0] not in s:
            return i[1]
            break


assert largest_area(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]) == 17

print(f"Size of the largest area: {largest_area(input)}")

# Solution for second puzzle


def size_of_region(input, size: int = 10000) -> int:
    data, data_list = create_data(input)
    grid = {}
    for i in range(max(data_list[0]) + 2):
        for j in range(max(data_list[1]) + 2):
            grid[(i, j)] = sum(abs(i - k) + abs(j - l) for k, l in data) < size
    return sum(grid.values())


assert (
    size_of_region(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"], 32) == 16
)

print(f"Size of the region: {size_of_region(input)}")

