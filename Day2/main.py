from collections import Counter

with open("input.txt") as n:
    input = [line.strip() for line in n]

# Solution for first puzzle

def checksum(ids, twos: int = 0, threes: int = 0):
    for n in range (0, len(ids)):
        dict = {i:ids[n].count(i) for i in ids[n]}
        if 2 in dict.values():
            twos += 1
        if 3 in dict.values():
            threes += 1
    return twos * threes

assert checksum([
    "abcdef",
    "bababc",
    "abbcde",
    "abcccd",
    "aabcdd",
    "abcdee",
    "ababab"]) == 12

print(f"The checksum is: {checksum(input)}")
