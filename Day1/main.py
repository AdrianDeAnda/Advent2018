import itertools

# Solution for first puzzle

with open("input.txt") as n:
    input = [int(line.strip()) for line in n]


def get_frequency(numbers):
    return sum(numbers)


assert get_frequency([+1, +1, +1]) == 3
assert get_frequency([+1, +1, -2]) == 0
assert get_frequency([-1, -2, -3]) == -6

print(f"Resulting frequency: {get_frequency(input)}")

# Solution for second puzzle


def repeated_frequency(numbers, value: int = 0):
    seen = set()

    for n in itertools.cycle(int(n) for n in numbers):
        value += n
        if value in seen:
            return value
            break
        seen.add(value)


assert repeated_frequency([+3, +3, +4, -2, -4]) == 10
assert repeated_frequency([-6, +3, +8, +5, -6]) == 5
assert repeated_frequency([+7, +7, -2, -7, -4]) == 14

print(f"First frequency reached twice: {repeated_frequency(input)}")
