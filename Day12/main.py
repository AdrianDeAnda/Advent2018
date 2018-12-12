import re

from typing import Set, Tuple

with open("input_test.txt") as f:
    test_input = f.read()

with open("input.txt") as f:
    input = f.read()

State = Set[int]

Rule = Tuple[int, int, int, int, int]
Rules = Set[Rule]

regex_state = "initial state: (.*)"
regex_rules = "(.....) => (.)"


def get_state_and_rules(raw: str) -> Tuple[State, Rules]:
    lines = raw.split("\n")
    initial_state = re.match(regex_state, lines[0]).groups()[0]
    state = {i for i, plant in enumerate(initial_state) if plant == "#"}
    rules = set()
    for line in lines[2:]:
        pattern, plant = re.match(regex_rules, line).groups()
        if plant == "#":
            key = tuple([c == "#" for c in pattern])
            rules.add(key)
    return state, rules


def instructions(state, rules):
    next_state = set()
    lo = min(state) - 2
    hi = max(state) + 2
    for plant in range(lo, hi + 1):
        key = tuple(
            [
                other in state
                for other in [plant - 2, plant - 1, plant, plant + 1, plant + 2]
            ]
        )
        if key in rules:
            next_state.add(plant)
    return next_state


# Solution for first puzzle


def count_plants(raw: str, generations: int = 20):
    state, rules = get_state_and_rules(raw)
    for _ in range(generations):
        state = instructions(state, rules)
    return sum(state)


assert count_plants(test_input) == 325

print(
    f"Sum of the numbers of all pots which contain a plant: {count_plants(input)}"
)

# Solution for second puzzle


def plants_pattern(raw: str, generations: int = 200):
    lpn1, lpn2, last_plants_number, current_gen = 0, 0, 0, 0
    state, rules = get_state_and_rules(raw)

    for i in range(generations):
        state = instructions(state, rules)
        plants_number = sum(state)

        if (plants_number - last_plants_number) == lpn1 and lpn1 == lpn2:
            current_gen = i + 1
            break

        if (plants_number - last_plants_number) == lpn1:
            lpn2 = plants_number - last_plants_number

        lpn1 = plants_number - last_plants_number
        last_plants_number = plants_number

    return sum(state) + ((50_000_000_000 - current_gen) * lpn2)


print(
    f"Sum of the numbers of all pots which contain a plant after 50 Billion generations: {plants_pattern(input)}"
)
