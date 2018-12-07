import re
import numpy as np

with open("input.txt") as n:
    input = [line.strip() for line in n]

regex = r"Step ([A-Z]) must be finished before step ([A-Z]) can begin."
alph = [chr(i) for i in range(ord("A"), ord("Z") + 1)]


def split_input(instructions: str):
    first, second = re.match(regex, instructions).groups()
    return (first, second)


def ordered_steps(input):
    lists = [split_input(line) for line in input]
    steps = {step for lst in lists for step in lst}
    before_step = {step: set() for step in steps}
    for first, second in lists:
        before_step[second].add(first)
    return before_step


# Solution for first puzzle


def find_order(input):
    requirements = instructions = ordered_steps(input)
    order = []

    while instructions:
        ordered = [step for step, reqs in requirements.items() if not reqs]
        next_inst = min(ordered)
        order.append(next_inst)

        for reqs in instructions.values():
            if next_inst in reqs:
                reqs.remove(next_inst)

        del requirements[next_inst]

    return "".join(order)


assert (
    find_order(
        [
            "Step C must be finished before step A can begin.",
            "Step C must be finished before step F can begin.",
            "Step A must be finished before step B can begin.",
            "Step A must be finished before step D can begin.",
            "Step B must be finished before step E can begin.",
            "Step D must be finished before step E can begin.",
            "Step F must be finished before step E can begin.",
        ]
    )
    == "CABDFE"
)

print(f"Order the steps should be completed: {find_order(input)}")

# Solution for second puzzle


def time_taken(input, workers: int = 5, base: int = 60):
    instructions = ordered_steps(input)
    working = [None] * workers
    time_left = np.zeros(workers)
    has = set()

    for i in range(10000):
        for j in range(workers):
            if working[j] is not None:
                time_left[j] -= 1
                if time_left[j] == 0:
                    has.add(working[j])
                    working[j] = None

        if set(alph) == has:
            return i
            break

        for j in range(workers):
            if working[j] is not None:
                continue

            for k in alph:
                if (
                    k not in has
                    and k not in working
                    and instructions[k] & has == instructions[k]
                ):
                    working[j] = k
                    time_left[j] = base + ord(k) - ord("A") + 1
                    break


print(f"Time taken: {time_taken(input)}")
