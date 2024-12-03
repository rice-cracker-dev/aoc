def readInputs() -> str:
    with open("./inputs.txt", "r") as f:
        return f.read()


# return number, length
def scanForNumber(s: str, index: int, builder: str = "") -> tuple[int | None, int]:
    if index >= len(s): return None, 0

    if not s[index].isnumeric():
        length = len(builder)
        if length > 0: return int(builder), length
        
        return None, 0

    return scanForNumber(s, index + 1, builder + s[index])


# parsing madness
def scanForMul(s: str, i: int) -> tuple[int | None, int | None]:
    if len(s) - i < len("mul("): return None, None

    keyword = s[i:i + len("mul")]
    functionStart = s[i + len("mul")]

    if keyword != "mul": return None, None
    if functionStart != "(": return None, None

    aIndex = i + len("mul") + 1
    a, aL = scanForNumber(s, aIndex)

    if not a: return None, None
    if s[aIndex + aL] != ",": return None, None

    bIndex = aIndex + aL + 1
    b, bL = scanForNumber(s, bIndex)

    if not b: return None, None
    if s[bIndex + bL] != ")": return None, None

    return a, b


def scanForDo(s: str, i: int) -> bool:
    keyword = s[i:i + len("do()")]
    return keyword == "do()"


def scanForDont(s: str, i: int) -> bool:
    keyword = s[i:i + len("don't()")]
    return keyword == "don't()"


def main():
    corrupted = readInputs()
    corruptedLength = len(corrupted)
    scannedSum = 0
    scannedDoSum = 0

    # i should've learnt regex
    do = True
    for i in range(corruptedLength):
        if corruptedLength - i >= len("do()") and scanForDo(corrupted, i):
            do = True
            continue

        if corruptedLength - 1 >= len("don't()") and scanForDont(corrupted, i):
            do = False
            continue

        a, b = scanForMul(corrupted, i);

        if a and b:
            mul = a * b
            scannedSum += mul
            if do: scannedDoSum += mul
            
            print(f"found: {a} * {b}")

    print(f"part1: {scannedSum}")
    print(f"part2: {scannedDoSum}")

if __name__ == "__main__":
    main()
