Point = tuple[int, int]


DIRECTIONS: list[Point] = list([(0, -1), (1, 0), (0, 1), (-1, 0)])
DIRECTIONS_LENGTH = len(DIRECTIONS)


def cycleDirection(index: int):
    return (index + 1) % DIRECTIONS_LENGTH


def readInputs() -> tuple[int, set[Point], Point]:
    with open("./inputs.txt") as f:
        grid = f.read().splitlines()

        size = len(grid)
        walls: set[Point] = set()
        pos: Point = (0, 0)

        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                if char == "^":
                    pos = x, y
                elif char == "#":
                    walls.add((x, y))
                

        return size, walls, pos


def outOfBound(size: int, point: Point) -> bool:
    x, y = point
    return y < 0 or y >= size or x < 0 or x >= size


def getNext(size: int, point: Point, dirIndex: int) -> Point | None:
    x, y = point
    dX, dY = DIRECTIONS[dirIndex]
    
    next = x + dX, y + dY

    return None if outOfBound(size, next) else next


def step(size: int, walls: set[Point], pos: Point, dirIndex: int) -> tuple[Point, int] | None:
    nextMove = getNext(size, pos, dirIndex)
    if not nextMove:
        return None

    if nextMove in walls:
        dirIndex = cycleDirection(dirIndex)
    else:
        pos = nextMove

    return pos, dirIndex


def run(size: int, walls: set[Point], pos: Point, dirIndex: int = 0) -> tuple[set[tuple[Point, int]], bool]:
    moves: set[tuple[Point, int]] = set()
    isRepeating = False
    while not outOfBound(size, pos):
        moves.add((pos, dirIndex))

        nextStep = step(size, walls, pos, dirIndex)
        if not nextStep:
            break

        if nextStep in moves:
            isRepeating = True
            break

        pos, dirIndex = nextStep
    
    return moves, isRepeating


def drawGrid(size: int, walls: set[Point], start: Point, extra: Point | None = None, moves: set[Point] | None = None):
    for y in range(size):
        builder = ""
        for x in range(size):
            if (x, y) == start:
                builder += "@"
            elif (x, y) == extra:
                builder += "O"
            elif moves and (x, y) in moves:
                builder += "$"
            else:
                builder += "#" if (x, y) in walls else "."
        print(builder)
    print()


def main():
    size, walls, start = readInputs()
    moves, _ = run(size, walls, start)
    print(f"part1: {len(set([move for move, _ in moves]))}")

    obstacles: set[Point] = set()
    for movePos, moveDir in moves:
        nextMove = getNext(size, movePos, moveDir)
        if not nextMove or nextMove in walls or nextMove == start:
            continue

        walls.add(nextMove)
        _, repeating = run(size, walls, start)
        if repeating:
            obstacles.add(nextMove)
        walls.remove(nextMove)

    print(f"part2: {len(obstacles)}")

if __name__ == "__main__":
    main()
