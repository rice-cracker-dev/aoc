def readInputs() -> list[list[int]]:
    with open("./inputs.txt", "r") as f:
        return [[int(x) for x in str.split(line, " ")] for line in f]


def isListSafe(l: list[int], ignoreIdx: int = -1) -> bool:
    desc = False
    asc = False
    prev = None
    for i, v in enumerate(l):
        if ignoreIdx == i: continue
        if prev is None:
            prev = v
            continue

        if prev < v: asc = True
        if prev > v: desc = True

        distance = abs(prev - v)
        if (distance < 1 or distance > 3) or (desc and asc): return False

        prev = v

    return True
        


def main():
    dataset = readInputs()
    safeCount, dampedCount = 0, 0

    for data in dataset:
        # part1
        if isListSafe(data): safeCount += 1
        
        # part2
        if any(isListSafe(data, i) for i in range(len(data))): dampedCount += 1

    print(f"part1: {safeCount}")
    print(f"part2: {dampedCount}")

if __name__ == "__main__":
    main()
