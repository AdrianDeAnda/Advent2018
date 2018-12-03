from collections import Counter

with open("input.txt") as n:
    input = [line.strip() for line in n]

# Solution for first puzzle


def checksum(ids, twos: int = 0, threes: int = 0):
    for n in range(len(ids)):
        dict = Counter(ids[n])
        if 2 in dict.values():
            twos += 1
        if 3 in dict.values():
            threes += 1
    return twos * threes


assert (
    checksum(
        ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
    )
    == 12
)

print(f"The checksum is: {checksum(input)}")

# Solution for second puzzle


def common_letters(ids):
    common_dict = Counter()
    for box_id in ids:
        for n in range(len(box_id)):
            delete_one = tuple(box_id[:n] + "_" + box_id[(n + 1) :])
            common_dict[delete_one] += 1
    [(top, count), (bot, bot_count)] = common_dict.most_common(2)
    return "".join([c for c in top if c != "_"])


assert (
    common_letters(
        ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
    )
    == "fgij"
)

print(f"The common letters are: {common_letters(input)}")
