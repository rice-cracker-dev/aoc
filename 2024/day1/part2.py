from utils import readInput

def calculateSimilarityScore(inputs: list[int], value: int, cachedValues: dict[int, int]) -> int:
    cached = cachedValues.get(value)
    if cached is not None: return cached

    score = 0;
    for input in inputs:
        if input == value:
            score += value

    cachedValues[value] = score
    return score

def main():
    lInputs, rInputs = readInput()

    score = 0
    cached: dict[int, int] = dict()
    for input in lInputs:
        score += calculateSimilarityScore(rInputs, input, cached)

    print(score)

if __name__ == "__main__":
    main()
