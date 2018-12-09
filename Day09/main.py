from collections import deque

# Solution for first and second puzzle


def marble_game(players: int, points: int, crnt: int = 0, nxt: int = 0):
    scores = [0 for _ in range(players)]
    marbles = deque([0])

    def left(n: int = 1):
        for _ in range(n):
            value = marbles.pop()
            marbles.appendleft(value)

    def right(n: int = 1):
        for _ in range(n):
            value = marbles.popleft()
            marbles.append(value)

    for marble in range(1, points + 1):
        if marble % 23 == 0:
            scores[nxt] += marble
            left(7)
            scores[nxt] += marbles.popleft()
        else:
            right(2)
            marbles.appendleft(marble)

        nxt = (nxt + 1) % players

    return max(scores)


assert marble_game(9, 25) == 32
assert marble_game(10, 1618) == 8317
assert marble_game(13, 7999) == 146_373
assert marble_game(17, 1104) == 2764
assert marble_game(21, 6111) == 54718
assert marble_game(30, 5807) == 37305

print(f"Score: {marble_game(427, 70723)}")
print(f"Score (points a 100 times bigger): {marble_game(427, 7072300)}")
