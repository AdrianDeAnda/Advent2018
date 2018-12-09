# Solution for first puzzle
def marble_game(
    players: int, points: int, crnt_plyr: int = 0, nxt_plyr: int = 0
):
    scores = [0 for _ in range(players)]
    marbles = [0]

    for marble in range(1, points + 1):
        if marble % 23 == 0:
            scores[nxt_plyr] += marble
            crnt_plyr = (crnt_plyr - 7) % len(marbles)
            scores[nxt_plyr] += marbles[crnt_plyr]
            marbles = marbles[:crnt_plyr] + marbles[crnt_plyr + 1:]
            crnt_plyr = crnt_plyr % len(marbles)
        else:
            insert_after = (crnt_plyr + 1) % len(marbles)
            crnt_plyr = insert_after + 1
            if insert_after == len(marbles) - 1:
                marbles.append(marble)
            else:
                marbles = (
                    marbles[: insert_after + 1]
                    + [marble]
                    + marbles[insert_after + 1 :]
                )

        nxt_plyr = (nxt_plyr + 1) % players

    return max(scores)


assert marble_game(9, 25) == 32
assert marble_game(10, 1618) == 8317
assert marble_game(13, 7999) == 146373
assert marble_game(17, 1104) == 2764
assert marble_game(21, 6111) == 54718
assert marble_game(30, 5807) == 37305

print(f"Score: {marble_game(427, 70723)}")
