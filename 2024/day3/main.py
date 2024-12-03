from re import search


mulRegex = "^mul\\([0-9]*,[0-9]*\\)"
doRegex = "^do\\(\\)"
dontRegex = "^don't\\(\\)"


def readInputs() -> str:
    with open("./inputs.txt", "r") as f: return f.read()


def parseMul(s: str) -> int:
    numbers = [int(x) for x in s[len("mul("):-len(")")].split(',')]
    return numbers[0] * numbers[1]


def main():
    corrupted = readInputs()
    total = 0
    totalDo = 0

    do = True
    for i in range(len(corrupted)):
        s = corrupted[i:]

        if search(doRegex, s):
            do = True
            continue

        if search(dontRegex, s):
            do = False
            continue

        matches = search(mulRegex, s)

        if not matches: continue

        parsed = parseMul(matches.group(0))
        total += parsed
        if do: totalDo += parsed
        
    print(f"part1: {total}")
    print(f"part2: {totalDo}")


if __name__ == "__main__":
    main()

