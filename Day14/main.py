def get_digits(value: int = 0):
    return [int(digit) for digit in str(value)]


def recipe_score(value: int = 0):
    digits = get_digits(value)
    scores = [3, 7]
    elf1, elf2 = 0, 1
    while (len(scores) < value + 10):
        total = scores[elf1] + scores[elf2]
        scores.extend(divmod(total, 10) if total >= 10 else (total,))
        elf1 = (elf1 + 1 + scores[elf1]) % len(scores)
        elf2 = (elf2 + 1 + scores[elf2]) % len(scores)
    return(''.join(str(score) for score in scores[value:value+10]))


print(recipe_score(793061))

# Solution for second puzzle


def left_recipes(value: int = 0):
    digits = get_digits(value)
    scores = [3, 7]
    elf1, elf2 = 0, 1
    while (scores[-len(digits):] != digits and scores[-len(digits)-1:-1] != digits):
        total = scores[elf1] + scores[elf2]
        scores.extend(divmod(total, 10) if total >= 10 else (total,))
        elf1 = (elf1 + 1 + scores[elf1]) % len(scores)
        elf2 = (elf2 + 1 + scores[elf2]) % len(scores)
    return len(scores) - len(digits) - (0 if scores[-len(digits):] == digits else 1)


print(left_recipes(793061))
