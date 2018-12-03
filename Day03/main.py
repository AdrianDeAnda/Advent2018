import re
import numpy as np

with open("input.txt") as n:
    input = [line.strip() for line in n]

regex = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

# Solution for firts puzzle


def split_input(list):
    split = [int(x) for x in re.match(regex, list).groups()]
    return split


def count_overlapped(new_matrix, height, width, overlapped: int = 0):
    for i in range(0, height):
        for j in range(0, width):
            if new_matrix[j][i] == -1:
                overlapped += 1
    return overlapped


def fill_matrix(data, height: int = 1000, width: int = 1000):
    matrix = np.zeros((height, width))
    for i in range(len(data)):
        rectangle = split_input(data[i])
        for x in range((rectangle[1]), (rectangle[1] + rectangle[3])):
            for y in range((rectangle[2]), (rectangle[2] + rectangle[4])):
                if matrix[y][x] == 0:
                    matrix[y][x] = rectangle[0]
                elif matrix[y][x] != 0:
                    matrix[y][x] = -1
    return count_overlapped(matrix, height, width)


assert (
    fill_matrix(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 8, 8) == 4
)

print(f"Number of square inches in other claims: {fill_matrix(input)}")
