from enum import Enum
from itertools import product


Equation = tuple[int, list[int]]
Range = tuple[int, int]


class Operator(Enum):
    ADD = 1
    MULTIPLY = 2
    COMBINE = 3


def readInputs() -> list[Equation]:
    with open("./inputs.txt") as f:
        equations: list[Equation] = []

        for line in f:
            s = line.split(":")
            equations.append((int(s[0]), [int(x) for x in s[1].strip().split(" ")]))

        return equations


def verifyEquation(equation: Equation, mulList: set[tuple[Operator, ...]]) -> bool:
    equal, sequences = equation

    for mulSet in mulList:
        acc = 0
        for i, v in enumerate(sequences):
            if mulSet[i] == Operator.MULTIPLY:
                acc *= v
            elif mulSet[i] == Operator.ADD:
                acc += v
            elif mulSet[i] == Operator.COMBINE:
                acc = int("%i%i" % (acc, v))
        
        if acc == equal:
            return True

    return False


def main():
    equations = readInputs()
    part1Operators = [Operator.ADD, Operator.MULTIPLY]
    part2Operators = part1Operators + [Operator.COMBINE]
    part1 = 0
    part2 = 0
    for index, (equal, sequences) in enumerate(equations):
        if verifyEquation((equal, sequences), set(product(part1Operators, repeat = len(sequences)))):
            part1 += equal
        if verifyEquation((equal, sequences), set(product(part2Operators, repeat = len(sequences)))):
            part2 += equal
        print(f"{index + 1} / {len(equations)}")

    print(f"part1: {part1}")
    print(f"part2: {part2}")

if __name__ == "__main__":
    main()
