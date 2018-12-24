puzzle = int(open("input.txt", "r").readlines()[8].split()[1])

def register_0(number, is_part_1):
    seen = set()
    c = 0
    last_unique_c = -1

    while True:
        a = c | 65536
        c = number

        while True:
            c = (((c + (a & 255)) & 16777215) * 65899) & 16777215

            if 256 > a:
                if is_part_1:
                    return c
                else:
                    if c not in seen:
                        seen.add(c)
                        last_unique_c = c
                        break
                    else:
                        return last_unique_c
            else:
                a //= 256


print(f"Lowest non-negative integer value for register 0 (fewest instructions): {register_0(puzzle, True)}")
print(f"Lowest non-negative integer value for register 0 (most instructions): {register_0(puzzle, False)}")
