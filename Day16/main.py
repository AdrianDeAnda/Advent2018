def parse_input(fname):
    s = open(fname).read()
    if s and s[-1] == "\n":
        s = s[:-1]
    return s.splitlines()


puzzle = parse_input("input.txt")


def list_map(f, s):
    return list(map(f, s))


def addr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + result[b]
    return result


def addi(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + b
    return result


def mulr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * result[b]
    return result


def muli(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * b
    return result


def banr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & result[b]
    return result


def bani(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & b
    return result


def borr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | result[b]
    return result


def bori(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | b
    return result


def setr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a]
    return result


def seti(registers, a, b, c):
    result = registers[::]
    result[c] = a
    return result


def gtir(registers, a, b, c):
    result = registers[::]
    result[c] = bool(a > result[b])
    return result


def gtri(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] > b)
    return result


def gtrr(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] > result[b])
    return result


def eqir(registers, a, b, c):
    result = registers[::]
    result[c] = bool(a == result[b])
    return result


def eqri(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] == b)
    return result


def eqrr(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] == result[b])
    return result


OPERATIONS = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr,
]


def possible_operations(instruction, before, after):
    result = set()
    for operation in OPERATIONS:
        op_result = operation(before, *instruction[1:])
        if op_result == after:
            result.add(operation)
    return result


def opcodes(lines):
    i = 0
    experiments = []
    while lines[i].strip():
        before, instruction, after = lines[i : i + 3]
        i += 4
        experiments.append(
            (
                list_map(int, instruction.split(" ")),
                eval(before[8:]),
                eval(after[8:]),
            )
        )
    return len(
        [
            experiment
            for experiment in experiments
            if len(possible_operations(*experiment)) >= 3
        ]
    )


def register_0(lines):
    i = 0
    experiments = []
    while lines[i].strip():
        before, instruction, after = lines[i : i + 3]
        i += 4
        experiments.append(
            (
                list_map(int, instruction.split(" ")),
                eval(before[8:]),
                eval(after[8:]),
            )
        )

    operations = {opcode: set(OPERATIONS) for opcode in range(16)}
    for experiment in experiments:
        opcode = experiment[0][0]
        operations[opcode].intersection_update(possible_operations(*experiment))

    while True:
        unique_ops = {}
        for op, ops in operations.items():
            if len(ops) == 1:
                unique_ops[op] = ops
        for op_, ops_ in unique_ops.items():
            for op, ops in operations.items():
                if op != op_:
                    ops.difference_update(ops_)
        if len(unique_ops) == len(operations):
            break

    for op in operations:
        operations[op] = operations[op].pop()
    registers = [0, 0, 0, 0]
    for line in lines[i:]:
        if not line.strip():
            continue
        opcode, a, b, c = list_map(int, line.split(" "))
        registers = operations[opcode](registers, a, b, c)
    return registers[0]


print(
    f"Samples in the puzzle input that behave like three or more opcodes: {opcodes(puzzle)}"
)
print(f"Value contained in register 0: {register_0(puzzle)}")
