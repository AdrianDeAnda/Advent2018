import string

with open("input.txt") as f:
    og_polymer = f.readline()

# Solution for first puzzle


def polymer_reducer(polymer: str) -> str:
    cases = [(x + x.upper()) for x in string.ascii_lowercase] + [
        (x.upper() + x) for x in string.ascii_lowercase
    ]
    prev_len = len(polymer) + 1
    while len(polymer) < prev_len:
        prev_len = len(polymer)

        for c in cases:
            polymer = polymer.replace(c, "")

    return polymer


def length_of_polymer(data: str) -> int:
    return len(polymer_reducer(data))


assert length_of_polymer("dabAcCaCBAcCcaDA") == 10

print(f"The size of the polymer is: {length_of_polymer(og_polymer)}")

# Solution for second puzzle


def shortest_polymer(polymer: str) -> int:
    best = {}

    for c in string.ascii_lowercase:
        polymer_no_char = polymer.replace(c, "").replace(c.upper(), "")
        best[c] = length_of_polymer(polymer_no_char)

    lowest = min(best.keys(), key=(lambda k: best[k]))
    return best[lowest]


assert shortest_polymer("dabAcCaCBAcCcaDA") == 4

print(
    f"Lowest polymer achievable by removing a character: {shortest_polymer(og_polymer)}"
)
