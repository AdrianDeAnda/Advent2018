import re

puzzle = open("input.txt").read().strip().splitlines()


def ints(s: str):
    return list(map(int, re.findall(r"-?\d+", s)))


def psub(x, y):
    if len(x) == 2:
        return [x[0] - y[0], x[1] - y[1]]
    return [a - b for a, b in zip(x, y)]


def pdist1(x, y=None):
    if y is not None:
        x = psub(x, y)
    if len(x) == 2:
        return abs(x[0]) + abs(x[1])
    return sum(map(abs, x))


class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [None] * n
        self.ranks = [1] * n
        self.num_sets = n

    def find(self, i: int) -> int:
        p = self.parents[i]
        if p is None:
            return i
        p = self.find(p)
        self.parents[i] = p
        return p

    def in_same_set(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)

    def merge(self, i: int, j: int) -> None:
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return

        i_rank = self.ranks[i]
        j_rank = self.ranks[j]

        if i_rank < j_rank:
            self.parents[i] = j
        elif i_rank > j_rank:
            self.parents[j] = i
        else:
            self.parents[j] = i
            self.ranks[i] += 1
        self.num_sets -= 1


to_i = dict()
uf = UnionFind(len(puzzle))

for i, line in enumerate(puzzle):
    p = tuple(ints(line))
    to_i[p] = i

    for point in to_i:
        if pdist1(p, point) <= 3:
            uf.merge(i, to_i[point])

print(f"Constellations formed by the fixed points in spacetime: {uf.num_sets}")
