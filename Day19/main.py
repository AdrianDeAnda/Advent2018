from re import findall

puzzle = [line.strip() for line in open("input.txt", "r").readlines()]


def addr(registers, a, b, c):
    registers[c] = registers[a] + registers[b]
    return registers


def addi(registers, a, b, c):
    registers[c] = registers[a] + b
    return registers


def mulr(registers, a, b, c):
    registers[c] = registers[a] * registers[b]
    return registers


def muli(registers, a, b, c):
    registers[c] = registers[a] * b
    return registers


def banr(registers, a, b, c):
    registers[c] = registers[a] & registers[b]
    return registers


def bani(registers, a, b, c):
    registers[c] = registers[a] & b
    return registers


def borr(registers, a, b, c):
    registers[c] = registers[a] | registers[b]
    return registers


def bori(registers, a, b, c):
    registers[c] = registers[a] | b
    return registers


def setr(registers, a, b, c):
    registers[c] = int(registers[a])
    return registers


def seti(registers, a, b, c):
    registers[c] = int(a)
    return registers


def gtir(registers, a, b, c):
    if a > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers


def gtri(registers, a, b, c):
    if registers[a] > b:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers


def gtrr(registers, a, b, c):
    if registers[a] > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers


def eqir(registers, a, b, c):
    if a == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers


def eqri(registers, a, b, c):
    if registers[a] == b:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers


def eqrr(registers, a, b, c):
    if registers[a] == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers


def register_0(lines, is_part_2=False):
    bound = int(lines[0].split(" ")[1])
    registers = [0] * 6
    ip = 0
    instructions = []

    for line in lines[1:]:
        nums = list(map(int, findall(r"-?\d+", line)))
        command = line.split(" ")[0]
        instructions.append((command, nums))

    if is_part_2:
        registers[0] = 1

    while True:
        try:
            command, (a, b, c) = instructions[ip]
            registers[bound] = ip
            registers = globals()[command](
                registers, a, b, c
            )  # I know, I know...
            ip = registers[bound] + 1
            if ip == 1:
                n = registers[-3]
                return sum(d for d in range(1, n + 1) if n % d == 0)
        except IndexError:
            return registers[0]



print(f"Value is left in register 0: {register_0(puzzle)}")
print(f"Value is left in register 0 started with value 1: {register_0(puzzle, True)}")
