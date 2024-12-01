def readInput() -> tuple[list[int], list[int]]:
    left: list[int] = list()
    right: list[int] = list()

    with open('./inputs.txt') as file:
        for line in file:
            split = str.split(line, '   ')
            left.append(int(split[0]))
            right.append(int(split[1]))
    
    return left, right

