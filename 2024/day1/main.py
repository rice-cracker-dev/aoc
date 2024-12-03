def readInput() -> tuple[list[int], list[int]]:
    with open("./inputs.txt") as f:
        left: list[int] = []
        right: list[int] = []

        for line in f:
            split = [int(x) for x in str.split(line, "   ")]
            left.append(split[0])
            right.append(split[1])

        return left, right


def calculateSimilarityScore(inputs: list[int], value: int) -> int:
    score = 0;
    for input in inputs:
        if input == value:
            score += value

    return score

    
def main():
    distance, score = 0, 0
    lInput, rInput = readInput();
    lInput.sort()
    rInput.sort()

    for left, right in zip(lInput, rInput):
        distance += abs(left - right)
        score += calculateSimilarityScore(rInput, left)

    print(f"part1: {distance}")
    print(f"part2: {score}")

if __name__ == "__main__":
    main()
