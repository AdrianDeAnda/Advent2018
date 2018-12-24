import numpy as np

from collections import defaultdict

with open("input.txt") as f:
    puzzle = np.array(
        [[y for y in x] for x in f.read().splitlines()], dtype=np.character
    )

scores = defaultdict(set, {})

for i in range(1_000_000_000):
    nd = puzzle.copy()
    for x in range(puzzle.shape[0]):
        for y in range(puzzle.shape[1]):
            if puzzle[x, y] == b".":
                if (
                    np.count_nonzero(
                        puzzle[max(0, x - 1) : x + 2, max(0, y - 1) : y + 2]
                        == b"|"
                    )
                    >= 3
                ):
                    nd[x, y] = b"|"
            elif puzzle[x, y] == b"|":
                if (
                    np.count_nonzero(
                        puzzle[max(0, x - 1) : x + 2, max(0, y - 1) : y + 2]
                        == b"#"
                    )
                    >= 3
                ):
                    nd[x, y] = b"#"
            elif puzzle[x, y] == b"#":
                if (
                    np.count_nonzero(
                        puzzle[max(0, x - 1) : x + 2, max(0, y - 1) : y + 2]
                        == b"#"
                    )
                    < 2
                    or np.count_nonzero(
                        puzzle[max(0, x - 1) : x + 2, max(0, y - 1) : y + 2]
                        == b"|"
                    )
                    == 0
                ):
                    nd[x, y] = b"."
    puzzle = nd
    score = np.count_nonzero(puzzle == b"#") * np.count_nonzero(puzzle == b"|")
    if i == 9:
        print(
            f"Total resource value of the lumber collection area be after 10 minutes: {score}"
        )
    if score in scores:
        if len(scores[score]) > 3:
            if (
                i % (i - sorted(scores[score])[-1])
                == 1_000_000_000 % (i - sorted(scores[score])[-1]) - 1
            ):
                print(
                    f"Total resource value of the lumber collection area be after 1000000000 minutes: {score}"
                )
                break
    scores[score].add(i)

