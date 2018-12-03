import re
import numpy as np

with open("input.txt") as n:
    input = [line.strip() for line in n]

regex = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"


def split_input(list):
    return [int(x) for x in re.match(regex, list).groups()]


def create_matrix(data, height, width):
    new_matrix = np.zeros((height, width))
    for i in range(len(data)):
        rectangle = split_input(data[i])
        for x in range((rectangle[1]), (rectangle[1] + rectangle[3])):
            for y in range((rectangle[2]), (rectangle[2] + rectangle[4])):
                if new_matrix[y][x] == 0:
                    new_matrix[y][x] = rectangle[0]
                elif new_matrix[y][x] != 0:
                    new_matrix[y][x] = -1
    return new_matrix


# Solution for first puzzle


def count_overlapped(data, height: int = 1000, width: int = 1000):
    matrix = create_matrix(data, height, width)
    unique, counts = np.unique(matrix, return_counts=True)
    values = dict(zip(unique, counts))
    return values[-1]


assert (
    count_overlapped(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 8, 8)
    == 4
)


print(f"Number of square inches in other claims: {count_overlapped(input)}")

# Solution for second puzzle


def clean_claim(data, height: int = 1000, width: int = 1000):
    claim_matrix = create_matrix(data, height, width)
    unique, counts = np.unique(claim_matrix, return_counts=True)
    values = dict(zip(unique, counts))
    for i in range(len(data)):
        rectangle = split_input(data[i])
        square_inches = rectangle[3] * rectangle[4]
        if rectangle[0] in values and values[rectangle[0]] == square_inches:
            return rectangle[0]


assert (
    clean_claim(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 8, 8) == 3
)

print(f"Claim ID that doesn't overlap: {clean_claim(input)}")
