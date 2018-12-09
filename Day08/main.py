with open("input.txt") as f:
    input = f.readline()


def get_metadata(list):
    return [int(x) for x in input.split()]


# Solution for first and second puzzle


def parse(data, totals: int = 0):
    children, metas = data[:2]
    data = data[2:]
    scores = []

    for i in range(children):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(
                scores[k - 1]
                for k in data[:metas]
                if k > 0 and k <= len(scores)
            ),
            data[metas:],
        )


data = get_metadata(input)
total, value, remaining = parse(data)

print(f"Sum of metadata entries: {total}")
print(f"Root node value: {value}")

