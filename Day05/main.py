with open("input.txt") as f:
    og_polymer = f.readline()

# Solution for first puzzle

def same_character(str1: str, str2: str) -> bool:
    return str1.lower() == str2.lower()


def polymer_reducer(data: str, reduced=True):
    polymer = data
    while reduced:
        reduced = False

        for i in range(1, len(polymer)):
            char1 = polymer[i - 1]
            char2 = polymer[i]
            if same_character(char1, char2) and char1 != char2:
                polymer = polymer[: i - 1] + polymer[i + 1 :]
                reduced = True
                break

    return polymer


def length_of_polymer(data: str):
    return len(polymer_reducer(data))


assert length_of_polymer("dabAcCaCBAcCcaDA") == 10

# print(f"The size of the polymer is: {length_of_polymer(og_polymer)}")

# Solution for second puzzle

def shortest_polymer(polymer: str):
    characters = {c.lower() for c in polymer}
    best = {}

    for c in characters:
        polymer_no_char = polymer.replace(c, "").replace(c.upper(), "")
        best[c] = length_of_polymer(polymer_no_char)

    lowest = min(best.keys(), key=(lambda k: best[k]))
    return best[lowest]


assert shortest_polymer("dabAcCaCBAcCcaDA") == 4

# print(
#     f"Lowest polymer achievable by removing a character: {shortest_polymer(og_polymer)}"
# )

# Only assertions are being run as polymer_reducer takes a shit load of time
# to run and takes an eternity to get answers. Function should be optimized.

# TODO:
# 1. Fix the polymer_reducer function
